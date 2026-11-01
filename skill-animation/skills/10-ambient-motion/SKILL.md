---
name: ambient-motion
description: Slow, looping, atmospheric motion — aurora gradients, particles, blobs, and marquees that add depth and mood behind content without ever competing with it.
tags: [ambient, background, atmosphere, looping, decorative]
related: [illustration-lottie, scroll-animation, easing-timing]
---

# Animation Skill: Ambient & Background Motion

## 1. Definition

Ambient motion is decorative, loop-based movement that lives behind or around content: drifting gradient meshes, floating particles, slow blob morphs, subtle marquees, breathing glows. Its purpose is mood and perceived quality — not information. Unlike every other animation category in this set, ambient motion has no trigger and no user intent attached to it; it simply exists, on a loop, in the perceptual background. That fact defines its single hard constraint: **subordination**. Ambient layers must be slow, low-contrast, and pausable, and they must be the first thing disabled whenever attention becomes scarce — when the user starts a task, when the device is under load, or when reduced motion is requested.

## 2. Core Motion Principles

- **Slow by definition:** one loop is 8–30s; anything faster starts competing with content.
- **Low luminance delta:** ambient layers shift subtly (5–10% brightness/alpha movement); they should be missed if ignored.
- **Behind content, never around the task:** restrict to heroes, empty sections, login screens, and 404s — not forms or data tables.
- **Pause when off-screen and when hidden:** IntersectionObserver + document.visibilityState govern the loop.
- **One ambient layer per view:** a single hero background motion, not stacked particles + blobs + marquee.
- **GPU-cheap or nothing:** blur/transform/opacity on compositor layers; ambient must not cost frames on mid-tier devices.

## 3. Motion Tokens

| Token | Value | Notes |
|---|---|---|
| `--motion-ambient-loop` | `20000ms` | Default gradient/blob loop duration |
| `--motion-ambient-loop-fast` | `12000ms` | Maximum perceptible speed for ambient movement |
| `--motion-ambient-drift` | `translate3d(2%, -2%, 0)` | Typical drift range per loop iteration |
| `--motion-ambient-opacity` | `0.6` | Max opacity of ambient layer behind content |
| `--motion-marquee-speed` | `40px/s` | Marquee/ticker linear speed |

Consume them via the generated token file — reference `assets/css/ambient-motion.css` in your page and use the `var(--motion-ambient-*)` custom properties in component styles; never hardcode loop durations or drift distances inline.

## 4. Choreography

- **Hero-only budget:** ambient motion occupies the hero; after scroll, it is out of sight and paused.
- **Crossfade idle states:** when the UI goes idle (no interaction for 30s+), ambient may gradually become more present — never the reverse.
- **Celebrate on top:** celebration effects (confetti, bursts) are momentary overlays, not ambient loops.

## 5. Signature Patterns

- **Aurora gradient:** two/three large blurred radial-gradient blobs on translate3d/rotate loops at 15–25s.
- **Canvas particles:** 30–80 particles, cap DPR, pause on visibility, honor reduced motion.
- **CSS marquee:** duplicated track translateX(-50%) loop, pause on hover.

## 6. Real-World Use Cases

- **AI/Web3/streaming hero sections:** Aurora-style landing pages where atmosphere signals innovation.
- **Empty states, 404s, auth screens:** low-stakes moments that benefit from atmosphere without task pressure.
- **Brand moments:** event pages, campaign microsites, music/entertainment products that trade on vibe.

## 7. Combination Notes

**With other animation skills:**

- **Pairs well with `illustration-lottie`:** a static-quality Lottie illustration inside a slow aurora hero shares the same "atmosphere" budget — treat them as one ambient layer together.
- **Caution with `easing-timing`:** ambient loops run on linear or custom long-cycle curves; do not reuse UI easing tokens on 20s loops, they read as mechanical.
- **Caution with `entrance-exit`:** if the hero staggers in, start the ambient loop paused and fade it in last, so choreography outranks atmosphere.
- **Caution with `scroll-animation`:** ambient belongs in the hero only; the moment scroll reveals begin, the ambient layer should be out of view and paused — never run both on the same surface.
- **Caution with `reduced-motion`:** ambient is the *first* category removed under `prefers-reduced-motion`; build the static midpoint frame from day one, not as a patch.
- **Avoid `micro-interactions`:** a layer that constantly drifts behind a button the user is pressing muddies the press feedback signal.
- **Avoid `feedback-confirmation`:** toasts and checkmarks must read instantly against a still background; ambient motion behind them steals the attention the feedback earned.
- **Avoid `page-transitions`:** route changes need spatial clarity; a moving background during navigation doubles the motion the eye must parse.
- **Avoid `loading-states`:** skeletons and spinners already signal waiting; ambient movement behind them fabricates activity that masks the real state.
- **Avoid `gesture-drag`:** drag tracking requires the finger and the element to be the only motion on screen; background drift reads as lag.
- **Avoid `data-animation`:** charts and count-ups demand stillness for comprehension; ambient motion behind data is a comprehension tax.

**With design styles (companion repo `skill-ui-ux`):**

- **Good with `aurora-ui`:** this is the style's defining ingredient — drifting multi-color gradients over dark glass.
- **Good with `glassmorphism`:** blurred translucent panels sit naturally over slow-moving gradient backdrops.
- **Good with `maximalism`:** rich atmosphere is welcome, but still honor the one-layer-per-view budget.
- **Caution with `minimalism`:** ambient motion can be the *only* decoration on a minimal page — keep it nearly invisible or drop it.
- **Caution with `flat-design`:** flat design's discipline conflicts with atmospheric depth; if used, keep it strictly below the fold's task content.

## 8. Anti-Patterns

- **Ambient over data:** looping backgrounds behind forms, tables, or reading surfaces sabotage the primary task
- **Fast ambient:** 2-4s loops that flicker in peripheral vision; ambient caught by peripheral vision is ambient too loud
- **Battery arson:** full-screen blur+filter animations running at 60fps on mobile for decoration
- **Stacked layers:** particles over blobs over marquee - two or more ambient layers is noise, not atmosphere

### Accessibility Notes

Ambient motion is the **highest-risk decorative category for vestibular triggers and the first thing removed** under `prefers-reduced-motion`. The strategy is full removal with a static substitute: render the loop's **midpoint frame** as a static image or gradient so the composition keeps its mood without movement — never keep it looping at a slower speed. In `assets/css/ambient-motion.css`, the global override under `@media (prefers-reduced-motion: reduce)` collapses all animation/transition durations to 1ms with `animation-iteration-count: 1`, which freezes ambient loops after one frame; components should additionally check `matchMedia('(prefers-reduced-motion: reduce)')` at init and skip starting Canvas/JS loops entirely. Also pause ambient layers when `document.visibilityState` is hidden and when the hero scrolls out of view — battery drain is an accessibility issue for users on low-power devices.

## 9. Code Examples

### Example 1 — Aurora gradient hero (CSS only)

Tokens: `assets/css/ambient-motion.css`

```html
<section class="hero">
  <div class="ambient" aria-hidden="true"></div>
  <div class="content">
    <h1>Ship motion that feels alive</h1>
    <p>Slow, atmospheric, and never in the way.</p>
  </div>
</section>
<style>
.hero { position: relative; overflow: hidden; min-height: 480px;
        display: grid; place-items: center; background: #0b0f1a; }
.ambient {
  position: absolute; inset: -20%;           /* oversized so blurred edges never show */
  opacity: var(--motion-ambient-opacity);    /* 0.6 max */
  background:
    radial-gradient(40% 50% at 30% 40%, #6C63FF 0%, transparent 70%),
    radial-gradient(35% 45% at 70% 60%, #22D3EE 0%, transparent 70%);
  filter: blur(60px);
  animation: ambient-drift var(--motion-ambient-loop) linear infinite; /* 20000ms */
}
@keyframes ambient-drift {
  0%   { transform: translate3d(0, 0, 0) rotate(0deg); }
  50%  { transform: translate3d(2%, -2%, 0) rotate(4deg); } /* --motion-ambient-drift range */
  100% { transform: translate3d(0, 0, 0) rotate(0deg); }
}
.content { position: relative; z-index: 1; color: #fff; text-align: center; }
</style>
<script>
// Pause when the hero leaves the viewport or the tab is hidden
const ambient = document.querySelector('.ambient');
const setPlay = run => ambient.style.animationPlayState = run ? 'running' : 'paused';
new IntersectionObserver(([e]) => setPlay(e.isIntersecting)).observe(ambient);
document.addEventListener('visibilitychange', () => setPlay(!document.hidden));
</script>
```

### Example 2 — Reduced-motion-aware Canvas particles

Tokens: `assets/css/ambient-motion.css`

```html
<canvas class="particles" width="600" height="320" aria-hidden="true"></canvas>
<script>
const canvas = document.querySelector('.particles');
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const dpr = Math.min(devicePixelRatio, 1.5); // cap DPR — GPU-cheap or nothing

if (reduceMotion) {
  // Static midpoint frame: draw once, never loop.
  drawFrame(0.5);
} else {
  const particles = Array.from({ length: 40 }, () => ({   // 30-80 particles
    x: Math.random() * canvas.width, y: Math.random() * canvas.height,
    r: 1 + Math.random() * 2, vy: -(0.05 + Math.random() * 0.1),
  }));
  let running = false, raf;
  function tick() {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.globalAlpha = 0.6;                                  // --motion-ambient-opacity
    for (const p of particles) {
      p.y += p.vy; if (p.y < 0) p.y = canvas.height;
      ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 7); ctx.fill();
    }
    raf = requestAnimationFrame(tick);
  }
  function drawFrame(t) { /* single-frame render for the static fallback */ }
  new IntersectionObserver(([e]) => {
    const shouldRun = e.isIntersecting && !document.hidden;
    if (shouldRun && !running) { running = true; tick(); }
    else if (!shouldRun && running) { running = false; cancelAnimationFrame(raf); }
  }).observe(canvas);
}
</script>```

## 10. Implementation Checklist

- [ ] Every ambient loop runs 8–30s (`--motion-ambient-loop` to `--motion-ambient-loop-fast`); nothing faster ships.
- [ ] Exactly one ambient layer per view, at `--motion-ambient-opacity` or lower, placed behind content with `z-index`.
- [ ] The loop pauses via IntersectionObserver when off-screen and via `visibilitychange` when the tab is hidden.
- [ ] Only compositor properties animate (`transform`, `opacity`); blur is baked, not animated, on mobile.
- [ ] Under `prefers-reduced-motion`, the ambient layer renders a static midpoint frame — verified with the OS setting enabled.
- [ ] Ambient never appears over forms, tables, or reading surfaces — hero, empty states, auth, and 404s only.
- [ ] `--motion-marquee-speed` (40px/s) respected for any ticker, with pause-on-hover and pause-on-focus.
