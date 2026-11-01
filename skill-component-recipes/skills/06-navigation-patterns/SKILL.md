---
name: navigation-patterns
description: Top bars, sidebars, breadcrumbs, and pagination: the wayfinding components, current-page semantics, and responsive collapse contracts.
tags: [navigation, sidebar, breadcrumbs, wayfinding, a11y]
related: [dropdowns-menus, tabs-accordions, command-palette]
---

# Component Recipe: Navigation Patterns

## 1. Definition

Navigation components are the wayfinding layer: top bars (identity + global actions), sidebars (section nav with collapsible groups), breadcrumbs (hierarchy location), tabs-as-nav, and pagination. The recipe covers each pattern's structure, the current-page contract (aria-current + visual marker), keyboard behavior, and responsive collapse (sidebar → drawer per responsive-layout guide 08).

## 2. Core Principles

- **Nav landmarks structure the page:** header/nav/main/footer landmarks with one main — the page skeleton ships as a template (a11y repo aria-fundamentals).
- **Current page is semantic + visual:** aria-current=page plus a visual marker — both, always (a11y 1.4.1).
- **Sidebars declare depth and grouping:** collapsible sections with aria-expanded; depth capped at 3 — deeper IA is restructured, not nested.
- **Breadcrumbs for hierarchy, back for flow:** breadcrumbs show where you are in a hierarchy; back buttons/links handle task flow — never confuse them.
- **Skip links are part of nav:** the nav block ships with the skip-to-content link as one template.
- **Keyboard paths are nav contracts:** menu triggers, drawer toggles, and breadcrumb links are all keyboard-operable with visible focus.
- **Pagination for archives, load-more for feeds:** pagination preserves place (URL state); infinite feeds need a 'jump to top' escape.
- **Responsive collapse is declared:** sidebar → drawer, top bar → bottom bar — the collapse contract is written with the component (responsive-layout guide 08).

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| nav-landmark-set | `--comp-nav-landmark-set` | `header-nav-main-footer` | Page skeleton; one main |
| nav-current-mark | `--comp-nav-current-mark` | `aria-current+visual` | Double signal for current location |
| sidebar-width | `--comp-sidebar-width` | `minmax(240px, 280px)` | Sidebar width contract |
| sidebar-depth-cap | `--comp-sidebar-depth-cap` | `3` | Deeper IA is restructured |
| sidebar-group-toggle | `--comp-sidebar-group-toggle` | `aria-expanded` | Collapsible groups narrated |
| breadcrumb-separator | `--comp-breadcrumb-separator` | `/-aria-hidden` | Separators decorative; nav is the list |
| skip-link-required | `--comp-skip-link-required` | `template-bundled` | Skip link ships with nav template |
| nav-target-size | `--comp-nav-target-size` | `44px` | Touch floor for nav items |
| pagination-policy | `--comp-pagination-policy` | `archives-only+url-state` | Feeds use load-more |
| nav-collapse-contract | `--comp-nav-collapse-contract` | `declared-per-breakpoint` | Collapse behavior is written, not discovered |

Consume them by linking `assets/css/navigation-patterns.css` once at the app root: the shell grid reads `var(--comp-sidebar-width)`, nav items enforce `var(--comp-nav-target-size)` as their minimum interactive area, and the collapse breakpoints resolve from `var(--comp-nav-collapse-contract)`-declared rules. Pages consume the nav template — no page-level stylesheet redefines widths, target sizes, or current-page styling.

## 4. Composition

- **Composes with responsive-layout guides 01/08:** the shell grid and mobile collapse contracts are shared documents.
- **Composes with keyboard-navigation (skill-accessibility guide 03):** skip links, landmarks, and keyboard paths are the a11y layer of this recipe.
- **Composes with dropdowns-menus (guide 09):** nav overflow items collapse into the menu pattern.

## 5. Signature Patterns

- **Nav template kit:** header + sidebar + breadcrumbs + skip link as one composable template — pages assemble wayfinding, never rebuild it.
- **Current-page contract:** one helper resolves aria-current + visual marker across top bar, sidebar, and breadcrumbs from the same route state.

## 6. Real-World Use Cases

- **App shells for dashboards and admin tools** where a persistent sidebar and top bar carry the whole IA.
- **Documentation/marketing sites with hierarchical nav** where breadcrumbs and section sidebars do the location work.
- **Audit** for missing aria-current, breadcrumbs-as-back-buttons, and sidebar depth spirals.

## 7. Combination Notes

### With other component-recipe skills

- **Good with dropdowns-menus, tabs-accordions, and command-palette:** nav overflow collapses into menus, section switches use tabs-as-nav, and power users reach any destination through the palette — all three extend the same wayfinding layer.
- **Good with buttons-badges, forms-inputs, and cards-lists:** top bar actions use the button contract, settings pages nest inside the shell, and content cards fill the main region the landmarks define.
- **Good with tables-data-grid, toasts-notifications, modals-dialogs, empty-loading-error, and accessibility-wiring:** data views, feedback, and dialogs all assume the shell exists — this recipe supplies the skeleton they render into, and wiring skills verify its landmark/current-page semantics.
- **No caution or avoid list:** wayfinding is infrastructure every other recipe sits inside; failures come from pages rebuilding nav rather than consuming the template.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** navigation benefits most from restraint — thin borders, clear current markers, no competing ornament — so the current-page signal stays the strongest visual on the surface.
- **Good affinity with class-morphism:** soft depth on sidebar groups and top bar gives gentle hierarchy without noisy borders, as long as active states keep a flat, unmistakable marker.
- **Caution with collage-art:** collage styling encourages rotated, overlapping fragments that undermine predictable nav placement; if used, keep the nav template itself geometric and reserve collage for content regions.

### With motion skills (companion repo skill-animation)

- **Good affinity with page-transitions and micro-interactions:** crossfade or shared-element page transitions belong at this layer — the shell stays stable while main content transitions — and sidebar group expand/collapse plus drawer slide-ins are the canonical micro-interactions, driven by the same aria-expanded state that narrates them.
- **No caution list:** motion must never gate navigation — links work during transitions, and reduced-motion collapses drawer/expand animations to instant state changes.

## 8. Anti-Patterns

- **Current-page guesswork** — users lost because active nav state is a subtle tint
- **Breadcrumb-as-back** — hierarchical crumbs used for task flow back-navigation
- **Depth spiral** — 5-level sidebar nesting nobody can hold in memory
- **Nav rebuild per page** — every page hand-rolling its header instead of consuming the template

### Accessibility Notes

Navigation implements WCAG 1.3.1/2.4.1/2.4.5-2.4.8: landmarks, skip links, current-location semantics, and consistent placement — the nav template is the accessibility skeleton of the product. The landmark set (header/nav/main/footer, exactly one main) gives screen reader users a map; the skip link bundled with the template bypasses repeated nav on every page; `aria-current="page"` plus a visible marker gives current location a double signal that survives color blindness and low vision; and consistent placement across pages means users learn the wayfinding once. Collapsible sidebar groups narrate their state through aria-expanded, and every trigger — drawer toggle, group header, breadcrumb link — is keyboard-operable with visible focus. The fallback rule: If a full sidebar cannot be keyboard-perfect in time, ship the flat top-nav variant — a simple, complete keyboard path beats a rich, broken one.

## 9. Code Examples

### Example 1 — App shell: header, sidebar, breadcrumbs, skip link, aria-current

```html
<a class="skip-link" href="#main">Skip to content</a>
<header class="topbar">
  <button class="drawer-toggle" aria-expanded="false" aria-controls="sidebar">☰</button>
  <span class="brand">Acme Admin</span>
  <nav aria-label="Global"><a href="/settings">Settings</a></nav>
</header>
<div class="shell">
  <nav id="sidebar" class="sidebar" aria-label="Sections">
    <a href="/dashboard">Dashboard</a><a href="/projects">Projects</a><a href="/members">Members</a>
  </nav>
  <main id="main">
    <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/dashboard">Dashboard</a></li></ol></nav>
    <h1>Dashboard</h1>
  </main>
</div><style>
  .skip-link { position: absolute; left: -9999px; top: 0; background: #2563EB; color: #fff; padding: 10px 16px; border-radius: 0 0 8px 0; z-index: 100; }
  .skip-link:focus { left: 0; }
  .topbar { display: flex; align-items: center; gap: 16px; height: 56px; padding: 0 20px; border-bottom: 1px solid #E5E5E5; }
  .topbar nav a { padding: 8px 12px; text-decoration: none; color: #171717; border-radius: 6px; }
  .topbar nav a:hover { background: #F5F5F5; }
  .brand { font: 650 15px Inter, sans-serif; margin-right: auto; }
  .shell { display: grid; grid-template-columns: var(--comp-sidebar-width, minmax(240px, 280px)) 1fr; min-height: calc(100vh - 56px); }
  .sidebar { border-right: 1px solid #E5E5E5; padding: 16px 8px; display: flex; flex-direction: column; gap: 2px; }
  .sidebar a { min-height: var(--comp-nav-target-size, 44px); display: flex; align-items: center; padding: 0 14px; border-radius: 8px; text-decoration: none; color: #404040; }
  .sidebar a:hover { background: #F5F5F5; }
  .sidebar a[aria-current="page"] { background: #EFF6FF; color: #1D4ED8; font-weight: 650; } /* double signal */
  .crumbs ol { list-style: none; display: flex; gap: 8px; margin: 0 0 12px; padding: 0; font: 13px Inter, sans-serif; }
  .crumbs li + li::before { content: "/"; margin-right: 8px; color: #D4D4D4; } /* decorative separator */
  .crumbs a { color: #737373; text-decoration: none; } .crumbs [aria-current="page"] { color: #171717; font-weight: 600; }
  main { padding: 24px; }
  @media (max-width: 767px) { /* declared collapse: sidebar → drawer */
    .shell { grid-template-columns: 1fr; }
    .sidebar { display: none; }
    .sidebar[data-open] { display: flex; position: fixed; inset: 56px 0 0 0; background: #fff; z-index: 50; }
  }
</style>
<script>
  // Current-page contract: one route state drives every marker.
  const route = '/dashboard';
  document.querySelectorAll('.sidebar a, .topbar nav a').forEach((a) => {
    if (a.getAttribute('href') === route) a.setAttribute('aria-current', 'page');
  });
  // Declared collapse: the drawer toggle narrates via aria-expanded.
  const toggle = document.querySelector('.drawer-toggle'), sidebar = document.getElementById('sidebar');
  toggle.addEventListener('click', () => toggle.setAttribute('aria-expanded', String(sidebar.toggleAttribute('data-open'))));
</script>
```

### Example 2 — Collapsible sidebar group with aria-expanded

```html
<nav class="sidebar-groups" aria-label="Workspace">
  <button class="group-toggle" aria-expanded="true" aria-controls="grp-projects">Projects <span class="chev" aria-hidden="true">▾</span></button>
  <ul id="grp-projects" class="group">
    <li><a href="/p/aurora">Aurora</a></li><li><a href="/p/nimbus">Nimbus</a></li>
  </ul>
  <button class="group-toggle" aria-expanded="false" aria-controls="grp-archive">Archive <span class="chev" aria-hidden="true">▾</span></button>
  <ul id="grp-archive" class="group" hidden>
    <li><a href="/a/2025">2025</a></li>
  </ul>
</nav>
<style>
  .sidebar-groups { width: 260px; border: 1px solid #E5E5E5; border-radius: 12px; padding: 8px; font: 14px/1.4 Inter, sans-serif; }
  .group-toggle { width: 100%; display: flex; align-items: center; justify-content: space-between; min-height: 44px;
                  padding: 0 12px; background: none; border: none; cursor: pointer; border-radius: 8px; font: 600 13px Inter, sans-serif; color: #171717; }
  .group-toggle:hover { background: #F5F5F5; }
  .group-toggle:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; }
  .group-toggle[aria-expanded="false"] .chev { transform: rotate(-90deg); }
  .chev { transition: transform 150ms ease; }
  .group { list-style: none; margin: 0 0 4px; padding: 0 0 0 24px; }
  .group a { display: flex; align-items: center; min-height: 44px; padding: 0 12px; border-radius: 8px; color: #404040; text-decoration: none; }
  .group a:hover { background: #F5F5F5; }
  .group a[aria-current="page"] { background: #EFF6FF; color: #1D4ED8; font-weight: 600; }
</style>
<script>
  document.querySelectorAll('.group-toggle').forEach((btn) => {
    btn.addEventListener('click', () => {
      const panel = document.getElementById(btn.getAttribute('aria-controls'));
      const open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open)); // state narrates to AT; visual matches
      panel.hidden = open;
    });
  });
</script>
```

## 10. Implementation Checklist

- [ ] Pages assemble the nav template (header + sidebar + breadcrumbs + skip link); no page hand-rolls its own header (`--comp-nav-landmark-set`, `--comp-skip-link-required`).
- [ ] Exactly one `<main>` landmark exists per page, and the skip link targets it.
- [ ] Current location is marked with `aria-current="page"` AND a visible marker in top bar, sidebar, and breadcrumbs from one route-state helper (`--comp-nav-current-mark`).
- [ ] Sidebar width uses `minmax(240px, 280px)` from the shell grid — no page-level width overrides (`--comp-sidebar-width`).
- [ ] Sidebar nesting never exceeds 3 levels; deeper IA goes back to restructuring, not more indentation (`--comp-sidebar-depth-cap`).
- [ ] Collapsible groups toggle `aria-expanded` and keep the panel's visual state in sync (`--comp-sidebar-group-toggle`).
- [ ] Breadcrumb separators are `aria-hidden` decorative content; breadcrumbs never substitute for back buttons in task flow (`--comp-breadcrumb-separator`).
- [ ] Every nav item meets the 44px touch floor, and the sidebar → drawer collapse behavior is written per breakpoint (`--comp-nav-target-size`, `--comp-nav-collapse-contract`).
