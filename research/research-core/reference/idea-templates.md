# Idea Template and Workflow

An idea file is a research proposal in progress. Its job is to answer one question before any code is written: **is this worth doing, and is it actually open?** A good idea file saves weeks of work on a covered direction. A bad one is a wishlist.

---

## Mandatory workflow order

```
1. Prior work audit   ← ALWAYS first, before writing the proposal
2. Feasibility check  ← solo GPU? model size? GPU-days?
3. Proposal           ← only for what's actually open
4. Falsification      ← concrete numbers that would kill the idea
5. Experimental plan  ← phased, week-by-week
```

**Never skip step 1.** The most common failure mode is writing a deep proposal for something that was published 6 months ago. The audit takes 30 minutes; the proposal takes hours. Do the audit first.

---

## Prior work audit (step 1)

For each proposed direction, run:

```bash
uv run .agents/skills/tcls-research/scripts/papers.py search "<direction keywords>"
uv run .agents/skills/tcls-research/scripts/papers.py fetch <arxiv_id>  # for promising hits
```

Search at least 3 angles per direction (e.g. "per-parameter sigma ES", "adaptive noise evolution strategies", "NES step size adaptation"). Record results in a table:

| Direction | Status | Blocking paper |
|---|---|---|
| A — short name | COVERED / OPEN / PARTIAL | Author year arxiv-id: one-line summary |

**COVERED** = someone has done this, published, and the paper is available.
**PARTIAL** = adjacent work exists but the specific application or combination is new.
**OPEN** = nothing found after thorough search.

Only propose OPEN or PARTIAL directions. For COVERED directions: note the paper, add it to `literature/index.md` as `unread`, move on.

---

## Feasibility check (step 2)

Answer these before writing anything else:

| Question | Answer |
|---|---|
| Solo researcher feasible? | yes / no / yes at smaller scale |
| Minimum hardware | 1× GPU model + VRAM, or N× GPUs |
| Model size for solo run | e.g. 0.5B–1.5B |
| GPU-days per ablation | rough estimate |
| Codebase to build on | link or paper |
| Result scope at solo scale | workshop / main-track / inconclusive |

If solo-GPU feasible only at a smaller model: state this explicitly. Results on 0.5B may not transfer to 7B — that is not a failure, it is a scoped contribution.

---

## YAML frontmatter

```yaml
---
type: idea
title: "Short descriptive title (method name if known)"
status: draft          # draft | active | abandoned | published
date: YYYY-MM-DD
description: "One dense sentence: what you propose and why it's open. ~25 words."
tags: [tag1, tag2, ...]
related:
  - "[[note-slug-1]]"
  - "[[note-slug-2]]"
---
```

**Rules:**
- `related` must be a YAML list with each wikilink **quoted** — `"[[slug]]"` not `[[slug]]`. Unquoted `[[` is invalid YAML (parsed as nested flow sequence).
- `tags` can use plain YAML flow sequence `[tag1, tag2]` — no wikilinks needed.
- `status: abandoned` when prior work audit kills the direction — keep the file as a record of what was checked.

---

## Full template

```markdown
---
type: idea
title: "..."
status: draft
date: YYYY-MM-DD
description: "..."
tags: [...]
related:
  - "[[...]]"
---

## Prior Work Audit (YYYY-MM-DD)

| Direction | Status | Blocking paper |
|---|---|---|
| A — ... | COVERED | Author year id: summary |
| B — ... | OPEN | — |

**Pivot**: keep B only. Drop A.

## TL;DR

One paragraph. What is broken, what you fix, what the expected result is.
No jargon without definition. Write so a smart non-specialist understands.

## Motivation

What specific failure mode or gap does this address?
Ground in at least one concrete observation (a number, a curve, a known result).
Do NOT restate the abstract of related papers — say what they fail to do.

## Background

Only the equations/concepts needed to understand the proposal.
Keep to ≤5 equations. If you need more, the proposal is too broad.

## Proposal

One section per open direction. For each:
- The core idea in one sentence
- The math (if applicable) — full equations, not prose
- Two concrete implementation variants (ablations)
- Cost estimate (memory, compute, lines of code)
- One specific risk and its mitigation

## Composition

If multiple directions: a ASCII diagram or table showing which combine cleanly.

## Feasibility

| Dimension | Assessment |
|---|---|
| Model size | ... |
| Population / batch size | ... |
| Hardware | ... |
| Compute | ... |
| Codebase | ... |
| Result scope | ... |

## Predicted Results

Table of variants vs expected metric on a specific benchmark.
Include: vanilla baseline (reproduced number), each upgrade alone, full combo.

**Falsification thresholds**: state the minimum delta that would confirm the hypothesis.
If the combo doesn't beat vanilla by ≥X pp, the idea is wrong — not "needs more tuning."

## Experimental Plan

```
   Week N — phase name (N GPU-days)
     ├── specific run 1
     └── specific run 2
```

Total compute estimate at the bottom.

## Risks and Failure Modes

Numbered list. For each: what breaks, why, mitigation.
Be honest — a risk you ignore is a surprise that kills the project.

## Open Questions

Numbered list of things you don't know yet that affect the design.
These are the first experiments to run.

## Connections

- [[note-slug]] — relationship (builds-on / competes-with / extends / uses)
- **External paper** (Author year) — relationship — one line
```

---

## When to mark a direction COVERED vs PARTIAL

**COVERED**: the paper does the same thing, on the same type of model, with the same goal. Running the experiment would reproduce their work, not extend it.

**PARTIAL**: the paper does the idea on a different domain (e.g., deep RL but not LLMs), or proposes the method without the specific application you care about, or has a key difference in mechanism. Cite it as prior work, explain the gap, and proceed.

**When in doubt**: fetch the abstract and ask "if I ran my experiment, would the result be already known?" If yes → COVERED. If there's a genuine question left → PARTIAL or OPEN.

---

## Routing

| Situation | Do this |
|---|---|
| Starting a new idea | Follow this template from step 1 |
| Idea was covered by audit | Mark `status: abandoned`, note blocking paper, add blocking paper to `literature/index.md` as `unread` |
| Idea is active / in experiment | Update `status: active`, add actual results to Predicted Results table |
| Writing a survey or connecting ideas | → use `synthesis-methods.md` |
| Need to find more related papers | → use `search-strategies.md` |
