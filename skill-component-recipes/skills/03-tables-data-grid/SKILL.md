---
name: tables-data-grid
description: Sortable, filterable, paginated tables: column semantics, sticky headers, selection models, and the grid-vs-table decision.
tags: [tables, data-grid, sorting, pagination, accessibility]
related: [buttons-badges, forms-inputs, dropdowns-menus]
---

# Component Recipe: Tables & Data Grids

## 1. Definition

Data tables are where information density and interaction meet: sorting, filtering, pagination, row selection, and inline editing. The recipe distinguishes a table (read data; native `<table>` semantics) from a grid (interactive cells; ARIA grid pattern) — and covers column types (numeric right-aligned tabular, actions as menus), sticky headers, and empty/loading states as first-class table states. Admin consoles, finance dashboards, and operations tools live and die by their tables, and most table failures are semantic ones: div-based layouts that screen readers cannot navigate, sorting that narrates nothing, and pagination that loses the user's place. This recipe makes the semantics, the column contracts, and the state coverage (empty/loading) non-negotiable.

## 2. Core Principles

- **Table vs grid is a semantics decision:** read-only data stays a native `<table>`; per-cell interactive editing becomes an ARIA grid — never a div-soup of either.
- **Real `<table>` semantics:** th scope, caption, thead/tbody — screen reader navigation (a11y repo aria-fundamentals) depends on it.
- **Column types have contracts:** numeric right-aligned + tabular figures (typography guide 10), text left-aligned, actions as kebab menus, timestamps relative-with-absolute-title.
- **Sorting announces:** aria-sort on column headers; sort buttons meet the 44px target floor.
- **Selection models are explicit:** none, single, multi — with select-all that respects filter scope and announces selection count.
- **Sticky headers for long tables:** position-sticky th persists context on scroll (responsive-layout guide 09 owns mobile adaptation).
- **Empty and loading are table states:** zero-results with a recovery suggestion; skeleton rows that preserve column alignment.
- **Pagination is honest:** counts ('1-25 of 1,204'), page size controls, and URL-persisted state — fake-infinite tables lose users' place.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Semantics | `--comp-table-semantics` | `native-table-or-aria-grid` | The documented decision rule |
| Row height | `--comp-table-row-height` | `48px` | Default; 40px compact tier |
| Header sticky | `--comp-table-header-sticky` | `position-sticky` | Column headers persist on vertical scroll |
| Numeric align | `--comp-table-numeric-align` | `right+tabular-nums` | Numeric columns contract |
| Row actions | `--comp-table-actions` | `kebab-menu-44px` | Row actions; touch floor met |
| Sort announce | `--comp-table-sort-announce` | `aria-sort-on-headers` | Sorting narrated |
| Selection model | `--comp-table-selection-model` | `none|single|multi` | Explicit per table; count announced |
| Empty state | `--comp-table-empty-state` | `message+suggestion` | Zero-results is designed, not blank |
| Loading state | `--comp-table-loading-state` | `skeleton-rows` | Column-aligned skeletons |
| Pagination | `--comp-table-pagination` | `counts+url-state` | 1-25 of N; state in URL |

Consume them by linking `assets/css/tables-data-grid.css` once and reading `var(--comp-table-...)` from the table kit. As with the other recipes, half the tokens are behavioral contracts (`semantics`, `sort-announce`, `selection-model`, `pagination`) that reviews assert against, and the visual ones (`row-height`, `numeric-align`) keep every table in the product on one density and alignment rhythm.

## 4. Composition

- **Composes with responsive-layout guide 09:** that guide owns narrow-screen adaptation; this recipe owns features and semantics.
- **Composes with data-viz-palettes (skill-color-theory guide 08):** status coloring inside tables follows the CVD-safe viz rules.
- **Composes with numeric-tabular (skill-typography guide 10):** tabular figures + alignment are shared contracts.

## 5. Signature Patterns

- **Table kit:** one Table component family (Table, Column, RowActions, Pagination) with the semantic/sticky/sort contracts implemented once. Products declare columns and data; the kit renders the correct `<table>` structure, sticky header, aria-sort updates, and pagination — no team re-implements the grid pattern per screen.
- **Column contract declarations:** columns declare type (numeric/text/action/date) and the kit applies alignment, figures, and menu treatment automatically. A `type="numeric"` column gets right alignment and tabular figures; `type="action"` becomes a kebab menu with a 44px target — column mistakes become impossible at the API level.

## 6. Real-World Use Cases

- **Admin and enterprise surfaces** where tables are the primary object.
- **Finance/analytics products** with comparison-critical data.
- **Audit:** div-tables, hover-only actions, fake pagination, unwired sorting.

## 7. Combination Notes

### With other component-recipe skills

- **Good with buttons-badges and forms-inputs:** toolbar and row-action buttons consume the sm-tier ramp and count badges express selection totals; filter rows and inline editors reuse field heights and validation timing.
- **Good with dropdowns-menus, modals-dialogs, and toasts-notifications:** row actions are kebab menus under the menu keyboard contract; destructive rows confirm in dialogs; bulk operations report via toasts.
- **Good with empty-loading-error, tabs-accordions, cards-lists, command-palette, navigation-patterns:** tables embed in all these containers and inherit their state and container contracts.
- **Good with accessibility-wiring:** it audits the aria-sort/selection/summary layer this recipe builds.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** dense data reads best with hairline borders, flat row surfaces, and disciplined alignment; class-morphism's subtle layering works for header/toolbar chrome without disturbing cell semantics.
- **Caution with collage-art and maximalism:** decorative backgrounds, rotated fragments, and ornament-heavy chrome fight information density and tabular readability — if a style demands it, confine expression to the toolbar and empty states, never the cell grid.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** sort re-orders, pagination swaps, and skeleton fade-ins should animate on short, tokenized durations so row positions stay trackable.
- **Caution with data-animation:** animated chart-like cell effects (animated counts, moving sparkline fills) can hurt scanning and comparison in dense tables — any cell-level animation must respect reduced-motion and never delay data legibility.

## 8. Anti-Patterns

- **Div-table soup:** CSS-grid divs where screen readers need th/td semantics
- **Hover-only actions:** row toolbars invisible to touch and keyboard
- **Sort-by-invisibility:** sorted columns with no aria-sort or visual direction cue
- **Pagination theater:** 'infinite' tables that reset scroll and lose user place

### Accessibility Notes

Tables implement WCAG 1.3.1 (structure), 2.1.1 (keyboard-sort/actions), and the ARIA grid pattern when interactive: scope/caption semantics, aria-sort, and keyboard-reachable row actions are the recipe's non-negotiables. In practice this means a caption names the table, `th scope` maps every header to its cells so screen reader users hear "Revenue, Q3, $4.2M" as a coordinate, sort headers are real buttons toggling `aria-sort` values, and the selection model announces its count in a live region. Row actions inside kebab menus must open and operate from the keyboard alone, and sticky headers must not trap or hide focus. If the full grid pattern is too heavy for a surface, ship the native table with keyboard-reachable actions (menus open via keyboard) — a semantic table with menus beats a partial grid.

## 9. Code Examples

### Example 1 — Sortable sticky-header table with row kebab actions

Tokens: `assets/css/tables-data-grid.css`

```html
<table class="dt">
  <caption>Invoices — 2 of 2 shown</caption>
  <thead>
    <tr>
      <th scope="col" aria-sort="ascending"><button class="sort" data-key="id">Invoice</button></th>
      <th scope="col">Customer</th> <th scope="col" class="num" aria-sort="none"><button class="sort" data-key="amount">Amount</button></th>
      <th scope="col"><span class="sr-only">Actions</span></th>
    </tr>  </thead>
  <tbody>
    <tr><td>INV-1042</td><td>Acme Corp</td><td class="num">1,204.00</td><td><button class="kebab" aria-haspopup="menu" aria-label="Actions for INV-1042">⋮</button></td></tr>
    <tr><td>INV-1043</td><td>Globex</td><td class="num">940.50</td><td><button class="kebab" aria-haspopup="menu" aria-label="Actions for INV-1043">⋮</button></td></tr>
  </tbody>
</table>
<script>
  const table = document.querySelector('.dt');
  table.querySelectorAll('.sort').forEach(btn => btn.addEventListener('click', () => {
    const th = btn.closest('th');
    const next = th.getAttribute('aria-sort') === 'ascending' ? 'descending' : 'ascending';
    table.querySelectorAll('th').forEach(h => h.setAttribute('aria-sort', 'none'));
    th.setAttribute('aria-sort', next); // sorting announces
    const i = [...th.parentElement.children].indexOf(th); const rows = [...table.tBodies[0].rows];
    rows.sort((a, b) => a.cells[i].textContent.localeCompare(b.cells[i].textContent, undefined, { numeric: true }));
    if (next === 'descending') rows.reverse();
    rows.forEach(r => table.tBodies[0].append(r));
</script>
<style>
  .dt { border-collapse: collapse; font: 14px/1.4 Inter, system-ui, sans-serif; max-width: 560px; } caption { text-align: left; font-weight: 600; padding: 8px 0; }
  thead th { position: sticky; top: 0; background: #fff; border-bottom: 1px solid #D4D4D4; }
  th, td { padding: 0 12px; height: var(--comp-table-row-height); text-align: left; border-bottom: 1px solid #F5F5F5; }
  .num { text-align: right; font-variant-numeric: tabular-nums; } /* numeric contract */
  .sort, .kebab { background: none; border: none; cursor: pointer; font: inherit; font-weight: 600; min-width: 44px; min-height: 44px; } /* 44px touch floor */
  .sort:focus-visible, .kebab:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; } .sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
</style>
```

### Example 2 — Pagination, selection, empty and loading skeleton states

Tokens: `assets/css/tables-data-grid.css`

```html
<div class="tablekit"> <p aria-live="polite" id="selCount">0 rows selected</p>
  <table class="dt"><caption>Payments</caption>
    <thead><tr><th scope="col"><input type="checkbox" id="all" aria-label="Select all on page"></th><th scope="col">Reference</th><th scope="col" class="num">Total</th></tr></thead>
    <tbody class="loading"> <tr><td colspan="3" class="skel"></td></tr> <tr><td colspan="3" class="skel"></td></tr> </tbody> <!-- skeletons keep column alignment -->
  </table>
  <div class="empty" hidden><p><strong>No payments match "q3 overdue".</strong> Try clearing filters or widening the date range.</p></div>
  <nav class="pager" aria-label="Payments pagination">
    <span>1-25 of 1,204</span> <button disabled aria-label="Previous page">‹</button> <button aria-label="Next page">›</button>
    <label>Per page <select aria-label="Rows per page"><option>25</option><option>50</option></select></label>
  </nav>
</div>
<script>
  // Simulated load: skeletons -> real rows (or empty state)
  setTimeout(() => {
    document.querySelector('.loading').remove();
    const tbody = document.querySelector('tbody');
    if (Math.random() > 0.5) {
      tbody.innerHTML = ['PAY-7781|120.00', 'PAY-7782|88.40'].map(r => { const [ref, amt] = r.split('|');
        return `<tr><td><input type="checkbox" class="rowSel" aria-label="Select ${ref}"></td><td>${ref}</td><td class="num">${amt}</td></tr>`; }).join('');
    } else {
      document.querySelector('table').hidden = true; document.querySelector('.empty').hidden = false; // zero-results is designed
    }
  }, 800);
  document.addEventListener('change', e => {
    if (e.target.id === 'all') document.querySelectorAll('.rowSel').forEach(c => c.checked = e.target.checked);
    const n = document.querySelectorAll('.rowSel:checked').length;
    document.getElementById('selCount').textContent = `${n} row${n === 1 ? '' : 's'} selected`; // count announced
  });
</script>
<style>
  .tablekit { font: 14px/1.4 Inter, system-ui, sans-serif; max-width: 480px; display: grid; gap: 8px; }
  .dt { border-collapse: collapse; width: 100%; }
  th, td { text-align: left; padding: 0 12px; height: var(--comp-table-row-height); border-bottom: 1px solid #F5F5F5; }
  .num { text-align: right; font-variant-numeric: tabular-nums; }
  .skel { height: var(--comp-table-row-height); padding: 0; }
  .skel::after { content: ""; display: block; height: 12px; margin: 0 12px; border-radius: 6px; background: linear-gradient(90deg, #F5F5F5, #E5E5E5, #F5F5F5); background-size: 200% 100%; animation: shimmer 1.2s ease infinite; }
  @keyframes shimmer { to { background-position: -200% 0; } }
  @media (prefers-reduced-motion: reduce) { .skel::after { animation: none; } }
  .empty { border: 1px dashed #D4D4D4; border-radius: 8px; padding: 16px; } .pager { display: flex; align-items: center; gap: 8px; }
  .pager button { min-width: 44px; min-height: 44px; border: 1px solid #D4D4D4; border-radius: 8px; background: #fff; cursor: pointer; }
  .pager button:focus-visible, .pager select:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every data view passes the `var(--comp-table-semantics)` decision rule: native `<table>` for read data, ARIA grid only for per-cell editing — no div tables.
- [ ] All tables declare `caption`, `th scope`, `thead`/`tbody` so screen reader navigation resolves every cell by its headers.
- [ ] Columns declare a type; numeric columns use `var(--comp-table-numeric-align)` (right-aligned, tabular figures) and actions render as kebab menus per `var(--comp-table-actions)`.
- [ ] Sortable headers are buttons that update `aria-sort` per `var(--comp-table-sort-announce)` and meet the 44px touch floor.
- [ ] Each table declares its selection model (`var(--comp-table-selection-model)`) and announces selection count via a live region.
- [ ] Long tables persist headers with `var(--comp-table-header-sticky)` without trapping focus.
- [ ] Zero-results shows a message plus suggestion (`var(--comp-table-empty-state)`); loading shows column-aligned `var(--comp-table-loading-state)` skeletons.
- [ ] Pagination reports counts and page size (`var(--comp-table-pagination)`) and persists page state in the URL.
