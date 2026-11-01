---
name: flexbox-patterns
description: One-dimensional layout patterns: nav bars, media objects, toolbars, and the alignment/gap idioms that solve 80% of component layout.
tags: [layout, flexbox, css, components, responsive]
related: [css-grid-patterns, layout-compositions, fluid-container-queries]
---

# Responsive Layout Skill: Flexbox Patterns

## 1. Definition

Flexbox solves one-dimensional layout: rows and columns of items that distribute space, align, and wrap. Its patterns cover most component-level layout — nav bars, media objects, button groups, toolbars, form rows — with `gap`, `align-items`, and the `flex` shorthand as the core vocabulary. The skill is knowing when flex is wrong: two-dimensional layouts belong to CSS Grid (guide 05), and content-flow documents belong to normal flow. Mastering flex means internalizing a small set of idioms — fill-plus-shrink, wrap-plus-gap, cross-axis alignment — and applying them as named patterns rather than re-solving spacing and alignment on every component.

## 2. Core Principles

- **One axis = flexbox:** toolbars, nav rows, button groups, media objects — if items flow in one direction, flex is the tool.
- **Two dimensions = grid:** page scaffolding and card grids belong to CSS Grid; forcing flex grids creates wrapper-div soup.
- **gap over margins:** flex gap handles spacing without `:last-child` overrides and works with wrap.
- **`flex: 1` is "fill remaining", not "equal":** flex-grow distributes leftover space; `min-width: 0` is required for content to shrink (the classic overflow bug).
- **align-items for cross-axis truth:** center alignment of mixed-height content (icon + two-line text) is flex's killer feature.
- **wrap is a layout decision:** `flex-wrap` on toolbars that must reflow; `nowrap` with overflow handling on scrollable rails.
- **Respect intrinsic content:** flex items size to content first — forcing equal widths needs `flex-basis` or grid, not min-width hacks.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Nav pattern | `--layout-flex-nav-pattern` | `space-between+center` | Nav bars: logo left, actions right, centered items |
| Media object | `--layout-flex-media-object` | `gap+align-start` | Icon/avatar + content rows; the workhorse pattern |
| Toolbar | `--layout-flex-toolbar` | `wrap+gap-2` | Button/action toolbars that reflow |
| Fill | `--layout-flex-fill` | `flex: 1 + min-width: 0` | Fill-remaining items; truncation needs min-width 0 |
| Gap unit | `--layout-flex-gap-unit` | `space tokens` | gap consumes the 4px scale |
| Truncate | `--layout-flex-truncate` | `ellipsis-on-flex-child` | min-width: 0 + overflow hidden + nowrap |
| Sticky footer | `--layout-flex-sticky-footer` | `column + mt-auto` | Page shell: header/content/footer pattern |
| Rail | `--layout-flex-rail` | `overflow-x + scroll-snap` | Horizontal card rails; pairs with scroll-animation |
| Centering | `--layout-flex-centering` | `place-center` | Absolute-free centering for badges/empty states |
| Flex vs grid | `--layout-flex-vs-grid` | `one-dim-vs-two-dim` | The documented decision rule |

Consume them by linking `assets/css/flexbox-patterns.css` once at the app root — it defines the pattern classes that reference `var(--layout-flex-toolbar)`, `var(--layout-flex-media-object)`, and friends. Components never hardcode `gap: 8px` or ad-hoc alignment; they read the token so density modes tighten every toolbar and media object at once.

## 4. Composition

- **Composes with css-grid-patterns:** grid lays the page, flex lays the components inside grid areas — the standard two-layer architecture. A grid area holds one flex toolbar or media object; flex never tries to be the page skeleton.
- **Composes with spacing tokens:** gap values are space tokens; density modes tighten gaps once at the token tier, so every flex pattern in the system reflows together without component edits.
- **Composes with rtl-i18n-layout:** flex follows direction automatically (`row-reverse` not needed) — logical properties keep RTL free, which is why physical `left/right` margins are banned from these patterns.

## 5. Signature Patterns

- **Media-object everywhere:** avatar/icon + text rows (comments, list items, notifications) as one shared pattern class — one CSS block serves every list in the product, differing only in gap and avatar size tokens.
- **Toolbar contract:** action bars use flex-wrap + gap so overflow reflows instead of clipping; overflow rails are a named exception with explicit `overflow-x` and scroll-snap, never a silent `nowrap` clip.

## 6. Real-World Use Cases

- **Component-level layout inside grid areas:** cards, list items, form rows — the flex patterns are what actually render inside each grid cell.
- **App shell header/footer with sticky-footer pattern:** a column flex shell with `margin-top: auto` on the footer keeps short pages pinned without absolute positioning.
- **Horizontal scroll rails for card carousels:** `nowrap` + `overflow-x` + scroll-snap, the one sanctioned exception to the wrap rule.

## 7. Combination Notes

### With other responsive-layout skills

- **Good with css-grid-patterns and layout-compositions:** these three form the two-layer architecture — grid/compositions draw the page, flex fills each area. Neither substitutes for the other; the boundary (`--layout-flex-vs-grid`) is the decision rule both guides reference.
- **Good with breakpoints-strategy, fluid-container-queries, and intrinsic-design:** flex patterns respond to content and container first, so they need few breakpoints — wrap and gap do the responsive work.
- **Good with mobile-navigation, data-tables-responsive, and responsive-images:** nav bars, table toolbars, and image+caption rows are all flex patterns; those guides consume this one's vocabulary rather than re-deriving it.
- **Good with rtl-i18n-layout and responsive-testing:** direction-following flex plus a test matrix that exercises wrap/truncation states keeps the patterns honest in every locale and viewport.
- **No caution or avoid list:** flex is the lowest-level layout layer here and conflicts with nothing above it — misuse shows up as the anti-patterns below, not as skill conflicts.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both styles live on disciplined spacing and alignment — gap-driven toolbars and media objects deliver exactly that with no decorative structure.
- **Caution with collage-art:** collage composition may want overlapping, rotated, absolutely-placed elements that resist flex flow; if a collage genuinely needs freedom positioning, opt out consciously per-instance rather than bending the media-object pattern.

### With motion skills (companion repo skill-animation)

- **Good affinity with scroll-animation:** horizontal flex rails (`--layout-flex-rail`) pair directly with scroll-driven reveals and scroll-snap timelines — the rail is designed as the animation's track.
- **No caution list:** flex layout is animation-neutral; just animate `transform`/`opacity` on items, never `flex-basis` or `gap` (layout thrash), per the animation repo's performance rules.

## 8. Anti-Patterns

- **Flex-as-grid** — nesting three wrapper divs to fake two-dimensional layout that grid expresses in one rule
- **Shrink-less overflow** — flex children without min-width: 0 pushing parents wider than the screen
- **Margin-based spacing** — :last-child margin overrides instead of gap
- **Infinite nowrap** — toolbars that clip actions instead of wrapping

### Accessibility Notes

Flex order is visual order: never use `order` or `row-reverse` to fix the visual sequence at the cost of a DOM/tab-order mismatch (WCAG 2.4.3) — reorder the DOM instead. This matters most in media objects and toolbars where a design tweak (icon on the right, primary action first) is tempting to patch in CSS; the rule is that CSS reordering of interactive elements is a blocker, content reordering must happen in source. The fallback is equally strict: if a flex pattern cannot preserve DOM = visual order, restructure the markup. Wrapping toolbars also need visible focus order that follows the reflowed layout, and truncation (`--layout-flex-truncate`) must expose full text via `title`, `aria-label`, or an expandable state so ellipsis never hides information from screen-reader or keyboard users.

## 9. Code Examples

### Example 1 — Media-object list (the workhorse pattern)

Tokens: `assets/css/flexbox-patterns.css`

```html
<ul class="feed" aria-label="Recent activity">
  <li class="media">
    <img class="media-avatar" src="avatar-1.png" alt="" width="40" height="40">
    <div class="media-body">
      <p class="media-title">Priya Sharma commented on <a href="#">Q3 roadmap</a></p>
      <p class="media-meta">12 minutes ago</p>
    </div>
  </li>
  <li class="media">
    <img class="media-avatar" src="avatar-2.png" alt="" width="40" height="40">
    <div class="media-body">
      <p class="media-title">Deploy #4821 succeeded — a very long build summary line that must truncate, never overflow</p>
      <p class="media-meta">1 hour ago</p>
    </div>
  </li>
</ul>
<style>
  .feed { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: var(--space-4); }
  .media { /* --layout-flex-media-object = gap+align-start */
    display: flex; gap: var(--space-3); align-items: flex-start;
  }
  .media-avatar { border-radius: 50%; flex-shrink: 0; } /* intrinsic size respected */
  .media-body { /* --layout-flex-fill = flex: 1 + min-width: 0 — required for truncation */
    flex: 1; min-width: 0;
  }
  .media-title {
    margin: 0;
    /* --layout-flex-truncate = ellipsis-on-flex-child */
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    font: 600 14px/1.5 system-ui, sans-serif;
  }
  .media-meta { margin: 2px 0 0; color: #555; font: 12px/1.5 system-ui, sans-serif; }
</style>
```

### Example 2 — Wrapping toolbar with truncating fill item

Tokens: `assets/css/flexbox-patterns.css`

```html
<div class="toolbar" role="toolbar" aria-label="Invoice actions">
  <strong class="toolbar-label">Invoices — March export review</strong>
  <div class="toolbar-actions">
    <button class="tb-btn" type="button">Approve</button>
    <button class="tb-btn" type="button">Export CSV</button>
    <button class="tb-btn" type="button">Send reminder</button>
    <button class="tb-btn" type="button">Archive</button>
  </div>
</div>
<style>
  .toolbar {
    /* --layout-flex-toolbar = wrap+gap-2 */
    display: flex; flex-wrap: wrap; gap: var(--space-2);
    align-items: center; /* --layout-flex-nav-pattern adds space-between on nav bars */
    justify-content: space-between;
    padding: var(--space-2) var(--space-4);
    border: 1px solid #ddd; border-radius: 8px;
  }
  .toolbar-label {
    /* fill + shrink so the label truncates instead of forcing the bar wide */
    flex: 1; min-width: 0;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    font: 600 14px/1.4 system-ui, sans-serif;
  }
  .toolbar-actions {
    display: flex; flex-wrap: wrap; gap: var(--space-2);
  }
  .tb-btn {
    padding: 8px 14px; border: 1px solid #ccc; border-radius: 6px;
    background: #fff; font: 500 13px/1 system-ui, sans-serif; cursor: pointer;
  }
  .tb-btn:focus-visible { outline: 2px solid #1d4ed8; outline-offset: 2px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every flex component spacing uses `gap` fed by space tokens — zero `:last-child` margin overrides in the codebase.
- [ ] Toolbar/action bars set `flex-wrap: wrap` per `--layout-flex-toolbar`; `nowrap` appears only inside named rails with `overflow-x` + scroll-snap.
- [ ] Every `flex: 1` item also sets `min-width: 0` per `--layout-flex-fill` — no flex child can push its parent wider than the container.
- [ ] Truncating text pairs ellipsis with an accessible full-text path (`title`, `aria-label`, or expandable state).
- [ ] No `order`, `row-reverse`, or direction hacks on interactive elements — DOM order equals visual and tab order (2.4.3).
- [ ] Page shells use the sticky-footer idiom (`column` + `margin-top: auto`), not absolute positioning.
- [ ] Two-dimensional needs escalate to `css-grid-patterns` per `--layout-flex-vs-grid`; no wrapper-div flex grids exist.
- [ ] Pattern classes consume `var(--layout-flex-...)` tokens from `assets/css/flexbox-patterns.css` — no hardcoded gaps or alignments in components.
