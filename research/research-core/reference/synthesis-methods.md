# Synthesis Methods

How to connect sources, build understanding across papers, and produce useful synthesis artifacts.

---

## The _survey.md file

A living document that evolves as you read more. Not a literature review — it's your current understanding of the field, written for yourself (and for the model as context).

### Structure

```markdown
# Survey: [Topic]
*Last updated: 2026-04-20*

## Current understanding
[What do you know right now? What's the consensus? Write in prose, not bullet points.
This section should read like the "Background" section of a paper you'd write.]

## Key approaches
[The main methods/paradigms in this space. Group by approach, not by paper.
"There are three main approaches to X: A, B, and C. A does... B does... C does..."]

## What works and what doesn't
[Empirical patterns across papers. "Method X consistently outperforms Y on Z."
"Approach A works at small scale but breaks at large scale."]

## Open questions
[What hasn't been answered? What contradictions exist? Where do papers disagree?]

## Connections to my work
[How does this field relate to what you're doing? What can you borrow?]

## Reading log
| Paper | Date read | Key takeaway |
|-------|-----------|-------------|
| Shao2024 | 2026-04-15 | GRPO eliminates the need for a critic model |
| Schulman2017 | 2026-04-16 | PPO is the baseline to beat |
```

### How to maintain it

- **After every paper**: add to reading log, update "Current understanding" if it changed your view
- **After every 5 papers**: rewrite "Key approaches" and "What works" — patterns should be emerging
- **When stuck**: re-read _survey.md before searching for more papers. Often you already have what you need.
- **Quality test**: could someone unfamiliar with your project read _survey.md and understand the field in 10 minutes? If not, it's too thin or too disorganized.

---

## Comparison tables

When you've read 3+ papers on the same topic, a comparison table crystallizes patterns faster than prose.

Build it in a `compare-*.md` file (see note-templates.md). Update it as you read more papers. The table is the artifact — prose observations below it explain what the patterns mean.

**What to compare depends on the field:**

| Research type | Useful columns |
|---------------|---------------|
| Method comparison | Method, dataset, metric, result, compute cost, key innovation |
| Architecture survey | Model, params, layers, attention type, training data, FLOPS |
| Training approaches | Algorithm, reward model, data requirements, stability, scaling behavior |
| Tool comparison | Tool, language, features, community, last update, license |

---

## Synthesis patterns

### Pattern: convergence
Multiple papers independently arrive at similar conclusions from different angles. This is strong evidence. Note it explicitly: "Papers A, B, and C all find that X, despite using different methods/datasets."

### Pattern: contradiction
Two papers claim opposite things. This is usually the most interesting finding. Investigate: different datasets? Different scales? Different definitions of the same term? The resolution is often a paper waiting to be written.

### Pattern: diminishing returns
Each new paper in a line of work gets smaller improvements. The paradigm may be approaching its limits. Look for: papers that break out of the paradigm entirely.

### Pattern: gap
Something obvious that nobody has tried. Check three times before getting excited — it's usually not tried because (a) it doesn't work, (b) someone tried and didn't publish negative results, or (c) the data/compute doesn't exist. But sometimes it's genuinely unexplored.

### Pattern: wrong baseline
Papers in a subfield keep comparing against the same weak baseline. If you can show that a simple, strong baseline beats the recent "advances", that's a valuable contribution.

---

## From synthesis to output

- **For a blog post**: _survey.md's "Current understanding" + "Key approaches" is your outline. Add your voice and examples.
- **For a paper's related work section**: _survey.md's "Key approaches" grouped by paradigm, with comparison tables as evidence.
- **For an experiment**: _survey.md's "Open questions" + ideas/ folder. What hasn't been tested?
- **For a talk or presentation**: _survey.md's "Current understanding" simplified to 3 key points.
