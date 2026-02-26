# Instant Anti-Hallucination Module

Executable verifier for `paper2slides` outputs:

- Script: `scripts/anti_hallucination_guard.py`
- Purpose: detect unsupported equations, claims, citations, and numeric values before delivery.

## Quick Start

```bash
python3 scripts/anti_hallucination_guard.py \
  --source "paper.tex" \
  --slides "slides.tex" \
  --report "anti_hallucination_report.md"
```

With bibliography:

```bash
python3 scripts/anti_hallucination_guard.py \
  --source "paper.tex" \
  --slides "slides.tex" \
  --bib "refs.bib" \
  --report "anti_hallucination_report.md"
```

## Checks

### 1) Equation Alignment

- Extract equations from slides and source.
- Normalize LaTeX notation.
- Compute best similarity against source equations.

Thresholds:

- `PASS`: score >= 0.90
- `WARN`: 0.75 <= score < 0.90
- `FAIL`: score < 0.75

Interpretation:

- `WARN` usually means aggressive notation compression.
- `FAIL` usually means unsupported equation or severe mismatch.

### 2) Citation-Key Consistency

- Parse slide citation keys (e.g., `\cite{A,B}`).
- Match against source keys plus optional `.bib`.
- Missing keys are treated as high risk (`FAIL` overall).

### 3) Numeric Claim Traceability

- Extract numbers from slides.
- Check whether each number appears in source text.
- Missing values are marked for manual review (`WARN`).

### 4) Textual Claim Similarity

- Detect claim-like sentences (find/show/prove/effect/etc.).
- Compare sentence overlap against source sentences.
- Low-overlap claims are flagged as `WARN`.

## Output Files

- Markdown report (`--report`, default `anti_hallucination_report.md`)
- JSON report (`--json`, default `anti_hallucination_report.json`)

## Exit Codes

- `0`: overall `PASS`, or `WARN` without strict mode
- `2`: overall `FAIL`
- `3`: `WARN` with `--fail-on-warn`

Use strict mode in CI:

```bash
python3 scripts/anti_hallucination_guard.py \
  --source "paper.tex" \
  --slides "slides.tex" \
  --fail-on-warn
```

## Recommended Remediation Flow

1. Resolve all equation `FAIL` rows first.
2. Fix missing citation keys.
3. Re-check numeric mismatches against original tables/figures.
4. Rewrite unsupported claims as presenter interpretation or remove them.
5. Re-run guard until no `FAIL` remains.
