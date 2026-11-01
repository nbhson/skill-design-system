---
name: illustration-lottie
description: Designer-authored, frame-perfect motion delivered as data — Lottie and Rive for mascots, empty states, onboarding stories, and celebrations, governed by size budgets and playback control.
tags: [lottie, rive, illustration, character, celebration]
related: [feedback-confirmation, loading-states, ambient-motion]
---

# Animation Skill: Illustration & Lottie

## 1. Definition

Illustration animation brings designer-authored, frame-perfect motion into the product as data: Lottie JSON exported from After Effects via Bodymovin, or Rive state machines. Unlike code-driven motion, the timeline is authored in a design tool — which makes it the ideal vehicle for character performance, mascots, onboarding stories, empty states, and celebration moments that hand-rolled CSS cannot match. The trade-off is that the animation arrives as an opaque blob the code did not create, so the engineering work is **governance**: file-size budgets, playback control from code, state-machine wiring for interactivity, and accessibility for content that otherwise carries no semantic meaning.

## 2. Core Motion Principles

- **Buy motion with bytes knowingly:** Lottie budgets — icons <30KB, loaders <80KB, hero moments <300KB; Rive often beats both.
- **Engine controls playback:** play/pause/speed/segment must be drivable from code; never embed a timeline you cannot stop.
- **Design for interruption:** celebrations can be cut at any point without visual brokenness.
- **Loop with intent:** loaders loop seamlessly; narrative animations end on a held final frame.
- **State machines over timelines for interactive characters:** Rive state machines handle input-driven transitions natively.
- **Animation is never the message:** pair every illustration with real text — the animation alone carries no meaning.

## 3. Motion Tokens

| Token | Value | Notes |
|---|---|---|
| `--motion-icon-budget` | `30KB` | Max Lottie size for icon-scale animation |
| `--motion-loader-budget` | `80KB` | Max size for loading/processing animation |
| `--motion-hero-budget` | `300KB` | Max size for hero/onboarding animation |
| `--motion-playback-speed` | `1.0` | Default rate; celebrations accept 0.8–1.2 |
| `--motion-celebration-duration` | `2000ms` | Confetti/success moments; cut after completion |

Consume them via the generated token file — reference `assets/css/illustration-lottie.css` and read the budget custom properties (`var(--motion-loader-budget)`, etc.) in build scripts and player setup code so size gates stay in sync with the spec.

## 4. Choreography

- **Empty-state flow:** illustration plays entrance once → settles into gentle loop → CTA fades in beneath.
- **Success handoff:** Lottie celebration plays 1–2s while the real content is already interactive behind it.
- **Onboarding sequences:** per-slide loops with swipe-driven segment control (play segment i on view).

## 5. Signature Patterns

- **lottie-web player with autoplay=false:** controlled segments via playSegments([start, end]).
- **Rive state machine:** bind inputs (hover/tap/progress) to state transitions instead of multiple files.
- **Lazy mount:** instantiate the player only when the container intersects the viewport.

## 6. Real-World Use Cases

- **Empty states, error pages, onboarding tours:** narrative moments where a scene teaches what to do next.
- **Brand mascots and character-driven products:** duolingo-style personalities that reward interaction.
- **Premium loaders and processing indicators:** loading moments that express brand craft rather than a bare spinner.

## 7. Combination Notes

**With other animation skills:**

- **Pairs well with `feedback-confirmation`:** a Lottie checkmark or confetti burst is the premium version of a success confirmation; keep it under `--motion-celebration-duration`.
- **Pairs well with `ambient-motion`:** a looping mascot or blob illustration can serve as the view's single ambient layer — share the one-layer budget.
- **Pairs well with `scroll-animation`:** scrub Lottie segments against scroll progress for scrollytelling scenes.
- **Pairs well with `loading-states`:** a branded Lottie loader replaces a generic spinner for waits >1s, on top of a truthful skeleton.
- **Caution with `easing-timing`:** easing lives inside the exported file; don't wrap the container in additional CSS transitions that fight the baked curve.
- **Caution with `entrance-exit`:** the Lottie's own entrance already choreographs appearance; do not double-animate the container fading and translating on top.
- **Caution with `page-transitions`:** don't fire a celebration or narrative clip mid-navigation — one motion story at a time.
- **Caution with `gesture-drag`:** interactive playback needs Rive state machines, not raw timelines; plain Lottie cannot follow a finger.
- **Caution with `data-animation`:** never let an illustrative chart animation stand in for real chart rendering; data must come from the data layer.
- **Caution with `reduced-motion`:** every Lottie needs a static exported frame as its fallback — ship it alongside the JSON.
- **Caution with `micro-interactions`:** Lottie is too heavy for hover/press feedback; use it for moments, not for control states.

**With design styles (companion repo `skill-ui-ux`):**

- **Good with `claymorphism`:** soft, rounded character illustration matches the tactile 3D feel.
- **Good with `maximalism`:** expressive, dense motion is part of the style's vocabulary.
- **Good with `retro`:** playful character animation amplifies nostalgic visual language.
- **Caution with `minimalism`:** a large animated illustration is a focal point; in minimal layouts keep it small, monochrome, or absent.
- **Caution with `brutalism-ui`:** raw, unpolished aesthetics clash with glossy After Effects output — match render style or skip.

## 8. Anti-Patterns

- **Megabyte heroes:** shipping multi-MB Lottie files for above-the-fold decoration
- **Unstoppable autoplay:** ambient character loops that cannot be paused and run forever in view
- **Animation as copy:** relying on the illustration alone to explain state (which error? what next?) with no text
- **Design-tool drift:** exporting revisions without a size/duration budget gate, regressing performance silently

### Accessibility Notes

A Lottie file is opaque to assistive technology, so accessibility must be added around it. **Fallback first:** replace narrative/celebration animation with a **static exported frame** (SVG/PNG) of the illustration under `prefers-reduced-motion`; loaders swap to a simple opacity pulse instead of playback. In `assets/css/illustration-lottie.css` the global override collapses animation durations to 1ms with `animation-iteration-count: 1` under `@media (prefers-reduced-motion: reduce)`, and the player should also check `matchMedia('(prefers-reduced-motion: reduce)')` at init to swap in the static frame rather than instantiate playback at all. Beyond motion: mark decorative illustrations `aria-hidden="true"`, give meaningful ones a text alternative, and always pair the visual with real copy — the principle "animation is never the message" is an accessibility rule as much as a design one.

## 9. Code Examples

### Example 1 — Governed Lottie empty state with lazy mount

Tokens: `assets/css/illustration-lottie.css`

```html
<div class="empty-state">
  <div class="lottie-mount" data-src="/anim/empty-box.json" role="img"
       aria-label="No projects yet"></div>
  <p>No projects yet. Create your first one to get started.</p> <!-- animation is never the message -->
  <button class="cta">New project</button>
</div>
<style>
.empty-state { display: grid; justify-items: center; gap: 12px; padding: 48px; }
.lottie-mount { width: 200px; height: 200px; }
.cta { opacity: 0; transition: opacity 240ms ease-out; } /* fades in after the loop settles */
.empty-state.settled .cta, .empty-state.settled p { opacity: 1; }
@media (prefers-reduced-motion: reduce) { .cta { opacity: 1; } }
</style>
<script type="module">
import lottie from 'lottie-web';

async function mount(el) {
  const res = await fetch(el.dataset.src);
  const bytes = (await res.arrayBuffer()).byteLength;
  const budget = parseFloat(
    getComputedStyle(document.documentElement).getPropertyValue('--motion-loader-budget')
  ); // 80KB gate — design-tool drift guard
  if (bytes > budget * 1024) { console.warn(`Lottie ${el.dataset.src} exceeds budget: ${bytes}B`); return; }

  const anim = lottie.loadAnimation({
    container: el, renderer: 'svg', loop: true, autoplay: false, // engine controls playback
    animationData: await res.json(),
  });

  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    // Static final frame instead of playback
    anim.playSegments([anim.totalFrames - 1, anim.totalFrames], true); anim.pause();
    el.closest('.empty-state').classList.add('settled');
    return;
  }
  anim.playSegments([0, 24], true);                       // entrance segment, once
  anim.addEventListener('complete', () => {
    anim.playSegments([24, 60], true);                    // settle into gentle loop
    el.closest('.empty-state').classList.add('settled');  // CTA fades in beneath
  });
}

const mount1 = document.querySelector('.lottie-mount');
new IntersectionObserver(([e], io) => {                   // lazy mount pattern
  if (e.isIntersecting) { io.disconnect(); mount(e.target); }
}).observe(mount1);
</script>
```

### Example 2 — Celebration with a hard stop

Tokens: `assets/css/illustration-lottie.css`

```html
<div class="success">
  <div id="celebration" aria-hidden="true"></div>
  <p>Publish successful</p>
</div>
<style>
.success { position: relative; display: grid; place-items: center; padding: 40px; }
#celebration { width: 160px; height: 160px; }
</style>
<script type="module">
import lottie from 'lottie-web';
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const anim = lottie.loadAnimation({
  container: document.getElementById('celebration'),
  renderer: 'svg', loop: false, autoplay: false,
  path: '/anim/confetti.json',
});
anim.setSpeed(1.0); // --motion-playback-speed
if (reduceMotion) {
  anim.goToAndStop(anim.totalFrames, true); // hold the static final frame — no playback
} else {
  anim.play();
  // Celebration-duration hard stop: cut after completion, content already interactive behind it.
  setTimeout(() => anim.destroy(), 2000);   // --motion-celebration-duration
}
</script>
```

## 10. Implementation Checklist

- [ ] Every Lottie file passes its budget gate at build time: icon <30KB, loader <80KB, hero <300KB (`--motion-*-budget` tokens).
- [ ] Player is instantiated with `autoplay: false` and playback (play/pause/speed/segments) is drivable from code.
- [ ] Static exported frames ship next to every animation and are swapped in under `prefers-reduced-motion`.
- [ ] Celebrations hard-stop after `--motion-celebration-duration` (2000ms) and never block the underlying content.
- [ ] Illustrations are `aria-hidden` when decorative and paired with real explanatory text when meaningful.
- [ ] Players lazy-mount on viewport intersection and destroy/stop when out of view.
- [ ] Rive state machines (not multiple files) handle any input-driven character behavior.
