---
name: easing-timing
description: The token foundation of all motion — a five-step duration hierarchy and a small family of easing curves that make every transition feel intentional instead of arbitrary.
tags: [motion-tokens, duration, easing, transitions, design-systems]
related: [micro-interactions, entrance-exit, reduced-motion]
---

# Animation Skill: Duration & Easing Fundamentals

## 1. Definition

Duration and easing are the vocabulary of motion design. Duration controls **how long** a transition takes; easing controls **how velocity changes** across that duration. Together they encode physics and intent: fast-and-sharp reads as responsive and light, slow-and-soft reads as deliberate and weighty. Because perceived quality in an interface is largely downstream of timing consistency, this skill is the token layer every other animation skill inherits from — micro-interactions, entrances, and page transitions all pull their durations and curves from these custom properties, and no component should ever hardcode its own timing values.

## 2. Core Motion Principles

- **Durations scale with distance and importance:** small state changes are fast (100-150ms), large surface changes are slower (300-480ms).
- **Use as few duration steps as possible:** a 5-step hierarchy (instant/fast/base/slow/deliberate) covers virtually all UI.
- **Enter with deceleration, exit with acceleration:** elements coming in lose speed as they arrive; elements leaving pick up speed as they go.
- **Never use linear easing for element transitions:** linear reads mechanical and is reserved for indeterminate loops and scroll-linked mapping.
- **One easing family per product:** pick a standard curve and use it for 80%+ of transitions; reserve emphasized curves for signature moments.
- **Overshoot (back/spring) only on small, non-text elements:** text and large surfaces distort badly under overshoot.
- **Timing is perceived, not absolute:** 300ms over 20px feels slow, the same 300ms across the full screen feels brisk - judge by perceived speed.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Duration | `--motion-duration-instant` | `100ms` | Press/active states, toggles, checkboxes |
| Duration | `--motion-duration-fast` | `150ms` | Hover, focus rings, icon swaps, tooltips |
| Duration | `--motion-duration-base` | `240ms` | Standard transitions: menus, dropdowns, cards |
| Duration | `--motion-duration-slow` | `320ms` | Large surfaces: modals, drawers, bottom sheets |
| Duration | `--motion-duration-deliberate` | `480ms` | Hero moments: onboarding, celebration, page-level reveals |
| Duration | `--motion-duration-loop` | `1200ms` | Indeterminate loops: spinners, shimmer sweeps |
| Easing | `--motion-ease-standard` | `cubic-bezier(0.2, 0, 0, 1)` | Default curve for enter + move (emphasized decelerate) |
| Easing | `--motion-ease-decelerate` | `cubic-bezier(0, 0, 0, 1)` | Elements entering the viewport or a container |
| Easing | `--motion-ease-accelerate` | `cubic-bezier(0.3, 0, 1, 1)` | Elements leaving the screen |
| Easing | `--motion-ease-emphasized` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful overshoot; small non-text elements only |
| Easing | `--motion-ease-linear` | `linear` | Loops and scroll-linked value mapping only |

Consume them by linking `assets/css/easing-timing.css` once at the app root, then referencing `var(--motion-<role>)` — e.g. `transition: transform var(--motion-duration-base) var(--motion-ease-standard)` — in every component. If a value not in this table seems necessary, the timing is wrong; adjust the token scale, not the component.

## 4. Choreography

- **Stagger sibling entrances 30-50ms apart** so the eye reads a wave, not a crowd.
- **Exit before enter when swapping content in the same slot:** old content leaves in ~40-60% of the enter duration.
- **Nested elements animate inside their parent's window:** children start after the parent container has begun moving.

## 5. Signature Patterns

- **Token-first:** define --duration-* and --ease-* as CSS custom properties and reference them everywhere; no magic numbers in components.
- **Pair enter/exit asymmetrically:** enter uses ease-decelerate at duration-slow, exit uses ease-accelerate at ~70% of that duration.

## 6. Real-World Use Cases

- **Design systems and component libraries** defining their motion spec.
- **Any product establishing a consistent feel** across teams and platforms.
- **Auditing an existing UI for motion debt:** inconsistent durations and curves.

## 7. Combination Notes

### With other animation skills

- **Pairs well with micro-interactions, entrance-exit, page-transitions, loading-states, feedback-confirmation, and reduced-motion:** every one of these skills consumes this token layer — it is their shared timing vocabulary.
- **Caution with gesture-drag:** during an active drag there is no time-based easing at all (the finger is the easing); these tokens only govern the post-release resolve.
- **Caution with ambient-motion and illustration-lottie:** loops and baked timelines run on their own clocks (`--motion-duration-loop`, designer-authored durations); do not force them onto the interaction duration scale.
- **Caution with scroll-animation:** scrubbed, scroll-linked mapping must use `--motion-ease-linear` — eased curves on scrubbing fight the user's hand.
- **Caution with data-animation:** chart entrances may run longer than the interaction scale (e.g. 800ms draw-ins); keep interactive feedback on the token scale and treat chart timelines as a documented exception.
- **No avoid list:** as the foundation layer, this skill has no incompatible partners — only skills that ignore it (which is the failure mode to prevent).

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and glassmorphism:** these styles reward restrained, physics-plausible timing on a small curve family.
- **Caution with retro and brutalism-ui:** both may deliberately want abrupt, stepped, or mechanical motion; if so, deviate consciously and document it — never by drifting token by token.

## 8. Anti-Patterns

- **Random durations:** every component picking its own 180/210/350ms values makes the product feel assembled from parts
- **Linear everywhere:** applying linear easing to menus and cards reads as robotic and low-effort
- **Overshoot on everything:** a back easing on text blocks and large panels looks broken, not playful
- **Slow entrances:** keeping users waiting with 600ms+ entrances for content they asked for; respect the 100-500ms envelope

### Accessibility Notes

Reduced motion here is about **shortening, not removing**: reduced-motion users still need duration tokens and visible state changes, so durations collapse rather than states disappearing. The fallback in `assets/css/easing-timing.css` collapses all durations to ≤1ms opacity-only fades under `prefers-reduced-motion` via a global override block (`animation-duration: 1ms !important; transition-duration: 1ms !important; animation-iteration-count: 1 !important`). Because the override uses the universal selector, per-component re-enables of safe short fades (≤150ms opacity) must come *after* it in the cascade. Overshoot curves (`--motion-ease-emphasized`) should also be neutralized to `--motion-ease-standard` in reduced mode, since springy motion is itself a vestibular trigger.

## 9. Code Examples

### Example 1 — CSS-only dropdown: enter decelerates, exit accelerates

Tokens: `assets/css/easing-timing.css`

```html
<nav class="menu-wrap">
  <button class="trigger">Actions ▾</button>
  <ul class="menu" role="menu">
    <li role="menuitem">Rename</li>
    <li role="menuitem">Duplicate</li>
    <li role="menuitem">Archive</li>
  </ul>
</nav>
<style>
.menu-wrap { position: relative; display: inline-block; font: 14px/1.4 system-ui; }
.trigger {
  padding: 10px 16px; border: 1px solid #d0d5dd; border-radius: 8px; background: #fff; cursor: pointer;
  transition: background var(--motion-duration-instant) var(--motion-ease-standard);
}
.menu {
  position: absolute; top: calc(100% + 6px); left: 0; margin: 0; padding: 6px;
  list-style: none; min-width: 160px;
  background: #fff; border: 1px solid #e4e7ec; border-radius: 10px;
  box-shadow: 0 8px 24px rgba(16, 24, 40, 0.12);
  opacity: 0; transform: translateY(-8px); pointer-events: none;
  /* EXIT: accelerate, ~70% of the enter duration */
  transition:
    opacity calc(var(--motion-duration-base) * 0.7) var(--motion-ease-accelerate),
    transform calc(var(--motion-duration-base) * 0.7) var(--motion-ease-accelerate);
}
.menu-wrap:hover .menu,
.menu-wrap:focus-within .menu {
  opacity: 1; transform: translateY(0); pointer-events: auto;
  /* ENTER: decelerate at full duration */
  transition:
    opacity var(--motion-duration-base) var(--motion-ease-decelerate),
    transform var(--motion-duration-base) var(--motion-ease-decelerate);
}
.menu li {
  padding: 8px 12px; border-radius: 6px; cursor: pointer;
  transition: background var(--motion-duration-instant) var(--motion-ease-standard);
}
.menu li:hover { background: #f2f4f7; }
.trigger:focus-visible { outline: 2px solid #4f46e5; outline-offset: 2px; }
</style>
```

### Example 2 — Token-driven Web Animations API (small JS snippet)

Tokens: `assets/css/easing-timing.css`

```html
<div class="card" id="card">New report available</div>
<script>
  // Read tokens at runtime — no magic numbers in JS either.
  const root = getComputedStyle(document.documentElement);
  const token = (name) => root.getPropertyValue(name).trim();

  document.getElementById('card').animate(
    [{ opacity: 0, transform: 'translateY(12px)' }, { opacity: 1, transform: 'translateY(0)' }],
    { duration: parseFloat(token('--motion-duration-base')), // 240
      easing: token('--motion-ease-decelerate'),
      fill: 'both' }
  );
</script>
```

## 10. Implementation Checklist

- [ ] Every transition references a `--motion-duration-*` and `--motion-ease-*` token — zero magic ms/bezier numbers in components.
- [ ] Enter uses deceleration, exit uses acceleration, and exit runs at ~70% of the enter duration.
- [ ] `--motion-ease-linear` appears only inside infinite loops and scroll-linked mappings — never on menus, cards, or hovers.
- [ ] `--motion-ease-emphasized` (overshoot) is used only on small, non-text elements and for 20% of transitions at most.
- [ ] No entrance for user-requested content exceeds 500ms; the whole scale stays inside the 100-500ms envelope.
- [ ] `prefers-reduced-motion` global override is loaded and verified: durations collapse to ≤1ms while state changes remain visible.
- [ ] New timing needs trigger a token-scale review, not a one-off value.
