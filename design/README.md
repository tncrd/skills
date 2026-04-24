# Design Skills

A curated set of design skills for building distinctive UI, motion graphics, and web experiences. Zero dependencies. Markdown only.

## What's included

**4 skills** that form a pipeline:

| Skill | Purpose | When to use |
|-------|---------|-------------|
| `design-shape` | Discovery interview → design brief | Before any significant UI work |
| `design` | Core principles + reference routing | During implementation |
| `design-audit` | Quality check, scored /20 with P0–P3 issues | After implementation, before shipping |
| `design-polish` | Final pre-ship checklist | Last step before deploy |

**11 reference files** loaded on-demand (never all at once):

| Reference | What's in it |
|-----------|-------------|
| `typography.md` | Type scales, vertical rhythm, font selection process, OpenType, web font loading |
| `font-pairings.md` | 40 curated pairings with CSS imports, organized by mood |
| `color.md` | OKLCH guide, step-by-step palette construction, dark/light reasoning |
| `palettes.md` | 50 industry-specific palettes (WCAG-verified accents) |
| `spatial.md` | Flex vs Grid, spacing system, elevation, optical adjustments, composition |
| `motion.md` | UI transitions, choreography, scroll-driven, SVG animation, Lottie, spring physics, video specs |
| `interaction-design.md` | Progressive disclosure, forms, focus management, loading/empty/error states |
| `responsive-design.md` | Mobile-first, container queries, fluid layouts, touch targets |
| `ux-writing.md` | Button labels, error messages, empty states, microcopy |
| `ux-guidelines.md` | 50 highest-impact UX rules with code examples |
| `patterns.md` | Landing page patterns by industry with section structure and CTA strategy |

## The pipeline

```
"I want to build a landing page for my dev tool"
            │
            ▼
    ┌─ design-shape ─┐
    │  Discovery      │  → asks about audience, tone, motion, constraints
    │  interview      │  → produces .design-brief.md
    └────────┬────────┘
             │
             ▼
    ┌─── design ──────┐
    │  Build with      │  → reads only the references needed
    │  references      │  → typography + color + spatial for a page
    └────────┬────────┘  → + motion if animations needed
             │
             ▼
    ┌─ design-audit ──┐
    │  Score /20       │  → 5 dimensions: slop, a11y, type/color, layout, motion
    │  P0–P3 issues   │  → prioritized fix list
    └────────┬────────┘
             │
             ▼
    ┌─ design-polish ─┐
    │  Final pass      │  → alignment, states, transitions, edge cases
    │  Checklist       │  → code hygiene, performance, a11y
    └─────────────────┘
```

## Usage

**New page or component** — full loop:
```
> Design a blog post layout for my Astro site

Agent triggers design-shape → asks 3-5 questions → writes .design-brief.md
Agent triggers design → reads brief + typography + color + spatial → builds it

> Audit this

Agent triggers design-audit → scores /20 → lists issues

> Fix the P0s and P1s

Agent fixes → you review

> Polish and ship

Agent triggers design-polish → runs checklist → done
```

**Quick change** — skip shape, go straight to build:
```
> Make the code blocks look better

Agent triggers design → reads typography + color → fixes it
```

**Something feels off** — start with audit:
```
> Something feels off about this page

Agent triggers design-audit → finds issues → you decide what to fix
```

**The feedback cycle:**
```
         ┌──────────────────────────────────┐
         │                                  │
         ▼                                  │
    ┌─ SHAPE ─┐   new feature?              │
    └────┬────┘                             │
         ▼                                  │
    ┌─ BUILD ─┐   agent loads refs          │
    └────┬────┘                             │
         ▼                                  │
    ┌─ AUDIT ─┐   score /20                 │
    └────┬────┘                             │
         │                                  │
         ├── score < 14 ── fix + re-audit ──┘
         │
         ▼  score ≥ 14
    ┌─ POLISH ┐   checklist
    └────┬────┘
         ▼
       SHIP
```

## Context management

The core skill loads ~920 tokens. Each reference file loads 500–1700 tokens. The routing table in `SKILL.md` tells the agent which references to read based on the task:

| Task | Tokens loaded |
|------|--------------|
| Choose a font | ~2200 (core + typography + pairings) |
| Choose a palette | ~2100 (core + color + palettes) |
| Animate a component | ~2600 (core + motion) |
| Build a full page | ~3400 (core + typography + color + spatial) |
| Everything at once | ~14700 (never necessary) |

## Structure

```
design/
├── SKILL.md                     core: routing + principles
└── reference/
    ├── typography.md
    ├── font-pairings.md
    ├── color.md
    ├── palettes.md
    ├── spatial.md
    ├── motion.md
    ├── interaction-design.md
    ├── responsive-design.md
    ├── ux-writing.md
    ├── ux-guidelines.md
    └── patterns.md
```

## Inspiration

Adapted from [Impeccable](https://github.com/pbakaus/impeccable) (Apache 2.0) and [Anthropic's frontend-design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design). Font pairings, palettes, UX guidelines, and landing patterns inspired by [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT).
