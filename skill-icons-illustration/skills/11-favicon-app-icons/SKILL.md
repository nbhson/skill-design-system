---
name: favicon-app-icons
description: The smallest brand surfaces: favicon sets, PWA icons, maskable variants, touch icons, and generation over hand-export.
tags: [favicon, pwa, app-icons, maskable, branding]
related: [icon-style-selection, icon-grid-sizing, icon-library-management]
---

# Visual Asset Guide: Favicons & App Icons

## 1. Definition

Favicons and app icons are the brand's smallest surfaces and its most fragmented: ico/png/svg stacks, apple-touch-icons, maskable PWA icons with safe zones, and theme-color tiles. This guide covers the modern minimal set (SVG favicon + 512/192 PWA + maskable + apple-touch 180), maskable-icon safe zones, generation pipelines (one master, all sizes generated), and the brand-consistency checks - the icon recognizable at 16px and in an OS dock alike. These assets ship once per product and are then seen millions of times in tab strips, bookmark bars, and home screens, so the cost of getting the set wrong is paid in every session; the discipline is small (one master, one pipeline, one test at 16px) and the payoff is brand presence in the most-repeated chrome on the web.

## 2. Core Principles

- **The modern minimal set:** SVG favicon (with ico fallback), 180px apple-touch, 512 + 192 PWA (regular + maskable) - more sizes are legacy, fewer is incomplete.
- **One master, generated sizes:** a 1024px master exports every size via pipeline - hand-exported per-size files drift.
- **Maskable icons respect the safe zone:** critical content within the inner 80% circle - the OS crops unpredictably.
- **Recognizable at 16px:** the favicon is re-drawn/simplified for small sizes if the master detail fails - test in an actual tab strip.
- **Consistency with the icon family:** the favicon uses the brand mark and product palette - not a different logo treatment.
- **Dark mode favicon where supported:** prefers-color-scheme-aware SVG favicon - a black glyph on dark tab strips vanishes.
- **theme-color matches the surface:** the meta theme-color (and light/dark variants) aligns with the browser chrome.
- **PWA completeness checked:** manifest icons + maskable + shortcuts verified in Lighthouse - broken PWA icons are silent failures.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Minimal set | `--icon-minimal-set` | `svg+ico,180-touch,512+192,maskable` | Modern favicon/app icon stack |
| Master source | `--icon-master-source` | `1024px-master` | All sizes generated from one file |
| Safe zone | `--icon-maskable-safe-zone` | `inner-80%-circle` | OS crop unpredictability |
| Small size test | `--icon-small-size-test` | `16px-tab-strip` | Recognized in a real tab bar |
| Brand consistency | `--icon-brand-consistency` | `mark+product-palette` | Same family as product icons |
| Dark favicon | `--icon-dark-favicon` | `prefers-color-scheme-svg` | Visible on dark tab strips |
| Theme color | `--icon-theme-color` | `light+dark-variants` | Browser chrome alignment |
| Manifest check | `--icon-manifest-check` | `lighthouse-pwa` | Icons verified in CI/Lighthouse |
| Generation pipeline | `--icon-generation-pipeline` | `automated-exports` | No hand-exported per-size drift |
| Fallback ico | `--icon-fallback-ico` | `bundled-for-legacy` | Old browsers still branded |

Consume them by linking `assets/css/favicon-app-icons.css` at the app root - the stylesheet carries the token definitions that CI tooling and preview components read via `var(--icon-...)`, so the manifest validator, the safe-zone overlay, and the tab-strip test all enforce the same declared set instead of private copies of the size list.

## 4. Composition

- **Composes with icon-style-selection + icon-grid-sizing:** the brand mark follows the same family rules at tiny sizes.
- **Composes with icon-library-management:** favicon assets are generated and versioned in the same pipeline.
- **Composes with svg-optimization:** the favicon set is part of the bundle budget.

## 5. Signature Patterns

- **The favicon generation pipeline:** one 1024px master -> automated export (svg, ico, apple-touch, PWA, maskable) -> manifest validated in CI - sizes never hand-made. The master is the only file an artist touches; everything in `<head>` is build output.
- **The maskable safe-zone template:** master art composed on an 80% safe-zone overlay so one design serves both regular and maskable without two sources. Art keeps critical content inside the inner circle; background fills bleed to the full square so any crop shape stays branded.

## 6. Real-World Use Cases

- **Every product launch** (the set ships once, correctly).
- **PWAs and installable apps** where icon quality drives trust.
- **Audit: single-favicon sites, maskable crops cutting the logo, dark-strip invisibility.**

## 7. Combination Notes

### With other icons-illustration skills

- **Good with icon-style-selection, icon-grid-sizing, and icon-library-management:** the brand mark is drawn under the same style spec and grid as the product's icons, and the favicon set lives in the same generated, versioned library as every other asset - no parallel brand-mark process.
- **Good with svg-optimization and icon-system-audit:** the set participates in the bundle budget, and the audit counts the minimal-set tokens as checklist items (manifest present, maskable present, dark variant present).
- **Good with illustration-direction and mascot-character:** when the mark is illustrative or character-based, the tiny-size redraw is part of that spec's detail budget - the character's 16px silhouette is designed, not compressed.
- **No caution or avoid entries:** every surface skill here either builds the master, pipelines it, or audits it - favicons have no incompatible partner, only incomplete sets.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** simple geometry with flat fills is exactly what survives a 16px tab strip and an unpredictable maskable crop - bold shapes and limited palettes compress gracefully.
- **Caution with detail-heavy styles generally:** gradients, thin line work, and intricate patterns from styles like maximalism or collage-art rarely survive 16px; where a style demands them, the small-size redraw simplifies deliberately while the master keeps the full styling at 512px.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** the only motion on these surfaces is in install/update transitions and splash screens; when a PWA animates its icon in, it follows easing tokens so the brief movement matches the product's motion system.
- **Caution with everything else - favicons and app icons must be static:** browsers and OSes do not support animated favicons consistently, and spinning tab glyphs read as broken pages; motion stays in the product, not the mark.

## 8. Anti-Patterns

- **The single-favicon site** — one 32px ico serving every context badly
- **Maskable crop casualties** — logos decapitated by OS rounding
- **Dark-strip invisibility** — dark glyphs on dark browser chrome
- **Hand-exported drift** — five sizes exported at five times, subtly different

### Accessibility Notes

Favicons are brand graphics with contrast obligations at 16px (WCAG 1.4.11 spirit): sufficient contrast against both light and dark tab strips, and text-free marks (text at 16px is unreadable) - the mark must survive the smallest context. That means the SVG favicon is authored scheme-aware (a light variant for dark strips, dark variant for light strips) or uses a mid-tone mark on a contrasting backing shape, never a bare dark glyph that vanishes on dark browser chrome. The fallback rule: if dark-mode favicon support is unavailable, pick a mid-tone mark with a contrasting backing shape that survives both strip colors - visibility in both strips outranks exact brand-color fidelity at this size.

## 9. Code Examples

### Example 1 — Favicon set demo: head links, manifest, theme-color, dark-mode favicon

Tokens: `assets/css/favicon-app-icons.css`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Favicon set — demo page</title>
  <!-- --icon-minimal-set: svg+ico,180-touch,512+192,maskable -->
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="alternate icon" href="/favicon.ico" sizes="32x32"> <!-- --icon-fallback-ico: bundled-for-legacy -->
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
  <link rel="manifest" href="/manifest.webmanifest">
  <!-- --icon-theme-color: light+dark-variants — browser chrome alignment -->
  <meta name="theme-color" media="(prefers-color-scheme: light)" content="#FFFFFF">
  <meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0B1220">
  <style>
    body { font: 14px/1.5 Inter, system-ui, sans-serif; margin: 24px; color: #1e293b; }
    .preview { display: flex; gap: 16px; align-items: center; }
  </style>
</head>
<body>
  <h1>Favicon set</h1>
  <p>Check the tab strip: the SVG below swaps with <code>prefers-color-scheme</code>.</p>
  <div class="preview">
    <svg viewBox="0 0 32 32" width="32" height="32" aria-label="Brand mark favicon preview" role="img">
      <!-- --icon-brand-consistency: mark+product-palette; --icon-dark-favicon: prefers-color-scheme-svg -->
      <style>
        .backing { fill: #6366F1; }
        .glyph { fill: #FFFFFF; }
        @media (prefers-color-scheme: dark) { .backing { fill: #A5B4FC; } .glyph { fill: #0B1220; } }
      </style>
      <rect class="backing" x="1" y="1" width="30" height="30" rx="7"/>
      <path class="glyph" d="M9 17l5 5 9-11" stroke="#fff" stroke-width="0" />
      <path class="glyph" d="M9.5 17l4.5 4.5 8.5-10" fill="none" stroke-width="3" stroke="currentColor" style="color:inherit"/>
    </svg>
    <span>32px tab preview</span>
  </div>
  <!-- /manifest.webmanifest: {"icons":[{"src":"/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/icon-512.png","sizes":"512x512","type":"image/png"},{"src":"/icon-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]} -->
  <!-- --icon-manifest-check: lighthouse-pwa — verify in CI -->
</body>
</html>
```

### Example 2 — 16px tab-strip readability test panel with maskable safe-zone overlay

Tokens: `assets/css/favicon-app-icons.css`

```html
<div class="tab-test">
  <h2>Tab-strip readability test</h2>
  <p class="hint">--icon-small-size-test: 16px-tab-strip — mark must read at 16px, both strip colors.</p>
  <div class="strip light">
    <span class="tab"><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" focusable="false">
      <rect x="0" y="0" width="16" height="16" rx="4" fill="#6366F1"/><path d="M4 8.5l2.8 2.8L12 5.5" fill="none" stroke="#fff" stroke-width="2"/>
    </svg> Deploy report</span>
  </div>
  <div class="strip dark">
    <span class="tab"><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" focusable="false">
      <rect x="0" y="0" width="16" height="16" rx="4" fill="#A5B4FC"/><path d="M4 8.5l2.8 2.8L12 5.5" fill="none" stroke="#0B1220" stroke-width="2"/>
    </svg> Deploy report</span>
  </div>
  <h2>Maskable safe zone</h2>
  <p class="hint">--icon-maskable-safe-zone: inner-80%-circle — critical art stays inside the circle.</p>
  <svg viewBox="0 0 64 64" width="96" height="96" role="img" aria-label="Maskable safe-zone overlay on the brand mark">
    <rect x="0" y="0" width="64" height="64" fill="#6366F1"/>
    <path d="M18 33l8 8 20-24" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
    <!-- Safe-zone overlay: inner 80% circle + crop guides -->
    <circle cx="32" cy="32" r="25.6" fill="none" stroke="#F59E0B" stroke-dasharray="4 3" stroke-width="1.5"/>
    <rect x="0" y="0" width="64" height="64" fill="none" stroke="#EF4444" stroke-width="1.5"/>
  </svg>
</div>
<style>
  .tab-test { font: 14px/1.5 Inter, system-ui, sans-serif; color: #1e293b; max-width: 420px; }
  .strip { display: flex; padding: 6px 10px; margin: 8px 0; border-radius: 6px; }
  .strip.light { background: #F1F5F9; }
  .strip.dark  { background: #0B1220; }
  .tab { display: inline-flex; align-items: center; gap: 6px; font-size: 12px; }
  .strip.light .tab { color: #0B1220; } .strip.dark .tab { color: #E2E8F0; }
  .hint { color: #475569; margin: 4px 0; }
</style>
```

## 10. Implementation Checklist

- [ ] The full `var(--icon-minimal-set)` is present: SVG favicon + ico fallback, 180px apple-touch, 512 + 192 PWA (regular + maskable).
- [ ] All sizes are generated from the `var(--icon-master-source)` 1024px master by `var(--icon-generation-pipeline)` - zero hand-exported files in the repo.
- [ ] Maskable variant keeps critical content inside the `var(--icon-maskable-safe-zone)` inner-80% circle, verified with the overlay.
- [ ] The mark passes the `var(--icon-small-size-test)`: recognizable in a real 16px tab strip on light and dark strips.
- [ ] The favicon honors `var(--icon-dark-favicon)` (prefers-color-scheme SVG) and `var(--icon-theme-color)` ships light + dark variants.
- [ ] `var(--icon-manifest-check)` runs in CI: manifest icons + maskable + shortcuts pass Lighthouse PWA.
- [ ] The mark uses `var(--icon-brand-consistency)` (brand mark + product palette), matching the product icon family.
- [ ] `var(--icon-fallback-ico)` is bundled so legacy browsers still show a branded tab.
