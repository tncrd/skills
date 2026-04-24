# UX Guidelines

Highest-impact rules only. Format: DO → DON'T.

## Navigation
- Highlight active nav item with color/underline → no visual feedback on current location
- Add `padding-top` to body equal to sticky nav height → let nav overlap first content
- Update URL on state/view changes → static URLs for dynamic content
- Use breadcrumbs for 3+ levels of depth → use on flat single-level sites

## Interaction states (every interactive element needs all of these)
- Hover: subtle color/scale change + pointer cursor → no hover feedback
- Focus: visible ring (never `outline: none` without replacement) → invisible focus
- Active: pressed state (scale down, color shift) → no tap feedback
- Disabled: reduced opacity + `not-allowed` cursor → looks same as enabled
- Loading: disable button + show spinner → allow double-submit
- Error: message near the problem → silent failure
- Success: brief confirmation → no acknowledgment

```css
/* Minimum viable interactive states */
.button { transition: all 150ms var(--ease-out-quart); }
.button:hover { background: var(--primary-600); transform: translateY(-1px); }
.button:active { transform: translateY(0) scale(0.98); }
.button:focus-visible { outline: 2px solid var(--ring); outline-offset: 2px; }
.button:disabled { opacity: 0.5; cursor: not-allowed; pointer-events: none; }
```

## Forms
- Label above or beside every input → placeholder as only label (disappears on type)
- Show error below the field that caused it → single error at top of form
- Validate on blur for most fields → validate only on submit
- Use `type="email"`, `type="tel"`, `inputmode` → `type="text"` for everything
- Use `autocomplete` attributes → block or ignore autofill
- Confirm before delete/irreversible actions → delete without confirmation

## Feedback & states
- Show skeleton/spinner for operations > 300ms → frozen UI with no feedback
- Empty states: helpful message + primary action → blank screen
- Error states: plain-language message + recovery path → "Error 500" with nothing
- Toast notifications: auto-dismiss after 3–5s → toasts that stay forever
- Multi-step flows: step indicator or progress bar → no sense of where you are

## Layout
- Reserve space for async content (aspect-ratio, min-height) → content pushing layout on load
- Use `dvh` not `100vh` for full-screen mobile → mobile viewport cut off by browser chrome
- Limit text `max-width: 65–75ch` → full-width text on large screens
- Define a z-index scale (10, 20, 30, 50…) → arbitrary `z-index: 9999`

## Touch & mobile
- Touch targets ≥ 44×44px → tiny tap areas
- ≥ 8px gap between adjacent touch targets → tightly packed buttons
- Minimum 16px body text on mobile → tiny unreadable text
- `max-width: 100%` on images → fixed-width images breaking layout
- Ensure no horizontal scroll at 320px viewport → content overflowing

## Accessibility
- Text contrast ≥ 4.5:1 (body), ≥ 3:1 (large text, UI components) → low-contrast text
- Use icon + text or `aria-label` for icon-only buttons → icon with no label
- Descriptive `alt` text on meaningful images; `alt=""` on decorative → missing alt
- Sequential heading levels h1→h2→h3 → skip levels or use for visual style only
- Tab order matches visual reading order → illogical keyboard flow
- `aria-live` or `role="alert"` for dynamic error messages → visual-only errors
- `<label for="...">` wired to every input → floated labels with no programmatic link

## Performance
- Use `loading="lazy"` on below-fold images → load all images upfront
- `font-display: swap` or `optional` → invisible text during font load
- Load third-party scripts `async`/`defer` → synchronous blocking scripts
- Use WebP/AVIF → unoptimized PNG/JPEG everywhere

## Typography
- Line height 1.5–1.75 for body text → cramped or excessive leading
- Consistent modular type scale → random font sizes
- Reserve layout space with fallback font metrics → layout shift on font load

## Content
- Relative or locale-aware dates ("3 days ago", not "04/05/24") → ambiguous date formats
- Thousand separators or abbreviations for large numbers → 1000000 unformatted
- Realistic placeholder data in development → Lorem Ipsum everywhere
- Truncate with ellipsis + expand option → overflow breaking layout
