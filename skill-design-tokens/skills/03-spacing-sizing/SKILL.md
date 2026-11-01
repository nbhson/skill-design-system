---
name: spacing-sizing
description: A 4px-base spacing scale, icon sizing, and touch-target minimums that give every layout decision a legal value.
tags: [spacing, sizing, layout, touch-targets, design-systems]
related: [color-tokens, typography-tokens, semantic-alias-naming]
---

# Design Token Skill: Spacing & Sizing Tokens

## 1. Definition

Spacing tokens are the rhythm section of a design system: one 4px-base scale (4/8/12/16/24/32/48/64) from which all padding, gap, and margin values are drawn, plus sizing tokens for icons and interactive targets. Because space is invisible when right and glaring when wrong, the scale's job is to make "close enough" impossible — any layout question has exactly one legal answer at each density level.

## 2. Core Token Principles

- **4px base, doubling emphasis:** 4/8/16/32 for structural rhythm, 12/24/48 as half-steps for dense and hero contexts.
- **Fewer steps, more discipline:** 8 spacing values cover everything; every added value dilutes the grid's meaning.
- **Spacing communicates hierarchy:** related items sit closer (space-2 to space-3) than unrelated ones (space-6 to space-8) — proximity is the token's semantics.
- **Icons get fixed slots:** 16/24/32px boxes that align to the spacing grid, so glyphs never optically drift.
- **Touch targets are a floor, not a style:** 44x44px minimum (WCAG 2.5.8) regardless of visual size.
- **Container padding derives from the same scale as gaps:** a card's padding is a spacing token, not a component-local decision.
- **Never ship negative spacing or odd values:** if a layout seems to need 13px, the composition is wrong, not the scale.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Spacing | `--dt-space-1` | `4px` | Icon-to-label gap, chip inner padding |
| Spacing | `--dt-space-2` | `8px` | Related-element gap, list item inner padding |
| Spacing | `--dt-space-3` | `12px` | Form field spacing, dense card padding |
| Spacing | `--dt-space-4` | `16px` | Default component padding, grid gutter |
| Spacing | `--dt-space-6` | `24px` | Card padding, section inner spacing |
| Spacing | `--dt-space-8` | `32px` | Between content groups |
| Spacing | `--dt-space-12` | `48px` | Between sections |
| Spacing | `--dt-space-16` | `64px` | Page-level section separation |
| Sizing | `--dt-size-icon-sm` | `16px` | Inline icons beside 14px text |
| Sizing | `--dt-size-icon-md` | `24px` | Standalone icon buttons, nav icons |
| Sizing | `--dt-size-touch-target` | `44px` | WCAG 2.5.8 minimum interactive target; pad small visuals to this |

Consume them by linking `assets/css/spacing-sizing.css` once at the app root, then referencing `var(--dt-space-*)` and `var(--dt-size-*)` in every padding, gap, margin, and icon-size declaration. If a value not in this table seems necessary, the composition is wrong; re-group the layout or add a step through review, never a 13px one-off.

## 4. Composition & Layering

- **Spacing tokens pair with typography tokens.** Line-height boxes + space tokens form the vertical rhythm; text blocks snap to the same 4px grid as everything else.
- **Component tokens consume spacing values** (component-card-padding = space-4), so a density mode can re-map one tier and tighten the whole UI without touching a component.
- **Touch-target sizing composes with contrast-validation.** Hit areas stay 44px even when the visible glyph is smaller — opacity and size are independent axes, and both have their own requirements.

## 5. Signature Patterns

- **Density modes as token overrides:** compact re-maps space-4 to space-3 at the alias tier; no component rewrites its own padding, so "compact" is one CSS block, not a code-wide diff.
- **Stack-and-gap layouts:** vertical rhythm expressed only as flex/grid gap of a scale value — margins are reserved for typographic exceptions, which keeps spacing auditable.

## 6. Real-World Use Cases

- **Design systems establishing a shared layout grid** across web and native.
- **Density modes** (compact tables, comfortable marketing pages) from one token set.
- **Auditing spacing debt:** magic numbers, misaligned gutters, sub-44px touch targets.

## 7. Combination Notes

### With other token skills

- **Pairs well with color-tokens and typography-tokens:** color and type define what a surface says; spacing defines how far apart the saying happens — the three together form the complete visual grammar of a component.
- **Pairs with radius-elevation, semantic-alias-naming, and component-tokens:** component tokens derive padding and gaps from this scale, so a density mode re-maps one alias tier and every surface tightens in lockstep.
- **Pairs with contrast-validation and platform-mapping:** target-size floors and unit conversions (px → dp/pt) must be validated like any other token contract, not hand-synced per platform.
- **Caution with dark-mode and multi-brand-theming:** spacing is theme- and brand-invariant, so theme layers should never touch these tokens — if a brand asks for tighter padding, answer with a density mode at the alias tier, not a brand fork.
- **No avoid list:** as a structural foundation, this skill has no incompatible partners — only layouts that bypass the scale, which is precisely the debt this skill exists to prevent.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism and flat-design:** both live and die by whitespace discipline, and a closed 8-value scale is what makes "generous but consistent" air reproducible instead of vibes.
- **Caution with maximalism and collage-art:** both encourage dense, overlapping, or intentionally irregular compositions that fight the grid; if so, deviate consciously as a documented layout mode — never by letting one-off gaps leak back into component tokens.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit and easing-timing:** stagger offsets and translate distances are layout values too — express entrance slides and stagger gaps in `--dt-space-*` steps so motion and layout share one grid.
- **No caution list:** spacing tokens impose no timing constraints; motion simply inherits the scale for distances, which is why the affinity is purely positive.

## 8. Anti-Patterns

- **Magic spacing:** 13px, 18px, 27px one-offs that quietly abandon the grid
- **Spacing as decoration:** inflating gaps to 'add air' instead of fixing hierarchy - proximity must stay meaningful
- **Sub-44px touch targets:** visually small icons shipped without invisible padding to the 44px floor
- **Parallel scales:** a separate 'dense' scale instead of one scale re-mapped at the alias tier

### Accessibility Notes

The scale owns WCAG 2.5.8 target size: any interactive element smaller than 44px must be padded to the floor with `--dt-size-touch-target`, so a 24px icon button ships as a 44px hit box around a 24px glyph — visual size and target size are independent axes. It also preserves WCAG 1.4.12 text-spacing tolerance: because line-height boxes and space tokens share the 4px grid, layouts survive when users override text spacing via user stylesheets, instead of collapsing the moment spacing is not user-controlled. The fallback is firm: if a dense layout cannot afford 44px targets, redesign the layout — target size is never traded away for density.

## 9. Code Examples

### Example 1 — Card list with stack-and-gap rhythm

Tokens: `assets/css/spacing-sizing.css`

```html
<div class="stack">
  <article class="card">
    <span class="card-icon" aria-hidden="true">◆</span>
    <div class="card-body">
      <h3 class="card-title">API rate limits</h3>
      <p class="card-text">Requests are capped at 600/min per token.</p>
    </div>
  </article>
  <article class="card">
    <span class="card-icon" aria-hidden="true">◆</span>
    <div class="card-body">
      <h3 class="card-title">Webhook retries</h3>
      <p class="card-text">Failed deliveries retry 5 times over 24 hours.</p>
    </div>
  </article>
</div>
<style>
  body { margin: 0; padding: var(--dt-space-8); font: 14px/1.5 Inter, system-ui, sans-serif; }
  /* Stack: rhythm expressed ONLY as gap of a scale value */
  .stack { display: grid; gap: var(--dt-space-4); max-width: 420px; }
  .card {
    display: flex;
    gap: var(--dt-space-3);          /* 12px: icon to text, dense context */
    padding: var(--dt-space-6);      /* 24px: card padding from the scale */
    border: 1px solid #e4e7ec;
    border-radius: 8px;
    background: #fff;
  }
  .card-icon {
    display: grid; place-items: center;
    width: var(--dt-size-icon-md);   /* fixed 24px icon slot */
    height: var(--dt-size-icon-md);
    color: #2563EB;
  }
  .card-body { display: grid; gap: var(--dt-space-1); } /* 4px: title to text */
  .card-title { margin: 0; font-size: 1rem; font-weight: 600; color: #171717; }
  .card-text  { margin: 0; color: #404040; }
</style>
```

### Example 2 — Icon button padded to the 44px touch floor

Tokens: `assets/css/spacing-sizing.css`

```html
<button class="icon-btn" aria-label="Delete row">
  <svg class="glyph" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2 4h12M5 4V2h6v2M4 4l1 10h6l1-10" fill="none" stroke="currentColor"
          stroke-width="1.5" stroke-linecap="round"/>
  </svg>
</button>
<script>
  // Contract check: the hit box must never fall below the touch floor
  const box = document.querySelector('.icon-btn').getBoundingClientRect();
  const floor = parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue('--dt-size-touch-target')
  );
  if (box.width < floor || box.height < floor) {
    console.error(`Touch target ${box.width}x${box.height} < ${floor}px (WCAG 2.5.8)`);
  }
</script>
<style>
  body { margin: 0; padding: var(--dt-space-6); }
  .icon-btn {
    /* 16px glyph + padding = 44px hit box, all from the scale */
    padding: calc((var(--dt-size-touch-target) - var(--dt-size-icon-sm)) / 2); /* 14px */
    border: 1px solid #e4e7ec;
    border-radius: 8px;
    background: #fff;
    cursor: pointer;
    display: inline-grid;
    place-items: center;
    line-height: 0;
  }
  .icon-btn:hover { background: #F5F5F5; }
  .icon-btn:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; }
  .glyph { width: var(--dt-size-icon-sm); height: var(--dt-size-icon-sm); }
</style>
```

## 10. Implementation Checklist

- [ ] Every padding, gap, and margin in the codebase references a `--dt-space-*` token — zero magic numbers (no 13px, 18px, 27px).
- [ ] No negative spacing values and no odd-pixel values exist anywhere in shipped CSS.
- [ ] Icons use fixed slots from `--dt-size-icon-sm/md` (16/24px) that align to the 4px grid.
- [ ] Every interactive element is at least `--dt-size-touch-target` (44px), with small visuals padded invisibly to the floor.
- [ ] Vertical rhythm is expressed as flex/grid `gap` of a scale value; margins appear only as documented typographic exceptions.
- [ ] Density modes re-map space tokens at the alias tier — no component rewrites its own padding for compact mode.
- [ ] Container padding (card padding, section insets) derives from the same scale as gaps between components.
- [ ] Layouts survive user text-spacing overrides (WCAG 1.4.12) — verified with a spacing-injection test.
