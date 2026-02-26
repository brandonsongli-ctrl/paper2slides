# Content Extraction Protocol

Rules for extracting presentation-worthy content from economics papers, organized by paper type and extraction priority.

---

## General Principles

1. **Extract the claim, not the proof.** Slides show *what* the paper proves, not *how* it proves it. Proofs go to backup slides only if specifically requested.
2. **Preserve the paper's own language for precision.** Do not paraphrase theorem statements — copy them exactly, then simplify notation if needed.
3. **Extract intuition separately from results.** The verbal explanation of *why* a result holds is often more important on slides than the formal statement.
4. **Prioritize visual content.** If the paper has a figure that conveys the result, use the figure instead of the equation.

---

## Extraction Priority Hierarchy

### Priority 1 — Must Include (every talk)
- Research question (1 sentence)
- Main result / headline finding (1–2 sentences)
- Core model setup OR identification strategy (the "machine" of the paper)
- One key equation (the estimating equation, objective function, or equilibrium condition)
- One key figure or table (the most informative visual)

### Priority 2 — Should Include (conference + seminar)
- Motivation / real-world relevance
- Key assumptions (numbered, with economic interpretation)
- Secondary results / comparative statics
- Robustness summary
- Literature positioning (how this differs from closest 3 papers)

### Priority 3 — Include if Space (seminar only)
- Proof sketch of main theorem
- Data description details
- Additional figures/tables
- Extensions and generalizations
- Detailed mechanism discussion
- Welfare analysis

### Priority 4 — Backup Slides Only
- Full proofs
- All robustness tables
- Data construction details
- Derivations
- Sensitivity analysis details

---

## Theory Paper Extraction

### Step 1: Model Primitives
Extract and organize into a single "Model" slide:

```
Players:        [List with notation]
Actions/Choices: [List with notation]
Types/States:   [Distribution, support]
Timing:         [Sequential/simultaneous, number of stages]
Information:    [Who knows what, when]
Solution Concept: [Nash/BNE/PBE/dominant strategy]
```

### Step 2: Assumptions
For each assumption in the paper:
1. Copy the formal statement exactly
2. Write a one-line plain-language interpretation
3. Classify: `[STANDARD]` (commonly used), `[RESTRICTIVE]` (drives the result), `[TECHNICAL]` (ensures existence/uniqueness)

Only restrictive assumptions need their own slide. Standard and technical ones go on the model setup slide.

### Step 3: Results
For each theorem/proposition:
1. Copy the formal statement
2. Extract the paper's own verbal interpretation (usually the paragraph after the theorem)
3. If the paper provides a graphical illustration, note the figure number
4. Determine the "headline version" — can the result be stated in one sentence?

**Slide assignment rule:**
- Main theorem → own slide with both formal statement and intuition
- Supporting lemmas → mentioned verbally or as a bullet point, not their own slide
- Corollaries → combine with the parent theorem

### Step 4: Numerical Example
If the paper includes a parametric example:
1. Extract the parameter values
2. Extract the computed equilibrium/optimal policy
3. Extract any figure that plots the example
4. This becomes a "Making It Concrete" slide that immediately follows the main theorem

### Step 5: Comparative Statics
Extract any statements of the form "As [parameter] increases, [outcome] increases/decreases":
1. List them as bullet points
2. If there's an associated figure, use it
3. This becomes a "What Drives the Result?" slide

---

## Empirical Paper Extraction

### Step 1: Research Question & Context
Extract:
- The causal question in one sentence
- The institutional/historical context in 2–3 sentences
- Why it matters for policy or theory

### Step 2: Identification Strategy
This is the most important extraction. Build an "Identification" slide that answers:
- What is the treatment?
- What is the source of exogenous variation?
- What is the key identifying assumption (in plain language)?
- What threats are addressed and how?

### Step 3: Data Snapshot
Extract for a "Data" slide:
- Source(s)
- Sample size (N)
- Unit of observation
- Time period
- Key variables (dependent, independent, controls)
- Summary statistics for 3–5 key variables

### Step 4: Main Specification
Copy the main estimating equation. For the slide version:
- Use a clean, numbered equation
- Define each term below the equation in a compact legend
- Highlight the coefficient of interest (e.g., with `\color{red}` or `\alert{}`)

### Step 5: Results Tables
For each key table:
1. Identify the 2–3 most important columns
2. Extract the coefficient of interest, standard error, and significance stars
3. Note the N and R²
4. **Do NOT reproduce the entire table on a slide** — select the key spec and present it cleanly

**Slide rule for tables:** Maximum 4 columns, 6 rows on a slide. If the original table is larger, select the most relevant subset.

### Step 6: Robustness
Summarize as a bullet list: "Results robust to [spec 1], [spec 2], [spec 3]." One slide maximum.

---

## Structural Paper Extraction

### Step 1: Model Timeline
Extract the timing of the model as a numbered sequence or a TikZ timeline diagram:
1. Nature draws types/shocks
2. Agents make decisions
3. Market clears / equilibrium realized
4. Outcomes observed

### Step 2: Estimation
Extract:
- What moments are targeted
- What method is used (MLE, GMM, simulated moments)
- What parameters are identified from what variation

### Step 3: Counterfactuals
Extract each policy experiment as:
- Description of the counterfactual
- Key quantitative finding (e.g., "Policy X increases welfare by 3.2%")
- Present as a comparison table or bar chart

---

## Formula Extraction Rules

When extracting equations for slides:

1. **Copy exactly first**, then compress. Never compress directly from memory.
2. **Verify against source:** After compression, grep the original file for key terms to confirm the equation matches.
3. **Preserve numbering:** Use the paper's equation numbers on slides so the audience can find them in the paper.
4. **Mark simplified versions:** If you simplify notation for the slide, add a small note: "Notation simplified; see Eq. (X) in the paper."
