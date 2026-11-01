---
name: breakpoints-strategy
description: Content-driven breakpoints (not device names): a small tier set, mobile-first queries, and when container queries replace them.
tags: [responsive, breakpoints, media-queries, mobile-first, layout]
related: [grid-systems, flexbox-patterns, mobile-navigation]
---

# Responsive Layout Skill: Breakpoints Strategy

## 1. Definition

Breakpoints are the viewport widths where layout reorganizes — and the strategy question is how few you can afford. Modern practice: mobile-first (base styles are the small-screen truth, min-width queries add complexity upward), 4–5 content-driven tiers (640/768/1024/1280/1536) named by what changes, never by devices (devices multiply; content is stable). Container queries (guide 03) are replacing page-level breakpoints for component-level adaptation, so this skill owns the shell while components adapt themselves.

## 2. Core Principles

- **Mobile-first:** base CSS is the mobile layout; min-width queries add columns and chrome as space allows.
- **Content defines breakpoints:** add a tier when the design breaks, not when a new iPad ships — devices are an implementation detail.
- **Few tiers, named by change:** 5 tiers maximum, each named for what reorganizes (nav-collapse, sidebar-reveal, 3-col).
- **One unit system per concern:** px for viewport queries, em for component queries (respects user font size).
- **Every tier is tested:** layouts are signed off at each tier's width, not just desktop and "roughly mobile".
- **No breakpoint inside components that own a container:** components with container queries ignore viewport tiers — one owner per adaptation.
- **Ranges never overlap:** min-width chains exclusive (max-width: 767.98px patterns die; single-axis min-width stacks).

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Breakpoint strategy | `--layout-bp-strategy` | `mobile-first-min-width` | Base = mobile; queries add complexity upward |
| Small tier | `--layout-bp-sm` | `640px` | Large phones / small tablets |
| Medium tier | `--layout-bp-md` | `768px` | Tablet portrait; nav may collapse |
| Large tier | `--layout-bp-lg` | `1024px` | Tablet landscape / laptop; sidebar reveals |
| Extra-large tier | `--layout-bp-xl` | `1280px` | Desktop; 3-col layouts unlock |
| Wide tier | `--layout-bp-2xl` | `1536px` | Wide desktop; content max-width governs beyond |
| Tier naming | `--layout-bp-naming` | `by-what-changes` | sm/md/lg aliases documented per product |
| Component query unit | `--layout-component-bp-unit` | `em` | Container queries size in em (user-font aware) |
| Test widths | `--layout-test-widths` | `320,640,768,1024,1280,1536` | Screenshot matrix per release |
| Container query first | `--layout-container-query-first` | `prefer` | Components adapt via container queries; page tiers only for shell |

Consume them by linking `assets/css/breakpoints-strategy.css`, which emits the `@media (min-width: ...)` tiers from `var(--layout-bp-*)` values, then authoring product CSS against those tier classes/variables only. A width not in this table is not a tier — if the design breaks somewhere new, that is a governance decision to add a named tier, not a local 1100px query.

## 4. Composition

- **Composes with grid-systems:** tiers change grid column counts and margins — the grid is the thing being reorganized, and each tier maps to a documented column set.
- **Composes with fluid-container-queries:** the strategy decides what adapts at page level vs container level; overlap is the failure mode, so this skill explicitly hands component adaptation over.
- **Composes with mobile-navigation (guide 08):** nav collapse is the most common breakpoint-driven change — the md/lg tiers carry the bottom-bar/drawer/sidebar handoffs.

## 5. Signature Patterns

- **Tier-per-change map:** a table of tiers × what changes (columns, nav, sidebar, density) reviewed before building — unowned tiers get deleted. If a tier's row is empty, the tier does not exist in the product.
- **min-width stack:** one-directional media queries layered in source order; no max-width unless a legacy base demands it. Reading order equals width order, so reasoning about any width means reading downward, not hunting for overrides in both directions.

## 6. Real-World Use Cases

- **App shells with responsive sidebars and nav:** the canonical md = nav collapse, lg = sidebar reveal tier map.
- **Marketing pages with tiered section layouts:** sections gain columns as tiers unlock, without per-section queries.
- **Audit:** dead breakpoints, device-named tiers, overlapping ranges — the residue of strategy-free responsive CSS.

## 7. Combination Notes

### With other responsive-layout skills

- **Pairs naturally with grid-systems:** the tier map reorganizes the grid (12/8/4 columns, margin tiers); a tokenized grid means each tier change is a small, reviewable edit rather than a rewrite.
- **Pairs with flexbox-patterns, css-grid-patterns, and layout-compositions:** these describe how a region behaves at a tier; the strategy decides when the tier fires. Together they keep "when" and "how" separate concerns.
- **Pairs with responsive-images, mobile-navigation, data-tables-responsive, rtl-i18n-layout, and responsive-testing:** the test-widths token doubles as the screenshot matrix for images and tables; nav collapse and RTL re-orientation attach to named tiers instead of ad-hoc widths.
- **Caution with fluid-container-queries:** both can own the same adaptation decision — the classic double-adaptation bug where a component and the page tier both change its layout. The contract: page tiers own the shell; container queries own components. Coordinate explicitly when a component crosses regions.
- **Caution with intrinsic-design:** intrinsic layouts (auto-fill, min-content) shift behavior continuously without tiers; if a region is intrinsic, do not also attach viewport tiers to it, or the two mechanisms will disagree at intermediate widths.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** few tiers, few rules — a disciplined 5-tier map matches these styles' restraint, and their sparse layouts reorganize cleanly between tiers without intermediate states.
- **Caution with collage-art and maximalism:** dense, expressive compositions can genuinely break between the standard tiers and tempt teams into adding device-matched queries; when this happens, prefer re-thinking the composition for the tier over multiplying breakpoints.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** tier changes should be perceivable as calm reorganizations, not jarring jumps — consistent duration/easing tokens on transitions around tier-triggered state changes (sidebar reveal, drawer) keep the shell feeling like one system.

## 8. Anti-Patterns

- **Device-named tiers** — iPad-Pro-2 breakpoints that multiply every product cycle
- **Breakpoint soup** — 14 overlapping queries nobody dares delete
- **Desktop-first shrink** — max-width overrides fighting the base layout instead of mobile-first growth
- **Untested tiers** — layouts signed off at 1440px and broken at 1024px where half the users are

### Accessibility Notes

Breakpoints must preserve WCAG 1.4.4/1.4.10: zoom to 400% reflows to the single-column tier — test at zoom widths, not just device widths, because a 320px phone with default zoom and a 1280px desktop at 400% zoom hit different tiers and both must stay usable. Em-based component queries respect user font size, so users who enlarge text get earlier, gentler reorganization instead of clipped labels. The fallback rule: if a tier cannot be tested in time, degrade to the nearest tested tier and ship the gap as a documented known issue — never an untested silent tier, because silent tiers fail exactly the users on the widths nobody checked.

## 9. Code Examples

### Example 1 — Mobile-first min-width stack

Tokens: `assets/css/breakpoints-strategy.css`

```html
<nav class="tier-nav" aria-label="Demo">
  <span class="tier-label">tier: base</span>
</nav>
<script>
  const tiers = ['640px', '768px', '1024px', '1280px', '1536px'];
  // One-directional stack: report which named tier is active
  const label = document.querySelector('.tier-label');
  const update = () => {
    const w = innerWidth;
    const t = w >= 1536 ? '2xl' : w >= 1280 ? 'xl' : w >= 1024 ? 'lg' : w >= 768 ? 'md' : w >= 640 ? 'sm' : 'base';
    label.textContent = 'tier: ' + t;
  };
  addEventListener('resize', update); update();
</script>
<style>
  .tier-nav {
    background: #F5F5F5; border-radius: 8px;
    font: 600 14px/1.4 Inter, system-ui, sans-serif;
  }
  /* Base = mobile truth. Each query only ADDS. */
  .tier-nav { padding: 12px 16px; }
  @media (min-width: 640px)  { .tier-nav { padding: 12px 20px; } }
  @media (min-width: 768px)  { .tier-nav { padding: 14px 24px; background: #EBEBEB; } }
  @media (min-width: 1024px) { .tier-nav { padding: 16px 32px; } }
  @media (min-width: 1280px) { .tier-nav { padding: 16px 48px; } }
</style>
```

### Example 2 — Tier-per-change map

Tokens: `assets/css/breakpoints-strategy.css`

```html
<table class="tier-map">
  <caption>Tier-per-change map — reviewed before build; unowned tiers are deleted</caption>
  <thead>
    <tr><th scope="col">Tier</th><th scope="col">Width</th><th scope="col">What changes</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">sm</th><td>640px</td><td>2-col feature rows unlock</td></tr>
    <tr><th scope="row">md</th><td>768px</td><td>Nav collapses to horizontal bar</td></tr>
    <tr><th scope="row">lg</th><td>1024px</td><td>Sidebar reveals (drawer → inline)</td></tr>
    <tr><th scope="row">xl</th><td>1280px</td><td>3-col card grids unlock</td></tr>
    <tr><th scope="row">2xl</th><td>1536px</td><td>Content max-width governs beyond</td></tr>
  </tbody>
</table>
<style>
  .tier-map {
    border-collapse: collapse;
    font: 14px/1.5 Inter, system-ui, sans-serif;
    width: 100%; max-width: 560px;
  }
  .tier-map caption { text-align: left; font-weight: 600; padding-bottom: 8px; }
  .tier-map th, .tier-map td { border: 1px solid #D4D4D4; padding: 8px 12px; text-align: left; }
  .tier-map thead th { background: #F5F5F5; }
  .tier-map tbody th { font-weight: 600; }
</style>
```

## 10. Implementation Checklist

- [ ] Base CSS is the mobile layout; every query is `@media (min-width: ...)` — no max-width chains, no overlap.
- [ ] Tiers come only from `var(--layout-bp-*)` (640/768/1024/1280/1536); no product CSS hardcodes another width.
- [ ] Every tier is named by what changes and has a row in the tier-per-change map; empty rows were deleted.
- [ ] No device names (ipad, iphone) appear in any query or comment.
- [ ] The `--layout-test-widths` screenshot matrix is captured per release, including zoom/reflow widths.
- [ ] Components with container queries carry no viewport media queries — one owner per adaptation.
- [ ] Component-level queries use em units via `--layout-component-bp-unit`.
