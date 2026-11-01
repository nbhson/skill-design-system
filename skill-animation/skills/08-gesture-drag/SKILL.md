---
name: gesture-drag
description: Direct manipulation - drag, swipe, pull-to-refresh, fling with momentum and springs - motion that stays glued to the finger and lands with physics.
tags: [gesture, drag, physics, springs, touch]
related: [page-transitions, data-animation, feedback-confirmation]
---

# Animation Skill: Gesture & Drag Physics

## 1. Definition

Gesture animation is motion under direct manipulation: the element tracks the pointer 1:1 while active — no easing, because the finger is the easing — then resolves on release with physics: momentum fling, spring snap-back, or velocity-based dismissal. The distinction from every other category is fundamental: during the gesture, animation is not time-based at all; it is input-based. All time-based motion happens after release, when springs take over and translate the last known position and velocity into a physical-feeling resolution. This split — raw tracking while touched, spring physics on release — is what makes drag interfaces feel like handling real objects instead of watching rendered frames.

## 2. Core Motion Principles

- **1:1 tracking during drag:** the element follows the pointer exactly; no lag, no easing, no rubber-band delay beyond intentional edge overscroll.
- **Velocity decides the outcome:** dismissal at ~30-50% distance OR sufficient fling velocity, whichever comes first.
- **Resolve with springs, not durations:** release motion uses spring physics (stiffness/damping) so it adapts to the release velocity.
- **Always give a home:** every draggable returns to a snap point or completes a dismissal - never rest mid-travel.
- **Show the outcome during the gesture:** alpha/overlay hints as thresholds cross (row turns red, card tilts) so release is confirmation, not surprise.
- **Interrupt everything:** a new touch during resolve must grab the current position and continue from there.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Dismiss threshold | `--motion-dismiss-threshold` | `0.4` | 40% of travel distance triggers dismissal |
| Fling velocity | `--motion-fling-velocity` | `500px/s` | Release velocity that forces the action regardless of distance |
| Spring (snap) | `--motion-spring-snap` | `stiffness 300, damping 30` | Return-to-home spring |
| Spring (settle) | `--motion-spring-settle` | `stiffness 170, damping 26` | Settle spring for completed dismissals/reflow |
| Rubber-band factor | `--motion-rubber-band` | `0.55` | Overscroll resistance factor at edges |
| Drag tilt | `--motion-drag-tilt` | `rotate(4deg)` | Max tilt while dragging cards |

Consume tokens by linking `assets/css/gesture-drag.css` and reading the custom properties: `--motion-dismiss-threshold` and `--motion-rubber-band` feed your pointer math in JS, while `--motion-drag-tilt` maps to a CSS transform on the dragging element. The spring tokens are physical specifications (stiffness/damping pairs) rather than CSS values — interpret them in your spring solver or a library such as Framer Motion / React Spring.

## 4. Choreography

- **Pull-to-refresh:** drag stretches a spinner arc; past threshold it snaps to armed state; release triggers refresh + settle.
- **Swipe-to-dismiss:** card follows finger, background intent layer fades in with progress, release springs out or snaps back.
- **Reorder drag:** dragged item lifts (scale+shadow), neighbors open the gap with the settle spring, drop settles with a soft bounce.

## 5. Signature Patterns

- **Pointer capture + transform:** track `pointermove` deltas into `translate3d`; commit on `pointerup` with velocity sampling.
- **Velocity sampling:** keep the last ~100ms of pointer positions to compute release velocity robustly.
- **Spring resolution:** Framer Motion / React Spring animate from current position+velocity to the target snap point.

## 6. Real-World Use Cases

- **Mobile lists:** swipe actions (archive, delete), reordering, dismissible cards and notifications.
- **Maps, sliders, scrubbers, carousels** - any continuous-value control.
- **Pull-to-refresh, bottom sheets** with drag-to-expand/collapse, gallery paging.

## 7. Combination Notes

- With other animation skills:
  - **Pairs well with `page-transitions`:** an edge-swipe or drag on a card can hand off directly into the shared-element route transition — gesture as navigation input.
  - **Pairs well with `data-animation`:** drag scrubbing a timeline or slider should update chart values in real time, interpolating at `--motion-update-duration` semantics.
  - **Pairs well with `feedback-confirmation`:** the dismissal outcome (undo toast, confirmation) must follow the fling immediately; the gesture resolves into a feedback beat.
  - **Pairs well with `loading-states`:** pull-to-refresh is a loading pattern at heart — release hands off to the refresh spinner, and content arrives through the standard loading handoff.
  - **Caution with `easing-timing`:** never apply a duration curve while the finger is down; reserve duration/easing tokens strictly for the post-release resolution.
  - **Caution with `micro-interactions`:** a draggable already has pressed/lifted states from the gesture itself — don't stack a hover lift on top, or the element responds to two masters.
  - **Caution with `entrance-exit`:** dismissal and entrance share the same slot; if an item can be dragged away, its removal animation should come from the drag resolution, not a separate exit choreography.
  - **Caution with `scroll-animation`:** both listen to continuous input; decide ownership up front (a draggable card is not also a scroll-scrubbed element) or the gesture fight will jank.
  - **Caution with `reduced-motion`:** keep 1:1 tracking (it is user-controlled and safe) but strip springs, tilt, and embellishments from the release (see Accessibility Notes).
  - **Caution with `illustration-lottie`:** Rive state machines can drive gesture-driven characters, but only bind one gesture → one state machine input; don't route the same pointer through two systems.
  - **Avoid `ambient-motion`:** a draggable must be glued to input at all times; a moving ambient layer behind it destroys the "handling a real object" feel and competes for the same frame budget.
- With design styles (companion repo `skill-ui-ux`):
  - **Good affinity:** glassmorphism, neumorphism, claymorphism — tactile, dimensional styles where cards visibly lift, tilt, and press like physical objects.
  - **Caution:** class-morphism and retro — skeuomorphic chrome and retro textures invite decoration on the drag surface (heavy shadows, bouncy exaggeration) that quickly overshoots the 4deg tilt and snap physics.

## 8. Anti-Patterns

- **Eased tracking:** applying time-based easing while the finger is down creates lag that reads as a broken touch screen
- **Keyboard-only dismissal:** swipe actions with no visible buttons duplicate; gesture must augment, not replace, affordances
- **No velocity memory:** slow-dragging past 39% fails while a fast flick at 10% succeeds - without velocity both feel arbitrary
- **Mid-air rest:** elements stopping between snap points after release because durations replaced springs

### Accessibility Notes

The gesture itself is user-controlled, so 1:1 tracking is kept under `prefers-reduced-motion: reduce` — the finger position is the animation, and removing it would break the interaction entirely. What changes is the release: replace post-release springs with fast, direct transitions (shortest path, no bounce), and remove embellishments such as tilt, rubber-band overscroll visuals, and parallax. The threshold overlay that fades in with progress becomes a static color change at the threshold crossing. The global override in `assets/css/gesture-drag.css` collapses `animation-duration`/`transition-duration` to 1ms, so any duration-based fallback resolves instantly. Also honor the anti-pattern above: every swipe action must have a visible button equivalent — gestures augment affordances, never replace them — and draggable components must be operable via keyboard (arrow keys + space/enter) with the same snap/dismiss outcomes.

## 9. Code Examples

### Example 1 — Swipe-to-dismiss with velocity sampling

Tokens: `assets/css/gesture-drag.css`

```html
<ul class="list">
  <li class="row"><span>Archive me</span><button class="undo-btn" hidden>Undo</button></li>
</ul>
<style>
  .row {
    position: relative; overflow: hidden;
  }
  .row .content {
    touch-action: pan-y;                 /* let the browser own vertical scroll */
    transition: transform var(--motion-fling-velocity) ; /* only for keyboard/no-JS path */
  }
  .row.dragging .content { transition: none; }  /* 1:1 tracking: no easing while down */
  .row.dismissed { transform: translateX(-110%); }
  @media (prefers-reduced-motion: reduce) {
    .row .content { transition: none; }
    .row { transition: opacity 1ms; }    /* release resolves via shortest path */
  }
</style>
<script>
  const DISMISS = 0.4, FLING = 500, TILT = 4; // tokens: threshold, px/s velocity, max tilt degrees
  for (const row of document.querySelectorAll('.row')) {
    const content = row.querySelector('.content');
    let startX = 0, dx = 0, dragging = false;
    const history = [];                        // last ~100ms of (t, x) samples for velocity

    row.addEventListener('pointerdown', (e) => {
      dragging = true; startX = e.clientX; dx = 0;
      row.classList.add('dragging');
      row.setPointerCapture(e.pointerId);
      history.length = 0; history.push([performance.now(), e.clientX]);
    });
    row.addEventListener('pointermove', (e) => {
      if (!dragging) return;
      dx = e.clientX - startX;
      history.push([performance.now(), e.clientX]);
      while (history.length > 2 && history[0][0] < performance.now() - 100) history.shift();
      content.style.transform = `translate3d(${dx}px, 0, 0) rotate(${Math.max(-TILT, Math.min(TILT, dx / 20))}deg)`;
      row.style.background = Math.abs(dx) > DISMISS * row.offsetWidth ? 'tomato' : ''; // intent hint
    });
    row.addEventListener('pointerup', (e) => {
      dragging = false;
      row.classList.remove('dragging');
      const [t0, x0] = history[0] ?? [performance.now(), e.clientX];
      const velocity = (e.clientX - x0) / Math.max(1, performance.now() - t0) * 1000;
      if (Math.abs(dx) > DISMISS * row.offsetWidth || Math.abs(velocity) > FLING) {
        row.classList.add('dismissed');        // threshold OR fling completes the dismissal
      } else {
        content.style.transform = '';          // spring snap-back home
      }
    });
  }
</script>
```

> **Keyboard/no-JS path:** every swipe action also ships a visible button; pressing `Delete`/`Backspace` on a focused row toggles the same `.dismissed` class (transition approximating the `--motion-spring-settle` spring), so gestures augment affordances rather than replace them.

## 10. Implementation Checklist

- [ ] Zero easing while the pointer is down — element tracks 1:1 via `translate3d`; easing exists only after release.
- [ ] Release decision uses both threshold (`~40%` travel) and fling velocity (`~500px/s`), sampled from the last ~100ms of pointer history.
- [ ] Every drag resolves to a snap point or a completed dismissal — the element never rests mid-travel.
- [ ] Intent overlays (color, tilt, alpha) preview the outcome during the drag so release confirms rather than surprises.
- [ ] Interruptible: a new `pointerdown` during resolve grabs the current position and continues from there.
- [ ] Every gesture has a visible button and keyboard equivalent; gestures augment affordances, not replace them.
- [ ] `prefers-reduced-motion: reduce` keeps 1:1 tracking but replaces springs with the shortest direct path and removes tilt.
