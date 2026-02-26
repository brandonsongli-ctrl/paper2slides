# Formula Compression Rules

Rules for compressing mathematical content from a full paper into slide-ready form. Every compression must preserve correctness while maximizing readability at presentation scale.

---

## Core Principle

> **Show the WHAT, not the HOW.** Slides present results and key equations. Papers present derivations.

---

## Decision Framework

For every mathematical object in the paper, ask:

```
Is this object needed to understand the RESULT?
├── Yes → Keep it
│   ├── Can it be simplified without loss of meaning?
│   │   ├── Yes → Compress (see rules below)
│   │   └── No → Keep verbatim
│   └── Is it a multi-step derivation?
│       ├── Yes → Show only first and last step
│       └── No → Keep as-is
└── No → Drop it
    └── Move to backup slides if it answers a likely question
```

---

## What to Keep

| Category | Example | Action |
|----------|---------|--------|
| **Definitions** | "Define $V(\tau) \equiv \max_{\pi} \E[u(\pi, \theta)]$" | Keep verbatim |
| **The optimization problem** | $\max_{x} f(x) \text{ s.t. } g(x) \leq 0$ | Keep verbatim |
| **Key equilibrium condition** | First-order condition of the main problem | Keep |
| **Main theorem statement** | Theorem 1 formal statement | Keep verbatim |
| **Estimating equation** | The regression specification | Keep verbatim |
| **Closed-form solutions** | $x^* = \frac{a - c}{2b}$ | Keep |

## What to Compress

### 1. Multi-line Derivations → Single Result

**Paper version (DON'T put on slide):**
$$
\begin{aligned}
V(\tau) &= \int_0^1 u(\tau, \theta) dF(\theta) \\
&= \int_0^{\tau} u_L(\theta) dF(\theta) + \int_{\tau}^1 u_H(\theta) dF(\theta) \\
&= F(\tau) \cdot \E[u_L | \theta \leq \tau] + (1-F(\tau)) \cdot \E[u_H | \theta > \tau] \\
&= F(\tau) \bar{u}_L(\tau) + (1-F(\tau)) \bar{u}_H(\tau)
\end{aligned}
$$

**Slide version (DO put on slide):**
$$
V(\tau) = F(\tau) \cdot \bar{u}_L(\tau) + (1 - F(\tau)) \cdot \bar{u}_H(\tau)
$$
*where $\bar{u}_L(\tau) \equiv \E[u_L | \theta \leq \tau]$ and $\bar{u}_H(\tau) \equiv \E[u_H | \theta > \tau]$*

### 2. Long Summations → Compact Notation

**Paper:** $\sum_{i=1}^{N} \sum_{t=1}^{T} w_{it} \cdot \mathbb{1}[y_{it} > \bar{y}] \cdot (x_{it} - \bar{x}_i)$

**Slide:** $\sum_{i,t} w_{it} \cdot \mathbb{1}_{it} \cdot \tilde{x}_{it}$ with definitions below

### 3. Repeated Substitutions → Final Expression

If the paper substitutes step-by-step (e.g., plugging the optimal $x^*$ into the value function, then that into the expected payoff), show only the final composite expression.

### 4. Systems of Equations → Key Equation Only

If the paper has a system of 5 FOCs, show only the one that generates the key result. Mention "the full system has 5 conditions; the binding one is..."

---

## What to Drop

| Category | Why Drop | Where It Goes |
|----------|----------|--------------|
| **Proof steps** | Audience doesn't verify proofs live | Backup slide (optional) |
| **Intermediate algebra** | No insight added | Nowhere |
| **Routine FOCs** | Standard; audience can derive | Mention verbally |
| **Measure-theoretic formalism** | Distracting; invoke by name | "By [theorem name]..." |
| **Appendix material** | Not part of the main argument | Backup slide |
| **Existence proofs** | State "exists" as a result | Backup slide |
| **Regularity conditions** | State "under standard regularity" | Footnote on assumption slide |

---

## Notation Simplification

### When to Simplify

Simplify when the paper's notation is heavier than needed for the slide context:

| Paper Notation | Slide Simplification | Condition |
|---------------|---------------------|-----------|
| $\mathcal{F}_{\Theta}^{(k)}$ | $F$ | If there's only one distribution on slides |
| $\sigma_{-i}^{NE}(\theta_i; \mu)$ | $\sigma^*(\theta)$ | If context is clear |
| $\mathbb{E}_{\theta \sim F}[\cdot]$ | $\E[\cdot]$ | If the distribution is obvious |
| $u_i(a_i, a_{-i}; \theta_i, \theta_{-i})$ | $u_i(a, \theta)$ | If the full argument list adds no insight |

### When NOT to Simplify

- When the distinction between two similar symbols matters for the result
- When the audience needs to look up the equation in the paper
- When the simplified version is ambiguous

### Mandatory Disclosure

Whenever notation is simplified, add a small note on the slide:
```latex
{\footnotesize \textit{Notation simplified from Eq.~(X) in the paper.}}
```

---

## Economics-Specific Compression Patterns

### Mechanism Design
**Paper:** Full revelation-principle argument → direct mechanism → IC/IR constraints → optimal mechanism characterization
**Slides:** State the optimal mechanism directly. Say "by the revelation principle, WLOG focus on direct mechanisms" verbally. Show IC constraint only if it's the key economic object.

### Game Theory
**Paper:** Strategy profile → best response derivation → fixed point → equilibrium characterization
**Slides:** State the equilibrium directly. Show the key best-response equation if it conveys economic intuition. Skip the fixed-point argument.

### Econometrics / Identification
**Paper:** Full derivation of the bias formula, showing each omitted variable's contribution
**Slides:** State the estimating equation. Show the bias formula only if it's the key insight (e.g., Equation (1) in Angrist & Pischke style).

### Welfare Analysis
**Paper:** Full social welfare function → substitution of equilibrium values → comparative statics
**Slides:** State the welfare expression with equilibrium values already substituted. Show the comparative static result directly.

---

## Compression Self-Check

Before finalizing, verify each compressed equation:

- [ ] **Correctness:** Does the compressed version follow from the paper's original? Re-derive to confirm.
- [ ] **Completeness:** Are all symbols on the slide defined somewhere (either on the same slide or a previous one)?
- [ ] **Consistency:** Is the notation on this slide consistent with all other slides?
- [ ] **Source traceability:** Can the audience find the full version in the paper? (Include equation numbers.)
- [ ] **Anti-hallucination:** Grep the original file for the key terms to confirm the equation actually appears in the paper — do not compress from memory.
