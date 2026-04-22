# Spatial Design

Space is the most underused design tool. The right rhythm and hierarchy can make simple content feel polished; wrong spacing makes even good content feel amateur.

---

## Spacing system

Use a 4pt base scale: **4, 8, 12, 16, 24, 32, 48, 64, 96px**. 8pt systems are too coarse — you'll frequently need 12px between 8 and 16.

Name tokens semantically: `--space-xs`, `--space-sm`, `--space-md`, `--space-lg`, `--space-xl`. Not `--spacing-8` (which tells you nothing about when to use it).

Use `gap` instead of margins for sibling spacing. It eliminates margin collapse and the cleanup hacks that come with it.

### Vary spacing for hierarchy

Identical spacing everywhere is the #1 cause of "flat" layouts. Space communicates:
- **Tight grouping** (4–12px): "these belong together" (icon + label, input + hint text)
- **Standard separation** (16–24px): "these are siblings" (list items, form fields)
- **Section breaks** (48–96px): "this is a new thought" (between page sections)

A heading with generous space above it reads as more important than one with tight space.

---

## Flex vs Grid: when to use which

**Flexbox** for 1D layouts — anything that flows in one direction:
- Navigation bars, button groups, card contents
- Rows of items that may wrap
- Component internals (label + input + icon)
- Most layout tasks are 1D. Default to Flex.

**Grid** for 2D layouts — when rows AND columns need coordinated control:
- Page-level structure (header, sidebar, main, footer)
- Dashboards with aligned rows and columns
- Data-dense interfaces
- Image galleries with controlled aspect ratios

Don't default to Grid when Flex with `flex-wrap` would be simpler.

### The self-adjusting grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-lg);
}
```

Responsive without breakpoints. Columns are at least 280px; as many as fit; leftovers stretch.

### Named grid areas for complex layouts

```css
.page {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 280px 1fr;
}
@media (max-width: 768px) {
  .page {
    grid-template-areas: "header" "main" "footer";
    grid-template-columns: 1fr;
  }
}
```

---

## Visual hierarchy

### The squint test

Blur your eyes (or screenshot → blur in image editor). Can you identify:
1. The most important element?
2. The second most important?
3. Clear groupings?

If everything looks the same weight → hierarchy problem.

### Hierarchy through multiple dimensions

Don't rely on size alone. Combine 2–3 of these:

| Tool | Strong hierarchy | Weak hierarchy |
|------|-----------------|----------------|
| Size | 3:1+ ratio between levels | <2:1 ratio |
| Weight | Bold vs Regular (700 vs 400) | Medium vs Regular (500 vs 400) |
| Color | High contrast accent vs muted | Similar tones |
| Position | Top-left (primary scan zone) | Bottom-right |
| Space | Surrounded by generous whitespace | Crowded with neighbors |

A heading that's **larger + bolder + has more space above it** creates dramatically stronger hierarchy than just making it bigger.

---

## Elevation and depth

### Shadow scale

Define a semantic shadow scale, not arbitrary `box-shadow` values:

```css
--shadow-sm: 0 1px 2px oklch(0% 0 0 / 0.05);           /* subtle lift */
--shadow-md: 0 4px 8px oklch(0% 0 0 / 0.08);            /* cards, dropdowns */
--shadow-lg: 0 12px 24px oklch(0% 0 0 / 0.12);          /* modals, popovers */
--shadow-xl: 0 24px 48px oklch(0% 0 0 / 0.16);          /* dialogs, toasts */
```

Shadows should be subtle and use the same hue-tint as your neutrals (not pure black). A warm-tinted neutral page with cold gray shadows looks broken.

### Z-index scale

Define semantic layers, not arbitrary numbers:

```css
--z-dropdown: 10;
--z-sticky: 20;
--z-modal-backdrop: 30;
--z-modal: 40;
--z-toast: 50;
--z-tooltip: 60;
```

Never use `z-index: 9999`. It's a symptom of not having a system.

---

## Optical adjustments

Geometric center ≠ visual center. Some situations need manual nudging:

- **Play button icons**: shift right ~2px to compensate for the triangle's visual weight being left-heavy
- **Text in circular buttons**: may need 1px vertical offset depending on font metrics
- **Icons next to text**: align to the text's x-height, not the baseline or cap-height

Only adjust when something visibly looks wrong. Don't speculatively nudge things.

---

## Container queries

Viewport queries are for page layout. Container queries are for components that appear in different contexts.

```css
.card-container { container-type: inline-size; }

@container (min-width: 400px) {
  .card { flex-direction: row; }
}
@container (max-width: 399px) {
  .card { flex-direction: column; }
}
```

A card in a narrow sidebar should adapt to the sidebar's width, not the viewport. Container queries make components truly portable.

---

## Composition principles

- **Don't wrap everything in cards.** Spacing and alignment create visual grouping naturally. Cards add visual noise. Use them only when content needs clear interaction boundaries or visual comparison.
- **Never nest cards inside cards.** Flatten hierarchy using spacing, typography, and subtle dividers within a card.
- **Don't center everything.** Left-aligned text with asymmetric layouts feels more designed. Center alignment is appropriate for hero sections and short labels, not for body content or complex layouts.
- **Break the grid intentionally.** An element that spans wider than its siblings (a full-bleed image in a contained layout) creates emphasis precisely because it breaks the pattern. But only break the grid when you mean to draw attention.
- **Don't use identical card grids.** The pattern of same-sized cards with icon + heading + text, repeated 3–6 times, is the most recognizable AI layout template. Vary card sizes, span columns, or mix cards with non-card content.
