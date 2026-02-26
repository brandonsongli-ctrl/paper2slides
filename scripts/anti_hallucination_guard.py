#!/usr/bin/env python3
"""Instant anti-hallucination checks for paper2slides outputs."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable


CLAIM_KEYWORDS = {
    "find",
    "finding",
    "show",
    "shows",
    "prove",
    "proves",
    "estimate",
    "estimated",
    "effect",
    "causal",
    "increase",
    "increases",
    "decrease",
    "decreases",
    "robust",
    "significant",
    "welfare",
    "equilibrium",
}


@dataclass
class EquationCheck:
    equation_preview: str
    best_score: float
    best_match_preview: str
    status: str


@dataclass
class ClaimCheck:
    claim: str
    best_score: float
    best_match_preview: str
    status: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify slide claims/equations/citations against source paper."
    )
    parser.add_argument("--source", required=True, help="Path to source paper (.tex/.pdf/.md/.txt).")
    parser.add_argument("--slides", required=True, help="Path to generated slides (.tex/.md/.txt).")
    parser.add_argument("--bib", help="Optional bibliography file (.bib) for citation-key checks.")
    parser.add_argument(
        "--report",
        default="anti_hallucination_report.md",
        help="Markdown report output path (default: anti_hallucination_report.md).",
    )
    parser.add_argument(
        "--json",
        default="anti_hallucination_report.json",
        help="JSON report output path (default: anti_hallucination_report.json).",
    )
    parser.add_argument(
        "--fail-on-warn",
        action="store_true",
        help="Return non-zero exit code when warnings exist.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() == ".pdf":
        if shutil.which("pdftotext") is None:
            raise RuntimeError("pdftotext is required to parse PDFs but is not installed.")
        result = subprocess.run(
            ["pdftotext", str(path), "-"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(f"pdftotext failed for {path}: {result.stderr.strip()}")
        return result.stdout

    return path.read_text(encoding="utf-8", errors="ignore")


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def preview(text: str, width: int = 120) -> str:
    one_line = normalize_whitespace(text)
    if len(one_line) <= width:
        return one_line
    return one_line[: width - 3] + "..."


def normalize_equation(eq: str) -> str:
    cleaned = re.sub(r"%.*", " ", eq)
    cleaned = re.sub(r"\\(label|tag)\{[^}]*\}", " ", cleaned)
    cleaned = cleaned.replace("\\left", " ").replace("\\right", " ")
    cleaned = cleaned.replace("\\!", " ").replace("\\,", " ").replace("\\;", " ")
    cleaned = cleaned.replace("\\:", " ").replace("\\quad", " ").replace("\\qquad", " ")
    cleaned = cleaned.replace("\\\\", " ")
    cleaned = re.sub(r"\\text\{[^}]*\}", " ", cleaned)
    cleaned = re.sub(r"\\operatorname\{([^}]*)\}", r"\1", cleaned)
    cleaned = re.sub(r"\\[a-zA-Z]+\*?", " ", cleaned)
    cleaned = cleaned.replace("{", " ").replace("}", " ")
    cleaned = cleaned.replace("&", " ")
    cleaned = re.sub(r"\s+", "", cleaned.lower())
    cleaned = re.sub(r"[^a-z0-9+\-*/=()_<>\[\].,^|:]", "", cleaned)
    return cleaned


def extract_equations(text: str) -> list[str]:
    patterns = [
        r"\\begin\{(?:equation\*?|align\*?|multline\*?|gather\*?)\}(.*?)\\end\{(?:equation\*?|align\*?|multline\*?|gather\*?)\}",
        r"\$\$(.*?)\$\$",
        r"\\\[(.*?)\\\]",
    ]
    equations: list[str] = []
    for pattern in patterns:
        equations.extend(re.findall(pattern, text, flags=re.DOTALL))

    inline = re.findall(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", text, flags=re.DOTALL)
    for eq in inline:
        eq_compact = normalize_whitespace(eq)
        if len(eq_compact) < 18:
            continue
        if not any(token in eq_compact for token in ["=", "\\", "_", "^", "\\sum", "\\max", "\\min"]):
            continue
        equations.append(eq)

    deduped: list[str] = []
    seen: set[str] = set()
    for eq in equations:
        key = normalize_equation(eq)
        if len(key) < 10:
            continue
        if key in seen:
            continue
        seen.add(key)
        deduped.append(eq)
    return deduped


def similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def best_match(target: str, candidates: Iterable[str]) -> tuple[float, str]:
    best_score = 0.0
    best_candidate = ""
    for candidate in candidates:
        score = similarity(target, candidate)
        if score > best_score:
            best_score = score
            best_candidate = candidate
    return best_score, best_candidate


def check_equations(source_text: str, slide_text: str) -> tuple[list[EquationCheck], int, int]:
    source_equations = extract_equations(source_text)
    slide_equations = extract_equations(slide_text)
    source_norm = [normalize_equation(eq) for eq in source_equations]

    results: list[EquationCheck] = []
    warn_count = 0
    fail_count = 0

    for eq in slide_equations:
        eq_norm = normalize_equation(eq)
        score, match = best_match(eq_norm, source_norm)
        if score >= 0.90:
            status = "PASS"
        elif score >= 0.75:
            status = "WARN"
            warn_count += 1
        else:
            status = "FAIL"
            fail_count += 1
        results.append(
            EquationCheck(
                equation_preview=preview(eq),
                best_score=round(score, 3),
                best_match_preview=preview(match) if match else "",
                status=status,
            )
        )

    return results, warn_count, fail_count


def extract_numbers(text: str) -> list[str]:
    tokens = re.findall(
        r"(?<![A-Za-z\\])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?",
        text,
    )
    cleaned: list[str] = []
    seen: set[str] = set()
    for token in tokens:
        raw = token.strip()
        if not raw:
            continue
        no_pct = raw[:-1] if raw.endswith("%") else raw
        no_comma = no_pct.replace(",", "")
        if re.fullmatch(r"-?\d+", no_comma):
            number = int(no_comma)
            if 0 <= number <= 12:
                continue
        if raw in seen:
            continue
        seen.add(raw)
        cleaned.append(raw)
    return cleaned


def check_numbers(source_text: str, slide_text: str) -> list[str]:
    source_norm = " " + normalize_whitespace(source_text).replace(",", "") + " "
    mismatches: list[str] = []
    for token in extract_numbers(slide_text):
        no_pct = token[:-1] if token.endswith("%") else token
        normalized = no_pct.replace(",", "")
        if f" {normalized} " not in source_norm and normalized not in source_norm:
            mismatches.append(token)
    return mismatches


def extract_cite_keys(text: str) -> set[str]:
    pattern = r"\\cite[a-zA-Z*]*\s*(?:\[[^\]]*\])?\s*(?:\[[^\]]*\])?\{([^}]*)\}"
    keys: set[str] = set()
    for match in re.findall(pattern, text):
        for key in match.split(","):
            cleaned = key.strip()
            if cleaned:
                keys.add(cleaned)
    return keys


def extract_bib_keys(bib_text: str) -> set[str]:
    return {key.strip() for key in re.findall(r"@\w+\{([^,]+),", bib_text)}


def split_sentences(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text)
    raw = re.split(r"(?<=[.!?])\s+|\n+", normalized)
    sentences: list[str] = []
    for sentence in raw:
        compact = sentence.strip()
        if len(compact) < 24:
            continue
        sentences.append(compact)
    return sentences


def normalize_sentence(text: str) -> str:
    lowered = text.lower()
    lowered = re.sub(r"\\[a-zA-Z]+\*?(\{[^}]*\})?", " ", lowered)
    lowered = re.sub(r"[^a-z0-9\s]", " ", lowered)
    lowered = re.sub(r"\s+", " ", lowered)
    return lowered.strip()


def extract_claim_sentences(text: str) -> list[str]:
    candidates: list[str] = []
    for sentence in split_sentences(text):
        normalized = normalize_sentence(sentence)
        if len(normalized) < 20:
            continue
        words = set(normalized.split())
        if words.intersection(CLAIM_KEYWORDS):
            candidates.append(sentence)
    return candidates


def check_claims(source_text: str, slide_text: str) -> list[ClaimCheck]:
    source_sentences = [normalize_sentence(s) for s in split_sentences(source_text)]
    claim_sentences = extract_claim_sentences(slide_text)

    checks: list[ClaimCheck] = []
    for claim in claim_sentences:
        claim_norm = normalize_sentence(claim)
        score, match = best_match(claim_norm, source_sentences)
        if score >= 0.62:
            status = "PASS"
        elif score >= 0.45:
            status = "WARN"
        else:
            status = "WARN"
        checks.append(
            ClaimCheck(
                claim=preview(claim),
                best_score=round(score, 3),
                best_match_preview=preview(match) if match else "",
                status=status,
            )
        )
    return checks


def aggregate_status(eq_fail: int, eq_warn: int, missing_cites: set[str], number_mismatches: list[str], claim_warn: int) -> str:
    if eq_fail > 0 or missing_cites:
        return "FAIL"
    if eq_warn > 0 or number_mismatches or claim_warn > 0:
        return "WARN"
    return "PASS"


def to_markdown(
    status: str,
    source_path: Path,
    slides_path: Path,
    equation_checks: list[EquationCheck],
    missing_cites: set[str],
    number_mismatches: list[str],
    claim_checks: list[ClaimCheck],
) -> str:
    eq_fail = sum(1 for item in equation_checks if item.status == "FAIL")
    eq_warn = sum(1 for item in equation_checks if item.status == "WARN")
    claim_warn = sum(1 for item in claim_checks if item.status != "PASS")

    lines = [
        "# Anti-Hallucination Report",
        "",
        f"- Generated (UTC): {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Source: `{source_path}`",
        f"- Slides: `{slides_path}`",
        f"- Overall status: **{status}**",
        "",
        "## Summary",
        "",
        f"- Equations checked: {len(equation_checks)}",
        f"- Equation FAIL: {eq_fail}",
        f"- Equation WARN: {eq_warn}",
        f"- Missing citation keys: {len(missing_cites)}",
        f"- Numeric mismatches: {len(number_mismatches)}",
        f"- Claim mismatches (WARN): {claim_warn}",
        "",
    ]

    if equation_checks:
        lines.extend(
            [
                "## Equation Alignment",
                "",
                "| Status | Score | Slide Equation (preview) | Best Source Match (normalized preview) |",
                "|---|---:|---|---|",
            ]
        )
        for item in equation_checks[:50]:
            lines.append(
                f"| {item.status} | {item.best_score:.3f} | {item.equation_preview} | {item.best_match_preview or '-'} |"
            )
        lines.append("")

    lines.extend(["## Citation Check", ""])
    if missing_cites:
        lines.append("Missing keys found in slides but not in source/bib:")
        for key in sorted(missing_cites):
            lines.append(f"- `{key}`")
    else:
        lines.append("- No missing citation keys detected.")
    lines.append("")

    lines.extend(["## Numeric Claim Check", ""])
    if number_mismatches:
        lines.append("Numbers in slides not found in source text (manual review required):")
        for token in number_mismatches[:80]:
            lines.append(f"- `{token}`")
    else:
        lines.append("- No numeric mismatches detected.")
    lines.append("")

    lines.extend(["## Textual Claim Check", ""])
    if claim_checks:
        lines.append("| Status | Score | Slide Claim (preview) | Best Source Match (normalized preview) |")
        lines.append("|---|---:|---|---|")
        for item in claim_checks[:40]:
            lines.append(
                f"| {item.status} | {item.best_score:.3f} | {item.claim} | {item.best_match_preview or '-'} |"
            )
    else:
        lines.append("- No claim-like sentences detected in slides.")
    lines.append("")

    lines.extend(
        [
            "## Remediation",
            "",
            "- For `FAIL` equations: replace with exact source equation or add explicit simplification mapping.",
            "- For missing citations: align slide citation keys with paper/bib entries.",
            "- For numeric mismatches: re-check table/figure values and units.",
            "- For claim warnings: trace each sentence to paper text and rewrite if unsupported.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    source_path = Path(args.source).expanduser().resolve()
    slides_path = Path(args.slides).expanduser().resolve()
    report_path = Path(args.report).expanduser().resolve()
    json_path = Path(args.json).expanduser().resolve()
    bib_path = Path(args.bib).expanduser().resolve() if args.bib else None

    try:
        source_text = read_text(source_path)
        slide_text = read_text(slides_path)
    except Exception as exc:  # noqa: BLE001
        print(f"[anti-hallucination] input error: {exc}", file=sys.stderr)
        return 1

    equation_checks, eq_warn, eq_fail = check_equations(source_text, slide_text)

    source_cites = extract_cite_keys(source_text)
    if bib_path:
        try:
            source_cites.update(extract_bib_keys(read_text(bib_path)))
        except Exception as exc:  # noqa: BLE001
            print(f"[anti-hallucination] bibliography read warning: {exc}", file=sys.stderr)
    slide_cites = extract_cite_keys(slide_text)
    missing_cites = slide_cites - source_cites

    number_mismatches = check_numbers(source_text, slide_text)
    claim_checks = check_claims(source_text, slide_text)
    claim_warn = sum(1 for item in claim_checks if item.status != "PASS")

    status = aggregate_status(eq_fail, eq_warn, missing_cites, number_mismatches, claim_warn)

    markdown = to_markdown(
        status=status,
        source_path=source_path,
        slides_path=slides_path,
        equation_checks=equation_checks,
        missing_cites=missing_cites,
        number_mismatches=number_mismatches,
        claim_checks=claim_checks,
    )
    report_path.write_text(markdown, encoding="utf-8")

    payload = {
        "status": status,
        "source": str(source_path),
        "slides": str(slides_path),
        "equations": [asdict(item) for item in equation_checks],
        "missing_citations": sorted(missing_cites),
        "number_mismatches": number_mismatches,
        "claim_checks": [asdict(item) for item in claim_checks],
        "summary": {
            "equation_fail": eq_fail,
            "equation_warn": eq_warn,
            "missing_citation_count": len(missing_cites),
            "number_mismatch_count": len(number_mismatches),
            "claim_warn_count": claim_warn,
        },
        "generated_utc": datetime.now(timezone.utc).isoformat(),
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[anti-hallucination] status={status}")
    print(f"[anti-hallucination] markdown_report={report_path}")
    print(f"[anti-hallucination] json_report={json_path}")

    if status == "FAIL":
        return 2
    if status == "WARN" and args.fail_on_warn:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
