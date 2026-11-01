---
name: brand-ramp-construction
description: One brand hue becomes a 9-11 step ramp - chroma curves, lightness anchors, and the per-step contrast contracts that make it usable.
tags: [color, ramps, brand, oklch, contrast]
related: [oklch-perceptual, semantic-color-system, gray-ramp-neutrals]
---

# Color Theory Skill: Brand Ramp Construction

## 1. Definition

A brand color is a single point; a product needs 9-11 steps around it: tints for surfaces and hover states, the core for primary actions, shades for pressed states and text-on-brand. Ramp construction converts the brand point into an OKLCH curve - lightness anchored to canonical stops, chroma peaked at the middle steps and tapered toward the ends - so every step has a documented contrast contract for its intended role.

## 2. Core Principles

- **9-11 steps, anchored to L stops:** the brand point is step 500-600; tints fill 50-400, shades fill 700-950 (Tailwind-convention steps).
- **Chroma curve, not flat chroma:** chroma peaks at mid steps and tapers toward white (pastel ends) and black (dark ends) - flat chroma produces neon tints or dead shades.
- **Every step gets a role contract:** 50-100 backgrounds, 200-300 hover surfaces, 500-600 primary, 700-900 pressed/text-on-light, 950 text-on-dark.
- **Text-on-brand is computed:** white or near-black on the 500-600 step - whichever passes 4.5:1 with margin - documented per step.
- **Hue drift is controlled:** ramp steps keep hue within a few degrees of the brand hue (or drift deliberately toward warmer darks); accidental drift makes ramps read as different colors.
- **Interactive states come from ramp steps:** hover = one step lighter, pressed = one step darker, disabled = 300 at reduced opacity - states are steps, not new colors.
- **The ramp validates against its consumers:** primary button, focus ring, badge, and link colors are the acceptance tests - the ramp exists for them.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Step count | `--clr-ramp-step-count` | `11` | 50/100/200/300/400/500/600/700/800/900/950 |
| Core step | `--clr-brand-core-step` | `500-600` | Where the brand point anchors |
| L anchors | `--clr-l-anchors` | `0.97-0.18` | Step 50 to step 950 lightness band |
| Chroma curve | `--clr-chroma-curve` | `peak-mid-taper-ends` | C peaks at 500-600, tapers toward both ends |
| Hue drift | `--clr-hue-drift-limit` | `within-5deg` | Steps stay on the brand hue (documented drift allowed) |
| Primary bg | `--clr-primary-bg` | `clr-brand-600` | Primary action surface |
| Primary text | `--clr-primary-text-on` | `white-or-950-computed` | Whichever passes 4.5:1+ with margin |
| Hover step | `--clr-hover-step` | `core-minus-1` | Hover = one ramp step lighter |
| Pressed step | `--clr-pressed-step` | `core-plus-1` | Pressed = one ramp step darker |
| Disabled recipe | `--clr-disabled-recipe` | `step-300-at-60%` | Disabled look; exempt from contrast, documented |

Consume them by linking `assets/css/brand-ramp-construction.css` and referencing `var(--clr-brand-<step>)` primitives through alias tokens (`var(--clr-primary-bg)`, `var(--clr-hover-step)`) - product code picks roles, and the ramp generator guarantees the contracts behind them. If a component needs a step outside its role contract, the ramp (or the contract) changes through review.

## 4. Composition

- **Composes with oklch-perceptual:** ramps are generated as OKLCH curves; the generator lives beside the tokens.
- **Composes with semantic-color-system:** semantic hues (success/warning/danger) are built as ramps with the same machinery.
- **Composes with skill-design-tokens guides 01/05:** ramp steps become color primitives; alias bindings (primary, hover) live in the token layer.

## 5. Signature Patterns

- **Ramp-from-point generator:** input (oklch brand point + chroma curve + L stops) emits the full ramp CSS + JSON - no hand-picked steps.
- **Consumer acceptance pass:** the ramp is validated by rendering a primary button, link, badge, and focus ring from its steps before adoption.

## 6. Real-World Use Cases

- **New brands converting a logo color into a working UI palette.**
- **Multi-brand theming:** each brand = (hue, chroma curve) parameters regenerating ramps (design-tokens guide 07).
- **Audit:** ramps whose hover/pressed states are new colors, steps with no contrast contract.

## 7. Combination Notes

### With other color-theory skills

- **Good with oklch-perceptual and gray-ramp-neutrals:** ramps are OKLCH curves generated from (hue, chroma curve, L stops), and they sit on a neutral backbone sharing the same hue temperature - generator and whisper stay coherent.
- **Good with semantic-color-system and dark-mode-palette:** status hues are built with the same ramp machinery, and dark themes re-bind the brand ramp through the alias layer (600 → 300-400) without redefining steps.
- **Good with color-harmony and color-psychology:** the scheme picks the brand hue and its relationships; psychology validates that the chosen hue/temperature still signals the brand - both happen before ramp generation.
- **Good with contrast-models and cvd-safe-design:** per-step role contracts are contrast math applied at generation time, and CVD simulation verifies the ramp's distinctions survive color-vision differences.
- **Caution with gradient-theory:** gradients run between ramp steps (500→700 is legitimate), but each gradient needs its own interpolation-space and banding plan - a ramp does not authorize free-form multi-stop gradients.
- **No avoid list:** every other skill either consumes this ramp or feeds its inputs; the failure mode to prevent is hand-picked ramps bypassing the generator.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** minimalism needs one confident brand hue doing the accent work (which a well-curved ramp provides); flat-design's solid fills map directly to mid steps; class-morphism's soft depth reads best with pastel tints from the tapered chroma ends.
- **Caution with collage-art:** collage styles deliberately clash and sample colors from found imagery, which fights the controlled hue-drift limit - if a collage composition needs foreign colors, they live outside the brand ramp, documented as intentional.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing and feedback-confirmation:** hover/pressed state changes are single-step lightness shifts that animate cleanly with duration tokens; confirmation feedback (success flash after an action) should reuse the ramp's own steps so the color change reads as system response, not decoration.
- **Caution generally:** do not animate brand steps beyond adjacent-step deltas - sweeping the full ramp (500→200) as a transition reads as a new color appearing, not an interactive state.

## 8. Anti-Patterns

- **Hand-picked ramps** — 11 hex values eyeballed in a design tool, no curve, no contracts
- **Neon tints** — 100-level steps at full chroma glowing like highlighters
- **Hover-by-hue** — interactive states as new hues instead of ramp steps
- **Computed-never text-on-brand** — white text on a 55% lightness core failing 4.5:1 by 0.8

### Accessibility Notes

The ramp's contrast contracts ARE its accessibility: each step's allowed roles (text/bg/border) are pre-validated in both themes - consumers pick steps, and accessibility comes pre-solved (guide 10 owns the math). This is why text-on-brand is a computed decision rather than a preference: white or near-black on the 500-600 core is chosen by whichever passes 4.5:1 with margin, and that decision is documented per step in the generator output. Interactive states inherit the guarantee - hover and pressed are adjacent steps whose own contracts were validated at generation, so a button never enters a state with unknown contrast. The fallback rule: when a step fails its intended role, the generator re-tunes L/C for that step and regenerates - manual hex patches are never shipped because they break the curve, and a patched step silently voids every contract built on its neighbors.

## 9. Code Examples

### Example 1 — Full 11-step brand ramp with per-step role contracts

Tokens: `assets/css/brand-ramp-construction.css` (generated from brand point `oklch(0.55 0.19 250)`)

```html
<div class="ramp">
  <div class="step s50"><span>50 · bg wash</span></div>
  <div class="step s100"><span>100 · tint bg</span></div>
  <div class="step s200"><span>200 · hover surface</span></div>
  <div class="step s300"><span>300 · hover / disabled</span></div>
  <div class="step s400"><span>400 · icons</span></div>
  <div class="step s500"><span>500 · brand core</span></div>
  <div class="step s600"><span>600 · primary bg</span></div>
  <div class="step s700"><span>700 · pressed / text</span></div>
  <div class="step s800"><span>800 · text-on-light</span></div>
  <div class="step s900"><span>900 · deep text</span></div>
  <div class="step s950"><span>950 · text-on-dark</span></div>
</div>
<style>
  .ramp { display: grid; grid-template-columns: repeat(11, 1fr); border-radius: 8px; overflow: hidden; max-width: 640px; }
  .step { height: 56px; display: grid; place-items: end center; font: 10px/1.4 ui-monospace, monospace; }
  /* Each step's label color IS its text contract, validated at generation */
  .s50   { background: var(--clr-brand-50);   color: var(--clr-brand-800); }
  .s100  { background: var(--clr-brand-100);  color: var(--clr-brand-800); }
  .s200  { background: var(--clr-brand-200);  color: var(--clr-brand-900); }
  .s300  { background: var(--clr-brand-300);  color: var(--clr-brand-950); }
  .s400  { background: var(--clr-brand-400);  color: var(--clr-brand-950); }
  .s500  { background: var(--clr-brand-500);  color: white; }           /* 4.5:1+ computed */
  .s600  { background: var(--clr-brand-600);  color: white; }           /* primary: white passes */
  .s700  { background: var(--clr-brand-700);  color: white; }
  .s800  { background: var(--clr-brand-800);  color: var(--clr-brand-50); }
  .s900  { background: var(--clr-brand-900);  color: var(--clr-brand-100); }
  .s950  { background: var(--clr-brand-950);  color: var(--clr-brand-200); }
</style>
```

### Example 2 — Primary button: states are steps, not new colors

```html
<button class="btn-primary">Create project</button>
<script>
  // Consumer acceptance check: text-on-brand must be pre-computed, not assumed
  const css = getComputedStyle(document.documentElement);
  const core = css.getPropertyValue('--clr-brand-600').trim();
  console.assert(core, 'brand-600 must carry a documented 4.5:1+ text-on-brand decision');
</script>
<style>
  .btn-primary {
    background: var(--clr-primary-bg); /* --clr-brand-600; white text passes 4.5:1+ with margin */
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font: 600 14px/1 Inter, system-ui, sans-serif;
    cursor: pointer;
    transition: background 150ms ease;
  }
  .btn-primary:hover  { background: var(--clr-brand-500); }  /* hover = core-minus-1 (lighter) */
  .btn-primary:active { background: var(--clr-brand-700); }  /* pressed = core-plus-1 (darker) */
  .btn-primary:disabled { background: var(--clr-brand-300); opacity: 0.6; cursor: not-allowed; }
  .btn-primary:focus-visible { outline: 2px solid var(--clr-brand-700); outline-offset: 2px; }
</style>
```

## 10. Implementation Checklist

- [ ] The brand ramp has 11 steps (50–950) generated from the brand point — zero hand-picked hex values.
- [ ] The chroma curve peaks at 500-600 and tapers toward both ends — no neon tints, no dead shades.
- [ ] Every step has a documented role contract (bg / hover surface / primary / pressed / text) in the generator output.
- [ ] `--clr-primary-text-on` records the computed choice (white or 950) that passes 4.5:1+ with margin on `--clr-primary-bg`.
- [ ] Hover and pressed states use `--clr-hover-step` (core-minus-1) and `--clr-pressed-step` (core-plus-1) — no new-hue states.
- [ ] Hue drift across steps stays within `--clr-hue-drift-limit` (or is documented as deliberate).
- [ ] The consumer acceptance pass (primary button, link, badge, focus ring) renders from ramp steps before adoption.
- [ ] Disabled styling follows `--clr-disabled-recipe` (step-300-at-60%) and its exemption is documented.
