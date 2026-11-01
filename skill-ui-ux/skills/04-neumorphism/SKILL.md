---
name: neumorphism
description: Soft, tactile UI where elements appear 'pushed out' or 'pressed in' using symmetrical soft shadows on a unified background.
tags: [soft, tactile, shadows, subtle-depth]
related: [claymorphism, class-morphism, flat-design]
---

# UI/UX Skill: Neumorphism

## 1. Definition

Neumorphism (New + Skeuomorphism) creates an effect of elements "pushed out" or "pressed in" from the surface, mimicking the tactile feel of soft materials (rubber, smooth plastic, silicone) on a flat background. Unlike old skeuomorphism (which simulated real materials like wood, leather), neumorphism relies solely on soft shadows to create depth without complex textures or gradients. The background and elements typically share the same hue, differing only in lightness.

## 2. Core Design Principles

- **Background and elements share the same hue:** background, buttons, and cards all belong to the same color group, differing only in lightness by ±10%.
- **Symmetrical soft shadows:** one light shadow on the top-left corner and one dark shadow on the bottom-right corner, with equal blur and spread. This is the core technique.
- **No clear borders:** no border, no outline — boundaries are created entirely through shadow.
- **Prefers neutral backgrounds:** light gray background (light mode) is the most common environment; dark mode requires shadow inversion (lighter instead of darker).
- **Clear interaction feedback:** when pressed, shadows reverse (shadow becomes inner shadow) creating a "pressed in" feel; hover states need subtle transitions.
- **Consistent border-radius:** rounded corners of 16–24px uniformly across elements, creating a soft, tactile feel.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background (light) | `#E4E9F2` | Warm gray-white — most common background |
| Primary background (dark) | `#2D3748` | Dark gray — for dark mode |
| Element (light) | `#ECF0F3` | 5–8% lighter than background |
| Light shadow | `#FFFFFF` (70% opacity) | Top-left corner |
| Dark shadow | `#A3B1C6` (50% opacity) | Bottom-right corner |
| Accent color | `#6C63FF` | Soft purple — used for icons/active states |
| Primary text | `#4A5568` | Medium-dark gray, not too dark |

**Rule:** accent color is only for icons and active states; interactive elements (buttons, toggles) should maintain the background color.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | Poppins (or Nunito, Quicksand) | H1: 36–48px / 500–600; H2: 24–28px / 500 |
| Body | Poppins | 15–16px / 400, line-height 1.6 |
| UI Label | Poppins | 13–14px / 500 |

Rounded fonts like Poppins, Nunito, and Quicksand are the best fit for the soft, tactile feel of neumorphism.

## 5. Signature Visual Elements

- Soft UI: shadow blur 20–40px, spread 5–15px, no hard edges.
- Inner shadow on press: `inset` shadow instead of `drop` shadow.
- No thin-stroke icons — use solid (filled) icons so they "pop" from the background.
- Sliders, toggles, inputs: "embedded" style (sinking into the surface) instead of "raised."
- Cards may be slightly raised; list items are flat-inset style.

## 6. Real-World Use Cases

- **Fitness / wellness apps:** Apple Fitness+, meditation apps — soft, friendly feel, gentle on the eyes.
- **Personal tools:** smart home remote, IoT control app — the tactile "touchable" feel creates user affinity.
- **Lightweight portfolios:** personal pages, profile apps — creates a refined feel, distinct from flat design.

## 7. Combination Notes

- **Combining with Flat Design:** use flat design for main content (text, images) and neumorphism only for interactive components (buttons, switches, sliders) — clearly separate zones.
- **Combining with Glassmorphism:** limit this combination because both rely on shadows/blur; if necessary, place glass panel at the top layer with neumorphic buttons underneath, ensuring sufficient contrast.
- **Avoid in data-heavy dashboards:** neumorphism is unsuitable for data-dense interfaces because subtle shadows don't provide enough layer differentiation with many components.

## 8. Anti-Patterns

- **Background-element color convergence:** using background and element colors that differ by less than 5% makes interactive elements nearly invisible—legibility must take precedence over subtle aesthetics.
- **Inconsistent shadow values:** applying different blur, spread, or opacity values across buttons and cards breaks the unified soft-material illusion that defines neumorphism.
- **Low-contrast text:** pairing gray-on-gray elements with soft shadows results in text that fails accessibility standards—the neumorphic aesthetic requires deliberate contrast planning.
- **Static interfaces:** neumorphism relies on shadow transitions to communicate pressed/raised states; without clear interaction feedback, the tactile quality that distinguishes this style is lost.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on element background: `#4A5568` on `#ECF0F3` | 6.57:1 | ✅ pass |
| body text on primary background: `#4A5568` on `#E4E9F2` | 6.18:1 | ✅ pass |

Gray-on-gray is the style's inherent accessibility risk: both verified pairs pass (6.57:1 and 6.18:1) but with limited headroom, so never use lighter grays for text and keep text off shadowed edges. Because boundaries are created by shadow alone, shadows **cannot replace a visible focus indicator** — always add a real `:focus-visible` ring on interactive elements. Also respect `prefers-contrast: more` by falling back to a bordered, higher-contrast variant.

## 9. Code Examples

### Example 1 — Neumorphic toggle card with pressed state

Tokens: `assets/css/neumorphism.css`

```html
<div class="panel">
  <p>Ambient mode</p>
  <button class="toggle" role="switch" aria-checked="true"><span class="knob"></span></button>
</div>
<style>
.panel {
  width: 280px; padding: 32px; border-radius: 24px;
  background: var(--color-primary-background-light); /* #E4E9F2 */
  font-family: var(--font-body); color: var(--color-primary-text); /* #4A5568 */
}
/* the core technique: two symmetric soft shadows */
.panel { box-shadow: -8px -8px 16px #FFFFFF, 8px 8px 16px #A3B1C6; }
.toggle {
  width: 64px; height: 32px; border: 0; border-radius: 16px;
  background: var(--color-primary-background-light);
  box-shadow: inset -4px -4px 8px #FFFFFF55, inset 4px 4px 8px #A3B1C650; /* pressed-in track */
}
.knob { display: block; width: 24px; height: 24px; border-radius: 50%;
        background: var(--color-element-light); /* #ECF0F3 */
        box-shadow: -2px -2px 4px #FFFFFF, 2px 2px 4px #A3B1C6;
        transform: translateX(32px); transition: transform 150ms ease; }
.toggle[aria-checked="false"] .knob { transform: translateX(8px); }
.toggle:focus-visible { outline: 2px solid var(--color-accent-color); outline-offset: 4px; }
</style>
```

### Example 2 — Raised tile

Tokens: `assets/css/neumorphism.css`

```html
<div class="tile">72 BPM</div>
<style>
.tile {
  display: grid; place-items: center; width: 96px; height: 96px; border-radius: 50%;
  background: var(--color-element-light); color: var(--color-primary-text);
  font-family: var(--font-body); font-weight: 600;
  box-shadow: -6px -6px 12px #FFFFFF70, 6px 6px 12px #A3B1C660; /* light TL, dark BR */
}
</style>
```

## 10. Implementation Checklist

- [ ] Text uses `#4A5568` (6.57:1 on elements, 6.18:1 on background) — never lighter grays for text.
- [ ] Background, buttons, and cards share one hue family with only ±10% lightness difference.
- [ ] Every raised element uses the same dual-shadow values (same blur, spread, opacity).
- [ ] All interactive elements have a pressed state via inset shadow, plus a `:focus-visible` ring that does not rely on shadow alone.
- [ ] Border-radius 16–24px applied uniformly.
- [ ] Layout on the 8pt grid; sliders/inputs use embedded (inset) styling.
- [ ] Touch targets ≥ 44×44px despite the soft, low-contrast aesthetic.
