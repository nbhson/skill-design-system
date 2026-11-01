---
name: color-harmony
description: The classical scheme machinery - complementary, analogous, triadic, split-complementary - applied as starting constraints, not rules.
tags: [color, harmony, schemes, palettes, proportion]
related: [oklch-perceptual, color-psychology, gray-ramp-neutrals]
---

# Color Theory Skill: Color Harmony & Schemes

## 1. Definition

Color harmony is the practice of selecting hues that read as intentional together: complementary pairs create tension and focus, analogous sets create calm and cohesion, triadic balances variety with order. Modern practice treats schemes as generators of starting points - a triadic pick is the first draft, refined by perceptual models (guide 02), contrast floors (guide 10), and brand constraints. The scheme names the relationship; the palette work makes it usable.

## 2. Core Principles

- **Schemes are relationships, not recipes:** complementary/analogous/triadic describe hue relationships; quality depends on saturation, lightness, and proportion.
- **Proportion beats hue choice:** the 60-30-10 distribution (dominant/secondary/accent) makes almost any scheme livable - the accent earns its pop by scarcity.
- **Analogous for product UI, complementary for marketing:** products read best with hue-adjacent calm; marketing moments earn contrast.
- **Complementary pairs need separation:** full-strength complements vibrate at equal saturation - shift one toward tint or shade before use.
- **Triadic schemes mute two:** use one hue strongly and its triadic partners desaturated, or the result reads as a circus.
- **Neutral anchoring is mandatory:** every scheme needs a neutral ramp (guide 04) carrying most of the surface area.
- **Scheme ≠ palette:** a scheme is 2-5 hue intents; a palette is ramps + aliases with contrast validation - schemes start palettes, they do not ship as them.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Scheme | `--clr-scheme-primary` | `hue-210` | The brand-dominant hue anchor (OKLCH hue angle) |
| Scheme | `--clr-scheme-type` | `analogous-plus-accent` | Documented scheme: analogous core + complementary accent |
| Harmony | `--clr-harmony-analogous-spread` | `30deg` | Hue neighbors for analogous sets |
| Harmony | `--clr-harmony-complement` | `180deg` | Opposite hue; always re-balanced for lightness |
| Harmony | `--clr-harmony-triadic` | `120deg` | Triadic spread; desaturate 2 of 3 |
| Harmony | `--clr-harmony-split` | `150-210deg` | Split-complementary band; softer than pure complement |
| Distribution | `--clr-distribution-60-30-10` | `60/30/10` | Dominant/secondary/accent area proportions |
| Accent | `--clr-accent-usage` | `sparingly-under-10%` | Accents collapse to noise when everywhere |
| Neutral | `--clr-scheme-neutral-pairing` | `always-paired` | No scheme ships without its neutral ramp (guide 04) |
| Refinement | `--clr-scheme-refinement` | `perceptual-pass-required` | Schemes pass through OKLCH + contrast refinement |

Consume them by linking `assets/css/color-harmony.css` once at the app root, then referencing `var(--clr-...)` wherever a scheme decision is documented in code - the scheme type, hue anchor, and spread values are contracts, not comments. The token values describe the scheme's geometry; the actual surface colors come from the ramps the scheme expands into, so changing `--clr-scheme-primary` re-derives the palette through the ramp generator, never through hand-edited hexes.

## 4. Composition

- **Composes with oklch-perceptual:** schemes are picked in hue terms; OKLCH makes them lightness/chroma-usable across ramps - the scheme supplies the hue angles, the perceptual space makes the values work at every lightness.
- **Composes with brand-ramp-construction:** the chosen scheme expands into structured ramps with chroma curves - a scheme hue is never shipped as a single point, only as a ramp.
- **Composes with skill-ui-ux:** each style has scheme preferences (minimalism: analogous+neutral; maximalism: triadic saturation) - the styleAffinity records which scheme leans serve which style.

## 5. Signature Patterns

- **Scheme-first palette workshop:** pick the scheme and proportions on a whiteboard before touching hex values - intent precedes pixels. The workshop output is the scheme token set (primary hue, type, spreads, distribution), which the ramp generator then consumes as input.
- **Accent rationing:** a single accent hue reused across status, CTA, and focus, rationed by area rules - accents stay meaningful. When every component earns the accent, none does; the `--clr-accent-usage` budget enforces scarcity in code review.

## 6. Real-World Use Cases

- **New brand/product palettes from scratch.** Start with the scheme workshop: pick the hue relationship and the 60-30-10 distribution, then let ramp construction and perceptual refinement turn the intent into a validated palette.
- **Marketing campaign palettes derived from (not breaking) the product scheme.** Campaigns may push contrast - a complementary burst against the analogous product core - while staying recognizably inside the brand's scheme geometry.
- **Audit: accent inflation, vibrating complements, orphan hues with no scheme membership.** Existing UI is checked against its declared scheme; every hue in the product either belongs to the scheme or gets removed.

## 7. Combination Notes

### With other color-theory skills

- **Good with oklch-perceptual, gray-ramp-neutrals, brand-ramp-construction, semantic-color-system, data-viz-palettes, gradient-theory, contrast-models, dark-mode-palette, color-psychology, and cvd-safe-design:** harmony is the hue-intent layer every other palette skill refines - schemes propose, ramps/contrast/CVD work dispose. The pipeline works because scheme output is the input for all of them.
- **Good but also caution with cultural-color-meaning:** the scheme can be built globally (hue relationships are universal), but the accent hue choice must be re-checked per market before launch - a scheme that is culturally safe in one region can flag the wrong message in another.
- **No avoid list:** harmony is generative, not restrictive; nothing in the palette stack contradicts it. The only incompatibility is skipping it - hue choices made without scheme logic surface later as orphan hues.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and maximalism:** minimalism runs analogous-plus-accent against a neutral ramp; flat design uses scheme hues at full, confident saturation; maximalism scales the triadic instinct up with the muting rules intact - each style maps cleanly to a scheme strategy.
- **Caution with skeuomorphism:** skeuomorphic surfaces add texture, gloss, and material rendering that shift perceived hue and chroma away from the scheme's math - scheme tokens describe flat values, and skeuomorphic treatment needs its own perceptual re-tune before the scheme relationship still reads.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing and entrance-exit:** scheme transitions (hover to pressed, rest to focus) move between ramp steps of the same scheme, so the hue never jumps - easing tokens pace the change the way 60-30-10 paces the area. Entrance animations that reveal sections in scheme order (dominant first, accent last) reinforce the distribution.
- **No caution list:** scheme-internal color motion stays inside validated ramp steps, so no animation pattern in the companion repo conflicts - as long as animated hues never leave the scheme's hue set.

## 8. Anti-Patterns

- **Scheme-by-decoration** — five unrelated brand hues with no scheme logic reading as a garage sale
- **Equal-proportion rainbow** — 20% red, 20% blue, 20% green - nothing dominates, everything shouts
- **Vibrating complements** — full-saturation complementary pairs touching, shimmering at edges
- **Accent inflation** — the accent hue on buttons, badges, links, and charts until it highlights nothing

### Accessibility Notes

Schemes must clear contrast floors before aesthetics are judged (guide 10): a harmonious palette that fails 4.5:1 is decorative art, not UI - harmony models pick hue relationships, contrast models pick usable steps. This is why `--clr-scheme-refinement` is set to `perceptual-pass-required`: the scheme workshop output is a draft, and the palette ships only after OKLCH lightness re-balancing and contrast validation pass every assigned role. The fallback rule keeps the scheme relationship intact: when a scheme hue cannot pass contrast at its assigned role, shift it along the lightness axis within the same hue family - keep the relationship, fix the values. Moving the complement darker instead of swapping in a new hue preserves the very geometry that makes the palette read as intentional, which is the entire point of declaring a scheme at all.

## 9. Code Examples

### Example 1 — 60-30-10 scheme demo (analogous core + accent)

Tokens: `assets/css/color-harmony.css`

```html
<div class="page">
  <header class="hero"><h1>Launch plan</h1></header>
  <aside class="panel"><h2>Status</h2><p>Analogous core: hues 180/210/240.</p></aside>
  <main class="content">
    <p>Dominant surface carries 60% of the area.</p>
    <button class="cta">Publish</button>
  </main>
</div>
<style>
  :root {
    --hue-core: 210;                                  /* --clr-scheme-primary */
    --spread: 30;                                     /* --clr-harmony-analogous-spread */
    --complement: 180;                                /* --clr-harmony-complement */
  }
  .page {
    display: grid; grid-template-columns: 2fr 1fr;
    font: 15px/1.5 Inter, system-ui, sans-serif;
    min-height: 320px;
  }
  .hero {   /* 60% dominant: core hue, tinted surface */
    background: oklch(0.97 0.02 var(--hue-core));
    color: oklch(0.25 0.05 var(--hue-core));
    grid-column: 1 / -1; padding: 24px; margin: 0;
  }
  .content { /* 30% secondary: analogous neighbor */
    background: oklch(0.93 0.03 calc(var(--hue-core) + var(--spread)));
    color: oklch(0.28 0.06 calc(var(--hue-core) + var(--spread)));
    padding: 24px;
  }
  .panel {  /* analogous neighbor on the other side */
    background: oklch(0.90 0.04 calc(var(--hue-core) - var(--spread)));
    padding: 24px;
  }
  .cta {    /* 10% accent: complement, lightness-rebalanced, scarce */
    background: oklch(0.55 0.16 calc(var(--hue-core) + var(--complement)));
    color: oklch(0.99 0.01 calc(var(--hue-core) + var(--complement)));
    border: none; border-radius: 8px; padding: 10px 20px;
    font: 600 14px/1 Inter, system-ui, sans-serif; cursor: pointer;
  }
</style>
```

### Example 2 — Scheme comparison grid

Tokens: `assets/css/color-harmony.css`

```html
<div class="grid">
  <figure class="scheme" data-scheme="analogous"><div class="strip"><i></i><i></i><i></i></div><figcaption>Analogous — calm, product UI</figcaption></figure>
  <figure class="scheme" data-scheme="complement"><div class="strip"><i></i><i></i><i></i></div><figcaption>Complementary — tension, marketing</figcaption></figure>
  <figure class="scheme" data-scheme="triadic"><div class="strip"><i></i><i></i><i></i></div><figcaption>Triadic — variety, one loud two muted</figcaption></figure>
  <figure class="scheme" data-scheme="split"><div class="strip"><i></i><i></i><i></i></div><figcaption>Split-complementary — softer tension</figcaption></figure>
</div>
<style>
  :root { --hue: 210; } /* var(--clr-scheme-primary) resolved */
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
          font: 13px/1.4 Inter, system-ui, sans-serif; max-width: 520px; }
  .scheme { margin: 0; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }
  .strip { display: flex; height: 56px; }
  .strip i { flex: 1; }
  /* analogous: core + 30deg neighbors */
  .scheme[data-scheme="analogous"] i:nth-child(1) { background: oklch(0.65 0.12 calc(var(--hue) - 30)); }
  .scheme[data-scheme="analogous"] i:nth-child(2) { background: oklch(0.60 0.15 var(--hue)); }
  .scheme[data-scheme="analogous"] i:nth-child(3) { background: oklch(0.65 0.12 calc(var(--hue) + 30)); }
  /* complementary: 180deg, second tone tinted for separation */
  .scheme[data-scheme="complement"] i:nth-child(1) { background: oklch(0.60 0.15 var(--hue)); }
  .scheme[data-scheme="complement"] i:nth-child(2) { background: oklch(0.85 0.06 calc(var(--hue) + 180)); }
  .scheme[data-scheme="complement"] i:nth-child(3) { background: oklch(0.45 0.10 calc(var(--hue) + 180)); }
  /* triadic: 120deg, partners desaturated */
  .scheme[data-scheme="triadic"] i:nth-child(1) { background: oklch(0.60 0.16 var(--hue)); }
  .scheme[data-scheme="triadic"] i:nth-child(2) { background: oklch(0.70 0.04 calc(var(--hue) + 120)); }
  .scheme[data-scheme="triadic"] i:nth-child(3) { background: oklch(0.70 0.04 calc(var(--hue) - 120)); }
  /* split-complementary: 150/210deg band */
  .scheme[data-scheme="split"] i:nth-child(1) { background: oklch(0.60 0.15 var(--hue)); }
  .scheme[data-scheme="split"] i:nth-child(2) { background: oklch(0.72 0.09 calc(var(--hue) + 150)); }
  .scheme[data-scheme="split"] i:nth-child(3) { background: oklch(0.72 0.09 calc(var(--hue) + 210)); }
  figcaption { padding: 8px 12px; }
</style>
```

## 10. Implementation Checklist

- [ ] The scheme is documented as tokens (`--clr-scheme-primary`, `--clr-scheme-type`) before any hex value is picked.
- [ ] Surface area follows the 60-30-10 distribution — the accent hue occupies under 10% of any screen.
- [ ] Every scheme hue expands into a ramp via brand-ramp-construction; no scheme hue ships as a single hex.
- [ ] Complementary and split pairs are lightness-separated before use — no full-strength complements touching.
- [ ] Triadic partners are desaturated; only one triadic hue runs at full strength.
- [ ] The scheme is anchored by a neutral ramp (`--clr-scheme-neutral-pairing: always-paired`) carrying most surface area.
- [ ] The palette passes OKLCH + contrast refinement (`--clr-scheme-refinement`) in both themes before release.
- [ ] Marketing campaigns derive from the declared scheme — no orphan hues with no scheme membership.
