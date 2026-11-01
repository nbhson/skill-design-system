---
name: reduced-motion
description: The accessibility layer of motion — a prefers-reduced-motion strategy built on vestibular safety, focus management, and per-category fallbacks that keep meaning while removing movement.
tags: [accessibility, prefers-reduced-motion, vestibular, fallback, wcag]
related: [easing-timing, ambient-motion, scroll-animation]
---

# Animation Skill: Reduced Motion & Accessibility

## 1. Definition

Reduced motion is not the removal of animation — it is the **substitution of safe motion**. The `prefers-reduced-motion: reduce` media query signals vestibular sensitivity: nausea, dizziness, and discomfort triggered by large, spinning, or parallax movement. Every animation skill in this set declares its fallback through this layer, making it the contract that turns motion from a liability into a first-class mode. The professional pattern is a three-tier strategy — remove what harms, replace what can be translated into a safer medium, retain what is already safe — so that users who opt out of movement still get every state change, every confirmation, and every piece of feedback, just delivered through opacity, color, icon, and text instead of travel and spin.

## 2. Core Motion Principles

- **Three tiers, applied in order:** REMOVE spinning/parallax/large travel; REPLACE travel with opacity+color; RETAIN short small fades as feedback.
- **Never remove meaning:** state changes must stay perceivable — swap the medium (movement → color/icon/text), not the message.
- **Respect the media query globally:** one global rule + per-component overrides beats scattered per-component queries.
- **Movement threshold heuristics:** translations >24px, rotations, scale >1.15, and all infinite loops are "large motion".
- **Kinetic payoffs stay instant:** after removing an entrance animation, elements are simply present — no delayed appearance.
- **Test with the setting on:** reduced motion is a first-class mode, QA it like dark mode, not a bug caveat.

## 3. Motion Tokens

| Token | Value | Notes |
|---|---|---|
| `--motion-rm-duration` | `1ms` | Replacement duration for removed large motion |
| `--motion-rm-fade` | `150ms` | Max allowed opacity fade in reduced mode |
| `--motion-rm-travel` | `0px` | All translation distances collapse to 0 |
| `--motion-rm-loop-policy` | `paused` | All infinite loops pause or play once |

Consume them via the generated token file — reference `assets/css/reduced-motion.css` and use the `var(--motion-rm-*)` custom properties inside your `@media (prefers-reduced-motion: reduce)` blocks, so component fallbacks stay in lockstep with the global contract.

## 4. Choreography

- **Global override pattern:** `@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 1ms !important; transition-duration: 1ms !important; scroll-behavior: auto !important } }` then re-enable specific safe fades.
- **JS awareness:** `matchMedia('(prefers-reduced-motion: reduce)')` gates springs, parallax, and particle systems at init time.
- **Live regions pair with toast motion:** screen-reader users get announcements regardless of visual motion.

## 5. Signature Patterns

- **Fade-replacement:** translateY(16px) entrance becomes opacity-only at rm-fade.
- **Static ambient frame:** render the loop's midpoint as a static gradient/image.
- **Physics bypass:** springs and drags resolve with direct duration-fast transitions under the flag.

## 6. Real-World Use Cases

- **Every product shipping motion:** the fallback layer is mandatory, not optional.
- **Health, government, education, enterprise:** accessibility-critical contexts where vestibular safety is a compliance requirement.
- **Design system motion specs:** defining per-component reduced behavior alongside each component's full-motion spec.

## 7. Combination Notes

**With other animation skills:**

Reduced motion is a **constraint layer, not a feature** — it does not "combine" with other skills; it *applies to* every one of them. Each skill declares what changes under the flag, and this guide defines the contract they all inherit:

- **`easing-timing` (the one "good" pairing):** duration and easing tokens survive reduced motion — durations are shortened rather than states removed, and this skill's `--motion-rm-duration` / `--motion-rm-fade` plug directly into that token hierarchy.
- **Caution with `ambient-motion`:** the strictest override — ambient layers are removed entirely and replaced with a static midpoint frame.
- **Caution with `scroll-animation`:** parallax and scrub are vestibular triggers; all scroll-scrubbed effects show their end state.
- **Caution with `gesture-drag`:** 1:1 tracking stays (it is user-controlled), but release springs become direct fast transitions and tilt is removed.
- **Caution with `data-animation`:** charts render final values immediately; count-ups and draw-ins are skipped, updates flash once.
- **Caution with `micro-interactions`:** scale and translate effects swap to background/border color transitions at instant duration.
- **Caution with `entrance-exit`:** reveals keep their timing but lose displacement and stagger — one short opacity fade for the group.
- **Caution with `page-transitions`:** slides and shared-element morphs collapse to a short crossfade so navigation still feels connected.
- **Caution with `feedback-confirmation`:** outcome signals (icon, color, text) are kept; shakes and travel become instant position plus a short fade.
- **Caution with `loading-states`:** shimmer/spin loops stop; skeletons become static blocks or a low-amplitude 1–2 Hz opacity pulse.
- **Caution with `illustration-lottie`:** narrative and celebration playback is replaced by the static final frame.

**With design styles (companion repo `skill-ui-ux`):**

- **Good with `minimalism`:** sparse layouts have little motion to strip, so the reduced experience is nearly identical to the full one.
- **Good with `flat-design`:** flat design's no-depth discipline already avoids the parallax and 3D movement this layer must remove.
- **Caution with `aurora-ui`:** its identity is built on drifting gradients — the static-frame fallback must carry the mood without the drift.
- **Caution with `maximalism`:** dense, expressive styles tend to accumulate decorative motion; audit every layer under the flag.
- **Caution with `retro`:** playful bounce and marquee effects need explicit per-component fallbacks or they regress to full motion.

## 8. Anti-Patterns

- **Kill-switch only:** disabling all animation including state feedback leaves users without any change signal
- **Query amnesia:** CSS honors the media query but JS-driven springs/particles ignore it
- **Reduced = invisible:** hiding elements instead of animating them, so content 'jumps in' with no continuity at all
- **Set-and-forget:** no QA pass with the OS setting enabled, so regressions ship silently

### Accessibility Notes

The heart of this skill is the **three-tier REMOVE / REPLACE / RETAIN strategy**, applied in order to every motion effect in the product:

1. **REMOVE** everything in the "large motion" class — spinning loaders, parallax layers, ambient loops, translations >24px, rotations, scale >1.15, and every infinite loop. Under `--motion-rm-loop-policy: paused`, loops either pause or play once; there is no sustained movement. Removed effects pay off instantly: the element is simply present, at `--motion-rm-travel: 0px`.
2. **REPLACE** motion whose *meaning* must survive with a safer medium: travel becomes opacity, state changes become color/icon/text swaps, springs become direct transitions. The replacement fade is capped at `--motion-rm-fade` (150ms) — short and small enough to be vestibularly safe — and removed large motion collapses to `--motion-rm-duration` (1ms).
3. **RETAIN** what is already safe: short, small opacity fades and color changes remain as feedback, because the failure mode to avoid is the "kill-switch" anti-pattern — a UI with no change signal at all.

Enforce it globally in `assets/css/reduced-motion.css`: the `@media (prefers-reduced-motion: reduce)` block collapses all animation and transition durations to 1ms with `animation-iteration-count: 1` and `scroll-behavior: auto`, then per-component rules re-enable the safe fades above `--motion-rm-fade`. JavaScript must gate at init with `matchMedia('(prefers-reduced-motion: reduce)')` — CSS alone cannot stop a Canvas particle system or a spring physics loop (see the "Query amnesia" anti-pattern). Finally, pair any motion-based feedback with live-region announcements and run a full QA pass with the OS setting enabled.

## 9. Code Examples

### Example 1 — Global override with re-enabled safe fades

Tokens: `assets/css/reduced-motion.css`

```html
<div class="toast" role="status">Saved</div>
<style>
.toast {
  transform: translateY(16px); opacity: 0;       /* full-motion entrance */
  transition: transform 240ms cubic-bezier(0.2, 0, 0, 1), opacity 240ms;
}
.toast.show { transform: translateY(0); opacity: 1; }

/* ---- global contract: assets/css/reduced-motion.css ---- */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 1ms !important;             /* --motion-rm-duration */
    transition-duration: 1ms !important;
    animation-iteration-count: 1 !important;        /* --motion-rm-loop-policy: paused */
    scroll-behavior: auto !important;
  }
  /* RETAIN tier: re-enable the one safe fade for this component */
  .toast {
    transform: none;                                /* --motion-rm-travel: 0px */
    transition: opacity var(--motion-rm-fade) ease-out; /* 150ms opacity-only */
  }
}
</style>
<script>
const toast = document.querySelector('.toast');
requestAnimationFrame(() => toast.classList.add('show')); // meaning kept, medium swapped
</script>
```

### Example 2 — JS gating for a particle/spring system

Tokens: `assets/css/reduced-motion.css`

```html
<canvas id="fx" width="400" height="200" aria-hidden="true"></canvas>
<script>
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
const MAX_TRAVEL = 24; // translations >24px are "large motion" by the threshold heuristic

function startParticles() {
  if (reduceMotion.matches) {
    renderStaticFrame();     // REMOVE tier: draw one midpoint frame, never loop
    return;
  }
  requestAnimationFrame(loop); // full-motion path
}

function resolveDrag({ x, y, velocity }) {
  if (reduceMotion.matches) {
    // Physics bypass (RETAIN tier): direct fast transition, no spring
    element.style.transition = 'transform 150ms ease-out'; // ~--motion-rm-fade
    element.style.transform = `translate(${x}px, ${y}px)`;
  } else {
    spring.animate({ from: current, to: { x, y }, velocity });
  }
}

// Listen for live changes — users can toggle the setting mid-session.
reduceMotion.addEventListener('change', e => e.matches ? haltAllLoops() : startParticles());
startParticles();
</script>
```

## 10. Implementation Checklist

- [ ] The global override from `assets/css/reduced-motion.css` ships site-wide before any component animation lands.
- [ ] Every component defines a three-tier fallback: REMOVE large motion, REPLACE with opacity/color, RETAIN a ≤150ms fade.
- [ ] All JS-driven motion (springs, Canvas, parallax, Lottie) gates on `matchMedia('(prefers-reduced-motion: reduce)')` at init and on `change`.
- [ ] No infinite loop survives the flag: `--motion-rm-loop-policy` holds — loops pause or play once, never sustain.
- [ ] State changes remain perceivable via color, icon, or text — never hide elements as the "reduced" behavior.
- [ ] Motion feedback that carries meaning is paired with live-region announcements for screen readers.
- [ ] A QA pass with the OS "reduce motion" setting enabled is part of every motion PR's definition of done.
