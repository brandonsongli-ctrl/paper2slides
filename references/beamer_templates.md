# Beamer Templates

Complete, compilable LaTeX Beamer templates for economics presentations. Each template includes the preamble, theme configuration, theorem environments, and slide structure.

---

## Universal Preamble

The following preamble works for all paper types. Copy it as the starting point for any presentation:

```latex
\documentclass[aspectratio=169, 11pt]{beamer}

% --- Theme ---
\usetheme{metropolis}
\metroset{
  numbering=fraction,
  progressbar=frametitle,
  block=fill
}

% --- Fonts ---
\usepackage[T1]{fontenc}
\usepackage{lmodern}

% --- Math ---
\usepackage{amsmath, amssymb, amsthm, mathtools}
\usepackage{bm}  % Bold math symbols

% --- Tables and Figures ---
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{arrows.meta, positioning, calc, decorations.pathreplacing}

% --- Colors (academic palette) ---
\definecolor{accent}{HTML}{2E86AB}
\definecolor{highlight}{HTML}{D7263D}
\definecolor{muted}{HTML}{6B717E}
\definecolor{resultbg}{HTML}{E8F4FD}
\setbeamercolor{alerted text}{fg=highlight}

% --- Theorem Environments ---
\setbeamertemplate{theorems}[numbered]
\newtheorem{assumption}[theorem]{Assumption}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{remark}[theorem]{Remark}

% --- Utilities ---
\newcommand{\E}{\mathbb{E}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\plim}{\mathrm{plim}}
\newcommand{\indep}{\perp \!\!\! \perp}
\newcommand{\highlight}[1]{\textcolor{highlight}{\textbf{#1}}}

% --- Slide numbering in footer ---
\setbeamertemplate{frame numbering}[fraction]

% --- Suppress navigation symbols ---
\setbeamertemplate{navigation symbols}{}

% --- Presenter notes (uncomment to enable) ---
% \setbeameroption{show notes on second screen=right}
```

---

## Template 1: Theory Paper

```latex
% ============================================================
% THEORY PAPER TEMPLATE
% ============================================================

\title{%
  \texorpdfstring{%
    Paper Title Here%
  }{Paper Title Here}%
}
\subtitle{A Conference Presentation}
\author{Author Name}
\institute{University \\ \texttt{email@institution.edu}}
\date{Conference Name \\ \today}

\begin{document}

% --- TITLE ---
\begin{frame}
  \titlepage
\end{frame}

% --- MOTIVATION ---
\begin{frame}{Motivation}
  \begin{itemize}
    \item \highlight{Broad question:} [One sentence about the real-world phenomenon]
    \item \highlight{Specific puzzle:} [What existing theory cannot explain]
    \item \highlight{This paper:} [What this paper does, in one sentence]
  \end{itemize}
  \note{Spend 1--1.5 minutes. Connect to something the audience cares about.}
\end{frame}

% --- PREVIEW ---
\begin{frame}{Preview of Results}
  \begin{enumerate}
    \item \textbf{Main Result:} [One-sentence headline]
    \item \textbf{Mechanism:} [Why this happens --- economic intuition]
    \item \textbf{Implication:} [What it means for policy / future theory]
  \end{enumerate}
  \note{The audience should know where you are going. No surprises.}
\end{frame}

% --- LITERATURE ---
\begin{frame}{Related Literature}
  \begin{itemize}
    \item \textbf{Strand 1:} [Author1 (Year), Author2 (Year)] --- [How this paper differs]
    \item \textbf{Strand 2:} [Author3 (Year)] --- [How this paper differs]
    \item \textbf{Strand 3:} [Author4 (Year)] --- [How this paper differs]
  \end{itemize}
  \note{Keep to 3 strands max. Position, don't survey.}
\end{frame}

% --- MODEL ---
\begin{frame}{Model Setup}
  \begin{itemize}
    \item \textbf{Players:} [List]
    \item \textbf{Actions:} [List]
    \item \textbf{Types:} $\theta \sim F$ on $[\underline{\theta}, \overline{\theta}]$
    \item \textbf{Timing:}
    \begin{enumerate}
      \item Stage 1: [...]
      \item Stage 2: [...]
    \end{enumerate}
    \item \textbf{Payoffs:} $u_i(\cdot)$ [brief description]
  \end{itemize}
\end{frame}

% --- ASSUMPTIONS ---
\begin{frame}{Key Assumptions}
  \begin{assumption}[Regularity]
    [Formal statement]
  \end{assumption}
  \vspace{0.3cm}
  \textcolor{muted}{\textit{Economic interpretation:} [One sentence]}
  
  \vspace{0.5cm}
  \begin{assumption}[Key Restriction]
    [Formal statement]
  \end{assumption}
  \vspace{0.3cm}
  \textcolor{muted}{\textit{Economic interpretation:} [One sentence]}
\end{frame}

% --- MAIN RESULT ---
\begin{frame}{Main Result}
  \begin{theorem}[Main]
    [Formal statement of the main theorem]
  \end{theorem}
  
  \vspace{0.5cm}
  \textbf{Intuition:}
  \begin{itemize}
    \item [Key economic force 1]
    \item [Key economic force 2]
    \item [Why the result is not obvious]
  \end{itemize}
  \note{This is the key slide. Spend 2--3 minutes here.}
\end{frame}

% --- ILLUSTRATION ---
\begin{frame}{Illustration: Numerical Example}
  % [Figure or parametric example here]
  % \includegraphics[width=0.8\textwidth]{example_figure.pdf}
  \begin{center}
    \textit{[Insert figure or numerical example]}
  \end{center}
  \note{Make the abstract result concrete. Use specific numbers.}
\end{frame}

% --- COMPARATIVE STATICS ---
\begin{frame}{Comparative Statics}
  \begin{proposition}
    [Statement about how outcomes change with parameters]
  \end{proposition}
  
  \vspace{0.3cm}
  \textbf{Interpretation:}
  \begin{itemize}
    \item As $[\text{parameter}]$ increases, $[\text{outcome}]$ [increases/decreases]
    \item This is because [economic mechanism]
  \end{itemize}
\end{frame}

% --- CONCLUSION ---
\begin{frame}{Conclusion}
  \begin{enumerate}
    \item \textbf{Main takeaway:} [One sentence]
    \item \textbf{Policy implication:} [One sentence]
    \item \textbf{Future work:} [One direction]
  \end{enumerate}
\end{frame}

% --- THANK YOU ---
\begin{frame}[standout]
  Thank you!
  
  \vspace{0.5cm}
  {\small \texttt{email@institution.edu}}
\end{frame}

% ============================================================
% BACKUP SLIDES
% ============================================================
\appendix

\begin{frame}{Proof Sketch: Main Theorem}
  \textit{[Key steps of the proof, not the full derivation]}
\end{frame}

\begin{frame}{Additional Comparative Statics}
  \textit{[Secondary results]}
\end{frame}

\end{document}
```

---

## Template 2: Empirical Paper

```latex
% ============================================================
% EMPIRICAL PAPER TEMPLATE
% ============================================================

\title{Paper Title Here}
\subtitle{A Conference Presentation}
\author{Author Name}
\institute{University \\ \texttt{email@institution.edu}}
\date{Conference Name \\ \today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Motivation}
  \begin{itemize}
    \item \highlight{Policy question:} [One sentence]
    \item \highlight{Why hard:} [The identification challenge]
    \item \highlight{This paper:} [Source of variation + headline result]
  \end{itemize}
\end{frame}

\begin{frame}{Preview of Results}
  \begin{enumerate}
    \item [Headline effect: direction, magnitude, significance]
    \item [Key mechanism / heterogeneity]
    \item [Robustness summary in one sentence]
  \end{enumerate}
\end{frame}

\begin{frame}{Data}
  \begin{itemize}
    \item \textbf{Source:} [Dataset name]
    \item \textbf{Sample:} $N = $ [size], [unit], [time period]
    \item \textbf{Key variables:}
    \begin{itemize}
      \item Dependent: [variable, mean, SD]
      \item Treatment: [variable, mean, SD]
      \item Key controls: [list]
    \end{itemize}
  \end{itemize}
\end{frame}

\begin{frame}{Identification Strategy}
  \highlight{Key idea:} [One-sentence summary of the source of variation]
  
  \vspace{0.3cm}
  \textbf{Identifying assumption:}
  \begin{quote}
    \textit{[State in plain language]}
  \end{quote}
  
  \vspace{0.3cm}
  \textbf{Threats addressed:}
  \begin{itemize}
    \item [Threat 1] $\rightarrow$ [How addressed]
    \item [Threat 2] $\rightarrow$ [How addressed]
  \end{itemize}
\end{frame}

\begin{frame}{Main Specification}
  \begin{equation}
    y_{it} = \alpha + \alert{\beta} \cdot Treatment_{it} + \mathbf{X}_{it}'\gamma + \phi_i + \tau_t + \varepsilon_{it}
  \end{equation}
  
  \vspace{0.3cm}
  \begin{small}
  \begin{tabular}{ll}
    $y_{it}$: & Outcome variable \\
    $\alert{\beta}$: & \alert{Coefficient of interest} \\
    $\phi_i, \tau_t$: & Unit and time fixed effects \\
    $\mathbf{X}_{it}$: & Controls \\
  \end{tabular}
  \end{small}
  
  \note{Highlight the coefficient of interest in red.}
\end{frame}

\begin{frame}{Main Results}
  \begin{table}
    \centering
    \begin{small}
    \begin{tabular}{lcc}
      \toprule
      & (1) OLS & (2) IV \\
      \midrule
      Treatment & $\alert{X.XX}^{***}$ & $\alert{X.XX}^{***}$ \\
                & (X.XX) & (X.XX) \\
      \midrule
      Controls & Yes & Yes \\
      FE & Unit + Year & Unit + Year \\
      $N$ & XX,XXX & XX,XXX \\
      \bottomrule
    \end{tabular}
    \end{small}
  \end{table}
  
  \vspace{0.3cm}
  \textbf{Magnitude:} A 1-SD increase in treatment $\rightarrow$ [X]\% change in outcome.
\end{frame}

\begin{frame}{Robustness}
  Results robust to:
  \begin{enumerate}
    \item [Alternative specification 1]
    \item [Alternative specification 2]
    \item [Placebo test: ...]
    \item [Alternative sample: ...]
  \end{enumerate}
  \textcolor{muted}{\textit{Details in backup slides.}}
\end{frame}

\begin{frame}{Conclusion}
  \begin{enumerate}
    \item \textbf{Main finding:} [One sentence with number]
    \item \textbf{Policy implication:} [One sentence]
    \item \textbf{Limitation:} [One honest caveat]
  \end{enumerate}
\end{frame}

\begin{frame}[standout]
  Thank you!
  
  \vspace{0.5cm}
  {\small \texttt{email@institution.edu}}
\end{frame}

\appendix

\begin{frame}{Robustness: Full Table}
  \textit{[Complete robustness table]}
\end{frame}

\begin{frame}{First Stage (IV)}
  \textit{[First-stage results if IV used]}
\end{frame>

\begin{frame}{Balance Table}
  \textit{[Covariate balance across treatment/control]}
\end{frame}

\end{document}
```

---

## Theme Variants

### Metropolis (Default)
Clean, modern, minimal. Best for micro theory and applied micro.
```latex
\usetheme{metropolis}
```

### Madrid
Classic, colorful. Common in European conferences.
```latex
\usetheme{Madrid}
\usecolortheme{whale}
```

### CambridgeUS
Traditional, red/gray. Common in U.S. department seminars.
```latex
\usetheme{CambridgeUS}
\usecolortheme{dolphin}
```

### Plain (no theme)
Maximum control. Good for job market talks.
```latex
\usetheme{default}
\usecolortheme{dove}
\setbeamertemplate{frametitle}{\insertframetitle}
```
