---
name: semantic-color-system
description: Success, warning, danger, info - the conventional status hues, their ramps, multi-signal delivery, and protection from brand drift.
tags: [color, semantics, feedback, status, accessibility]
related: [brand-ramp-construction, contrast-models, gray-ramp-neutrals]
---

# Color Theory Skill: Semantic Status & Feedback Color

## 1. Definition

Semantic colors are the conventional vocabulary of UI feedback: green success, amber warning, red danger, blue info. Their hues are conventions users learned long before your product, so this skill defines them as protected ramps with roles (bg, text, border per status), multi-signal delivery (never hue alone - a11y repo guide 02), and an explicit policy that brand palettes do not recolor them. It answers: which green, how light for backgrounds, how dark for text, and who is allowed to change it.

## 2. Core Principles

- **Conventions are the base:** green=success/safe, amber=warning/caution, red=danger/error, blue=info/neutral-notice - deviations need exceptional justification.
- **Each status is a ramp, not a color:** text-tone (700-800), border (300-400), and background (50-100) steps per status - alerts need all three layers.
- **Never hue alone:** status always pairs with icon + text (a11y 1.4.1) - the color is reinforcement, the icon+text is the message.
- **Status hues are protected from brand:** campaigns, theming, and rebrands do not touch semantic ramps - they are vocabulary, not style.
- **Warning is the hardest hue:** amber must read distinctly from both success-green and danger-red - chroma/hue placement is validated against its neighbors.
- **Destructive actions use danger consistently:** the delete button, the confirmation dialog, and the error text are the same danger ramp - consistency builds the reflex.
- **Intensity maps to urgency:** banner (bg 50 + border 300 + text 800) for ambient, filled (600 + white text) for blocking - urgency scales through ramp layers.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Success text | `--clr-success-text` | `clr-success-700` | Success text on light bg |
| Success bg | `--clr-success-bg` | `clr-success-50` | Success banner/tint background |
| Success border | `--clr-success-border` | `clr-success-300` | Banner border tier |
| Warning text | `--clr-warning-text` | `clr-warning-800` | Warning text; darker than others for hue clarity |
| Warning bg | `--clr-warning-bg` | `clr-warning-50` | Warning tint bg |
| Danger text | `--clr-danger-text` | `clr-danger-700` | Danger text on light bg |
| Danger bg | `--clr-danger-bg` | `clr-danger-50` | Error tint bg |
| Danger filled | `--clr-danger-filled` | `clr-danger-600 + white` | Destructive button contract (computed text) |
| Info text | `--clr-info-text` | `clr-info-700` | Info text on light bg |
| Signal pairing | `--clr-status-signal-pairing` | `icon+text+color` | Never color alone (a11y 1.4.1); documented triple |

Consume them by linking `assets/css/semantic-color-system.css` and referencing the role tokens - `var(--clr-success-text)` for status text, `var(--clr-danger-filled)` for destructive surfaces - never raw ramp steps in product code. The role layer is what makes status hues brandable-adjacent yet protected: a rebrand re-points brand aliases, never semantic ones.

## 4. Composition

- **Composes with brand-ramp-construction:** status ramps are generated with the same OKLCH machinery as brand ramps.
- **Composes with color-psychology:** the conventional associations are protected exactly because psychology makes them powerful.
- **Composes with forms-errors (skill-accessibility guide 07) and component-recipes:** alerts, badges, and form states consume these roles.

## 5. Signature Patterns

- **Status alert recipe:** one alert component consuming (text, border, bg, icon) roles per status - banners, toasts, and inline errors share it.
- **Destructive-action contract:** danger-filled button + confirmation dialog + undo toast use the same danger ramp end-to-end.

## 6. Real-World Use Cases

- **Any app with forms, notifications, or destructive actions (all of them).**
- **Multi-brand systems keeping one semantic vocabulary across brands.**
- **Audit:** brand-tinted error states, hue-only warnings, missing banner layers.

## 7. Combination Notes

### With other color-theory skills

- **Good with brand-ramp-construction and oklch-perceptual:** status ramps are generated with the same (hue, chroma curve, L stops) machinery as brand ramps, so the vocabulary is engineered, not hand-picked - and warning's neighbor-distinctness is validated in the same OKLCH space.
- **Good with contrast-models and cvd-safe-design:** every status text/bg pair passes the contrast floors, and CVD simulation confirms status survives color-vision differences - which is why the icon+text triple exists.
- **Good with gray-ramp-neutrals and dark-mode-palette:** status banners sit on neutral surfaces, and dark themes re-bind status text steps (400-500) through the alias layer without touching the ramps.
- **Good with color-psychology, color-harmony, and cultural-color-meaning:** psychology explains why the conventions are worth protecting, harmony keeps status hues from colliding with the scheme, and cultural review localizes the vocabulary where conventions differ.
- **Good with data-viz-palettes and gradient-theory:** charts borrowing status hues for "good/bad" series must use the same ramps, and status colors never become gradient endpoints - vocabulary does not decorate.
- **No avoid or caution list:** semantic color is the most compatible skill in the set - it constrains itself and consumes everything else; the only failure to prevent is bypassing it with ad-hoc reds and greens.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both keep status communication crisp - a flat, three-layer banner (bg/border/text) with an icon is the clearest possible feedback surface, and the ramp layers carry the whole message without ornament.
- **Caution with collage-art and brutalism-ui:** both may want to recolor, distress, or deconstruct status elements for expressive effect - which dissolves the vocabulary. If such a style must stylize status, it may change shape and texture, never hue, layer structure, or the icon+text pairing.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation and micro-interactions:** status color is strongest at the moment of response - a confirm flash on success, a subtle shake plus danger text on failed submit - and micro-interactions are how the color earns attention without hue alone carrying the signal.
- **Caution generally:** status colors must not animate into each other or into brand hues - a transition that lerps a success banner to brand-500 mid-flight temporarily displays a status the system never meant; state changes should swap layers with short, discrete transitions.

## 8. Anti-Patterns

- **Brand-tinted danger** — error states recolored to the campaign palette - vocabulary dissolved
- **Hue-only warnings** — amber banners with no icon or text label
- **One-flat-status** — a single red for text, border, and background - layers missing
- **Green-is-good drift** — success green so bright it reads as decoration rather than confirmation

### Accessibility Notes

This guide implements WCAG 1.4.1 (use of color) at the palette level: every status signal ships as color+icon+text, and all status text/bg pairs pass 4.5:1 - CVD users (guide 11) must decode status without the hue. The ramp structure is what makes this practical: text-tone steps (700-800) are validated dark enough for their tint backgrounds, border steps (300-400) clear the 3:1 UI-component floor, and the icon in the signal triple guarantees the message survives deuteranopia, protanopia, and grayscale rendering. Warning deserves special attention - amber is the hue most easily confused with both green and red under CVD, so its text step is darker (800) and its placement validated against its neighbors. The fallback rule: where a status hue cannot meet contrast at a layer, shift that layer's L (darker text, lighter bg) within the status ramp - the hue convention holds, the values flex.

## 9. Code Examples

### Example 1 — Status alert with text/border/bg/icon layers per status

Tokens: `assets/css/semantic-color-system.css`

```html
<div class="alert alert-success" role="status">
  <svg class="alert-icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 11L3 8l1-1 2 2 5-5 1 1z"/></svg>
  <div><strong>Changes saved</strong> Your workspace settings were updated.</div>
</div>
<div class="alert alert-warning" role="alert">
  <svg class="alert-icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1l7 13H1zm-1 5h2v4H7zm0 5h2v2H7z"/></svg>
  <div><strong>Storage almost full</strong> 92% of quota in use.</div>
</div>
<div class="alert alert-danger" role="alert">
  <svg class="alert-icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1a7 7 0 100 14A7 7 0 008 1zm1 11H7v-2h2zm0-3H7V4h2z"/></svg>
  <div><strong>Payment failed</strong> The card was declined by the bank.</div>
</div>
<style>
  .alert {
    display: flex; gap: 10px; align-items: flex-start;
    padding: 12px 14px; border-radius: 8px; border: 1px solid transparent;
    font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 460px; margin-bottom: 10px;
  }
  /* The status alert recipe: one component consuming (bg, border, text, icon) roles */
  .alert-success { background: var(--clr-success-bg); border-color: var(--clr-success-border); color: var(--clr-success-text); }
  .alert-warning { background: var(--clr-warning-bg); border-color: var(--clr-warning-border, var(--clr-warning-text)); color: var(--clr-warning-text); }
  .alert-danger  { background: var(--clr-danger-bg);  border-color: var(--clr-danger-border, var(--clr-danger-text));  color: var(--clr-danger-text); }
  .alert-icon { width: 16px; height: 16px; flex-shrink: 0; fill: currentColor; margin-top: 2px; }
  .alert strong { font-weight: 600; }
</style>
```

### Example 2 — Destructive-action contract: button + confirm + undo

```html
<div class="danger-flow">
  <button class="btn-danger" id="delete-btn">Delete workspace</button>
  <div class="confirm" id="confirm" hidden role="alertdialog" aria-labelledby="confirm-title">
    <p id="confirm-title">Delete this workspace? This cannot be undone later.</p>
    <button class="btn-danger" id="confirm-yes">Yes, delete</button>
    <button class="btn-ghost" id="confirm-no">Cancel</button>
  </div>
  <div class="undo" id="undo" hidden role="status">
    Workspace deleted. <button class="undo-link" id="undo-btn">Undo</button>
  </div>
</div>
<script>
  // One danger ramp end-to-end: trigger → confirm → undo all consume --clr-danger-* roles
  const show = (id, on) => { document.getElementById(id).hidden = !on; };
  show("confirm", !!document.getElementById("delete-btn").addEventListener("click", () => { show("confirm", true); }));
  document.getElementById("confirm-no").addEventListener("click", () => show("confirm", false));
  document.getElementById("confirm-yes").addEventListener("click", () => { show("confirm", false); show("undo", true); });
  document.getElementById("undo-btn").addEventListener("click", () => show("undo", false));
</script>
<style>
  .danger-flow { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 460px; }
  .confirm, .undo { margin-top: 10px; padding: 12px 14px; border-radius: 8px; }
  .confirm { background: var(--clr-danger-bg); border: 1px solid var(--clr-danger-border, var(--clr-danger-text)); color: var(--clr-danger-text); }
  .undo    { background: var(--clr-danger-bg); color: var(--clr-danger-text); }
  .btn-danger {
    background: var(--clr-danger-filled); /* --clr-danger-600 + white, computed 4.5:1+ */
    color: white; border: none; border-radius: 8px; padding: 10px 18px;
    font: 600 14px/1 Inter, system-ui, sans-serif; cursor: pointer;
  }
  .btn-danger:hover  { filter: brightness(1.08); }
  .btn-ghost { background: transparent; border: 1px solid currentColor; border-radius: 8px; padding: 9px 16px; font: 600 14px/1 Inter, system-ui, sans-serif; cursor: pointer; }
  .undo-link { background: none; border: none; color: inherit; text-decoration: underline; font: 600 14px/1.5 Inter, system-ui, sans-serif; cursor: pointer; }
</style>
```

## 10. Implementation Checklist

- [ ] All four status hues (success/warning/danger/info) exist as ramps with text, border, and bg layers — no single-hex statuses.
- [ ] Product code consumes only role tokens (`var(--clr-success-text)`, `var(--clr-danger-filled)`, ...) — raw status steps never appear in components.
- [ ] Every status signal ships as the documented triple `icon+text+color` (`--clr-status-signal-pairing`) — no hue-only warnings.
- [ ] All status text/bg pairs pass 4.5:1 and border layers pass 3:1; warning text uses `--clr-warning-text` (800) for hue clarity.
- [ ] Destructive flows (button, confirmation dialog, error text, undo) all draw from the same danger ramp.
- [ ] Brand aliases and campaigns never re-point semantic tokens — status hues are protected vocabulary.
- [ ] Warning's hue/chroma placement is validated against success-green and danger-red, including under CVD simulation.
- [ ] Intensity tiers (banner: bg 50 + border 300 + text 800; filled: 600 + white) are the only sanctioned urgency escalations.
