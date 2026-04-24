---
name: tcls-design
description: "Frontend design system, visual guidelines, and motion graphics. Use this skill whenever the user asks to build, style, or improve any UI — pages, components, landing pages, dashboards, blogs, apps — or mentions typography, colors, layout, spacing, animations, motion graphics, or design quality. Also use when adding or implementing any new feature in an existing app (forms, inputs, modals, menus, tags, filters, lists, buttons) — any feature that involves UI needs design guidance even if the request sounds purely functional. Also use for SVG animation, scroll-driven effects, page transitions, or visual choreography. Invoke when the user says things like 'make it look better', 'it feels off', 'too generic', 'add some personality', 'animate this', 'make it move', 'add X to my app', 'I need a form for X', 'implement X feature'."
---

# Design

Guidelines for distinctive, production-grade frontend interfaces and motion graphics that avoid generic "AI output" aesthetics. Combines expert design principles with curated data (font pairings, industry palettes, landing patterns, motion specs).

## Project conventions

All skill-generated artifacts go in `_design/` at the project root:

```
_design/
├── .design-brief.md     ← produced by design-shape (commit this)
├── audits/              ← produced by design-audit (gitignore)
└── docs/                ← component documentation (optional)
```

HTML preview files always go in `_previews/` (gitignore, delete before ship).

Suggest adding to `.gitignore`:
```
_design/audits/
_previews/
```

The design brief (`_design/.design-brief.md`) should be committed — it’s the project’s design memory.

1. **Shape** → run `design-shape` to produce a design brief before writing code
2. **Build** → use this skill with the relevant references
3. **Audit** → run `design-audit` to verify quality before shipping
4. **Polish** → run `design-polish` for the final pre-ship pass

For quick changes or small components, skip to step 2.

## Context first

Good design decisions require knowing who this is for and what it should feel like. Before making visual choices, establish:

- **Audience** — who uses this, in what context, what's their state of mind?
- **Tone** — 3 concrete words (not "modern" — try "warm and dense and opinionated", "calm and clinical", "fast and irreverent")
- **Theme** — light or dark? Derive from context. A hospital portal → light. An SRE dashboard at night → dark. Don't default.

If `.design-brief.md`, `_design/.design-brief.md`, `.impeccable.md`, or an `AGENTS.md` with a `## Design Context` section exists, read it first — especially at the start of a new conversation on an existing project.

If context is unclear, ask before proceeding.

## Reference routing

Read only what the current task needs. Never load everything at once.

| Task | Read |
|------|------|
| Choosing fonts | [typography.md](reference/typography.md) + [font-pairings.md](reference/font-pairings.md) |
| Choosing colors / palette | [color.md](reference/color.md) + [palettes.md](reference/palettes.md) |
| Layout, spacing, grids, depth | [spatial.md](reference/spatial.md) |
| UI transitions, easing, timing | [motion.md](reference/motion.md) |
| Motion graphics, SVG animation, scroll-driven, Lottie, choreography | [motion.md](reference/motion.md) |
| Forms, focus, loading, empty/error states | [interaction-design.md](reference/interaction-design.md) |
| Responsive / mobile / touch | [responsive-design.md](reference/responsive-design.md) |
| Labels, error messages, microcopy | [ux-writing.md](reference/ux-writing.md) |
| Landing page structure | [patterns.md](reference/patterns.md) |
| UX review / audit | [ux-guidelines.md](reference/ux-guidelines.md) |
| Full page / component | typography.md + color.md + spatial.md first. Pull others as needed. |

---

## Typography

Typographic hierarchy communicates importance. Without contrast between levels, everything competes equally.

- Modular scale, ratio ≥ 1.25. Sizes too close together create muddy hierarchy.
- Cap line length at 65–75ch. Increase line-height on dark backgrounds (+0.05–0.1).
- App UI: fixed `rem` scales. Marketing pages: fluid `clamp()` on headings.

Before naming any font, follow the selection process in [typography.md](reference/typography.md) — it prevents reaching for training-data defaults that make output look generic.

## Color

Use OKLCH for perceptual uniformity. Tint neutrals toward brand hue. 60-30-10 by visual weight.

Gray text on colored backgrounds looks washed out — use a shade of that background color. See [color.md](reference/color.md) for the full palette construction guide and [palettes.md](reference/palettes.md) for 50 industry starting points.

## Spacing

Spacing is a design material. Identical spacing everywhere produces monotonous rhythm. Vary intentionally: tight for grouping, generous for separation.

4pt scale. Use `gap`. See [spatial.md](reference/spatial.md) for Flex vs Grid guidance, elevation system, and optical adjustments.

## Motion

Animation serves feedback, continuity, and narrative. [motion.md](reference/motion.md) covers everything from button transitions to scroll-driven choreography, SVG animation, spring physics, Lottie, and video-ready motion specs.

---

## The AI slop test

Before delivering: if you showed this to someone and said "an AI made this", would they immediately believe it?

The most recognizable tells:
- `border-left: 3–4px solid [color]` as card accent
- `background-clip: text` + gradient
- Glassmorphism used decoratively everywhere
- Cards nested inside cards
- Identical card grid: rounded-square icon + heading + text, repeated
- Hero metric layout: big number + small label + stats + gradient
- Purple-to-blue or cyan-on-dark palette
- Emojis as icons instead of SVG
- Bounce/elastic easing
- Default fonts (Inter, Roboto, system) with no intentional choice
