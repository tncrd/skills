# Reading Strategies

Different content types require different reading modes. Pick the mode before you start — it determines what you extract.

---

## Lossless Extraction Flow

For any scientific or ML paper you're reading seriously (Mode 1 or Mode 2). An ordered protocol that ensures no critical information is dropped. The order matters: each pass contextualizes the next.

```
STEP 0 — Discover structure
  Command: papers.py toc <id>
  Read the full TOC. Identify which sections correspond to each pass below.
  Use section numbers (not names) for all subsequent calls — numbers are stable,
  names vary between papers.

  Mapping guide (the section may be called anything):
    Pass 2 (Claim)       → introduction + conclusion sections
    Pass 3 (Math)        → core method / approach / architecture / algorithm section
    Pass 4 (Evidence)    → experiments / evaluation / results / analysis section
    Pass 5 (Positioning) → related work / background / prior work section
    Pass 6 (Limits)      → limitations / conclusion / discussion section
    Pass 7 (Threads)     → future work / discussion / conclusion section

  If a section is absent from the TOC → skip that pass or look in the nearest
  adjacent section. Do not guess section names.

PASS 1 — Identity
  Command: papers.py fetch <id>
  Extract: paper type (method / finding / dataset / survey / negative-result)

PASS 2 — Claim
  Command: papers.py section <id> <intro_number>
           papers.py section <id> <conclusion_number>
  Extract: what do they assert? does the conclusion match the abstract?
  Flag: discrepancy between claimed and delivered contribution

PASS 3 — Math (cannot be skipped for scientific/ML papers)
  Command: papers.py section <id> <method_number>
  Extract in this order:
    1. Core objective / loss function → full LaTeX
    2. How the key quantity is computed (advantage, reward, attention, gradient) → LaTeX
    3. Every equation cited by number elsewhere in the paper → LaTeX
    4. "We found that..." sentences → verbatim (undocumented tricks)
  Rule: prose description of math is NOT a substitute. Write the formula.
  Rule: $$...$$ for display equations, $...$ for inline. Code blocks are for code only.
  Rule: inside $...$ or $$...$$, use LaTeX commands not Unicode symbols.
        \omega not ω, \theta not θ, \pi not π, \nabla not ∇, \sum not Σ, \leq not ≤

PASS 4 — Evidence
  Command: papers.py section <id> <experiments_number>
  Extract:
    - Delta over the main baseline (not absolute numbers alone)
    - Which ablation isolates the key factor
    - Any weak or surprising result
  Flag: missing error bars, outdated baselines, cherry-picked benchmarks

PASS 5 — Positioning
  Command: papers.py section <id> <related_work_number>
  Extract: 5–8 entries with direction
    - [Author Year] — builds-on / supersedes / competes-with / enables — one-line reason
  Flag: what does this paper claim prior work cannot do?

PASS 6 — Limits
  Command: papers.py section <id> <limitations_number>
           papers.py section <id> <conclusion_number>   (limits often hidden here)
  Extract:
    - What the authors admit
    - What they did NOT test (unstated assumptions)
    - What you'd need to verify before trusting the results

PASS 7 — Threads
  Command: papers.py section <id> <future_work_or_discussion_number>
  Extract: concrete open questions worth pursuing
  These feed directly into ideas/ files

WRITE — Assemble note
  Order: math before prose in ## Method
  Equations first, then "what each term does" in 1–2 lines
  Never write a prose summary and add equations later

BEFORE WRITING — Completion check
  Verify each pass was covered. Do not skip to WRITE until all 7 are done.
  If a section doesn't exist in this paper, explicitly note it as absent.

  ☐ Pass 1 — Identity (fetch)
  ☐ Pass 2 — Claim (introduction + conclusion)
  ☐ Pass 3 — Math (method / core algorithm)
  ☐ Pass 4 — Evidence (experiments / results)
  ☐ Pass 5 — Positioning (related work)
  ☐ Pass 6 — Limits (limitations / conclusion)
  ☐ Pass 7 — Threads (future work / discussion)
```

The passes can overlap but the extraction order should be respected.

---

## Mode 1: Understand (academic paper)

Goal: grasp the contribution and assess its relevance.

**Reading order** (not front-to-back):
1. **Title + abstract** — what do they claim?
2. **Figures and tables** — what does the evidence look like?
3. **Conclusion** — what do they actually deliver vs what was promised?
4. **Introduction (last 2 paragraphs)** — the contribution statement, usually "In this paper, we..."
5. **Method** — how they did it
6. **Related work** — only if you need context on the field

**Extract**: question, method, key result, limitations, relevance to your work, positioning against prior work.

**Related work** — don't skip. This section is the paper's map of the field. Extract:
- The 2–3 most important prior works this paper builds directly on
- The 1–2 competing approaches it supersedes or competes with
- Any explicit "prior work cannot do X, we now can"

5–8 entries maximum, with a one-line note on WHY each matters.

**Skip**: motivation paragraphs, acknowledgements, proofs you don't need to understand the contribution.

**Time**: 20–40 minutes for a first pass. If a paper takes longer, it's either very dense (normal for math-heavy work) or poorly written (not your problem to fix).

---

## Mode 2: Implement (academic paper)

Goal: reproduce or adapt the method in code. Keshav's "third pass" standard — attempt to virtually re-implement the paper: making the same assumptions as the authors, reconstruct the work. The gap between your reconstruction and the actual paper reveals the real innovations and hidden assumptions.

**Reading order**:
1. **Method section** — the core algorithm
2. **Pseudocode / algorithm blocks** — if they exist, these are your primary source
3. **Appendix** — hyperparameters, training details, architectural specifics often hidden here
4. **Ablation studies** — which components actually matter vs which are optional
5. **Code repository** — if linked, read it BEFORE implementing from scratch
6. **Evaluation protocol** — so you know when your implementation is correct

**Extract**: architecture (layers, dimensions, activations), hyperparameters (lr, batch size, optimizer, schedule), training procedure (steps, warmup, data), evaluation (metrics, datasets, baselines to reproduce), tricks (initialization, normalization, any "we found that..." sentences).

**Common traps**:
- Papers omit details that are in the appendix or supplementary material
- "Standard" settings often mean "same as [previous paper]" — go check that paper
- Reported results may require specific random seeds, data preprocessing, or hardware
- If the paper has a repo, check the issues — other people's implementation problems are your shortcut

---

## Mode 3: Survey (screening papers)

Goal: quickly decide if a paper is relevant. 2–5 minutes per paper.

**Reading order**:
1. **Title** — relevant?
2. **Abstract** — what specifically do they do?
3. **Section headings** — skim structure only
4. **Conclusion** — what's the actual contribution?
5. **Glance at references** — are there papers you already know? Familiar names = familiar territory

**Decision gate — the 5 Cs** (Keshav 2007): after 5 minutes, answer these before continuing:
1. **Category** — what type? New method, measurement study, survey, system description?
2. **Context** — which papers does it relate to? What theoretical basis?
3. **Correctness** — do the assumptions appear valid?
4. **Contributions** — what are the main claims?
5. **Clarity** — is it well written enough to be worth reading?

If you can't answer 3 of 5 after the first pass → stop. The paper either isn't relevant or isn't ready to be read yet.

**Decision**: read in full (Mode 1 or 2), save for later, or discard.

**Extract** (if keeping): one-line summary, how it relates to your topic, which references to follow.

---

## Mode 4: Tech article / blog post

Goal: extract practical knowledge you can apply.

**Reading order**:
1. **Skim headers** — is this the right article?
2. **Code blocks** — what are they actually showing?
3. **Key paragraphs around code** — the WHY behind the HOW
4. **Comments and discussion** (if available) — corrections, caveats, alternatives

**Extract**: key takeaway, applicable to what in your work, code/commands to keep, source reliability (who wrote this? do they have credibility on this topic?).

**Watch for**: outdated information (check the date), oversimplification, untested claims. Blog posts are not peer-reviewed — verify critical claims against docs or papers.

---

## Mode 5: Critical review

Goal: evaluate a paper's claims rigorously.

**Reading order**: full paper, then:
1. **Claims** — list every claim made (explicitly and implicitly)
2. **Evidence** — what evidence supports each claim?
3. **Methodology** — is the experimental setup sound? Controls? Statistical significance?
4. **Baselines** — are they fair? Up to date? Or are they comparing against weak baselines?
5. **Limitations (written and unwritten)** — what do they NOT test? What assumptions could break?

**Extract**: strengths, weaknesses, questions for authors, overall assessment.

**Red flags**:
- Results that are only marginally better than baselines
- Missing error bars or confidence intervals
- Comparisons against outdated baselines
- Claims that go far beyond what the experiments show
- No ablation studies (you can't tell what's actually working)

---

## General principles

- **Read with a question.** "What am I trying to learn from this?" before you start. Without a question, reading is passive and retention is low.
- **Write while reading.** Notes taken during reading are 5× more useful than notes taken afterward. Use the templates in [note-templates.md](note-templates.md).
- **It's OK to stop.** If a paper isn't relevant after 5 minutes of screening, stop. You don't owe every paper a full read.
- **Re-read is normal.** Understanding a dense paper often takes 2–3 passes. First pass for structure, second for details, third for connections to your work.
