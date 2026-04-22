---
name: tcls:design-shape
description: "Plan the design of a feature or page BEFORE writing any code. Runs a focused discovery interview and produces a design brief that guides implementation. Use at the START of any significant UI work — when the user says 'I want to build X', 'design a landing page for Y', 'create a dashboard for Z', or any time design decisions need to be made before implementation begins. Also use when a design feels directionless or 'AI generic' — shaping forces the thinking that generic output skips."
---

# Design Shape

Produce a design brief through a short discovery interview. This brief becomes the single reference point for all implementation that follows — it answers the questions that, left unanswered, produce generic output.

The problem with most AI-generated UI isn't bad code — it's skipped thinking. The agent jumps straight to "here's a card grid" without asking who this is for, what it should feel like, or what would make it memorable. This skill inverts that.

**Scope**: Thinking and planning only. No code. The output is a brief that any implementation skill (or the `design` skill) can act on.

---

## Phase 1: Read before asking

Before the interview, scan what exists:
- README, docs — project purpose, stated goals
- `package.json` — tech stack, existing design libraries
- Existing components — current patterns, spacing, colors in use
- Any `.impeccable.md`, `AGENTS.md` — prior design context
- CSS variables, tokens — existing palette, font stacks

Note what you learned and what remains unclear. Don't ask questions you can answer yourself.

---

## Phase 2: Discovery interview

Ask these in conversation — not as a form dump. Adapt based on what you already know. The goal is understanding, not checklist completion.

**Purpose**
- Who specifically uses this? (Not "users" — role, context, frequency, device)
- What job are they trying to get done?
- What's their state of mind when they reach this? (Rushed? Exploring? Anxious?)

**Tone and feel**
- How should this feel in 3 concrete words? (Not "modern" — try "dense and irreverent", "calm and premium", "fast and unimpressed")
- Any references — sites, apps, products — that capture the right feel? What specifically?
- What should this explicitly NOT look like? (Anti-references are often more useful than references)

**Motion and animation**
- Should this feel static, subtly alive, or cinematically animated?
- What's the motion personality? (Snappy and precise? Fluid and organic? Playful and bouncy? Cinematic?)
- Any specific motion needs? (Page entrance, scroll effects, SVG animation, loading choreography)
- Performance budget? (Mobile-first? Complex page with many elements?)

**Constraints**
- Light or dark? Any colors that must appear or be avoided?
- Framework / tech constraints?
- Accessibility requirements beyond WCAG AA?

**Anti-goals**
- What's the biggest risk of getting this wrong aesthetically?
- Is there a "safe but boring" version that should be avoided?

---

## Phase 3: Design brief

Synthesize findings into a structured brief. Present it for confirmation before finishing.

```markdown
## Design Brief — [Feature/Page Name]

### Who and why
[Who uses this, their context, their job to be done, their state of mind]

### Tone
[3-word personality. What it should feel like. What it should NOT feel like.]

### Visual direction
[Aesthetic approach: type style, color temperature, density.
Reference the tone — derive specific visual choices from it, not from defaults.]

### Motion character
[How should this move? Static, subtly alive, or cinematically animated?
Motion personality, key moments to animate, performance constraints.]

### Layout strategy
[What gets emphasis, what's secondary, how information flows.
Describe hierarchy and rhythm, not CSS.]

### Key states
[List every state needed: default, empty, loading, error, success, edge cases.
For each: what does the user need to see and feel?]

### Content and copy
[What text, labels, empty states, errors, CTAs are needed.
Note dynamic content and realistic ranges: min/typical/max.]

### Design system notes
[Existing tokens, components, or patterns to respect or deliberately break.
Which reference files are most relevant: typography? palettes? patterns?]

### Open questions
[Anything unresolved that should be decided during implementation.]
```

At the end of the brief, add:

```markdown
### Suggested references
[List which of these are most relevant for implementation:
typography.md, font-pairings.md, color.md, palettes.md,
spatial.md, motion.md, interaction-design.md, responsive-design.md, patterns.md]
```

To suggest a font direction, consult [reference/font-pairings.md](../design/reference/font-pairings.md) for pairings that match the tone words. To suggest a color starting point, consult [reference/palettes.md](../design/reference/palettes.md) for the closest industry match. Include these as non-binding suggestions — the implementer can override.

Save the brief to `_design/.design-brief.md` at the project root (create `_design/` if needed). Update if it already exists.

After confirmation, the brief is ready. Pass it to the `design` skill for implementation, or use it to guide any other approach.

---

**Why this matters**: The brief doesn't constrain creativity — it directs it. A blank canvas produces generic output because there are infinite equally-valid choices and no reason to prefer one over another. The brief gives the implementation a specific target. "Dense and irreverent for a developer tool used at 11pm" produces completely different typography, color, and spacing choices than "calm and premium for a wellness brand used Sunday morning". Both are valid. Neither can be reached without the brief.
