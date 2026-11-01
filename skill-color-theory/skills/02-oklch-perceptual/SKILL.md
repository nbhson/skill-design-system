---
name: oklch-perceptual
description: Working in perceptually uniform spaces - OKLCH/OKLab for ramp math, interpolation, and adjustments that look how the numbers say they look.
tags: [color, oklch, oklab, perceptual, gradients]
related: [color-harmony, brand-ramp-construction, gradient-theory]
---

# Color Theory Skill: OKLCH & Perceptual Color Spaces

## 1. Definition

OKLCH is a perceptually uniform color space: L (lightness), C (chroma), H (hue) move independently in ways human vision agrees with - unlike HSL, where 50% lightness is a completely different brightness per hue. Building palettes in OKLCH means consistent lightness steps produce consistent perceived steps, hue rotation does not shift brightness, and interpolation does not travel through muddy gray. It is the working space of every serious modern palette.

## 2. Core Principles

- **HSL is a lie:** equal L values differ wildly in perceived brightness (yellow glows, blue sinks) - ramps in HSL need per-hue hacks that OKLCH makes unnecessary.
- **L is perceived lightness, C is colorfulness, H is hue:** adjust each independently; consistent L steps across a ramp read as equal steps.
- **Chroma is bounded per hue:** some hues carry high chroma (yellow), others cannot (blue); ramps cap C per hue instead of forcing uniform saturation.
- **Interpolate in OKLab, not sRGB:** gradients between hues stay vivid in OKLab; sRGB interpolation muddies through gray.
- **One working space for the whole system:** scheme, ramps, gradients, and dark-mode math all happen in OKLCH, then convert to sRGB for legacy with documented gamut mapping.
- **Wide-gamut awareness:** oklch() can express P3 colors sRGB cannot - declare the gamut strategy (guide: 08) before publishing values.
- **Lightness is accessibility's leverage point:** contrast fixes happen on the L axis, leaving hue identity intact - the cheapest accessible adjustments.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Space | `--clr-working-space` | `oklch` | All palette math in OKLCH; sRGB is output |
| Ramp | `--clr-l-ramp-steps` | `0.97,0.93,0.86,0.77,0.66,0.55,0.45,0.35,0.27,0.20,0.15` | A canonical 11-step lightness ramp |
| Text | `--clr-l-body-text` | `0.25` | Body text lightness on light theme |
| Surface | `--clr-l-bg-surface` | `0.97-0.99` | Surface lightness band on light theme |
| Brand | `--clr-c-brand-cap` | `0.15-0.25` | Usable chroma band for brand hues in UI |
| Neutral | `--clr-c-neutral-tint` | `0.005-0.015` | The hue whisper in tinted neutrals |
| Blend | `--clr-interpolation-space` | `oklab` | Gradient/blending interpolation space |
| Gamut | `--clr-gamut-strategy` | `srgb-clamp-with-p3-enhance` | Baseline sRGB; @media (color-gamut: p3) enhancement |
| Syntax | `--clr-css-syntax` | `oklch(L C H)` | Modern CSS color syntax; fallback via @supports |
| Legacy | `--clr-hsl-deprecation` | `legacy-reading-only` | HSL accepted only when reading old palettes |

Consume them by linking `assets/css/oklch-perceptual.css` once at the app root, then referencing `var(--clr-...)` from any palette-generating code - ramp scripts read `--clr-l-ramp-steps` instead of hardcoding lightness values, and gradient utilities read `--clr-interpolation-space` to build `linear-gradient(in oklab, ...)` declarations. The tokens encode the working-space policy: anything that computes a color goes through OKLCH, and sRGB appears only as output, never as the space where decisions happen.

## 4. Composition

- **Composes with color-harmony:** scheme relationships (hue angles) are OKLCH hue differences - the same H axis. A scheme's "30deg analogous spread" is literally an H delta, so scheme math and ramp math share one coordinate system.
- **Composes with brand-ramp-construction and gray-ramp-neutrals:** ramps are L/C/H curves, not hex lists - the ramp generator walks this guide's lightness steps along a chroma curve on the scheme's hue.
- **Composes with skill-design-tokens guide 01:** token values may carry oklch() primitives; this guide owns the color math. Token infrastructure stores and themes values; this skill guarantees the values were computed perceptually.

## 5. Signature Patterns

- **Ramp generator in OKLCH:** one script emits brand ramps from (hue, chroma curve, L steps) - palette changes become parameter changes. Rebranding from blue to teal is editing two numbers, not re-picking eleven hexes; the lightness skeleton (`--clr-l-ramp-steps`) stays constant so contrast contracts survive the swap.
- **OKLab interpolation utility:** all gradients (CSS, canvas, design tools) interpolate in OKLab - sRGB interpolation is lint-blocked. The utility is the single place hue blending happens, which makes "sRGB-mud" a build failure rather than a design review catch.

## 6. Real-World Use Cases

- **Building brand ramps that work identically across themes.** Because L is perceived lightness, a step that hits 4.5:1 in light mode maps to a predictable dark-mode sibling on the same ramp - theming becomes arithmetic, not re-design.
- **Migrating legacy HSL palettes to perceptually uniform values.** Convert first, then audit: most "inconsistent brand colors" are HSL lightness lies that vanish once values are expressed in OKLCH and re-stepped evenly.
- **Designing gradients that stay vivid instead of muddying.** Declare `in oklab` and the hue-to-hue transition travels the short, vivid path - the difference is visible immediately on any brand-to-complement blend.

## 7. Combination Notes

### With other color-theory skills

- **Good with color-harmony, brand-ramp-construction, gray-ramp-neutrals, semantic-color-system, dark-mode-palette, gradient-theory, contrast-models, data-viz-palettes, color-psychology, cultural-color-meaning, and cvd-safe-design:** this is the computational substrate of the whole stack - schemes speak H deltas, ramps speak L steps, gradients speak interpolation spaces, and contrast math lives on the L axis. Every other palette skill is easier and more honest when its numbers are perceptual.
- **Caution with gray-ramp-neutrals:** the caution is about low-lightness chroma behavior, not conflict - tinted neutrals carry the brand hue whisper (C 0.005-0.015), and OKLCH is exactly what reveals that tints read purple below ~0.2 L. The neutrals guide owns that dark-mode re-tuning; this guide supplies the math that proves why it is needed.
- **No avoid list:** perceptual uniformity has no ideological opponents in the palette stack - only skills that have not adopted it yet, which is a migration task, not an incompatibility.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and aurora-ui:** minimalism and flat design depend on small palettes whose few values are exactly right - perceptual stepping is what makes a 5-color palette feel intentional. Aurora UI is layered gradients at scale, which is impossible to art-direct without OKLab interpolation.
- **Caution with retro:** retro palettes often target the specific (im)precision of older color spaces and printing processes - faithful period color is sometimes *wrong* perceptually on purpose. Apply OKLCH normalization to the UI chrome, but preserve documented legacy values where the style's authenticity depends on them.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing and data-animation:** color transitions and chart animations both interpolate between values, and perceptual interpolation makes animated color moves read as constant-speed - an HSL-animated hover visibly stalls in the middle. Data animations that sweep sequential ramps stay honest because the ramp's L axis is monotonic and uniform.
- **No caution list:** motion consumes the same interpolation utility the gradients use, so animated color and static color cannot drift apart - there is one blending space in the system.

## 8. Anti-Patterns

- **HSL holdout** — mixing L values in HSL while claiming a perceptual system - the numbers disagree with the eyes
- **Chroma-max ramps** — forcing the same chroma on every hue until some hues are radioactive and others are dead
- **sRGB-mud gradients** — hue-to-hue interpolation in sRGB traveling through gray
- **Wide-gamut leakage** — P3 values shipped without a documented sRGB fallback, breaking on older displays

### Accessibility Notes

Perceptual uniformity is an accessibility multiplier: contrast (guide 10) and APCA math operate on lightness - OKLCH's L axis is the one that moves contrast predictably, so accessible adjustments stop being trial-and-error. When a pairing fails 4.5:1, the fix is a known L delta rather than a guessing session, and because only L moves, the hue identity the brand depends on survives every accessibility fix. The fallback rule covers the legacy end: where oklch() is unsupported in a required target, pre-converted sRGB fallbacks ship via @supports - computed, not hand-translated, so the two stay in sync. Hand-translated fallbacks are how wide-gamut leakage and silent drift enter a system; generated `@supports` blocks keep the OKLCH source of truth and the sRGB baseline identical by construction.

## 9. Code Examples

### Example 1 — 11-step OKLCH ramp rendered as swatches

Tokens: `assets/css/oklch-perceptual.css`

```html
<div class="ramp" role="img" aria-label="11-step OKLCH brand ramp, hue 250"></div>
<style>
  .ramp {
    display: grid; grid-template-columns: repeat(11, 1fr);
    width: 100%; max-width: 640px; height: 72px;
    border-radius: 8px; overflow: hidden;
    font: 12px/1.3 ui-monospace, monospace;
  }
  .ramp i { position: relative; }
  .ramp i:nth-child(1)  { background: oklch(0.97 0.015 250); }
  .ramp i:nth-child(2)  { background: oklch(0.93 0.035 250); }
  .ramp i:nth-child(3)  { background: oklch(0.86 0.075 250); }
  .ramp i:nth-child(4)  { background: oklch(0.77 0.115 250); }
  .ramp i:nth-child(5)  { background: oklch(0.66 0.15 250); }
  .ramp i:nth-child(6)  { background: oklch(0.55 0.17 250); } /* chroma peak */
  .ramp i:nth-child(7)  { background: oklch(0.45 0.15 250); }
  .ramp i:nth-child(8)  { background: oklch(0.35 0.115 250); }
  .ramp i:nth-child(9)  { background: oklch(0.27 0.085 250); }
  .ramp i:nth-child(10) { background: oklch(0.20 0.055 250); }
  .ramp i:nth-child(11) { background: oklch(0.15 0.035 250); }
</style>
```

### Example 2 — OKLab vs sRGB gradient + hex→OKLCH converter

Tokens: `assets/css/oklch-perceptual.css`

```html
<div class="compare">
  <div class="grad oklab" role="img" aria-label="OKLab gradient, vivid"></div>
  <p>in oklab</p>
  <div class="grad srgb" role="img" aria-label="sRGB gradient, muddy"></div>
  <p>sRGB default</p>
</div>
<form class="converter">
  <label>Hex <input id="hex" value="#2563EB" pattern="#[0-9a-fA-F]{6}"></label>
  <output id="out">—</output>
</form>
<script type="module">
  // sRGB hex -> OKLCH, displayed so palette authors see the real numbers
  const toLinear = c => { c /= 255; return c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4; };
  const out = document.getElementById('out');
  document.getElementById('hex').addEventListener('input', e => {
    const v = e.target.value;
    if (!/^#[0-9a-fA-F]{6}$/.test(v)) return;
    const [r, g, b] = [1, 3, 5].map(i => toLinear(parseInt(v.slice(i, i + 2), 16)));
    // LMS cone response, then cube-root to OKLab
    const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
    const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
    const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
    const L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s;
    const A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s;
    const B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s;
    const C = Math.hypot(A, B);
    const H = ((Math.atan2(B, A) * 180 / Math.PI) + 360) % 360;
    out.textContent = `oklch(${L.toFixed(3)} ${C.toFixed(3)} ${H.toFixed(1)})`;
  });
  document.getElementById('hex').dispatchEvent(new Event('input'));
</script>
<style>
  .compare { font: 13px/1.4 Inter, system-ui, sans-serif; max-width: 480px; }
  .grad { height: 48px; border-radius: 8px; margin-top: 8px; }
  .oklab { background: linear-gradient(in oklab, oklch(0.7 0.17 300), oklch(0.7 0.17 60)); }
  .srgb  { background: linear-gradient(oklch(0.7 0.17 300), oklch(0.7 0.17 60)); }
  .converter { margin-top: 16px; display: flex; gap: 12px; align-items: center; }
  .converter input { font: inherit; padding: 6px 10px; border: 1px solid #ccc; border-radius: 6px; }
  .converter output { font: 12px/1 ui-monospace, monospace; }
</style>
```

## 10. Implementation Checklist

- [ ] All palette math runs in OKLCH — `--clr-working-space: oklch` is enforced, and HSL appears only when reading legacy palettes (`--clr-hsl-deprecation`).
- [ ] Ramps use the canonical lightness skeleton from `--clr-l-ramp-steps` — adjacent steps differ by consistent perceived deltas.
- [ ] Chroma is capped per hue within `--clr-c-brand-cap` — no forced uniform saturation across hues.
- [ ] Every hue-to-hue gradient declares `in oklab` — sRGB interpolation is lint-blocked.
- [ ] Tinted neutrals keep chroma inside `--clr-c-neutral-tint` (0.005-0.015).
- [ ] Wide-gamut values follow `--clr-gamut-strategy`: sRGB baseline with a `@media (color-gamut: p3)` enhancement and `@supports` fallbacks.
- [ ] Accessibility fixes move L only — hue identity survives every contrast correction.
- [ ] Shipped sRGB fallbacks are computed from the OKLCH source, never hand-translated.
