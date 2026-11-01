---
name: icon-grid-sizing
description: The construction grid: 24px base, 16/20/24/32 scale, padding budgets, keyline shapes, and pixel-snapping for crisp strokes.
tags: [icons, grid, sizing, keylines, pixel-snapping]
related: [icon-style-selection, icon-library-management, icon-usability]
---

# Visual Asset Guide: Icon Grid & Sizing

## 1. Definition

Every icon family is built on a construction grid: a 24px base with keyline shapes (circle, square, portrait, landscape), a padding budget (~2px at 24), and a size ramp (16/20/24/32/48) that maps to UI slots. This guide covers grid setup, keyline shapes that keep optical balance, pixel-snapping so strokes stay crisp at 1x, and how a single 24px master scales (or is redrawn) for smaller sizes. The grid is invisible in the shipped product but decisive in it: two glyphs drawn on different grids never quite align, and users read that misalignment as unpolished without being able to name why.

## 2. Core Principles

- **One grid, one family:** all icons share the 24px base grid — alignment across icons is what makes a toolbar read as a set.
- **Keyline shapes enforce optical balance:** circle, square, portrait, landscape zones — glyphs touching keylines read consistent.
- **Padding budget is sacred:** ~2px padding at 24px (8% of canvas) — glyphs touching the edge look caged; too much padding looks weak.
- **The size ramp maps to slots:** 16 (inline text), 20 (dense UI), 24 (default), 32/48 (empty/feature) — sizes are chosen per slot, not ad hoc.
- **Pixel-snap strokes:** strokes land on half-pixel boundaries at shipping sizes — un-snapped strokes blur at 1x displays.
- **Small sizes get redrawn, not squeezed:** 16px icons are simplified masters (fewer details), not scaled-down 24px files.
- **Corner radius inside icons scales with size:** inner radii are proportional to the grid, keeping family feel across the ramp.
- **The grid is exported with the family:** grid templates and keyline files ship with the icon library for contributors.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Base grid | `--icon-base-grid` | `24px` | The master construction size |
| Size ramp | `--icon-size-ramp` | `16,20,24,32,48` | Mapped to UI slots |
| Padding budget | `--icon-padding-budget` | `2px-at-24 (8%)` | Glyphs never touch canvas edge |
| Keyline shapes | `--icon-keyline-shapes` | `circle,square,portrait,landscape` | Optical balance zones |
| Pixel snap | `--icon-pixel-snap` | `half-pixel-strokes` | Crisp at 1x displays |
| Small-size policy | `--icon-small-size-policy` | `redrawn-at-16` | Simplified masters, not scaled |
| Inner radius | `--icon-inner-radius` | `proportional-to-grid` | Family feel across sizes |
| Grid export | `--icon-grid-export` | `template-shipped` | Contributors build on the grid |
| Alignment rule | `--icon-alignment-rule` | `cross-icon-consistency` | Toolbar reads as one set |
| Export sizes | `--icon-export-sizes` | `per-slot-only` | No ad-hoc export sizes |

Consume these by linking `assets/css/icon-grid-sizing.css` once at the app root, then referencing `var(--icon-...)` from icon components — `--icon-base-grid` and the `--icon-size-ramp` steps drive `width`/`height` in generated components, so a component API accepts only ramp values and rejects anything else. The contract tokens (`--icon-keyline-shapes`, `--icon-pixel-snap`) are enforced at authoring time by the keyline overlay and export tooling.

## 4. Composition

- **Composes with icon-style-selection (guide 01):** stroke weight and grid are one system — decisions co-lock. A 2px stroke is only predictable on a 24px grid with half-pixel snapping; choosing stroke and grid together is what keeps the family coherent at every size.
- **Composes with skill-design-tokens spacing/radius scales:** icon sizes and inner radii align with the spacing ramp — 16/20/24 slots sit inside 4/8-based spacing, and inner radii reuse the radius scale so icons and containers share a corner personality.
- **Composes with icon-library-management (guide 03):** the grid is enforced at library contribution time — the contribution gate refuses glyphs that violate keylines, so grid discipline survives contributors.

## 5. Signature Patterns

- **The master-icon workflow:** every icon drawn once at 24px on the grid, then simplified masters for 16/20 — a one-way pipeline, not per-size drawing. Details are removed as size decreases (the 16px master drops interior strokes the 24px master keeps), which is why 16px stays legible instead of turning to mush.
- **The keyline check:** new icons are overlaid on keyline shapes; glyphs violating zones are resized optically before merge. A circle touches the circle keyline, a square the square keyline — equal areas read equal, and no glyph looks bloated or starved inside the set.

## 6. Real-World Use Cases

- **Icon library construction from zero** — establishing the 24px base, keyline file, and ramp before the first contributor submits.
- **Migrating an ad-hoc icon set to a grid-based system** — re-basing existing glyphs onto keylines in priority order (navigation first).
- **Audit: caged glyphs, blurry 1x strokes, inconsistent optical sizing** — measuring a shipped set against the padding budget and pixel-snap rules.

## 7. Combination Notes

### With other icons-illustration skills

- **Pairs naturally with icon-style-selection (guide 01) and icon-library-management (guide 03):** style and grid co-lock, and the library's gate enforces keyline compliance at merge — the grid survives only when the pipeline checks it.
- **Pairs with icon-usability, accessible-icons, and svg-optimization:** grid padding keeps touch targets predictable, optical balance keeps 3:1 contrast feasible at small sizes, and snapped geometry survives optimization without shifting.
- **Pairs with icon-system-audit, empty-error-illustrations, animation-integration, favicon-app-icons, illustration-direction, and mascot-character:** audits detect caged glyphs and blur; larger slots (empty states, feature icons, favicons) consume 32/48 ramp steps under the same grid contract.
- **No caution list:** the grid is infrastructure — every glyph-producing skill benefits from it, and none requires deviating from it.
- **No avoid list:** grid violations are a review failure, never a skill conflict.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles favor simple geometry on strict structure — a disciplined keyline grid is their natural icon foundation, and their spacing/radius scales map cleanly onto icon padding and inner radii.
- **No caution list:** expressive styles change what glyphs look like, not the grid they are drawn on; even maximalist detail is budgeted inside the same 24px base and padding rules.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing and micro-interactions:** grid-snapped glyphs animate predictably — morph transitions between icons interpolate cleanly when both endpoints share the grid, and micro-feedback (press scale, swap) respects the same half-pixel boundaries so animations never blur strokes.

## 8. Anti-Patterns

- **Edge-caged glyphs** — artwork touching the canvas edge with no padding
- **Scaled-down 16px mush** — details vanishing because nobody redrew the small master
- **Blurry strokes** — un-snapped geometry shimmering on 1x screens
- **Per-size ad-hoc drawing** — 16 and 24 versions drawn independently, drifting apart

### Accessibility Notes

Grid discipline serves WCAG 1.4.11 and 2.5.8: optically balanced glyphs at target sizes keep 3:1 contrast feasible, and consistent padding keeps touch-target sizing predictable — the grid is the a11y foundation of the family. A glyph that fills its canvas leaves no room for the surrounding hit area and forces down-stream components to fake spacing; a snapped stroke that blurs on 1x displays erodes contrast for low-vision users in exactly the sizes they rely on most. The fallback: if redrawn small masters are too costly, restrict small slots to the subset of icons that survive scaling — complexity migrates to larger slots rather than degrading recognition at 16px.

## 9. Code Examples

### Example 1 — 24px grid and keyline visualizer (dashed keyline shapes + glyph)

```html
<figure class="keyline-demo">
  <svg viewBox="0 0 24 24" role="img" aria-label="24px grid with keyline shapes and a home glyph">
    <rect x="0" y="0" width="24" height="24" fill="none" stroke="#D4D4D4" stroke-width="0.25"/>
    <rect x="2" y="2" width="20" height="20" fill="none" stroke="#93C5FD" stroke-width="0.5" stroke-dasharray="1.5 1.5"/>
    <circle cx="12" cy="12" r="10" fill="none" stroke="#93C5FD" stroke-width="0.5" stroke-dasharray="1.5 1.5"/>
    <rect x="4" y="2" width="16" height="20" fill="none" stroke="#FCA5A5" stroke-width="0.5" stroke-dasharray="1.5 1.5"/>
    <rect x="2" y="4" width="20" height="16" fill="none" stroke="#FCA5A5" stroke-width="0.5" stroke-dasharray="1.5 1.5"/>
    <path d="M12 4.5 19.5 10v9.5h-5.5v-5h-4v5H4.5V10Z" fill="none" stroke="#404040" stroke-width="2" stroke-linejoin="round"/>
  </svg>
  <figcaption>Home glyph on the 24px grid: circle/square (blue) and portrait/landscape (red) keylines, 2px padding.</figcaption>
</figure>
<style>
  :root {
    /* Mirror of assets/css/icon-grid-sizing.css */
    --icon-base-grid: 24px;
    --icon-padding-budget: 2px;   /* 8% of the 24px canvas */
  }
  .keyline-demo { width: var(--icon-base-grid); height: var(--icon-base-grid); margin: 0; padding: 24px; border: 1px solid #e5e5e5; border-radius: 10px; width: max-content; font: 12px/1.4 Inter, system-ui, sans-serif; }
  .keyline-demo svg { width: calc(var(--icon-base-grid) * 8); height: calc(var(--icon-base-grid) * 8); display: block; image-rendering: pixelated; }
  figcaption { max-width: 240px; color: #737373; }
</style>
```

### Example 2 — Size ramp: 16/20/24/32/48 of the same glyph

```html
<div class="ramp" role="img" aria-label="Star glyph at 16, 20, 24, 32 and 48 pixels">
  <svg class="step s16" viewBox="0 0 24 24"><path d="M12 3.5 14.7 9l6 .7-4.5 4.1 1.2 5.9L12 16.8 6.6 19.7l1.2-5.9L3.3 9.7l6-.7Z"/></svg>
  <svg class="step s20" viewBox="0 0 24 24"><path d="M12 3.5 14.7 9l6 .7-4.5 4.1 1.2 5.9L12 16.8 6.6 19.7l1.2-5.9L3.3 9.7l6-.7Z"/></svg>
  <svg class="step s24" viewBox="0 0 24 24"><path d="M12 3.5 14.7 9l6 .7-4.5 4.1 1.2 5.9L12 16.8 6.6 19.7l1.2-5.9L3.3 9.7l6-.7Z"/></svg>
  <svg class="step s32" viewBox="0 0 24 24"><path d="M12 3.5 14.7 9l6 .7-4.5 4.1 1.2 5.9L12 16.8 6.6 19.7l1.2-5.9L3.3 9.7l6-.7Z"/></svg>
  <svg class="step s48" viewBox="0 0 24 24"><path d="M12 3.5 14.7 9l6 .7-4.5 4.1 1.2 5.9L12 16.8 6.6 19.7l1.2-5.9L3.3 9.7l6-.7Z"/></svg>
</div>
<style>
  :root {
    /* Mirror of assets/css/icon-grid-sizing.css */
    --icon-size-ramp: 16, 20, 24, 32, 48;
    --icon-inner-radius: proportional-to-grid;
  }
  .ramp { display: flex; align-items: flex-end; gap: 20px; padding: 20px 24px; border: 1px solid #e5e5e5; border-radius: 10px; width: max-content; }
  .step { fill: #2563EB; stroke: none; stroke-linejoin: round; display: block; }
  .s16 { width: 16px; height: 16px; }  /* inline text slots */
  .s20 { width: 20px; height: 20px; }  /* dense UI */
  .s24 { width: 24px; height: 24px; }  /* default */
  .s32 { width: 32px; height: 32px; }  /* empty-state slots */
  .s48 { width: 48px; height: 48px; }  /* feature slots */
</style>
```

## 10. Implementation Checklist

- [ ] Every glyph is drawn on the shared 24px base grid (`--icon-base-grid`); no icon ships off-grid.
- [ ] New icons pass the keyline check — circle, square, portrait, landscape zones (`--icon-keyline-shapes`) overlaid before merge.
- [ ] The ~2px padding budget at 24px (`--icon-padding-budget`) holds: no glyph touches the canvas edge.
- [ ] UI components accept only ramp sizes (16/20/24/32/48) via `var(--icon-...)`; ad-hoc export sizes are rejected.
- [ ] Strokes are pixel-snapped to half-pixel boundaries (`--icon-pixel-snap`) and verified crisp at 1x displays.
- [ ] 16px slots use simplified, redrawn masters (`--icon-small-size-policy`) — never scaled-down 24px files.
- [ ] Inner radii scale proportionally with size, aligned to the design-token radius scale.
- [ ] Grid templates and keyline files ship with the library (`--icon-grid-export`) so contributors build on the grid.
