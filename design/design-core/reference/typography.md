# Typography

## Vertical rhythm

Your line-height is the base unit for all vertical spacing. If body text is `line-height: 1.5` on 16px (= 24px rhythm unit), spacing values should be multiples of 24px. This creates subconscious harmony — text and space share a mathematical foundation.

## Type scale

The common mistake: too many sizes too close together (14, 15, 16, 18px). This creates muddy hierarchy where the eye can't distinguish levels.

Use fewer sizes with more contrast. A 5-size system covers most interfaces:

| Role | Typical ratio | Use |
|------|--------------|-----|
| xs | 0.75rem | Captions, legal, timestamps |
| sm | 0.875rem | Secondary UI, metadata, labels |
| base | 1rem (16px) | Body text |
| lg | 1.25–1.5rem | Subheadings, lead text |
| xl+ | 2–4rem | Headlines, hero display |

Ratios: **1.25** (major third — conservative), **1.333** (perfect fourth — balanced), **1.5** (perfect fifth — dramatic). Pick one and commit.

**App UI**: fixed `rem` scale, optionally adjusted at 1–2 breakpoints. Fluid sizing undermines the spatial predictability dense layouts need.

**Marketing / content pages**: fluid sizing via `clamp(min, preferred, max)` for headings. Keep body text fixed.

```css
h1 { font-size: clamp(2rem, 5vw, 3.5rem); }
h2 { font-size: clamp(1.5rem, 3vw, 2.25rem); }
body { font-size: 1rem; } /* fixed */
```

## Readability

- **Measure**: `max-width: 65ch` for body text. Wider than ~75ch is fatiguing because the eye loses its place tracking back to the start of the next line.
- **Line-height**: scales inversely with line length. Narrow columns (40ch) want tighter leading (~1.4). Wide columns (70ch) want more (~1.6). For light text on dark backgrounds, add 0.05–0.1 to your normal line-height — light type reads as lighter weight and needs more breathing room.
- **Minimum**: 16px / 1rem for body text. Smaller is acceptable only for captions and metadata.

## Font selection process

Do this before typing any font name.

1. **Write 3 concrete brand words** from the brief. Not "modern" or "elegant" — those are dead categories. Try "warm and mechanical and opinionated", "calm and clinical and careful", "fast and dense and unimpressed", "handmade and a little weird".

2. **List the 3 fonts you'd normally reach for.** Write them down. Now check each against the reflex rejection list:

> Inter, Roboto, Open Sans, Lato, Montserrat, Arial, Poppins, DM Sans, Space Grotesk, Playfair Display, Cormorant Garamond, Fraunces, Newsreader, Lora, Crimson Pro, Crimson Text, Outfit, Plus Jakarta Sans, Instrument Sans, Instrument Serif, IBM Plex Sans, IBM Plex Serif, IBM Plex Mono, Syne, Space Mono, DM Serif Display, DM Serif Text

Reject every match. These are training-data defaults that create monoculture across projects.

3. **Browse with the 3 words as a physical object.** Imagine the font as something the brand could ship: a museum exhibit caption, a hand-painted shop sign, a 1970s mainframe terminal manual, a fabric label, a children's book on cheap newsprint, a tax form. Whichever physical object fits the words is pointing at the right *kind* of typeface. Sources: Google Fonts, Pangram Pangram, Future Fonts, Adobe Fonts, ABC Dinamo, Klim Type Foundry, Velvetyne.

4. **Reject the first thing that "looks designy."** That's the trained reflex. Keep looking.

5. **Cross-check.** If your final pick matches your previous project, go back to step 3. If your pick lines up with the obvious category default (serif for "elegant", monospace for "technical"), question it — the right font for a technical brief is not necessarily a sans-serif.

See [font-pairings.md](font-pairings.md) for curated alternatives organized by context.

## Pairing

**You often don't need two fonts.** One well-chosen family in multiple weights creates cleaner hierarchy than two competing typefaces. Only add a second font when you need genuine contrast.

When pairing, contrast on **multiple axes**:
- Structure: serif + sans-serif
- Personality: geometric + humanist
- Weight: a heavy display face + a light body face

Avoid pairing two fonts that are *similar but not identical* (two geometric sans-serifs). The near-match reads as a mistake.

## Anti-reflexes

These are worth defending against because they're the default AI response:
- A technical/developer brief does NOT need a serif "for warmth"
- An editorial/premium brief does NOT need the same expressive serif everyone is using
- A children's product does NOT need a rounded display font
- "Modern" does NOT mean geometric sans. The most modern choice in 2026 is not using the font everyone else is using.
- System fonts (`-apple-system, system-ui`) are underrated for apps where performance > personality

## OpenType features

Many fonts include features that improve rendering but are off by default:

```css
.body-text {
  font-feature-settings: "kern" 1, "liga" 1;  /* kerning + ligatures */
  font-variant-numeric: tabular-nums;          /* aligned columns in data */
}
.headings {
  font-feature-settings: "kern" 1, "liga" 1, "ss01" 1; /* stylistic set 1 */
}
```

- `tabular-nums`: numbers align in columns (essential for data tables, prices, stats)
- `oldstyle-nums`: lowercase-style figures for body text in editorial design
- `liga`: standard ligatures (fi, fl, ff)
- `ss01`–`ss20`: stylistic alternates (varies by font — check the font's feature list)

## Web font loading

Fonts cause two problems: invisible text (FOIT) and layout shift (FOUT).

```css
@font-face {
  font-family: 'CustomFont';
  src: url('/fonts/custom.woff2') format('woff2');
  font-display: swap;                    /* show fallback immediately, swap when loaded */
  unicode-range: U+0020-007F, U+00A0-00FF; /* Latin only — smaller download */
}
```

- **`font-display: swap`**: shows fallback immediately, swaps when custom font loads. Best for body text.
- **`font-display: optional`**: uses custom font only if it loads very fast, otherwise sticks with fallback. Best for non-critical display text.
- **Preload critical fonts**: `<link rel="preload" href="/fonts/custom.woff2" as="font" type="font/woff2" crossorigin>`
- **Subset aggressively**: Latin-only subsets are often 50–80% smaller than full Unicode coverage.
- **Metric-matched fallbacks**: use `size-adjust`, `ascent-override`, `descent-override` on the fallback `@font-face` to minimize layout shift.

Load only the weights you actually use. Each weight adds 20–50KB.
