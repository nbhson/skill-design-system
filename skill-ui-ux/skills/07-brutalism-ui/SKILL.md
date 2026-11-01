---
name: brutalism-ui
description: Raw, unpolished anti-design with system fonts, thick black borders, basic colors, and intentional visual disorder.
tags: [raw, bold, anti-design, borders, system-fonts]
related: [maximalism, retro]
---

# UI/UX Skill: Brutalism UI

## 1. Definition

Brutalism UI in web/digital design is a "raw, bare, unpolished" style — inspired by architectural brutalism (exposing raw concrete), but applied to digital interfaces. Elements are presented in their raw form: system fonts, basic background colors, gridless or very rough layouts, obvious hover states, and content displayed almost without processing. The goal is to break aesthetic conventions to create attention, uniqueness, and deliberate anti-design.

## 2. Core Design Principles

- **System or "raw" fonts:** use Arial, Courier New, Times New Roman, or dedicated brutalist fonts like Archivo Black, Monoton — not professionally designed "beautiful" fonts.
- **Unsophisticated basic colors:** bright yellow, light red, lime green, candy pink — usually unnatural colors, CSS color keywords like `yellow`, `red`, `blue`.
- **Intentional disorderly layout:** may use skewed arrangement, slight overlaps, imperfectly aligned elements; but there's a hidden visual logic.
- **Thick black borders:** 2–4px borders surrounding most blocks; this is the strongest identifier.
- **Obvious hover states:** background color change, color inversion, or white/black text highlighting.
- **No soft shadows:** if shadows exist, they are hard shadows (`4px 4px 0 #000`) or no shadows at all.
- **"Raw" navigation:** can be text link lists, DOS-style buttons, or the simplest possible menu.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background | `#FFFEF0` | Off-white — "paper" feel |
| Accent 1 | `#FFE600` | Bright yellow — large block backgrounds |
| Accent 2 | `#FF5C00` | Orange-red — CTAs |
| Accent 3 | `#FF00FF` | Bright magenta — hover states |
| Text | `#000000` | Absolute black |
| Accent | `#00FF00` | Terminal green — for highlights |

**Rule:** no gray colors — either #000 or #FFF. Color combinations must have high contrast, never use muted intermediate colors.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Display | Archivo Black (or Impact, Arial Black) | 48–120px / 900, uppercase |
| Body | Courier New (or Space Mono, Roboto Mono) | 16–18px / 400–700 |
| UI Label | Arial (or Helvetica) | 14–16px / 700 |

Monospace fonts (Courier New, Space Mono) are the most popular choice in brutalism UI because they create a "raw, unpolished" feel.

## 5. Signature Visual Elements

- 2–4px black borders around almost everything.
- Hard shadow: `box-shadow: 4px 4px 0px #000;`.
- "Raw" checkbox/button: browser-native interface, unstyled.
- Imperfect grid: blocks slightly misaligned, creating a "rushed" or "deliberately wrong" feel.
- Thick underlines for links: 3px underline, no hover underline.
- Marquee text, scrolling text, simple text animations.

## 6. Real-World Use Cases

- **Creative agency portfolios:** Balenciaga, Bloomberg (old version), design studios wanting to be completely different.
- **Tech startups / developer tooling:** developer tools (pages like old figma.com, glitch.me) — brutalism conveys "we don't care about appearance, function is what matters."
- **Rebellious brands / digital art:** streetwear brands, digital artists, NFTs — expressing strong personality.

## 7. Combination Notes

- **Combining with Maximalism:** most natural combination — both oppose design conventions, brutalism provides the structural backbone (layout/borders) and maximalism provides the flesh (graphics/patterns), but commit to a shared grid system.
- **Combining with Retro:** shares common DNA (system fonts, bold borders) — brutalism can be seen as "retro but modernized."
- **Do not combine with Neumorphism/Claymorphism/Aurora UI:** diametrically opposite in every element; the combination will produce an "indecisive mix."

## 8. Anti-Patterns

- **Confusing intentionality with negligence:** truly disordered layouts (randomly rotated everything, completely broken grids) may read as amateur mistakes rather than deliberate anti-design—some hidden logic must remain.
- **Usability sacrificed for shock value:** using tiny click targets, illegible type, or poor contrast under the guise of brutalism damages user experience without artistic justification.
- **Half-hearted boldness:** mixing bold brutalist elements with polished, refined ones creates indecision rather than tension—a committed brutalist approach is more effective.
- **Random interactivity:** adding marquees or scroll effects without purpose feels gimmicky; every "raw" element should have intentional function alongside its aesthetic.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on primary background: `#000000` on `#FFFEF0` | 20.69:1 | ✅ pass |
| body text on yellow accent block: `#000000` on `#FFE600` | 16.57:1 | ✅ pass |

Black text on the off-white and yellow blocks is extremely safe (20.69:1 and 16.57:1). The failure mode is white text on the orange `#FF5C00` (3.1:1) or magenta `#FF00FF` — invert to black text or reserve those accents for decoration. Marquees and scroll effects must stop under `prefers-reduced-motion: reduce`, and 'raw' styling never excuses missing focus indicators: keep the browser-default focus ring or a chunky custom one.

## 9. Code Examples

### Example 1 — Brutalist heading + raw nav

Tokens: `assets/css/brutalism-ui.css`

```html
<header class="raw">
  <h1>DESIGN
    IS BROKEN*</h1>
  <p>*on purpose</p>
  <nav aria-label="Main">
    <a href="#work">WORK</a>
    <a href="#about">ABOUT</a>
    <a href="#contact">CONTACT</a>
  </nav>
</header>
<style>
header { padding: 24px; background: var(--color-primary-background); /* #FFFEF0 */
         color: var(--color-text); font-family: "Courier New", monospace; }
h1 { font-family: var(--font-heading); font-size: clamp(48px, 12vw, 120px);
     font-weight: 900; text-transform: uppercase; line-height: 0.9; margin: 0; }
nav { display: flex; gap: 16px; margin-top: 24px; }
nav a { color: var(--color-text); font-weight: 700; text-decoration: none;
        border: 3px solid #000; padding: 8px 16px;
        box-shadow: 4px 4px 0 #000; background: var(--color-accent-1); } /* #FFE600 */
nav a:hover { background: var(--color-text); color: var(--color-primary-background); }
nav a:focus-visible { outline: 4px solid var(--color-accent-2); outline-offset: 2px; }
</style>
```

### Example 2 — Hard-shadow card

Tokens: `assets/css/brutalism-ui.css`

```html
<article class="card">
  <h2>Post 001</h2>
  <p>Raw content, thick borders, no apologies.</p>
  <a class="more" href="#001">READ →</a>
</article>
<style>
.card { max-width: 360px; padding: 24px; background: var(--color-accent-1); /* #FFE600 */
        border: 4px solid #000; box-shadow: 8px 8px 0 #000;
        font-family: var(--font-body); color: var(--color-text); }
h2 { font-family: var(--font-heading); font-size: 40px; margin: 0 0 8px; text-transform: uppercase; }
.more { text-decoration: underline 3px; font-weight: 700; color: var(--color-text); }
</style>
```

## 10. Implementation Checklist

- [ ] Black text on bright blocks (`#000` on `#FFFEF0` 20.69:1, on `#FFE600` 16.57:1); never white text on `#FF5C00`/`#FF00FF` (3.1:1) for body copy.
- [ ] 2–4px black borders on all major blocks.
- [ ] Shadows are hard offsets only (`4px 4px 0 #000`) — never soft.
- [ ] Hover states are unmistakable (color inversion or full background swap).
- [ ] Deliberate disorder keeps a hidden logic — the layout is never actually random.
- [ ] Marquee/scroll effects pause under `prefers-reduced-motion: reduce`.
- [ ] Interactive targets ≥ 44×44px with a visible focus indicator despite the raw aesthetic.
