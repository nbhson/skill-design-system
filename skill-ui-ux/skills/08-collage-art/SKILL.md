---
name: collage-art
description: Layered, mixed-media composite with overlapping images, text, and illustrations at varied scales and blend modes.
tags: [collage, layers, mixed-media, textures, overlapping]
related: [maximalism, brutalism-ui]
---

# UI/UX Skill: Collage Art

## 1. Definition

Collage Art in UI/UX is a style that uses multiple layers of images, text, illustrations, and graphic elements cut, pasted, and overlapping to create a vibrant composite (collage). Unlike purely artistic paper collage (handmade, cut-and-paste), Collage Art in digital UI is adapted for digital interfaces: it must be readable, interactive, and maintain usability. Each layer typically has different opacity, creating a visual "layered" effect.

## 2. Core Design Principles

- **Layering with depth:** 3–5 overlapping layers, each with different opacity (60–90%) and blend modes (multiply, screen, overlay).
- **Varied scales and angles:** images in the collage are often cropped, rotated, scaled non-standardly — creating energy and asymmetry.
- **Diverse fonts in one viewport:** combine 2–3 font families (serif + sans-serif + display) to increase the "cut-and-paste" feel.
- **Background texture:** paper scraps, canvas fabric, film grain — texture creates a tangible material feel.
- **Non-uniform colors:** each layer has its own color palette, creating richness; but there should be one dominant color for coherence.
- **Content remains readable:** despite busyness, main text and CTAs must stand out and be easy to read — use solid backgrounds behind text if needed.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Textured background | `#F5F0E8` | Cream — aged paper |
| Layer 1 | `#C026D3` | Magenta — vivid color layer |
| Layer 2 | `#F59E0B` | Orange — warm layer |
| Layer 3 | `#06B6D4` | Cyan — cool layer |
| Text overlay | `#FFFFFF` | White on dark colors |
| Text on solid | `#1E293B` | Dark blue-gray — text with solid background |

**Rule:** the overall palette should include both warm and cool colors, similar to the color scheme of a fashion magazine.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Display | Playfair Display (classic serif) | 48–80px / 700, may be italic |
| Sub-head | Space Grotesk | 20–28px / 500 |
| Body | DM Sans (or Libre Baskerville) | 14–16px / 400 |
| Accent text | Staatliches (or Bebas Neue) | 24–48px / 400, wide letter-spacing |

**Rule:** combine serif (Playfair) + sans-serif (DM Sans) + display (Staatliches) — not limited to 1 family like other styles.

## 5. Signature Visual Elements

- Non-standard-ratio cropped images.
- Background textures: paper, cardboard, fabric, film grain.
- Shape masks: circles, stars, freeform shapes — not just rectangles.
- Tape/pins/stickers: elements holding layers together (masking tape, pushpins, stickers).
- Partial overlaps: elements overlapping completely or only partially (half-overlap).

## 6. Real-World Use Cases

- **Editorial/Magazine websites:** online magazines, fashion blogs, culture pages — collage fits art-focused content.
- **Art/creative brands:** design studios, artists, content creators — expressing personality and diversity.
- **Campaign/Event landing pages:** event pages, advertising campaigns — attracting attention with rich imagery.

## 7. Combination Notes

- **Combining with Brutalism/Maximalism:** share "multi-layered, non-uniform" characteristics — can use brutalist borders and typography as a "frame" for the collage inside.
- **Combining with Glassmorphism:** place glass panels (a transparent layer) over collage — creates a "glass over a painting" effect, very interesting.
- **Do not combine with Neumorphism/Minimalism:** too contrasting; collage requires visual richness while minimalism/neumorphism require simplicity.

## 8. Anti-Patterns

- **Layers obscuring content:** stacking images and shapes at full opacity without text containers renders labels and CTAs unreadable—accessibility requires that key content remains visible.
- **Random visual assembly:** combining disparate images, fonts, and colors without a unifying theme or dominant color creates noise rather than a cohesive collage.
- **Static composition:** without rotation, scaling, or overlapping elements, the collage reads as a standard grid layout—motion and asymmetry are essential to the style.
- **Uniform palette:** using the same color for all layers eliminates the visual depth that comes from contrasting warm and cool tones against textured backgrounds.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on textured background: `#1E293B` on `#F5F0E8` | 12.9:1 | ✅ pass |
| text overlay on magenta layer: `#FFFFFF` on `#C026D3` | 4.71:1 | ✅ pass |

Both core pairs pass AA, but white on the magenta layer `#C026D3` has almost no headroom (4.71:1) — any texture or image behind it drops it below 4.5:1. Put text on **solid plates** rather than directly over busy layers. Rotation/parallax effects are decorative: wrap any motion in `prefers-reduced-motion: reduce` guards and never animate the text plates themselves.

## 9. Code Examples

### Example 1 — Collage hero with text plate

Tokens: `assets/css/collage-art.css`

```html
<section class="collage">
  <img class="cut" src="photo.jpg" alt="Artist portrait, cropped">
  <div class="tape" aria-hidden="true"></div>
  <div class="plate">
    <h1>Paste &amp; Remix</h1>
    <p>An exhibition of layered identities.</p>
    <a class="cta" href="/tickets">Tickets</a>
  </div>
</section>
<style>
.collage { position: relative; min-height: 420px; padding: 32px;
           background: var(--color-textured-background) url(paper-grain.png); /* #F5F0E8 */
           font-family: var(--font-body); }
.cut { position: absolute; right: 8%; top: 10%; width: 40%;
       transform: rotate(3deg); border: 8px solid #FFFFFF; }
.tape { position: absolute; left: 12%; top: 6%; width: 120px; height: 32px;
        background: rgba(245, 159, 11, 0.75);
        transform: rotate(-6deg); }
.plate { position: relative; max-width: 420px; padding: 24px;
         background: var(--color-text-on-solid); color: #FFFFFF; } /* solid plate keeps 4.5:1+ */
.plate h1 { font-family: var(--font-heading); font-size: 56px; font-weight: 700; margin: 0 0 8px; }
.cta { display: inline-block; margin-top: 16px; padding: 12px 24px;
       background: var(--color-layer-1); color: #FFFFFF; /* #C026D3 — 4.71:1, large/bold text only */
       text-decoration: none; transform: rotate(-1deg); }
@media (prefers-reduced-motion: reduce) {
  .cut, .cta, .tape { transition: none; animation: none; }
}
</style>
```

### Example 2 — Layered sticker composition

Tokens: `assets/css/collage-art.css`

```html
<div class="strip" aria-hidden="true">
  <span class="chip chip--a">MAGENTA</span>
  <span class="chip chip--b">CYAN</span>
  <span class="chip chip--c">AMBER</span>
</div>
<style>
.strip { display: flex; gap: 12px; padding: 16px; background: var(--color-textured-background); }
.chip { padding: 8px 16px; font-family: var(--font-body); font-weight: 700;
        border: 2px solid #1E293B; }
.chip--a { background: var(--color-layer-1); color: #FFFFFF; }  /* #C026D3 */
.chip--b { background: var(--color-layer-2); color: #1E293B; }  /* #F59E0B */
.chip--c { background: var(--color-layer-3); color: #FFFFFF; }  /* #06B6D4 */
.chip--a { transform: rotate(-3deg); } .chip--b { transform: rotate(2deg); }
</style>
```

## 10. Implementation Checklist

- [ ] All key text and CTAs sit on solid plates — 4.5:1 verified against the busiest layer behind them (white on `#C026D3` is 4.71:1 with no headroom).
- [ ] 3–5 overlapping layers with varied opacity (60–90%) and blend modes.
- [ ] One dominant color unifies the palette across layers.
- [ ] Max 2–3 font families per viewport (serif + sans + display).
- [ ] Elements are cropped, rotated, or scaled non-standardly — never a plain grid.
- [ ] Background texture is present (paper/grain) but never behind text plates.
- [ ] Motion (parallax, hover lifts) is decorative and disabled under `prefers-reduced-motion: reduce`.
