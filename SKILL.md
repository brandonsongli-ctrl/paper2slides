---
name: paper2slides
description: "Converts academic economics papers (LaTeX or PDF) into presentation-ready Beamer slides or Markdown decks. Automatically extracts motivation, model, theorems, and intuition; compresses formulas; and generates a 15–25 minute seminar talk."
trigger_words: [paper2slides, paper to slides, make slides, beamer, presentation, seminar talk, 做幻灯片, 做PPT, 生成slides, 论文转PPT, job market talk, conference presentation]
allowed-tools: [Read, Write, Edit, Bash]
---

# Paper2Slides: Academic Paper → Presentation Converter

## Overview

Paper2Slides converts an economics working paper or published article into a structured, presentation-ready slide deck. It reads `.tex` or `.pdf` files, extracts the essential content, compresses mathematical notation, and outputs a complete LaTeX Beamer document that compiles directly to a polished academic presentation.

The skill is designed for the specific demands of economics seminars: 20-minute conference talks, 75-minute job market presentations, and 15-minute "lunch seminar" versions. It handles theory papers (with theorem environments and proofs), empirical papers (with regression tables and identification strategies), and structural papers (with model estimation and counterfactuals).

## When to Use This Skill

- Converting a working paper into a seminar or conference presentation
- Preparing a job market talk from a PhD dissertation chapter
- Creating a discussant's slide deck for a conference
- Building a reading-group presentation from someone else's paper
- Generating a "lightning talk" (5–10 minutes) version of a long paper

**Supported input:** `.tex` (LaTeX source), `.pdf`, `.md` (Markdown drafts)
**Output formats:** LaTeX Beamer (`.tex`), Marp Markdown (`.md`)

---

## Presentation Workflow

### Stage 0: Intake and Classification

1. **Identify the target file** and read it using `view_file` (for `.tex`/`.md`) or `pdftotext` (for `.pdf`).
2. **Classify the paper:**

| Dimension | Options |
|-----------|---------|
| **Paper Type** | Theory, Empirical, Structural, Experimental, Survey |
| **Subfield** | Micro Theory, Political Economy, IO, Labor, Public, Macro, Econometrics, Finance |
| **Talk Length** | Lightning (5–10 min / 8–12 slides), Conference (15–20 min / 15–22 slides), Seminar (40–75 min / 30–50 slides) |

3. **Extract the structural skeleton:**
   - For `.tex`: grep for `\section`, `\subsection`, `\begin{theorem}`, `\begin{lemma}`, `\begin{proposition}`, `\begin{assumption}`, `\begin{equation}`, `\begin{table}`, `\begin{figure}`.
   - For `.pdf`: extract full text and identify section headers, theorem-like statements, and key equations by formatting patterns.

### Stage 1: Content Extraction

Follow the extraction protocol in `references/extraction_protocol.md`. For each paper type, extract:

#### Theory Papers
1. **Research Question** — one sentence, plain language
2. **Model Primitives** — players, actions, types, timing, information structure
3. **Key Assumptions** — numbered, with economic interpretation
4. **Main Results** — theorems/propositions with statement (not proof)
5. **Intuition** — the "why" behind each result, separate from the math
6. **Numerical Example** — if present, extract the parametric example that illustrates the main result
7. **Comparative Statics** — how key outcomes change with parameters

#### Empirical Papers
1. **Research Question** — what causal effect is being estimated?
2. **Identification Strategy** — one-paragraph summary of the source of variation
3. **Data** — source, sample size, key variables, time period
4. **Main Specification** — the core regression equation
5. **Key Results** — 2–3 headline coefficients with magnitudes and significance
6. **Robustness** — summary of the most important robustness checks
7. **Key Figures/Tables** — which tables/figures to reproduce on slides

#### Structural Papers
1. **Model** — primitives, timing, equilibrium concept
2. **Identification** — what variation identifies structural parameters
3. **Estimation** — method (MLE, GMM, simulated moments)
4. **Counterfactuals** — key policy experiments and welfare results

### Stage 2: Formula Compression

Apply the compression rules in `references/compression_rules.md`:

- **Keep:** Definitions, the main optimization problem, key equilibrium conditions, the core estimating equation, main theorem statements
- **Compress:** Multi-line derivations → single key result; long summations → compact notation; repeated substitutions → final expression only
- **Drop:** All proof steps, intermediate algebra, routine FOCs that don't add insight, appendix material
- **Simplify notation:** If the paper uses unnecessarily complex notation (e.g., $\mathcal{F}_{\theta}^{(k)}$ when $F$ would suffice for the slide context), simplify with a footnote on the slide explaining the correspondence

### Stage 3: Slide Architecture

Build the presentation according to the slide design principles in `references/slide_design_principles.md`. The canonical structure depends on talk length:

#### Conference Talk (15–20 min, ~18 slides)

| Slide # | Content | Time |
|---------|---------|------|
| 1 | Title slide | 0:30 |
| 2 | Motivation: Why should the audience care? | 1:30 |
| 3 | Research question + preview of main result | 1:00 |
| 4 | Related literature (brief, positioning only) | 1:00 |
| 5 | Model setup / Data description | 2:00 |
| 6–7 | Key assumptions / Identification strategy | 2:00 |
| 8–9 | Main model/specification | 2:00 |
| 10–12 | Main results (1 slide per key result) | 3:00 |
| 13 | Intuition / Mechanism | 1:30 |
| 14–15 | Robustness / Extensions | 2:00 |
| 16 | Conclusion + implications | 1:00 |
| 17 | Future work (optional) | 0:30 |
| 18 | Thank you + contact | 0:00 |

#### Seminar Talk (40–75 min, ~35 slides)
Same structure but expanded: more model detail (3–5 slides), full proof sketch for main theorem (2–3 slides), additional robustness (3–5 slides), more literature context (2 slides), deeper mechanism discussion (2–3 slides).

#### Lightning Talk (5–10 min, ~10 slides)
Extremely compressed: Title → Question → Key insight in one sentence → Model in one equation → Main result → One figure/table → Conclusion.

### Stage 4: Beamer Code Generation

Generate a complete, compilable LaTeX Beamer document following the templates in `references/beamer_templates.md`. The output must:

1. **Compile without errors** using `pdflatex` (or `xelatex` for CJK content)
2. **Use a clean academic theme** — default to `metropolis` theme (modern, clean, widely used in economics seminars). Fall back to `Madrid` or `CambridgeUS` if requested.
3. **Include all necessary packages** — `amsmath`, `amssymb`, `amsthm`, `graphicx`, `booktabs`, `tikz` (if figures needed)
4. **Define theorem environments** matching the paper's conventions
5. **Use consistent notation** — carry over the paper's notation exactly, or simplify with explicit mapping
6. **Include presenter notes** via `\note{}` commands with talking points for each slide

### Stage 5: Self-Verification

Before delivering the slides, verify:

#### Content Accuracy
- [ ] Every theorem/result on a slide is stated correctly (compare word-for-word with the paper)
- [ ] No formula has been incorrectly simplified (re-derive compressed versions)
- [ ] Notation is consistent across all slides
- [ ] No results are attributed that the paper doesn't actually prove

#### Structural Quality
- [ ] The talk has a clear narrative arc (question → model → answer → implications)
- [ ] Each slide has a single main point (no overloaded slides)
- [ ] Time budget is realistic (~1–1.5 minutes per slide for conference, ~2 min for seminar)
- [ ] The "preview of results" slide matches what is actually shown later

#### Technical Quality
- [ ] LaTeX compiles without errors (test via `pdflatex` if possible)
- [ ] All `\ref{}` and `\label{}` commands resolve
- [ ] Figure/table references point to existing files or are marked as placeholders
- [ ] Font sizes are readable (minimum 18pt for body text on slides)

#### Anti-Hallucination (critical)
- [ ] Every equation on the slides exists in the paper (grep the source to confirm)
- [ ] Every claim attributed to the paper is actually stated in the paper
- [ ] Literature citations on slides are verified (use `search_web` if unsure)
- [ ] No "intuition" is fabricated — it must come from the paper's own discussion or be clearly marked as the presenter's interpretation

---

## Customization Options

When triggered, ask the user (if not specified):

1. **Talk length**: Lightning / Conference / Seminar?
2. **Output format**: Beamer LaTeX / Marp Markdown?
3. **Theme**: Metropolis (default) / Madrid / Custom?
4. **Language**: English / Chinese / Other?
5. **Audience**: Specialists in the field / General economics / Non-economists?
6. **Include proofs?**: Full proof sketch / Key steps only / Omit entirely?

If the user doesn't specify, default to: **Conference (18 slides), Beamer, Metropolis, English, Specialist audience, Proofs omitted**.

---

## Resources

### references/extraction_protocol.md
Detailed rules for extracting content from theory, empirical, and structural economics papers. Includes field-specific extraction patterns and priority hierarchies for what to include vs. omit.

### references/beamer_templates.md
Complete Beamer templates for three paper types (theory/empirical/structural) with pre-defined theorem environments, clean formatting, and presenter notes infrastructure.

### references/slide_design_principles.md
Academic presentation design principles: one-point-per-slide rule, formula visibility standards, color usage, animation guidelines, and common mistakes to avoid.

### references/compression_rules.md
Rules for compressing mathematical content: what to keep, what to simplify, what to drop, with economics-specific examples (mechanism design, game theory, econometrics).

---

## Final Delivery Checklist

- [ ] Output file is a single, self-contained `.tex` file (or `.md` for Marp)
- [ ] File compiles without errors
- [ ] Slide count matches the target talk length
- [ ] Every slide has a clear title and single main point
- [ ] Mathematical notation is consistent with the paper
- [ ] Presenter notes are included for each substantive slide
- [ ] A "backup slides" section is included with overflow material (detailed proofs, additional robustness, data description)
