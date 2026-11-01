---
name: fluid-container-queries
description: Components that adapt to their container, not the viewport: container queries, cqi units, and fluid spacing/type between bounds.
tags: [container-queries, fluid, cqi, components, layout]
related: [grid-systems, intrinsic-design, layout-compositions]
---

# Responsive Layout Skill: Fluid Layout & Container Queries

## 1. Definition

Container queries invert responsive design: instead of components asking "how wide is the viewport", they ask "how wide is my container" — so a card renders its compact variant in a sidebar and its full variant in the main column, with no viewport knowledge. Combined with fluid spacing/type (clamp on cqi units) and intrinsic sizing (min/max-content), layouts become truly reusable: the same component works anywhere it is dropped, whether that is a 260px dashboard widget, a modal body, or a full-width marketing band.

## 2. Core Principles

- **Container queries for components, media queries for the shell:** page chrome (nav, sidebar reveal) stays viewport-driven; widgets adapt to their slot.
- **Name containers by role:** `.card-container`, `.widget-container` — containment is explicit, never accidental global containment.
- **cqi/cqw for internal fluid sizing:** container query units make internal type/spacing scale with the container, not the screen.
- **Every container-queried component has 2-3 named states:** compact / standard / expanded — states documented like the breakpoints they replaced.
- **Fallbacks for legacy browsers:** modern targets are fine (container queries are Baseline 2023), but feature-detect rather than assume in long-support products.
- **Fluid bounds are tokens:** clamp() endpoints come from the spacing/type scales — fluidity never introduces off-scale values.
- **Test components in their narrowest slot:** a card tested only full-width will break in the sidebar it was promised to work in.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Container query strategy | `--layout-cq-strategy` | `components-over-viewport` | Widgets adapt to containers; shell uses media queries |
| Container type | `--layout-cq-type` | `inline-size` | Default containment; height queries are rare |
| Compact below | `--layout-cq-compact-below` | `320px` | Compact state trigger (container width) |
| Standard range | `--layout-cq-standard-range` | `320-640px` | Standard state |
| Expanded above | `--layout-cq-expanded-above` | `640px` | Expanded state trigger |
| Fluid space | `--layout-fluid-space` | `clamp(1rem, 3cqi, 2rem)` | Internal padding scales with container |
| Fluid heading (cq) | `--layout-fluid-heading-cq` | `clamp(1.25rem, 4cqi, 1.953rem)` | Widget title scales in container space |
| Intrinsic width | `--layout-intrinsic-width` | `min-content/max-content` | Intrinsic sizing before container math |
| Container query fallback | `--layout-cq-fallback` | `@supports-feature-detect` | Legacy path: viewport query equivalent |
| Test slots | `--layout-cq-test-slots` | `sidebar,main,modal` | Every container component tested in its 3 slots |

Consume them by linking `assets/css/fluid-container-queries.css`, then declaring `container-type: var(--layout-cq-type)` on named slot wrappers and using `var(--layout-fluid-space)` / `var(--layout-fluid-heading-cq)` inside components. A clamp endpoint not drawn from the spacing/type scales is an off-scale value — extend the scale through review, never inline a magic clamp.

## 4. Composition

- **Composes with grid-systems and layout-compositions:** containers are the slots the grid creates; components adapt inside them, so the grid stays macro and containers handle micro.
- **Composes with breakpoints-strategy:** the strategy split (shell vs component) prevents double adaptation — one owner per responsive decision, negotiated explicitly.
- **Composes with typography fluid tokens (skill-typography guide 06):** cqi-based type inside containers follows the same clamp discipline as viewport fluid type — same method, different query context.

## 5. Signature Patterns

- **Slot-tested components:** each container-aware component ships with a test page rendering it in sidebar/main/modal slots simultaneously — the demo page is the component's contract, and a state that fails in one slot blocks release.
- **Progressive containment:** add container-type to wrappers; components declare `@container` rules that no-op gracefully without a named ancestor — dropping a card into an un-instrumented page degrades to its base styles, never to breakage.

## 6. Real-World Use Cases

- **Design systems:** one card component that works in every slot — sidebar rail, main column, modal, bento cell.
- **Dashboard widgets rearranged per user (masonry/bento):** widgets must look right wherever a user drags them; container queries are the only honest mechanism.
- **CMS-driven pages where component placement is unpredictable:** editors compose layouts the component author never saw, so adaptation must travel with the component.

## 7. Combination Notes

### With other responsive-layout skills

- **Pairs naturally with grid-systems and layout-compositions:** the grid and named compositions create the slots (sidebar, main, modal, bento cell); container queries are how components adapt inside those slots. Slots declare containment; components declare states.
- **Pairs with flexbox-patterns and css-grid-patterns:** the component internals that switch between compact/standard/expanded states are flex/grid patterns — container queries decide which pattern renders, flex/grid implement it.
- **Pairs with responsive-images, intrinsic-design, mobile-navigation, data-tables-responsive, rtl-i18n-layout, and responsive-testing:** images can size to container width, tables and nav can adapt per slot, logical properties keep RTL container-safe, and the slot test page extends the testing matrix from viewports to slots.
- **Caution with breakpoints-strategy:** the two overlap on one question — who owns an adaptation. The contract: shell (nav, sidebar reveal, page columns) is viewport-driven; widgets are container-driven. Both skills together are good only with that split written down; without it, double adaptation fights itself.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and maximalism styles:** bento-style maximalist dashboards and flat layouts are exactly the "same component, many slots" world container queries were built for, and minimal components carry fewer state branches per container state.
- **Caution with collage-art:** collage compositions deliberately overlap and rotate elements, which undermines the tidy containment boundaries container queries assume; if a component must live inside a collage region, give it an explicit named container rather than inheriting one from the collage wrapper.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** state changes between compact/standard/expanded should animate with duration/easing tokens, so a card reflowing as its slot resizes feels like a continuous, calm transition rather than a snap.
- **Caution with continuous/ambient motion tied to cqi units:** anything animating with container units on every frame should be measured for jank; fluid spacing is for layout stability, not for animated values on the hot path.

## 8. Anti-Patterns

- **Double adaptation** — a component with both media and container queries fighting over the same decision
- **Anonymous containment** — container-type sprinkled globally, changing layout for everything downstream
- **Viewport-brained components** — widgets that ask viewport width and break in sidebars
- **Untested narrow slots** — container components shipped after testing only full-width

### Accessibility Notes

Container adaptation must keep WCAG 1.4.4/1.4.10 floors: compact states never shrink text below 12px or targets below 24px — adapt the layout, not the legibility, because "compact" must mean fewer elements and tighter chrome, never smaller type or un-tappable controls. The fallback rule: if container queries are unsupported in a required target, the feature-detect fallback (`@supports (container-type: inline-size)`) renders the standard viewport-based variant — compact variants are progressive enhancement, so the baseline experience is complete without them and no user ever receives a broken intermediate state.

## 9. Code Examples

### Example 1 — Card with named container states and fluid spacing

Tokens: `assets/css/fluid-container-queries.css`

```html
<aside class="slot-sidebar"><article class="cq-card">Compact card in a narrow slot</article></aside>
<main class="slot-main"><article class="cq-card">Standard card in the main column —
  padding and title size with the container, not the screen.</article></main>
<style>
  .slot-sidebar, .slot-main { container: card-container / inline-size; }
  .slot-sidebar { width: 280px; }
  .slot-main { width: 560px; }
  .cq-card {
    /* Fluid spacing: scales 1rem → 2rem with container width */
    padding: var(--layout-fluid-space);
    border: 1px solid #D4D4D4; border-radius: 8px;
    font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .cq-card h3 { margin: 0 0 8px; font: 600 var(--layout-fluid-heading-cq)/1.3 Inter, sans-serif; }
  .cq-card .meta { display: none; } /* hidden in compact */
  /* Named states, mirrors the cq tokens */
  @container card-container (max-width: 320px) { .cq-card { --state: compact; } }
  @container card-container (min-width: 320px) and (max-width: 640px) {
    .cq-card .meta { display: flex; gap: 8px; }
  }
  @container card-container (min-width: 640px) {
    .cq-card .extra { display: block; }
  }
  .cq-card { background: #F5F5F5; }
</style>
```

### Example 2 — Slot test page with fallback detection

Tokens: `assets/css/fluid-container-queries.css`

```html
<div class="slots">
  <div class="slot slot-sidebar" data-slot="sidebar"><article class="cq-card">Sidebar</article></div>
  <div class="slot slot-main" data-slot="main"><article class="cq-card">Main</article></div>
  <div class="slot slot-modal" data-slot="modal"><article class="cq-card">Modal</article></div>
</div>
<script>
  // Feature-detect: compact states are progressive enhancement
  const ok = CSS.supports('container-type: inline-size');
  document.documentElement.dataset.cq = ok ? 'supported' : 'fallback';
  // Test slots mirror --layout-cq-test-slots: sidebar, main, modal
  console.assert(document.querySelectorAll('.slot').length === 3, 'all 3 test slots must render');
</script>
<style>
  .slots { display: flex; flex-direction: column; gap: 16px; font: 14px/1.5 Inter, system-ui, sans-serif; }
  .slot { container: card-container / inline-size; border: 1px dashed #D4D4D4; border-radius: 8px; padding: 8px; }
  .slot-sidebar { width: 260px; }
  .slot-main { width: 480px; }
  .slot-modal { width: 380px; }
  .cq-card { padding: var(--layout-fluid-space); background: #F5F5F5; border-radius: 8px; }
  @container card-container (max-width: 320px) {
    .cq-card { padding: 8px; } /* compact: tighter chrome, never smaller than 12px text */
  }
  :root[data-cq="fallback"] .cq-card { padding: 16px; } /* viewport-equivalent fallback */
</style>
```

## 10. Implementation Checklist

- [ ] Components adapt via `@container` rules only; viewport media queries live exclusively in the shell — zero double adaptation.
- [ ] Every container wrapper declares `container-type: var(--layout-cq-type)` with a role-named class; no anonymous containment.
- [ ] Internal padding/spacing uses `var(--layout-fluid-space)`; internal headings use `var(--layout-fluid-heading-cq)`.
- [ ] Each container-queried component documents its compact/standard/expanded states against `--layout-cq-*` thresholds.
- [ ] Every container component ships a slot test page covering sidebar, main, and modal.
- [ ] A `@supports` fallback path renders the standard variant for legacy targets.
- [ ] clamp() endpoints come from spacing/type scale tokens — no off-scale fluid values.
