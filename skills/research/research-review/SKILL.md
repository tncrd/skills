---
name: tcls:research-review
description: "Systematic literature review, field mapping, bibliography building, and gap analysis. Use when the user wants to map an entire research area, build a structured bibliography, find gaps in the literature, or produce a survey. Also use when the user says 'what's the state of the art in X', 'map this field', 'build a bibliography on X', or 'where are the gaps'."
---

# Research Review

Structured process for systematically mapping a research field. Produces a bibliography (`literature/`), an evolving synthesis (`_survey.md`), and identifies gaps and opportunities.

Different from `research` (read one thing, take notes) — this is the disciplined process of covering a field.

## Workflow

```
1. SCOPE    — define the question and boundaries
2. SEARCH   — systematic search + snowball
3. SCREEN   — triage papers (title → abstract → quick read)
4. EXTRACT  — read and note (using research skill templates)
5. SYNTHESIZE — write and update _survey.md
6. GAPS     — identify what's missing → feed to research-ideation
```

This is not strictly sequential — you loop between steps as understanding deepens.

## Reference routing

| Step | Read |
|------|------|
| Planning the review | [review-process.md](reference/review-process.md) |
| Identifying gaps and positioning | [gap-analysis.md](reference/gap-analysis.md) |
| Searching for papers | → `research` skill's [search-strategies.md](../research/reference/search-strategies.md) |
| Reading papers | → `research` skill's [reading-strategies.md](../research/reference/reading-strategies.md) |
| Taking notes | → `research` skill's [note-templates.md](../research/reference/note-templates.md) |
| Generating ideas from gaps | → `research-ideation` skill |

## Project structure

This skill manages the `literature/` folder and `_survey.md`:

```
project/
├── literature/
│   ├── author2024-topic.md      ← individual paper notes
│   ├── compare-methods.md       ← comparison tables
│   └── _survey.md               ← evolving synthesis (this skill owns this)
├── ideas/                        ← owned by research-ideation
└── ...
```

## _survey.md

The central synthesis artifact. Updated after every batch of papers read. Format defined in `research` skill's [synthesis-methods.md](../research/reference/synthesis-methods.md).

**Quality test**: after 15+ papers read, someone unfamiliar with your project should be able to read `_survey.md` and understand the field in 10 minutes.

## Git discipline (recommended)

```
research(scope): define review on [topic]
research(search): initial search, [N] papers found
research(read): batch [N] papers, updated _survey.md
research(gaps): gap analysis complete, [N] opportunities identified
```

Commit `_survey.md` after each reading batch. This creates a timeline of how your understanding evolved.

## Typical requests

- **"Map the field of X"** → full workflow: scope → search → screen → extract → synthesize
- **"What's the state of the art in X?"** → search + screen + quick synthesis
- **"Build a bibliography on X"** → search + screen + extract notes into `literature/`
- **"Where are the gaps in X?"** → load gap-analysis.md, analyze existing `_survey.md`
- **"Update my review with new papers"** → search recent work, screen, update `_survey.md`
