---
name: css-grid-patterns
description: Two-dimensional layout: page shells, card grids with auto-fit, named areas, and subgrid - the patterns that replaced framework grids.
tags: [layout, grid, css, scaffolding, responsive]
related: [flexbox-patterns, layout-compositions, breakpoints-strategy]
---

# Responsive Layout Skill: CSS Grid Patterns

## 1. Definition

CSS Grid is two-dimensional layout: rows and columns designed together. Its patterns cover page scaffolding (header/main/sidebar/footer in one rule), responsive card grids (auto-fill/auto-fit with minmax), named template areas that make layout readable, and subgrid for aligning nested content. Grid made framework grid systems optional — the native primitives are more capable and token-friendly. The skill is treating `grid-template-areas` strings as first-class artifacts: readable, reorderable per breakpoint, and directly expressible as the named compositions in guide 06.

## 2. Core Principles

- **Grid for the page skeleton:** header/main/aside/footer in one `grid-template-areas` rule — readable, reorderable per breakpoint.
- **auto-fill + minmax for card grids:** `repeat(auto-fill, minmax(240px, 1fr))` responds to available space without breakpoints.
- **Named areas are documentation:** `grid-template-areas` strings read like layout diagrams — prefer them over numbered lines.
- **minmax() encodes constraints:** minimum comfortable card width + maximum stretch in one declaration.
- **Subgrid aligns nested rhythm:** card internals (title/meta rows) align across a grid row with subgrid.
- **gap consumes space tokens:** grid gap is the 4px scale — gutters stay consistent with the rest of the system.
- **Implicit grid is a smell:** auto-placed items are fine, but important placements get explicit areas — debuggable and RTL-safe.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Shell areas | `--layout-grid-shell-areas` | `'header header' 'aside main' 'footer footer'` | App shell in one template-areas rule |
| Card min | `--layout-grid-card-min` | `240px` | Card grid minmax minimum |
| Card template | `--layout-grid-card-template` | `repeat(auto-fill, minmax(240px, 1fr))` | The responsive card grid one-liner |
| Gap | `--layout-grid-gap` | `space tokens` | Row/column gap from the 4px scale |
| Sidebar template | `--layout-grid-sidebar-template` | `minmax(240px, 280px) 1fr` | Sidebar + fluid main |
| Subgrid | `--layout-grid-subgrid` | `subgrid` | Nested alignment for card internals |
| Named lines | `--layout-grid-named-lines` | `[main-start]` | Named lines for complex placements |
| Masonry fallback | `--layout-grid-masonry-fallback` | `columns-fallback` | Until masonry ships: columns() or JS masonry |
| Dense packing | `--layout-grid-dense-packing` | `grid-auto-flow: dense` | Backfill holes in mixed-size grids (bento) |
| Grid vs flex | `--layout-grid-vs-flex` | `two-dim-vs-one-dim` | The decision rule (flexbox guide) |

Consume them by linking `assets/css/css-grid-patterns.css` at the app root: the shell, card-grid, and sidebar classes reference `var(--layout-grid-card-template)`, `var(--layout-grid-sidebar-template)`, and `var(--layout-grid-gap)` so gutters and minimums change once at the token tier. Pages never write raw `repeat(auto-fill, ...)` literals or bare line numbers; they consume the preset or escalate through review.

## 4. Composition

- **Composes with grid-systems:** the 12-col system can be implemented AS a CSS grid pattern; named areas implement the compositions. The abstract system becomes concrete markup without wrapper classes.
- **Composes with flexbox-patterns:** grid areas hold flex components — the two-layer rule that keeps both readable. Grid decides where; flex decides how items sit inside each area.
- **Composes with layout-compositions:** bento, split, and sidebar layouts are named grid-template-areas strings — guide 06 turns these patterns into a consumable catalog with collapse contracts.

## 5. Signature Patterns

- **Area-string breakpoints:** layout reorganization expressed by swapping `grid-template-areas` per tier — the whole page change in 3 lines. One rule per breakpoint, no property-by-property surgery.
- **minmax card catalog:** the design system documents its minmax presets (card 240px, table 480px, widget 320px) once — every grid in the product picks a preset instead of inventing a minimum.

## 6. Real-World Use Cases

- **App shells and dashboard scaffolding:** header/aside/main/footer in one areas rule, reorganized per breakpoint by swapping the strings.
- **Responsive card/product grids without breakpoints:** `auto-fill` + `minmax` fills every viewport width naturally — no media queries per column count.
- **Bento/marketing grids with mixed-size cells:** explicit areas plus `grid-auto-flow: dense` backfills holes left by spanned cells.

## 7. Combination Notes

### With other responsive-layout skills

- **Good with flexbox-patterns and layout-compositions:** the two-layer architecture — grid draws rows/columns/areas, flex lays out component internals, compositions name the results. Each guide cross-references the same decision rule (`--layout-grid-vs-flex`), so teams escalate or descend deliberately.
- **Good with grid-systems, breakpoints-strategy, and fluid-container-queries:** the 12-col system is implemented as these grid patterns; area strings swap per breakpoint tier; container queries let grids adapt per slot rather than per viewport.
- **Good with responsive-images, mobile-navigation, and data-tables-responsive:** product grids, nav shells, and table scaffolds are all grid consumers — those guides assume this one's templates and presets exist.
- **Good with intrinsic-design, rtl-i18n-layout, and responsive-testing:** intrinsic sizing is what auto-fill/minmax encode; explicit areas (not auto-placement of interactive items) keep RTL safe; testing validates the area-string swaps and minmax presets at every tier.
- **No caution or avoid list:** grid sits at the scaffolding layer and composes with everything above it — misuse appears as the anti-patterns below, not as incompatible partners.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** clean column rhythm, generous token-driven gutters, and diagram-readable area strings are exactly how these styles want structure expressed.
- **Good affinity with maximalism:** bento grids and dense packing support busy, mixed-size compositions — but the size grammar belongs to layout-compositions so maximal density stays hierarchical, not random.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit:** grids animate well when items enter with transform/opacity per cell — staggered card entrances on `auto-fill` grids are a canonical pattern; never animate `grid-template-*` or gap values (layout thrash).
- **No caution list:** grid geometry is static by design; all motion happens at the item level, which keeps the animation repo's performance rules satisfied by default.

## 8. Anti-Patterns

- **12-wrapper-col markup** — framework-style div.col-md-6 wrappers instead of native minmax/auto-fill
- **Magic line numbers** — grid-column: 3 / 7 scattered without named lines or areas
- **Fixed-height rows** — hardcoded row heights that break with dynamic content
- **Grid-inside-grid confusion** — subgrid ignored where nested alignment was the actual goal

### Accessibility Notes

Grid reordering must keep DOM order aligned with visual reading order (WCAG 1.3.2 / 2.4.3): template-areas reorganization is visual only — the source order stays logical. When a breakpoint swaps `'aside main'` for `'main aside'`, the markup order of the regions must already match the mobile reading order, so keyboard and screen-reader traversal never diverges from the visual sequence. `grid-auto-flow: dense` is the sharper edge: backfilled cells can land in positions far from their DOM neighbors, creating confusing tab sequences — apply dense packing only to grids of non-interactive content (cards with a single trailing link), never to forms or control clusters. The fallback rule: if a grid pattern reorders interactive elements visually, restructure the DOM to match — visual-only reordering of focusable content is a blocker.

## 9. Code Examples

### Example 1 — App shell with grid-template-areas

Tokens: `assets/css/css-grid-patterns.css`

```html
<div class="shell">
  <header class="shell-header">Acme Dashboard</header>
  <aside class="shell-aside" aria-label="Primary">
    <a href="#">Overview</a><a href="#">Reports</a><a href="#">Settings</a>
  </aside>
  <main class="shell-main">
    <h1>Overview</h1><p>KPIs and activity land here.</p>
  </main>
  <footer class="shell-footer">© 2026 Acme Inc.</footer>
</div>
<style>
  .shell {
    /* --layout-grid-shell-areas = 'header header' 'aside main' 'footer footer' */
    display: grid;
    grid-template-areas: 'header header' 'aside main' 'footer footer';
    grid-template-columns: var(--layout-grid-sidebar-template, minmax(240px, 280px) 1fr);
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
    gap: var(--space-4); /* --layout-grid-gap = space tokens */
  }
  .shell-header { grid-area: header; padding: var(--space-4); border-bottom: 1px solid #ddd; font: 600 16px/1.4 system-ui, sans-serif; }
  .shell-aside  { grid-area: aside; display: flex; flex-direction: column; gap: var(--space-2); padding: var(--space-4); background: #f5f5f5; }
  .shell-main   { grid-area: main; padding: var(--space-4); }
  .shell-footer { grid-area: footer; padding: var(--space-3) var(--space-4); border-top: 1px solid #ddd; }
  @media (max-width: 1023px) {
    /* area-string breakpoint: whole-page change in 3 lines */
    .shell { grid-template-areas: 'header' 'aside' 'main' 'footer'; grid-template-columns: 1fr; }
  }
</style>
```

### Example 2 — auto-fill card grid with subgrid card internals

Tokens: `assets/css/css-grid-patterns.css`

```html
<div class="cards">
  <article class="card">
    <h2 class="card-title">Quarterly review</h2>
    <p class="card-meta">Updated 2h ago</p>
    <p class="card-body">Summary text that may run one line or four — rows still align.</p>
  </article>
  <article class="card">
    <h2 class="card-title">Migration plan</h2>
    <p class="card-meta">Updated yesterday</p>
    <p class="card-body">Short.</p>
  </article>
  <article class="card">
    <h2 class="card-title">Access audit</h2>
    <p class="card-meta">Updated 3d ago</p>
    <p class="card-body">Another varying-length summary paragraph for the row.</p>
  </article>
</div>
<style>
  .cards {
    /* --layout-grid-card-template = repeat(auto-fill, minmax(240px, 1fr)) */
    display: grid;
    grid-template-columns: var(--layout-grid-card-template);
    gap: var(--space-4);
  }
  .card {
    display: grid; grid-template-rows: auto auto 1fr;
    grid-template-rows: subgrid; /* --layout-grid-subgrid: internals align across the row */
    grid-row: span 3;
    gap: var(--space-2);
    padding: var(--space-4); border: 1px solid #ddd; border-radius: 8px;
  }
  .card-title { margin: 0; font: 600 15px/1.4 system-ui, sans-serif; }
  .card-meta  { margin: 0; color: #555; font: 12px/1.4 system-ui, sans-serif; }
  .card-body  { margin: 0; font: 14px/1.5 system-ui, sans-serif; }
</style>
```

## 10. Implementation Checklist

- [ ] Page shells and scaffolds use `grid-template-areas` from `--layout-grid-shell-areas`; no numbered-line placements for structural regions.
- [ ] Card grids use the documented minmax presets via `var(--layout-grid-card-template)` — no per-page `auto-fill` literals with invented minimums.
- [ ] All grid gaps come from space tokens (`--layout-grid-gap`); zero hardcoded px gutters.
- [ ] Breakpoint reorganization swaps area strings only; DOM source order matches mobile reading order (1.3.2 / 2.4.3).
- [ ] `grid-auto-flow: dense` is restricted to non-interactive grids; no dense-packed focusable content.
- [ ] Nested grids that need cross-row alignment use `subgrid` (`--layout-grid-subgrid`) instead of parallel row hacks.
- [ ] No fixed-height rows on dynamic content — rows size with `auto`/`minmax`/`1fr`.
- [ ] Masonry-style layouts declare the `--layout-grid-masonry-fallback` strategy before shipping.
