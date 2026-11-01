---
name: fluid-responsive
description: clamp()-interpolated type that scales with the viewport between scale stops — smooth scaling without breakpoint soup.
tags: [typography, fluid-type, clamp, responsive, viewport]
related: [type-scale, line-height, letter-spacing]
---

# Typography Skill: Fluid & Responsive Typography

## 1. Definition

Fluid typography interpolates font sizes continuously with the viewport width using clamp(min, fluid, max): text grows smoothly between two scale stops instead of jumping at breakpoints. Applied to heading roles (not body — body stays fixed at readable sizes), it eliminates the 'title looks huge on mobile / timid on desktop' problem while keeping every size anchored to the modular scale. The craft is in the arithmetic: the clamp's endpoints are scale steps (never invented sizes), the vw coefficient is computed from a documented viewport range, and the whole construction is rem-based so user font-size preferences still multiply through.

## 2. Core Principles

- **Fluid applies to headings, not body:** body text is already optimal at 16-18px; fluid body drifts into unreadable territory.
- **clamp() between two scale stops:** clamp(1.563rem, calc(1.2rem + 2vw), 3.052rem) — the endpoints ARE scale steps, nothing off-scale renders.
- **Compute the vw coefficient deliberately:** slope = (max - min) / (viewportMax - viewportMin); hand-tuned vw values break the scale.
- **Cap the growth:** the max clamp bound exists so 4K screens do not render 200px titles.
- **Test the extremes:** 320px and 2560px are the design targets, not 1440px alone.
- **Line-height rebalances at extremes:** tight display leading may need a higher value at min sizes — use clamp on line-height too when needed.
- **Access the user preference:** fluid type still multiplies with root font-size (rem-based) — WCAG 1.4.4 holds at every viewport.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Fluid strategy | `--type-fluid-strategy` | `headings-only` | Body stays fixed; headings interpolate |
| Fluid h1 | `--type-fluid-h1` | `clamp(2.441rem, 1.5rem + 3.5vw, 3.815rem)` | 39px -> 61px between 320-1440 |
| Fluid h2 | `--type-fluid-h2` | `clamp(1.953rem, 1.4rem + 2.5vw, 2.441rem)` | 31px -> 39px |
| Fluid h3 | `--type-fluid-h3` | `clamp(1.563rem, 1.3rem + 1.5vw, 1.953rem)` | 25px -> 31px |
| Fluid body fixed | `--type-fluid-body-fixed` | `1rem` | Body exempt from fluidity by policy |
| Viewport range | `--type-fluid-viewport-range` | `320px-1440px` | The documented design range |
| Fluid line-height | `--type-fluid-line-height` | `clamp(1.1, 1rem + 0.5vw, 1.25)` | Display leading loosens at small sizes |
| Min floor | `--type-fluid-min-floor` | `12px` | No interpolated value ever renders below 12px |
| Anchors | `--type-fluid-anchors` | `scale-stops-only` | Clamp endpoints must be modular-scale steps |
| Test points | `--type-fluid-test-points` | `320,768,1440,2560` | The four screenshot test widths |

Consume them by linking `assets/css/fluid-responsive.css` once at the app root, then referencing `var(--type-fluid-h1)` (and siblings) from heading roles — product code never writes a raw clamp() or vw value. The endpoints inside each token are modular-scale stops (2.441rem, 3.815rem...), so fluidity re-uses the scale instead of forking it; `--type-fluid-test-points` names the four widths every heading must be screenshotted at, and `--type-fluid-min-floor` is the hard floor code review checks interpolated values against.

## 4. Composition

- **Fluid typography consumes the modular scale's stops as clamp endpoints** — fluidity never introduces off-scale sizes. The scale is the contract; the clamp is just a continuous path between two of its points, which is what makes "nothing off-scale renders" verifiable rather than aspirational.
- **It composes with responsive-layout (skill-responsive_layout guides 01-03):** type fluidity is one axis of the layout system's responsiveness — grids reflow at breakpoints while type glides between them, and the two must be tuned against the same documented viewport range.
- **It composes with accessible-typography:** rem-based clamps preserve zoom and user-preference scaling (WCAG 1.4.4) — because the min/max bounds are in rem, a user who raises their root font size shifts the whole fluid range up proportionally rather than being clamped to fixed pixel caps.

Bundled properties travel with the fluid size: tracking (em-based) and line-height (unitless or clamped via `--type-fluid-line-height`) interpolate alongside without re-tuning, which is why heading roles — not raw h1 selectors — are the consumers.

## 5. Signature Patterns

- **Fluid role set:** only the heading roles (h1-h3) get fluid tokens; every other text role stays at fixed scale steps — simplicity by exclusion. Keeping the fluid set at three tokens means every interpolated size can be eyeballed, tested, and reviewed; a fully fluid system is unreviewable.
- **Slope-per-step:** precompute the vw slope per step for the documented viewport range; the formula lives beside the tokens. For h1: slope = (3.815 - 2.441) / (14.4 - 2) rem across 320-1440px, giving the `1.5rem + 3.5vw` form. Publishing the formula (as comments next to each token) turns every clamp from magic numbers into a checkable derivation — a reviewer can recompute it in one line.

## 6. Real-World Use Cases

- **Marketing sites:** hero titles that fill space gracefully from phone to desktop — the canonical case where breakpoint jumps are most visible.
- **Docs platforms:** consistent headings across any viewport without breakpoints — content teams never know the reader's window width.
- **Audit:** finding hand-tuned vw sizes whose endpoints are off-scale — the tell is a clamp whose bounds don't match any modular-scale step.

## 7. Combination Notes

### With other typography skills

- **Good with type-scale, line-height, and letter-spacing:** the clamp endpoints ARE scale steps, the display leading may clamp alongside (`--type-fluid-line-height`), and em-based tracking scales with the interpolated size without re-tuning — fluidity consumes all three as inputs and invents nothing.
- **Good with visual-hierarchy and readability-legibility:** fluid interpolation preserves the size *relationships* between ranks (all heading roles move together), so the hierarchy holds at 320px as at 2560px — while the body-stays-fixed policy keeps reading text inside the 16-18px readability window.
- **Good with font-pairing and variable-fonts:** interpolated sizes land between optical-size thresholds on variable fonts, letting the face's optical axis adjust continuously — often eliminating the need for separate display/text cuts.
- **Good with accessible-typography and multilingual-vietnamese:** rem-based clamps keep WCAG 1.4.4 intact at every viewport, and the min floor guarantees interpolated sizes never render below the 12px legibility floor where diacritic stacks would clip first.
- **No caution/avoid list:** fluid type has no incompatible partners — only misapplications (fluid body, unbounded vw, off-scale endpoints), each covered by an anti-pattern and a token guard.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and aurora-ui:** these styles lean on large, confident type and generous space; smooth interpolation keeps that presence on small screens without a jarring "mobile heading" downgrade. Aurora UI's soft gradients pair especially well with type that also moves continuously rather than snapping.
- **Caution with collage-art and brutalism-ui:** both styles may want deliberately fixed, confronting type sizes — a brutalist poster-style headline is part of the composition, not a responsive element; if fluidity conflicts with the style's intended scale relationships, pin those roles at fixed steps consciously.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** heading entrances can sync with the fluid range — a title animating in at a viewport between stops should settle at the interpolated size, and em-based motion (translate by line-height units) stays proportional to the fluid text.
- **Caution beyond that:** continuous scroll-driven font-size animation stacks on top of clamp() interpolation and produces jittery re-layout; treat the clamp as the resting state motion reveals, and never animate the same size axis that fluidity already interpolates.

## 8. Anti-Patterns

- **Fluid body text** — paragraphs shrinking to 13px on phones because everything interpolated
- **Unbounded vw** — text-[5vw] growing forever on 4K displays
- **Off-scale endpoints** — clamp bounds that are not scale steps, quietly forking the ramp
- **Fluid-only testing** — signing off at 1440px while 320px renders cramped or 2560px renders cartoonish

### Accessibility Notes

rem-based clamps are the trick that keeps fluid type accessible: because the min and max bounds are expressed in rem, the entire fluid range multiplies with the user's root font-size preference — a user at 150% gets a proportionally larger interpolated range, and WCAG 1.4.4 (resize text) holds at every viewport width rather than only at the designer's laptop. This is also why px-based vw formulas are banned: they pin the bounds in device pixels and silently override user scaling. Line-height participates too — unitless or clamped values re-balance as sizes interpolate, keeping the 1.5 body floor and diacritic headroom intact. The fallback rule: if a user override at 200% zoom collides with fluid bounds, the clamp max yields — cap fluidity lower or raise the max bound; user scaling never loses. The `--type-fluid-min-floor` (12px) is the last line of defense: no interpolated value ever renders below it regardless of viewport.

## 9. Code Examples

### Example 1 — Fluid hero heading with clamped leading

Tokens: `assets/css/fluid-responsive.css`

```html
<header class="hero">
  <h1 class="fluid-title">Analytics for teams that ship</h1>
  <p class="hero-body">Fixed at 16px — body text is exempt from fluidity by policy.</p>
</header>
<!-- Test points: 320 / 768 / 1440 / 2560 — screenshot all four before sign-off.
     At 320px: min bound (2.441rem = 39px). At 1440px+: max bound (3.815rem = 61px).
     2560px must render identical to 1440px — growth is capped. -->
<style>
  .hero {
    padding: 48px 24px;
    background: #FAFAFA;
    font-family: Inter, system-ui, sans-serif;
  }
  .fluid-title {
    /* Endpoints are modular-scale stops: 2.441rem (2xl) -> 3.815rem (4xl) */
    margin: 0 0 12px;
    font-size: var(--type-fluid-h1);
    line-height: var(--type-fluid-line-height); /* leading loosens at small sizes */
    letter-spacing: -0.025em; /* em-based: scales with the fluid size */
    max-width: 22ch;
    color: #171717;
  }
  .hero-body {
    margin: 0;
    font-size: var(--type-fluid-body-fixed); /* 1rem, never fluid */
    line-height: 1.5;
    color: #404040;
  }
</style>
```

### Example 2 — Rendered font-size logger for the four test widths

Tokens: `assets/css/fluid-responsive.css`

```html
<h1 class="fluid-title" id="probe">Quarterly overview</h1>
<p class="hint">Open the console; resize the window across the 4 test widths.</p>
<script>
  // Log the rendered font-size at the current viewport (devtools QA aid).
  const el = document.getElementById("probe");
  const MIN_FLOOR = 12; // --type-fluid-min-floor, px
  function logFluidSize() {
    const px = parseFloat(getComputedStyle(el).fontSize);
    const inside = innerWidth >= 320 && innerWidth <= 2560;
    console.log(
      `viewport ${innerWidth}px -> rendered ${px.toFixed(1)}px ` +
      `(bounds ${inside ? "within" : "OUTSIDE"} design range)`
    );
    console.assert(px >= MIN_FLOOR, "Fluid size fell below the 12px min floor");
    // Off-scale endpoint guard: rendered size must approach a scale stop at extremes.
    if (innerWidth <= 330) {
      console.assert(Math.abs(px - 39) < 1, "320px should render the min bound (39px)");
    }
    if (innerWidth >= 2550) {
      console.assert(Math.abs(px - 61) < 1, "2560px should render the max bound (61px)");
    }
  }
  addEventListener("resize", logFluidSize);
  logFluidSize();
</script>
<style>
  .fluid-title {
    font-size: var(--type-fluid-h2); /* clamp(1.953rem, 1.4rem + 2.5vw, 2.441rem) */
    line-height: 1.2;
    letter-spacing: -0.01em;
    margin: 0;
    color: #171717;
    font-family: Inter, system-ui, sans-serif;
  }
  .hint {
    margin: 8px 0 0;
    font: 14px/1.5 Inter, system-ui, sans-serif;
    color: #737373;
  }
</style>
```

## 10. Implementation Checklist

- [ ] Only heading roles (h1-h3) carry `--type-fluid-*` tokens; body renders at `--type-fluid-body-fixed` (1rem) everywhere.
- [ ] Every clamp() endpoint in `assets/css/fluid-responsive.css` is a modular-scale step (`--type-fluid-anchors: scale-stops-only`) — no invented sizes.
- [ ] Every vw coefficient is derived from `slope = (max - min) / (viewportMax - viewportMin)` over `--type-fluid-viewport-range` (320-1440px), with the formula documented beside the token.
- [ ] No interpolated value can render below `--type-fluid-min-floor` (12px).
- [ ] Display leading uses `--type-fluid-line-height` where tight leading risks clipping at small sizes.
- [ ] Screenshots pass at all four `--type-fluid-test-points` (320, 768, 1440, 2560) — sign-off at 1440px alone is rejected.
- [ ] All clamps are rem-based; zero px-bounded fluid sizes exist (WCAG 1.4.4 user scaling verified at 200% zoom).
- [ ] No scroll-driven or looping animation drives the same size axis a clamp interpolates.
