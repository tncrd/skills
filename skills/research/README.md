# Research Skills

A curated set of research skills for literature search, ideation, and field mapping. Zero dependencies. Markdown only.

## What's included

**3 skills** that form a pipeline:

| Skill | Purpose | When to use |
|-------|---------|-------------|
| `research` | Literature search, paper reading, note-taking | Reading one paper or finding sources |
| `research-ideation` | Hypothesis generation from structured frameworks | Stuck on ideas, need new angles |
| `research-review` | Systematic field mapping, bibliography, gap analysis | Surveying an entire area |

**Reference files** loaded on-demand:

| Skill | References |
|-------|-----------|
| `research` | `search-strategies.md`, `reading-strategies.md`, `note-templates.md`, `synthesis-methods.md` |
| `research-ideation` | `frameworks.md`, `idea-evaluation.md` |
| `research-review` | `gap-analysis.md`, `review-process.md` |

## The pipeline

```
"Map the state of the art in X"
            │
            ▼
    ┌─── research ────┐
    │  Find + read    │  → searches APIs, reads papers, takes structured notes
    │  papers         │  → never generates citations from memory
    └────────┬────────┘
             │
             ▼
    ┌─ research-ideation ─┐
    │  Generate           │  → 10 frameworks: analogy, constraint, gap-first...
    │  hypotheses         │  → produces testable research directions
    └────────┬────────────┘
             │
             ▼
    ┌─ research-review ───┐
    │  Map the field      │  → systematic coverage, structured bibliography
    │  Find gaps          │  → produces _survey.md + literature/
    └─────────────────────┘
```

## Usage

**Read a single paper:**
```
> Note this paper: arxiv.org/abs/2401.xxxxx

Agent triggers research → fetches via papers.py → structured notes
```

**Generate research ideas:**
```
> I'm stuck on what to try next for X

Agent triggers research-ideation → picks framework → produces hypotheses
```

**Map a field:**
```
> What's the state of the art in efficient attention mechanisms?

Agent triggers research-review → systematic search → bibliography + gaps
```

## Structure

```
research/
├── SKILL.md
└── reference/
    ├── search-strategies.md
    ├── reading-strategies.md
    ├── note-templates.md
    └── synthesis-methods.md
research-ideation/
├── SKILL.md
└── reference/
    ├── frameworks.md
    └── idea-evaluation.md
research-review/
├── SKILL.md
└── reference/
    ├── gap-analysis.md
    └── review-process.md
```

## Inspiration

Inspired by [Orchestra AI Research Skills](https://github.com/Orchestra-Research/AI-research-SKILLs).
