---
name: tcls-design-audit
description: "Run a systematic quality audit of any UI — pages, components, designs, codebases. Scores 5 dimensions and produces a prioritized list of issues (P0–P3). Use when the user wants a design review, accessibility check, 'something feels off', pre-launch quality check, or wants to know what to fix first. Also use after implementing a design to verify quality before shipping."
---

# Design Audit

Systematic technical and aesthetic quality check. Produces a scored report with prioritized issues — not a list of opinions, but a structured diagnosis of what's broken and what needs fixing first.

Read [reference/ux-guidelines.md](../design/reference/ux-guidelines.md) during the UX dimension. For interaction-specific issues (forms, states, focus), also consult [reference/interaction-design.md](../design/reference/interaction-design.md). For mobile/responsive issues, consult [reference/responsive-design.md](../design/reference/responsive-design.md).

---

## Dimension 1 — AI Slop (check this first)

Before anything else: does this look like it was made by an AI following defaults?

Check for the most recognizable tells:
- `border-left: 3–4px solid [color]` as card accent
- Gradient text (`background-clip: text` + gradient background)
- Glassmorphism used decoratively (backdrop-blur on every card)
- Cards nested inside cards
- Identical card grid: rounded-square icon + heading + text, repeated
- Hero metric layout: big number + small label + supporting stats + gradient
- Purple-to-blue or cyan-on-dark color scheme
- Emojis as icons
- Bounce or elastic easing
- Inter / Roboto / system fonts with no intentional typographic choice

**Score 0–4**: 0 = gallery of AI tells (5+), 1 = heavy (3–4 tells), 2 = some (1–2 noticeable), 3 = mostly clean, 4 = no tells — distinctive, intentional

---

## Dimension 2 — Accessibility

- Text contrast ratios (body: ≥ 4.5:1, large text: ≥ 3:1, UI components: ≥ 3:1)
- Interactive elements have keyboard focus indicators
- Logical tab order, no keyboard traps
- Semantic HTML (headings hierarchy, landmarks, button vs div)
- Images have alt text; decorative images have `alt=""`
- Form inputs have labels (not just placeholders)
- `prefers-reduced-motion` respected

**Score 0–4**: 0 = fails WCAG A, 1 = major gaps, 2 = partial (some effort, significant gaps), 3 = WCAG AA mostly met, 4 = WCAG AA fully met

---

## Dimension 3 — Typography and Color

- Type scale is consistent (same roles use same sizes throughout)
- Line length ≤ 75ch on body text
- Gray text not used on colored backgrounds (should use a shade of that color)
- No pure `#000` or `#fff` for large areas (should be tinted)
- Color tokens used consistently (no random hard-coded values)
- Dark mode (if applicable) has verified contrast, not just inverted colors

**Score 0–4**: 0 = arbitrary, inconsistent, 1 = some effort, major drift, 2 = partial system with gaps, 3 = consistent with minor issues, 4 = intentional and systematic throughout

---

## Dimension 4 — Layout and Spacing

- Spacing follows a scale (not arbitrary values)
- Spacing varies to create hierarchy (not identical everywhere)
- Cards not nested inside cards
- Touch targets ≥ 44×44px on interactive elements
- No horizontal overflow on mobile viewports
- Container queries or media queries handle responsive behavior

**Score 0–4**: 0 = arbitrary, broken on mobile, 1 = major layout issues, 2 = functional but rough, 3 = good with minor issues, 4 = systematic, responsive, rhythmic

---

## Dimension 5 — Motion and Animation

### UI motion
- Interactive elements have all states: default, hover, focus, active, disabled, loading
- Transitions use `transform`/`opacity` only (not layout properties)
- Durations feel appropriate (not too fast/sluggish)
- No bounce or elastic easing
- `prefers-reduced-motion` respected with meaningful fallback

### Motion graphics (if applicable)
- Entrance choreography: stagger order matches visual hierarchy
- Scroll-driven effects degrade gracefully (static fallback for unsupported browsers)
- SVG animations use grouped `<g>` elements with meaningful IDs
- Lottie files optimized (< 100KB for web)
- Spring physics used for drag/repositioning interactions (not cubic-bezier)
- Motion tokens documented for cross-tool handoff
- Canvas/WebGL effects pause when off-screen

**Score 0–4**: 0 = no states, layout-animating, 1 = partial states, poor timing, 2 = main states present, gaps remain, 3 = good coverage, minor issues, 4 = all states smooth, choreography intentional, accessible

---

## Report format

### Audit scorecard

| Dimension | Score | Key finding |
|-----------|-------|-------------|
| AI Slop | ? / 4 | [worst tell or "none found"] |
| Accessibility | ? / 4 | [most critical issue] |
| Typography & Color | ? / 4 | [main issue] |
| Layout & Spacing | ? / 4 | [main issue] |
| Motion & Interaction | ? / 4 | [main issue] |
| **Total** | **? / 20** | |

**Rating**: 18–20 excellent, 14–17 good, 10–13 needs work, 6–9 poor, 0–5 critical

### Issues by severity

Tag every issue P0–P3:
- **P0 Blocking** — prevents task completion or WCAG A violation. Fix now.
- **P1 Major** — WCAG AA violation or significant UX break. Fix before release.
- **P2 Minor** — annoyance, workaround exists. Fix in next pass.
- **P3 Polish** — no real user impact. Fix if time permits.

For each issue:
- **[P?] Issue name**
- **Location** (component, file, line if known)
- **Impact** (what it does to users)
- **Fix** (specific, actionable)

### What's working

Note patterns done well — these should be preserved and replicated, not accidentally broken during fixes.

### Recommended next steps

Ordered by priority. End with: "Re-run `design-audit` after fixes to see your score improve."

### Output

Save the audit report to `_design/audits/YYYY-MM-DD-component-name.md`. Create `_design/audits/` if needed.
