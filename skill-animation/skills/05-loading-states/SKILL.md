---
name: loading-states
description: Spinners, skeletons, progress, and optimistic UI — motion that manages waiting honestly, communicates progress, and hands off smoothly to real content.
tags: [spinners, skeletons, progress, optimistic-ui, async]
related: [easing-timing, entrance-exit, feedback-confirmation, data-animation]
---

# Animation Skill: Loading States

## 1. Definition

Loading animation is the interface between delay and trust. Its job is to set expectations: an indeterminate spinner says "unknown length", a skeleton says "this exact layout is coming", a progress bar says "measurable progress", optimistic UI says "assumed success, correctable". The craft is choosing the right honesty level for each wait duration and handing off from placeholder to content without a jarring swap — a shimmer that lies about layout or a bar stalled at 90% damages trust faster than showing nothing at all.

## 2. Core Motion Principles

- **Match the pattern to the wait:** <300ms show nothing; 300ms-1s spinner or pulse; >1s skeleton or progress bar.
- **Skeletons must mirror the real layout:** a skeleton that differs from the loaded content causes a jarring reflow.
- **Delay before showing:** render the spinner only after ~300ms to avoid flashing on fast loads.
- **Loops imply progress that does not exist:** indeterminate loops must be visibly 'indeterminate' (sweep, not count-up).
- **Optimistic UI needs an escape hatch:** every optimistic state must be visually correctable on failure (undo, revert, error tint).
- **Never block the whole UI:** keep navigation and unrelated controls interactive while a region loads.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Show delay | `--motion-show-delay` | `300ms` | Wait before revealing any loading indicator |
| Spinner loop | `--motion-spinner-loop` | `1000ms` | Linear rotation loop |
| Shimmer loop | `--motion-shimmer-loop` | `1500ms` | Skeleton shimmer sweep |
| Shimmer travel | `--motion-shimmer-travel` | `200%` | Gradient sweep distance across the skeleton |
| Progress fill | `--motion-progress-fill` | `240ms` | Eased fill step when progress updates |
| Handoff duration | `--motion-handoff-duration` | `200ms` | Skeleton → content crossfade |

Consume tokens by importing `assets/css/loading-states.css` and referencing the custom properties (`var(--motion-show-delay)`, `var(--motion-shimmer-loop)`, …) wherever placeholders, spinners, or handoff transitions are defined. All loop timings and the handoff window come from this single generated file (sourced from `skills/data.json`) — never re-hardcode them per component.

## 4. Choreography

- **Placeholder in, content in:** skeleton fades in fast, content crossfades over the skeleton in the same slot.
- **Per-region loading:** each async region owns its own indicator; never a single global spinner for mixed content.
- **Progress then complete:** an indeterminate bar becomes determinate when progress is known, then flashes to 100% briefly before handoff.

## 5. Signature Patterns

- **Skeleton shimmer:** repeating-linear-gradient background-position animation on gray placeholder blocks.
- **Optimistic create:** render the item instantly with an 'ephemeral' style, replace with server state or revert with an error toast.
- **Streaming text:** token-by-token arrival with a cursor pulse for AI/chat responses.

## 6. Real-World Use Cases

- **Feeds, dashboards, search results, media grids** - any async list/grid.
- **File uploads, payments, long form submissions** with real progress.
- **AI/chat streaming, messaging 'typing' indicators, pull-to-refresh.**

## 7. Combination Notes

### With other animation skills

- **Pairs well with `easing-timing`:** loops run on `ease-linear` by definition; fills and handoffs use the standard decelerate curve.
- **Pairs well with `data-animation` and `entrance-exit`:** dashboards pair skeleton grids with chart entrances, and the skeleton→content crossfade is entrance choreography with content staggering in after handoff.
- **Pairs well with `feedback-confirmation` and `gesture-drag`:** failed optimistic creates hand off to error toasts with undo; pull-to-refresh is a gesture that resolves into a loading state.
- **Pairs well with `illustration-lottie`:** branded loaders are Lottie's second-best fit, within the loader byte budget.
- **Use with caution alongside `page-transitions` and `scroll-animation`:** resolve data before navigating rather than spinning inside the new route, and coordinate infinite-feed thresholds so skeletons never pop in after scroll settles.
- **Use with caution alongside `micro-interactions`:** don't micro-animate placeholders themselves — shimmer plus press effects is noise.
- **Use with caution alongside `reduced-motion`:** all loops are removed in reduced mode; static fallbacks must be designed, not improvised.
- **Avoid `ambient-motion`:** decorative loops behind loading regions double the visual churn and slow perceived performance.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with Minimalism, Flat Design, and Aurora UI:** clean flat-gray skeleton blocks fit naturally; Aurora's soft gradients make a gentle shimmer feel on-brand.
- **Use caution with Neumorphism and Brutalism UI:** soft dual shadows make skeleton blocks indistinguishable from real content; Brutalism favors explicit text status over placeholder illusion.

## 8. Anti-Patterns

- **Spinner-only culture:** a lone spinner for every wait gives no layout, no progress, and no expectation.
- **Skeleton lie:** placeholder blocks shaped nothing like the arriving content, causing layout shift on load.
- **Instant-in spinner:** flashing a spinner for a 150ms request makes fast things feel slow.
- **Fake progress:** a bar that sits at 90% for a minute erodes trust faster than no bar at all.

### Accessibility Notes

Loops are the core vestibular and attention hazard here: continuous shimmer and rotation draw the eye without end. The strategy from `skills/data.json` → `reducedMotion`: **stop all looping shimmer/spin; use a static placeholder with a pulsing opacity step (1–2 Hz, low amplitude) or plain static blocks.** The fallback renders static gray skeletons plus a text status ("Loading results…"), and progress bars fill directly without easing loops. The global override in `assets/css/loading-states.css` collapses all animation and transition durations to 1ms under `prefers-reduced-motion: reduce`, freezing loops on their first frame — pair it with an explicit per-component static variant so placeholders stay meaningful. Announce async region status via `aria-live="polite"` and mark decorative placeholders `aria-hidden="true"`.

## 9. Code Examples

### Example 1 — Skeleton with shimmer, delayed reveal, and crossfade handoff

Tokens: `assets/css/loading-states.css`

```html
<div class="region" aria-live="polite" aria-busy="true">
  <div class="skeleton" aria-hidden="true">
    <span class="sk sk--avatar"></span><span class="sk"></span>
  </div>
  <div class="content" hidden><p>Jordan Lee posted a new trail log.</p></div>
</div>

<style>
  .sk {
    display: inline-block; height: 14px; width: 220px; border-radius: 7px;
    background: linear-gradient(90deg, #e5e7eb 25%, #f3f4f6 50%, #e5e7eb 75%);
    background-size: var(--motion-shimmer-travel) 100%;
    animation: shimmer var(--motion-shimmer-loop) linear infinite;
  }
  .sk--avatar { width: 40px; height: 40px; border-radius: 50%; }
  @keyframes shimmer { from { background-position: 100% 0; } to { background-position: -100% 0; } }
  @keyframes fade-in { from { opacity: 0; } }

  /* Handoff: content crossfades over the skeleton in the same slot */
  .region.loaded .skeleton { display: none; }
  .region.loaded .content { display: block; animation: fade-in var(--motion-handoff-duration) both; }

  @media (prefers-reduced-motion: reduce) {
    .sk { animation: none; background: #e5e7eb; } /* static gray block */
  }
</style>

<script>
  const region = document.querySelector('.region');
  // Reveal the skeleton only if the wait exceeds the show-delay (300ms).
  const showTimer = setTimeout(() => region.classList.add('ready'), 300);
  fetch('/feed').then(r => r.json()).then(() => {
    clearTimeout(showTimer); // fast load: no spinner flash
    region.classList.add('loaded'); region.setAttribute('aria-busy', 'false'); // crossfade handoff
  });
</script>
```

### Example 2 — Indeterminate → determinate progress bar

Tokens: `assets/css/loading-states.css`

```html
<div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="100">
  <div class="bar bar--indeterminate"></div>
</div>

<style>
  .progress { height: 4px; border-radius: 2px; background: #e5e7eb; overflow: hidden; }
  .bar { height: 100%; background: #1a73e8; border-radius: 2px; }
  .bar--indeterminate { width: 40%; animation: sweep var(--motion-shimmer-loop) linear infinite; }
  @keyframes sweep { from { transform: translateX(-100%); } to { transform: translateX(350%); } }
  /* Determinate step once real progress is known */
  .bar--determinate { transition: width var(--motion-progress-fill) cubic-bezier(0.2, 0, 0, 1); }
  @media (prefers-reduced-motion: reduce) {
    .bar--indeterminate { animation: none; width: 100%; opacity: 0.4; }
  }
</style>

<script>
  source.addEventListener('progress', (e) => {
    bar.className = 'bar bar--determinate';  // indeterminate → determinate
    bar.style.width = `${e.percent}%`;       // eased fill per update
  });
</script>
```

## 10. Implementation Checklist

- [ ] Match pattern to wait: nothing under 300ms, spinner/pulse for 300ms–1s, skeleton or progress beyond 1s.
- [ ] Skeleton blocks mirror the real content layout exactly — same dimensions, same grid — to prevent layout shift.
- [ ] All loops (spinner `--motion-spinner-loop`, shimmer `--motion-shimmer-loop`) run on `linear` and are visibly indeterminate.
- [ ] Loading is per-region; navigation and unrelated controls stay interactive during any wait.
- [ ] Every optimistic state has a visible escape hatch: revert, undo, or error tint on failure.
- [ ] Handoff is a crossfade in the same slot (`--motion-handoff-duration`), never a hard swap.
- [ ] `prefers-reduced-motion: reduce` stops all shimmer/spin loops and falls back to static gray skeletons with text status (global override in `assets/css/loading-states.css`).
