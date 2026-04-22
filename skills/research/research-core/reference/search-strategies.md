# Search Strategies

Where to search, how to search, and how to follow the citation trail.

---

## Where to search what

| Looking for | Source | Tool |
|-------------|--------|------|
| ML/AI papers by topic | Semantic Scholar | `papers.py search "query"` |
| Specific arXiv paper | arXiv | `papers.py fetch 2402.03300` |
| Recent preprints (last months) | arXiv | `papers.py search "query"` with date filter |
| Who cites this paper | Semantic Scholar | `papers.py citations <id>` |
| What this paper cites | Semantic Scholar | `papers.py references <id>` |
| Related papers | Semantic Scholar | `papers.py related <id>` |
| BibTeX entry | CrossRef / Semantic Scholar | `papers.py bibtex <id>` |
| Blog posts, tech articles | Web search | Agent's web search tools |
| Documentation, API reference | Official docs | Direct URL fetch |
| Code implementations | GitHub | GitHub search / repo links from paper |

---

## Snowball method

The most reliable way to build comprehensive coverage of a topic. Start from one good paper and expand outward.

### Backward snowball (this paper's references)
```
papers.py references <id>  →  which of these are relevant?  →  read those  →  repeat
```
Finds the foundations — what the field is built on. Stop when you keep seeing the same papers.

### Forward snowball (who cites this paper)
```
papers.py citations <id>  →  which of these are relevant?  →  read those  →  repeat
```
Finds the follow-ups — what happened after this paper. Sort by date for recent work, by citation count for influential work.

### Combined strategy
1. Start with 1–3 seed papers (the most relevant you know)
2. Backward snowball each → find the foundations (usually 5–10 key papers)
3. Forward snowball the seed papers → find recent follow-ups
4. Forward snowball the most-cited foundations → find work you missed
5. Stop when new papers keep citing papers you've already read

---

## Keyword strategy

Academic search is sensitive to terminology. The same concept has different names across communities:

| If you search | Also try |
|---------------|----------|
| RLHF | "reward modeling", "preference optimization", "alignment from human feedback" |
| Fine-tuning | "adaptation", "transfer learning", "instruction tuning" |
| Attention mechanism | "self-attention", "cross-attention", "transformer" |
| Quantization | "model compression", "low-bit inference", "weight quantization" |

**Tips**:
- Start broad, narrow with additional terms
- Use author names if you know key researchers in the area
- Check the "Keywords" section of papers you've already found — borrow their terminology
- Semantic Scholar's relevance ranking is usually good; arXiv's is chronological

---

## Screening workflow

When search returns 20–50 papers:

1. **Title scan** (30 sec each) — discard obviously irrelevant
2. **Abstract scan** (1 min each) — categorize: definitely relevant / maybe / skip
3. **Quick read** the "definitely relevant" ones (Mode 3 from reading-strategies.md)
4. **Full read** the ones that pass quick screening (Mode 1 or 2)

Don't try to read everything. A good screening funnel: 50 titles → 15 abstracts → 8 quick reads → 4 full reads. That's a productive session.

---

## Staying current

- **arXiv daily**: check relevant categories (cs.LG, cs.CL, cs.CV, etc.)
- **Semantic Scholar alerts**: set up for key authors or topics
- **Twitter/X academic ML**: many researchers post paper summaries
- **Conference proceedings**: NeurIPS, ICML, ICLR, ACL, AAAI — check accepted paper lists
- **Newsletter**: papers.cool, The Batch, ML News

Keep a "to-read" list. Not everything needs to be read immediately — but capture it so you don't lose it.
