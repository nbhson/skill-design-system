---
name: aurora-ui
description: Living, animated light layers mimicking the aurora borealis - multi-layer gradients, bokeh, shimmer, and glass panels.
tags: [aurora, gradients, animated, glass, bokeh, light]
related: [claymorphism, class-morphism, flat-design, glassmorphism]
---

# UI/UX Skill: Aurora UI

## 1. Definition

Aurora UI is a style that uses dynamic, soft light like the aurora borealis — multi-layered gradients overlapping, seamlessly transitioning colors, often combined with shimmer effects, high blur, and smooth motion. This style is closely associated with Apple (macOS Sonoma, iOS 17 animated wallpapers, visionOS) and high-end tech brands wanting to convey a futuristic, magical, and living feel. The core element is "light that feels real" — gradients are not flat, they have depth and motion.

## 2. Core Design Principles

- **Multi-layer gradients:** at least 2–3 overlapping gradients at different angles, creating a "light layer" with depth.
- **High blur (Bokeh effect):** bright areas are often heavily blurred (40–80px) to create "light orb" effects similar to photography.
- **Smooth motion:** gradients/light move slowly (8–20s cycle), using CSS animation or Lottie; transitions are subtle, not attention-grabbing.
- **Natural yet vibrant colors:** blues, purples, pinks, greens — colors reminiscent of real aurora.
- **Avoid hard contrast:** no thick black lines, no heavy dark text on aurora backgrounds — use white text with soft shadow instead.
- **Backdrop blur for content:** when placing content over aurora, use `backdrop-filter: blur()` or glass panels.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Background layer 1 | `#0F0C29` | Deep purple-black — creates depth |
| Background layer 2 | `#302B63` | Dark purple |
| Light layer 1 | `#6366F1` | Indigo — central light area |
| Light layer 2 | `#06B6D4` | Cyan — cool light area |
| Light layer 3 | `#A855F7` | Purple-pink — warm alternating area |
| Accent | `#22D3EE` | Bright cyan — icons, highlights |
| Text | `#FFFFFF` (90% opacity) | Soft white, light shadow |

**Note:** gradients typically combine radial + linear, not linear alone.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Display | SF Pro Display (or Geist, Inter) | 48–72px / 600–700, soft text-shadow |
| Header | SF Pro Display | 28–36px / 600 |
| Body | SF Pro Text (or Inter) | 15–17px / 400–500, 85–90% opacity |
| Label | SF Pro Text | 12–14px / 500, letter-spacing 0.05em |

Use sharp, non-serif fonts (Apple/tech style) to contrast with the soft light behind — creating a visual anchor point.

## 5. Signature Visual Elements

- **Animated background:** slow-moving gradients, infinite loop.
- **Light orbs:** blurred circles floating on the background.
- **Glass cards:** transparent frosted panels (`backdrop-filter: blur(20px)`, `background: rgba(255,255,255,0.1)`) placed over aurora.
- **Shimmer effect:** a light streak running across a surface to simulate "real light."
- **Icons:** white thin strokes or filled white — never dark colors on aurora backgrounds.

## 6. Real-World Use Cases

- **Operating systems & devices:** macOS Sonoma, iOS 17+, visionOS, Android 12+ dynamic color — aurora is a platform-level trend.
- **Streaming / gaming apps:** Spotify (new version), Discord (dark mode), Epic Games launcher — creates a living space for younger users.
- **Premium Web3/AI/Fintech brands:** landing pages for high-end tech products wanting to convey innovation and the future.

## 7. Combination Notes

- **Combining with Glassmorphism:** most natural pairing — glass cards floating over aurora create the "light passing through glass" effect, visually stunning.
- **Combining with Flat Design:** can use flat elements (text, monochrome icons) over aurora — this is the most common combination (e.g., macOS widgets).
- **Limitations:** do not place detailed photographs or live video directly over aurora due to visual conflict; use a glass overlay as an intermediary.

## 8. Anti-Patterns

- **Jarring or distracting motion:** fast, abrupt gradient animations defeat the ethereal quality of aurora—the gentle, slow movement is what makes the effect feel magical.
- **Sharp photographs on soft gradients:** placing detailed images or videos directly over aurora backgrounds creates visual conflict; always use a glass intermediary layer.
- **Dark text on bright aurora:** dark text on vibrant gradient backgrounds is difficult to read—white text with soft shadow is non-negotiable for accessibility.
- **Over-blurring:** applying excessive bokeh blur (80px+) everywhere creates an unfocused, inaccessible interface; blur should enhance depth, not obscure content.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on darkest background layer: `#FFFFFF` on `#0F0C29` | 19.01:1 | ✅ pass |
| body text on mid background layer: `#FFFFFF` on `#302B63` | 12.72:1 | ✅ pass |

White text passes AA on both dark background layers (19.01:1 and 12.72:1). Text over the bright light layers (`#6366F1`, `#06B6D4`, `#A855F7`) is **not verified and must be avoided** — keep text on the darkest zones or on a glass panel. Aurora is animated by definition: wrap all motion in `@keyframes` and disable it under `prefers-reduced-motion: reduce` with a static gradient fallback. Glass panels on aurora should also degrade under `prefers-reduced-transparency: reduce`.

## 9. Code Examples

### Example 1 — Animated aurora background + content panel

Tokens: `assets/css/aurora-ui.css`

```html
<section class="aurora">
  <div class="orb orb--1" aria-hidden="true"></div>
  <div class="orb orb--2" aria-hidden="true"></div>
  <div class="panel">
    <h1>Light that feels alive</h1>
    <p>Slow gradients, deep blur, white type.</p>
  </div>
</section>
<style>
.aurora { position: relative; min-height: 480px; overflow: hidden;
          background: linear-gradient(160deg, var(--color-background-layer-1), var(--color-background-layer-2)); /* #0F0C29 → #302B63 */
          font-family: var(--font-body); display: grid; place-items: center; }
.orb { position: absolute; border-radius: 50%; filter: blur(64px); opacity: 0.6; }
.orb--1 { width: 420px; height: 420px; background: var(--color-light-layer-1); /* #6366F1 */
          animation: drift 18s ease-in-out infinite alternate; }
.orb--2 { width: 320px; height: 320px; background: var(--color-light-layer-2); /* #06B6D4 */
          animation: drift 14s 2s ease-in-out infinite alternate-reverse; }
@keyframes drift { from { transform: translate(-8%, -6%); } to { transform: translate(10%, 8%); } }
.panel { position: relative; padding: 32px 40px; border-radius: 20px;
         background: rgba(255,255,255,0.10); backdrop-filter: blur(20px);
         color: var(--color-text); text-align: center; } /* #FFFFFF — 12.7–19:1 on dark layers */
.panel h1 { font-family: var(--font-heading); font-size: 48px; font-weight: 600;
            text-shadow: 0 2px 12px rgba(0,0,0,0.35); margin: 0 0 8px; }
@media (prefers-reduced-motion: reduce) {
  .orb { animation: none; } /* static gradient, no drift */
}
@media (prefers-reduced-transparency: reduce) {
  .panel { background: rgba(15, 12, 41, 0.92); backdrop-filter: none; }
}
</style>
```

### Example 2 — Light-orb accent

Tokens: `assets/css/aurora-ui.css`

```html
<div class="glow" aria-hidden="true"></div>
<style>
.glow { width: 240px; height: 240px; border-radius: 50%;
        background: radial-gradient(circle, var(--color-accent) 0%, transparent 70%); /* #22D3EE */
        filter: blur(48px); }
</style>
```

## 10. Implementation Checklist

- [ ] Text sits only on the darkest background layers or glass panels — 19.01:1 / 12.72:1 verified; never over bright light layers.
- [ ] Gradient/light motion runs 8–20s per cycle and stops under `prefers-reduced-motion: reduce`.
- [ ] Content placed over aurora uses a glass intermediary (`backdrop-filter: blur(10–30px)`).
- [ ] No thick black lines or dark text anywhere on aurora backgrounds.
- [ ] Bokeh blur ≤ 80px and limited to decorative layers, never content.
- [ ] Icons are white (stroke or filled); never dark icons on aurora.
- [ ] Focus states remain visible on glass panels over moving light.
