# Motion Design

Motion in interfaces serves three roles: **feedback** (confirming actions), **continuity** (smoothing state changes), and **narrative** (telling a visual story). The first two are UI essentials. The third is where motion graphics begins.

---

## UI Motion (transitions and feedback)

### Duration by purpose

| Duration | Purpose | Examples |
|----------|---------|----------|
| 100–150ms | Instant feedback | Button press, toggle, color change |
| 200–300ms | State change | Menu open, tooltip, hover effect |
| 300–500ms | Layout shift | Accordion, modal, drawer, tab switch |
| 500–800ms | Entrance | Page load reveal, hero section |
| 800–1200ms | Narrative | Scroll-driven sequence, cinematic transition |

Exit animations should be ~75% of entrance duration. Users want to see things arrive; they want departures to be quick.

### Easing

Never use `ease` (the CSS default) — it's a compromise that's rarely optimal.

| Curve | When | CSS |
|-------|------|-----|
| ease-out | Elements entering view | `cubic-bezier(0.16, 1, 0.3, 1)` |
| ease-in | Elements leaving view | `cubic-bezier(0.7, 0, 0.84, 0)` |
| ease-in-out | State toggles (there and back) | `cubic-bezier(0.65, 0, 0.35, 1)` |

Exponential curves for micro-interactions (feel natural because they mimic friction):
```css
--ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);    /* smooth default */
--ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);    /* slightly snappier */
--ease-out-expo:  cubic-bezier(0.16, 1, 0.3, 1);     /* confident, decisive */
```

Bounce and elastic easing feel dated because they draw attention to the animation mechanics rather than the content. Real objects decelerate — they don't bounce at rest.

### Performance rules

Animate only `transform` and `opacity`. Everything else (`width`, `height`, `top`, `left`, `padding`, `margin`) triggers layout recalculation on every frame, causing jank.

For height animation (accordions, expandable sections): `grid-template-rows: 0fr → 1fr` instead of animating `height` directly.

```css
.expandable {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 300ms var(--ease-out-quart);
}
.expandable.open {
  grid-template-rows: 1fr;
}
.expandable > .inner {
  overflow: hidden;
}
```

### Reduced motion

Non-negotiable. Always provide a meaningful alternative — not just disabling everything.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## Choreography (entrance sequences and page transitions)

### Staggered reveals

Use CSS custom properties for clean stagger with a single animation definition:

```css
.stagger-item {
  opacity: 0;
  transform: translateY(12px);
  animation: reveal 400ms var(--ease-out-quart) forwards;
  animation-delay: calc(var(--i, 0) * 60ms);
}
@keyframes reveal {
  to { opacity: 1; transform: translateY(0); }
}
```
```html
<div class="stagger-item" style="--i: 0">First</div>
<div class="stagger-item" style="--i: 1">Second</div>
<div class="stagger-item" style="--i: 2">Third</div>
```

Cap total stagger time. 10 items × 60ms = 600ms total entrance. For long lists, stagger only the first 5–8 visible items and let the rest appear immediately.

### Page transitions (View Transitions API)

Same-document View Transitions work in all modern browsers. Cross-document is Chrome/Edge/Safari only — always provide a fallback.

```js
if (document.startViewTransition) {
  document.startViewTransition(() => updateDOM());
} else {
  updateDOM(); // instant fallback
}
```

```css
::view-transition-old(hero) { animation: fade-out 200ms ease-in; }
::view-transition-new(hero) { animation: fade-in 300ms ease-out; }
```

Shared element transitions (a list item expanding into a detail page, a thumbnail growing into a full image) create spatial continuity that makes navigation feel physical rather than digital.

---

## Scroll-driven animation

CSS `animation-timeline: scroll()` lets you tie any animation to scroll position — no JavaScript. Parallax, progress bars, reveal sequences all become pure CSS.

```css
.parallax-bg {
  animation: parallax linear;
  animation-timeline: scroll();
}
@keyframes parallax {
  from { transform: translateY(0); }
  to { transform: translateY(-100px); }
}
```

Browser support: Chrome, Edge, Safari. Firefox: flag only. **Always provide a static fallback:**

```css
@supports not (animation-timeline: scroll()) {
  .parallax-bg { transform: translateY(-30px); /* static offset */ }
}
```

---

## Spring physics

Cubic-bezier curves are mathematical — they don't model how physical objects actually move. Springs (mass + tension + damping) create motion that feels natural because it models real-world physics: overshoot, settle, rest.

When to use springs vs cubic-bezier:
- **Cubic-bezier**: simple state transitions, hover effects, opacity fades
- **Springs**: drag interactions, element repositioning, anything that should feel "physically connected" to user input

Libraries: Framer Motion (React), GSAP, or a minimal spring solver (~20 lines of JS). The key parameters are:
- **Stiffness** (higher = snappier, 100–300 typical)
- **Damping** (higher = less oscillation, 10–30 typical)
- **Mass** (higher = heavier feel, 1 default)

---

## SVG animation

SVG elements can be animated via CSS (transforms, opacity, stroke properties), SMIL (declarative, limited browser support — avoid), or JavaScript (Web Animations API, GSAP).

### Stroke drawing (the "line draw" effect)
```css
.path {
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
  animation: draw 2s var(--ease-out-quart) forwards;
}
@keyframes draw {
  to { stroke-dashoffset: 0; }
}
```
Set `stroke-dasharray` to the path's total length (use `path.getTotalLength()` in JS to measure).

### Animating SVG groups
Structure SVG with named `<g>` groups for each animatable element. This enables independent timing per element and clean export to Lottie.

```svg
<svg viewBox="0 0 200 200">
  <g id="background"><rect .../></g>
  <g id="icon" style="--i: 0"><path .../></g>
  <g id="text" style="--i: 1"><text .../></g>
</svg>
```

---

## Lottie / Bodymovin

Lottie renders After Effects animations as lightweight JSON. Workflow:
1. Design animation in After Effects
2. Export via Bodymovin plugin → `.json` file
3. Render in browser with `lottie-web` (or `@lottiefiles/lottie-player`)

```html
<lottie-player src="animation.json" background="transparent"
  speed="1" style="width: 300px; height: 300px" autoplay loop>
</lottie-player>
```

When to use Lottie vs CSS:
- **CSS**: simple transitions, state changes, hover effects, staggered reveals
- **Lottie**: complex multi-element choreography, character animation, illustrative motion, anything designed in After Effects

Keep Lottie files under 100KB for web. Compress with LottieFiles optimizer.

---

## Video-ready motion specs

When motion needs to export for video editing (After Effects, Premiere, DaVinci):

### Motion tokens file
Store alongside assets as `.motion.json`:
```json
{
  "entrance": {
    "duration": 400,
    "easing": "cubic-bezier(0.25, 1, 0.5, 1)",
    "stagger": 60,
    "transform": "translateY(12px) → translateY(0)",
    "opacity": "0 → 1"
  },
  "exit": {
    "duration": 300,
    "easing": "cubic-bezier(0.7, 0, 0.84, 0)",
    "transform": "translateY(0) → translateY(-8px)",
    "opacity": "1 → 0"
  }
}
```

### Export guidelines
- SVG layers: separate `<g>` groups with meaningful IDs for per-element animation
- PNG sequence: export at target resolution (1920×1080 for HD, 3840×2160 for 4K)
- Frame rate: 30fps for web preview, 60fps for production video
- Color space: sRGB for web, Rec. 709 for broadcast

---

## Canvas and WebGL

For effects CSS can't express: particle systems, generative art, post-processing, data visualization with thousands of elements.

- **Canvas 2D**: custom rendering, pixel manipulation. Use `OffscreenCanvas` in a Web Worker for heavy rendering without blocking the main thread.
- **WebGL/WebGL2**: shader effects, 3D, GPU-accelerated rendering. Libraries: Three.js (full 3D), OGL (lightweight), regl (functional).
- **WebGPU** (Chrome/Edge, Safari partial): next-gen GPU compute. Always fall back to WebGL2.

### Progressive enhancement pattern
```js
if ('gpu' in navigator) { /* WebGPU path */ }
else if (canvas.getContext('webgl2')) { /* WebGL2 path */ }
else { /* CSS-only fallback — must still look good */ }
```

Lazy-initialize GPU contexts only when near viewport. Pause off-screen rendering. Kill what you can't see.

---

## Principles

- **One hero moment per page**. A well-orchestrated page entrance creates more impact than scattered micro-animations everywhere.
- **Motion communicates hierarchy**. The first element to appear draws the most attention. Stagger order = importance order.
- **Match motion to personality**. Snappy and precise for a developer tool. Fluid and organic for a wellness brand. The same easing curve doesn't fit every project.
- **Test on real devices**. An animation smooth on your M3 MacBook may jank on a mid-range Android. Target 60fps on the lowest device you support.
- **Iterate visually**. Motion that "works" in code rarely looks right on the first try. The gap between functional and beautiful is closed through visual iteration, not more code.
