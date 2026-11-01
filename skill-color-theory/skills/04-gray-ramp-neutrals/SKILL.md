---
name: gray-ramp-neutrals
description: Building the neutral backbone - pure gray vs tinted gray philosophy, elevation steps, and the chroma whisper that ties neutrals to the brand.
tags: [color, neutrals, grays, ramps, elevation]
related: [oklch-perceptual, brand-ramp-construction, dark-mode-palette]
---

# Color Theory Skill: Gray Ramps & Tinted Neutrals

## 1. Definition

Neutrals carry most of any interface's surface area, so the gray ramp is the most-used palette in the product. The central decision: pure grays (colorless, clinical) vs tinted grays (a whisper of brand hue, cohesive). The ramp is structured in lightness steps large enough to read as elevation (0.05-0.08 L deltas), tuned in OKLCH, and temperature-matched to the brand hue - the neutral ramp is where palettes quietly win or lose.

## 2. Core Principles

- **Tint or pure - decide and document:** tinted neutrals (~0.005-0.015 chroma in brand hue) read cohesive; pure grays read neutral-tool. Either is valid; mixing them is not.
- **Elevation needs visible steps:** adjacent neutral steps differ by 0.04-0.08 lightness - subtler deltas read as rendering dirt, not hierarchy.
- **Dark-mode neutrals are not inverted light-mode:** dark grays get less chroma (tints read purple at low lightness) and more elevation contrast.
- **Text neutrals anchor the ramp:** the text-on-surface pair is the highest-contrast, most-used pairing - it is tuned first (guide 10).
- **A gray for every role:** bg, surface, surface-raised, border, text-secondary, text-primary, overlay - the ramp maps to roles, not to math alone.
- **The whisper hue matches the brand temperature:** a warm-hued brand (orange) uses warm-tinted grays; a cool brand (blue) cool-tinted - mismatched whispers read dirty.
- **Neutrals are validated like brand colors:** borders and disabled states have contrast requirements (3:1 UI components) - gray does not mean exempt.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Strategy | `--clr-neutral-strategy` | `tinted-brand-hue` | Documented: tinted (0.005-0.015 C) or pure |
| Hue source | `--clr-neutral-hue-source` | `brand-hue` | The whisper chroma rides the brand hue |
| Background | `--clr-gray-bg` | `oklch(0.985 0.008 210)` | Page background, light theme |
| Surface | `--clr-gray-surface` | `oklch(1.00 0 0)` | Card surface (white) against tinted bg |
| Surface raised | `--clr-gray-surface-raised` | `oklch(1.00 0 0) + shadow` | Elevation via shadow + border, not just fill |
| Border | `--clr-gray-border` | `oklch(0.90 0.01 210)` | Borders pass 3:1 against adjacent surfaces |
| Text secondary | `--clr-gray-text-secondary` | `oklch(0.45 0.02 210)` | Secondary text; 4.5:1+ on surfaces |
| Text primary | `--clr-gray-text-primary` | `oklch(0.22 0.02 210)` | Primary text; near-black with whisper |
| Overlay | `--clr-gray-overlay` | `oklch(0.15 0.02 210 / 60%)` | Scrim/overlay with alpha |
| Step delta | `--clr-gray-step-delta` | `0.04-0.08-L` | Minimum lightness delta between adjacent steps |

Consume them by linking `assets/css/gray-ramp-neutrals.css` at the app root, then referencing `var(--clr-gray-...)` from the alias or component tiers - roles (bg, surface, border, text) are the contract; product code never samples a gray by eye. If a role has no mapped step, extend the ramp through review, not a one-off hex.

## 4. Composition

- **Composes with oklch-perceptual:** ramps are L/C/H structures; the whisper chroma rides the brand hue angle.
- **Composes with dark-mode-palette:** dark themes re-tune the neutral ramp (less chroma, wider elevation deltas) as its own structure.
- **Composes with skill-design-tokens guide 01:** neutral primitives and their alias bindings (surface, border, text) live in the token system.

## 5. Signature Patterns

- **Whisper-tint generator:** the neutral ramp derives from the brand hue + fixed chroma cap - rebranding re-tints all neutrals in one parameter.
- **Role-ramp matrix:** every neutral role (bg→text) mapped to a ramp step with its contrast requirement - roles, not raw steps, are consumed.

## 6. Real-World Use Cases

- **Any palette's foundation:** the neutral ramp is built before brand ramps.
- **Dark themes:** neutrals re-tuned for low-lightness chroma behavior.
- **Audit:** muddy grays (accidental mixed hues), invisible borders, indistinct elevation.

## 7. Combination Notes

### With other color-theory skills

- **Good with oklch-perceptual and brand-ramp-construction:** ramps are generated as L/C/H curves from the brand hue, so the neutral ramp and the brand ramp share one temperature and one generator - the whisper stays consistent.
- **Good with dark-mode-palette and semantic-color-system:** dark themes re-tune this ramp as their own structure (less chroma, wider deltas), and status colors need neutral surfaces to sit against - both consume the role-ramp matrix.
- **Caution with oklch-perceptual:** the math space is shared, but the whisper chroma band (0.005-0.015 C) is this guide's own decision - do not let generic ramp tooling apply brand-level chroma to neutrals, or tints turn muddy.
- **Good with contrast-models, data-viz-palettes, gradient-theory, color-harmony, color-psychology, cultural-color-meaning, and cvd-safe-design:** every scheme needs its neutral anchor (60-30-10), charts need a neutral surface, and gradients need validated endpoints.
- **No avoid list:** neutrals are the substrate everything sits on; the failure to prevent is bypassing this ramp with sampled grays, not any partner skill.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and glassmorphism:** minimalism leans on a disciplined neutral backbone doing the compositional work; flat-design needs crisp borders and distinct fills; glassmorphism's blur layers read only when the tint behind them is consistent.
- **Caution generally:** styles that sample colors from imagery (collage-art) or deliberately want raw, un-tinted grays (brutalism-ui) conflict with a documented whisper strategy - if a style overrides the tint, it must override the documented strategy token, not the values piecemeal.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** elevation is most convincing when surface lightness changes animate with the same easing curve as shadow and transform - a raised state that fades its fill faster than it lifts reads as a flicker.
- **Caution generally:** avoid animating between neutral steps so subtle they sit inside the 0.04-0.08 L delta floor - animated sub-delta transitions read as rendering dirt rather than intentional motion.

## 8. Anti-Patterns

- **Mixed-hue mud** — grays sampled from screenshots and tools, each carrying a different accidental hue
- **Invisible borders** — 1px hairlines at 0.95 L nobody can see (and fail 3:1)
- **Elevation-by-guess** — card, modal, and drawer surfaces within 0.01 lightness of the background
- **Purple-dark-mode** — tinted-light-mode grays reused in dark theme, reading violet at low lightness

### Accessibility Notes

Neutrals are where WCAG lives: text/surface pairings need 4.5:1+, borders and control boundaries 3:1 (guide 10) - the neutral ramp is validated pair-by-pair, not assumed safe for being gray. That is why the token set documents contrast per role (`--clr-gray-text-secondary` at 4.5:1+ on surfaces, `--clr-gray-border` passing 3:1 against adjacent surfaces) and why the role-ramp matrix is the consumption surface: consumers pick validated roles, not raw steps. The fallback rule: when a gray step fails its role's contrast floor, move the step on the L axis (darken/lighten) while keeping the hue whisper - the tint survives, the pairing passes. Disabled states and decorative hairlines are the only documented exemptions, and each must be recorded in the matrix.

## 9. Code Examples

### Example 1 — Tinted-neutral ramp with role bindings

Tokens: `assets/css/gray-ramp-neutrals.css`

```html
<main class="page">
  <section class="card">
    <h2 class="card-title">Workspace settings</h2>
    <p class="card-text">Members see published projects only. Changes apply at midnight UTC.</p>
    <hr class="card-divider" />
    <span class="card-hint">Last edited 2 hours ago</span>
  </section>
</main>
<style>
  .page {
    /* Role bindings consume the ramp — never raw steps in product code */
    background: var(--clr-gray-bg); /* oklch(0.985 0.008 210) */
    min-height: 100vh;
    display: grid;
    place-items: center;
    font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .card {
    background: var(--clr-gray-surface); /* oklch(1.00 0 0) */
    border: 1px solid var(--clr-gray-border); /* 3:1 against adjacent surfaces */
    border-radius: 10px;
    padding: 24px;
    max-width: 380px;
  }
  .card-title { margin: 0 0 6px; font-size: 16px; color: var(--clr-gray-text-primary); }
  .card-text  { margin: 0; color: var(--clr-gray-text-secondary); } /* 4.5:1+ */
  .card-divider { border: 0; border-top: 1px solid var(--clr-gray-border); margin: 16px 0; }
  .card-hint  { font-size: 12px; color: var(--clr-gray-text-secondary); }
</style>
```

### Example 2 — Elevation demo: surface vs raised via lightness

```html
<div class="elev-demo">
  <div class="elev-base">
    Base surface
    <div class="elev-raised">Raised card (surface-raised + border)</div>
  </div>
  <div class="scrim-note">Overlay scrim: 60% alpha over content</div>
</div>
<style>
  .elev-demo {
    background: var(--clr-gray-bg);
    padding: 32px;
    font: 14px/1.5 Inter, system-ui, sans-serif;
    border-radius: 10px;
    max-width: 420px;
  }
  .elev-base {
    background: var(--clr-gray-surface);
    border: 1px solid var(--clr-gray-border);
    border-radius: 8px;
    padding: 20px;
    color: var(--clr-gray-text-primary);
  }
  /* Elevation step: raised reads via fill+border+shadow, min 0.04 L delta from base */
  .elev-raised {
    background: var(--clr-gray-surface);
    border: 1px solid var(--clr-gray-border);
    box-shadow: 0 2px 8px oklch(0.15 0.02 210 / 0.18);
    border-radius: 8px;
    padding: 14px;
    margin-top: 12px;
  }
  .scrim-note {
    margin-top: 12px;
    padding: 12px;
    border-radius: 8px;
    background: var(--clr-gray-overlay); /* oklch(0.15 0.02 210 / 60%) */
    color: oklch(0.98 0.005 210);
  }
</style>
```

## 10. Implementation Checklist

- [ ] The neutral strategy (tinted at 0.005-0.015 C vs pure) is documented in `--clr-neutral-strategy` before any gray value ships.
- [ ] All neutral tokens live in `assets/css/gray-ramp-neutrals.css` and product code consumes only `var(--clr-gray-*)` roles.
- [ ] Every adjacent ramp step differs by at least 0.04 L (`--clr-gray-step-delta`) — no sub-delta "elevation" surfaces.
- [ ] Every role (bg, surface, surface-raised, border, text-secondary, text-primary, overlay) maps to a validated step in the role-ramp matrix.
- [ ] `--clr-gray-border` passes 3:1 against the surfaces it separates; hairlines below that fail review.
- [ ] `--clr-gray-text-secondary` and `--clr-gray-text-primary` pass 4.5:1+ on every surface they may sit on.
- [ ] The whisper chroma rides `--clr-neutral-hue-source` (brand hue) — no grays sampled from screenshots or tools.
- [ ] Dark theme neutrals are built as their own ramp (less chroma, wider deltas), never light grays reused.
