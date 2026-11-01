---
name: scroll-animation
description: Motion tied to scroll position - parallax, reveals, progress indicators, and sticky choreography - driven by the user's own input, not the clock.
tags: [scroll, parallax, reveal, scrubbing, progress]
related: [data-animation, illustration-lottie, entrance-exit]
---

# Animation Skill: Scroll-Driven Animation

## 1. Definition

Scroll-driven animation maps scroll progress to visual state: the timeline is the scrollbar, not the clock. Scrub effects, entrance reveals, parallax layers, and progress indicators all derive their state from where the user has scrolled, which makes the category inherently user-controlled — the user drags the timeline themselves. This gives scroll motion a distinctive character: it must feel like a physical consequence of scrolling, never an independent performance running on a timer. Modern CSS scroll-driven animations (`animation-timeline: scroll()` and `view()`) now cover most scrubbed cases natively without JavaScript, running on the compositor; IntersectionObserver handles the enter/exit reveals that play once on visibility.

## 2. Core Motion Principles

- **Scroll-linked means scrubbed:** values must move both directions with the scroll, never one-shot play on threshold.
- **Reveal once, then stay:** entrance reveals triggered on visibility play a single time; they do not re-trigger on every scroll wiggle.
- **Parallax is a spice:** 1 background layer at 0.5-0.8x speed is enough; multi-layer parallax beyond 2 layers degrades into noise.
- **Keep text readable:** never apply parallax or blur to body copy; restrict to imagery, headers, and decorative layers.
- **Respect the user's scroll velocity:** animations competing with fast scrolling must be compositor-only (transform/opacity).
- **Provide a non-scroll path:** critical content and CTAs must be fully accessible with animations off.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Reveal threshold | `--motion-reveal-threshold` | `0.2` | IntersectionObserver: trigger at 20% visibility |
| Reveal duration | `--motion-reveal-duration` | `600ms` | One-shot reveal play time (clock-based, scroll-triggered) |
| Parallax speed | `--motion-parallax-speed` | `0.5` | Background layer moves at half scroll speed |
| Progress range | `--motion-progress-range` | `0deg-360deg` | Scroll progress indicator sweep range |
| Scrub easing | `--motion-scrub-easing` | `linear` | Scroll-scrubbed mapping must be linear (time easings fight the user) |

Consume tokens by linking `assets/css/scroll-animation.css` and referencing the custom properties — `animation-duration: var(--motion-reveal-duration)` for IO-triggered reveals, `animation-timing-function: var(--motion-scrub-easing)` for anything scrubbed. Note the deliberate split: `--motion-reveal-duration` is clock time for one-shot plays, while scrubbed effects map directly to scroll position and take no duration at all.

## 4. Choreography

- **Sticky-step stories:** a sticky container pins while inner scenes swap at scroll progress milestones.
- **Header collapse:** scroll down collapses the header (height+shadow), scroll up expands it - state changes are stepped, not jittery.
- **Reveal queue:** elements within the same viewport row reveal together; elements a screen apart reveal independently.

## 5. Signature Patterns

- **CSS scroll-driven:** `@keyframes` with `animation-timeline: view(); animation-range: entry 0% entry 60%.`
- **IO reveal:** IntersectionObserver adds `.revealed` once; transition handles the clock-based play.
- **Scroll progress bar:** fixed top bar with `scaleX` driven by `animation-timeline: scroll(root)`.

## 6. Real-World Use Cases

- **Marketing/landing pages:** product storytelling, feature reveals, scrollytelling.
- **Editorial/magazine layouts** with pinned imagery and text sequences.
- **Reading progress indicators, infinite feed headers, map zoom pans.**

## 7. Combination Notes

- With other animation skills:
  - **Pairs well with `data-animation`:** trigger chart count-ups and draw-ins once, when the chart scrolls into view — the natural alliance of the two skills.
  - **Pairs well with `illustration-lottie`:** play Lottie segments as sticky-step scenes swap, gated on scroll progress.
  - **Caution with `easing-timing`:** never put a time-based easing on a scrubbed value — only the linear mapping (`--motion-scrub-easing`) belongs inside scroll-linked motion; clock-based curves are for the one-shot reveals only.
  - **Caution with `entrance-exit`:** scroll reveals and list staggers overlap; pick one owner per region or the same element will animate twice (on load and on scroll).
  - **Caution with `page-transitions`:** don't run a route transition and a scroll reveal on the same viewport entry — stagger them or the incoming view fights the scroll.
  - **Caution with `micro-interactions`:** scroll effects must never hijack hover/press feedback on the same element; keep the two event vocabularies separate.
  - **Caution with `reduced-motion`:** this is the highest-risk category for vestibular triggers — coordinate the fallback strategy explicitly (see Accessibility Notes).
  - **Caution with `loading-states`:** content that reveals on scroll must still be reachable while loading; don't gate a skeleton's visibility on scroll position.
  - **Caution with `feedback-confirmation`:** progress bars driven by scroll are indicators, not confirmations — don't conflate reading progress with action success.
  - **Caution with `gesture-drag`:** both categories listen to continuous input; never let a scroll-scrubbed element also respond to drag, or ownership of the gesture becomes ambiguous.
  - **Caution with `ambient-motion`:** a parallax background is already ambient movement; stacking an aurora loop behind it doubles the peripheral distraction.
- With design styles (companion repo `skill-ui-ux`):
  - **Good affinity:** aurora-ui, collage-art, maximalism — expressive styles where layered depth, pinned imagery, and scroll storytelling reinforce the aesthetic.
  - **Caution:** minimalism and neumorphism — restrained, tactile styles where parallax and pinned choreography easily read as decoration rather than information; if used, keep it to a single reveal pattern.

## 8. Anti-Patterns

- **Jank from layout reads:** reading scrollY and writing styles in the same frame; use compositor-only properties or native timelines
- **Re-triggering reveals:** elements that fade out and replay every time they re-enter the viewport
- **Parallax on text:** body copy drifting at a different speed than its container is a readability failure
- **Scroll hijacking:** overriding native scroll behavior (snap-forcing, speed remapping) breaks the primary input metaphor

### Accessibility Notes

Scroll animation is the highest-risk category for vestibular triggers: parallax drift, large pinned movement, and scrubbed zooms can cause dizziness and nausea for motion-sensitive users. Under `prefers-reduced-motion: reduce`, disable parallax entirely, show all scrubbed effects at their end state, make reveals instant visibility (or a single short fade ≤ 150ms), and keep a static, non-animated progress bar. The global override in `assets/css/scroll-animation.css` collapses `animation-duration`/`transition-duration` to 1ms and forbids `scroll-behavior: smooth`, so nothing depends on JS timing to be safe. Vestibular safety explicitly means: no scroll-hijacking, no smooth-scroll behavior injection, no multi-speed layer movement, and critical content fully visible without any scrolling ritual — scrubbing is an enhancement, never a gate.

## 9. Code Examples

### Example 1 — Native CSS scroll-driven reveal + progress bar

Tokens: `assets/css/scroll-animation.css`

```html
<div class="progress" role="progressbar" aria-label="Reading progress"></div>
<section class="card"><h2>Feature one</h2><p>Reveals as it enters the viewport.</p></section>
<section class="card"><h2>Feature two</h2><p>Same reveal, independent timing.</p></section>
<style>
  .progress {
    position: fixed; inset: 0 0 auto 0; height: 3px;
    transform-origin: 0 50%; transform: scaleX(0);
    background: currentColor;
    animation: grow var(--motion-progress-range) var(--motion-scrub-easing) both;
    animation-timeline: scroll(root); /* scrubbed: no clock duration involved */
  }
  @keyframes grow { to { transform: scaleX(1); } }

  .card {
    opacity: 0; transform: translateY(24px);
  }
  @media (prefers-reduced-motion: no-preference) {
    .card {
      animation: reveal var(--motion-reveal-duration) both;
      animation-timeline: view();
      animation-range: entry 0% entry calc(var(--motion-reveal-threshold) * 100%);
    }
  }
  @keyframes reveal { to { opacity: 1; transform: none; } }
  /* Under prefers-reduced-motion: reduce the global override in
     assets/css/scroll-animation.css collapses durations; the card is
     simply visible at its final state. */
</style>
```

### Example 2 — IntersectionObserver one-shot reveal (fallback path)

Tokens: `assets/css/scroll-animation.css`

```html
<section class="card io-reveal"><h2>Legacy-safe reveal</h2><p>Plays once, then stays.</p></section>
<style>
  .io-reveal {
    opacity: 0; transform: translateY(24px);
    transition:
      opacity var(--motion-reveal-duration) var(--motion-scrub-easing),
      transform var(--motion-reveal-duration) var(--motion-scrub-easing);
  }
  .io-reveal.revealed { opacity: 1; transform: none; }
  @media (prefers-reduced-motion: reduce) {
    .io-reveal { opacity: 1; transform: none; transition: none; }
  }
</style>
<script>
  const cards = document.querySelectorAll('.io-reveal');
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      e.target.classList.add('revealed');   // one-shot: never removed again
      io.unobserve(e.target);               // no re-triggering on scroll wiggle
    }
  }, { threshold: 0.2 });                   // var(--motion-reveal-threshold)
  cards.forEach((c) => io.observe(c));
</script>
```

## 10. Implementation Checklist

- [ ] Scrubbed values are linear and bidirectional — no time-based easing inside `animation-timeline` mappings.
- [ ] All scroll-reactive styles use compositor-only properties (transform/opacity) or native CSS timelines; no scrollY read + style write in the same frame.
- [ ] Reveals fire once via IntersectionObserver (unobserved after entry) — no replay on re-entry.
- [ ] At most one parallax layer, at 0.5-0.8x speed, never applied to body text.
- [ ] Native scroll behavior is untouched: no hijacking, no forced snap, no injected smooth scrolling.
- [ ] Critical content and CTAs are fully accessible with all scroll effects off.
- [ ] `prefers-reduced-motion: reduce` disables parallax, shows scrubbed end states, and keeps a static progress bar (vestibular safety verified).
