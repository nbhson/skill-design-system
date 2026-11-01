---
name: layout-compositions
description: The catalog: sidebar, split, stack, cluster, bento, holy grail - named, token-driven compositions instead of re-solved layout problems.
tags: [layout, patterns, catalog, design-systems, responsive]
related: [flexbox-patterns, css-grid-patterns, fluid-container-queries]
---

# Responsive Layout Skill: Named Layout Compositions

## 1. Definition

Layout compositions are named solutions to recurring layout problems: the sidebar+main shell, the split-pane, the stack (vertical rhythm), the cluster (wrapped chips), the bento grid, the holy grail. Giving them names and token-driven implementations turns layout from per-page problem-solving into a catalog — designers and engineers say "split with 320px sidebar" and both know exactly what renders. The catalog is the API between layout mechanics (guides 04–05) and page assembly: each composition is a small, documented class with token inputs and a declared responsive contract, so no page ever re-solves a sidebar from scratch.

## 2. Core Principles

- **Name every reusable layout:** unnamed layouts cannot be reused or audited — the catalog is the API.
- **Compositions consume tokens:** sidebar widths, gaps, and max-widths are tokens — a composition has no magic numbers.
- **Each composition declares its responsive behavior:** how it collapses (sidebar → drawer, split → stack) is part of the name's contract.
- **Stack is the default; complexity is earned:** most content is a stack with gaps — reach for sidebar/split only when hierarchy demands it.
- **Bento grids need hierarchy rules:** mixed-size cells must follow a size grammar (1 large + 2 medium + n small), not random tiles.
- **Compositions nest predictably:** sidebar contains stacks and clusters; nesting is documented, depth-capped (3 levels).
- **Every composition is RTL-safe and container-aware:** logical properties + container queries are baked into the catalog, not added per use.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Sidebar | `--layout-comp-sidebar` | `minmax(240px, 280px) 1fr` | Sidebar + fluid main; collapses to drawer under lg |
| Split | `--layout-comp-split` | `1fr 1fr + gap space-6` | Equal split panes; stacks under md |
| Stack | `--layout-comp-stack` | `flex column + gap space-4` | The default vertical rhythm container |
| Cluster | `--layout-comp-cluster` | `flex wrap + gap space-2` | Chips, tags, filter rows |
| Bento | `--layout-comp-bento` | `auto-fit minmax + dense` | Mixed-size dashboard grid |
| Holy grail | `--layout-comp-holy-grail` | `'header header' 'aside main' 'footer footer'` | The classic shell, grid-areas named |
| Center | `--layout-comp-center` | `place-items-center + min-height` | Empty states, loaders, splash |
| Sidebar collapse | `--layout-comp-sidebar-collapse` | `drawer-under-1024px` | The documented responsive contract |
| Nesting depth | `--layout-comp-nesting-depth` | `max-3` | Composition nesting ceiling |
| Catalog owner | `--layout-comp-catalog-owner` | `design-system` | The catalog lives in the DS; pages consume it |

Consume them by linking `assets/css/layout-compositions.css` at the app root — the catalog classes read `var(--layout-comp-sidebar)`, `var(--layout-comp-split)`, and `var(--layout-comp-cluster)`, so density and breakpoint changes propagate to every page at once. Pages never hand-roll a sidebar or split; if a composition does not fit, request a catalog addition through review rather than inlining bespoke CSS.

## 4. Composition

- **Compositions are the consuming layer of grid-systems, flexbox-patterns, and css-grid-patterns:** the patterns become named products. A sidebar composition is the `minmax` grid template with a collapse contract; a cluster is the flex wrap+gap idiom with a name.
- **Composes with fluid-container-queries:** compositions declare `container-type` so nested components adapt per slot — a card inside a narrow bento cell responds to the cell, not the viewport.
- **Composes with skill-component-recipes:** component recipes assume the catalog (tables render inside "sidebar" or "split" compositions), so component guidance stays layout-agnostic and the compositions carry the responsive burden.

## 5. Signature Patterns

- **Catalog-as-code:** each composition is a small class/utility with token inputs and documented collapse behavior — pages compose them. The composition source doubles as documentation: name, inputs, contract.
- **Collapse-contract table:** one table listing every composition × its mobile behavior; new compositions fill a row before shipping. QA tests against the row, not against folklore.

## 6. Real-World Use Cases

- **Design systems shipping layout primitives (Radix/Every Layout style):** the catalog is the public layout API of the system.
- **Rapid page assembly from named layouts instead of bespoke CSS:** a new page is a holy-grail shell containing a sidebar, a stack, and a cluster — hours, not days.
- **Audit: pages re-implementing "sidebar" badly instead of consuming the composition** — the named catalog makes deviations grep-able and review-able.

## 7. Combination Notes

### With other responsive-layout skills

- **Good with flexbox-patterns and css-grid-patterns:** these are the mechanics the catalog is built from — the compositions layer exists precisely to name and productize them. Building compositions without 04/05 means duplicating their patterns; using 04/05 raw on pages means the catalog was skipped.
- **Good with grid-systems and breakpoints-strategy:** named areas implement the 12-col system, and each composition's collapse contract declares which breakpoint tier triggers it — the strategy guide defines the tiers, this catalog fills in the per-composition behavior.
- **Good with fluid-container-queries and intrinsic-design:** container-awareness and intrinsic sizing are baked into every catalog entry, so pages get them for free instead of re-adding them per use.
- **Good with responsive-images, mobile-navigation, data-tables-responsive, rtl-i18n-layout, and responsive-testing:** images, drawers, tables, RTL mirroring, and the test matrix all assume compositions exist as named slots — those guides specify behavior inside a slot, never a new layout mechanism.
- **No caution or avoid list:** as the top consuming layer, this skill composes with everything beneath it; deviations surface as anti-patterns (bespoke layouts, magic numbers), not partner conflicts.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** the catalog enforces restrained, systematic structure — stacks with token gaps and clean splits are the structural expression of both styles.
- **Good affinity with maximalism:** the bento composition with its size grammar (1 large + 2 medium + n small) gives maximalist density a disciplined hierarchy, which is what separates expressive from chaotic.

### With motion skills (companion repo skill-animation)

- **Good affinity with page-transitions:** named pages assembled from named compositions give page transitions stable regions to animate between — the shell persists, main content cross-fades.
- **Good affinity with entrance-exit:** catalog entries are the stagger units — items entering a stack, cluster, or bento animate per composition slot with duration/easing tokens.
- **No caution list:** collapse contracts (drawer, stack) should pair with the animation repo's transition guidance so collapse is animated as a state change, not improvised per page.

## 8. Anti-Patterns

- **Bespoke everything** — every page re-solving sidebar layout with different values
- **Magic-number compositions** — named layouts with hardcoded px inside
- **Undeclared collapse** — compositions whose mobile behavior is discovered in QA
- **Nesting spirals** — 6-deep composition stacks where 2 would do

### Accessibility Notes

Composition collapse behavior is an accessibility surface: sidebar → drawer must preserve focus management and DOM order (a11y guides 03/04) — when the sidebar collapses under 1024px, focus moves into the drawer on open and returns to the trigger on close, and the underlying page is inert while the drawer is open. Collapse must never hide content from assistive technology without disclosure: content that disappears visually must either reappear in DOM order (stacked) or be inside a properly labeled disclosure widget. The fallback rule: if a composition cannot collapse accessibly (e.g. bento on mobile), it stacks in DOM order — visual bento is a wide-screen enhancement only, so the reading order of stacked cells must equal the desktop visual hierarchy defined by the size grammar.

## 9. Code Examples

### Example 1 — Page assembled from the catalog (holy grail + sidebar + stack + cluster + bento)

Tokens: `assets/css/layout-compositions.css`

```html
<div class="comp-holy-grail">
  <header class="hg-header">Admin Console</header>
  <div class="comp-sidebar">
    <nav class="comp-stack" aria-label="Sections">
      <a href="#">Overview</a><a href="#">Products</a><a href="#">Team</a>
    </nav>
  </div>
  <main class="hg-main">
    <div class="comp-cluster" aria-label="Filters">
      <button>All</button><button>Active</button><button>Archived</button>
    </div>
    <div class="comp-stack">
      <div class="comp-bento">
        <div class="bento-cell bento-large">Revenue — hero metric</div>
        <div class="bento-cell">Churn</div>
        <div class="bento-cell">MRR</div>
      </div>
    </div>
  </main>
  <footer class="hg-footer">© 2026</footer>
</div>
<style>
  .comp-holy-grail { /* --layout-comp-holy-grail = 'header header' 'aside main' 'footer footer' */
    display: grid; grid-template-areas: 'header header' 'aside main' 'footer footer';
    grid-template-columns: var(--layout-comp-sidebar); /* minmax(240px, 280px) 1fr */
    grid-template-rows: auto 1fr auto; min-height: 100vh; gap: var(--space-4);
  }
  .hg-header { grid-area: header; padding: var(--space-4); border-bottom: 1px solid #ddd; }
  .hg-main   { grid-area: main; container-type: inline-size; padding: var(--space-4); }
  .hg-footer { grid-area: footer; padding: var(--space-3) var(--space-4); border-top: 1px solid #ddd; }
  .comp-sidebar  { grid-area: aside; background: #f5f5f5; padding: var(--space-4); }
  .comp-stack    { display: flex; flex-direction: column; gap: var(--space-4); } /* --layout-comp-stack */
  .comp-stack > a { color: #171717; text-decoration: none; padding: 6px 8px; border-radius: 6px; font: 500 14px/1.4 system-ui, sans-serif; }
  .comp-stack > a:hover { background: #eee; }
  .comp-cluster  { display: flex; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-4); } /* --layout-comp-cluster */
  .comp-cluster > button { padding: 6px 12px; border: 1px solid #ccc; border-radius: 999px; background: #fff; font: 500 13px/1 system-ui, sans-serif; cursor: pointer; }
  .comp-bento { /* --layout-comp-bento = auto-fit minmax + dense */
    display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); grid-auto-flow: dense; gap: var(--space-4); }
  .bento-cell    { padding: var(--space-4); border: 1px solid #ddd; border-radius: 8px; font: 14px/1.5 system-ui, sans-serif; }
  .bento-large   { grid-column: span 2; grid-row: span 2; font: 600 18px/1.4 system-ui, sans-serif; }
  @media (max-width: 1023px) { /* collapse contract: sidebar → drawer under lg (--layout-comp-sidebar-collapse) */
    .comp-holy-grail { grid-template-areas: 'header' 'main' 'footer'; grid-template-columns: 1fr; }
    .comp-sidebar { position: fixed; inset: 0 auto 0 0; width: 280px; transform: translateX(-100%); transition: transform 200ms ease; }
    .comp-sidebar[data-open] { transform: none; }
  }
</style>
```

### Example 2 — Collapse-contract table

Tokens: `assets/css/layout-compositions.css`

```html
<table class="contracts">
  <caption>Collapse contracts — every composition declares its mobile behavior before shipping</caption>
  <thead>
    <tr><th scope="col">Composition</th><th scope="col">Token</th><th scope="col">Mobile behavior</th></tr>
  </thead>
  <tbody>
    <tr><td>Sidebar</td><td><code>var(--layout-comp-sidebar-collapse)</code></td><td>Drawer under 1024px, focus-managed</td></tr>
    <tr><td>Split</td><td><code>var(--layout-comp-split)</code></td><td>Stacks to one column under 768px</td></tr>
    <tr><td>Stack</td><td><code>var(--layout-comp-stack)</code></td><td>Unchanged — already the default</td></tr>
    <tr><td>Cluster</td><td><code>var(--layout-comp-cluster)</code></td><td>Wraps; never clips</td></tr>
    <tr><td>Bento</td><td><code>var(--layout-comp-bento)</code></td><td>Stacks in DOM order (size grammar defines order)</td></tr>
  </tbody>
</table>
<style>
  .contracts { border-collapse: collapse; width: 100%; max-width: 640px; font: 14px/1.5 system-ui, sans-serif; }
  .contracts caption { text-align: left; font-weight: 600; padding-bottom: 8px; }
  .contracts th, .contracts td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
  .contracts thead th { background: #f5f5f5; }
</style>
```

## 10. Implementation Checklist

- [ ] Every reusable layout on a page resolves to a named catalog class — zero bespoke sidebar/split/stack re-implementations.
- [ ] Catalog classes consume `var(--layout-comp-...)` tokens from `assets/css/layout-compositions.css`; no hardcoded px inside any composition.
- [ ] Every composition's collapse behavior is written in the collapse-contract table before it ships.
- [ ] Sidebar → drawer collapse implements focus management (focus in on open, restore on close) and never hides content from AT without disclosure.
- [ ] New pages default to the stack composition; sidebar/split/bento require a stated hierarchy reason.
- [ ] Bento grids follow the size grammar (1 large + 2 medium + n small); no random tile mixes.
- [ ] Composition nesting stays within `--layout-comp-nesting-depth` (max 3).
- [ ] All compositions use logical properties and declare `container-type`, staying RTL-safe and container-aware by default.
