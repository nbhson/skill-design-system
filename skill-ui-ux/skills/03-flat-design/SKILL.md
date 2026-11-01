---
name: flat-design
description: Purely two-dimensional UI with solid colors, simple shapes, and clear boundaries - no 3D effects, born as a reaction to skeuomorphism.
tags: [flat, 2d, solid-colors, geometric]
related: [minimalism, neumorphism]
---

# UI/UX Skill: Flat Design

## 1. Definition

Flat Design is a purely two-dimensional (2D) style that eliminates all three-dimensional effects such as heavy gradients, shadows, textures, and bevels. Interface elements are represented with solid colors, simple geometric shapes, and clear boundaries. This style originated as a reaction to skeuomorphism of iOS 6 and became widely popular after Microsoft adopted it for Windows 8 (Metro UI) and Apple for iOS 7.

## 2. Core Design Principles

- **No heavy gradients, no 3D shadows:** use only solid colors or very subtle gradients (transition ≤15% lightness).
- **Basic geometric shapes:** rectangles, circles, triangles; consistent border-radius (usually 4–12px).
- **High color contrast:** choose background and text with contrast ratio ≥ 4.5:1; use complementary/triadic colors to distinguish groups.
- **Clear typography:** medium-to-bold weight, large enough size to compensate for the lack of depth-creating shadows.
- **Glyph/solid icons:** filled or thin-stroke icons, all with solid flat color — no gradients.
- **Grid-based layout:** align to an 8pt or 4pt grid, with consistent spacing throughout.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background | `#F8FAFC` | Cool light gray |
| Block background | `#3B82F6` | Blue — most common in flat design |
| Accent 1 | `#10B981` | Green — success, secondary CTA |
| Accent 2 | `#F59E0B` | Amber — warning |
| Danger | `#EF4444` | Red — error |
| Primary text | `#1E293B` | Dark gray, avoid absolute black |
| Secondary text | `#64748B` | Medium gray |

**Color selection rule:** use "safe" flat design colors (Flat UI v2 palette: Mint, Emerald, Peter River, Sun Flower, Belize Hole…).

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | Nunito Sans (or Open Sans, Source Sans Pro) | H1: 32–48px / 700; H2: 24–32px / 600 |
| Body | Open Sans (or Roboto) | 15–17px / 400, line-height 1.5 |
| UI Label | Open Sans / Nunito Sans | 13–14px / 600, uppercase for status labels |

A single font family (e.g., Open Sans) for both headers and body maintains overall flat consistency.

## 5. Signature Visual Elements

- Flat buttons: solid background, thin or no border, uniform border-radius.
- Cards: no shadows (or only a 1px stroke), 8px border-radius.
- Images: standard photographs (no filters) or flat vector illustrations.
- Icons: single-color glyphs, 20–24px size, 1.5–2px stroke for line icons.

## 6. Real-World Use Cases

- **Cross-platform mobile apps:** Uber, Spotify (core UI), utility apps — flat design loads fast and enables quick visual recognition.
- **Dashboard / Analytics:** flat-color charts, clean tables — data stands out without "noise" from decoration.
- **Corporate websites:** landing pages, product introductions — delivers messages directly and professionally.

## 7. Combination Notes

- **Combining with Neumorphism:** strong contrast; if needed, use flat design for the main background and neumorphism only for interactive components, ensuring contrast between the two styles in the same view doesn't exceed aesthetic thresholds.
- **Combining with Flat 2.0 / Semi-flat:** add a layer of micro-shadows (elevation 1–2px) or extremely subtle gradients for a touch of depth while maintaining the flat essence — known as "flat design 2.0".

## 8. Anti-Patterns

- **Confusing interactive states:** removing all shadows makes it difficult for users to distinguish buttons from cards or identify clickable elements—some form of visual feedback is essential.
- **Low contrast combinations:** pairing colors with insufficient contrast (e.g., light gray text on white) violates flat design's core emphasis on clarity and legibility.
- **Insufficient typography weight:** using thin, light fonts at small sizes leaves text unreadable because the lack of shadow-based depth was not compensated for through type treatment.
- **Over-flattening everything:** applying flat styling uniformly to all contexts, including complex charts or data visualizations, loses the nuance needed for information hierarchy.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on primary background: `#1E293B` on `#F8FAFC` | 13.98:1 | ✅ pass |
| secondary text on primary background: `#64748B` on `#F8FAFC` | 4.55:1 | ✅ pass |

Both core pairs pass AA. The secondary gray `#64748B` sits at only 4.55:1 — use it at 15px or larger; for small labels darken to `#475569` (7.24:1). White text on the blue block `#3B82F6` is the standard CTA pairing — keep block colors out of body-text roles. Because flat UI has no shadows, hover/pressed/focus states must be communicated with color or border changes alone.

## 9. Code Examples

### Example 1 — Flat stat card + primary button

Tokens: `assets/css/flat-design.css`

```html
<div class="card">
  <div class="icon" aria-hidden="true">▲</div>
  <h3>Uptime</h3>
  <p class="value">99.98%</p>
  <button class="btn">View report</button>
</div>
<style>
.card {
  width: 240px; padding: 24px; border-radius: 8px; /* uniform radius */
  background: var(--color-primary-background);     /* #F8FAFC */
  font-family: var(--font-body); color: var(--color-primary-text); /* #1E293B */
  border: 1px solid #E2E8F0;
}
.icon { width: 40px; height: 24px; background: var(--color-block-background); /* #3B82F6 */
        clip-path: polygon(0 100%, 25% 40%, 55% 75%, 100% 0); }
.btn { margin-top: 16px; padding: 8px 16px; border: 0; border-radius: 8px;
       background: var(--color-block-background); color: #FFFFFF;
       font-family: var(--font-body); font-weight: 600; }
.btn:hover { background: #2563EB; }
.btn:focus-visible { outline: 3px solid var(--color-danger); outline-offset: 2px; }
</style>
```

### Example 2 — Flat status label

Tokens: `assets/css/flat-design.css`

```html
<span class="tag tag--ok">Operational</span>
<style>
.tag { font-family: var(--font-body); font-size: 13px; font-weight: 600;
       text-transform: uppercase; letter-spacing: 0.04em;
       padding: 4px 8px; border-radius: 4px; }
.tag--ok { background: var(--color-accent-1); color: #FFFFFF; } /* #10B981 */
</style>
```

## 10. Implementation Checklist

- [ ] Body text ≥ 4.5:1 — `#1E293B` on `#F8FAFC` (13.98:1); use `#64748B` (4.55:1) only at ≥ 15px, or darken to `#475569` (7.24:1) for small labels.
- [ ] Only solid colors; any gradient shifts ≤ 15% lightness.
- [ ] No more than 5 palette colors per screen (background, block, 2 accents, danger).
- [ ] All layout aligned to an 8pt (or 4pt) grid with consistent spacing.
- [ ] Border-radius 4–12px, uniform across buttons, cards, and inputs.
- [ ] Hover / pressed / focus states communicated by color or border — never by shadow alone.
- [ ] Icons are single-color glyphs at 20–24px with 1.5–2px strokes.
