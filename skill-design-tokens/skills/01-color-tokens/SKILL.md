---
name: color-tokens
description: Primitive color scales built as perceptually-even ramps (neutral, brand, feedback) — the raw material every semantic color decision draws from.
tags: [color, tokens, ramps, design-systems, primitives]
related: [typography-tokens, spacing-sizing, semantic-alias-naming]
---

# Design Token Skill: Color Token Scales

## 1. Definition

Color tokens are the primitive layer of a color system: complete, perceptually-even scales (50–950) per hue family, named by step number instead of by intent. Step numbers keep decisions honest — `blue-500` says nothing about where it may be used, which is exactly what keeps the primitive layer reusable across themes, brands, and platforms. Every semantic decision (text, background, action) is expressed later, in the alias tier, by pointing at these steps; nothing in product code consumes a raw scale directly.

## 2. Core Token Principles

- **Build scales by perceptual evenness, not by eye:** use OKLCH lightness so the jump between step 300 and 400 feels the same as 500 to 600 — eyeballed ramps drift and break predictable contrast.
- **Name steps by number, never by intent:** `gray-500`, not `gray-border` — intent lives in the alias tier and must never leak into primitives.
- **One neutral ramp per system:** derive warm/cool variants from it instead of introducing parallel neutral scales that quietly disagree.
- **Fix anchors first:** pick the brand anchor (usually 500), then extend up and down so contrast against white/black is predictable at every step.
- **11 steps (50–950) is enough:** fewer steps force off-scale values; more steps create decision fatigue.
- **Feedback hues get full-scale treatment:** success/warning/danger/info each need the same ramp as brand, not two lonely hexes.
- **Annotate contrast once:** every step states which pass 4.5:1 on white and which pass 3:1, so consumers never guess.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Color | `--dt-color-neutral-0` | `#FFFFFF` | Pure surface; text never lands directly on it without alias review |
| Color | `--dt-color-neutral-100` | `#F5F5F5` | Subtle fill: hover washes, code blocks, table stripes |
| Color | `--dt-color-neutral-300` | `#D4D4D4` | Disabled borders, dividers; fails all text contrast - decoration only |
| Color | `--dt-color-neutral-500` | `#737373` | Placeholder text on white passes 4.5:1; icons at 3:1 |
| Color | `--dt-color-neutral-700` | `#404040` | Secondary body text on white: 10.3:1 |
| Color | `--dt-color-neutral-900` | `#171717` | Primary body text on white: 16.9:1 |
| Color | `--dt-color-brand-500` | `#2563EB` | Brand anchor; white text on it passes 4.6:1 |
| Color | `--dt-color-brand-600` | `#1D4ED8` | Brand hover/pressed; links on white pass 6.3:1 |
| Color | `--dt-color-success-500` | `#22C55E` | Success accents/icons on white at 2.2:1 - pair with success-700 for text |
| Color | `--dt-color-warning-500` | `#F59E0B` | Warning accents; never as text on white (2.1:1) |
| Color | `--dt-color-danger-500` | `#EF4444` | Error accents; error text uses danger-600/700 for 4.5:1 |

Consume them by linking `assets/css/color-tokens.css` once at the app root, then referencing `var(--dt-color-<family>-<step>)` from the alias or component tiers — product code never hardcodes a hex. If a value not in this table seems necessary, the palette is wrong; extend the scale through review, not the component.

## 4. Composition & Layering

- **Primitive scales sit at tier 0.** The alias tier (semantic-alias-naming) and component tier consume them; the reference direction is never reversed, or theming collapses into a code-wide find-and-replace.
- **Scales ship as flat custom properties.** Themes re-point aliases, never re-define scales, so every theme — light, dark, every brand — shares one ramp.
- **New hue families enter only by review.** They must define the full 11-step ramp, not a single hex; a lone `#3B82F6` is an anti-pattern, not a shortcut.

## 5. Signature Patterns

- **Annotate-once contrast map:** a generated table of every step's ratio on white and black ships beside the scale (owned by the contrast-validation skill), making each step self-documenting.
- **Scale-first palette build:** derive an entire product palette by re-pointing brand anchors, while feedback hues stay constant across brands — one ramp, many products.

## 6. Real-World Use Cases

- **Design systems defining their primitive color layer** for the first time.
- **Multi-theme products** needing one ramp that survives light/dark and multi-brand remapping.
- **Auditing an existing palette** for off-scale hexes, orphan colors, and undocumented contrast.

## 7. Combination Notes

### With other token skills

- **Pairs naturally with typography-tokens and spacing-sizing:** text tokens and space tokens are theme-invariant; color supplies only the surfaces they sit on — the cleanest possible tier separation.
- **Pairs with semantic-alias-naming, dark-mode, and multi-brand-theming:** these skills consume this ramp exclusively; a validated 11-step ramp is what makes alias re-pointing (and therefore dark mode) cheap.
- **Pairs with contrast-validation, component-tokens, and token-pipeline-figma:** the annotated ratio table turns this scale into a checkable contract that component tokens inherit and the pipeline can generate.
- **Caution with platform-mapping:** hexes are sRGB on web but color-managed differently per platform; map ramps with the explicit unit/color table rather than copy-pasting hex strings.
- **No avoid list:** as the foundation layer, this skill has no incompatible partners — only skills that bypass it (off-scale hexes), which is the failure mode to prevent.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and glassmorphism:** these styles lean on small, disciplined palettes where perceptually-even ramps and one neutral ramp per system do the heavy lifting.
- **Caution with collage-art and brutalism-ui:** both may deliberately want clashing, raw, or off-ramp colors; if so, deviate consciously via documented alias overrides — never by smuggling off-scale hexes into components.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing and data-animation:** hover/pressed color changes should animate with duration tokens, and chart palettes drawn from these ramps stay legible across data-animation timelines.
- **Caution with ambient-motion:** slowly shifting ambient color fields can push surfaces outside the validated pairings in this scale; any animated background must keep its resting pairing annotated and passing.

## 8. Anti-Patterns

- **Intent-named primitives:** 'color-border' in the primitive tier blocks every future use that is not a border
- **Off-scale hexes:** components shipping #3B82F6 when the scale says brand-500 forks the system silently
- **Single-hex feedback colors:** one green with no lighter/darker steps cannot support bg, border, and text roles accessibly
- **Eye-built ramps:** scales stepped by eyeball feel uneven and break predictable contrast at known steps

### Accessibility Notes

Accessibility here starts earlier than most teams expect: primitives are not exempt from contrast documentation, so each step must declare its ratio on white and black in the generated contrast map — alias authors should never have to guess whether a step is text-safe. This scale ships those annotations in the Notes column (e.g. `--dt-color-neutral-700` at 10.3:1 on white, `--dt-color-warning-500` explicitly failing as text at 2.1:1). The fallback rule is equally strict: if a needed step fails contrast, do not bend the scale to squeeze through — pick the adjacent passing step, or add a validated step through governance. Because accent hues like success/warning/danger at 500 are intentionally not text-safe, feedback text roles must be drawn from darker sibling steps, which is why single-hex feedback colors are banned.

## 9. Code Examples

### Example 1 — Feedback banner built from the ramp

Tokens: `assets/css/color-tokens.css`

```html
<div class="banner" role="status">
  <strong class="banner-title">Deploy successful</strong>
  <p class="banner-text">Build #4821 shipped to production at 14:02.</p>
</div>
<style>
  .banner {
    /* Alias tier consumes the ramp — primitives are never styled directly in product code */
    background: var(--dt-color-neutral-0);
    border: 1px solid var(--dt-color-neutral-300);
    border-left: 4px solid var(--dt-color-success-500);
    border-radius: 8px;
    padding: 16px;
    max-width: 420px;
    font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .banner-title {
    display: block;
    color: var(--dt-color-neutral-900); /* 16.9:1 on white */
    font-weight: 600;
    margin-bottom: 4px;
  }
  .banner-text {
    margin: 0;
    color: var(--dt-color-neutral-700); /* 10.3:1 on white */
  }
</style>
```

### Example 2 — Primary button with validated hover pairings

Tokens: `assets/css/color-tokens.css`

```html
<button class="btn-primary">Create project</button>
<script>
  // Guard: refuse to render a pairing not annotated in the scale
  const css = getComputedStyle(document.documentElement);
  const anchor = css.getPropertyValue('--dt-color-brand-500').trim();
  const onAction = css.getPropertyValue('--dt-color-neutral-0').trim();
  console.assert(anchor && onAction, 'brand-500 / neutral-0 pairing must exist in the scale');
</script>
<style>
  .btn-primary {
    background: var(--dt-color-brand-500); /* anchor: white on it passes 4.6:1 */
    color: var(--dt-color-neutral-0);
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font: 600 14px/1 Inter, system-ui, sans-serif;
    cursor: pointer;
    transition: background 150ms ease;
  }
  .btn-primary:hover  { background: var(--dt-color-brand-600); } /* darker step, keeps 4.5:1+ */
  .btn-primary:active { background: var(--dt-color-brand-600); }
  .btn-primary:focus-visible { outline: 2px solid var(--dt-color-brand-600); outline-offset: 2px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every ramp is perceptually even (OKLCH) with 11 steps from 50 to 950 — no off-scale hexes anywhere in the codebase.
- [ ] All primitive tokens use the `--dt-color-<family>-<step>` naming; zero intent-named primitives exist.
- [ ] Product code references only `var(--dt-color-...)` via the alias tier — a direct primitive reference in a component fails review.
- [ ] The annotated contrast map (ratios on white/black per step) is generated and ships beside `assets/css/color-tokens.css`.
- [ ] Feedback hues (success/warning/danger/info) each have a full ramp, not single hexes.
- [ ] Text roles use only steps documented at 4.5:1+ on their surface (e.g. neutral-700/900, danger-600/700).
- [ ] Themes re-point aliases only — no theme block re-defines a `--dt-color-*` primitive value.
- [ ] New hue or step requests go through governance review, never a one-off hex in a component.
