---
name: dark-mode-palette
description: Dark themes as designed, not inverted: desaturated tints, lightness-scaled elevation, and surface roles that survive low-light viewing.
tags: [dark-mode, color, themes, elevation, oklch]
related: [gray-ramp-neutrals, oklch-perceptual, semantic-color-system]
---

# Color Theory Skill: Dark Mode Palette

## 1. Definition

A dark theme is a second palette built for low-light conditions, not a light theme with colors flipped. Dark surfaces need less chroma (tints read as neon at low lightness), more lightness separation between elevation levels, and brand colors re-tuned — the 600 step on light becomes a 300–400 step on dark. This skill covers the palette side of dark mode: dark neutral ramps, brand re-mapping, status re-tuning, and the elevation-by-lightness model that replaces the shadow-driven depth cues of light interfaces.

## 2. Core Principles

- **Never #000:** pure black maximizes smearing, halation, and makes shadows invisible — the darkest surface is 0.10–0.15 lightness (oklch ~0.13).
- **Elevation gets lighter, not darker:** dark-mode surfaces raise by lightness (0.13 → 0.17 → 0.21) — the inverse of light mode's shadow model.
- **Desaturate tints:** brand/status chroma drops 20–40% at dark lightness — full-chroma brand color on dark reads as vibration.
- **Brand steps re-map per theme:** light-mode 600 (primary) maps to dark-mode 300–400 — the alias layer (design-tokens guide 06) re-binds, values stay ramps.
- **Status hues re-tune:** dark-mode danger/success shift lighter (400–500 text) to keep 4.5:1 on dark surfaces — same ramp, different steps.
- **Shadows are nearly useless on dark:** elevation communicates via surface lightness + border, shadow is a whisper.
- **Validate dark as its own theme:** every pairing re-computed in dark (a11y repo guide 02) — "it looks fine" in light proves nothing about dark.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Dark background | `--clr-dark-bg` | `oklch(0.13 0.01 210)` | Page background; never #000 |
| Dark surface | `--clr-dark-surface` | `oklch(0.17 0.012 210)` | Card surface; elevation step 1 |
| Dark surface raised | `--clr-dark-surface-raised` | `oklch(0.21 0.014 210)` | Modal/popover; elevation step 2 |
| Dark text primary | `--clr-dark-text-primary` | `oklch(0.93 0.005 210)` | Primary text on dark; not pure white (halation) |
| Dark text secondary | `--clr-dark-text-secondary` | `oklch(0.70 0.01 210)` | Secondary text; 4.5:1+ on dark surfaces |
| Dark brand primary | `--clr-dark-brand-primary` | `clr-brand-400` | Light-mode 600 re-mapped down |
| Dark chroma reduction | `--clr-dark-chroma-reduction` | `20-40%` | Tint chroma cut at dark lightness |
| Dark border | `--clr-dark-border` | `oklch(0.28 0.015 210)` | Borders carry dark-mode elevation |
| Dark shadow policy | `--clr-dark-shadow-policy` | `border-plus-lightness` | Shadows secondary; lightness+borders primary |
| Dark status shift | `--clr-dark-status-shift` | `text-steps-400-500` | Status text steps re-mapped lighter |

Consume them by linking `assets/css/dark-mode-palette.css` and reading `var(--clr-dark-*)` from the theme layer — these tokens are the dark half of the alias re-binding table, never values product code hardcodes.

## 4. Composition

- **Composes with gray-ramp-neutrals:** the dark neutral ramp is built as its own structure — less chroma, wider lightness deltas — not a copy of the light ramp darkened.
- **Composes with brand-ramp-construction and semantic-color-system:** ramps are theme-agnostic; alias re-binding per theme does the dark work, so a new dark theme is a mapping exercise, not a repaint.
- **Composes with skill-design-tokens guide 06 (dark mode):** that guide owns the theming mechanics (attribute switching, persistence, pipeline); this one owns the palette construction that the mechanics re-bind to.

## 5. Signature Patterns

- **Alias re-binding table:** every semantic alias lists its light and dark step (`bg: gray-50/gray-950`, `brand: brand-600/brand-400`) — this manifest is what dark themes are generated from, and the single source both themes trace back to.
- **Dark-mode first pass:** design the dark palette alongside light from day one. Retrofitted dark always ships with tinted-purple grays and vibrating brand colors because nobody re-tuned chroma — building both at once forces the re-mapping decisions early.

## 6. Real-World Use Cases

- **Products shipping dark themes:** developer tools, media apps, and any modern product where dark is now a launch requirement, not a novelty.
- **OLED-heavy audiences:** true blacks vs near-blacks decided deliberately per surface, weighing smear risk against battery.
- **Audit:** hunting #000 backgrounds, neon brand buttons, and invisible elevation in an existing dark theme.

## 7. Combination Notes

### With other color-theory skills

- **Pairs with gray-ramp-neutrals, oklch-perceptual, brand-ramp-construction, and semantic-color-system:** these are the raw materials — a dark neutral ramp, perceptual lightness math, re-mapped brand steps, and the alias tier that re-binds them. Dark mode is downstream of all four.
- **Pairs with contrast-models and cvd-safe-design:** every dark pairing is re-computed, and CVD simulations re-run on the dark palette — dark is validated as its own theme, never inherited from light.
- **Pairs with data-viz-palettes and gradient-theory:** charts and gradients both need dedicated dark variants (lower L/C), and this skill's surfaces are what their 3:1 and scrim checks run against.
- **Pairs with color-harmony, color-psychology, and cultural-color-meaning:** hue relationships and emotional/semantic readings survive the theme switch because chroma is re-tuned, not hue identity.
- **No caution or avoid list:** dark mode composes with the entire color-theory family — the failure mode is bypassing it (inverting light), not combining it.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with glassmorphism, aurora-ui, and minimalism:** glass layers and aurora fields live on dark surfaces, and minimalism's restrained palettes make the desaturated-tint discipline easy to hold.
- **Caution with skeuomorphism:** its shadow-and-texture depth model assumes light-mode physics; on dark, elevation-by-lightness replaces cast shadows, so skeuomorphic depth cues need deliberate re-interpretation.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** theme switches (light↔dark) and elevation transitions should animate with duration tokens so surface lightness changes read as intentional layering, not flicker.
- **Good affinity with ambient-motion:** slow ambient color fields sit naturally on dark surfaces — provided they keep chroma within the desaturated budgets this palette sets.

## 8. Anti-Patterns

- **Invert-filter dark:** flipped light palette with vibrating brand colors and purple grays
- **Pure-black surfaces:** #000 everywhere - smearing, invisible shadows, OLED smear worry
- **Un-desaturated brand:** light-mode chroma shipped to dark, buttons glowing like indicators
- **Light-only validation:** dark theme released because light mode's contrast was checked

### Accessibility Notes

Dark themes re-validate every WCAG pairing (a11y repo guide 02): text/surface at 4.5:1, UI components at 3:1 — and halation (bright-on-dark glare) is a low-vision concern that caps pure-white text and full-chroma fills. That is why primary text lands at `oklch(0.93 …)` instead of white, and why tints desaturate before they decorate. The fallback rule: when a brand or status step cannot hit contrast in dark, use a different step from the same ramp (never invent one) — the alias re-binding table absorbs the shift, so the fix is a mapping edit, not a new color.

## 9. Code Examples

### Example 1 — Light/dark theme switcher via alias re-binding

Tokens: `assets/css/dark-mode-palette.css`

```html
<header class="bar">
  <span class="bar-title">Settings</span>
  <button class="theme-toggle" id="toggle" aria-pressed="false">Dark</button>
</header>
<main class="page">
  <article class="card">
    <h2 class="card-title">Workspace</h2>
    <p class="card-text">Elevation, text, and brand colors all re-bind through aliases.</p>
    <button class="btn-primary">Invite teammate</button>
  </article>
</main>
<style>
  :root {
    /* Light aliases — point at the light ramp (gray-ramp-neutrals) */
    --clr-bg: oklch(0.97 0.005 210);
    --clr-surface: oklch(1 0 0);
    --clr-text: oklch(0.21 0.01 210);
    --clr-text-muted: oklch(0.45 0.01 210);
    --clr-border: oklch(0.88 0.008 210);
    --clr-brand: var(--clr-dark-brand-primary, oklch(0.62 0.19 255)); /* re-bound below */
  }
  /* Dark aliases — the re-binding table in action: same names, dark steps */
  [data-theme="dark"] {
    --clr-bg: var(--clr-dark-bg);                          /* oklch(0.13 0.01 210) */
    --clr-surface: var(--clr-dark-surface);                /* elevation step 1 */
    --clr-text: var(--clr-dark-text-primary);              /* 0.93, not white */
    --clr-text-muted: var(--clr-dark-text-secondary);      /* 4.5:1+ on dark */
    --clr-border: var(--clr-dark-border);                  /* borders carry elevation */
    --clr-brand: var(--clr-dark-brand-primary);            /* brand-400, not 600 */
  }
  body { margin: 0; background: var(--clr-bg); color: var(--clr-text);
         font: 14px/1.5 Inter, system-ui, sans-serif; }
  .bar { display: flex; justify-content: space-between; align-items: center;
         padding: 12px 20px; border-bottom: 1px solid var(--clr-border); }
  .bar-title { font-weight: 600; }
  .theme-toggle { background: none; border: 1px solid var(--clr-border);
         color: var(--clr-text); border-radius: 6px; padding: 6px 12px; cursor: pointer; }
  .page { padding: 24px; }
  .card { background: var(--clr-surface); border: 1px solid var(--clr-border);
          border-radius: 10px; padding: 20px; max-width: 420px; }
  .card-title { margin: 0 0 6px; font-size: 16px; }
  .card-text { margin: 0 0 16px; color: var(--clr-text-muted); }
  .btn-primary { background: var(--clr-brand); color: var(--clr-bg); border: none;
          border-radius: 8px; padding: 10px 18px; font-weight: 600; cursor: pointer; }
</style>
<script>
  const btn = document.getElementById('toggle');
  btn.addEventListener('click', () => {
    const root = document.documentElement;
    const dark = root.dataset.theme === 'dark';
    root.dataset.theme = dark ? 'light' : 'dark';
    btn.textContent = dark ? 'Dark' : 'Light';
    btn.setAttribute('aria-pressed', String(!dark));
  });
</script>
```

### Example 2 — Dark elevation: surfaces raise by lightness

Tokens: `assets/css/dark-mode-palette.css`

```html
<div class="stage">
  <div class="card">
    <p class="label">Surface — elevation 1</p>
    <div class="popover">
      <p class="label">Raised — elevation 2</p>
      <p class="hint">Lightness rises 0.13 → 0.17 → 0.21; borders carry the edge, shadow is a whisper.</p>
    </div>
  </div>
</div>
<style>
  body { margin: 0; background: var(--clr-dark-bg);              /* 0.13 — page */
         font: 14px/1.5 Inter, system-ui, sans-serif; }
  .stage { display: grid; place-items: center; min-height: 100vh; }
  .card { background: var(--clr-dark-surface);                   /* 0.17 — step 1 */
          border: 1px solid var(--clr-dark-border);
          border-radius: 12px; padding: 20px; width: 340px; }
  .popover { background: var(--clr-dark-surface-raised);         /* 0.21 — step 2 */
             border: 1px solid var(--clr-dark-border); border-radius: 10px;
             padding: 16px; margin-top: 14px;
             box-shadow: 0 4px 16px oklch(0 0 0 / 0.35); }       /* whisper, not model */
  .label { margin: 0; color: var(--clr-dark-text-primary); font-weight: 600; }
  .hint  { margin: 6px 0 0; color: var(--clr-dark-text-secondary); }
</style>
```

## 10. Implementation Checklist

- [ ] No surface in the dark theme is `#000`; page background sits at `var(--clr-dark-bg)` (~0.13 lightness).
- [ ] Elevation levels raise by lightness (0.13 → 0.17 → 0.21) and carry a `var(--clr-dark-border)` edge.
- [ ] Brand and status aliases re-bind to lighter steps (brand-400, status text 400–500) — never reuse light-mode values.
- [ ] Tint chroma is reduced 20–40% on dark surfaces; no full-chroma fills on dark.
- [ ] Primary text uses `var(--clr-dark-text-primary)` (0.93); every alias in the re-binding table lists both its light and dark step, and all dark pairings re-validated independently.
- [ ] Product code consumes only `var(--clr-*)` aliases; no component hardcodes a dark hex.
