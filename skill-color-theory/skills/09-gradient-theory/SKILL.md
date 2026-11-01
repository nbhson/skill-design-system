---
name: gradient-theory
description: Gradients as designed objects: interpolation space, stop placement, hue travel, and the modern mesh/aurora looks without mud or banding.
tags: [gradients, color, oklab, aurora, design-systems]
related: [oklch-perceptual, brand-ramp-construction, dark-mode-palette]
---

# Color Theory Skill: Gradient Design

## 1. Definition

Gradients are transitions between colors — and their quality is decided by invisible math: the interpolation space (OKLab stays vivid, sRGB muddies), the stop placement (evenly-spaced stops on long distances band), and the hue path (traveling through the hue wheel or between it). Modern CSS (`linear-gradient` in oklab, conic gradients, mesh-ish layering) makes the theory directly usable; this skill covers building gradients that look intentional in both themes — declared interpolation, deliberate stops, short hue paths, band-killing treatments, and contrast-safe text zones.

## 2. Core Principles

- **Interpolate in OKLab:** CSS `in oklab` keeps hue-to-hue gradients vivid; default sRGB interpolation travels through gray — declare the space or eat the mud.
- **Stop placement controls pacing:** unequal spacing between stops changes where the eye reads the transition — place stops where the design needs tension, not evenly by default.
- **Short hue paths read clean:** traveling 30–60 degrees of hue is cohesive; 180+ degree paths need deliberate stops or they vibrate.
- **Bandkill via subtle noise or stops:** banding on wide soft gradients is fixed by dithering, tiny hue jitter, or added midpoints — not by hoping.
- **Two-color gradients are the default:** three+ color gradients need a reason (brand storytelling); most UI needs tint→hue or hue→shade.
- **Text never sits on active gradients without a scrim:** gradient backgrounds need a contrast-safe overlay zone where text lives (guide 10).
- **Dark mode re-tunes gradients:** gradients built for light read as neon on dark — dark themes get lower-lightness, lower-chroma gradient variants.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Gradient interpolation | `--clr-gradient-interpolation` | `oklab` | CSS in oklab; sRGB interpolation lint-blocked |
| Gradient structure default | `--clr-gradient-structure-default` | `two-color` | Tint→core or core→shade; 3+ needs justification |
| Gradient hue path | `--clr-gradient-hue-path` | `30-60deg-travel` | Short hue paths; long paths need stops plan |
| Gradient hero | `--clr-gradient-hero` | `clr-brand-500 to clr-brand-700` | CTA/hero fill default |
| Gradient text safe | `--clr-gradient-text-safe` | `scrim-under-text` | Contrast-safe zone where text overlays gradients |
| Gradient mesh recipe | `--clr-gradient-mesh-recipe` | `layered-radials-blur` | Aurora/mesh look via layered radial gradients |
| Gradient bandkill | `--clr-gradient-bandkill` | `midpoints-or-noise` | Anti-banding treatment documented per gradient |
| Gradient dark variant | `--clr-gradient-dark-variant` | `re-tuned-for-dark` | Lower L/C variants for dark theme |
| Gradient conic use | `--clr-gradient-conic-use` | `progress-wheels-only` | Conic for progress/charts, not decoration |
| Gradient usage budget | `--clr-gradient-usage-budget` | `hero-and-brand-only` | Gradients are accents in product UI, not surfaces |

Consume them by linking `assets/css/gradient-theory.css` and reading `var(--clr-gradient-*)` from the gradient layer — endpoints resolve through `var(--clr-brand-*)` ramp steps, so a gradient can never introduce an off-ramp color.

## 4. Composition

- **Composes with oklch-perceptual:** OKLab interpolation and OKLCH ramp endpoints are shared machinery — the same perceptual space that keeps ramps even keeps gradient transitions vivid and predictable.
- **Composes with brand-ramp-construction:** gradients run between ramp steps; off-ramp endpoints are lint-blocked, so every gradient inherits the contrast and governance work already done on the ramp.
- **Composes with skill-ui-ux:** aurora-ui and glassmorphism lean on gradients heavily — the styleAffinity documents which styles gradients serve, and which ones gradients overwhelm.

## 5. Signature Patterns

- **Aurora assembly:** 2–3 large blurred radial gradients in brand-adjacent hues over a dark surface — the reusable aurora recipe with dark/light variants, sized so fields overlap softly instead of banding at their edges.
- **Gradient-on-brand contract:** every gradient's endpoints are brand ramp steps, its text zone has a validated scrim, and both themes have variants — a gradient that fails any of the three is not shipped.

## 6. Real-World Use Cases

- **Hero sections, CTA fills, and brand moments:** the legitimate gradient zones where a usage budget is spent deliberately.
- **Aurora/glassmorphism backgrounds:** layered radial fields with contrast-safe text zones carved out by scrims.
- **Audit:** hunting muddy hue-to-hue gradients, banded washes, and unreadable text sitting on transitions.

## 7. Combination Notes

### With other color-theory skills

- **Pairs with oklch-perceptual:** shared interpolation machinery — endpoints and stops are chosen in the same perceptual space that validates ramps, so gradients and ramps agree about what "halfway" means.
- **Pairs with brand-ramp-construction (with a caution):** the good case is structural — `--clr-gradient-hero` runs `brand-500 → brand-700`, endpoints resolved from the ramp so contrast work transfers. The caution is direction: gradients must never bend the ramp — if a gradient wants a step the ramp lacks, the ramp is extended through governance, not by the gradient smuggling a new color in.
- **Pairs with dark-mode-palette and gray-ramp-neutrals:** aurora fields live on dark surfaces, and every gradient gets a re-tuned dark variant (lower L/C) so it never reads as neon against `--clr-dark-bg`.
- **Pairs with contrast-models and cvd-safe-design:** scrims are validated with the same contrast math as any text pairing, and gradients never become the sole carrier of meaning that CVD users could lose.
- **Pairs with data-viz-palettes:** in charts, gradient-looking things are sequential ramps only — decoration gradients are banned from encoding data, and conic use is reserved for progress wheels.
- **Pairs with color-harmony, color-psychology, semantic-color-system, and cultural-color-meaning:** short hue paths keep the harmony intact, and a gradient between brand hues inherits their emotional and semantic reading rather than inventing a new one mid-travel.
- **No avoid list:** gradients compose with the whole family — the failure mode is undeclared interpolation and unvalidated text zones, not combination.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with aurora-ui, glassmorphism, and maximalism:** these styles are built on gradient fields — aurora's layered radials, glass's tinted translucency, and maximalism's rich color moments all run through this skill's interpolation and bandkill rules.
- **Caution with minimalism and brutalism-ui:** both spend decoration budget near zero — a gradient in a minimal UI must be the single brand moment, and brutalism's raw flatness actively fights soft washes; in either, most gradients are subtracted, not designed.

### With motion skills (companion repo skill-animation)

- **Good affinity with ambient-motion:** slow aurora drift is the canonical ambient use — fields translate and breathe on long, gentle easings while the scrim and text zone stay static, so contrast never changes under the text.
- **Good affinity with easing-timing:** gradient state changes (CTA hover deepening brand-500 → brand-700) animate with duration tokens, keeping the ramp-step transition legible instead of a flash.
- **No caution list:** the constraint is architectural, not a skill conflict — anything moving under text must re-validate the scrim zone, which is this skill's own contract.

## 8. Anti-Patterns

- **sRGB mud:** hue-to-hue gradients that travel through gray because nobody declared oklab
- **Banded washes:** wide soft gradients with visible stair-stepping
- **Text-on-gradient gambling:** headlines crossing hue transitions with unknown contrast
- **Gradient everywhere:** buttons, cards, and tables all gradient - accents dissolved into noise

### Accessibility Notes

Gradients create unknown-contrast zones: text over gradients must pass 4.5:1 across the entire text area (guide 10), and gradient-only state signaling fails 1.4.1 — gradients decorate, they never carry meaning alone. The practical consequence is the scrim contract: any text sitting on a gradient gets a `--clr-gradient-text-safe` overlay zone validated across the worst point of the underlying transition, not the average. The fallback rule: when text must sit on a gradient and no scrim passes contrast, place text on a solid section adjacent to the gradient — contrast certainty beats gradient reach.

## 9. Code Examples

### Example 1 — OKLab vs sRGB interpolation, same endpoints

Tokens: `assets/css/gradient-theory.css`

```html
<div class="compare">
  <figure>
    <div class="swatch srgb" role="img" aria-label="sRGB gradient, muddy middle"></div>
    <figcaption><strong>sRGB (default)</strong> — hue-to-hue travel passes through gray</figcaption>
  </figure>
  <figure>
    <div class="swatch oklab" role="img" aria-label="OKLab gradient, vivid throughout"></div>
    <figcaption><strong>in oklab</strong> — same endpoints, vivid and even</figcaption>
  </figure>
</div>
<style>
  :root {
    --clr-brand-500: #2563EB;   /* ramp step — gradient endpoint */
    --clr-warm-500: #EA580C;    /* ramp step — gradient endpoint */
  }
  body { font: 14px/1.5 Inter, system-ui, sans-serif; background: #FAFAFA;
         color: #171717; margin: 0; padding: 24px; }
  .compare { display: grid; gap: 20px; max-width: 480px; }
  figure { margin: 0; }
  .swatch { height: 56px; border-radius: 10px; border: 1px solid #D4D4D4; }
  .srgb   { background: linear-gradient(to right, var(--clr-brand-500), var(--clr-warm-500)); }
  .oklab  { /* declared interpolation — the lint rule demands `in oklab` */
            background: linear-gradient(in oklab to right, var(--clr-brand-500), var(--clr-warm-500)); }
  figcaption { margin-top: 8px; color: #404040; font-size: 13px; }
  figcaption strong { color: #171717; }
</style>
```

### Example 2 — Aurora hero: layered radials with a scrim-protected text zone

Tokens: `assets/css/gradient-theory.css`

```html
<section class="hero">
  <div class="aurora" aria-hidden="true"></div>
  <div class="scrim" aria-hidden="true"></div>
  <div class="hero-copy">
    <h1>Ship interfaces that feel alive</h1>
    <p>Layered radials in brand-adjacent hues, blurred into fields — with a
       validated scrim zone where the headline lives.</p>
    <button class="cta">Start building</button>
  </div>
</section>
<style>
  :root {
    --clr-dark-bg: oklch(0.13 0.01 210);        /* dark-mode-palette surface */
    --clr-dark-text-primary: oklch(0.93 0.005 210);
    --clr-dark-text-secondary: oklch(0.70 0.01 210);
    --clr-brand-400: oklch(0.65 0.19 255);      /* ramp steps — endpoints */
    --clr-brand-500: oklch(0.58 0.21 262);
    --clr-brand-700: oklch(0.45 0.19 265);
  }
  body { margin: 0; font: 14px/1.5 Inter, system-ui, sans-serif; }
  .hero { position: relative; overflow: hidden; background: var(--clr-dark-bg);
          min-height: 420px; display: flex; align-items: flex-end; }
  /* Aurora assembly: 2-3 large blurred radials, brand-adjacent hues, short hue paths */
  .aurora { position: absolute; inset: -20%; filter: blur(48px);
            background:
              radial-gradient(46rem 30rem at 18% 28%, oklch(0.55 0.16 262 / 0.55), transparent 70%),
              radial-gradient(40rem 28rem at 82% 18%, oklch(0.60 0.13 230 / 0.45), transparent 70%),
              radial-gradient(42rem 30rem at 62% 90%, oklch(0.52 0.15 290 / 0.40), transparent 70%); }
  /* Scrim: contrast-safe zone under the text — worst point passes 4.5:1 */
  .scrim { position: absolute; inset: 0;
           background: linear-gradient(in oklab to top,
             oklch(0.13 0.01 210 / 0.92) 0%, oklch(0.13 0.01 210 / 0.60) 42%, transparent 72%); }
  .hero-copy { position: relative; max-width: 560px; padding: 96px 40px 56px; }
  h1 { color: var(--clr-dark-text-primary); font-size: 32px; margin: 0 0 10px; }
  p  { color: var(--clr-dark-text-secondary); margin: 0 0 22px; }
  .cta { /* two-color default: core → shade, in oklab, bandkill via the mid stop */
         background: linear-gradient(in oklab to bottom,
           var(--clr-brand-500), var(--clr-brand-700));
         color: var(--clr-dark-text-primary); border: none; border-radius: 8px;
         padding: 12px 22px; font-weight: 600; cursor: pointer; }
  .cta:focus-visible { outline: 2px solid var(--clr-brand-400); outline-offset: 2px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every `linear-gradient`/`radial-gradient` declares `in oklab` — default sRGB interpolation fails lint.
- [ ] Gradient endpoints resolve through `var(--clr-brand-*)` ramp steps; no off-ramp endpoint colors.
- [ ] Default structure is two-color (tint→hue or hue→shade); three+ stops carry documented justification.
- [ ] Hue travel stays within 30–60 degrees unless a deliberate stops plan is documented.
- [ ] Every gradient under text has a validated scrim zone (`var(--clr-gradient-text-safe)`) passing 4.5:1.
- [ ] Both themes ship variants — dark gradients use lower-L/C re-tuned values, never the light ones.
- [ ] Conic gradients appear only as progress wheels/charts; gradients stay within the hero-and-brand budget.
