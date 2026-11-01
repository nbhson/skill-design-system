---
name: maximalism
description: 'More is more': controlled visual energy built from vibrant colors, patterns, layered imagery, and bold typography.
tags: [bold, vibrant, patterns, layers, expressive]
related: [brutalism-ui, collage-art]
---

# UI/UX Skill: Maximalism

## 1. Definition

Maximalism is the antithesis of minimalism: "More is more" — flooding space with vibrant colors, patterns, textures, bold typography, and layered imagery stacked on top of each other. The goal is not chaos but controlled visual energy, telling the brand story through visual richness. The boundaries between elements are often deliberately broken.

## 2. Core Design Principles

- **Full but ordered:** despite dense content, a visual axis is needed to guide the eye (a large title, a dominant color) giving the eye an anchor point.
- **Clear layering:** stack 2–3 layers (background pattern → content block → decorative details) with sufficient contrast between layers.
- **Large palette but dominant:** 5–7 vibrant colors, with one color occupying ~40–50% of the area to prevent color chaos.
- **Bold typography with control:** 2–3 font families maximum, using very large sizes for headers as "anchors" amid the visual density.
- **Visual rhythm:** alternate dense zones with brief breathing zones so the eye doesn't tire.
- **Every element serves the story:** patterns, stickers, textures are all related to the brand/content — no random decoration.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Dominant color | `#7C3AED` | Vivid purple — large backgrounds, titles |
| Secondary background | `#FDE047` | Lemon yellow — large accent blocks |
| Hot accent | `#FF3EA5` | Neon pink — CTAs, badges |
| Cool accent | `#22D3EE` | Cyan — links, hover states |
| Text contrast | `#1A1024` | Deep purple-black — text on light backgrounds |
| Soft background | `#FFF1F2` | Light pink — long content areas |

**Rule:** use maximum 3 "hot" colors in the same viewport; remaining colors serve as background/support.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Display | Clash Display (or Archivo Black, Space Grotesk Bold) | 64–96px / 700, may be uppercase |
| Sub-head | Space Grotesk | 24–32px / 600 |
| Body | Inter | 16–18px / 400–500, line-height 1.5 |
| Label/decoration | DM Mono (or Anybody) | 12–14px / 500, wide letter-spacing |

Permitted for headers: rotated text (±5°), outlined text (text-stroke), multicolor text (gradient text).

## 5. Signature Visual Elements

- Repeating patterns (checkered, zigzag, decorative motifs), stickers, round badge-style stickers.
- Multiple geometric chart types: circles + stars + zigzags in the same area.
- Bold, multi-color gradients (not the soft, faint aurora style).
- Thick borders 2–4px in black/vivid color, hard offset shadows (`4px 4px 0 #000`).
- Cut-and-paste images, mixed-media, hand-drawn illustrations mixed with photographs.

## 6. Real-World Use Cases

- **Entertainment / music / streaming:** artist pages, events, festivals — high energy, creates a "party" feel.
- **Fashion / streetwear / NFT:** brands with strong personality, youth-oriented, wanting to stand out from minimalist competitors.
- **Creative agencies / marketing campaigns:** campaign landing pages needing to make an impression in the first 3 seconds.

## 7. Combination Notes

- **Combining with Brutalism:** the two naturally resonate (both are bold, raw, large) — use brutalism as the structural backbone (layout/borders) and maximalism as the decorative layer, but commit to a shared grid system.
- **Do not directly combine with Minimalism/Neumorphism:** these are diametrically opposite; if mixing is needed, apply maximalism to the campaign page and minimalism to the app/dashboard section separately.

## 8. Anti-Patterns

- **Visual noise without anchor:** layering vibrant colors, patterns, and typography without a dominant focal point creates chaos instead of energy—the eye needs somewhere to rest.
- **No breathing room:** packing every pixel with content exhausts users; even in maximalism, visual rhythm requires zones of lower density.
- **Random decoration:** using patterns, stickers, or textures that have no relation to the brand message undermines the intentionality that makes maximalism compelling.
- **Everything competing for attention:** when every element is bold, colorful, and large, nothing stands out—the principle of "dominant color" (occupying 40-50% of area) is often ignored.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on soft background: `#1A1024` on `#FFF1F2` | 16.72:1 | ✅ pass |
| accent text on soft background: `#7C3AED` on `#FFF1F2` | 5.19:1 | ✅ pass |

The verified pairs use the deep purple-black text on the light soft background (16.72:1 and 5.19:1). Neon pink `#FF3EA5` and cyan `#22D3EE` fail contrast on light backgrounds — they are **decoration only**, never body text (black on cyan reaches 11.62:1 if you need text on a cyan block). Keep body copy on the dominant or soft backgrounds and reserve gradients/patterns for non-text zones.

## 9. Code Examples

### Example 1 — Event hero — dominant color + hard shadows

Tokens: `assets/css/maximalism.css`

```html
<section class="poster">
  <div class="sticker">NEW DROP</div>
  <h1>NOISE<br>FESTIVAL</h1>
  <p>Three days. Twelve stages. Zero restraint.</p>
  <a class="cta" href="/tickets">Get tickets</a>
</section>
<style>
.poster {
  position: relative; max-width: 720px; padding: 64px 48px;
  background: var(--color-dominant-color);        /* #7C3AED ≈ 45% of viewport */
  color: var(--color-text-contrast);              /* #1A1024 */
  font-family: var(--font-body);
  border: 3px solid #000; box-shadow: 8px 8px 0 #000; /* hard offset shadow */
}
.poster h1 { font-family: var(--font-heading); font-size: 88px; font-weight: 700;
             line-height: 0.95; text-transform: uppercase; margin: 0 0 24px; }
.sticker { display: inline-block; background: var(--color-secondary-background); /* #FDE047 */
           padding: 8px 16px; transform: rotate(-4deg);
           border: 2px solid #000; font-family: var(--font-body); font-weight: 500; }
.cta { display: inline-block; background: var(--color-hot-accent); /* #FF3EA5 */
       color: #1A1024; padding: 12px 24px; font-weight: 700;
       border: 3px solid #000; box-shadow: 4px 4px 0 #000; text-decoration: none; }
</style>
```

### Example 2 — Pattern block with breathing zone

Tokens: `assets/css/maximalism.css`

```html
<div class="poster-block">
  <h2>Visual rhythm</h2>
  <p>Alternate dense zones with brief low-density zones so the eye can rest.</p>
</div>
<style>
.poster-block { background: var(--color-soft-background); /* #FFF1F2 */
          color: var(--color-text-contrast); padding: 32px;
          font-family: var(--font-body); }
h2 { font-family: var(--font-heading); font-size: 32px; font-weight: 600; }
</style>
```

## 10. Implementation Checklist

- [ ] Dominant color occupies 40–50% of the area so the eye always has an anchor.
- [ ] Palette capped at 5–7 colors and 2–3 font families.
- [ ] Body text uses verified pairs only — `#1A1024` on `#FFF1F2` (16.72:1); neon pink/cyan are decoration, never text.
- [ ] Dense zones alternate with breathing zones at least once per viewport.
- [ ] Every pattern/sticker/texture relates to the brand or message — no random decoration.
- [ ] Interactive elements keep a visible focus state even under patterns and layers.
- [ ] Headline hierarchy survives: one largest anchor element per viewport.
