---
name: grid-systems
description: Column grids, gutters, and content max-widths: the alignment skeleton every layout composes on, from 12-col desktop to single-column mobile.
tags: [layout, grid, alignment, gutters, responsive]
related: [breakpoints-strategy, fluid-container-queries, css-grid-patterns]
---

# Responsive Layout Skill: Grid Systems

## 1. Definition

A grid system is the alignment contract of a layout: columns, gutters, and margins that every component snaps to. The web standard is a 12-column grid (divisible by 2, 3, 4, 6) with fluid gutters and a content max-width; mobile collapses to fewer columns or one. The grid is invisible when right — everything aligns for reasons users feel rather than see — and it is the substrate the other layout skills compose on. Treat it as infrastructure, not styling: the grid definition is singular and global, sections consume it, and no component ever redefines it per page.

## 2. Core Principles

- **12 columns on desktop, 8 on tablet, 4 on mobile:** fewer columns as space shrinks; spans stay meaningful at every tier.
- **Gutters are tokens, not guesses:** 16px mobile, 24px desktop from the spacing scale — gutters never invented per section.
- **Content max-width bounds reading:** 1200–1440px on desktop; a 66ch reading measure inside it (typography guide 08).
- **Margins grow with viewport:** edge padding scales (16/24/32/48px) so content never touches screen edges on large displays.
- **Components span columns, they do not define grids:** sections consume grid classes; the grid definition is singular and global.
- **Grid alignment beats perfect symmetry:** optical alignment (icons, text edges) may override mathematical edges — judge optically after building mathematically.
- **Breakpoint changes alter columns, not component anatomy:** a card is the same card spanning 12 or 4 columns.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Grid columns desktop | `--layout-grid-columns-desktop` | `12` | Desktop standard; divisible by 2/3/4/6 |
| Grid columns tablet | `--layout-grid-columns-tablet` | `8` | 768-1023px tier |
| Grid columns mobile | `--layout-grid-columns-mobile` | `4` | Under 768px; cards may span all 4 |
| Grid gutter mobile | `--layout-grid-gutter-mobile` | `16px` | From the 4px spacing scale |
| Grid gutter desktop | `--layout-grid-gutter-desktop` | `24px` | Desktop gutter tier |
| Grid margin mobile | `--layout-grid-margin-mobile` | `16px` | Edge padding, small screens |
| Grid margin desktop | `--layout-grid-margin-desktop` | `48px` | Edge padding grows with viewport |
| Content max width | `--layout-content-max-width` | `1440px` | App shell ceiling; reading content nested inside |
| Reading measure | `--layout-reading-measure` | `66ch` | Text content bound inside the grid |
| Grid implementation | `--layout-grid-implementation` | `css-grid-12` | Native CSS Grid; no framework grid CSS |

Consume them by linking `assets/css/grid-systems.css` once at the app root, then referencing `var(--layout-grid-gutter-desktop)`, `var(--layout-content-max-width)`, and friends from shell and component CSS — no page hardcodes a gutter, margin, or column count. If a span or margin not derivable from this table seems necessary, the grid is wrong; extend it through governance, not a per-section exception.

## 4. Composition

- **Composes with css-grid-patterns and flexbox-patterns:** the grid system is the vocabulary; those guides are its sentence patterns — the 12-col definition is implemented as native CSS Grid, and flex lays components inside grid areas.
- **Composes with spacing tokens (skill-design-tokens guide 03):** gutters and margins are spacing tokens — density modes re-map them once at the token tier instead of editing every section.
- **Composes with layout-compositions:** sidebar, split, and bento layouts are named compositions of this grid; pages consume the compositions rather than re-deriving spans.

## 5. Signature Patterns

- **Grid class vocabulary:** `.col-4` / `.col-6` / `.col-12` utilities generated from the token definition — one source, consistent spans. Generation (not hand-writing) keeps the utility layer honest when the column counts change.
- **Optical audit:** after grid math, nudge optically (icon baselines, text edges) and document overrides — math first, eyes second. Every optical nudge is recorded so the next designer knows it was a decision, not drift.

## 6. Real-World Use Cases

- **App shells:** sidebar + content grids for dashboards and admin tools, with the content region itself a 12-col grid.
- **Marketing pages:** hero, feature, and footer sections snapping to one grid so the page reads as one system, not stacked screens.
- **Audit:** elements floating off-grid, gutter drift, margin chaos — the symptoms that trigger a grid-systems intervention.

## 7. Combination Notes

### With other responsive-layout skills

- **Pairs naturally with breakpoints-strategy:** tiers change grid column counts and margins; the grid is the thing being reorganized, so a tokenized grid is what makes tier changes a three-line edit.
- **Pairs with fluid-container-queries:** grid areas create the slots that container-queried components adapt inside; the grid owns the macro, containers own the micro.
- **Pairs with css-grid-patterns, flexbox-patterns, and layout-compositions:** these are the implementation and catalog layers of the same system — the grid system defines, the patterns build, the compositions name.
- **Pairs with responsive-images, mobile-navigation, data-tables-responsive, rtl-i18n-layout, and responsive-testing:** images size to grid slots, nav collapse follows column tiers, tables and RTL inherit gutters, and the testing matrix verifies spans at every tier.
- **Caution with intrinsic-design:** intrinsic sizing (auto-fill/minmax) and a fixed 12-col system are two alignment philosophies; mixing them ad hoc produces elements that align to neither. Choose which regions are token-grid and which are intrinsic, and document the boundary.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles rely on disciplined whitespace and crisp alignment; a visible 12-col skeleton with token gutters is the quiet discipline that makes their simplicity look intentional rather than empty.
- **Caution with collage-art:** collage deliberately breaks the grid for expressive effect; if a collage style is wanted, break it consciously per region and return to the grid immediately — never let the break become the default alignment mode.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit:** staggered card/section reveals land cleanly when items share grid rhythm — the grid's even gutters give stagger animations a natural timing lattice to follow.

## 8. Anti-Patterns

- **Grid per section** — every section redefining its own grid until nothing aligns across sections
- **Pixel-position layouts** — absolute-positioned elements that shatter at any viewport change
- **Invisible gutters drift** — 15px here, 18px there — alignment erodes one component at a time
- **Framework grid lock-in** — Bootstrap columns overriding the token-defined grid

### Accessibility Notes

Grid alignment serves WCAG 1.4.4/1.4.10: layouts that snap to tokens survive zoom and reflow, because column spans and gutters recompute from tokens instead of shattering fixed pixel positions. DOM order must follow visual column order (a11y repo keyboard-navigation) — a grid is a visual arrangement, not a license to reorder the source so tab order wanders sideways. The fallback rule: when a design cannot fit the grid, extend the grid via governance — adding a documented span or tier — never float an element off-grid as a one-off, because every floating element teaches the next one to float too.

## 9. Code Examples

### Example 1 — 12-col grid shell with generated column utilities

Tokens: `assets/css/grid-systems.css`

```html
<div class="shell">
  <header class="shell-header col-12">App header</header>
  <main class="shell-main">
    <section class="col-8">Primary content</section>
    <aside class="col-4">Related items</aside>
  </main>
  <footer class="col-12">Footer</footer>
</div>
<style>
  .shell {
    max-width: var(--layout-content-max-width);
    margin-inline: auto;
    padding-inline: var(--layout-grid-margin-desktop);
    font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .shell-main {
    display: grid;
    grid-template-columns: repeat(var(--layout-grid-columns-desktop), 1fr);
    gap: var(--layout-grid-gutter-desktop);
  }
  .shell-header { margin-bottom: var(--layout-grid-gutter-desktop); }
  .col-12 { grid-column: span 12; }
  .col-8  { grid-column: span 8; }
  .col-4  { grid-column: span 4; }
  @media (max-width: 767.98px) {
    .shell { padding-inline: var(--layout-grid-margin-mobile); }
    .shell-main { grid-template-columns: repeat(var(--layout-grid-columns-mobile), 1fr); gap: var(--layout-grid-gutter-mobile); }
    .col-8, .col-4 { grid-column: span 4; }
  }
  .col-12, .shell-header, footer { background: #F5F5F5; border-radius: 8px; padding: 16px; }
  section, aside { background: #F5F5F5; border-radius: 8px; padding: 16px; }
</style>
```

### Example 2 — Reading column bounded inside the grid

Tokens: `assets/css/grid-systems.css`

```html
<article class="reading">
  <h1>Quarterly platform report</h1>
  <p>Long-form prose stays inside a bounded measure even when its grid column is wide.</p>
</article>
<script>
  const css = getComputedStyle(document.documentElement);
  const max = css.getPropertyValue('--layout-content-max-width').trim();
  const measure = css.getPropertyValue('--layout-reading-measure').trim();
  console.assert(max && measure, 'content-max-width and reading-measure tokens must exist');
</script>
<style>
  .reading {
    max-width: var(--layout-content-max-width);
    margin-inline: auto;
    padding-inline: var(--layout-grid-margin-desktop);
  }
  .reading h1, .reading p {
    /* Prose measure: capped inside the wide grid column */
    max-width: var(--layout-reading-measure);
    margin-inline: 0;
    font: 16px/1.6 Georgia, serif;
  }
  .reading h1 { font: 600 24px/1.3 Inter, system-ui, sans-serif; }
</style>
```

## 10. Implementation Checklist

- [ ] The grid definition is singular: one token-driven 12/8/4 column set in `assets/css/grid-systems.css`, no section redefines it.
- [ ] Gutters and margins use only `var(--layout-grid-gutter-*)` / `var(--layout-grid-margin-*)` — zero hardcoded px paddings in sections.
- [ ] Column utility classes (`.col-*`) are generated from `--layout-grid-columns-*`, not hand-maintained.
- [ ] Page shells cap at `var(--layout-content-max-width)`; prose inside uses `var(--layout-reading-measure)`.
- [ ] Edge padding scales with viewport (16px mobile → 48px desktop) via the margin tokens.
- [ ] No framework grid CSS (Bootstrap/`col-md-*`) coexists with the token grid.
- [ ] DOM order matches visual column order; every optical-alignment override is documented.
- [ ] Layouts are reviewed at 375px, 768px, 1024px, and 1440px against the token grid.
