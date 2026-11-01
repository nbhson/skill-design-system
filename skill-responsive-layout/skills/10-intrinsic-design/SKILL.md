---
name: intrinsic-design
description: Layouts from content, not viewport: min/max/clamp sizing, aspect-ratio, and the Every-Layout approach that needs fewer breakpoints.
tags: [layout, intrinsic-sizing, css-grid, fluid, every-layout]
related: [fluid-container-queries, flexbox-patterns, responsive-images]
---

# Responsive Layout Skill: Intrinsic Layout

## 1. Definition

Intrinsic design builds layouts from the content's own size preferences instead of viewport assumptions: min-content, max-content, fit-content, clamp(), and aspect-ratio let components absorb available space gracefully across any width. Popularized by Every Layout, the approach produces layouts that need dramatically fewer media queries — the content flexes, the viewport merely bounds it. It is the philosophy behind why modern CSS needs fewer breakpoints, not more.

## 2. Core Principles

- **Sizing from content:** min-content and max-content describe what content needs; layout math starts there, not from a guessed px value.
- **clamp() is the workhorse:** min 0, ideal some fraction, max 1 — the sidebar pattern minmax(auto, 1fr) absorbs space without queries.
- **The 'sidebar' pattern needs no breakpoint:** grid-template-columns: fit-content(280px) 1fr collapses naturally as space shrinks.
- **aspect-ratio reserves space declaratively:** media boxes and cards hold their shape without padding hacks.
- **Fewer queries is a symptom of good intrinsic math:** if every component needs 3 queries, the sizing strategy is wrong.
- **Intrinsic + container queries compose:** intrinsic sizing decides how a component wants to flex; container queries decide which variant renders.
- **Intrinsic does not mean uncontrolled:** max-width tokens and ch measures still bound growth — content-flexing within documented limits.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Strategy | `--layout-intrinsic-strategy` | `content-first-fewer-queries` | Sizing math before media queries |
| Sidebar | `--layout-intrinsic-sidebar` | `fit-content(280px) 1fr` | Breakpoint-free sidebar pattern |
| Clamp space | `--layout-intrinsic-clamp-space` | `clamp(1rem, 50vw - 10rem, 2rem)` | Fluid spacing without queries |
| Min width | `--layout-intrinsic-min-width` | `min-content` | The floor a flex item may shrink to |
| Max width | `--layout-intrinsic-max-width` | `max-content` | The ceiling content occupies naturally |
| Fit | `--layout-intrinsic-fit` | `fit-content(66ch)` | Reading measure as an intrinsic bound |
| Aspect | `--layout-intrinsic-aspect` | `aspect-ratio 16/9` | Media boxes reserve shape declaratively |
| Minmax absorb | `--layout-intrinsic-minmax-absorb` | `minmax(min-content, 1fr)` | Columns that absorb space, never overflow |
| Query budget | `--layout-intrinsic-query-budget` | `only-when-content-breaks` | Media queries added when content, not viewport, demands |
| Test range | `--layout-intrinsic-test-range` | `240px-2560px` | Continuous resize test, no fixed tier set |

Consume them by linking `assets/css/intrinsic-design.css` once at the app root, then referencing `var(--layout-intrinsic-*)` from layout classes — `grid-template-columns: var(--layout-intrinsic-sidebar)` is the canonical use. Because several values are sizing grammar (not lengths), they flow into declarations as whole values rather than individual units; never re-inline the raw math in a component, or the audit loses its single source.

## 4. Composition

- **Composes with fluid-container-queries:** intrinsic sizing is the pre-CQ philosophy; together they cover 'how it flexes' and 'which variant renders'.
- **Caution with grid-systems and breakpoints-strategy:** fixed 12-col tiers and fixed tier sets answer a different question — document which approach owns each surface instead of mixing both in one component.
- **Composes with responsive-images:** aspect-ratio and intrinsic width are shared contracts between layout and media.

## 5. Signature Patterns

- **The Every Layout primitives:** stack, cluster, sidebar, switcher, center, cover, grid — implemented once as reusable, query-light classes.
- **Query-budget audit:** count media/container queries per component; more than 1-2 signals the intrinsic math should be redone.

## 6. Real-World Use Cases

- **Content-of-unknown-length surfaces:** CMS pages, i18n text, user-generated content.
- **Component libraries meant to work in any slot without slot knowledge.**
- **Refactors reducing breakpoint count without losing responsive quality.**

## 7. Combination Notes

### With other responsive-layout skills

- **Good with fluid-container-queries:** these are two halves of one philosophy — intrinsic sizing answers how a component wants to flex, container queries answer which variant renders in the slot it landed in.
- **Good with flexbox-patterns, css-grid-patterns, and layout-compositions:** the Every Layout primitives (stack, cluster, sidebar, switcher) are intrinsic implementations of those patterns' vocabulary; flex/grid supply the mechanics, intrinsic sizing supplies the math.
- **Good with responsive-images:** aspect-ratio reservation and intrinsic width are contracts shared by layout and media — an image that flexes must sit in a box that already knows its shape.
- **Good with mobile-navigation, data-tables-responsive, rtl-i18n-layout, and responsive-testing:** intrinsic layouts still collapse (nav) and still scroll honestly (tables), and RTL plus continuous-resize testing is how the flexing claims get verified.
- **Caution with grid-systems:** a fixed 12-column system and intrinsic sizing answer different questions — one is an alignment skeleton, the other is content flexing. Mixing both inside one component produces double bookkeeping; document which approach owns each surface (e.g. shell on the grid, widgets intrinsic).
- **Caution with breakpoints-strategy:** fixed tier sets and intrinsic math fight over the same adaptation decisions. Do not sprinkle media queries on top of a component whose sizing is already intrinsic — the query budget exists precisely to police this boundary.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles favor quiet, well-proportioned structures where content-driven flexing and declarative shape reservation (aspect-ratio) do the compositional work without decoration.
- **Caution with collage-art and maximalism:** both may demand deliberately fixed, overlapping, or dimensioned placements that intrinsic flexing dissolves; where a style mandates fixed dimensions, scope them per-surface and document the deviation rather than fighting the intrinsic math.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** intrinsic layouts resize continuously as users resize or content changes; transitions on those size changes should use the shared duration/easing tokens so flexing feels intentional, not jittery.
- **No caution pairs:** intrinsic sizing does not conflict with any motion pattern — but animated size changes must never fight the user's resize gestures; keep durations short and respect reduced-motion.

## 8. Anti-Patterns

- **Viewport-brained defaults:** fixed widths everywhere with queries papering over the cracks
- **Query inflation:** 4 queries per component because the sizing strategy was never intrinsic
- **Unbounded flexing:** intrinsic sizing with no max-width tokens - text lines run to 200ch on wide screens
- **Cargo-cult minimalism:** refusing any breakpoint where a genuine content break exists

### Accessibility Notes

Intrinsic sizing is a zoom/accessibility ally: content-driven layouts survive 200%-400% zoom and text-spacing overrides better than fixed-width ones (WCAG 1.4.4/1.4.10) — flexing content IS the reflow strategy. The fallback rule keeps the approach honest: where intrinsic patterns cannot express a required design, add the minimal named breakpoint and document it — pragmatism over dogma. Note that 'unbounded flexing' is itself an accessibility hazard: a 200ch line is unreadable, so the ch-based bounds and max-width tokens are part of the accessibility floor, not just aesthetics.

## 9. Code Examples

### Example 1 — Query-light sidebar (fit-content absorbs, minmax never overflows)

Tokens: `assets/css/intrinsic-design.css`

```html
<div class="shell">
  <aside class="shell-nav">
    <h2>Workspace</h2>
    <a href="#">Overview</a><a href="#">Reports</a><a href="#">Settings</a>
  </aside>
  <main class="shell-main">
    <h1>Quarterly review</h1>
    <p>Content of unknown length flexes; the sidebar yields space without a media query.</p>
  </main>
</div>
<style>
  .shell {
    display: grid;
    /* fit-content collapses naturally; minmax(min-content, 1fr) absorbs, never overflows */
    grid-template-columns: var(--layout-intrinsic-sidebar);
    /* fallback absorb behavior for the main column */
    grid-auto-columns: var(--layout-intrinsic-minmax-absorb);
  }
  @media (max-width: 640px) {
    /* the ONE named query: a genuine content break (nav becomes a top strip) */
    .shell { grid-template-columns: 1fr; }
  }
  .shell-nav {
    padding: var(--layout-intrinsic-clamp-space);
    border-inline-end: 1px solid #ddd;
  }
  .shell-main {
    padding: var(--layout-intrinsic-clamp-space);
    max-width: var(--layout-intrinsic-fit); /* reading measure bounds growth */
  }
</style>
```

### Example 2 — Stack / cluster / switcher primitives + query-budget audit

```html
<div class="stack">
  <header class="cluster">
    <img src="avatar.png" alt="" width="48" height="48" style="aspect-ratio: 1; border-radius: 50%;">
    <strong>Media object via cluster</strong>
    <span class="spacer"></span>
    <button>Edit</button>
  </header>
  <div class="switcher">
    <section><h3>Card A</h3><p>Switcher children flip from row to column by count/space.</p></section>
    <section><h3>Card B</h3><p>No viewport query involved.</p></section>
    <section><h3>Card C</h3><p>Shape reserved declaratively below.</p></section>
  </div>
</div>
<style>
  .stack { display: flex; flex-direction: column; gap: var(--layout-intrinsic-clamp-space); }
  .cluster { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem; }
  .cluster .spacer { margin-inline-start: auto; }
  .switcher {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(auto-fit, minmax(min(var(--layout-intrinsic-min-width), 100%), 1fr));
  }
  .switcher section {
    aspect-ratio: 16 / 9; /* shape reserved without padding hacks */
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 8px;
  }
</style>
<script>
  // Query-budget audit: more than 1-2 media queries per component means the
  // intrinsic math should be redone (see --layout-intrinsic-query-budget).
  const budget = 2;
  document.querySelectorAll('.stack, .switcher').forEach(el => {
    const rules = [...document.styleSheets].flatMap(s => { try { return [...s.cssRules]; } catch { return []; } });
    const hits = rules.filter(r => r.media && [...r.media].some(() => true)).length;
    console.assert(hits <= budget, `query budget exceeded: ${hits} queries on`, el);
  });
</script>
```

## 10. Implementation Checklist

- [ ] Sizing math starts from min-content/max-content/fit-content via `var(--layout-intrinsic-*)` tokens — no guessed px widths in components.
- [ ] The sidebar composition uses `var(--layout-intrinsic-sidebar)` (fit-content + 1fr) and collapses with zero or one named media query.
- [ ] Fluid spacing uses `var(--layout-intrinsic-clamp-space)`; clamp endpoints never invent off-scale values.
- [ ] Every media box and card reserves shape with aspect-ratio (`--layout-intrinsic-aspect`) — no padding-hack ratio boxes.
- [ ] Growth is bounded: reading measure via `var(--layout-intrinsic-fit)` and documented max-width tokens — no 200ch lines.
- [ ] Each component's media/container query count is within the `--layout-intrinsic-query-budget` (1-2); violations trigger an intrinsic-math review.
- [ ] Layouts are verified by continuous resize across `var(--layout-intrinsic-test-range)` (240px-2560px), not just fixed tiers.
- [ ] Any unavoidable breakpoint is added minimally, named, and documented per the accessibility fallback rule.
