---
name: data-viz-palettes
description: Categorical, sequential, and diverging palettes built for comprehension: distinguishability, colorblind safety, and 3:1 against surfaces.
tags: [data-visualization, color, charts, cvd, accessibility]
related: [oklch-perceptual, cvd-safe-design, contrast-models]
---

# Color Theory Skill: Data Visualization Palettes

## 1. Definition

Data visualization needs palettes that encode meaning: categorical palettes give each series an equally-weighted, distinguishable identity; sequential ramps map magnitude to lightness; diverging palettes center a neutral midpoint between two hue extremes. Viz palettes have harder constraints than UI palettes — many colors at once, small marks, no labels — so they are engineered for distinguishability and CVD safety first, aesthetics second. Where a UI palette can lean on context and proximity to disambiguate, a chart palette must do the work through color structure alone.

## 2. Core Principles

- **Categorical = distinguishability:** series colors differ in hue AND lightness (not hue alone); 6–8 categories maximum before the palette collapses.
- **Sequential = lightness ramp with monotonic chroma:** magnitude reads through lightness order; perceptually uniform ramps (viridis-class) prevent banding lies.
- **Diverging needs a true neutral midpoint:** two hues diverging from a real center (white/neutral) — the midpoint is data's zero, not a random gray.
- **Colorblind-safe by construction:** test every palette through CVD simulation (guide 11); red-green categorical pairs are pre-disqualified.
- **Marks carry 3:1 against their surface:** chart series are UI graphical objects (WCAG 1.4.11) — every series color passes against the chart background.
- **Do not differentiate by color alone:** series get labels, patterns, or direct annotation — color is one channel of the encoding (a11y 1.4.1).
- **Chart palette is a token set, not ad hoc:** the categorical/sequential/diverging palettes are versioned tokens consumed by all charts — one source, consistent dashboards.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Categorical set | `--clr-categorical-set` | `8-hue-l-and-c-varied` | Differing in hue + lightness; CVD-verified |
| Categorical max | `--clr-categorical-max` | `8-series` | Beyond 8: small multiples, not more colors |
| Sequential ramp | `--clr-sequential-ramp` | `viridis-class-uniform` | Perceptually uniform; single-hue or multi-hue |
| Sequential steps | `--clr-sequential-steps` | `5-7-displayed` | Displayed steps; ramps store more |
| Diverging center | `--clr-diverging-center` | `true-neutral-midpoint` | Data zero = neutral; hues diverge outward |
| Diverging hues | `--clr-diverging-hues` | `opposing-hue-pair` | e.g. blue↔orange (CVD-safe axis) |
| Viz contrast floor | `--clr-viz-contrast-floor` | `3:1-vs-surface` | WCAG 1.4.11 for marks/series |
| Viz CVD check | `--clr-viz-cvd-check` | `deuteranopia-verified` | All palettes pass deuteranopia/protanopia simulation |
| Viz non-color channel | `--clr-viz-non-color-channel` | `label-or-pattern` | Direct labels/patterns accompany series color |
| Viz palette owner | `--clr-viz-palette-owner` | `token-set-versioned` | One viz palette set consumed by every chart |

Consume them by linking `assets/css/data-viz-palettes.css` and reading `var(--clr-viz-*)` plus the named series tokens (`var(--clr-viz-series-1)` … `var(--clr-viz-series-8)`) from every chart component — dashboards never pick colors chart-by-chart.

## 4. Composition

- **Composes with oklch-perceptual:** sequential ramps and categorical sets are OKLCH structures with documented lightness and chroma separation — the perceptual math is what makes "equally weighted" verifiable instead of vibes.
- **Composes with cvd-safe-design:** simulation testing is the shared gate, and viz palettes are its strictest customers — eight simultaneous series leave no room for a deuteranopia collision to hide in.
- **Composes with numeric-tabular (skill-typography guide 10):** tabular figures and aligned columns complete the data-reading surface; a correct palette over ragged, proportional digits still produces unreadable dashboards.

## 5. Signature Patterns

- **Blue-orange default axis:** the diverging pair that survives all CVD types — it is the default when no domain reason (political red/blue, thermal hot/cold) favors another, so divergence never has to be re-litigated per chart.
- **Series palette token set:** dashboards consume named series tokens (`viz-series-1..8`) so every chart re-colors consistently in one change — retheming dark mode or brand means editing the token set, not forty chart configs.

## 6. Real-World Use Cases

- **Analytics dashboards:** multi-series charts that stay distinguishable as series count grows.
- **Maps and heatmaps:** sequential/diverging ramps that encode magnitude and signed deviation honestly.
- **Audit:** hunting rainbow categorical chaos, lightness-lying sequential ramps, and red-green series pairs.

## 7. Combination Notes

### With other color-theory skills

- **Pairs with oklch-perceptual and contrast-models:** perceptual ramps supply the lightness order and the 3:1 floor is checked pair-by-pair — together they make the palette a checkable contract.
- **Pairs with cvd-safe-design:** the simulation gate is mandatory here; viz is where CVD failures are most visible because eight series sit side by side with no context to rescue them.
- **Pairs with gray-ramp-neutrals and brand-ramp-construction:** chart surfaces, gridlines, and axes come from the neutral ramp, while brand ramps seed the categorical set so dashboards feel owned.
- **Pairs with semantic-color-system, dark-mode-palette, and gradient-theory:** status-colored series, dark-theme chart variants, and smooth ramp endpoints all inherit this skill's distinguishability rules.
- **Pairs with color-harmony, color-psychology, and cultural-color-meaning:** categorical sets stay harmonious and semantically/culturally safe (danger red means danger in a chart too) even while maximizing separation.
- **No caution or avoid list:** every color-theory skill strengthens viz palettes; the failure mode is bypassing them (ad-hoc chart colors), not combining.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** flat, disciplined styles keep marks clean and let the palette — not decoration — carry the encoding; small palettes leave room for the 8 series to read.
- **Caution with collage-art:** collage layering puts series marks over unpredictable backgrounds, breaking the 3:1-vs-surface guarantee; if used, charts must sit on validated solid zones.

### With motion skills (companion repo skill-animation)

- **Good affinity with data-animation:** series tokens animate consistently across timelines — transitions between data states re-color through the same validated palette, so no intermediate state invents a color.
- **Caution with ambient-motion:** ambient color fields behind charts shift the surface the 3:1 floor was computed against; animated backgrounds must keep the chart surface static or re-validated.

## 8. Anti-Patterns

- **Rainbow categorical:** 12 hues at full saturation fighting for attention
- **Hue-only series:** 6 reds distinguished by nothing a human (or CVD human) can see
- **Lightness-lying ramps:** sequential gradients whose midpoints are darker than their ends
- **Dashboard-by-dashboard palettes:** every chart picking its own series colors

### Accessibility Notes

Viz palettes implement WCAG 1.4.11 (non-text contrast) and 1.4.1 (color alone) at the chart level: 3:1 marks, CVD-tested sets, and a non-color channel on every series — plus charts ship accessible data tables (a11y repo guide 09). In practice that means every series color is checked against the chart background before it ships, every series carries a direct label, pattern, or legend-linked annotation, and the underlying numbers are available to screen readers as a table rather than trapped in an SVG. The fallback rule: when categorical sets exceed 8 series, switch to small multiples or a legend-driven highlight model — more colors is never the fix.

## 9. Code Examples

### Example 1 — Categorical bar chart with a CVD-safe 8-series token set

Tokens: `assets/css/data-viz-palettes.css`

```html
<figure class="chart">
  <figcaption class="chart-title">Revenue by region (Q3, $M)</figcaption>
  <svg viewBox="0 0 420 240" role="img" aria-label="Bar chart of Q3 revenue by region">
    <g class="bars">
      <rect x="20"  y="40"  width="36" height="170" fill="var(--clr-viz-series-1)"/>
      <rect x="70"  y="90"  width="36" height="120" fill="var(--clr-viz-series-2)"/>
      <rect x="120" y="70"  width="36" height="140" fill="var(--clr-viz-series-3)"/>
      <rect x="170" y="120" width="36" height="90"  fill="var(--clr-viz-series-4)"/>
      <rect x="220" y="55"  width="36" height="155" fill="var(--clr-viz-series-5)"/>
      <rect x="270" y="105" width="36" height="105" fill="var(--clr-viz-series-6)"/>
      <rect x="320" y="85"  width="36" height="125" fill="var(--clr-viz-series-7)"/>
      <rect x="370" y="135" width="36" height="85"  fill="var(--clr-viz-series-8)"/>
    </g>
    <g class="labels" aria-hidden="true">
      <text x="38"  y="34">NA 42</text><text x="88"  y="84">EU 30</text>
      <text x="138" y="64">APAC 35</text><text x="188" y="114">LATAM 22</text>
      <text x="238" y="49">MEA 39</text><text x="288" y="99">JP 26</text>
      <text x="338" y="79">UK 31</text><text x="388" y="129">ANZ 21</text>
    </g>
  </svg>
</figure>
<style>
  /* Series token set — hue AND lightness varied, CVD-verified, 3:1 on the surface */
  :root {
    --clr-viz-series-1: #2563EB;  /* blue    */
    --clr-viz-series-2: #EA580C;  /* orange  */
    --clr-viz-series-3: #0D9488;  /* teal    */
    --clr-viz-series-4: #7C3AED;  /* violet  */
    --clr-viz-series-5: #65A30D;  /* olive   */
    --clr-viz-series-6: #DB2777;  /* magenta */
    --clr-viz-series-7: #B45309;  /* bronze  */
    --clr-viz-series-8: #475569;  /* slate   */
    --clr-viz-surface: #FAFAFA;
    --clr-viz-ink: #171717;
  }
  .chart { background: var(--clr-viz-surface); margin: 0; padding: 16px;
           border: 1px solid #D4D4D4; border-radius: 10px; max-width: 460px;
           font: 13px/1.4 Inter, system-ui, sans-serif; }
  .chart-title { color: var(--clr-viz-ink); font-weight: 600; margin-bottom: 10px; }
  .labels text { fill: var(--clr-viz-ink); font-size: 10px; font-weight: 600; }
</style>
```

### Example 2 — Sequential ramp and diverging axis with legend

Tokens: `assets/css/data-viz-palettes.css`

```html
<figure class="ramps">
  <figcaption class="ramps-title">Temperature anomaly (°C)</figcaption>
  <svg viewBox="0 0 420 150" role="img" aria-label="Sequential and diverging ramps with legend">
    <!-- Sequential: lightness order encodes magnitude (5 displayed steps) -->
    <g aria-hidden="true">
      <rect x="20"  y="30" width="50" height="24" fill="oklch(0.93 0.05 250)"/>
      <rect x="70"  y="30" width="50" height="24" fill="oklch(0.82 0.09 250)"/>
      <rect x="120" y="30" width="50" height="24" fill="oklch(0.71 0.12 250)"/>
      <rect x="170" y="30" width="50" height="24" fill="oklch(0.58 0.14 250)"/>
      <rect x="220" y="30" width="50" height="24" fill="oklch(0.45 0.15 250)"/>
      <text x="20" y="22" class="tick">Low</text>
      <text x="243" y="22" class="tick">High</text>
    </g>
    <!-- Diverging: blue ↔ orange around a true neutral midpoint (data zero) -->
    <g aria-hidden="true">
      <rect x="20"  y="90" width="40" height="24" fill="oklch(0.55 0.14 250)"/>
      <rect x="60"  y="90" width="40" height="24" fill="oklch(0.75 0.07 250)"/>
      <rect x="100" y="90" width="40" height="24" fill="oklch(0.93 0 0)"/>
      <rect x="140" y="90" width="40" height="24" fill="oklch(0.80 0.09 60)"/>
      <rect x="180" y="90" width="40" height="24" fill="oklch(0.60 0.16 45)"/>
      <text x="20" y="82" class="tick">−2</text>
      <text x="116" y="82" class="tick">0 (neutral)</text>
      <text x="196" y="82" class="tick">+2</text>
    </g>
    <text x="280" y="47"  class="legend">Sequential: L rises monotonically</text>
    <text x="280" y="107" class="legend">Diverging: neutral midpoint = zero</text>
  </svg>
</figure>
<style>
  .ramps { background: var(--clr-viz-surface, #FAFAFA); margin: 0; padding: 16px;
           border: 1px solid #D4D4D4; border-radius: 10px; max-width: 460px;
           font: 13px/1.4 Inter, system-ui, sans-serif; }
  .ramps-title { color: var(--clr-viz-ink, #171717); font-weight: 600; margin-bottom: 10px; }
  .tick, .legend { fill: var(--clr-viz-ink, #171717); }
</style>
```

## 10. Implementation Checklist

- [ ] One versioned viz token set (`var(--clr-viz-series-1)` … `8`, ramps) is the only source of chart colors.
- [ ] Categorical series differ in hue AND lightness; sets are capped at 8 with small multiples beyond.
- [ ] Sequential ramps are perceptually uniform with monotonic lightness; 5–7 steps displayed.
- [ ] Diverging palettes center on a true neutral midpoint (data zero), blue↔orange by default.
- [ ] Every series and mark passes 3:1 against its chart surface; all palettes pass deuteranopia/protanopia simulation.
- [ ] Every series carries a non-color channel (WCAG 1.4.1); charts ship accessible data tables.
- [ ] Dark-theme chart variants re-validated against `var(--clr-dark-bg)`.