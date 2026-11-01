---
name: variable-fonts
description: One file, many styles: weight/optical axes, named instances, and when a variable font beats static weights — plus the loading math.
tags: [typography, variable-fonts, font-axes, optical-sizing, web-performance]
related: [type-scale, webfont-loading, font-pairing, numeric-tabular, accessible-typography, fluid-responsive]
---

# Typography Skill: Variable Fonts

## 1. Definition

Variable fonts encode an entire design space (weight, width, optical size, slant) in one file along continuous axes: `font-variation-settings` or high-level properties (`font-weight`, `font-optical-sizing`) pick any point on those axes. The payoff: one 60–90KB file replaces 3–5 static weights, enables fine-grained hierarchy (weight 550), and unlocks optical sizing. The cost: axis abuse (animating weight on body text) and fallback complexity if size-adjust is skipped.

## 2. Core Principles

- **Adopt when axes exceed static needs:** 3+ weights or optical sizing justifies one variable file; 2 weights may be cheaper static.
- **High-level properties first:** `font-weight`/`font-stretch`/`font-optical-sizing` map to axes and inherit correctly — `font-variation-settings` is a low-level escape hatch, not the default.
- **Named instances are the safe menu:** expose axis values as named tokens (400/600/700), not raw axis playgrounds.
- **Optical size axes are free micro-typography:** `font-optical-sizing: auto` selects display/text cuts at every size — better tracking and contrast for free.
- **Do not animate weight on reading text:** weight interpolation on body text reflows lines every frame (layout shift + unreadable) — animate color/opacity instead.
- **One variable file per family:** loading a variable font AND its static weights doubles cost — pick one strategy per face.
- **Fallback metrics still apply:** variable or not, fallbacks need size-adjust tuning (see webfont-loading skill).
- **Custom axes need design review:** experimental axes (slnt, GRAD, custom) enter only after design review — no raw `wght: 537` in production.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Strategy | `--type-vf-strategy` | `one-file-per-family` | Variable replaces static weights; never both |
| Weight | `--type-vf-weight-range` | `100-900` | wght axis range as loaded (subset if narrower) |
| Optical | `--type-vf-optical` | `auto` | font-optical-sizing: auto when opsz axis exists |
| Weights | `--type-vf-named-weights` | `400,600,700` | The tokenized subset users may pick |
| Axes | `--type-vf-experimental-axes` | `review-gated` | Custom axes (slnt, GRAD) need design review |
| Animation | `--type-vf-animation-policy` | `no-text-weight-anim` | Weight animation on reading text forbidden |
| Size | `--type-vf-size-budget` | `under-120kb` | Per-family variable file ceiling |
| Grade | `--type-vf-grade-axis` | `emphasis-only` | GRAD axis for subtle emphasis, not hierarchy |
| Fallback | `--type-vf-fallback` | `size-adjust-tuned` | Same fallback discipline as static |
| Support | `--type-vf-support-policy` | `modern-browsers` | Variable fonts have universal modern support |

Consume them by linking `assets/css/variable-fonts.css` once at the app root, then referencing `--type-vf-named-weights` and `--type-vf-optical` from text roles — product code never writes a raw `font-variation-settings` value unless it passes the review-gated token. If the file exceeds `--type-vf-size-budget`, trim the axis range to the weights the product actually uses.

## 4. Composition

- **Composes with type-scale:** named instance tokens plug into the scale's text roles — weight 600 at 25px is one role definition, not a font-variation-setting scattered in components.
- **Composes with webfont-loading:** one variable file simplifies the loading pipeline (fewer requests, same subsets); the loading skill's subset strategy applies to the single file.
- **Composes with skill-design-tokens guide 02:** the weight budget in tokens maps to the variable axis range — if the scale needs 400/600/700, the axis must at least cover that range.

## 5. Signature Patterns

- **Tokenized instances:** font-weight tokens (400/600/700) expose only reviewed axis points; raw axis values (`font-weight: 537`) fail lint — the lint is the named-instance contract.
- **Optical-first display:** for families with opsz, `font-optical-sizing: auto` handles display/text cuts — `--type-vf-optical` documents that this token replaces the need for separate display face files.

## 6. Real-World Use Cases

- **Products needing rich hierarchy** (many weights) without payload multiplication — one variable file vs. three statics at ~20KB each.
- **Editorial/display-heavy products** benefiting from optical sizing — news, publishing, and reading apps where display vs. body rendering matters.
- **Reducing font requests in performance-critical apps** — one request replaces five, cutting font-loading round-trips.

## 7. Combination Notes

### With other typography skills

- **Good with type-scale, webfont-loading, font-pairing, and line-height:** the named-instance token set plugs directly into the scale; one file reduces the loading pipeline; the face's optical behavior affects the scale's size decisions.
- **Good with letter-spacing, visual-hierarchy, readability-legibility, and fluid-responsive:** tracking and leading adapt to the variable face's optical cuts; fluid type benefits from the axis range covering every breakpoint weight.
- **Good with numeric-tabular, accessible-typography, multilingual-vietnamese, and fluid-responsive:** variable face features (tnum, slashed-zero) apply the same as on statics; named instances protect a11y predictability; optical sizing aids multilingual text at every size.
- **Avoid list is empty:** variable fonts compose cleanly with all typography skills; only misapplied axis values (537, weight animation) are the risk, prevented by the named-instance and animation-policy tokens.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and brutalism-ui:** minimalism and flat-design benefit from the single-file performance gain; brutalism-ui pairs variable weight contrast with the wght axis for dramatic headings.
- **Caution with skeuomorphism:** skeuomorphic styles may prefer specific static weight cuts that evoke physical type; variable flexibility can work against that specific aesthetic intent — validate with the brand team first.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** when variable-font text reveals itself, the easing curves apply to opacity/scale rather than weight — the two properties compose cleanly.
- **Caution with ambient-motion:** ambient animations should never drive `font-variation-settings` (weight, slnt) as a continuous property — weight-axis animation on text is the no-text-weight-anim policy in motion form.

## 8. Anti-Patterns

- **Double loading** — variable file + static weights shipped together
- **Axis playground** — unreviewed wght values (537) appearing wherever a developer felt like it
- **Weight-animated paragraphs** — body text morphing weight and reflowing every frame
- **Max-range files** — loading wght 100-900 when the product uses 3 instances

### Accessibility Notes

Named instances protect predictability: screen magnifier and low-vision users rely on consistent weights — weight animation on text also violates reduced-motion norms (perpetual motion). Variable fonts are universally supported in modern browsers, so the named-instance contract holds everywhere. The fallback rule: if variable font behavior is unpredictable in a target browser, fall back to static weights of the same family — identical tokens, different delivery mechanism. The token set does not change; only the loading strategy degrades.

## 9. Code Examples

### Example 1 — Variable font with named instances and optical sizing

Tokens: `assets/css/variable-fonts.css`

```html
<h1 class="display">Recursive Display</h1>
<p class="body">Body text with optical sizing active.</p>
<style>
  @import url("assets/css/variable-fonts.css");

  /* Load one variable file; never also load static weights */
  @font-face {
    font-family: "Recursive";
    src: url("/fonts/Recursive-Variable.woff2") format("woff2-variations");
    font-weight: 300 1000;
    font-display: swap;
  }

  body { font-family: Inter, system-ui, sans-serif; }

  .display {
    /* Named instance from --type-vf-named-weights: 700 is a safe reviewed point */
    font-size: 3rem;
    font-weight: 700; /* uses wght axis at 700 */
    /* Optical sizing active when opsz axis exists — free micro-typography */
    font-optical-sizing: auto;
    line-height: 1.1;
    color: #171717;
  }

  .body {
    font-size: 1.125rem;
    font-weight: 400;
    font-optical-sizing: auto;
    line-height: 1.6;
    color: #404040;
  }

  /* Guard: reject non-named axis values at lint time */
  .illegal {
    font-weight: 537; /* ❌ 537 is not in --type-vf-named-weights */
  }
</style>
```

### Example 2 — Weight animation is forbidden; grade axis for emphasis only

```html
<div class="card-highlight">
  <p class="card-emphasis">Important callout text</p>
</div>
<script>
  // Policy: NEVER animate font-weight on reading text.
  // Wrong — this is the anti-pattern in motion form:
  //   el.style.transition = "font-weight 300ms ease";
  //   el.style.fontWeight = "700"; // reflows every frame

  // Correct — animate color/opacity for emphasis instead:
  const card = document.querySelector(".card-emphasis");
  card.animate(
    [{ opacity: 0.6, color: "#525252" }, { opacity: 1, color: "#171717" }],
    { duration: 400, easing: "ease-out", fill: "forwards" }
  );

  // Grade axis for subtle emphasis (does not reflow):
  // GRAD axis: values like 0 to 1 — subtle weight change, no layout shift
  if (CSS.supports("font-synthesis: none")) {
    card.style.fontVariationSettings = "'GRAD' 0.5";
  }
</script>
<style>
  .card-highlight {
    background: #F5F5F5;
    border-left: 3px solid #2563EB;
    padding: 16px 20px;
    border-radius: 0 8px 8px 0;
    font-family: Inter, system-ui, sans-serif;
    font-size: 1rem;
    line-height: 1.5;
  }
  .card-emphasis {
    margin: 0;
    font-weight: 600; /* Named instance — safe, no axis playground */
    color: #171717;
    /* font-optical-sizing: auto from --type-vf-optical */
  }
</style>
```

## 10. Implementation Checklist

- [ ] One variable file loads per family; static weights of that same family are absent from the loading pipeline — zero double-loading.
- [ ] All `--type-vf-named-weights` (400, 600, 700) are tested and rendering correctly in the target faces.
- [ ] `--type-vf-optical: auto` is set on all body text roles; opsz axis coverage is verified in the font scorecard.
- [ ] No raw `font-variation-settings` values appear in product code without passing the review-gated token check.
- [ ] `--type-vf-animation-policy: no-text-weight-anim` is enforced: no code animates font-weight on reading text; emphasis uses color/opacity.
- [ ] Variable file size is under `--type-vf-size-budget` (120KB); axis range is subset to the weights the product uses (not 100-900 when 400/600/700 suffice).
- [ ] Fallback font has `size-adjust` and `ascent-override` tuned so fallback metrics match the variable face — CLS is measured at 200% zoom.
- [ ] Lint gate rejects any `font-variation-settings` with a wght value not in `--type-vf-named-weights`.