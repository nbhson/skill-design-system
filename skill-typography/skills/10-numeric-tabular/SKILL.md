---
name: numeric-tabular
description: Proportional vs tabular figures, OpenType features, and data-typography: numbers that align in tables and count in dashboards.
tags: [typography, numeric, tabular-figures, opentype, data-typography]
related: [type-scale, font-pairing, variable-fonts, accessible-typography, fluid-responsive]
---

# Typography Skill: Numeric & Tabular Figures

## 1. Definition

Numeric typography is its own craft: tables need tabular (monospaced-width) figures so columns align; dashboards need them for count-ups and comparisons; prose needs proportional figures for natural rhythm. OpenType features (tnum, lnum, onum, zero, frac) decide which rendering a face produces — and default proportional figures in a data table is the classic misalignment nobody can name.

## 2. Core Principles

- **Tables and dashboards get tnum:** `font-variant-numeric: tabular-nums` on all numeric columns — digits share one width and align.
- **Prose keeps proportional figures:** proportional digits read better in sentences; do not tnum the blog body.
- **Lining figures for data, oldstyle for editorial:** lining (uniform height) suits tables and finance; oldstyle suits book typography.
- **Slashed or dotted zero for identifiers:** `font-variant-numeric: slashed-zero` disambiguates O/0 in codes, tokens, and IDs.
- **Count-ups animate in tabular space:** number animations (skill-animation data-animation) jitter unless digits are tabular-width.
- **Monospace for codes and tokens:** IDs, hashes, and API keys use the mono token — copying accuracy beats aesthetics.
- **Currency and units outside the digits:** '1,234,567 VND' — unit text uses the text face, digits keep tabular alignment.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Figures | `--type-figures-table` | `tabular-nums` | All data tables, dashboards, timelines |
| Figures | `--type-figures-prose` | `proportional-nums` | Default for running text |
| Figures | `--type-figures-lining` | `lining-nums` | Data and finance contexts |
| Figures | `--type-figures-oldstyle` | `oldstyle-nums` | Editorial long-form only |
| Figures | `--type-figures-zero` | `slashed-zero` | Identifiers, codes, config values |
| Numeric | `--type-numeric-mono` | `font-family-mono` | IDs, hashes, tokens, API keys |
| Display | `--type-kpi-display` | `tnum + semibold` | Dashboard KPIs: tabular + weight for stability |
| Animation | `--type-countup-alignment` | `tabular-required` | Animated numbers jitter without tnum |
| Fractions | `--type-fraction-policy` | `diagonal-fractions` | frac feature for recipes/measures |
| Units | `--type-unit-typography` | `text-face-units` | Units/currency in text face, digits tabular |

Consume them by linking `assets/css/numeric-tabular.css` once at the app root, then referencing `var(--type-figures-table)`, `var(--type-kpi-display)`, and `var(--type-numeric-mono)` from data UI and table components — product code never writes a raw `font-variant-numeric` value. If tabular alignment breaks, the face lacks tnum support and the mono fallback applies instead.

## 4. Composition

- **Composes with type-scale and font-pairing:** figure features are declared per face — verify the chosen face supports tnum before adoption; a face without tnum is disqualified from data surfaces regardless of aesthetics.
- **Composes with skill-component-recipes guide 03 (tables) and guide 12 (charts):** tabular figures are a hard requirement in those recipes, not an optional enhancement.
- **Composes with skill-animation data-animation:** count-up choreography assumes tabular-width digits; the `--type-countup-alignment` token documents that requirement for the motion engineer.

## 5. Signature Patterns

- **Data-typography utility:** `.num-table` / `.num-kpi` classes bundle `font-variant-numeric` + face + size, so data UI consumes one class — never a raw feature value.
- **Feature support gate:** family adoption checks tnum/zero coverage in the scorecard (font-pairing) — a data-product face without tnum is disqualified at selection, not at render time.

## 6. Real-World Use Cases

- **Financial dashboards and tables** where column alignment is trust — a misaligned decimal column is a data integrity signal.
- **Analytics products with animated KPI count-ups** — tabular digits guarantee every frame counts up without jitter.
- **Developer tools rendering IDs, hashes, and config values** — mono face + slashed-zero prevents copy errors on ambiguous pairs.

## 7. Combination Notes

### With other typography skills

- **Good with type-scale, font-pairing, line-height, and visual-hierarchy:** tabular figures slot into text roles without conflict; the scale's numeric display step uses `--type-kpi-display` as its natural expression.
- **Good with variable-fonts:** variable axes can expose weight without forcing proportional figures on data surfaces — the features are independent.
- **Good with accessible-typography, fluid-responsive, webfont-loading, and multilingual-vietnamese:** tabular alignment aids comprehension (a11y), fluid type needs tnum at every breakpoint, variable fonts simplify subset loading, and Vietnamese numbers benefit from tabular treatment the same way Arabic does. The caution/avoid lists are empty by design: numeric typography has no forbidden partners, only misapplied figures (tnum in prose, proportional in tables — e.g. oldstyle figures serve readability in editorial prose but clash with strict tabular tables, so pick lining for tables and oldstyle for long-form).

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** data-first styles value alignment and clarity; tabular figures serve the product's functional aesthetic.
- **Caution with collage-art:** collage-art may deliberately use proportional figures at large display sizes as a style gesture — if so, keep prose and table roles untouched and apply the display exception consciously.

### With motion skills (companion repo skill-animation)

- **Good affinity with data-animation:** count-up choreography is the primary use case; `--type-countup-alignment: tabular-required` is the contract the motion engineer implements.
- **Caution beyond that:** ambient-motion and text-reveal animations must not animate `font-variant-numeric` as a property — digit-width changes reflow the layout.

## 8. Anti-Patterns

- **Proportional tables** — default figures in data columns - columns shimmer with misalignment
- **Jittering count-ups** — animated numbers without tabular-nums twitching on every frame
- **tnum everywhere** — tabular figures in prose making sentences stiff
- **Ambiguous zeros** — O/0 confusion in rendered IDs where slashed-zero cost nothing

### Accessibility Notes

Aligned numeric columns are a comprehension aid for dyslexic and low-vision users; slashed-zero removes transcription errors — data typography is cognitive accessibility in disguise. The fallback rule: if the chosen face lacks OpenType numeric features (no `tnum`, `zero`, `lnum`), switch data surfaces to the `--type-numeric-mono` face — monospace digits are tabular by construction and available everywhere the web runs. Mono substitution is a layout-preserving degradation, not a broken fallback.

## 9. Code Examples

### Example 1 — Data table with tabular figures and slashed zeros

Tokens: `assets/css/numeric-tabular.css`

```html
<table class="transactions">
  <thead>
    <tr><th>TXN ID</th><th>Date</th><th>Amount</th><th>Balance</th></tr>
  </thead>
  <tbody>
    <tr><td>TXN_9A2F</td><td>2024-11-01</td><td>−1,250.00</td><td>4,832.10</td></tr>
    <tr><td>TXN_7B1E</td><td>2024-11-02</td><td>+3,400.00</td><td>8,232.10</td></tr>
  </tbody>
</table>
<style>
  .transactions { width: 100%; border-collapse: collapse; font: 14px/1.5 Inter, system-ui, sans-serif; }
  .transactions th {
    text-align: left;
    font: 600 0.75rem/1.5 Inter, system-ui, sans-serif;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #525252;
    border-bottom: 2px solid #E5E5E5;
    padding: 10px 14px;
  }
  /* Numeric columns: tabular alignment + slashed zero */
  .transactions :is(th, td):nth-child(3),
  .transactions :is(th, td):nth-child(4) {
    text-align: right;
    font-variant-numeric: var(--type-figures-table) var(--type-figures-zero);
  }
  /* TXN IDs: monospace face — copying accuracy beats aesthetics */
  .transactions td:first-child {
    font-family: var(--type-numeric-mono);
    font-variant-numeric: var(--type-figures-zero);
  }
  .transactions td { border-bottom: 1px solid #E5E5E5; padding: 12px 14px; color: #171717; }
</style>
```

### Example 2 — KPI count-up using tabular figures

```html
<div class="kpi-row">
  <div class="kpi-card">
    <p class="kpi-label">Monthly Revenue</p>
    <p class="kpi-value" id="kpi-revenue">0</p>
  </div>
  <div class="kpi-card">
    <p class="kpi-label">Active Users</p>
    <p class="kpi-value" id="kpi-users">0</p>
  </div>
</div>
<script>
  const easeOut = (t) => 1 - Math.pow(1 - t, 3);

  function countUp(el, target, duration = 1400) {
    const start = performance.now();
    (function step(now) {
      const progress = Math.min((now - start) / duration, 1);
      el.textContent = Math.round(easeOut(progress) * target).toLocaleString();
      if (progress < 1) requestAnimationFrame(step);
    })(performance.now());
  }

  // Guard: the alignment token must be present — without it the count-up jitters.
  const computed = getComputedStyle(document.documentElement)
    .getPropertyValue("--type-countup-alignment").trim();
  console.assert(computed === "tabular-required", "Count-up requires tabular figures");

  countUp(document.getElementById("kpi-revenue"), 843200);
  countUp(document.getElementById("kpi-users"), 12458);
</script>
<style>
  .kpi-row { display: flex; gap: 24px; }
  .kpi-card {
    background: #FAFAFA; border: 1px solid #E5E5E5; border-radius: 12px;
    padding: 20px 24px; min-width: 200px;
  }
  .kpi-label { margin: 0 0 8px; font-size: 0.875rem; font-weight: 500; color: #525252; }
  /* KPI value: tabular + semibold = --type-kpi-display */
  .kpi-value {
    margin: 0;
    font-size: 2rem;
    font-weight: 600;
    font-variant-numeric: var(--type-figures-table); /* tabular-required: no width shifts */
    color: #171717;
  }
</style>
```

## 10. Implementation Checklist

- [ ] Every data table and dashboard column carries `--type-figures-table` (tabular-nums); no raw numeric column without the token exists in production code.
- [ ] `--type-figures-zero` (slashed-zero) applies to all ID/code/token columns; a lint rule catches un-slashed monospace identifiers.
- [ ] All numeric animation (count-up, ticker, score) requires `--type-countup-alignment: tabular-required` to be set on the animating element.
- [ ] `--type-numeric-mono` wraps all IDs, hashes, API keys; human-copyable strings are monospace by contract.
- [ ] Font family adoption checks tnum and zero support in the scorecard; a face without tnum is rejected from data-product roles.
- [ ] Fraction feature (`--type-fraction-policy: diagonal-fractions`) applies to recipe/measure UIs; a lint gate prevents `frac` on non-measurement contexts.
- [ ] Prose text roles use `--type-figures-prose`; tnum is never applied to running body text.
- [ ] At 200% text zoom, all tabular columns maintain alignment — mono fallback is verified when the face lacks tnum.