---
name: data-tables-responsive
description: Tables that survive narrow screens — priority columns, card fallback, sticky headers, and horizontal scroll done honestly.
tags: [tables, responsive, data-dense, sticky-header, touch]
related: [grid-systems, breakpoints-strategy, responsive-testing]
---

# Responsive Layout Skill: Responsive Data Tables

## 1. Definition

Data tables are the hardest responsive problem: they are dense, two-dimensional, and comparison-oriented — exactly what small screens hate. The strategy ladder: (1) reduce columns by priority, (2) allow honest horizontal scroll with sticky first column, (3) restructure to stacked cards per row as last resort (losing comparability). The choice is per-table by data type — and horizontal scroll with sticky headers beats pseudo-card tables for comparison tasks. Tables fail on mobile not because they are too wide but because teams adapt them blindly: cropping columns silently, stacking rows into cards that destroy comparison, or squeezing cells until numbers wrap into slivers. This skill makes the adaptation a deliberate, per-table decision with a documented priority matrix behind it.

## 2. Core Principles

- **Cut before you adapt:** mobile tables show priority columns (2–4); the rest live in a detail view — column priority is an IA decision, made before any CSS is written.
- **Horizontal scroll is honest:** a scrollable table with sticky header + sticky identifier column preserves comparability; hide-scroll-by-crop is a lie that hides data without telling the user.
- **Card-stack is the last resort:** stacked rows lose column comparison — use only when rows are self-contained records (orders, messages), not comparison grids.
- **Sticky first column = row identity:** the identifier column pins so users never lose which row they are reading while scrolling horizontally.
- **Row height and touch targets:** 48px rows; row actions as a menu, not a hover-only toolbar (hover does not exist on touch).
- **Numeric columns stay tabular:** `tnum` figures + right alignment (typography guide 10) — alignment survives adaptation, and digit columns stay comparable.
- **Scroll indicators are visible:** a faded edge or shadow marks truncation; users must know more exists (3.2.x predictability) — silent truncation is a data-integrity bug.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Priority columns | `--layout-table-priority-cols` | `2-4-on-mobile` | IA decision: which columns survive mobile |
| Scroll mode | `--layout-table-scroll-mode` | `horizontal+sticky-id` | Default adaptation: honest scroll, pinned identity |
| Sticky header | `--layout-table-sticky-header` | `position-sticky-top` | Column headers persist on vertical scroll |
| Row height | `--layout-table-row-height` | `48px` | Touch-comfortable rows; 40px compact tier |
| Card fallback | `--layout-table-card-fallback` | `self-contained-rows-only` | Card stacking only for record-like rows |
| Row actions | `--layout-table-actions` | `menu-not-hover` | Row actions in a kebab menu on touch |
| Numeric align | `--layout-table-numeric-align` | `right+tabular` | Numbers right-aligned, tabular figures |
| Scroll indicator | `--layout-table-scroll-indicator` | `edge-fade` | Visible truncation cue |
| Empty width | `--layout-table-empty-width` | `min-100%` | Tables never compress below readable column width |
| Sort targets | `--layout-table-sort-targets` | `44px-header-buttons` | Sort headers meet the touch floor |

Consume them by linking `assets/css/data-tables-responsive.css` at the app root, then referencing `var(--layout-table-...)` in the table component — scroll mode, row height, and the edge-fade cue are shared contracts across every table in the product. Per-table variation lives in the priority matrix (which columns are mobile/core/extended), never in improvised CSS widths.

## 4. Composition

- **Composes with grid-systems:** tables span the full content column; their scroll container respects the shell's margins, so the scroll region never fights the grid for width.
- **Composes with skill-component-recipes guide 03 (tables):** the recipe owns features (sort/filter/pagination); this guide owns responsive behavior — feature code and adaptation code stay separable.
- **Composes with numeric-tabular (skill-typography guide 10):** alignment and figure style are shared contracts — right-aligned tabular numerals are agreed once and consumed by every table.

## 5. Signature Patterns

- **Priority-column matrix:** per table, document columns × importance (mobile/core/extended); the mobile set falls out of the matrix — column cuts are auditable decisions, not ad-hoc hiding.
- **Sticky-scroll pattern:** scroll container + `position: sticky` th + sticky first column + edge fade — the reusable honest-scroll implementation every comparison table consumes.

## 6. Real-World Use Cases

- **Admin/enterprise tools where tables are the primary surface:** user lists, inventories, logs — dense grids that must stay usable at 360px.
- **Finance and analytics products with comparison-critical tables:** columns are the point; the adaptation must preserve row-by-row comparison.
- **Audit:** hover-only actions, cropped scroll, card-tables that lost comparability — the three findings that define a failing responsive table.

## 7. Combination Notes

### With other responsive-layout skills

- **Good with grid-systems, breakpoints-strategy, fluid-container-queries, flexbox-patterns, css-grid-patterns, layout-compositions, responsive-images, intrinsic-design, rtl-i18n-layout, responsive-testing, mobile-navigation:** tables live inside the shell (grid gives them the full content column), adapt at the documented tiers (breakpoints decide when the priority set applies), flex inside their cells, mirror under RTL (logical properties in the scroll container), and are verified by the responsive-testing matrix at every width. Container queries let a table adapt to its slot (main column vs. side panel) rather than the viewport.
- **Caution with mobile-navigation:** both compete for the same small-screen vertical space — a bottom bar plus sticky table header plus scroll container can consume the entire viewport. Coordinate the height budget: on table-heavy screens the bar may hide on scroll, and only one sticky layer may own the top. The conflict is about space, not technique — resolved by planning, not by abandoning either pattern.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** minimalism cuts columns ruthlessly (which is the priority-matrix discipline anyway); flat-design keeps cell chrome light so density stays readable; class-morphism's structured surfaces suit zebra rows and sticky column treatments without ornament fighting the grid.
- **Caution with collage-art:** collage treatments (rotated tiles, overlapping fragments, irregular frames) break the one thing a table needs — aligned rows and columns. If a collage direction applies to the page, confine it to the page chrome; the table surface itself stays disciplined or the data becomes unreadable.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** sort re-orderings, row expansion, and drawer-style detail views animate with duration/easing tokens, making state changes legible rather than jarring; horizontal scroll physics are native and never overridden.
- **Caution with data-animation:** chart-style animation inside table cells (animated numbers, growing bars) can fight the tabular-figure contract and repaint costs on dense grids — if used, keep it out of the sticky column and bound it by reduced-motion rules, so comparison reading is never animated underneath the user's eyes.

## 8. Anti-Patterns

- **Crop-scroll lie** — tables that silently clip columns with no scroll affordance
- **Card-table everything** — comparison data stacked into cards, destroying the only reason it was a table
- **Hover-only row actions** — toolbars invisible to touch and keyboard users
- **Squeezed columns** — letting tables compress until cells wrap into unreadable slivers

### Accessibility Notes

Tables need real `<table>` semantics (`th` scope, caption) regardless of visual adaptation (a11y repo aria-fundamentals) — card and stacked presentations still expose row/column relationships to assistive tech, which is why the underlying markup never becomes divs. Scroll containers must stay keyboard-scrollable and actions keyboard-reachable (2.1.1): a kebab menu is focusable, opens with Enter, and its items are tab-navigable. The fallback rule: if the card fallback is used, keep a "switch to table view" control — comparability is user-selectable, not design-fated.

## 9. Code Examples

### Example 1 — Honest-scroll table: sticky header + sticky ID column + edge fade

Tokens: `assets/css/data-tables-responsive.css`

```html
<div class="table-wrap" tabindex="0" role="region" aria-label="Invoices, scrollable">
  <table><caption>Open invoices — Q3</caption>
    <thead><tr>
        <th scope="col" class="id-col">Invoice</th>
        <th scope="col" class="num">Amount</th>
        <th scope="col">Status</th>
        <th scope="col">Issued</th>
        <th scope="col" class="actions"><span class="visually-hidden">Actions</span></th>
      </tr></thead><tbody><tr>
        <th scope="row" class="id-col">INV-2041</th>
        <td class="num">$12,400.00</td> <td>Paid</td> <td>Sep 14</td>
        <td class="actions"><button class="kebab" aria-haspopup="menu" aria-expanded="false" aria-label="Actions for INV-2041">⋮</button></td>
      </tr>
      <tr>
        <th scope="row" class="id-col">INV-2042</th>
        <td class="num">$860.50</td> <td>Overdue</td> <td>Sep 21</td>
        <td class="actions"><button class="kebab" aria-haspopup="menu" aria-expanded="false" aria-label="Actions for INV-2042">⋮</button></td>
      </tr></tbody>
  </table>
</div>
<style>
  .table-wrap {
    overflow: auto; max-height: 320px; position: relative;
    /* var(--layout-table-scroll-indicator) = edge-fade — visible truncation cue */
    background:
      linear-gradient(to right, #fff 30%, rgba(255,255,255,0)) left/32px 100% no-repeat local,
      linear-gradient(to left, #fff 30%, rgba(255,255,255,0)) right/32px 100% no-repeat local,
      linear-gradient(to left, rgba(0,0,0,0.15), transparent 32px) right/32px 100% no-repeat scroll,
      linear-gradient(to right, rgba(0,0,0,0.15), transparent 32px) left/32px 100% no-repeat scroll;
    font: 14px/1.4 system-ui, sans-serif;
  }
  table { border-collapse: separate; border-spacing: 0; min-width: 100%; } /* var(--layout-table-empty-width) */
  th, td { padding: 12px 16px; min-width: 110px; text-align: start; border-bottom: 1px solid #e5e5e5; }
  thead th { position: sticky; top: 0; background: #fafafa; z-index: 2; min-height: 44px; /* sticky-header + sort-targets */ }
  /* var(--layout-table-scroll-mode) = horizontal+sticky-id — row identity pins */
  .id-col { position: sticky; inset-inline-start: 0; background: #fff; z-index: 1; } thead .id-col { z-index: 3; }
  .num { text-align: end; font-variant-numeric: tabular-nums; } /* var(--layout-table-numeric-align) */ tr { height: 48px; } /* var(--layout-table-row-height) */
  .kebab { min-width: 44px; min-height: 44px; border: none; background: none; cursor: pointer; }
  .visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
</style>
```

### Example 2 — Priority-column matrix + kebab row actions (menu, not hover)

```html
<table class="prio">
  <caption>Users — mobile priority set: Name, Role, Actions</caption>
  <thead><tr>
      <th scope="col" data-priority="mobile">Name</th>
      <th scope="col" data-priority="mobile">Role</th>
      <th scope="col" data-priority="core">Email</th>
      <th scope="col" data-priority="extended">Last login</th>
      <th scope="col"><span class="sr">Actions</span></th>
    </tr></thead>
  <tbody><tr>
      <td>Amara Okafor</td><td>Admin</td>
      <td data-priority="core">amara@corp.io</td>
      <td data-priority="extended">Today 09:12</td>
      <td><button class="kebab" aria-haspopup="menu" aria-expanded="false" aria-label="Actions for Amara Okafor">⋮</button>
        <ul role="menu" hidden>
          <li><button role="menuitem">View details</button></li>
          <li><button role="menuitem">Reset password</button></li>
        </ul>
      </td>
    </tr></tbody></table>
<style>
  /* Priority-column matrix: mobile set from data-priority, per var(--layout-table-priority-cols) */
  @media (max-width: 767.98px) { [data-priority="core"], [data-priority="extended"] { display: none; } }
  .prio { width: 100%; border-collapse: collapse; font: 14px/1.4 system-ui, sans-serif; }
  .prio th, .prio td { padding: 12px; text-align: start; border-bottom: 1px solid #e5e5e5; min-height: 44px; }
  .kebab { min-width: 44px; min-height: 44px; border: none; background: none; cursor: pointer; }
  .prio [role="menu"] { margin: 0; padding: 4px; list-style: none; background: #fff; border: 1px solid #e5e5e5;
                        border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,.1); }
  .prio [role="menuitem"] { min-width: 44px; width: 100%; padding: 10px; border: none; background: none; text-align: start; cursor: pointer; }
  .sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
</style>
<script>
  // var(--layout-table-actions) = menu-not-hover — kebab opens a focusable menu
  document.querySelectorAll('.kebab').forEach((btn) => { const menu = btn.nextElementSibling;
    btn.addEventListener('click', () => {
      menu.hidden = !menu.hidden;
      btn.setAttribute('aria-expanded', String(!menu.hidden));
      if (!menu.hidden) menu.querySelector('[role="menuitem"]')?.focus();
    });
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every table has a priority-column matrix (mobile/core/extended) and renders 2–4 columns on mobile (var(--layout-table-priority-cols)).
- [ ] The default adaptation is honest scroll: sticky header (var(--layout-table-sticky-header)) + sticky identifier column (var(--layout-table-scroll-mode)).
- [ ] A visible truncation cue (edge fade or shadow, var(--layout-table-scroll-indicator)) marks horizontal overflow — no silent crops.
- [ ] Rows are 48px (var(--layout-table-row-height)) and sort header buttons meet 44px (var(--layout-table-sort-targets)).
- [ ] Row actions live in a kebab menu (var(--layout-table-actions)) — hover-only toolbars do not exist; actions are keyboard-reachable.
- [ ] Numeric columns are right-aligned with tabular figures (var(--layout-table-numeric-align)).
- [ ] Tables never compress below readable width (var(--layout-table-empty-width)); the card fallback (var(--layout-table-card-fallback)) is used only for self-contained rows, with a switch-to-table control.
- [ ] Markup keeps real `<table>` semantics: caption, `th scope`, and a keyboard-scrollable region with an accessible name.
