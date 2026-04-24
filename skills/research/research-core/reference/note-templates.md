# Note-Taking Strategy

A research note is a compressed, high-density representation of a paper. The goal is to extract the useful information and drop the rest — so you never need to re-read the paper, and the note is useful as context for the model.

A paper is verbose by design (reviewers expect thoroughness). A note is dense by design. Multiple paragraphs often compress to one line.

---

## Extraction by section

Each section has different extraction value. Read and extract accordingly.

**Abstract** — extract the claim, but verify it against the results. Abstracts oversell. Note what they *say* they contribute, then check if the results actually support it.

**Introduction** — skip the motivation paragraphs (they restate the abstract). Extract: the last 2 paragraphs (contribution statement) and the list of "our contributions" if present. Everything else is background you probably know.

**Related work** — skip entirely on first read. Come back only to extract papers worth following. Note them in "Key references" and move on. The positioning arguments aren't useful — you'll form your own.

**Method** — highest extraction value. For scientific and ML papers, **the equations are not optional** — prose is not a substitute for math. "They normalize rewards within the group" without the formula loses the most important information. You can reconstruct prose from an equation; you cannot reconstruct an equation from prose.

Extract:
- The core objective or loss function in full LaTeX
- How the key quantity is computed (advantage, reward, attention score, gradient)
- Any equation the paper references by number later — if they write "as in Eq. 3", that equation belongs in your notes
- Any "we found that..." sentence — those are undocumented tricks

Multiple pages of method often compress to 1–2 equations + 3 lines of prose explaining what each term does. That compression is the goal.

**Experiments** — extract: the delta over the most relevant baseline (not absolute numbers), which ablation isolates the key factor, and any result that surprised you. Drop: tables you won't reference again, benchmarks irrelevant to your work.

**Conclusion** — usually redundant. Skim for "future work" — those sentences have ideation value.

**Appendix** — often where the real implementation details live: exact hyperparameters, data preprocessing, training tricks. Read if you're implementing. Skip otherwise.

---

## Compression rules

- Multiple motivation paragraphs → 1 line: what problem, why it matters
- 3-page method description → core equation or algorithm + prose for what each term does
- Results table → 2–3 key numbers with context ("X% on Y, +Z over baseline B")
- Limitations section → bullet list, 2–4 items, only the ones that affect your use case
- "We propose a novel framework" → delete, replace with what the framework actually does

The target: a note you can read in 3 minutes that gives you 80% of the value of re-reading the paper.

---

## What to drop

- "In this paper, we..." sentences (the paper is the paper)
- Extensive related work summaries
- Proofs you don't need to understand the contribution
- Absolute benchmark numbers without delta or context
- Experimental details irrelevant to your work
- Acknowledgements, author contributions, boilerplate

---

## Calibrate to your purpose

**Reading to understand**: extract claim + mechanism + key result. For scientific/ML papers, equations are mandatory even in understand mode — the math is the mechanism.

**Reading to implement**: extract architecture/algorithm, all hyperparameters, training procedure, evaluation protocol. Equations mandatory. Note every "we found that..." sentence.

**Screening**: one line per paper — what it does + relevance to your work. Nothing else.

**Reading a tech article**: key takeaway + what you'd apply + any code worth keeping. Note publication date (content ages).

---

## Template

The template enforces compression. Each section has an explicit length limit — staying within it forces you to decide what matters. Add extension sections only when the content genuinely requires it.

```markdown
---
type: paper | paper-impl | article | comparison
title: "..."
authors: [Last1 et al.]
year: 2024
arxiv: "2402.03300"    # omit if not applicable
contribution: method | finding | dataset | unification | negative-result | survey
tags: [topic1, topic2]
status: to-read | reading | read | implemented
---

## Summary
[2–4 lines. What the paper does and what it shows.
Not the abstract — your compression of it.]

## Method
[Core algorithm or design decision.
For scientific/ML papers: the equations are mandatory, not optional.
Write the objective function, loss, or key operation in full LaTeX.
Then explain what each term does in 1–2 lines of prose.
Max 15 lines total including equations.

Math notation rules — no exceptions:
- Display equations: $$...$$
- Inline math: $...$
- Code blocks (``` ```) are for code only — NEVER for mathematical formulas
- Inside $...$ or $$...$$: LaTeX commands, not Unicode symbols
  (\omega not ω, \theta not θ, \pi not π, \nabla not ∇, \sum not Σ, \leq not ≤)

Correct:
$$\mathcal{L} = -\log p(y \mid x, \theta)$$

Wrong:
\[L = -log p(y | x, θ)\]

## Results
[2–4 key numbers with context. Delta over the relevant baseline.
Call out any result that looks weak or cherry-picked.]

## Limits
[3–5 bullets. What the paper doesn't test, what assumptions could
break, what you'd verify before trusting the results.]

## Connections
[The paper's position in the field. 5–8 entries max.
Format: [Author Year] — direction — one-line reason
Directions: builds-on | supersedes | competes-with | enables

Example:
- [Schulman 2017] — builds-on — PPO baseline; GRPO removes the value model
- [Lightman 2023] — competes-with — process vs outcome supervision
- [DeepSeek-R1 2025] — enables — GRPO used for pure RL reasoning]
```

**Extension sections** — add when needed, not by default:
- `## Hyperparameters` — when implementing
- `## Open questions` — when the paper raises something worth exploring
- `## Relevance` — when the connection to your work isn't obvious

Never add a `## Citation` or `## BibTeX` block. Citations are retrieved via `papers.py bibtex`, never written from memory.

---

## Filename

`author2024-topic.md` — lowercase, hyphens, no spaces.
`shao2024-grpo.md`, `vaswani2017-attention.md`, `lilianweng-rlhf-overview.md`
