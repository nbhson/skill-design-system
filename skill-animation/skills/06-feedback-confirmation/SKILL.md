---
name: feedback-confirmation
description: System-to-user communication — toasts, success checkmarks, destructive-action confirms, and undo flows with motion that makes outcomes unambiguous.
tags: [toasts, undo, confirmation, errors, success]
related: [micro-interactions, easing-timing, entrance-exit, loading-states]
---

# Animation Skill: Feedback & Confirmation

## 1. Definition

Feedback animations are how the system answers back: a toast sliding in, a checkmark drawing itself after a save, a row flashing red before deletion, an undo pill offering reversal. They are declarative and outcome-focused — the opposite of decorative motion. Their job is to remove ambiguity about what just happened, especially for actions that are slow, destructive, or happened off-screen. Every feedback animation should be justifiable as a sentence the interface says to the user — "saved", "that input was invalid", "deleted — undo?". If it cannot be phrased as a message, it is decoration and belongs to another skill.

## 2. Core Motion Principles

- **Outcome first, decoration second:** the state change (color, icon, text) carries meaning; the motion only draws attention to it.
- **Confirm in place when possible:** an inline checkmark beats a toast; a toast beats a modal.
- **Destructive actions get friction:** a shake on invalid input, a brief red flash, or a confirm step - never instant irreversible motion.
- **Undo is the real confirmation:** for destructive or bulk actions, animate the removal but keep recovery one tap away.
- **Toasts are ephemeral and dismissible:** 4-8s on screen, swipe/click to dismiss, hover pauses the timer.
- **Errors demand stillness:** error states animate attention-getting (shake, flash) once, then hold steady for reading.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Toast enter | `--motion-toast-enter` | `240ms` | Slide+fade in with ease-decelerate |
| Toast exit | `--motion-toast-exit` | `160ms` | Fade/slide out with ease-accelerate |
| Toast duration | `--motion-toast-duration` | `5000ms` | Default on-screen time; action toasts 8000ms |
| Checkmark draw | `--motion-checkmark-draw` | `300ms` | SVG stroke-dashoffset draw after success |
| Shake amplitude | `--motion-shake-amplitude` | `6px` | Error shake; 2–3 oscillations max |
| Highlight flash | `--motion-highlight-flash` | `600ms` | Row/field flash on update or error |

Consume tokens by importing `assets/css/feedback-confirmation.css` and referencing the custom properties (`var(--motion-toast-enter)`, `var(--motion-checkmark-draw)`, …) in every toast, checkmark, and error effect. Timings for the full confirm flow — enter, draw, hold, exit — chain from these six values; do not invent per-component variants.

## 4. Choreography

- **Save flow:** button label swaps to spinner (150ms) -> checkmark draws (300ms) -> button returns to idle (200ms later).
- **Toast stacking:** new toasts push existing ones up with the collapse duration; exits do not shift unread toasts abruptly.
- **Delete flow:** item collapses -> neighbors reflow -> undo toast enters from bottom in the same beat.

## 5. Signature Patterns

- **SVG checkmark draw:** set stroke-dasharray = path length, animate stroke-dashoffset to 0.
- **Invalid shake:** translateX keyframes +-6px over 300ms on the input wrapper, paired with a red border tint.
- **Undo toast:** destructive UI updates instantly, toast offers 'Undo' for 5-8s before the real backend delete.

## 6. Real-World Use Cases

- **Save/send/publish confirmations** in editors and forms.
- **Cart actions, wishlist, subscriptions** - commerce feedback.
- **Form validation errors, permission denials, failed network actions.**

## 7. Combination Notes

### With other animation skills

- **Pairs well with `easing-timing` and `micro-interactions`:** toast enter uses decelerate and exit uses accelerate per the standard curve hierarchy, and the button press plus success checkmark are two halves of one feedback story.
- **Pairs well with `entrance-exit` and `loading-states`:** the delete flow is exit choreography (collapse + reflow) with an undo toast as recovery, and the save flow hands off from spinner to checkmark.
- **Pairs well with `illustration-lottie` and `gesture-drag`:** celebration moments belong to Lottie within the celebration duration budget; swipe-to-dismiss toasts resolve into confirmation or undo.
- **Use with caution alongside `page-transitions`:** fire the toast after the route settles, not during the snapshot — stacked motion muddles both.
- **Use with caution alongside `reduced-motion`:** shake and travel are removed in reduced mode while outcome signals must survive intact.
- **Use with caution alongside `scroll-animation` and `data-animation`:** error flashes and value ticks share the highlight-flash language — each must play once per event, never double-fire.
- **Avoid `ambient-motion`:** celebratory feedback is momentary and outcome-bound; ambient loops behind toasts and errors bury the message.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with Minimalism, Flat Design, and Neumorphism:** clean toasts, flat color flashes, and soft pressed/raised confirm states read clearly in these systems without ornament.
- **Use caution with Maximalism and Brutalism UI:** these styles tempt designers into oversized celebration effects and harsh shakes that overpower the outcome — scale feedback down and let color and text carry meaning.

## 8. Anti-Patterns

- **Celebrating everything:** confetti and fanfare on every save dilutes the moments that deserve celebration.
- **Toast overload:** firing five toasts for one action; consolidate into one message with a summary.
- **Uncatchable feedback:** an error flash so brief users cannot tell what failed; error states must persist.
- **Modal spam:** confirming trivial actions with modal dialogs; reserve modals for truly destructive/irreversible choices.

### Accessibility Notes

Motion must never be the only carrier of an outcome — color, icon, and text survive even when movement is removed. The strategy from `skills/data.json` → `reducedMotion`: **keep all outcome signals (icon, color, text); remove shake and travel, using instant position plus a short opacity fade.** The fallback renders toasts fading in place, checkmarks appearing without the draw, and errors indicated by persistent color plus text with no shake. The global override in `assets/css/feedback-confirmation.css` collapses all animation and transition durations to 1ms under `prefers-reduced-motion: reduce`. Complement the visuals with `role="status"`/`aria-live="polite"` on toast regions so screen readers announce outcomes, keep error messages persistent (not just flashed), and make toasts keyboard-dismissible with the auto-dismiss timer paused on hover/touch.

## 9. Code Examples

### Example 1 — Toast with enter/exit, auto-dismiss, and undo action

Tokens: `assets/css/feedback-confirmation.css`

```html
<div class="toast" role="status" aria-live="polite" hidden>
  <span>Board moved to trash</span> <button class="toast__action" type="button">Undo</button>
</div>

<style>
  .toast { display: flex; align-items: center; gap: 16px; padding: 12px 16px; border-radius: 8px; background: #1f2937; color: #fff; }
  .toast.is-entering { animation: toast-in var(--motion-toast-enter) cubic-bezier(0, 0, 0, 1) both; }
  .toast.is-leaving  { animation: toast-out var(--motion-toast-exit) cubic-bezier(0.3, 0, 1, 1) both; }
  @keyframes toast-in  { from { opacity: 0; transform: translateY(12px); } }
  @keyframes toast-out { to   { opacity: 0; transform: translateY(8px); } }
  .toast__action { border: 0; background: none; color: #8ab4f8; font-weight: 600; cursor: pointer; }
  .toast__action:focus-visible { outline: 2px solid #8ab4f8; outline-offset: 2px; }
  @media (prefers-reduced-motion: reduce) { .toast.is-entering { animation: none; } }
</style>

<script>
  function showToast({ action, duration = 5000 } = {}) {
    const toast = document.querySelector('.toast');
    toast.hidden = false;
    toast.classList.add('is-entering');
    let timer = setTimeout(dismiss, duration); // pass 8000 for action toasts
    toast.addEventListener('mouseenter', () => clearTimeout(timer)); // hover pauses
    toast.querySelector('.toast__action').onclick = () => { action?.(); dismiss(); };
    function dismiss() {
      clearTimeout(timer);
      toast.classList.replace('is-entering', 'is-leaving');
      toast.addEventListener('animationend', () => (toast.hidden = true), { once: true });
    }
  }
</script>
```

### Example 2 — Success checkmark draw and invalid-input shake

Tokens: `assets/css/feedback-confirmation.css`

```html
<!-- JS adds .is-success to the button once the save request resolves. -->
<button class="save" type="button">
  <svg class="check" viewBox="0 0 24 24" aria-hidden="true">
    <path d="M4 12.5l5 5L20 7" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" pathLength="100"/>
  </svg>
  <span class="save__label">Save</span>
</button>

<style>
  .save { display: inline-flex; align-items: center; gap: 8px; padding: 10px 20px; border: 0;
          border-radius: 8px; background: #1a73e8; color: #fff; font-weight: 600; cursor: pointer; }
  .save:focus-visible { outline: 2px solid #1a73e8; outline-offset: 3px; }
  .check { width: 18px; height: 18px; display: none; }
  .save.is-success .check { display: block; }
  .save.is-success .check path { stroke-dasharray: 100;
    animation: draw var(--motion-checkmark-draw) cubic-bezier(0, 0, 0, 1) both; }
  @keyframes draw { from { stroke-dashoffset: 100; } to { stroke-dashoffset: 0; } }
  /* Invalid shake: 2-3 oscillations at +-6px, then the error state holds */
  .field.is-invalid { animation: shake 300ms both; border-color: #d93025; }
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(calc(var(--motion-shake-amplitude) * -1)); }
    55% { transform: translateX(var(--motion-shake-amplitude)); }
    80% { transform: translateX(calc(var(--motion-shake-amplitude) * -0.5)); }
  }
  @media (prefers-reduced-motion: reduce) {
    .save.is-success .check path { animation: none; stroke-dashoffset: 0; }
    .field.is-invalid { animation: none; } /* persistent red border carries the error */
  }
</style>
```

## 10. Implementation Checklist

- [ ] Confirm in place first: inline checkmark > toast > modal — modals reserved for truly irreversible choices.
- [ ] Toast timings come from tokens: 240ms enter, 160ms exit, 5s default / 8s with action, hover pauses the timer.
- [ ] Every destructive action animates its removal but keeps an undo affordance for 5–8s before the backend commit.
- [ ] Error states animate attention once (shake ≤3 oscillations, single flash) then persist — never a flash that disappears unread.
- [ ] Outcome signals (color, icon, text) never rely on motion alone to communicate.
- [ ] Toast regions use `role="status"`/`aria-live="polite"` and are keyboard-dismissible with visible `:focus-visible` rings.
- [ ] `prefers-reduced-motion: reduce` removes shake, travel, and checkmark draw while keeping persistent color + text outcomes (global override in `assets/css/feedback-confirmation.css`).
