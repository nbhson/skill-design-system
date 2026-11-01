---
name: skeuomorphism
description: Real-world material mimicry: leather, wood, metal textures with multi-layer shadows and physical button interactions.
tags: [material, texture, realistic, depth, nostalgic]
related: [retro]
---

# UI/UX Skill: Skeuomorphism

## 1. Definition

Skeuomorphism is a design style that mimics real-world objects in digital interfaces: the interface looks like real materials (leather, wood, metal) or real objects (calculators, notebooks, radios). This was the most popular style from 2007–2012 (Apple iOS before iOS 7, Windows Vista/7, Apple apps before 2013), before being replaced by Flat Design. Today, skeuomorphism is used selectively for contexts that need to create familiarity or a nostalgic feeling.

## 2. Core Design Principles

- **Mimic real materials:** leather (texture), wood (grain), metal (heavy gradient + highlight), paper (soft shadow).
- **Clear depth:** multiple shadow layers creating depth — drop shadow + bottom shadow + top highlight.
- **Bevel and Emboss:** create raised/pressed effects using border gradients (light on top = raised, dark on top = pressed).
- **Repeating textures:** material patterns (leather, linen, wood grain) as background, visible even on areas without content.
- **Physical buttons:** buttons have raised shapes, with clear "pressed-down" states using inner shadow and gradient.
- **Physical interaction feedback:** when pressed, buttons sink; volume sliders have grooves; switches have obvious on/off states.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Brown leather background | `#8B5A2B` | Leather brown |
| Black leather | `#3D3D3D` | Black leather (iPod classic) |
| Light wood | `#C4A574` | Light wood yellow |
| Silver metal | `#C0C0C0` → `#E8E8E8` | Metal gradient |
| Gold metal | `#D4AF37` → `#FFD700` | Brass/gold |
| Highlight | `#FFFFFF` (30% opacity) | Light on the surface |
| Dark shadow | `#000000` (30–50% opacity) | Drop shadow |

**Rule:** texture is the dominant element; color is secondary in skeuomorphism because material already provides color.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | Georgia (or Palatino, Rockwell) | H1: 32–48px / 700, bold serif |
| Body | Trebuchet MS (or Verdana) | 15–17px / 400, readable |
| Digital display | Digital-7 Mono (or LCD mono) | 24–48px — for LED/digital screens |

Serif fonts (Georgia, Palatino) or "soft" sans-serif (Trebuchet) fit the realistic material feel better than modern pure fonts.

## 5. Signature Visual Elements

- Background textures: leather, linen, wood, metal — used as background for the entire interface or for specific panels.
- Bevel border: 1px gradient border with light on top and dark on bottom to create a raised effect.
- Multi-layer drop shadow: outer shadow + inner shadow combined.
- Complex gradients: instead of flat colors, use multi-stop gradients to simulate light on a 3D surface.
- 3D icons: icons with depth, shadow, and highlight — not 2D glyphs.

## 6. Real-World Use Cases

- **Music/audio apps:** music players, guitar tuners, DJ apps — mimicking audio equipment (equalizers, cassette players, turntables) creates familiarity.
- **Game UI / Immersive apps:** mobile games, simulator apps (flight simulators, racing dashboards) — skeuomorphism creates a "touchable" feel.
- **Nostalgic/retro products:** notebook-style note apps, virtual garden apps — creates emotional connection.

## 7. Combination Notes

- **Combining with Retro:** very natural — many retro products can combine skeuomorphism to enhance the nostalgic feel.
- **Combining with Flat Design:** can use skeuomorphism for elements needing emphasis (key features) and flat for the rest — called "flat skeuomorphism hybrid" (e.g., iOS Calculator).
- **Do not combine with Neumorphism/Glassmorphism/Aurora UI:** both use shadows but with completely different principles; mixing them creates chaotic, inconsistent depth.

## 8. Anti-Patterns

- **Texture everything:** covering every surface with leather, wood, and metal textures overwhelms the interface and makes it feel cluttered rather than tactile—the "real material" should be applied selectively.
- **Mismatched metaphors:** applying skeuomorphic styling to contexts where the physical metaphor doesn't fit (e.g., a banking app designed as a leather notebook) creates confusion rather than familiarity.
- **Texture over readability:** heavy material patterns behind text or icons diminish legibility—the real-world metaphor should enhance, not obstruct, usability.
- **Stuck in 2010:** continuing to use heavy skeuomorphism (deep gradients, prominent bevels) when modern design has moved toward subtlety makes the interface appear dated rather than nostalgic.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on brown leather background: `#FFFFFF` on `#8B5A2B` | 5.84:1 | ✅ pass |
| text on black leather: `#FFFFFF` on `#3D3D3D` | 10.86:1 | ✅ pass |

White text on the brown leather passes AA (5.84:1) but only has ~1.3 headroom — keep leather backgrounds darkened and untextured behind copy. Dark text on leather fails hard (`#3D3D3D` on `#8B5A2B` is 1.86:1): engraved/dark text is decoration only. LCD-style displays should use near-black numerals on a pale green/gray LCD for maximum legibility.

## 9. Code Examples

### Example 1 — Skeuomorphic music player panel

Tokens: `assets/css/skeuomorphism.css`

```html
<section class="music-player">
  <div class="lcd">02:47</div>
  <div class="controls">
    <button class="btn" aria-label="Previous">&#9664;</button>
    <button class="btn btn--main" aria-label="Play">&#9654;</button>
    <button class="btn" aria-label="Next">&#9654;</button>
  </div>
</section>
<style>
.music-player {
  width: 320px; padding: 24px; border-radius: 16px; text-align: center;
  background: var(--color-brown-leather-background) url(leather.png); /* #8B5A2B */
  font-family: var(--font-body); color: #FFFFFF;  /* 5.84:1 on leather */
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.30),  /* top highlight = raised */
              0 6px 12px rgba(0,0,0,0.40);           /* drop shadow */
}
.lcd { font-family: "Digital-7 Mono", monospace; font-size: 40px;
       background: #1A1A1A; color: #9EFF9E; padding: 8px 16px; border-radius: 8px;
       box-shadow: inset 0 2px 8px rgba(0,0,0,0.8); margin-bottom: 16px; }
.btn { width: 56px; height: 40px; border: 0; cursor: pointer;
       background: linear-gradient(180deg, var(--color-silver-metal), #E8E8E8); /* metal bevel */
       border-radius: 6px;
       box-shadow: inset 0 2px 0 #FFFFFFCC, inset 0 -3px 6px rgba(0,0,0,0.35), 0 2px 4px rgba(0,0,0,0.5); }
.btn:active { box-shadow: inset 0 3px 6px rgba(0,0,0,0.45); } /* pressed-in */
.btn:focus-visible { outline: 2px solid #FFFFFF; outline-offset: 3px; }
</style>
```

### Example 2 — Bevelled knob

Tokens: `assets/css/skeuomorphism.css`

```html
<button class="knob" aria-label="Volume"></button>
<style>
.knob { width: 72px; height: 72px; border-radius: 50%;
        background: radial-gradient(circle at 35% 30%, #E8E8E8, var(--color-silver-metal) 70%);
        box-shadow: inset 0 2px 2px rgba(255,255,255,0.9), inset 0 -4px 8px rgba(0,0,0,0.35),
                    0 4px 8px rgba(0,0,0,0.4); }
</style>
```

## 10. Implementation Checklist

- [ ] Text on leather is white or near-white (5.84:1 on `#8B5A2B`); dark text on leather (`#3D3D3D` on `#8B5A2B`, 1.86:1) is decoration only.
- [ ] Material textures are used selectively — never behind body text without a solid/darkened plate.
- [ ] Bevels read correctly: light on top = raised, dark on top = pressed.
- [ ] Every physical control has an obvious pressed state (inner shadow + gradient flip).
- [ ] Multi-layer shadows (drop + inner + top highlight) use consistent values across components.
- [ ] Serif or soft sans-serif type (`Georgia`, `Trebuchet MS`) at ≥ 15px over busy textures.
- [ ] Focus states are explicit — engraved/tactile looks must not swallow the focus ring.
