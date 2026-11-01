---
name: svg-optimization
description: Lean vectors: SVGO discipline, viewBox hygiene, currentColor theming, sprite strategies, and what never to hand-edit.
tags: [svg, optimization, svgo, performance, theming]
related: [icon-library-management, empty-error-illustrations, mascot-character]
---

# Visual Asset Guide: SVG Optimization

## 1. Definition

Every kilobyte of icon and illustration ships to every user; unoptimized SVG bloat is pure waste. This guide covers the optimization pipeline: SVGO with a reviewed config (which transforms are safe), viewBox hygiene (no stray whitespace/precision bloat), currentColor + CSS-variable fills for theming, sprite sheets vs inline vs external use strategies, and the danger list - what hand-editing (or naive optimization) breaks: gradients, clip paths, and ARIA attributes.

## 2. Core Principles

- **SVGO runs with a reviewed config:** default settings strip ARIA and title elements - the config preserves accessibility nodes.
- **viewBox hygiene:** tight viewBox, 1-2 decimal precision, no editor metadata (Inkscape/Figma layers) shipped to production.
- **currentColor for single-color icons:** theming and dark mode come free; hardcoded fills are banned for mono glyphs.
- **CSS variables for multi-color art:** illustration fills mapped to variables enable theming without duplicating files.
- **The delivery strategy is deliberate:** inline SVG for styled/interactive glyphs, sprite for repeated mono icons, file/URL for large illustrations.
- **Never hand-edit generated output:** masters -> pipeline -> assets; editing the dist file means the fix dies at the next build.
- **Gradients and clip paths are fragile:** optimization transforms that flatten groups break them - tested exceptions in the config.
- **Measure the wins:** bundle budgets per page (icons < 50KB total typical) tracked in CI - optimization without measurement decays.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Optimizer | `--icon-optimizer` | `svgo-reviewed-config` | ARIA/title preserved |
| Viewbox hygiene | `--icon-viewbox-hygiene` | `tight+low-precision` | No editor metadata in prod |
| Mono fill | `--icon-mono-fill` | `currentColor` | Theming free for single-color icons |
| Multicolor fill | `--icon-multicolor-fill` | `css-variables` | Theme-capable illustrations |
| Delivery strategy | `--icon-delivery-strategy` | `inline\|sprite\|file-by-use` | Deliberate per slot |
| No hand edit | `--icon-no-hand-edit` | `masters-to-pipeline` | Dist edits die at next build |
| Fragile features | `--icon-fragile-features` | `gradients+clip-paths-tested` | Config exceptions documented |
| Icon budget | `--icon-icon-budget` | `<50kb-per-page` | Tracked in CI |
| Sprite strategy | `--icon-sprite-strategy` | `symbol+use-for-repeat` | Repeated mono icons |
| Compression check | `--icon-compression-check` | `gzip-in-budget` | Budgets measured gzipped |

Consume them by linking `assets/css/svg-optimization.css`, which defines the variable-fill contract (`--icon-multicolor-fill: css-variables`) and the mono rule (`--icon-mono-fill: currentColor`); components reference `var(--icon-<role>)` in build scripts and review tooling. The tokens are the pipeline's contract - a config change that violates one (say, dropping ARIA preservation) fails review against the token table, not against a memory of what SVGO defaults do.

## 4. Composition

- **Composes with icon-library-management (guide 03):** the export pipeline IS this optimization - one automated step. Masters land in the library; SVGO with the reviewed config produces the dist assets; there is no gap where hand-editing could happen.
- **Composes with skill-design-tokens:** variable-driven fills consume semantic tokens - theming consistency end to end. An illustration fill referencing `var(--icon-*)` or a `--dt-color-*` alias re-themes with the rest of the system in one re-point.
- **Composes with animation-integration (guide 10):** animated SVGs need optimization exceptions - the config knows which files, so a draw-in animation's stroke attributes survive the transform pass while static siblings still compress fully.

## 5. Signature Patterns

- **The build pipeline:** masters -> SVGO (reviewed config) -> themed fills -> sprites/components -> CI budget check - fully automated, never manual. The pipeline is the only path from design tool to production asset; every other path is a fork that drifts.
- **The delivery decision table:** interactive/styled -> inline; repeated mono -> sprite; large art -> optimized file with lazy loading. The decision is recorded per asset class so two teams don't ship the same glyph inline and as a sprite in the same page.

## 6. Real-World Use Cases

- **Design systems shipping icons to bundle-sensitive products.** The `<50kb-per-page` budget is a hard contract, tracked gzipped in CI.
- **Performance-focused audits of icon payload.** Finding the 400KB editor export, the duplicated glyph shipped inline and in a sprite, the metadata riding along to production.
- **Dark-mode/theming migrations converting hardcoded fills.** Moving mono glyphs to `currentColor` and multi-color art to CSS variables so theming stops requiring file duplication.

## 7. Combination Notes

### With other icons-illustration skills

- **Good with icon-library-management (guide 03):** this optimization is the library's export step - one pipeline from master to dist asset, which is precisely what makes `--icon-no-hand-edit: masters-to-pipeline` enforceable.
- **Good with icon-grid-sizing and icon-style-selection:** optimization never rescales strokes or restyles art; the grid and style specs define what the pipeline must preserve byte-semantically (stroke geometry, cap/join styles).
- **Good with accessible-icons:** the reviewed SVGO config exists to preserve title/aria nodes - accessibility preservation is an optimization requirement, not a separate concern.
- **Good with empty-error-illustrations, illustration-direction, and mascot-character:** every illustration surface ships through this pipeline; the 30KB state-art budget (guide 07) and mascot pose payloads are budgeted and gzipped here.
- **Good with icon-system-audit, icon-usability, and favicon-app-icons:** audits measure pipeline compliance; favicons are part of the bundle budget.
- **Caution with animation-integration (guide 10):** animated assets need tested config exceptions - transforms that flatten groups break CSS-driven animation hooks. The caution is by design: the pipeline must know which files are animated and relax only those transforms, or motion dies silently in the build.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** minimal and flat artwork is structurally simple - few nodes, no texture rasters - so the optimizer's wins are large and fragile features (gradients, clips) rarely appear; class-morphism's controlled depth maps cleanly to variable fills that theme well.
- **Caution notes:** none listed, but texture-heavy styles raise the stakes: richly detailed art must still pass budgets, which argues for simplification at the master level rather than optimizer heroics.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing and illustration-lottie:** eased CSS animations reference class hooks the optimizer must preserve (class names, transform origins on grouped paths), and Lottie assets are optimized at export rather than through SVGO - both strategies documented in the config's exception list.
- **Caution notes:** none listed here because the animation caution is already carried on the icons side (`animation-integration` in caution) - the config's per-file exceptions are the mechanism, and they are tested, not assumed.

## 8. Anti-Patterns

- **The 400KB icon** — unoptimized editor output shipped raw
- **ARIA-stripped by SVGO** — optimizer config deleting title/aria attributes
- **Hand-edited dist** — fixes overwritten at the next build
- **Hardcoded fills** — mono icons immune to theming and dark mode

### Accessibility Notes

Optimization must preserve the a11y nodes: the SVGO config keeps title/aria attributes (accessible-icons guide), and contrast survives fill changes - performance work must never delete the aria contract. In practice this means `removeTitle`, `removeDesc`, and ARIA-stripping transforms are disabled in the reviewed config, `currentColor` and CSS-variable fills keep glyph contrast a theming decision rather than a baked-in accident, and every pipeline change re-runs the accessibility checks alongside the size checks. The fallback rule: if the config review is pending, disable removeTitle/removeARIA transforms immediately - those two settings cause the most a11y damage.

## 9. Code Examples

### Example 1 — Before/after SVGO: same glyph, raw vs optimized

Tokens: `assets/css/svg-optimization.css`

```html
<p>check-circle.svg - raw editor output: <strong>1,284 B</strong> / after reviewed SVGO: <strong>212 B</strong> (gzip: 148 B)</p>

<!-- dist/check-circle.svg (after SVGO, reviewed config: ARIA/title preserved) -->
<svg class="glyph" viewBox="0 0 24 24" role="img" aria-labelledby="cc-t">
  <title id="cc-t">Completed</title>
  <path fill="currentColor" d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-1 14-4-4 1.4-1.4L11 13.2l5.6-5.6L18 9z"/>
</svg>

<!-- raw export (what the editor produced, for comparison - never shipped) -->
<svg class="glyph raw" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     version="1.1" id="Layer_1" x="0px" y="0px" width="48px" height="48px"
     viewBox="0 0 48 48" enable-background="new 0 0 48 48" xml:space="preserve">
  <metadata>Created with a design tool - editor layers and metadata ride along</metadata>
  <g id="Layer_2">
    <g id="check-circle">
      <path fill="#737373" stroke="#737373" stroke-width="0.5" d="M24.000,4.000 C12.954,4.000 4.000,12.954 4.000,24.000 C4.000,35.046 12.954,44.000 24.000,44.000 C35.046,44.000 44.000,35.046 44.000,24.000 C44.000,12.954 35.046,4.000 24.000,4.000 Z M22.000,34.000 L14.000,26.000 L16.800,23.200 L22.000,28.400 L32.800,17.600 L35.600,20.400 Z"/>
    </g>
  </g>
</svg>

<style>
  .glyph { width: 32px; height: 32px; color: var(--glyph-ink, #404040); }
  .glyph.raw { width: 48px; height: 48px; }
  p { font: 14px/1.5 Inter, system-ui, sans-serif; }
</style>
<script>
  // CI budget check against the token table
  const css = getComputedStyle(document.documentElement);
  const budget = css.getPropertyValue('--icon-icon-budget').trim();
  console.assert(budget.includes('50kb'), 'page icon budget token must be present');
  // Viewbox hygiene guard: optimized glyphs are tight, low-precision, no fill attributes
  const opt = document.querySelector('.glyph:not(.raw)');
  console.assert(opt.getAttribute('viewBox') === '0 0 24 24', 'tight viewBox required');
  console.assert(opt.querySelector('path').getAttribute('fill') === 'currentColor',
    'mono glyphs use currentColor per --icon-mono-fill');
</script>
```

### Example 2 — Theming demo: currentColor + CSS-variable fills across themes

```html
<div class="demo light">
  <svg class="glyph" viewBox="0 0 24 24" role="img" aria-label="Settings"><path fill="currentColor" d="M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm0 6a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/><path fill="currentColor" d="m20 13-2 .4a6 6 0 0 1 0-2.8l2 .4v-2l-1.6.3a8 8 0 0 0-1.7-2.9L18 5l-1.4-1.4-1.4 1.3A8 8 0 0 0 12 4V2h-2v2.3a8 8 0 0 0-2.4 1L6 5 4.6 6.4 6 7.7A8 8 0 0 0 4.6 11H2v2h2.6a8 8 0 0 0 1 2.3L4.6 17 6 18.4l1.3-1.3a8 8 0 0 0 2.7 1.1V22h2v-3.8a8 8 0 0 0 2.7-1.1l1.3 1.3L18 17l-1.3-1.3a8 8 0 0 0 1.7-2.9l1.6.3z"/></svg>
  <span>Mono glyph: fill is <code>currentColor</code> - theme changes text color, glyph follows.</span>
</div>

<div class="card light">
  <svg viewBox="0 0 24 24" class="art" aria-hidden="true">
    <circle class="f-a" cx="12" cy="10" r="7"/><path class="f-b" d="M6 20h12v2H6z"/>
  </svg>
  <span>Multi-color art: fills are CSS variables per <code>--icon-multicolor-fill</code>.</span>
</div>

<style>
  /* Themes re-point variables; assets never change */
  :root, .light { --glyph-ink: #404040; --il-a: #BFDBFE; --il-b: #2563EB; --surface: #FFFFFF; --text: #171717; }
  .dark         { --glyph-ink: #D4D4D4; --il-a: #1E3A8A; --il-b: #93C5FD; --surface: #171717; --text: #F5F5F5; }
  body { font: 14px/1.5 Inter, system-ui, sans-serif; margin: 0; padding: 16px; }
  .demo, .card { display: flex; gap: 10px; align-items: center; padding: 12px;
                 border-radius: 8px; margin-bottom: 8px; background: var(--surface); color: var(--text); }
  .glyph { width: 24px; height: 24px; }
  .art { width: 24px; height: 24px; }
  .art .f-a { fill: var(--il-a); }
  .art .f-b { fill: var(--il-b); }
</style>
<script>
  // Toggle to watch both theming strategies respond with zero asset changes
  document.body.onclick = () => document.body.classList.toggle('dark');
</script>
```

## 10. Implementation Checklist

- [ ] SVGO runs only with the reviewed config that preserves title/ARIA nodes (`--icon-optimizer: svgo-reviewed-config`).
- [ ] Every shipped SVG has a tight viewBox, 1-2 decimal precision, and zero editor metadata (`--icon-viewbox-hygiene: tight+low-precision`).
- [ ] Mono glyphs fill with `currentColor` (`--icon-mono-fill: currentColor`); zero hardcoded fills in single-color icons.
- [ ] Multi-color art fills route through CSS variables (`--icon-multicolor-fill: css-variables`) tied to semantic tokens.
- [ ] Each asset's delivery mode is deliberate per the decision table (`--icon-delivery-strategy: inline|sprite|file-by-use`).
- [ ] No dist file is hand-edited - all fixes flow masters -> pipeline (`--icon-no-hand-edit: masters-to-pipeline`).
- [ ] Gradient/clip-path assets have tested config exceptions (`--icon-fragile-features: gradients+clip-paths-tested`).
- [ ] Page icon budgets are tracked gzipped in CI (`--icon-icon-budget: <50kb-per-page`, `--icon-compression-check: gzip-in-budget`).
