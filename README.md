# Paper2Slides (Academic Beamer Generator)

`paper2slides` is a specialized AI skill designed to automate the painful process of converting highly technical academic economics papers (working papers, PDFs, or LaTeX files) into clean, professional, and compilable LaTeX Beamer presentations within minutes.

## Features

- **Intelligent Extraction:** Automatically identifies and extracts the core Motivation, Literature Review, Model Setup, Identification Strategy, and Main Results based on paper type (Theory, Empirical, or Structural).
- **Formula Compression:** Intelligently summarizes dense math blocks and proofs, keeping only the essential notation required for a presentation slide format.
- **Audience Calibration:** Automatically adjusts the density and slides count for Lightning Talks (5 mins), Conference Talks (15 mins), or full Seminars (60-90 mins).
- **Anti-Hallucination:** Built-in multi-round verification to ensure equations, citations, and empirical magnitudes reflect the actual source document.
- **Compilable Output:** Generates ready-to-use `.tex` source files (using the `metropolis` theme) or Markdown implementations for Marp/Reveal.js.

## Skill Structure

The skill is built for integration with Claude desktop or any capable LLM agent system:

```text
paper2slides/
├── SKILL.md                                 # Main execution logic and trigger words
└── references/
    ├── extraction_protocol.md               # Rules for extracting content by paper type
    ├── slide_design_principles.md           # Academic presentation best practices 
    ├── compression_rules.md                 # Rules for reducing formula complexity
    └── beamer_templates.md                  # Baseline compilable LaTeX Beamer structures
```

## How to Use

When integrated with an agent or directly passed as system context, you can trigger it simply by passing the path to an academic PDF or `.tex` file:

```bash
# Example user prompt:
paper2slides '/path/to/my_economics_working_paper.pdf'
```

You can customize the output by specifying parameters:
> "Use `paper2slides` on this paper. Make it a 15-minute conference talk. Focus specifically on the robustness checks section."

## Output Example

The tool generates a single, clean LaTeX file that compiles directly into a PDF presentation:
- Standardized `metropolis` modern theme
- Highlighted key variables
- Presenter notes attached to each slide via `\note{}`

---

*Built with the Grant Copilot mindset—designed by economists, for economists.*
