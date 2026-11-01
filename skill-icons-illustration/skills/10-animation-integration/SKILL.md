---
name: animation-integration
description: Motion on vector assets: when icons animate, Lottie vs SMIL vs CSS, weight costs, and reduced-motion fallbacks.
tags: [animation, icons, lottie, motion, reduced-motion]
related: [svg-optimization, icon-system-audit, empty-error-illustrations]
---

# Visual Asset Guide: Icon & Illustration Animation

## 1. Definition

Animated icons and illustrations carry delight - and weight, complexity, and a11y obligations. This guide covers the integration rules: when an icon earns animation (state feedback, loading, celebration), the technique choice (CSS for simple transforms, Lottie for character/scene work, SMIL deprecated), weight budgets (animation multiplies file size), and the mandatory reduced-motion fallback (static frame equivalents). Motion on vector assets is an enhancement layered on a system that must stay fully legible without it: every animated asset has a static resting state, every loop is rationed, and every animated state change is also communicated through a channel that survives with animation disabled.

## 2. Core Principles

- **Animation earns its place:** state feedback (success check draw-in), loading, and celebration justify motion - idle decoration rarely does.
- **Technique by complexity:** CSS transforms for simple (rotate/scale/draw), Lottie for character/scene work, SMIL/CSS keyframe hackery avoided - the choice is documented per asset.
- **Weight budget doubles for animation:** an animated icon should cost < 15KB; Lottie scenes < 100KB - motion must justify its payload.
- **Reduced-motion is mandatory:** every animated asset has a static fallback frame (or collapses to opacity fade) under prefers-reduced-motion - no exceptions.
- **Loop with restraint:** looping ambient animation is rationed (one per viewport max) - looping everywhere reads as a game.
- **Draw-on/load-in is the default pattern:** stroke draw-in and fade-scale entrances are the tasteful 90% - flarb/bounce is opt-in.
- **Animation state is communicated:** loading spinners, success draw-ins, and error shakes narrate (aria-live or visible text pair) - motion is never the only signal.
- **Play controls for long scenes:** illustrations animating > 5s offer pause - ambient loops under 5s exempt.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Justification | `--icon-animation-justification` | `feedback,loading,celebration` | The three earning moments |
| Technique | `--icon-technique-choice` | `css-simple,lottie-scene` | SMIL avoided; choice documented |
| Icon budget | `--icon-animated-icon-budget` | `<15kb` | Per animated icon |
| Scene budget | `--icon-lottie-budget` | `<100kb` | Per scene; lazy-loaded |
| Reduced motion | `--icon-reduced-motion` | `static-fallback-required` | No exceptions |
| Loop policy | `--icon-loop-policy` | `one-per-viewport-max` | Ambient rationed |
| Default pattern | `--icon-default-pattern` | `draw-in+fade-scale` | The tasteful defaults |
| State announce | `--icon-state-announce` | `motion-never-only-signal` | Text/live-region paired |
| Long scene pause | `--icon-long-scene-pause` | `>5s-offers-pause` | 2.2.2 pause control |
| Trigger timing | `--icon-trigger-timing` | `on-state-change` | Motion tracks real events |

Consume them by linking `assets/css/animation-integration.css` once at the app root, then referencing `var(--icon-<role>)` from component styles - animation code reads budgets, loop policy, and pause thresholds from tokens rather than hardcoding magic numbers, so tightening a budget or changing the loop policy is a token edit, not a codebase hunt.

## 4. Composition

- **Composes with skill-animation:** motion tokens (durations/easings) drive all icon/illustration animation - one timing system.
- **Composes with svg-optimization (guide 09):** animated assets need config exceptions and weight budgets - caution pairing is by design.
- **Composes with empty-error-illustrations + mascot-character:** the celebration/loading moments are the earning moments.

## 5. Signature Patterns

- **The draw-in pattern:** stroke-dashoffset draw for success/check glyphs - 300-500ms, easing-timing tokens, static fallback. The check mark completes in the time a user takes to register the state change; slower reads as lag, faster reads as a flicker.
- **The Lottie budget gate:** scenes are weight-checked at contribution (lottie-web renderer, sub-100KB, lazy-loaded) before entering the library. A scene that cannot meet the budget is simplified or rejected - the gate protects the payload, not the art.

## 6. Real-World Use Cases

- **Success/celebration moments** (save complete, goal reached).
- **Loading states with branded personality.**
- **Audit: flarb-everything motion, unthrottled loops, missing reduced-motion.**

## 7. Combination Notes

### With other icons-illustration skills

- **Good with svg-optimization, icon-system-audit, and empty-error-illustrations:** optimization gives animated assets a lean pipeline, the audit checks loop policy and fallbacks as criteria, and empty/error states are where loading and celebration animation legitimately earns its place.
- **Good with icon-style-selection and icon-grid-sizing:** animated icons stay in the same family - motion animates the grid-drawn glyph, never replaces it with a different artwork.
- **Caution with svg-optimization (also listed good):** the pairing is deliberately flagged both ways - SVGO's default transforms can strip animation hooks and flatten groups that strokes animate through, so animated files need documented config exceptions; the skills compose, but only with the exception list reviewed.
- **No avoid list:** no guide here forbids motion - the risk is unrationed motion, which the loop-policy and budget tokens contain.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with claymorphism, aurora-ui, and glassmorphism:** these styles already trade in soft depth, gradient light, and layered surfaces, so draw-in strokes, fade-scale entrances, and gentle scene animation extend the language instead of contradicting it.
- **Caution with minimalism:** minimalist UIs promise stillness - every animation must be a state-change reply, never ambient decoration; keep the loop count at zero and reserve motion for feedback only.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions, illustration-lottie, and loading-states:** draw-ins and fade-scales are micro-interactions on vector assets, Lottie scenes are the illustration-lottie technique applied, and branded loading states give waiting a personality.
- **Caution with ambient-motion:** ambient loops are exactly what the one-per-viewport policy rations - an ambient-motion direction on icons needs explicit justification plus a pause control, or it collides with the loop-restraint rule.

## 8. Anti-Patterns

- **Motion everywhere** — every icon bouncing, nothing readable as stable UI
- **The 500KB celebration** — a Lottie scene punishing the success page
- **No static fallback** — animation required for meaning, breaking reduced-motion users
- **Infinite loops en masse** — five ambient animations fighting in one viewport

### Accessibility Notes

This guide implements WCAG 2.2.2 (pause, stop, hide) and 2.3.3 (animation from interactions) plus reduced-motion: static fallbacks are mandatory, long scenes offer pause, and motion never carries the only meaning - animation state must be text-announced. In practice that means every draw-in, shake, or celebration has a static frame the same glyph collapses to under `prefers-reduced-motion`, any scene running past five seconds ships a visible pause control (WCAG 2.2.2), and a success animation pairs with an `aria-live` announcement or visible text so screen-reader and vestibular-sensitive users receive the same information. The fallback rule is absolute: if a static fallback cannot be produced per asset, disable the animation entirely - motion is enhancement, never the baseline.

## 9. Code Examples

### Example 1 — Draw-in success check (400ms, reduced-motion static fallback)

Tokens: `assets/css/animation-integration.css`

```html
<div class="toast" role="status">
  <svg class="check" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
    <circle class="check-ring" cx="12" cy="12" r="10" />
    <path class="check-mark" d="M7 12.5l3.2 3.2L17 9" />
  </svg>
  <span class="toast-text">Project saved</span>
</div>
<style>
  .toast {
    display: inline-flex; align-items: center; gap: 10px;
    padding: 12px 16px; border-radius: 8px;
    background: var(--icon-animated-icon-budget) none; /* budget token read by JS below */
    border: 1px solid currentColor; color: #067647;
    font: 14px/1.4 Inter, system-ui, sans-serif;
  }
  .check-ring, .check-mark {
    fill: none; stroke: currentColor; stroke-width: 2;
    stroke-linecap: round; stroke-linejoin: round;
  }
  /* --icon-default-pattern: draw-in; --icon-trigger-timing: on-state-change */
  .check-ring { stroke-dasharray: 63; stroke-dashoffset: 63; animation: draw 400ms ease-out forwards; }
  .check-mark { stroke-dasharray: 15; stroke-dashoffset: 15; animation: draw 400ms ease-out 250ms forwards; }
  @keyframes draw { to { stroke-dashoffset: 0; } }
  @media (prefers-reduced-motion: reduce) {
    /* --icon-reduced-motion: static-fallback-required - final frame, no animation */
    .check-ring, .check-mark { stroke-dashoffset: 0; animation: none; }
  }
</style>
<script>
  // --icon-state-announce: motion-never-only-signal (role="status" narrates) + --icon-animated-icon-budget (<15kb) asserted
  const bytes = new Blob([document.querySelector('.check').outerHTML]).size / 1024;
  console.assert(bytes < 15, 'animated icon must stay under --icon-animated-icon-budget');
</script>
```

### Example 2 — Loop restraint: one ambient loop per viewport + pause for >5s scenes

Tokens: `assets/css/animation-integration.css`

```html
<div class="stage">
  <!-- The one ambient loop allowed in this viewport: a slow pulse, 4s cycle (< 5s => pause exempt) -->
  <svg class="ambient" viewBox="0 0 24 24" width="32" height="32" aria-hidden="true" focusable="false">
    <circle cx="12" cy="12" r="8" />
  </svg>

  <!-- Long scene (runs 8s): --icon-long-scene-pause (>5s-offers-pause) requires a pause control -->
  <div class="scene-wrap">
    <svg class="scene" viewBox="0 0 48 24" width="96" height="48" aria-hidden="true" focusable="false">
      <circle class="orb a" cx="10" cy="12" r="6" />
      <circle class="orb b" cx="24" cy="12" r="6" />
      <circle class="orb c" cx="38" cy="12" r="6" />
    </svg>
    <button class="pause-btn" type="button" aria-pressed="false">Pause animation</button>
  </div>
</div>
<style>
  .stage { font: 14px/1.5 Inter, system-ui, sans-serif; color: #1e293b; display: grid; gap: 16px; }
  .ambient { fill: none; stroke: #6366f1; stroke-width: 2; animation: pulse 4s ease-in-out infinite; }
  .scene-wrap { display: flex; align-items: center; gap: 12px; }
  .pause-btn { border: 1px solid #cbd5e1; background: #fff; border-radius: 6px; padding: 6px 12px; font: inherit; cursor: pointer; }
  .orb { fill: #6366f1; animation: drift 8s ease-in-out infinite; }
  .orb.b { animation-delay: 150ms; } .orb.c { animation-delay: 300ms; }
  .scene.is-paused .orb { animation-play-state: paused; }
  @keyframes pulse { 50% { transform: scale(1.15); opacity: .7; } }
  @keyframes drift { 50% { transform: translateY(-6px); } }
  @media (prefers-reduced-motion: reduce) {
    /* --icon-reduced-motion: static-fallback-required — resting frames, loops off */
    .ambient, .orb { animation: none; }
  }
</style>
<script>
  // --icon-loop-policy: one-per-viewport-max — refuse a second ambient loop
  const ambientCount = document.querySelectorAll('.ambient').length;
  console.assert(ambientCount <= 1, 'loop policy: max one ambient animation per viewport');
  // WCAG 2.2.2 pause control for the 8s scene
  const btn = document.querySelector('.pause-btn'), scene = document.querySelector('.scene');
  btn.addEventListener('click', () => {
    const paused = scene.classList.toggle('is-paused');
    btn.setAttribute('aria-pressed', String(paused));
    btn.textContent = paused ? 'Resume animation' : 'Pause animation';
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every animated asset justifies itself against `var(--icon-animation-justification)` - feedback, loading, or celebration; idle decoration removed.
- [ ] Technique per asset is documented against `var(--icon-technique-choice)` - CSS for simple transforms, Lottie for scenes, SMIL absent from the codebase.
- [ ] Animated icons measure under `var(--icon-animated-icon-budget)` (<15KB) and Lottie scenes under `var(--icon-lottie-budget)` (<100KB), lazy-loaded.
- [ ] Every animation collapses to its static fallback under `var(--icon-reduced-motion)` - verified per asset, no exceptions.
- [ ] Viewport scan confirms `var(--icon-loop-policy)`: at most one ambient loop, and loops over 5s are exempted only with a pause control per `var(--icon-long-scene-pause)`.
- [ ] Motion-triggered state changes pair with text or `aria-live` per `var(--icon-state-announce)` - motion is never the only signal.
- [ ] Animations fire on `var(--icon-trigger-timing)` (state change), not on scroll-idle or timers.
