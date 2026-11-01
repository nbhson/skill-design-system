---
name: data-animation
description: Animating numbers, charts, and live data - count-ups, bar and draw-in reveals, morphs between states, and updates that make change perceptible without lying.
tags: [charts, data, count-up, dashboards, live-data]
related: [loading-states, scroll-animation, gesture-drag]
---

# Animation Skill: Data & Chart Animation

## 1. Definition

Data animation makes quantitative change perceptible: a KPI counting up, bars growing to height, a line chart drawing left-to-right, a donut sweeping, a live value ticking. Its contract is honesty — motion must never exaggerate, hide, or fabricate change. Charts animate on entrance (once), on update (interpolating between real values), and on drill (hierarchy transitions), while tables and dense data mostly should not animate at all. The craft is restraint with purpose: a single well-timed count-up teaches magnitude; fifty animated cells teach nothing and cost comprehension time. Every animated pixel must be traceable to a true value at every frame of the transition.

## 2. Core Motion Principles

- **Animate the encoding, not the pixels:** bars animate height, lines animate path length, points animate position - values stay truthful throughout.
- **One entrance, then stability:** charts play their entrance once; subsequent updates animate only what changed.
- **Interpolate between real values:** morphing connects two true states; it never passes through fabricated intermediate data.
- **Count-up respects magnitude:** long counts use eased progress but must end exactly at the real value; rounding drift is unacceptable.
- **Dense data stays still:** tables, grids, and dashboards with 20+ live cells skip entrance animation entirely.
- **Live updates are subtle:** a value change is a brief highlight flash or a small tick, not a replay of the entrance.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Chart entrance | `--motion-chart-enter` | `800ms` | Full chart entrance; staggered series +100ms each |
| Count-up duration | `--motion-countup-duration` | `1200ms` | KPI count-up with ease-out |
| Update duration | `--motion-update-duration` | `400ms` | Interpolation between states on data change |
| Draw duration | `--motion-draw-duration` | `1000ms` | Line/path drawing via stroke-dashoffset |
| Tick flash | `--motion-tick-flash` | `600ms` | Background flash on a cell/value change |

Consume tokens by linking `assets/css/data-animation.css` and referencing the custom properties — `animation: grow var(--motion-chart-enter)` for chart entrances, `transition: height var(--motion-update-duration)` for live value changes, `animation: flash var(--motion-tick-flash)` for cell updates. For JS-driven count-ups, read `--motion-countup-duration` from `getComputedStyle(document.documentElement)` so the timing stays token-owned even inside `requestAnimationFrame` code.

## 4. Choreography

- **Axis first, series second:** axes/gridlines settle, then series draw/grow in reading order.
- **Series stagger:** multi-series charts start bars/lines 80-120ms apart so each is parseable.
- **Drill-down zoom:** parent bar/segment morphs into the child view's frame while siblings fade.

## 5. Signature Patterns

- **Count-up:** `requestAnimationFrame` from 0 to value with ease-out; format per frame; end exact.
- **Line draw-in:** `stroke-dasharray` = total length, animate `stroke-dashoffset` length → 0.
- **D3-style interpolation:** interpolate previous datum → next datum and re-render the path each frame.

## 6. Real-World Use Cases

- **Analytics dashboards, KPI cards, financial summaries.**
- **Reports and pitch decks:** hero numbers and chart storytelling.
- **Live feeds:** prices, scores, queues, system metrics.

## 7. Combination Notes

- With other animation skills:
  - **Pairs well with `loading-states`:** the skeleton → chart handoff is a data-animation problem too; the chart entrance IS the loading handoff for dashboard regions.
  - **Pairs well with `scroll-animation`:** trigger the one-shot chart entrance via IntersectionObserver when the chart scrolls into view — the standard dashboard/landing combination.
  - **Pairs well with `gesture-drag`:** draggable scrubbers and time-range selectors drive chart updates; the drag is input, the data morph is the response.
  - **Pairs well with `entrance-exit`:** KPI cards and chart containers enter with the standard fade-up choreography, then the chart plays its own entrance inside.
  - **Caution with `easing-timing`:** count-ups use ease-out per the token notes, but interpolation of live values should stay near-linear — a heavily eased mid-value misrepresents the trajectory of real data.
  - **Caution with `micro-interactions`:** don't wrap chart entrances in hover lifts or press scales; the chart's one entrance is already its moment.
  - **Caution with `feedback-confirmation`:** a tick-flash communicates "value changed", not "action succeeded" — keep the two flash vocabularies visually distinct.
  - **Caution with `page-transitions`:** chart entrances are internal to a view; when navigating between dashboard routes, let the page transition own the motion and skip re-animating charts that persist.
  - **Caution with `reduced-motion`:** the fallback here still keeps one perceptible signal (see Accessibility Notes) — coordinate so the tick-flash survives while count-ups and draw-ins are dropped.
  - **Caution with `illustration-lottie`:** decorative Lottie celebrations around data moments add milliseconds without information; if a celebration is warranted, keep the chart's own values untouched.
  - **Avoid `ambient-motion`:** looping background movement behind charts sabotages reading precision and violates the honesty contract — data surfaces need stillness.
- With design styles (companion repo `skill-ui-ux`):
  - **Good affinity:** minimalism, flat-design, aurora-ui — clean encodings where bars, lines, and numbers carry the visual weight and motion highlights change without chart junk.
  - **Caution:** maximalism and skeuomorphism — decoration-heavy styles invite 3D pie spins, bouncing bars, and textured chart surfaces that add milliseconds but no information.

## 8. Anti-Patterns

- **Fake data in motion:** easing a number through invented intermediate values on a live metric misrepresents the data
- **Re-animating on every render:** charts replaying their full entrance whenever a prop changes
- **Animating everything dense:** 50-cell tables with entrance staggers delay comprehension by seconds
- **Chart junk in motion:** 3D pie spins and bouncing bars that add milliseconds but no information

### Accessibility Notes

Under `prefers-reduced-motion: reduce`, show final values and full charts immediately: no count-up (render the real number), no draw-in (render the complete path), no staggered bar growth. The one exception is deliberate — keep a single tick-flash for updates so change remains perceptible without movement-dependent encoding; the fallback is that update changes flash the background once at `--motion-tick-flash` duration (a brief opacity/color change, which is a retained, safe signal rather than removed meaning). The global override in `assets/css/data-animation.css` collapses `animation-duration`/`transition-duration` to 1ms and caps iteration at 1, so any CSS animation resolves to its end state instantly — pair it with a JS check (`matchMedia('(prefers-reduced-motion: reduce)')`) that skips the count-up loop entirely and writes the final value. Also ensure color flashes are paired with a text or icon change, so updates never rely on color alone.

## 9. Code Examples

### Example 1 — Honest count-up KPI with tick-flash updates

Tokens: `assets/css/data-animation.css`

```html
<div class="kpi"><span class="label">Monthly active users</span><span class="value" id="value">0</span></div>
<style>
  .kpi { font: 500 14px/1.4 system-ui; }
  .value { display: block; font-size: 40px; font-weight: 700; font-variant-numeric: tabular-nums; }
  .value.tick { animation: flash var(--motion-tick-flash) ease-out; } /* 600ms flash on change */
  @keyframes flash { 0% { background: #FFF3C4; } 100% { background: transparent; } }
  @media (prefers-reduced-motion: reduce) { .value.tick { animation-duration: 1ms; } } /* keep the signal, drop the sweep */
</style>
<script>
  const el = document.getElementById('value');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const duration = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--motion-countup-duration')) || 1200;
  const render = (v) => { el.textContent = Math.round(v).toLocaleString(); };

  const tween = (from, to, dur) => {           // shared rAF tween (entrance + updates)
    if (reduced) { render(to); return; }       // no count-up; final value immediately
    const t0 = performance.now();
    (function frame(now) {
      const p = Math.min(1, (now - t0) / dur);
      render(from + (to - from) * (1 - Math.pow(1 - p, 3))); // ease-out per token notes
      if (p < 1) requestAnimationFrame(frame);
      else render(to);                         // end EXACTLY at the real value
    })(t0);
  };

  const update = (next) => {                   // live update: interpolate + tick flash
    const from = Number(el.dataset.v || 0);    // entrance ran once; never replay it
    el.dataset.v = next;
    el.classList.remove('tick'); void el.offsetWidth; el.classList.add('tick');
    tween(from, next, 400);                    // var(--motion-update-duration)
  };
  tween(0, 48213, duration);
  // update(49870);   // later: 400ms interpolation + 600ms tick flash
</script>
```

### Example 2 — Bar chart entrance with axis-first, series-stagger choreography

Tokens: `assets/css/data-animation.css`

```html
<div class="chart" role="img" aria-label="Revenue by quarter: Q1 30, Q2 55, Q3 72, Q4 90">
  <div class="bar" style="--v: 30%"><i>Q1</i></div><div class="bar" style="--v: 55%"><i>Q2</i></div>
  <div class="bar" style="--v: 72%"><i>Q3</i></div><div class="bar" style="--v: 90%"><i>Q4</i></div>
</div>
<style>
  .chart {
    display: flex; align-items: flex-end; gap: 12px;
    height: 160px; border-bottom: 1px solid #D0D5DD; /* axis settles first */
  }
  .bar {
    width: 48px; height: var(--v);
    background: #6C63FF; transform-origin: bottom;
    animation: grow var(--motion-chart-enter) cubic-bezier(0, 0, 0, 1) backwards;
    animation-delay: calc(var(--i, 0) * 100ms); /* series stagger: +100ms each */
  }
  .bar:nth-child(1) { --i: 0; } .bar:nth-child(2) { --i: 1; }
  .bar:nth-child(3) { --i: 2; } .bar:nth-child(4) { --i: 3; }
  @keyframes grow { from { transform: scaleY(0); } }
  @media (prefers-reduced-motion: reduce) { .bar { animation-duration: 1ms; animation-delay: 0ms; } } /* full chart immediately */
</style>
```

## 10. Implementation Checklist

- [ ] Every animated frame is traceable to real values — interpolation connects true states, never fabricated data.
- [ ] Charts play their entrance exactly once; prop/data changes trigger only the `--motion-update-duration` interpolation.
- [ ] Count-ups end exactly at the real value (final `render(target)` after the loop) with no rounding drift.
- [ ] Encoding animates, not pixels: bar height, path length, point position — never a decorative spin or bounce.
- [ ] Dense surfaces (20+ live cells, tables, grids) skip entrance animation entirely.
- [ ] Live updates use the `--motion-tick-flash` highlight plus a text/icon change, never color alone.
- [ ] `prefers-reduced-motion: reduce` renders final values and full charts immediately, retaining only the single tick-flash.
