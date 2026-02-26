---
name: paper2slides
description: Convert economics papers (`.tex`, `.pdf`, `.md`) into presentation-ready Beamer or Marp decks with extraction, formula compression, and strict anti-hallucination verification. Use for seminar/conference/lightning talks, job market talks, discussant decks, and paper-to-slides workflows where equation/result fidelity matters.
allowed-tools: [Read, Write, Edit, Bash]
metadata:
  version: "2.1.0"
---

# Paper2Slides

Convert a research paper into a clean slide deck that compiles and remains traceable to the source text.

## Default Output Contract

If user does not specify:

- Talk profile: Conference (15-20 min)
- Slide count: 16-20
- Format: Beamer (`.tex`)
- Theme: `metropolis`
- Audience: field specialists
- Proof level: theorem statements + intuition, proofs in backup only
- Language: same as source paper (default English)

## Workflow

### Stage 0: Intake and Classification

1. Identify source file path (`.tex`, `.pdf`, `.md`).
2. Classify paper type: Theory / Empirical / Structural / Experimental / Survey.
3. Detect talk profile: Lightning / Conference / Seminar.
4. Build an extraction map with only high-value targets:
   - sections and subsections
   - theorem/proposition/lemma environments
   - equations
   - figures/tables

For `.pdf`, extract text first:

```bash
pdftotext "paper.pdf" "paper.txt"
```

### Stage 1: Extraction (Mandatory)

Use [references/extraction_protocol.md](references/extraction_protocol.md).

Always extract:

- one-sentence research question
- one headline result
- one core equation (model/specification/equilibrium)
- one key visual (or explicit placeholder)
- mechanism/intuition paragraph

Do not extract proofs into main slides.

### Stage 2: Formula Compression (Mandatory)

Use [references/compression_rules.md](references/compression_rules.md).

Rules:

- Keep definitions, objective/specification, and headline theorem statements.
- Compress derivations to first step + final result, or final result only.
- Drop routine algebra and appendix-only math from main deck.
- If notation is simplified, add mapping note: `Notation simplified from Eq. (X).`

### Stage 3: Slide Architecture

Use [references/slide_design_principles.md](references/slide_design_principles.md).

Minimum structure:

1. Title
2. Motivation + question
3. Preview of results
4. Model/Data setup
5. Main equation / identification
6. Main results
7. Mechanism / intuition
8. Robustness or extension
9. Conclusion
10. Backup slides

Design constraints:

- one core point per slide
- at most 2 equations on one slide
- no full regression table screenshots
- every slide title must be informative

### Stage 4: Deck Generation

Use [references/beamer_templates.md](references/beamer_templates.md) as skeleton.

Require:

- compilable preamble (`amsmath`, `amssymb`, `amsthm`, `graphicx`, `booktabs`)
- consistent notation across slides
- presenter notes for substantive slides (`\note{...}`)
- backup appendix for proofs and overflow robustness

### Stage 5: Technical Verification

If output is Beamer, compile-check:

```bash
pdflatex -interaction=nonstopmode slides.tex
```

Fix unresolved refs, missing assets, and syntax errors before delivery.

### Stage 6: Instant Anti-Hallucination Module (Mandatory)

Run the built-in guard:

```bash
python3 scripts/anti_hallucination_guard.py \
  --source "paper.tex" \
  --slides "slides.tex" \
  --report "anti_hallucination_report.md"
```

For citation-key verification, optionally pass bibliography:

```bash
python3 scripts/anti_hallucination_guard.py \
  --source "paper.tex" \
  --slides "slides.tex" \
  --bib "refs.bib" \
  --report "anti_hallucination_report.md"
```

Interpretation:

- `PASS`: no high-risk mismatch
- `WARN`: potential simplification mismatch; review manually
- `FAIL`: likely hallucination (equation/claim/citation unsupported)

Never deliver final slides with unresolved `FAIL`.

See [references/anti_hallucination_module.md](references/anti_hallucination_module.md) for thresholds and remediation.

## Delivery Checklist

- Output is a single `.tex` or `.md` slide source
- Slide count matches talk profile
- Main claims/equations trace to source paper
- Anti-hallucination report generated
- Beamer output compiles (if `.tex`)
- Backup section included

## Resource Map

- [references/extraction_protocol.md](references/extraction_protocol.md): extraction logic by paper type
- [references/compression_rules.md](references/compression_rules.md): compression rules and safety checks
- [references/slide_design_principles.md](references/slide_design_principles.md): visual and pacing standards
- [references/beamer_templates.md](references/beamer_templates.md): compilable deck templates
- [references/anti_hallucination_module.md](references/anti_hallucination_module.md): verification policy
- `scripts/anti_hallucination_guard.py`: executable guard and report generator
