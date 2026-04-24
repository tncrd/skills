# Review Process

Step-by-step guide for conducting a systematic literature review. Not every review needs every step — scale to your needs.

---

## Step 1: Scope

Before searching, define boundaries. Without scope, reviews expand indefinitely.

**Write a scoping statement:**
```
I want to understand [TOPIC] in the context of [APPLICATION/DOMAIN].
Specifically: [SPECIFIC QUESTION].
Boundaries: published after [YEAR], focused on [CONSTRAINT].
Not interested in: [EXCLUSIONS].
```

**Example**: "I want to understand reward modeling for LLM alignment. Specifically: how do different reward model architectures affect policy optimization stability? Published after 2022. Not interested in: pure theoretical analysis without experiments."

**Output**: a 3–5 sentence scope statement saved at the top of `_survey.md`.

---

## Step 2: Systematic search

Use `papers.py` + the search strategies from the research skill.

**Phase 1 — Keyword search:**
```bash
python3 papers.py search "reward modeling LLM alignment"
python3 papers.py search "reward model architecture RLHF"
python3 papers.py search "preference optimization stability"
```

Try 3–5 keyword variations. Collect all results, deduplicate by title.

**Phase 2 — Snowball from best results:**
```bash
python3 papers.py citations <best_paper_id>     # who built on this?
python3 papers.py references <best_paper_id>     # what's this built on?
python3 papers.py related <best_paper_id>         # what's similar?
```

**Phase 3 — Author search:**
Identify the 2–3 most active researchers from Phase 1. Search their recent work — they may have newer papers not yet well-cited.

**Stopping criterion**: when new searches keep returning papers you've already seen, you have good coverage.

---

## Step 3: Screen

Triage all collected papers. Use reading Mode 3 (Survey) from reading-strategies.md.

| Category | Action | Time per paper |
|----------|--------|---------------|
| **A — Core** | Full read (Mode 1 or 2) | 30–60 min |
| **B — Relevant** | Quick read, note key result | 10–15 min |
| **C — Peripheral** | Abstract only, maybe later | 2 min |
| **D — Irrelevant** | Discard | 30 sec |

Typical distribution for a focused review: 20% A, 30% B, 20% C, 30% D.

---

## Step 4: Extract

Read category A and B papers using appropriate reading mode. Create a note per paper using the templates from note-templates.md.

**After every 3–5 papers**, update `_survey.md`:
- Add to reading log
- Update "Current understanding" if your view changed
- Update "Key approaches" if you found a new paradigm
- Add to comparison table if applicable

Don't wait until you've read everything to start writing _survey.md. Write as you go — it forces you to process what you're reading, not just accumulate.

---

## Step 5: Synthesize

After reading all A papers and most B papers, do a synthesis pass:

1. **Re-read** _survey.md from top to bottom
2. **Identify patterns**: convergence, contradiction, diminishing returns, gaps (see synthesis-methods.md)
3. **Rewrite** "Current understanding" as a coherent narrative, not a paper-by-paper summary
4. **Build** or update comparison tables
5. **Write** "Open questions" based on what you've learned

**The transformation**: from "Paper A does X, Paper B does Y" → "There are two main approaches to this problem. Approach 1 (A, C, E) works by... Approach 2 (B, D) works by... The key difference is..."

---

## Step 6: Gaps → Ideas

This is where review meets ideation. Read [gap-analysis.md](gap-analysis.md) for the detailed process.

Quick version:
1. Look at the comparison table. Any empty cells?
2. Look at "Open questions" in _survey.md. Any testable?
3. Look at contradictions. Any resolvable?
4. For each promising gap → create an idea file in `ideas/` (owned by research-ideation skill)

---

## Review maintenance

A review doesn't end — it evolves. Periodically:

- **Monthly**: search for new papers on the same keywords. Add to _survey.md if relevant.
- **After experiments**: update "What works and what doesn't" with your own results.
- **Before writing**: re-read _survey.md to refresh context. Update if stale.
