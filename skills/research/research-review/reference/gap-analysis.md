# Gap Analysis

How to systematically identify what's missing in a field and assess whether the gaps are worth pursuing.

---

## Finding gaps

### 1. Comparison table analysis

Look at your comparison tables (from the review). Gaps appear as:
- **Empty cells**: combinations not yet tried (method × dataset, technique × domain)
- **Missing baselines**: strong simple approaches nobody compared against
- **Missing scales**: only tested at one scale (small or large, never both)
- **Missing modalities**: only tested on text, or only images, never both

### 2. Contradiction analysis

From your _survey.md, look for:
- Papers that disagree on a factual claim → the resolution is a paper
- Papers using different definitions of the same term → clarification is a contribution
- Papers showing opposite trends at different scales → the transition point is interesting

### 3. Future work mining

Collect "future work" mentions from your A-category papers:
- Group by theme (many papers suggesting the same thing = hot area)
- Check if anyone has done it since (forward snowball the paper)
- Prioritize suggestions from highly cited papers

### 4. Assumption questioning

Every paper makes assumptions (stated and unstated):
- "We assume i.i.d. data" → what happens without it?
- "We use a pretrained model" → what if training from scratch?
- "We evaluate on English" → what about other languages?
- "We use [standard dataset]" → is that dataset actually good?

The most impactful gaps come from questioning assumptions everyone takes for granted.

### 5. Method combination

List the top methods in your comparison table. Which combinations haven't been tried?
- Method A's training procedure + Method B's architecture?
- Method C's data augmentation + Method A's objective?

Not all combinations are meaningful — filter with the feasibility and impact criteria from idea-evaluation.md.

---

## Validating gaps

A gap exists for one of three reasons. You MUST determine which before investing time:

| Reason | What to do |
|--------|-----------|
| **Nobody thought of it** | Rare. Verify by thorough search. If confirmed, this is high-value. |
| **Someone tried, it didn't work** | Check workshop papers, rejected paper discussions, negative result venues. If you find evidence, you need a NEW approach, not just the same attempt. |
| **Data/compute doesn't exist** | Was true before, may not be now. Check if new datasets, models, or hardware have changed the feasibility. |

**How to check reason 2** (hardest to find):
- Search for workshop papers (less competitive, more preliminary results)
- Check paper discussions on OpenReview (reviews sometimes mention failed attempts)
- Look at GitHub issues in related repositories
- Ask in community channels (Twitter/X ML, relevant Discord/Slack)

---

## Positioning your contribution

Once you've identified a gap, frame it:

### The contribution statement

```
Despite progress in [FIELD], no existing work addresses [GAP].
This matters because [WHY].
We propose [WHAT], which [HOW IT FILLS THE GAP].
```

### Types of contributions

| Type | Example | Typical venue reaction |
|------|---------|----------------------|
| New method | "We propose X that solves Y" | Strong if results are convincing |
| New finding | "We show that X actually causes Y" | Strong if evidence is rigorous |
| Negative result | "Contrary to belief, X doesn't work because Y" | Undervalued but important |
| Benchmark/dataset | "We create X to evaluate Y" | Strong if it fills a real need |
| Unification | "Methods A, B, C are all special cases of X" | Strong if the framework generates new predictions |
| Scaling study | "We show X holds/breaks at scale Y" | Increasingly valued |

---

## From gap to idea

For each promising gap:

1. Write a one-sentence hypothesis
2. Score with the 4-dimension filter from idea-evaluation.md
3. If it passes → create an idea file in `ideas/`
4. If it needs more evidence → add to _survey.md's "Open questions" and keep reading

Not every gap becomes an idea. Gaps inform your understanding of the field even when you don't pursue them.
