---
name: icon-style-selection
description: Choosing the icon language: filled vs outline, stroke weight, corner radius, and the one-style rule across a product.
tags: [icons, style, filled-outline, stroke-weight, design-systems]
related: [icon-grid-sizing, icon-library-management, icon-usability]
---

# Visual Asset Guide: Icon Style Selection

## 1. Definition

Icons are a visual language, and mixing dialects is the most common icon failure. This guide covers the style decision matrix: filled vs outline (and when each reads better), stroke weight consistency (1.5px/2px families), corner treatment (rounded vs sharp matching the product's radius scale), optical vs pixel grids, and the duotone/two-tone option — all governed by the one-style rule: a product ships one icon family, chosen deliberately and documented. Style is not an aesthetic mood board; it is a family contract. Once stroke, corner, fill, and grid are locked, every new icon inherits them, so the 50th glyph looks like a sibling of the first rather than a stranger from another system.

## 2. Core Principles

- **One style per product:** filled and outline icons never mix in the same navigation level — consistency is the readability of icons.
- **Filled vs outline is a hierarchy signal:** filled = active/selected; outline = inactive — the weight difference must survive at 16px.
- **Stroke weight is a family commitment:** 1.5px and 2px families exist — pick one; mixing stroke weights looks like a rendering bug.
- **Corner treatment matches the radius scale:** icons inherit the product's radius personality (rounded product, rounded icons).
- **Optical sizing beats mathematical sizing:** circles and squares optically adjusted (± 2%) so equal-sized shapes read equal.
- **The style decision is documented:** an icon spec sheet records stroke, corner, fill, and grid — so the 50th icon matches the first.
- **Density context decides detail:** toolbars at 16-20px carry simple glyphs; illustration-adjacent slots at 40px+ can carry more detail.
- **Test at target sizes:** an icon style chosen at 48px must be re-reviewed at 16px — detail that reads at large sizes turns to mud.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Style family | `--icon-style-family` | `one-per-product` | No mixing in the same nav level |
| Filled/outline rule | `--icon-filled-outline-rule` | `filled=active,outline=inactive` | Weight difference survives 16px |
| Stroke weight | `--icon-stroke-weight` | `2px-default` | 1.5px allowed as documented alternate |
| Corner treatment | `--icon-corner-treatment` | `matches-radius-scale` | Icons inherit product personality |
| Optical adjustment | `--icon-optical-adjustment` | `plus-minus-2%` | Circles/squares optically balanced |
| Style spec sheet | `--icon-style-spec-sheet` | `stroke+corner+fill+grid` | Documented for the 50th icon |
| Size range | `--icon-size-range` | `16-24px-ui` | Detail budget tied to target size |
| Duotone policy | `--icon-duotone-policy` | `documented-or-banned` | Two-tone needs explicit rules |
| Density context | `--icon-density-context` | `detail-scales-with-size` | Toolbars simple; large slots richer |
| Style review size | `--icon-style-review-size` | `16px-gate` | Re-review at smallest target |

Consume these by linking `assets/css/icon-style-selection.css` once at the app root, then referencing `var(--icon-...)` from icon components and review tooling — the executable tokens (`--icon-stroke-weight`, `--icon-optical-adjustment`) style SVG geometry directly, while the contract tokens (`--icon-style-family`, `--icon-filled-outline-rule`) drive linters and the 16px review gate. Components never hardcode a stroke width or fill hex.

## 4. Composition

- **Composes with icon-grid-sizing (guide 02):** style decisions land on the grid — stroke weight and grid are one system. A 2px stroke at 24px assumes 24px keyline geometry; choosing them together avoids re-drawing the family when the other decision changes.
- **Composes with skill-design-tokens:** icon color and stroke consume semantic/alias tokens, never raw hex — so dark mode and brand theming re-color the whole family by re-pointing tokens, not by editing artwork.
- **Composes with skill-ui-ux styles:** icon personality should match the design style — a neumorphic or rounded product does not ship sharp-cornered industrial glyphs. The styleAffinity table records the lean per style.

## 5. Signature Patterns

- **The icon spec sheet:** one document recording family (filled/outline), stroke, corner, grid, and optical rules — the contract every new icon cites. Reviewers diff new glyphs against the sheet, not against their memory of the last icon, which is how the 50th icon stays a sibling of the first.
- **The 16px gate:** every new icon is reviewed at its smallest shipping size before merge — style choices that fail small are rejected. Detail budget is allocated per shipping size, so toolbar glyphs stay simple regardless of how pretty they look at 48px in the design file.

## 6. Real-World Use Cases

- **Design systems choosing their first icon family** — locking stroke, corner, and fill rules before the first fifty icons exist, not after.
- **Products with mixed icon styles (acquisitions, legacy) planning unification** — the decision matrix supplies the target family and the migration order.
- **Audit: stroke-weight drift, filled/outline chaos, mud-at-16px glyphs** — measuring an existing set against its own spec sheet (or discovering it never had one).

## 7. Combination Notes

### With other icons-illustration skills

- **Pairs naturally with icon-grid-sizing (guide 02) and icon-library-management (guide 03):** stroke and grid co-lock as one system, and the library's contribution gate enforces the spec sheet on every merge — style without a pipeline decays within a quarter.
- **Pairs with icon-usability, accessible-icons, and svg-optimization:** the 16px gate feeds recognition testing, the filled variant doubles as a contrast fallback under WCAG 1.4.11, and the locked stroke geometry survives SVGO cleanly.
- **Pairs with icon-system-audit, empty-error-illustrations, animation-integration, favicon-app-icons, illustration-direction, and mascot-character:** audits measure style drift; state and app-icon sets are drawn under the same family contract.
- **Caution with illustration-direction and mascot-character:** they are good partners overall, but illustration languages invite detail, texture, and tone that bleed into icon style — keep the glyph family deliberately simpler than the artwork, and do not let a mascot's expressive line weight become the icon stroke.
- **No avoid list:** as the family contract, this skill conflicts with nothing — only with the absence of a decision.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles read as clean geometry with restrained detail — exactly what a single-stroke or single-fill family produces, and their radius personalities map directly onto icon corner treatment.
- **Caution with maximalism:** maximalist surfaces want expressive density, which tempts teams toward duotone, heavy fills, or per-context glyph variants; if a maximalist product needs richer glyphs, extend the family through the documented duotone policy — never by improvising a second style inline.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions and easing-timing:** filled/outline state changes animate cleanly (cross-fade or morph) when the geometry is one family, and hover/press feedback on icons should reuse the shared duration and easing tokens rather than ad-hoc springs.

## 8. Anti-Patterns

- **Style salad** — filled and outline icons side by side in one toolbar
- **Stroke drift** — 1.5px legacy icons beside 2px new ones
- **Mud at 16px** — detailed illustrations compressed into navigation glyphs
- **Undocumented style** — no spec sheet, so every new icon guesses

### Accessibility Notes

Icon style must survive WCAG 1.4.11 (non-text contrast: 3:1 for meaningful graphics) at the smallest size — thin 1px strokes at low contrast fail, and a style that only passes on the design file's white artboard will fail on tinted surfaces. Paired with the accessible-names contract (the a11y repo's media-alt-text guide), the style decision is also a recognition decision: a filled active state must remain distinguishable from an outline inactive state for low-vision users, not just by color but by the weight difference itself. The fallback is explicit: if a chosen style fails contrast at small sizes, thicken strokes or add a filled variant for active states — the style serves recognition, not fashion.

## 9. Code Examples

### Example 1 — Toolbar enforcing the one-family rule (filled = active, outline = inactive)

```html
<nav class="toolbar" aria-label="Document tools">
  <button class="tool is-active" aria-pressed="true" aria-label="Home">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 21 10v11h-7v-6h-4v6H3V10Z"/></svg>
  </button>
  <button class="tool" aria-pressed="false" aria-label="Search">
    <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" aria-hidden="true">
      <circle cx="11" cy="11" r="6"/><path d="m20 20-4.5-4.5"/>
    </svg>
  </button>
  <button class="tool" aria-pressed="false" aria-label="Profile">
    <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" aria-hidden="true">
      <circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>
    </svg>
  </button>
</nav>
<style>
  :root {
    /* Mirror of assets/css/icon-style-selection.css */
    --icon-stroke-weight: 2px;        /* 2px-default family */
    --icon-stroke-color: #404040;     /* from design-tokens alias tier */
    --icon-fill-color: #2563EB;       /* filled = active */
    --icon-size-ui: 20px;             /* within the 16-24px-ui range */
  }
  .toolbar { display: flex; gap: 4px; padding: 8px; border: 1px solid #e5e5e5; border-radius: 10px; width: max-content; font: 14px/1 Inter, system-ui, sans-serif; }
  .tool { width: 40px; height: 40px; display: grid; place-items: center; border: 0; background: transparent; border-radius: 8px; cursor: pointer; }
  .tool svg { width: var(--icon-size-ui); height: var(--icon-size-ui); stroke: var(--icon-stroke-color); }
  .tool.is-active svg { fill: var(--icon-fill-color); stroke: var(--icon-fill-color); }
  .tool.is-active { background: #EFF6FF; }
  .tool:focus-visible { outline: 2px solid var(--icon-fill-color); outline-offset: 2px; }
</style>
```

### Example 2 — Filled vs outline pair comparison (weight difference must survive 16px)

```html
<div class="compare">
  <figure class="cell">
    <svg class="glyph" viewBox="0 0 24 24" aria-label="Home, active (filled)"><path d="M12 3 21 10v11h-7v-6h-4v6H3V10Z"/></svg>
    <figcaption>filled · active</figcaption>
  </figure>
  <figure class="cell">
    <svg class="glyph glyph-outline" viewBox="0 0 24 24" fill="none" aria-label="Home, inactive (outline)">
      <path d="M12 3 21 10v11h-7v-6h-4v6H3V10Z" stroke-width="2" stroke-linejoin="round"/>
    </svg>
    <figcaption>outline · inactive</figcaption>
  </figure>
</div>
<style>
  :root {
    /* Mirror of assets/css/icon-style-selection.css */
    --icon-stroke-weight: 2px;
    --icon-stroke-color: #404040;
    --icon-fill-color: #2563EB;
    --icon-optical-adjustment: 2%;    /* circles/squares balanced optically */
  }
  .compare { display: flex; gap: 24px; padding: 16px; border: 1px solid #e5e5e5; border-radius: 10px; width: max-content; font: 12px/1.4 Inter, system-ui, sans-serif; }
  .cell { display: grid; justify-items: center; gap: 8px; margin: 0; }
  .glyph { width: 32px; height: 32px; fill: var(--icon-fill-color); stroke: var(--icon-fill-color); }
  .glyph-outline { fill: none; stroke: var(--icon-stroke-color); }
  figcaption { color: #737373; }
</style>
```

## 10. Implementation Checklist

- [ ] One icon family is documented in a spec sheet (`--icon-style-spec-sheet`: stroke + corner + fill + grid) and cited in every icon review.
- [ ] Filled and outline never mix within one navigation level; `--icon-filled-outline-rule` (filled=active, outline=inactive) is enforced in code and design files.
- [ ] Every glyph uses the family stroke from `var(--icon-stroke-weight)` — no per-icon stroke overrides.
- [ ] Icon corner treatment matches the product radius scale; no glyph invents its own radius personality.
- [ ] Circles and squares carry the documented optical adjustment (`plus-minus-2%`) so equal shapes read equal.
- [ ] Every new icon passes the 16px gate (`--icon-style-review-size`) at its smallest shipping size before merge.
- [ ] Duotone/two-tone usage is either documented under `--icon-duotone-policy` or banned — no improvised two-tone glyphs.
- [ ] Icon color comes from design-token aliases via `var(--icon-...)`; meaningful glyphs keep 3:1 contrast at target sizes (WCAG 1.4.11).
