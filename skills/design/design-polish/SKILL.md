---
name: tcls:design-polish
description: "Final quality pass before shipping. Catches alignment, spacing, consistency, missing states, and micro-detail issues that separate good from great. Use when the user says 'polish this', 'finishing touches', 'pre-launch review', 'almost done', 'something looks off', or wants to go from good to great. Run this AFTER design-audit — audit finds issues, polish fixes the small stuff."
---

# Design Polish

The last pass before shipping. Polish is not about redesigning — it's about precision. Every pixel, every state, every transition examined. The difference between "good enough" and "this feels intentional".

**Prerequisite**: the feature must be functionally complete. Don't polish incomplete work.

---

## 1. Find the design system

Before polishing, understand what you're polishing toward:
- Search for design tokens, CSS variables, component libraries
- Note the spacing scale, color tokens, typography styles, shadow system
- Identify where the feature drifts from the system: hard-coded values that should be tokens, custom components that duplicate shared ones, spacing that doesn't match the scale

If a design system exists, polish aligns toward it. If none exists, polish against the conventions visible in the codebase.

---

## 2. Run the checklist

Go through systematically. Don't skip sections.

### Alignment and spacing
- [ ] All elements align to the spacing scale (no arbitrary 13px gaps)
- [ ] Spacing varies to create hierarchy (not identical everywhere)
- [ ] Responsive: spacing and alignment work at every breakpoint
- [ ] Optical adjustments where needed (icons, play buttons)

### Typography
- [ ] Same roles use same sizes/weights throughout
- [ ] Line length ≤ 75ch on body text
- [ ] No widows (single word on last line of a paragraph) in key headings
- [ ] Font loading doesn't cause layout shift

### Color and theme
- [ ] All colors use design tokens (no random hex values)
- [ ] No gray text on colored backgrounds
- [ ] No pure `#000` or `#fff` on large surfaces
- [ ] Dark mode (if applicable) has verified contrast, not just inverted
- [ ] Contrast ratios meet WCAG AA

### Interaction states
Every interactive element must have:
- [ ] Default, hover, focus, active, disabled states
- [ ] Loading state for async actions
- [ ] Error and success states where applicable
- [ ] Focus indicators visible and meeting 3:1 contrast

### Transitions
- [ ] All state changes animate smoothly (150–300ms)
- [ ] Only `transform` and `opacity` animated
- [ ] Easing is intentional (ease-out-quart, not `ease` default)
- [ ] `prefers-reduced-motion` respected
- [ ] No jank on mid-range devices

### Content and copy
- [ ] Consistent terminology (same things called same names)
- [ ] Consistent capitalization (Title Case or Sentence case, not mixed)
- [ ] No typos or grammar issues
- [ ] Error messages are helpful (what happened + what to do)
- [ ] Empty states are friendly (not blank screens)

### Icons and images
- [ ] All icons from same family or matching style
- [ ] Icons optically aligned with adjacent text
- [ ] All images have descriptive `alt` text
- [ ] Images don't cause layout shift (width/height or aspect-ratio set)
- [ ] Retina: 2x assets for high-DPI screens

### Forms
- [ ] Every input has a visible label
- [ ] Required fields clearly indicated
- [ ] Tab order is logical
- [ ] Errors appear near the field that caused them
- [ ] Form content preserved on error (never wiped)

### Edge cases
- [ ] Very long text doesn't break layout (truncate or wrap)
- [ ] Very short text doesn't leave awkward gaps
- [ ] Zero items shows helpful empty state
- [ ] Many items (100+) doesn't break performance
- [ ] Offline state handled (if applicable)

### Performance
- [ ] No layout shift on load (CLS)
- [ ] Images lazy-loaded below fold
- [ ] No console errors or warnings
- [ ] Smooth interactions (no jank)

### Code hygiene
- [ ] No `console.log` in production code
- [ ] No commented-out code
- [ ] No unused imports
- [ ] No TypeScript `any` or suppressed errors
- [ ] Custom implementations replaced with design system components where available

---

## 3. Verify

- **Use it yourself.** Actually click through every flow.
- **Test on a real phone.** Not just DevTools emulation.
- **Fresh eyes.** Show it to someone who hasn't seen it.
- **Squint test.** Blur your vision — is hierarchy still clear?

---

## 4. Clean up

After polishing:
- Delete `_previews/` — HTML preview files are dev artifacts, not shipping code
- Delete any orphaned styles, components, or files made obsolete
- Consolidate new values into the token system if they should be reusable
- Check for duplication introduced during polish

Polish is done when you can look at every screen, every state, every breakpoint and nothing feels accidental.
