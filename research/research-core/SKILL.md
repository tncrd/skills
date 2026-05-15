---
name: tcls-research
description: "Literature search, paper reading, note-taking, and knowledge synthesis for ML research and tech exploration. Use when the user wants to find papers, read and extract from academic or technical content, take structured notes, build a bibliography, or synthesize knowledge across sources. Also use when the user says 'note this paper', 'find papers on X', 'summarize what I know about X', 'what does this paper say', or 'search for related work'."
---

# Research

Core research methodology: how to search, read, extract, and organize knowledge. Routes to reference files by task and to `papers.py` for academic API queries.

## Citation hygiene

**Never generate a citation from memory.** AI-generated references have ~40% error rate — wrong authors, wrong years, papers that don't exist.

| Action | ✅ Correct | ❌ Wrong |
|--------|-----------|----------|
| Adding a citation | Search API → verify → format | Write from memory |
| Uncertain about a paper | Mark `[CITATION NEEDED]` | Guess |
| Can't find exact paper | Say "I couldn't verify this" | Invent similar-sounding paper |

## Paper access

**Always use `papers.py` — never download papers manually.**

| Action | ✅ Correct | ❌ Wrong |
|--------|-----------|----------|
| Read a paper | `papers.py read <id>` | `wget`, `curl`, direct URL fetch |
| Get structure | `papers.py toc <id>` | Manual PDF parsing |
| Search | `papers.py search "query"` | Web search for papers |

The script handles HTML → PDF fallback, rate limiting, math extraction, and section navigation automatically.

## Tools

Script: `.agents/skills/research/scripts/papers.py`

```bash
# Table of contents — see paper structure before reading
uv run .agents/skills/research-core/scripts/papers.py toc 2402.03300

# Read a specific section by name or number
uv run .agents/skills/research-core/scripts/papers.py section 2402.03300 "GRPO"
uv run .agents/skills/research-core/scripts/papers.py section 2402.03300 16

# Read full paper (HTML → PDF fallback)
uv run .agents/skills/research-core/scripts/papers.py read 2402.03300

# Abstract + metadata only
uv run .agents/skills/research-core/scripts/papers.py fetch 2402.03300

# Search, citations, snowball
uv run .agents/skills/research-core/scripts/papers.py search "GRPO reinforcement learning"
uv run .agents/skills/research-core/scripts/papers.py citations 2402.03300
uv run .agents/skills/research-core/scripts/papers.py references 2402.03300
uv run .agents/skills/research-core/scripts/papers.py related 2402.03300
uv run .agents/skills/research-core/scripts/papers.py bibtex 2402.03300
uv run .agents/skills/research-core/scripts/papers.py index literature/
```

**Preferred workflow** (aligned with the extraction flow):
1. `toc` — always start here, works with HTML or PDF
2. `section` — read per pass (Pass 3 → method, Pass 4 → experiments, Pass 5 → related work)
3. `read` — only when both `toc` and `section` fail entirely
4. Never use `fetch` when taking notes — it returns abstract only (~300 words)

Optional: set `SEMANTIC_SCHOLAR_API_KEY` for higher rate limits (free: https://www.semanticscholar.org/product/api#api-key-form).

## Checklists (required — create a TodoWrite task per item before proceeding)

### Before writing any note ("note this paper", "read this paper")
- [ ] Read `reference/note-templates.md` — vault note structure and conventions
- [ ] Read `literature/index.md` — check if a note already exists and absorb the style of existing entries

### After writing or updating any note (mandatory — do not skip)
- [ ] Run `papers.py index literature/ --lint` — rebuilds `literature/index.md` from YAML frontmatter and flags missing fields
- [ ] Fix any `⚠ missing` warnings before finishing (add `description:`, `tags:`, or `year:` to the note YAML as needed)

### Before searching for papers ("find papers on X", "related work")
- [ ] Read `reference/search-strategies.md` — query construction and snowballing strategies

### Before synthesizing or surveying ("summarize what I know", "write a survey")
- [ ] Read `literature/index.md` — inventory what is already in the vault
- [ ] Read `reference/synthesis-methods.md` — synthesis and comparison patterns

## Reference routing

| Situation | Read |
|-----------|------|
| Reading a paper or article | [reading-strategies.md](reference/reading-strategies.md) |
| Taking notes on what I read | [note-templates.md](reference/note-templates.md) |
| Searching for papers or resources | [search-strategies.md](reference/search-strategies.md) |
| Connecting sources, writing a survey | [synthesis-methods.md](reference/synthesis-methods.md) |
| Writing or developing a research idea | [idea-templates.md](reference/idea-templates.md) |
| Want new ideas or angles | → use `research-ideation` skill |
| Mapping an entire field systematically | → use `research-review` skill |

## Project structure

When working on a research project, expect this structure:

```
project/
├── literature/          # one .md per paper/article read
│   ├── author2024-topic.md
│   └── _survey.md       # evolving synthesis (owned by research-review)
├── ideas/               # one .md per idea (owned by research-ideation)
│   └── idea-slug.md
└── ...
```

## Typical requests

- **"Note this paper"** → `papers.py read` → extract using note strategy → save to `literature/` → `papers.py index literature/`
- **"Find papers on X"** → `papers.py search`, then summarize results
- **"What do I already have on X?"** → read `literature/index.md` first, then relevant notes
- **"Summarize what I know about X"** → read `literature/index.md` → read relevant notes → synthesize
- **"What does this paper say about Y"** → read the paper note, answer specifically
- **"Compare these approaches"** → build comparison table (see note-templates.md)
- **"Write a blog post from my research on X"** → read `_survey.md` + relevant notes, pass to `writing` skill
- **"Implement this paper's architecture"** → read the implementation note, start coding
