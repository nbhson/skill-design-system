---
name: retro
description: Era-inspired aesthetics from the 1950s through 1990s - distinct palettes, typography, and graphic motifs for each decade.
tags: [retro, nostalgic, era-specific, synthwave, vintage]
related: [brutalism-ui, skeuomorphism]
---

# UI/UX Skill: Retro

## 1. Definition

Retro in UI/UX is a style inspired by past decades — typically the 1950s (Americana/diner), 1960s (psychedelic), 1970s (disco/bohemian), 1980s (synthwave/neon), or 1990s (early web/Y2K). Unlike skeuomorphism which mimics materials, Retro focuses on the aesthetic of an era: color palettes, typography, graphic motifs, and the overall feel of a time period. This is a style with strong storytelling — each decade has its own narrative.

## 2. Core Design Principles

- **Clearly identify the decade:** each era has distinct palettes, fonts, and motifs; do not mix multiple decades in one viewport (unless intentionally collaging).
- **Era-specific palettes:**
  - 1950s: pastels + cherry red/neon orange
  - 1970s: terra cotta, brown, mustard, olive green
  - 1980s: neon purple, cyan, electric pink, black
  - 1990s: neutral blues, gray, deep purple, white
- **Period-appropriate typography:** use vintage fonts from each era (see Typography section).
- **Period-specific graphic motifs:** scanline, halftone dot, sunburst, chevron pattern, multi-directional typography.
- **Analog textures:** film grain, scan lines, dithering — evoking analog media.

## 3. Suggested Color Palette (by decade)

**Synthwave / 80s:**
| Role | Hex Code |
|---|---|
| Dark background | `#0D0221` |
| Neon purple | `#FF00FF` |
| Neon pink | `#FF6EC7` |
| Neon cyan | `#00FFFF` |
| Hot yellow | `#FFE900` |

**Y2K / 90s:**
| Role | Hex Code |
|---|---|
| White background | `#F0F0F0` |
| Windows teal | `#008080` |
| Deep purple | `#663399` |
| Silver desktop | `#C0C0C0` |
| Navy | `#000080` |

**Diner / 50s:**
| Role | Hex Code |
|---|---|
| Cherry red | `#FF2D2D` |
| Mint green | `#98FF98` |
| Cream yellow | `#F7E7CE` |
| Bubblegum pink | `#FFB6C1` |
| Milk white | `#FFFDD0` |

## 4. Typography

| Decade | Display Font | Body Font |
|---|---|---|
| 1950s | Lobster / Pacifico | Open Sans / Lato |
| 1970s | Righteous / Satisfy | Roboto Slab / Merriweather |
| 1980s | Press Start 2P / Orbitron | VT323 / Share Tech Mono |
| 1990s | Eurostile / Arial Black | Verdana / Trebuchet MS |

8-bit/pixel fonts (Press Start 2P) for display + screen fonts (VT323) for body is the most common retro 80s pairing.

## 5. Signature Visual Elements

- **Scanline:** thin horizontal lines overlaid on images, creating a CRT monitor effect.
- **Halftone:** small dots arranged in patterns, creating a classic print effect.
- **Sunburst:** rays bursting from a center point, popular in 50s-60s design.
- **Neon glow:** glow effects around text/icons for 80s synthwave.
- **Grunge texture:** dirty, worn textures on surfaces — popular in 90s retro.

## 6. Real-World Use Cases

- **Retro/indie games:** pixel art games, arcade games — retro UI enhances immersion.
- **Vintage-inspired fashion brands:** online stores with retro inspiration — creates a period atmosphere.
- **Music/entertainment:** album covers, synthwave/indie artist websites — retro is the natural style of the genre.
- **Nostalgia campaigns:** brands wanting to connect with memories, "golden era" nostalgia.

## 7. Combination Notes

- **Combining with Brutalism:** share "raw, imperfect" characteristics — brutalism provides layout framework and retro provides palette + typography; this combination is powerful for campaign landing pages.
- **Combining with Skeuomorphism:** especially for 80s-90s retro, skeuomorphism (game consoles, CRT TVs) enhances authenticity.
- **Do not combine with Minimalism:** diametrically opposed; retro requires visual richness while minimalism demands simplicity. If needed, use retro for campaign pages and minimalism for product/app sections separately.

## 8. Anti-Patterns

- **Mixing eras:** combining 1950s diners, 1980s neon, and 1990s Y2K aesthetics in one viewport creates temporal confusion—the chosen decade should be clear and consistent.
- **Style over usability:** using tiny pixel fonts, excessive scanlines, or low-contrast retro colors that impair readability sacrifices function for form.
- **Surface nostalgia:** merely applying scanlines and halftones without understanding the genuine spirit of the era produces inauthentic, superficial retro that feels like costume rather than design.
- **Uniform treatment:** applying retro styling to every element equally (header, body, buttons, inputs) flattens the hierarchy—retro treatment should emphasize focal points while modern principles guide functional elements.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| synthwave body text on dark background: `#FFFFFF` on `#0D0221` | 20.04:1 | ✅ pass |
| Y2K text on deep purple: `#FFFFFF` on `#663399` | 8.41:1 | ✅ pass |

Dark-era pairs pass AA (20.04:1 synthwave, 8.41:1 Y2K). The 50s diner palette is the risk zone: cherry red `#FF2D2D` on cream `#F7E7CE` is only 3.05:1 — reserve it for large display text, or darken to `#B91C1C` (5.32:1, passes AA) for body-size text. Scanline/marquee/blink effects must stop under `prefers-reduced-motion: reduce`, and pixel fonts should never go below 16px (small pixel fonts fail legibility as well as contrast).

## 9. Code Examples

### Example 1 — 80s synthwave card

Tokens: `assets/css/retro.css`

```html
<section class="synth scanlines">
  <h1 class="neon">NIGHT DRIVE</h1>
  <p>Insert cassette. Press play.</p>
  <button class="btn">PLAY</button>
</section>
<style>
.synth { max-width: 480px; padding: 48px 32px; text-align: center;
         background: var(--color-synthwave-dark-background); /* #0D0221 */
         font-family: var(--font-body); color: var(--color-synthwave-neon-pink); /* #FF6EC7 */
         border: 2px solid var(--color-synthwave-neon-purple); }
.neon { font-family: var(--font-heading); font-size: 56px; font-weight: 700;
        color: var(--color-synthwave-neon-cyan); /* #00FFFF on #0D0221 — high contrast */
        text-shadow: 0 0 8px var(--color-synthwave-neon-cyan),
                     0 0 24px var(--color-synthwave-neon-purple); }
.btn { margin-top: 16px; padding: 12px 32px; font-family: var(--font-heading);
       background: var(--color-synthwave-neon-purple); color: #FFFFFF;
       border: 2px solid var(--color-synthwave-hot-yellow); }
.scanlines { position: relative; }
.scanlines::after { content: ""; position: absolute; inset: 0; pointer-events: none;
        background: repeating-linear-gradient(0deg, rgba(0,0,0,0.25) 0 1px, transparent 1px 3px); }
@media (prefers-reduced-motion: reduce) { .synth { animation: none; } }
</style>
```

### Example 2 — 50s diner badge

Tokens: `assets/css/retro.css`

```html
<div class="diner">OPEN 24H</div>
<style>
.diner { display: inline-block; padding: 12px 24px; border-radius: 999px;
         background: var(--color-50s-milk-white);  /* #FFFDD0 */
         color: #B91C1C;                            /* darkened cherry — 5.3:1 on cream */
         font-family: var(--font-heading); font-weight: 700;
         border: 3px solid #B91C1C; }
</style>
```

## 10. Implementation Checklist

- [ ] One decade per viewport — palettes, fonts, and motifs never mix eras.
- [ ] Body text ≥ 4.5:1: synthwave white on `#0D0221` (20.04:1) ✓; 50s cherry on cream (3.05:1) is large-display only — darken to `#B91C1C` (5.32:1) for body text.
- [ ] Pixel fonts used at ≥ 16px; monospace body 14–18px.
- [ ] Scanline / marquee / glow-pulse effects stop under `prefers-reduced-motion: reduce`.
- [ ] Era motifs (scanlines, halftone, sunburst) stay subtle enough to leave UI readable.
- [ ] Neon glow uses shadow only around text/icons, never replacing color contrast.
- [ ] Functional (non-decorative) controls use modern, predictable interaction patterns.
