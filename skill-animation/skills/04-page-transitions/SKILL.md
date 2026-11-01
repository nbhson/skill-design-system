---
name: page-transitions
description: Movement between screens and routes — shared elements, directional slides, and the View Transitions API keeping spatial context across navigation.
tags: [navigation, shared-elements, view-transitions, spatial-context, routing]
related: [easing-timing, entrance-exit, gesture-drag, loading-states]
---

# Animation Skill: Page & View Transitions

## 1. Definition

Page transitions connect two screens into one spatial story. Instead of a hard cut, the outgoing and incoming views coordinate: a shared card expands into its detail page, a tab panel slides horizontally, a route crossfades through a snapshot. The user should always know where they are relative to where they were — direction and continuity are information, not decoration. Modern browsers support this natively via the View Transitions API; frameworks provide equivalents (Framer Motion AnimatePresence, Next.js templates). Total transition time stays short: navigation is a means to content, never an event in itself.

## 2. Core Motion Principles

- **Direction is meaning:** forward navigation moves left/forward, back navigation reverses it; vertical hierarchies drill down.
- **Shared elements anchor the transition:** one element that visibly persists (image, card header) outweighs ten decorative fades.
- **Hierarchy of layers:** background exits first, content crossfades, navigation chrome persists unchanged.
- **Keep total transition under 400ms:** navigation is a means, not an event.
- **Interruptible and reversible:** navigating mid-transition must work - transitions queue or reverse, never lock the UI.
- **Snapshot-based fallback:** where the View Transitions API is unsupported, fall back to a plain crossfade, not a broken layout.

## 3. Motion Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Standard route transition | `--motion-transition-duration` | `320ms` | Standard route transition |
| Shared-element morph | `--motion-transition-duration-shared` | `400ms` | Shared-element morphs, slightly longer to be readable |
| Sibling-route push | `--motion-slide-distance` | `100%` | Full-width pushes between sibling routes |
| Fallback crossfade | `--motion-crossfade-duration` | `200ms` | Fallback crossfade; also the root snapshot fade |
| Navigation curve | `--motion-ease-navigation` | `cubic-bezier(0.2, 0, 0, 1)` | Standard curve for route changes |

Consume tokens by importing `assets/css/page-transitions.css` once at the app root and referencing the custom properties (`var(--motion-transition-duration)`, `var(--motion-ease-navigation)`, …) in every route-level transition. Never hardcode durations or curves in components — the token file is generated from `skills/data.json` and is the single source of truth.

## 4. Choreography

- **Push pattern:** old view translates out -25% with slight dim, new view slides in from 100% (iOS-style).
- **Drill-down:** detail page scales from 92% to 100% with opacity; back reverses exactly.
- **Shared-element morph:** capture the trigger card's bounds, animate it to the detail hero position while surrounding content fades.

## 5. Signature Patterns

- **View Transitions API:** document.startViewTransition(() => updateTheDOM()) with ::view-transition-old/new animations.
- **view-transition-name per shared element:** assign unique names to elements that should morph between pages.
- **Route-level suspense handoff:** resolve data before starting the transition so the entering view is complete.

## 6. Real-World Use Cases

- **E-commerce:** product grid -> product detail with shared product image.
- **Mobile-first SPAs and PWAs** where spatial navigation matches native expectations.
- **Tabbed interfaces, wizards/steppers, settings drill-downs.**

## 7. Combination Notes

### With other animation skills

- **Pairs well with `easing-timing`:** route transitions inherit their curve and duration hierarchy directly from the token foundation.
- **Pairs well with `entrance-exit`:** the entering view's internal content staggers in using entrance choreography once the route settles.
- **Pairs well with `gesture-drag`:** edge-swipe back gestures and push/pull transitions are one continuum; share the spatial language.
- **Use with caution alongside `loading-states`:** resolve data before starting the transition; do not chain spinner → transition or navigation feels doubly slow.
- **Use with caution alongside `micro-interactions`:** keep micro-feedback on controls out of the route-change window — one motion story at a time.
- **Use with caution alongside `scroll-animation`:** settle scroll-driven effects before capturing snapshots, or the transition starts mid-scroll.
- **Use with caution alongside `reduced-motion`:** transitions are high-travel motion; wire the crossfade fallback from day one.
- **Use with caution alongside `feedback-confirmation`, `data-animation`, and `illustration-lottie`:** sequence these after the route settles instead of overlapping effects.
- **Avoid `ambient-motion`:** looping layers behind a route change cause snapshot flicker and compete with directional meaning.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with Minimalism, Flat Design, and Class Morphism:** restrained, functional styles let a directional slide or shared-element morph read clearly without noise.
- **Use caution with Brutalism UI and Collage Art:** deliberately raw, disjointed aesthetics often justify hard cuts; forced smoothness fights the style's language.

## 8. Anti-Patterns

- **Transition on every navigation:** hard cuts are correct for lateral jumps (tabs at depth); motion for motion's sake disorients.
- **Breaking the back gesture:** locking scroll or ignoring edge-swipe during a transition breaks platform muscle memory.
- **Long shared-element morphs:** stretching a small thumbnail across the screen for 700ms+ reads as sluggish, not cinematic.
- **Flash of unstyled entering view:** starting the transition before data/layout resolves, so the new page pops after arriving.

### Accessibility Notes

Navigation motion is large-travel motion — exactly the category that triggers vestibular discomfort. The strategy from `skills/data.json` → `reducedMotion`: **disable slides and morphs entirely; keep a short crossfade so navigation still feels connected.** The fallback renders old/new root snapshots as a plain opacity crossfade at `--motion-crossfade-duration`, and shared elements fade in place instead of traveling. The global override in `assets/css/page-transitions.css` collapses all `animation-*` and `transition-*` durations to 1ms under `prefers-reduced-motion: reduce`. Also never lock the UI or the back gesture during a transition — interruptibility is an accessibility requirement, not just polish.

## 9. Code Examples

### Example 1 — Route change via the View Transitions API with a shared card

Tokens: `assets/css/page-transitions.css`

```html
<a class="card" href="/product/42">
  <img src="shoe.jpg" alt="Trail runner" style="view-transition-name: product-hero">
  <h3>Trail Runner</h3>
</a>

<style>
  .card { display: block; width: 240px; padding: 16px; border-radius: 12px;
          background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .card:focus-visible { outline: 2px solid #1a73e8; outline-offset: 2px; }

  /* Root snapshots crossfade quickly; the shared element morphs longer */
  ::view-transition-old(root), ::view-transition-new(root) {
    animation-duration: var(--motion-crossfade-duration);
    animation-timing-function: var(--motion-ease-navigation);
  }
  ::view-transition-old(product-hero), ::view-transition-new(product-hero) {
    animation-duration: var(--motion-transition-duration-shared);
    animation-timing-function: var(--motion-ease-navigation);
  }
</style>

<script>
  document.querySelector('.card').addEventListener('click', async (e) => {
    if (!document.startViewTransition) return; // unsupported: normal navigation
    e.preventDefault();
    const url = e.currentTarget.href;
    await document.startViewTransition(async () => { // data resolves before snapshot
      document.getElementById('app').innerHTML = await (await fetch(url)).text();
    }).finished; // interruptible: browser queues/reverses for new navigations
  });
</script>
```

### Example 2 — Directional sibling-route push (fallback, CSS-only)

Tokens: `assets/css/page-transitions.css`

```html
<div class="routes">
  <section class="route route--leaving">List view</section>
  <section class="route route--entering">Detail view</section>
</div>

<style>
  .routes { position: relative; overflow: hidden; }
  .route { position: absolute; inset: 0; }
  .route--entering {
    animation: push-in var(--motion-transition-duration) var(--motion-ease-navigation) both;
  }
  .route--leaving {
    animation: push-out var(--motion-transition-duration) var(--motion-ease-navigation) both;
  }
  @keyframes push-in  { from { transform: translateX(var(--motion-slide-distance)); } }
  @keyframes push-out { to   { transform: translateX(-25%); filter: brightness(0.92); } }

  /* Reduced motion: no travel — only the short root crossfade */
  @media (prefers-reduced-motion: reduce) {
    .route--entering, .route--leaving { animation: none; }
    .route--entering { animation: fade var(--motion-crossfade-duration) both; }
    @keyframes fade { from { opacity: 0; } }
  }
</style>
```

## 10. Implementation Checklist

- [ ] Total transition stays under 400ms (320ms standard routes, 400ms shared-element morphs max).
- [ ] Direction encodes hierarchy: forward = push forward, back = exact reverse; lateral tab jumps get hard cuts.
- [ ] Data is resolved before `document.startViewTransition()` fires — no flash of unstyled entering view.
- [ ] Shared elements get unique `view-transition-name`s; never reuse a name for two simultaneous elements.
- [ ] Transitions are interruptible: mid-transition navigation queues or reverses, never locks the UI or back gesture.
- [ ] Unsupported browsers fall back to a plain crossfade at `--motion-crossfade-duration`, not a broken layout.
- [ ] `prefers-reduced-motion: reduce` disables slides/morphs and keeps only the short crossfade (global override in `assets/css/page-transitions.css`).
