---
name: responsive-images
description: srcset/sizes, art direction, modern formats, and lazy loading — images that ship the right bytes for every slot and bandwidth.
tags: [responsive, images, performance, srcset, lazy-loading]
related: [grid-systems, breakpoints-strategy, layout-compositions]
---

# Responsive Layout Skill: Responsive Images & Media

## 1. Definition

Images dominate page weight; responsive image technique ships the right pixels for the slot: `srcset`/`sizes` for resolution switching, `<picture>` for art direction (different crops per viewport), AVIF/WebP with fallbacks, lazy loading below the fold, and `aspect-ratio` boxes that reserve space (zero CLS). The skill is treating images as layout citizens — sized by tokens, loaded strategically, never causing shift. An image is not a blob dropped into a page; it is a component with a slot contract (what width will I render at), a loading contract (when do my bytes arrive), and an accessibility contract (what do I mean to someone who cannot see me). Teams that master this skill turn images from the top source of performance regressions into a predictable, testable part of the layout system.

## 2. Core Principles

- **srcset + sizes for the common case:** let the browser pick from a width descriptor list; `sizes` must match the actual rendered slot — a wrong `sizes` is worse than none, because it lies to the selection algorithm.
- **Art direction via `<picture>` only when crops differ:** a mobile hero that needs a tighter crop is `<picture>`; mere resizing is `srcset`. Reaching for `<picture>` for every image multiplies asset maintenance for no gain.
- **AVIF first, WebP fallback:** modern formats cut 30–50% of JPEG weight; the `type` attribute negotiates per browser so old clients degrade cleanly.
- **Lazy-load below the fold:** `loading="lazy"` on non-critical images; above-the-fold stays eager + preload for LCP.
- **Aspect-ratio boxes kill CLS:** `width`/`height` or `aspect-ratio` on every img — space reserved before bytes arrive, so the page never jumps on load.
- **Object-fit for slot-filling:** `cover`/`contain` semantics explicit — never distort; focal point via `object-position` for crops.
- **LCP image is special:** preload it, `fetchpriority="high"`, no lazy — the largest contentful paint drives perceived speed.
- **Alt text is part of the image contract:** every meaningful image ships with alt (a11y repo media-alt-text); decorative images ship `alt=""` explicitly, never by omission.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Resolution ladder | `--layout-img-resolution-srcset` | `480w,800w,1200w,2000w` | Standard width descriptor ladder |
| Sizes policy | `--layout-img-sizes-policy` | `match-rendered-slot` | sizes attr mirrors the layout's real slot width |
| Format stack | `--layout-img-format-stack` | `avif,webp,jpeg` | `<picture>` type negotiation order |
| Art direction | `--layout-img-art-direction` | `picture-only-for-crops` | Different crops per viewport; not mere resizing |
| Loading fold | `--layout-img-loading-fold` | `eager-above-lazy-below` | loading=lazy below fold; eager + preload for LCP |
| LCP contract | `--layout-img-lcp` | `preload+fetchpriority-high` | Hero/LCP image contract |
| Aspect reservation | `--layout-img-aspect-reserved` | `aspect-ratio-set` | Zero CLS: space reserved pre-load |
| Object fit | `--layout-img-object-fit` | `cover-or-contain` | Slot-filling semantics; never distort |
| Fluid base | `--layout-img-max-width` | `100%` | Fluid base: images never overflow containers |
| Decode | `--layout-img-decode-async` | `decoding-async` | Off-main-thread decode for large images |

Consume them by linking `assets/css/responsive-images.css` once at the app root, then referencing `var(--layout-img-...)` from image components and CI rules — the tokens encode the *policy* (which ladder, which fold rule) so components stay declarative. If a new width or format seems necessary, extend the token set through review, never by hand-editing one `<img>`.

## 4. Composition

- **Composes with layout compositions:** slot sizes (sidebar, card, hero) generate the `sizes` attribute values — layout informs loading, so an image component must know which slot it renders in to pick the right width hints.
- **Composes with perceived-performance (skill-design-review guide 10):** LCP/CLS from images are the top perceptual-speed factors; the image loading contract and the perf budget are two views of the same discipline.
- **Composes with skill-animation scroll-animation:** parallax/lazy-reveal images follow the same loading discipline — reveal effects never change *what* loads, only *when* it paints.

## 5. Signature Patterns

- **Image component with slots:** one `<Image>` wrapper consuming slot tokens (card/hero/sidebar) and emitting the correct `srcset`/`sizes`/`lazy`/`preload` attributes — authors declare the slot, the component emits the contract.
- **Zero-CLS rule:** CI checks every `img` for explicit dimensions or `aspect-ratio`; a shift-causing image fails the build. Layout stability is enforced by tooling, not by vigilance.

## 6. Real-World Use Cases

- **E-commerce grids:** hundreds of product images sized right per card — a 300px card slot should never receive a 2000w file.
- **Editorial/hero pages with art-direction crops:** wide cinematic crop on desktop, tight focal crop on mobile, one semantic payload.
- **Perf audits:** LCP, CLS, and wasted bytes from oversized images — the three findings this skill eliminates.

## 7. Combination Notes

### With other responsive-layout skills

- **Good with nearly everything — grid-systems, breakpoints-strategy, fluid-container-queries, flexbox-patterns, css-grid-patterns, layout-compositions, mobile-navigation, data-tables-responsive, intrinsic-design, rtl-i18n-layout, responsive-testing:** images are layout citizens, and every one of these skills defines the slot an image renders into. `sizes` is generated *from* the grid/layout slot; container queries make image adaptation slot-local; responsive-testing verifies the ladder at each width. There is no caution or avoid list because image loading is orthogonal to layout structure — the contracts compose without conflict.
- **Why the pairing is strict:** the one hard rule is that layout must inform loading. An image component that guesses its slot ("just use 100vw") breaks the moment it lands in a sidebar, which is exactly what the composition partners exist to prevent.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and collage-art:** minimalism wants few, perfectly-sized media; flat-design keeps imagery decorative-light and fast; collage-art wants many images in mixed slots — which is precisely what slot-driven `sizes` and `aspect-ratio` reservation make safe. In all three, disciplined image loading is a visual-quality requirement, not just a perf one.
- **No caution list:** because this skill constrains engineering (bytes, timing, stability) rather than visual treatment, no style conflicts with it — styles decide *what* the image looks like, this skill decides *how* it arrives.

### With motion skills (companion repo skill-animation)

- **Good affinity with scroll-animation:** scroll-linked reveals and lazy loading share a timing contract — the image loads (eager/lazy decision) before the animation reveals it, so motion never waits on decode and never animates an empty box.
- **Caution in spirit, not rule:** scroll effects that scale or translate large images can push repaint costs up; keep `decoding="async"` and respect the aspect-reserved box so animated media never causes shift — the motion should move the *reserved* box, not introduce new layout.

## 8. Anti-Patterns

- **Desktop images everywhere** — 2000w hero rendered in a 300px slot
- **CLS by images** — no dimensions on img - the whole page jumps on load
- **Lazy LCP** — loading=lazy on the hero image, tanking the largest paint
- **Distorted fills** — stretched thumbnails from missing object-fit

### Accessibility Notes

Every informative image carries alt (a11y repo guide 09); decorative images are explicitly `alt=""` — omission is not a strategy, because screen readers then announce filenames. Aspect-ratio reservation is itself an accessibility feature: it prevents the layout jumps that disorient zoom and screen-magnifier users mid-read, complementing WCAG 1.4.4/1.4.10 reflow requirements. The fallback rule: if art direction cannot be produced per viewport, ship one well-cropped 16:9 master with `object-fit` — a single good crop beats three bad ones, and a single crop keeps one alt payload consistent across every variant.

## 9. Code Examples

### Example 1 — Hero with art direction, LCP contract, and zero CLS

Tokens: `assets/css/responsive-images.css`

```html
<!-- LCP hero: eager, preloaded, fetchpriority=high; aspect-ratio reserves space -->
<link rel="preload" as="image" href="hero-1200w.avif" fetchpriority="high"
      media="(max-width: 767px)" />
<picture class="hero-media">
  <!-- Art direction: mobile gets a tighter 4:5 crop -->
  <source media="(max-width: 767px)" type="image/avif"
          srcset="hero-mobile-480w.avif 480w, hero-mobile-800w.avif 800w"
          sizes="calc(100vw - var(--layout-img-inset, 16px))" />
  <source media="(max-width: 767px)" type="image/webp"
          srcset="hero-mobile-480w.webp 480w, hero-mobile-800w.webp 800w"
          sizes="calc(100vw - var(--layout-img-inset, 16px))" />
  <source type="image/avif"
          srcset="hero-800w.avif 800w, hero-1200w.avif 1200w, hero-2000w.avif 2000w"
          sizes="(min-width: 1024px) 60vw, 100vw" />
  <img src="hero-1200w.jpg"
       srcset="hero-800w.jpg 800w, hero-1200w.jpg 1200w, hero-2000w.jpg 2000w"
       sizes="(min-width: 1024px) 60vw, 100vw"
       width="1200" height="675" alt="Product analytics dashboard overview"
       fetchpriority="high" decoding="async" />
</picture>
<!-- Below the fold: lazy, reserved box, no preload -->
<img class="thumb" src="chart-800w.avif"
     srcset="chart-480w.avif 480w, chart-800w.avif 800w, chart-1200w.avif 1200w"
     sizes="(min-width: 768px) 320px, 90vw"
     width="800" height="450" alt="Weekly active users trend"
     loading="lazy" decoding="async" />
<style>
  /* var(--layout-img-max-width) = 100% — fluid base, images never overflow */
  .hero-media img, .thumb {
    display: block;
    max-width: var(--layout-img-max-width);
    height: auto;
    /* var(--layout-img-object-fit) = cover-or-contain — explicit, never distort */
    object-fit: cover;
  }
  /* var(--layout-img-aspect-reserved) = aspect-ratio-set — zero CLS */
  .hero-media { aspect-ratio: 16 / 9; }
  .hero-media img { width: 100%; height: 100%; }
  .thumb { width: 100%; aspect-ratio: 16 / 9; }
</style>
```

### Example 2 — Card image with slot-driven sizes and a loading contract check

```html
<div class="card">
  <img class="card-img" src="product-800w.avif"
       srcset="product-480w.avif 480w, product-800w.avif 800w"
       sizes="300px" width="800" height="800" alt="Standing desk, oak finish"
       loading="lazy" decoding="async" />
  <h3>Oak Standing Desk</h3>
</div>
<script>
  // Zero-CLS contract: every img must declare dimensions (aspect-ratio-set)
  document.querySelectorAll('img').forEach((img) => {
    const reserved = img.getAttribute('width') && img.getAttribute('height');
    console.assert(reserved, `img "${img.alt}" must reserve space (width/height)`);
    // LCP contract: the hero is never lazy (eager-above-lazy-below)
    if (img.closest('.hero-media')) {
      console.assert(img.loading !== 'lazy', 'LCP image must not be lazy');
    }
  });
</script>
<style>
  .card { max-width: 300px; font: 14px/1.5 system-ui, sans-serif; }
  .card-img {
    width: var(--layout-img-max-width);
    aspect-ratio: 1 / 1;      /* reserved box: no shift when bytes land */
    object-fit: cover;        /* slot-fill without distortion */
    border-radius: 8px;
  }
  .card h3 { margin: 12px 0 0; font-size: 16px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every `img` has explicit `width`/`height` or CSS `aspect-ratio` (var(--layout-img-aspect-reserved)) — CI fails on shift-causing images.
- [ ] `sizes` values are generated from the real rendered slot (var(--layout-img-sizes-policy)), reviewed whenever a slot changes.
- [ ] `srcset` ladders use the standard width list (var(--layout-img-resolution-srcset)); no one-off widths per image.
- [ ] `<picture>` is used only where crops genuinely differ per viewport (var(--layout-img-art-direction)); format stack is avif→webp→jpeg (var(--layout-img-format-stack)).
- [ ] The LCP image is eager, preloaded, and `fetchpriority="high"` (var(--layout-img-lcp)); everything below the fold is `loading="lazy"` (var(--layout-img-loading-fold)).
- [ ] Slot-filling images declare `object-fit: cover` or `contain` (var(--layout-img-object-fit)) — no distorted fills.
- [ ] All images respect `max-width: 100%` (var(--layout-img-max-width)) and use `decoding="async"` (var(--layout-img-decode-async)).
- [ ] Every informative image has meaningful alt text; decorative images ship explicit `alt=""`.
