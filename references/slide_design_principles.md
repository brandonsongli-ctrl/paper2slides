# Slide Design Principles for Academic Economics Presentations

Rules for creating effective academic slides. These principles are specific to economics seminars and conferences where the audience consists of researchers who expect mathematical precision but limited patience for cluttered slides.

---

## The Core Rule: One Point Per Slide

Every slide must have **exactly one main point**. If you find yourself writing "and also..." on a slide, split it.

| Slide Element | Maximum |
|--------------|---------|
| Main point | 1 |
| Bullet points | 5 |
| Equations | 2 (ideally 1) |
| Table columns | 4 |
| Table rows | 6 |
| Words (excluding math) | 40 |
| Figures | 1 |

---

## Slide Titles

### Rules
1. **Every slide must have a title.** No untitled slides except the title slide and "Thank You."
2. **Titles should be informative, not descriptive.** Use the result, not the category.
3. **Maximum title length:** one line (avoid two-line wrapping titles).

### Examples

| ❌ Bad Title | ✅ Good Title |
|-------------|--------------|
| "Results" | "Radio Exposure Reduces Nazi Vote Share" |
| "Model" | "Two-Stage Persuasion Game" |
| "Table 3" | "Main Estimates: Coverage → Voter Knowledge" |
| "Robustness" | "Results Robust to Alternative Specifications" |
| "Literature" | "Contribution Relative to DellaVigna & Kaplan (2007)" |

---

## Mathematical Content on Slides

### Font Size
- Body text: minimum **18pt** (11pt in Beamer with default scaling)
- Equations: should be **at least as large** as body text
- Subscripts/superscripts: must remain legible at projected size
- Table contents: minimum **14pt** (9pt in Beamer)

### Equation Presentation
1. **Number key equations** — use the paper's equation numbers so the audience can look them up
2. **Highlight the key term** — use `\alert{}` or `\textcolor{red}{}` for the coefficient of interest or object of study
3. **Define symbols immediately below the equation** in a compact legend
4. **Use `align` environments** sparingly — avoid multi-line aligned derivations on slides

### Example: Good equation slide
```latex
\begin{frame}{Estimating Equation}
  \begin{equation}\tag{1}
    y_{it} = \alpha + \alert{\beta} \cdot Slant_t \times Exposure_{it} 
    + \mathbf{Z}_{it}'\gamma + \phi_i + \tau_t + \varepsilon_{it}
  \end{equation}
  
  \vspace{0.3cm}
  \begin{small}
  \begin{tabular}{ll}
    $\alert{\beta}$: & \alert{Effect of slanted radio on Nazi vote share} \\
    $Slant_t$: & $\{0, -1, +1\}$ for neutral / pro-government / pro-Nazi \\
    $Exposure_{it}$: & Radio signal strength (or subscription rate) \\
    $\phi_i, \tau_t$: & District and year fixed effects \\
  \end{tabular}
  \end{small}
\end{frame}
```

---

## Tables on Slides

### The Golden Rule
**Never paste an entire regression table onto a slide.** Extract the key rows and columns.

### Formatting
1. Use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`) — never use vertical lines
2. Bold or color the coefficient of interest
3. Include standard errors in parentheses directly below coefficients
4. Show N and R² at the bottom
5. Put significance stars with a footnote: `* p<0.1, ** p<0.05, *** p<0.01`

### Slide Table Template
```latex
\begin{frame}{Main Results}
  \begin{table}\centering
  \begin{small}
  \begin{tabular}{lcc}
    \toprule
    & (1) Baseline & (2) With Controls \\
    \midrule
    Treatment & \alert{0.45}$^{***}$ & \alert{0.38}$^{***}$ \\
              & (0.12) & (0.11) \\[0.3em]
    \midrule
    Controls & No & Yes \\
    Fixed Effects & Year & Year + District \\
    Observations & 4{,}206 & 4{,}206 \\
    $R^2$ & 0.18 & 0.27 \\
    \bottomrule
  \end{tabular}
  \end{small}
  \end{table}
  
  \vspace{0.2cm}
  {\footnotesize \textit{Note:} Robust SE clustered by region. 
  $^*p{<}0.1$, $^{**}p{<}0.05$, $^{***}p{<}0.01$.}
\end{frame>
```

---

## Figures on Slides

1. **Maximize figure size** — use `\includegraphics[width=\textwidth]` or close to it
2. **Label axes clearly** — assume the audience cannot read small print from the back of the room
3. **Add a one-line caption below** explaining what the figure shows
4. **Use TikZ for simple diagrams** — model timelines, game trees, causal diagrams
5. **Never use screenshots of figures from papers** — redraw or reproduce cleanly

---

## Color Usage

### Academic Palette
Keep colors minimal and purposeful:

| Use | Color | Purpose |
|-----|-------|---------|
| Emphasis / coefficient of interest | Red (`\alert{}`) | Draw attention to key result |
| Secondary emphasis | Blue | Model components, definitions |
| De-emphasis | Gray | Footnotes, caveats, notation legends |
| Background | White | Always (never use dark backgrounds for academic talks) |

### Never
- Use more than 3 colors on a single slide
- Use green-on-white (low contrast at projection)
- Use color as the only distinguishing feature (colorblind accessibility)

---

## Animation and Overlays

### When to Use
- **Revealing bullet points sequentially** — use `\pause` or `\onslide<2->{}` for complex arguments where you want to explain each point before showing the next
- **Building up a figure** — use TikZ overlays to add elements one at a time
- **Before/after comparison** — show the baseline on one overlay and the result on the next

### When NOT to Use
- Tables (show the full table at once)
- Equations (show the full equation at once, then highlight parts)
- Literature slides (list everything at once)

### Implementation
```latex
% Simple pause
\begin{frame}{Three Key Results}
  \begin{enumerate}
    \item First result \pause
    \item Second result \pause  
    \item Third result
  \end{enumerate}
\end{frame}

% Overlay specification
\begin{frame}{Building the Argument}
  \only<1>{First piece of evidence...}
  \only<2>{Second piece of evidence...}
  \only<3>{Therefore, the conclusion is...}
\end{frame}
```

---

## Time Budget

### Rule of Thumb
- Conference talk: **1.0–1.5 minutes per slide**
- Seminar talk: **1.5–2.5 minutes per slide**
- Lightning talk: **0.5–1.0 minutes per slide**

### Time Allocation by Section

| Section | Conference (20 min) | Seminar (60 min) |
|---------|-------------------|------------------|
| Motivation + Question | 2.5 min (12%) | 5 min (8%) |
| Literature | 1 min (5%) | 3 min (5%) |
| Model / Data | 4 min (20%) | 15 min (25%) |
| Main Results | 6 min (30%) | 15 min (25%) |
| Robustness / Extensions | 3 min (15%) | 10 min (17%) |
| Intuition / Mechanism | 2 min (10%) | 8 min (13%) |
| Conclusion | 1.5 min (8%) | 4 min (7%) |

---

## Common Mistakes to Avoid

1. **"Wall of text" slides** — if a slide has more than 40 words, it needs to be split or compressed
2. **Reading slides verbatim** — slides are visual aids, not scripts; use presenter notes for talking points
3. **Including all robustness checks** — pick the 3 most important, put the rest in backup
4. **Full proofs on main slides** — proofs belong in backup slides; main slides show the result and intuition
5. **Too many literature citations** — 3 strands with 2–3 key papers each, not a comprehensive survey
6. **Missing "so what?"** — every result slide should make clear why the audience should care
7. **Ending with "Future Work"** — end with the takeaway, not with what you haven't done yet
8. **No backup slides** — always prepare 5–10 backup slides for anticipated questions
