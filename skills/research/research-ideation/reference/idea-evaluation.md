# Idea Evaluation

How to filter ideas from "interesting" to "worth pursuing." Not every good idea is worth the time investment.

---

## The 4-dimension filter

Score each idea 1–5 on four dimensions:

| Dimension | Question | 1 (low) | 5 (high) |
|-----------|----------|---------|----------|
| **Novelty** | Has this been done? | Incremental improvement on existing work | No one has tried this |
| **Feasibility** | Can I actually do this? | Requires resources I don't have | I can start this week |
| **Impact** | Would people care? | Niche corner of a subfield | Changes how people think about X |
| **Testability** | Can I measure if it works? | Vague, hard to evaluate | Clear metric, clear experiment |

**Minimum threshold**: any idea below 2 on any dimension needs either revision or parking.

**Sweet spot**: Novelty ≥ 3, Feasibility ≥ 3, Impact ≥ 3, Testability ≥ 4. Testability is the most important — untestable ideas waste the most time.

---

## Red flags

**Park the idea if**:
- You can't state the hypothesis in one sentence
- The evaluation metric is unclear or subjective
- Success requires multiple things to work simultaneously (high coupling)
- The idea requires a dataset that doesn't exist and would take months to create
- You can't explain why it would work (not just what you'd try, but WHY)

**Don't park the idea just because**:
- It's simple (simple ideas that work are the best papers)
- It's been "kind of" tried (partial overlap ≠ same idea)
- You're not sure it'll work (nobody is — that's research)

---

## Effort estimation

Before committing, estimate the minimum viable experiment:

| Question | Answer |
|----------|--------|
| What's the simplest version that tests the hypothesis? | |
| How long to implement? (hours, not weeks) | |
| What compute do I need? | |
| What data do I need? | |
| What's the baseline? | |
| How do I know if it worked? | |

If the minimum viable experiment takes more than 2 weeks, simplify. Either reduce scope, find a proxy task, or use smaller scale.

---

## Comparison: when you have multiple ideas

Rank ideas on a 2×2:

```
                    High Impact
                        │
         EXPLORE        │        DO THIS
     (high risk,        │     (high impact,
      high reward)      │      feasible)
                        │
  ──────────────────────┼──────────────────
                        │
         PARK           │        QUICK WIN
     (low impact,       │     (low risk,
      hard to do)       │      easy to test)
                        │
                    Low Impact
        Hard ──────────────────── Easy
```

**Do first**: high impact + feasible. **Quick wins**: do if they take < 1 day — they build momentum. **Explore**: only if you have runway and risk tolerance. **Park**: revisit when circumstances change.

---

## Status tracking

When ideas accumulate, periodically review:

1. **Active ideas** (exploring + testing): are you spread too thin? Max 2–3 active at a time.
2. **Parked ideas**: any that new knowledge has made more feasible or more interesting?
3. **Abandoned ideas**: any that deserve reconsideration given new results?
4. **Published ideas**: are there follow-ups?

Update the YAML frontmatter `status` and `updated` fields in each idea file when evidence changes.
