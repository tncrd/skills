# Color & Contrast

## Why OKLCH

HSL lies about lightness. `hsl(60, 100%, 50%)` (yellow) looks bright. `hsl(240, 100%, 50%)` (blue) looks dark. Both claim 50% lightness. OKLCH fixes this — equal lightness values *look* equally light.

`oklch(lightness chroma hue)` — lightness 0–100%, chroma ~0–0.4, hue 0–360.

As you move toward white or black, **reduce chroma**. High chroma at 90% lightness produces garish pastels. High chroma at 10% lightness produces muddy darks. A light tint at 85% lightness wants ~0.08 chroma, not 0.15.

---

## Building a palette step by step

### 1. Pick a brand hue

This is a brand decision. Don't reach for blue (hue ~250) or warm orange (hue ~60) by reflex — those are the dominant AI-design defaults. Start from the brief's tone words and the audience's context.

### 2. Build the primary scale

Hold chroma and hue roughly constant. Vary lightness to create a 5–7 step scale:

```css
--primary-50:  oklch(97% 0.02 250);   /* lightest tint */
--primary-100: oklch(93% 0.04 250);
--primary-200: oklch(85% 0.08 250);
--primary-500: oklch(55% 0.20 250);   /* base */
--primary-700: oklch(40% 0.16 250);
--primary-900: oklch(25% 0.10 250);   /* darkest shade */
```

Notice chroma decreases at the extremes. This is intentional.

### 3. Tint your neutrals

Pure gray (`oklch(50% 0 0)`) feels dead next to colored UI. Add a tiny chroma (0.005–0.015) hued toward your brand:

```css
--neutral-50:  oklch(97% 0.005 250);  /* barely perceptible tint */
--neutral-200: oklch(88% 0.008 250);
--neutral-500: oklch(55% 0.010 250);
--neutral-800: oklch(25% 0.008 250);
--neutral-950: oklch(12% 0.005 250);
```

The tint should come from THIS brand's hue. Not from "warm = friendly, cool = tech" formulas.

### 4. Add semantic colors

These are functional, not decorative:

| Role | Base hue | When |
|------|----------|------|
| Success | green (~145) | Completion, positive change |
| Error | red (~25) | Failure, destructive action |
| Warning | amber (~85) | Caution, requires attention |
| Info | blue (~250) | Neutral information |

2–3 shades each is enough. Match the lightness range to your primary scale.

### 5. Define surfaces

```css
--surface-base:     oklch(99% 0.003 250);  /* page background */
--surface-raised:   oklch(100% 0 0);       /* cards on base */
--surface-overlay:  oklch(100% 0 0);       /* modals, popovers */
```

In dark mode, invert the relationship: base is darkest, raised is slightly lighter.

---

## The 60-30-10 rule

This is about visual **weight**, not pixel count:

- **60%**: neutral surfaces, white space, backgrounds
- **30%**: secondary text, borders, inactive elements
- **10%**: accent — CTAs, active states, highlights

Accents work because they're rare. The moment you use your accent color on 30% of the page, it stops being an accent.

---

## Dark vs light

Derive from audience and viewing context. Not preference, not default.

| Context | Theme | Why |
|---------|-------|-----|
| SRE dashboard at night | Dark | Reduces eye strain in dim rooms |
| Hospital portal for anxious patients | Light | Light feels safer and calmer |
| Children's reading app | Light | High contrast, bright, approachable |
| Music player for nighttime listening | Dark | Matches the environment |
| Wedding planning on Sunday morning | Light | Warm, aspirational, hopeful |
| Coding IDE | Dark | Reduces fatigue during long sessions |

Don't default to dark "to look cool" or light "to play safe". Both are lazy.

---

## Contrast requirements

| Content | Minimum ratio | Standard |
|---------|--------------|----------|
| Body text | 4.5:1 | WCAG AA |
| Large text (≥24px or ≥18.5px bold) | 3:1 | WCAG AA |
| UI components and borders | 3:1 | WCAG AA |

**Gray text on colored backgrounds looks washed out** because the gray has no color relationship with its surroundings. Use a darker shade of the background color, or use `color-mix()`:

```css
.muted-on-blue {
  color: color-mix(in oklch, var(--blue-500) 70%, black);
}
```

---

## What to avoid and why

- **Pure black (#000) or pure white (#fff)**: never appears in nature. Even the darkest surfaces benefit from a tiny tint. Pure black next to colors creates harsh, vibrating edges.
- **Gradient text** (`background-clip: text` + gradient): decorative rather than meaningful. Top-3 AI design tell. Use weight or size for emphasis, not gradient fill.
- **The AI palette**: cyan-on-dark, purple-to-blue gradients, neon accents on dark backgrounds. These are the most overused color combinations in AI-generated output because they appeared in many training examples. They signal "machine made this" immediately.
- **Defaulting**: choosing dark "because it looks modern" or light "because it's safe". Both defaults skip the thinking that produces distinctive work.
