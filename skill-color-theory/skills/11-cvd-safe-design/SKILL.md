---
name: cvd-safe-design
description: Designing for the 8% who see color differently: CVD types, simulation testing, safe hue pairs, and palettes that survive deuteranopia.
tags: [cvd, colorblind, accessibility, palettes, simulation]
related: [data-viz-palettes, semantic-color-system, oklch-perceptual]
---

# Color Theory Skill: Color Vision Deficiency Safety

## 1. Definition

Roughly 8% of men and 0.5% of women have color vision deficiency: deuteranopia/protanopia (red-green confusion), tritanopia (blue-yellow), and monochromacy (rare). CVD-safe design builds palettes and signals that remain distinguishable under these conditions: verified hue pairs, lightness separation as the backbone, simulation testing as a gate, and the standing rule that color never carries meaning alone.

## 2. Core Principles

- **Lightness is the backbone:** colors differing in L remain distinguishable under every CVD type - lightness separation is the primary differentiation channel.
- **The safe hue axes:** blue↔orange, blue↔yellow, and purple-ish blue vs teal survive red-green CVD; red↔green pairs are pre-disqualified.
- **Simulate, don't imagine:** every palette passes through deuteranopia + protanopia + tritanopia simulation (tools: Chrome DevTools, Sim Daltonism) before adoption.
- **Red-green pairs are forbidden as differentiators:** status/error vs success must separate by more than hue - icon, text, position, lightness.
- **Charts and status are the hot zones:** multi-series charts, semantic badges, and heatmaps are where CVD users lose meaning fastest.
- **Never color-alone, always:** CVD safety is WCAG 1.4.1 applied with the most common failure in mind - multi-signal delivery is the floor, not an enhancement.
- **Test with the actual palette, not principles:** two palettes can both 'avoid red-green' and still collapse under simulation - the gate is simulated, documented results.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Safety | `--clr-cvd-simulation-gate` | `deutan-protan-tritan` | Three simulation passes required for adoption |
| Safety | `--clr-safe-pair-axis` | `blue-orange` | The default CVD-safe opposing axis |
| Safety | `--clr-unsafe-pairs` | `red-green-primary` | Disallowed as differentiators |
| Safety | `--clr-lightness-separation` | `0.08+-L-between-series` | Series distinguishable by L alone |
| Safety | `--clr-non-color-signal` | `icon-text-position` | Meaning carried on 3 channels minimum |
| Safety | `--clr-chart-cvd-check` | `per-chart-per-release` | Dashboards re-simulated with real data colors |
| Safety | `--clr-status-cvd-check` | `badge-simulation-pass` | Status badges distinguishable without hue |
| Safety | `--clr-cvd-prevalence-target` | `8%-men-covered` | Design floor: all common CVD types pass |
| Safety | `--clr-pattern-overlay-option` | `texture-for-critical-charts` | Patterns on top of color for critical series |
| Safety | `--clr-cvd-audit-cadence` | `per-palette-change` | Simulation re-run on every palette edit |

Consume them by linking `assets/css/cvd-safe-design.css` once at the app root, then referencing `var(--clr-...)` from simulation scripts, review templates, and chart components — the gates and cadences are configuration, not memory. A series color not meeting the lightness-separation rule does not enter the chart; a badge that fails simulation does not ship.

## 4. Composition

- **Composes with data-viz-palettes:** viz palettes are the strictest CVD customers - simulation gates every set.
- **Composes with semantic-color-system:** status colors are validated for deuteranopia, not just contrast.
- **Composes with skill-accessibility guide 02:** color-contrast covers the ratios; this guide covers the perceptual confusion dimension.

## 5. Signature Patterns

- **Simulation CI:** palette files run through CVD simulation in the pipeline; new palettes ship with simulation screenshots attached to the PR.
- **Blue-orange house rule:** when no domain constraint dictates otherwise, diverging and opposing pairs default to the blue-orange axis.

## 6. Real-World Use Cases

- **Dashboards and charts (the highest CVD risk surfaces).**
- **Status/feedback systems: badges, banners, and form states.**
- **Audit: CVD simulation walkthrough of every color-meaning surface.**

## 7. Combination Notes

### With other color-theory skills

- **Good with data-viz-palettes:** the strongest pairing in the set — viz surfaces (multi-series charts, heatmaps) are where CVD users lose meaning fastest, so simulation gates every categorical set before adoption.
- **Good with semantic-color-system:** status badges are the second hot zone; error-red vs success-green is exactly the axis red-green CVD cannot read, so status systems must separate by icon, text, position, and lightness — not hue.
- **Good with oklch-perceptual and contrast-models:** lightness is the CVD backbone, and OKLCH's L axis is where separation is engineered and measured; the contrast manifest proves pairs pass, simulation proves they survive confusion.
- **Good with brand-ramp-construction, dark-mode-palette, gray-ramp-neutrals, color-harmony, gradient-theory, color-psychology, and cultural-color-meaning:** every palette-producing skill ships candidates that must pass the simulation gate — CVD safety is a downstream check that never blocks upstream creativity, only unverified adoption.
- **No caution or avoid entries:** simulation is compatible with any palette strategy; the only failure is skipping the gate.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** flat, untextured styles lean fully on color for series identity, which makes lightness-separated, simulation-tested palettes essential rather than optional — the styles' restraint also keeps category counts within the 6-8 ceiling.
- **Caution with collage-art:** layered, clashing collage palettes multiply the confusable-pair surface and often resist systematic validation; if a collage look is required, the meaning-bearing marks (series, status) still get CVD-verified colors while decoration stays decoration.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** animated series entrance (drawing lines, growing bars) preserves each series' lightness identity throughout the motion, so CVD distinguishability holds during animation, not only at rest.
- **Caution with any animation that recolors series mid-flight:** if a chart animation interpolates colors between series, transient frames can pass through confusable pairs — either animate position/length only, or keep series hue+lightness fixed and animate geometry.

## 8. Anti-Patterns

- **Red-green charts** — series distinguished by exactly the axis CVD users cannot read
- **Simulation theater** — one glance at a CVD filter, no documented pass criteria
- **Hue-only badges** — status communicated by color chip alone
- **8%-who-cares** — deprioritizing the largest single-vision-impairment group in UI

### Accessibility Notes

CVD safety is core accessibility (WCAG 1.4.1's most common real-world failure): every hue-meaning pairing must survive deuteranopia simulation - this guide turns that from aspiration into a gate. The gate is concrete, not aspirational: three simulation passes (deutan, protan, tritan) with documented pass criteria, re-run on every palette change and with real data colors per chart release. The fallback rule completes the discipline: when a required pairing cannot be made CVD-distinguishable, add a non-color channel (pattern, label, position) strong enough to carry the meaning without the hue - then re-simulate. Meaning must always survive on at least three channels (icon, text, position), because simulation failures are discovered after design, not before — the multi-channel floor is what makes the inevitable palette miss survivable.

## 9. Code Examples

### Example 1 — CVD-safe categorical chart demo

```html
<div class="viz">
  <h2>Quarterly revenue by region</h2>
  <div class="chart" role="img" aria-label="Bar chart: four regions, revenue in millions. Each bar is directly labeled.">
    <div class="series" style="--h: 82%"><i class="bar emea"></i><b>EMEA · 82</b></div>
    <div class="series" style="--h: 64%"><i class="bar apac"></i><b>APAC · 64</b></div>
    <div class="series" style="--h: 41%"><i class="bar amer"></i><b>Americas · 41</b></div>
    <div class="series" style="--h: 27%"><i class="bar latam"></i><b>LATAM · 27</b></div>
  </div>
  <p class="note">Series differ in hue AND lightness (≥0.08 L apart) and carry direct labels — no legend, no red-green pair.</p>
</div>
<style>
  .viz { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 440px; }
  .chart { display: flex; gap: 16px; align-items: flex-end; height: 180px; padding: 8px 0; }
  .series { display: flex; flex-direction: column; align-items: center; gap: 6px; height: 100%; justify-content: flex-end; }
  .bar { width: 44px; height: calc(var(--h)); border-radius: 4px 4px 0 0; }
  /* blue-orange CVD-safe axis with lightness separation */
  .emea  { background: #1d4ed8; } /* dark blue   */
  .apac  { background: #93c5fd; } /* light blue  */
  .amer  { background: #c2410c; } /* dark orange */
  .latam { background: #fdba74; } /* light orange*/
  .series b { font-size: 12px; font-weight: 600; color: #171717; }
  .note { color: #525252; font-size: 12px; }
</style>
```

### Example 2 — Status badges (icon+text+color triple) + deuteranopia simulation

```html
<div class="badges">
  <span class="badge success" role="status">✔ Deployed</span>
  <span class="badge warning" role="status">▲ Draining</span>
  <span class="badge danger" role="status">✖ Failed</span>
</div>
<div class="sim">
  <h2>Deuteranopia simulation</h2>
  <div class="row" id="original">
    <span class="swatch" style="background:#15803d"></span>
    <span class="swatch" style="background:#b45309"></span>
    <span class="swatch" style="background:#b91c1c"></span>
    <em>original</em>
  </div>
  <div class="row" id="simulated">
    <span class="swatch" style="background:#15803d"></span>
    <span class="swatch" style="background:#b45309"></span>
    <span class="swatch" style="background:#b91c1c"></span>
    <em>deuteranopia</em>
  </div>
</div>
<style>
  body { font: 14px/1.5 Inter, system-ui, sans-serif; padding: 16px; }
  .badges { display: flex; gap: 8px; }
  .badge { padding: 4px 12px; border-radius: 999px; font-weight: 600; }
  .success { background: #dcfce7; color: #166534; border: 1px solid #15803d; }
  .warning { background: #fef3c7; color: #92400e; border: 1px solid #b45309; }
  .danger  { background: #fee2e2; color: #991b1b; border: 1px solid #b91c1c; }
  .sim { margin-top: 16px; }
  .row { display: flex; gap: 8px; align-items: center; margin-bottom: 6px; }
  .swatch { width: 32px; height: 20px; border-radius: 4px; display: inline-block; }
  em { font-size: 12px; color: #525252; }
</style>
<script>
  // Deuteranopia approximation via an RGB→LMS→RGB simulation matrix
  // (Brettel/Viénot-style linear approximation, applied per channel)
  const M = [
    0.625, 0.375, 0.000,
    0.700, 0.300, 0.000,
    0.000, 0.300, 0.700,
  ];
  document.querySelectorAll('#simulated .swatch').forEach(el => {
    const bg = getComputedStyle(el).backgroundColor.match(/\d+/g).map(Number);
    const [r, g, b] = [0, 3, 6].map(i =>
      Math.round(M[i] * bg[0] + M[i + 1] * bg[1] + M[i + 2] * bg[2]));
    el.style.background = `rgb(${r}, ${g}, ${b})`;
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every categorical palette passes all three simulations (`--clr-cvd-simulation-gate`: deutan, protan, tritan) with documented criteria before adoption.
- [ ] Chart series separate by lightness (≥0.08 L, `--clr-lightness-separation`), never by hue alone.
- [ ] No red↔green pair is used as a differentiator anywhere (`--clr-unsafe-pairs` is enforced by review).
- [ ] Opposing/diverging pairs default to the blue↔orange axis (`--clr-safe-pair-axis`) unless a domain constraint is documented.
- [ ] Status badges ship as icon+text+color triples (`--clr-non-color-signal`) and pass `--clr-status-cvd-check`.
- [ ] Dashboards re-run simulation per chart per release with real data colors (`--clr-chart-cvd-check`).
- [ ] Critical charts carry a pattern/texture overlay option (`--clr-pattern-overlay-option`).
- [ ] Simulation re-runs on every palette edit (`--clr-cvd-audit-cadence`), with screenshots attached to the PR.
