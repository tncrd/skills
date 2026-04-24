# Responsive Design

## Mobile-first

Write base styles for mobile, then add complexity for larger screens with `min-width` queries. This forces you to decide what's essential — desktop-first causes mobile to be an afterthought where things get progressively hidden and broken.

```css
/* base: mobile */
.nav { display: none; }

/* enhancement: desktop */
@media (min-width: 1024px) {
  .nav { display: flex; }
}
```

## Container queries over viewport queries for components

A card in a narrow sidebar should adapt to the sidebar's width, not the viewport's width. Viewport queries are for page-level layout decisions. Container queries are for components that appear in different contexts.

```css
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

## Fluid layouts

`repeat(auto-fit, minmax(280px, 1fr))` gives you a responsive grid that reflows without any breakpoints. Columns are at minimum 280px wide; as many as fit on a row; leftover space distributed evenly.

Use `clamp()` for fluid sizing: `font-size: clamp(1.2rem, 3vw, 2rem)` scales between the min and max based on viewport, with the preferred value as a middle ground.

## Breakpoint strategy

Don't pick breakpoints based on device sizes (there are too many). Pick them based on where the layout breaks — where does the content stop looking good? That's your breakpoint.

Common useful points: 480px (large phone), 768px (tablet), 1024px (small desktop), 1280px (standard desktop). But your content may need different points.

## What to adapt, not hide

Hiding functionality on mobile is not responsive design — it's giving mobile users a worse product. Instead:
- Navigation: collapse to drawer or bottom bar, but keep all destinations
- Tables: horizontal scroll container, or reflow to card layout per row
- Complex forms: single-column reflow, same fields
- Dense data: progressive disclosure to show key columns, expand for detail

## Touch considerations

- Minimum touch target: 44×44px. Anything smaller is regularly mis-tapped.
- Thumb zones matter: bottom half of the screen is easier to reach. Put primary actions there on mobile.
- Remove hover-only interactions. `hover` events don't fire reliably on touch. If something only appears on hover, it's invisible to touch users.
- `touch-action: manipulation` removes the 300ms tap delay on older browsers.

## Images

```html
<img
  src="image-800.webp"
  srcset="image-400.webp 400w, image-800.webp 800w, image-1600.webp 1600w"
  sizes="(max-width: 768px) 100vw, 50vw"
  loading="lazy"
  alt="..."
/>
```

Always set `width` and `height` attributes to prevent layout shift while images load. Use `aspect-ratio` in CSS as a modern alternative.
