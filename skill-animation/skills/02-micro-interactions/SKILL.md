---
name: micro-interactions
description: Small, single-purpose feedback animations on interactive elements — hover, press, toggle, like, copy — the contained details that make UI feel alive within 100-300ms.
tags: [feedback, hover, press, toggles, interaction-design]
related: [easing-timing, feedback-confirmation, entrance-exit]
---

# Animation Skill: Micro-interactions

## 1. Definition

A micro-interaction is a contained animation that communicates the result of a single user action on a single element: a button depressing, a heart bursting, a toggle sliding, a checkmark drawing itself. It answers the user's question — *"did that register?"* — within 100-300ms, before doubt can set in. Its grammar is deliberately narrow: scale, translate, color, and small loops, applied only to the element that was touched. Layout-shifting movement is never part of this vocabulary; the surrounding interface must stay perfectly still while the control speaks.

## 2. Core Motion Principles

- **Feedback within 100ms:** the state change must begin almost instantly or the action feels dropped.
- **Animate a property the eye tracks on that element:** scale, background, icon state - not the surrounding layout.
- **One effect per event:** a press can depress OR pulse, not both; stacked effects read as noise.
- **Respect a trigger hierarchy:** hover is subtle (lift, tint), press is stronger (scale down), success is declarative (checkmark, color swap).
- **Make it reversible:** hover-in and hover-out use mirrored timing; toggles animate both directions equally.
- **Never block the action:** the animation decorates the result, it does not delay it.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Press | `--motion-press-scale` | `scale(0.97)` | Buttons depress ~3% on `:active` |
| Hover | `--motion-hover-lift` | `translateY(-2px)` | Cards/buttons rise subtly on hover |
| Hover | `--motion-hover-shadow` | `0 4px 12px rgba(0,0,0,0.12)` | Paired with hover-lift for elevation |
| Transition | `--motion-transition-fast` | `150ms cubic-bezier(0.2, 0, 0, 1)` | Default micro-interaction transition |
| Spring | `--motion-spring-tactile` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Toggles, likes, small celebratory pops |

Consume them by linking `assets/css/micro-interactions.css` and composing the custom properties directly: `transition: transform var(--motion-transition-fast)` plus `transform: var(--motion-press-scale)` on `:active`. Because the spring token carries overshoot, reserve `var(--motion-spring-tactile)` for small controls — buttons, knobs, icons — and fall back to `var(--motion-transition-fast)` for anything larger.

## 4. Choreography

- **Icon swap after state settles:** background color lands first (~100ms), then the icon crossfades/draws.
- **Burst effects radiate from the touch/click point,** not the element center, when the trigger is positional.
- **Press-then-release on touch:** animate down on touchstart, complete on touchend so quick taps still feel responsive.

## 5. Signature Patterns

- **Scale-depress button:** :active { transform: scale(0.97) } at 100ms - the cheapest universal 'it pressed' signal.
- **Icon morph:** crossfade or SVG path-draw (stroke-dashoffset) between default and success states.
- **Haptic pairing:** on supported platforms pair press/success with light/medium haptics.

## 6. Real-World Use Cases

- **Buttons, toggles, checkboxes, radio, sliders, tabs** - all interactive controls.
- **Like/favorite/save/bookmark actions** in social and content products.
- **Copy-to-clipboard, download-complete, add-to-cart confirmations.**

## 7. Combination Notes

### With other animation skills

- **Pairs well with easing-timing:** micro-interactions inherit their duration and curve discipline from the token layer; these tokens (`--motion-transition-fast`) are pre-mixed instances of it.
- **Pairs well with feedback-confirmation:** micro-interactions cover the instant "registered" signal; feedback-confirmation takes over for outcomes that need toasts, checkmark draws, and undo.
- **Pairs well with entrance-exit:** controls entering a view can stagger in, then hand over to steady-state hover/press behavior without conflicting timelines.
- **Caution with data-animation:** never attach press/hover effects to dense chart cells or table rows — animate the encoding, not every cell.
- **Caution with gesture-drag:** a draggable element already tracks the pointer 1:1; layering hover lift or press scale on top of an active drag muddies the physical metaphor.
- **Caution with reduced-motion:** swap transforms for color/opacity state changes instead of disabling feedback (see Accessibility Notes).
- **Caution with page-transitions, loading-states, scroll-animation, and illustration-lottie:** keep micro-feedback confined to its control during navigation, loading hand-offs, scroll reveals, or baked Lottie playback — one motion story at a time per region.
- **Avoid ambient-motion:** looping background decoration and instant per-action feedback are opposite ends of the attention budget; ambient loops behind interactive controls bury the feedback.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with neumorphism, claymorphism, and glassmorphism:** all three are tactile or material styles that depend on press/hover physics (inset shadows, squish, elevation) to feel real — micro-interactions are their mandatory motion layer.
- **Caution with minimalism and flat-design:** the styles allow micro-interactions but demand extreme restraint — a single 2px lift or 3% scale, never stacked effects.

## 8. Anti-Patterns

- **Animating layout:** using top/left/width for micro-feedback causes reflow jank; transform and opacity only
- **Effect stacking:** hover lift + shadow + tint + icon change at once exceeds the threshold of subtlety
- **Blocking delays:** an 800ms success animation before the next screen; feedback must never gate progress
- **Invisible hover on touch:** hover-only affordances on touch devices with no pressed-state equivalent

### Accessibility Notes

Under `prefers-reduced-motion`, the strategy is **replace, not remove**: keep the state change itself, but swap scale/translate effects for opacity and color transitions. The fallback in `assets/css/micro-interactions.css` swaps transform effects for background/border color transitions at duration-instant, so a pressed button still flashes its active tint and a toggle still flips its track color — nothing simply vanishes mid-interaction. Because hover has no meaning on touch and no meaning for keyboard users, every hover affordance must also exist as a `:focus-visible` state, and every hover-only effect needs a pressed-state equivalent on touch devices. The global reduced-motion override in the token file collapses all transitions to 1ms; component-level color fallbacks belong after it in the cascade.

## 9. Code Examples

### Example 1 — Button: hover lift, press depress, visible focus (CSS-only)

Tokens: `assets/css/micro-interactions.css`

```html
<button class="btn">Add to cart</button>
<style>
.btn {
  padding: 12px 24px; border: 0; border-radius: 12px;
  background: #4f46e5; color: #fff; font: 500 15px/1 system-ui; cursor: pointer;
  /* one transition line drives hover AND press; instant duration on :active below */
  transition: transform var(--motion-transition-fast), box-shadow var(--motion-transition-fast);
}
.btn:hover {
  transform: var(--motion-hover-lift);          /* translateY(-2px) */
  box-shadow: var(--motion-hover-shadow);        /* paired elevation */
}
.btn:active {
  transform: var(--motion-press-scale);          /* scale(0.97) */
  transition-duration: 100ms;                    /* press must be instant-feeling */
}
.btn:focus-visible {
  outline: 2px solid #4f46e5; outline-offset: 3px;
}
@media (prefers-reduced-motion: reduce) {
  /* replace movement with color feedback; keep the state change */
  .btn:hover  { transform: none; background: #6366f1; box-shadow: none; }
  .btn:active { transform: none; background: #3730a3; }
}
</style>
```

### Example 2 — Tactile toggle with spring overshoot (tiny JS for aria state)

Tokens: `assets/css/micro-interactions.css`

```html
<button class="toggle" role="switch" aria-checked="false" aria-label="Notifications">
  <span class="knob"></span>
</button>
<style>
.toggle {
  width: 52px; height: 30px; padding: 3px; border: 0; border-radius: 15px;
  background: #cbd5e1; cursor: pointer;
  transition: background var(--motion-transition-fast);
}
.knob {
  display: block; width: 24px; height: 24px; border-radius: 50%;
  background: #fff; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
  transition: transform var(--motion-transition-fast);
}
.toggle[aria-checked="true"] { background: #16a34a; }
.toggle[aria-checked="true"] .knob {
  transform: translateX(22px);
  /* spring only on the small knob — never on text or large panels */
  transition-timing-function: var(--motion-spring-tactile);
}
.toggle:focus-visible { outline: 2px solid #16a34a; outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) {
  .knob { transition: none; } /* state flip stays, travel goes */
}
</style>
<script>
  // JS only flips state; the animation is pure CSS and mirrors both directions.
  document.querySelector('.toggle').addEventListener('click', (e) => {
    const el = e.currentTarget;
    el.setAttribute('aria-checked', String(el.getAttribute('aria-checked') !== 'true'));
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every state change starts within 100ms of the trigger — no entrance delay on feedback.
- [ ] Only `transform` and `opacity` (plus color) animate; `top/left/width/height` never appear in a micro-interaction transition.
- [ ] One effect per event: hover = lift OR tint, press = scale-down, success = icon/color — never stacked.
- [ ] `:active` uses `var(--motion-press-scale)` and `:hover` uses `var(--motion-hover-lift)` + `var(--motion-hover-shadow)`, not bespoke values.
- [ ] `var(--motion-spring-tactile)` is reserved for small non-text elements; text and panels use the standard curve.
- [ ] Hover effects are mirrored on hover-out, duplicated as `:focus-visible` states, and have pressed-state equivalents on touch.
- [ ] Under `prefers-reduced-motion`, transforms are replaced with color/opacity state changes and no feedback is removed.
