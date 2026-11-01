---
name: entrance-exit
description: How elements appear and disappear — fade+displace reveals, staggered siblings, and asymmetric timing that teach hierarchy and continuity instead of dumping content on screen.
tags: [entrance, exit, stagger, choreography, reveals]
related: [easing-timing, page-transitions, micro-interactions]
---

# Animation Skill: Entrance & Exit Choreography

## 1. Definition

Entrance and exit animations govern the appearance and disappearance of content: page loads, list reveals, modal in/out, list item removal. Done well, they teach two things at once — **hierarchy** (what to look at first) and **continuity** (where content went when it left). The core techniques are fade+displace entrances, staggered siblings, and asymmetric timing: exits are always faster than entrances. Together they turn a hard content swap into a spatial story the user can follow, without ever holding requested content hostage to a long sequence.

## 2. Core Motion Principles

- **Animate from the direction of origin:** modals rise from their trigger, drawers slide from their edge, dropdowns descend from their button.
- **Stagger creates order:** siblings enter 30-50ms apart, capped at ~300ms total or the sequence feels sluggish.
- **Exits are faster than entrances:** 60-70% of the enter duration, with acceleration easing.
- **Enter with opacity + small displacement:** 8-24px translate plus fade is the universal, safe reveal.
- **Never animate content the user explicitly requested slower than 500ms:** task-critical content enters near-instantly.
- **Removed items collapse (height/scale) while neighbors reflow,** so the list does not visually teleport.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Enter | `--motion-enter-distance` | `16px` | Default translateY/X offset for fade-in reveals |
| Enter | `--motion-enter-duration` | `240ms` | Per-item entrance with ease-decelerate |
| Exit | `--motion-exit-duration` | `160ms` | Per-item exit with ease-accelerate |
| Stagger | `--motion-stagger-step` | `40ms` | Delay between sibling items |
| Stagger | `--motion-stagger-cap` | `300ms` | Maximum total stagger window |
| Collapse | `--motion-collapse-duration` | `200ms` | Height/scale collapse for removal |

Consume them by linking `assets/css/entrance-exit.css` and composing per-item entrances as `transform: translateY(var(--motion-enter-distance))` with `animation-delay: min(calc(var(--i) * var(--motion-stagger-step)), var(--motion-stagger-cap))`. The easing curves themselves come from the easing-timing token layer (`ease-decelerate` for enter, `ease-accelerate` for exit); this skill owns the distances, durations, and stagger rhythm.

## 4. Choreography

- **Container first, children second:** the modal/backdrop fades in, then its content staggers in.
- **Reading-order stagger:** top-to-bottom, or F-pattern for grids; never random order.
- **Directional continuity:** in a wizard, new content enters from the direction of the next button, returning content from the opposite side.

## 5. Signature Patterns

- **Fade-up list:** li { opacity:0; translateY(16px) -> 0 } with animation-delay: calc(var(--i) * 40ms).
- **FLIP removal:** measure item height, collapse with scale+opacity, let the list reflow underneath.
- **Shared-element grow:** a card expands into a detail panel by animating position and size, not by crossfading two screens.

## 6. Real-World Use Cases

- **Feed/list first paint, search results, dashboards** after data resolves.
- **Modals, drawers, popovers, command palettes** - overlay entrances.
- **Undo/delete flows:** item flies out, neighbors close the gap, toast appears.

## 7. Combination Notes

### With other animation skills

- **Pairs well with easing-timing and page-transitions:** enter/exit durations ride the shared token scale (ease-decelerate in, ease-accelerate out), and route changes are the same choreography at view scale — shared elements and directional slides extend the continuity rules.
- **Pairs well with micro-interactions and loading-states:** once content has entered, hover/press feedback takes over (keep the two timelines sequential), and skeleton-to-content handoffs are themselves entrances at `--motion-enter-duration`.
- **Pairs well with feedback-confirmation and data-animation:** delete flows hand the item's exit directly to the undo toast's entrance, and charts enter with stagger principles (series 80-120ms apart) after their axes settle.
- **Caution with scroll-animation and illustration-lottie:** viewport-triggered reveals must play once and stay (no scroll re-triggering), and a baked Lottie hero competes with a staggered UI entrance for the same first-paint attention — pick one anchor per view.
- **Caution with reduced-motion:** keep the reveal, drop the displacement and stagger (see Accessibility Notes).
- **Caution with gesture-drag and ambient-motion:** dragged elements resolve via physics, not entrance tokens; ambient loops must never participate in the entrance window.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, aurora-ui, and glassmorphism:** clean fade+displace reveals and disciplined staggers match restrained or atmospheric styles; aurora and glass panels especially benefit from container-first, content-second layering.
- **Caution with brutalism-ui and retro:** both may favor abrupt, unanimated appearance or deliberately mechanical movement; if content simply pops in as a stylistic choice, do it consistently and skip half-hearted staggers.

## 8. Anti-Patterns

- **Simultaneous dump:** all elements fading in at the same instant with no stagger reads as a slow page load, not choreography
- **Overlong sequences:** 15 items x 40ms + 240ms each keeps content hostage for seconds; cap the window
- **Exit-less replacement:** old content vanishing instantly while new content animates in breaks continuity
- **Animating from nowhere:** entrances using opacity 0 -> 1 with no spatial cue miss the chance to teach origin

### Accessibility Notes

Under `prefers-reduced-motion`, the strategy is **keep the reveal, remove the travel**: displacement and stagger go away, and the whole group plays a single short opacity fade instead. The fallback in `assets/css/entrance-exit.css` renders all items opacity-only at duration-fast with no stagger, so hierarchy and ordering information still land — content does not "jump in" with no continuity. Set `animation: none` plus `opacity: 1; transform: none` on entering items inside the media query (the token file's global 1ms override also enforces it), and ensure removals collapse instantly rather than animating height, since layout-adjacent motion is a common vestibular trigger. Whatever the mode, the final state must be reached: no element may remain hidden because its entrance animation was cancelled.

## 9. Code Examples

### Example 1 — CSS-only staggered fade-up list (enter with distance + cap)

Tokens: `assets/css/entrance-exit.css`

```html
<ul class="feed">
  <li style="--i: 0">Design review — 10:00</li>
  <li style="--i: 1">Handoff notes</li>
  <li style="--i: 2">QA checklist</li>
  <li style="--i: 3">Release plan</li>
  <li style="--i: 4">Retro actions</li>
</ul>
<style>
.feed { display: grid; gap: 8px; max-width: 360px; margin: 0; padding: 0;
        font: 14px/1.4 system-ui; list-style: none; }
.feed li {
  padding: 14px 16px; background: #f8fafc;
  border: 1px solid #e2e8f0; border-radius: 10px;
  /* start hidden, displaced by the enter-distance token */
  opacity: 0; transform: translateY(var(--motion-enter-distance));
  animation: enter var(--motion-enter-duration) var(--motion-ease-decelerate) forwards;
  /* stagger step with a hard cap: min(40ms * i, 300ms) */
  animation-delay: min(calc(var(--i) * var(--motion-stagger-step)), var(--motion-stagger-cap));
}
@keyframes enter { to { opacity: 1; transform: translateY(0); } }
@media (prefers-reduced-motion: reduce) {
  /* keep the reveal, drop travel and stagger: one short group fade instead */
  .feed li { animation: none; opacity: 1; transform: none; transition: opacity 150ms ease; }
}
</style>
```

### Example 2 — FLIP-style list removal (small JS genuinely needed)

Tokens: `assets/css/entrance-exit.css`

```html
<ul class="list" id="list">
  <li>Inbox zero sprint <button aria-label="Remove">✕</button></li>
  <li>Ship motion tokens <button aria-label="Remove">✕</button></li>
  <li>QA reduced motion <button aria-label="Remove">✕</button></li>
</ul>
<style>
.list { max-width: 360px; margin: 0; padding: 0; font: 14px/1.4 system-ui; list-style: none; }
.list li {
  display: flex; justify-content: space-between; align-items: center; gap: 12px;
  padding: 12px 16px; margin-bottom: 8px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
}
.list button { border: 0; background: none; cursor: pointer; padding: 4px; }
.list button:focus-visible { outline: 2px solid #4f46e5; outline-offset: 2px; }
</style>
<script>
  const list = document.getElementById('list');
  list.addEventListener('click', (e) => {
    const btn = e.target.closest('button');
    if (!btn) return;
    const li = btn.closest('li');
    // 1) fly out: fast exit with acceleration
    li.style.transition = 'transform var(--motion-exit-duration) var(--motion-ease-accelerate), opacity var(--motion-exit-duration) var(--motion-ease-accelerate)';
    li.style.transform = 'translateX(24px)'; li.style.opacity = '0';
    li.addEventListener('transitionend', () => {
      // 2) collapse height so neighbors reflow instead of teleporting
      li.style.overflow = 'hidden';
      li.style.height = li.offsetHeight + 'px';
      li.style.transition = 'height var(--motion-collapse-duration) var(--motion-ease-standard), margin var(--motion-collapse-duration) var(--motion-ease-standard), padding var(--motion-collapse-duration) var(--motion-ease-standard)';
      requestAnimationFrame(() => {
        li.style.height = '0'; li.style.marginBottom = '0'; li.style.paddingTop = '0'; li.style.paddingBottom = '0';
        li.addEventListener('transitionend', () => li.remove(), { once: true });
      });
    }, { once: true });
  });
</script>
```

## 10. Implementation Checklist

- [ ] Entrances combine opacity + 8-24px displacement from the direction of origin — never opacity alone, never large travel.
- [ ] Siblings stagger 30-50ms apart using `--motion-stagger-step`, capped at `--motion-stagger-cap` (300ms) total.
- [ ] Exits run at 60-70% of the enter duration with acceleration easing — no exit-less content swaps.
- [ ] Removals collapse height/scale and let neighbors reflow; lists never teleport.
- [ ] User-requested and task-critical content enters near-instantly — nothing waits past 500ms.
- [ ] Choreography follows container-first-then-children and reading order, never random.
- [ ] Under `prefers-reduced-motion`, entrances become a single short opacity fade for the group with no stagger, and all elements still reach their final visible state.
