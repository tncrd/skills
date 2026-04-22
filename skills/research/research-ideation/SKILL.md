---
name: tcls:research-ideation
description: "Structured ideation frameworks for generating research ideas, finding novel angles, and tracking hypotheses over time. Use when the user wants new ideas, says 'I'm stuck', 'what could I try', 'find me an angle on X', 'brainstorm', 'what's novel here', or when gap analysis reveals unexplored territory. Also use to manage the ideas/ tracker."
---

# Research Ideation

Ten frameworks for moving from "vague curiosity" to "testable hypothesis." Each targets a different cognitive mode — use the routing table to pick the right one, or browse several when exploring broadly.

## Reference routing

| Situation | Read |
|-----------|------|
| Need an idea, any idea | [frameworks.md](reference/frameworks.md) — browse multiple |
| Stuck on current direction | frameworks.md → Tension Hunting or Reformulation |
| Want cross-domain insight | frameworks.md → Bisociation or Cross-Pollination |
| Have ideas, need to filter | [idea-evaluation.md](reference/idea-evaluation.md) |
| Updating ideas with new evidence | idea-evaluation.md → Status tracking section |

## Quick framework picker

| Your state | Best framework |
|------------|---------------|
| "I have no idea what to work on" | Abstraction Ladder + Gap Mining |
| "I know the field but need a fresh angle" | Bisociation + Reformulation |
| "Two things seem contradictory" | Tension Hunting |
| "I saw something interesting in another field" | Cross-Pollination + Analogy Transfer |
| "I have too many ideas, can't choose" | → use idea-evaluation.md |
| "My current approach isn't working" | Inversion + Constraint Manipulation |
| "I want to push the boundaries of X" | Boundary Exploration + Scaling |
| "I need to combine existing methods" | Combinatorial Creativity |

## Ideas tracker

This skill owns the `ideas/` folder. Each idea is one markdown file with YAML frontmatter.

### Format

```markdown
---
id: idea-slug
status: exploring | testing | parked | abandoned | published
origin: paper:author2024 | experiment:run-014 | brainstorm:2026-04-20
created: 2026-04-20
updated: 2026-04-20
tags: [topic1, topic2]
---

## [Idea title]

**Hypothesis**: [one testable sentence]

**For**:
- [evidence supporting this idea]

**Against**:
- [evidence against]

**Next step**: [concrete action]
```

### Status transitions

```
exploring → testing    (when you start running experiments)
exploring → parked     (interesting but not now)
exploring → abandoned  (evidence against, or better idea found)
testing   → published  (wrote it up: blog, paper, or internal doc)
testing   → abandoned  (experiments disprove it)
parked    → exploring  (revisiting with new context)
```

### Maintaining ideas

- **After reading a paper**: check if it provides evidence for/against any existing idea
- **After an experiment**: update the relevant idea with results
- **After ideation session**: create new idea files, evaluate with idea-evaluation.md
- **Periodically**: review parked ideas — new knowledge may make them viable

## Typical requests

- **"I need ideas for X"** → load frameworks.md, apply 2–3 relevant frameworks
- **"What could I try next?"** → review `ideas/` for exploring/parked ideas, then frameworks if none fit
- **"This is interesting but I don't know where to go"** → Tension Hunting + Abstraction Ladder
- **"Evaluate my ideas"** → load idea-evaluation.md, score each idea
- **"Update idea X with this result"** → edit the idea file, update evidence and status
