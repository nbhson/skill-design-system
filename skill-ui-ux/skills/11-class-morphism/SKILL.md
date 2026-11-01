---
name: class-morphism
description: Elegant classicism meets morphic depth: golden ratio layouts, warm shadows, glass panels, and refined serif typography.
tags: [luxury, elegant, serif, gold, warm, glass]
related: [aurora-ui, neumorphism, glassmorphism]
---

# UI/UX Skill: Class Morphism

## 1. Definition

Class Morphism (also known as "Classy Morphism" — not a universal industry term; coined by this skill set to describe the luxury classic + morphic hybrid) is a style that combines the elegance of Classicism with the depth principles of Morphism (neumorphism, glassmorphism). This style features: (1) golden ratio, symmetrical balance like classical design; (2) soft shadows and/or backdrop blur like morphic design; (3) warm, contemplative palettes instead of overly vibrant ones; and (4) medium-weight serif typography. Overall, Class Morphism creates a "luxurious, contemplative, with depth" feel — suitable for luxury brands and premium products.

## 2. Core Design Principles

- **Golden ratio / Symmetrical balance:** layouts use 1:1.618 or 3:5 ratios, elements arranged symmetrically or near-symmetrically — different from asymmetrical modern design.
- **Gentle morphic effects:** warm soft shadows (not cold shadows like pure neumorphism) or subtle glass effect — creating depth without being overly "popping."
- **Warm, contemplative palette:** avoid neon colors, overly pale pastels; prioritize blush, deep navy, champagne gold, off-white, dusty rose.
- **Not overly decorative:** take the spirit of classicism but don't use too many ornaments (florals, ripples); use only 1–2 meaningful decorative elements.
- **Generous spacing:** ample white space, comfortable margins — luxury is expressed through spatial abundance.
- **Subtle texture:** may use subtle texture (silk, faint stone grain) for backgrounds, not too obvious.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background | `#F5F0EB` | Warm off-white — creates quality paper feel |
| Glass background | `#FFFFFF` (30–50% opacity) | Transparent panel over background |
| Dominant color | `#1C3A5F` | Deep navy — composed, luxurious |
| Accent | `#C9A96E` | Champagne gold — gentle highlight |
| Soft accent | `#BFA89E` | Dusty rose — naturally warm color |
| Shadow | `#8B7355` (12% opacity) | Warm shadow, not cold gray |
| Primary text | `#1A1A1A` | Soft black |
| Secondary text | `#6B5B4F` | Warm gray-brown |

**Rule:** do not use overly cool colors (#00FFFF, #FF00FF); if cool colors are needed, use only muted forms (blue-gray).

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Display | Playfair Display (or Cormorant Garamond) | H1: 40–56px / 500–600, italic variant |
| Header | Cormorant Garamond | H2: 28–36px / 500 |
| Body | Lora (or Source Serif Pro) | 16–18px / 400, line-height 1.7 |
| Label | Jost (or Montserrat) | 12–13px / 500, letter-spacing 0.08em |

**Rule:** serif dominates; don't overuse sans-serif; may use Jost (light geometric sans) for labels and captions to add a modern accent.

## 5. Signature Visual Elements

- Glass cards: `backdrop-filter: blur(15px)`, background `rgba(255,255,255,0.35)`, border `1px solid rgba(255,255,255,0.5)`.
- Warm shadows: `box-shadow: 0 8px 32px rgba(139,115,85,0.12)` — not cold gray shadows.
- Icons: thin 1px strokes, muted colors, usually outline style.
- Dividers: thin decorative lines, may have a small ornament in the center.
- Subtle patterns: classic motifs (faint damask, thin stripes) as background, very low opacity (5–10%).

## 6. Real-World Use Cases

- **Luxury brand / jewelry:** luxury brand websites, auction houses — class morphism conveys value, elegance, and artistic quality.
- **Premium real estate:** luxury property landing pages, interior design — creates an upscale living space feel.
- **Wedding / event planning:** event websites, wedding pages — warm palette and serif typography fit the refined, romantic theme.
- **Premium editorial:** luxury online magazines, lifestyle blogs — editorial style with depth.

## 7. Combination Notes

- **Combining with Glassmorphism:** most natural pairing — glassmorphism is a form of "morphism" so it blends well with class morphism; use glass panels as main cards and light shadows for decorative elements.
- **Combining with Neumorphism:** can combine if colors are adjusted — ensure shadows become warm and the palette shifts to muted tones.
- **Do not combine with Maximalism/Brutalism:** philosophically opposite; class morphism values elegance and balance while maximalism/brutalism value boldness and breaking conventions.

## 8. Anti-Patterns

- **Ornamental excess:** overusing classical decorations (floral borders, ornate dividers, excessive gold accents) contradicts the understated elegance that defines class morphism—restraint is key.
- **Forced symmetry:** applying symmetrical layouts to inherently asymmetrical content (like social feeds or news streams) creates awkward, unnatural arrangements—symmetry serves composition, not the reverse.
- **Cool-glass-on-warm-classic:** adding glassmorphism panels with cold blue tints over warm champagne and navy backgrounds creates a jarring contrast that undermines the contemplative palette.
- **Modern-bold mixing:** pairing heavy modern sans-serif fonts (Arial Black, Helvetica Bold) with delicate serif typography creates visual discord—class morphism demands refined, medium-weight fonts throughout.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on primary background: `#1A1A1A` on `#F5F0EB` | 15.37:1 | ✅ pass |
| secondary text on primary background: `#6B5B4F` on `#F5F0EB` | 5.73:1 | ✅ pass |

Both text pairs pass AA (15.37:1 and 5.73:1). Champagne gold `#C9A96E` on the off-white background is only ~2.1:1 — it is a **decorative accent only** (dividers, ornaments, borders), never text. Glass panels should keep the warm tint of the palette; avoid cold blue-tinted glass over the warm background, and provide a solid fallback under `prefers-reduced-transparency: reduce`.

## 9. Code Examples

### Example 1 — Luxury hero with warm glass panel

Tokens: `assets/css/class-morphism.css`

```html
<section class="hero">
  <div class="glass">
    <p class="eyebrow">Maison — Est. 1897</p>
    <h1>Quiet Luxury</h1>
    <span class="rule" aria-hidden="true"></span>
    <p class="lede">Crafted slowly, worn for decades.</p>
    <a class="cta" href="/collection">View the collection</a>
  </div>
</section>
<style>
.hero { display: grid; place-items: center; min-height: 520px; padding: 48px;
        background: var(--color-primary-background) url(silk-texture.png); /* #F5F0EB */
        font-family: var(--font-body); color: var(--color-primary-text); } /* #1A1A1A — 15.37:1 */
.glass { max-width: 520px; padding: 48px 56px; text-align: center;
         background: rgba(255, 255, 255, 0.35);        /* warm-tinted glass */
         backdrop-filter: blur(15px);
         border: 1px solid rgba(255, 255, 255, 0.5); border-radius: 4px;
         box-shadow: 0 8px 32px rgba(139, 115, 85, 0.12); } /* warm shadow, not cold gray */
.eyebrow { font-family: var(--font-body); font-size: 13px; letter-spacing: 0.08em;
           text-transform: uppercase; color: var(--color-secondary-text); } /* #6B5B4F — 5.73:1 */
h1 { font-family: var(--font-heading); font-size: 48px; font-weight: 500; font-style: italic; margin: 8px 0 0; }
.rule { display: block; width: 64px; height: 1px; margin: 24px auto;
        background: var(--color-accent); } /* #C9A96E — decoration only */
.cta { display: inline-block; padding: 12px 32px; border: 1px solid var(--color-dominant-color);
       color: var(--color-dominant-color); text-decoration: none; letter-spacing: 0.06em; }
@media (prefers-reduced-transparency: reduce) {
  .glass { background: #FFFFFF; backdrop-filter: none; }
}
</style>
```

### Example 2 — Golden-ratio split

Tokens: `assets/css/class-morphism.css`

```html
<div class="split">
  <img src="product.jpg" alt="Hand-stitched leather bag">
  <div class="copy">
    <h2>Atelier Series</h2>
    <p>One artisan. One piece per week.</p>
  </div>
</div>
<style>
.split { display: grid; grid-template-columns: 1fr 1.618fr; /* golden ratio */
         gap: 32px; align-items: center; font-family: var(--font-body);
         color: var(--color-primary-text); background: var(--color-primary-background); }
h2 { font-family: var(--font-heading); font-weight: 500; font-size: 32px; }
</style>
```

## 10. Implementation Checklist

- [ ] Text pairs pass AA — `#1A1A1A` on `#F5F0EB` (15.37:1), `#6B5B4F` (5.73:1); gold `#C9A96E` (~2.1:1) is decoration only, never text.
- [ ] Layouts follow golden-ratio or symmetric composition (1:1.618 / 3:5).
- [ ] Shadows are warm (`rgba(139,115,85,…)`) and consistent — no cold gray shadows.
- [ ] Serif typography stays at medium weight; no heavy modern sans-serifs.
- [ ] Only 1–2 classical ornaments per viewport; generous white space throughout.
- [ ] Glass panels are warm-tinted and degrade to solid under `prefers-reduced-transparency: reduce`.
- [ ] Focus states are elegant but clearly visible (thin gold-navy outline).
