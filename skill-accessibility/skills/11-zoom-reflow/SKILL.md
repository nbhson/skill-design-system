---
name: zoom-reflow
description: 200% zoom, 320px reflow, orientation lock, and pointer alternatives - the responsive side of WCAG (1.4.4, 1.4.10, 1.3.4, 2.5.x).
tags: [zoom, reflow, responsive, wcag, low-vision]
related: [wcag-fundamentals, keyboard-navigation, testing-audit]
---

# Accessibility Skill: Zoom, Reflow & Responsive A11y

## 1. Definition

Users zoom: to 200% text (WCAG 1.4.4), to 400% with single-column reflow at 320 CSS px (1.4.10), and they rotate devices (1.3.4) and use pointers of every kind (2.5.x). This skill covers the WCAG criteria that live at the intersection of responsive design and accessibility - where a layout that works at 1440px quietly fails at 400% zoom on a laptop, which is exactly where many low-vision users actually browse. Low vision is the largest single accessibility population, and its primary assistive technology is not a screen reader but the browser zoom control; every layout decision here is therefore a mainstream decision with an accessibility contract attached.

## 2. Core Principles

- **200% text zoom must keep function:** text scales via rem/vw tokens; no clipped controls, no overlaps (WCAG 1.4.4).
- **400% zoom reflows to one column at 320px:** no two-dimensional scrolling for reading (WCAG 1.4.10).
- **Orientation is never locked:** support both portrait and landscape unless essential (WCAG 1.3.4).
- **Pointer gestures have single-pointer alternatives:** multipoint/path-based gestures get simple taps (WCAG 2.5.1).
- **Dragging has a non-drag path:** reorder-by-drag offers up/down buttons or a list mode (WCAG 2.5.7, new in 2.2).
- **Pointer targets meet the 24px floor:** 24x24 CSS px minimum, 44px preferred (WCAG 2.5.8).
- **Hover content is dismissible, hoverable, persistent:** tooltips that trap the cursor fail 1.4.13.
- **Character key shortcuts are remappable:** or active only on focus (WCAG 2.1.4).

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Text zoom | `--a11y-text-zoom-tested` | `200%` | WCAG 1.4.4: all flows pass at 200% text-only zoom |
| Reflow | `--a11y-reflow-width` | `320px` | WCAG 1.4.10: single column, no 2D scroll at 400% |
| Zoom strategy | `--a11y-zoom-strategy` | `rem-vw-tokens` | Type tokens in rem; spacing may stay px-fixed |
| Orientation | `--a11y-orientation-policy` | `both-supported` | WCAG 1.3.4 unless orientation is essential |
| Gesture | `--a11y-gesture-alternative` | `single-tap` | WCAG 2.5.1: simple pointer alternative for gestures |
| Drag | `--a11y-drag-alternative` | `buttons-or-list` | WCAG 2.5.7: non-drag reorder path |
| Target size | `--a11y-target-size-min` | `24px` | WCAG 2.5.8 floor; 44px per design-tokens spacing guide |
| Hover content | `--a11y-hover-content` | `dismissible-hoverable-persistent` | WCAG 1.4.13 content-on-hover contract |
| Motion trigger | `--a11y-motion-trigger-policy` | `user-initiated-only` | WCAG 2.3.1: no parallax/shake without opt-in |
| Shortcuts | `--a11y-shortcut-policy` | `remap-or-focus-only` | WCAG 2.1.4 character shortcuts |

Consume them by linking `assets/css/zoom-reflow.css` once at the app root, then reading `var(--a11y-reflow-width)` in media queries (`@media (max-width: 320px)` or the zoom-equivalent `(max-width: 1280px)` at 400%), `var(--a11y-target-size-min)` in component min-height/min-width rules, and `var(--a11y-hover-content)` in tooltip component contracts. The values are testing commitments, not styling values: a release that has not passed the 200%/400% passes has not satisfied the tokens.

## 4. Composition

- **Composes with skill-responsive-layout:** that repo builds the responsive mechanics (breakpoints, grids, container queries); this skill states the WCAG constraints they must satisfy - reflow at 320px, no 2D scroll, targets 24px+.
- **Composes with design-tokens (skill-design-tokens):** rem-based type tokens and 44px touch targets are token-level guarantees for 1.4.4 and 2.5.8; a px-locked type scale fails this skill by construction.
- **Composes with skill-animation:** motion-trigger and reduced-motion policies are the animation-side twins of WCAG 2.3.1 - motion initiated by scroll or hover must be opt-in, pauseable, and respectful.

## 5. Signature Patterns

- **Zoom-first QA:** run core flows at 200% text zoom and 400% page zoom before release; screenshot the failures as tickets. This flips the default QA order - zoom is tested first, not as a final polish pass.
- **Reflow smoke test:** a 320px viewport walkthrough where every reading surface must be single-column and every control reachable. Ten minutes per release; catches the 1.4.10 failures automation misses.

## 6. Real-World Use Cases

- **Low-vision users (the majority of accessibility needs)** who browse at high zoom.
- **Responsive redesigns claiming WCAG conformance.**
- **Drag-and-drop interfaces needing 2.5.7 alternatives.**

## 7. Combination Notes

### With other accessibility skills

- **Good with keyboard-navigation and focus-management:** at 400% zoom the visible viewport shrinks, so focus moves and scroll-into-view behavior must land the focused control on screen - keyboard and zoom failures compound.
- **Good with color-contrast:** zoom magnifies anti-aliased edges and thin borders; contrast pairings must still hold when 1px borders become the only control boundary visible at 320px.
- **Good with forms-errors and aria-patterns-widgets:** labels, error summaries, and widget keymaps must survive reflow - a two-column form collapsing to one must not orphan its labels.
- **Good with wcag-fundamentals and testing-audit:** 1.4.4/1.4.10/2.5.x are fixed lanes in the audit checklist, and zoom passes are scripted there rather than ad hoc.
- **Caution/avoid: none.** Reflow is a property every component must satisfy, so no sibling skill conflicts with it.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** single-column, few-elements layouts reflow trivially; there is little density to break at 320px, and generous whitespace keeps targets above the 24px floor naturally.
- **Caution with collage-art and maximalism:** overlapping layers, rotated elements, and dense multi-column grids are the first things to clip or stack wrongly at 400% zoom. If used, restrict them to hero/marketing surfaces and keep task flows on a reflow-safe grid.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion and easing-timing:** motion triggered by scroll or device orientation must be user-initiated per `--a11y-motion-trigger-policy`, and token-driven easing keeps transitions smooth rather than jarring at high zoom.
- **Caution with scroll-animation and ambient-motion:** scroll-jacking and parallax are exactly what WCAG 2.3.1 restricts - motion triggered by scrolling without opt-in fails the criterion and destabilizes reflowed layouts; gate both behind explicit user activation.

## 8. Anti-Patterns

- **Px-locked text** — font sizes that ignore 200% zoom until controls clip and overlap
- **Hover traps** — tooltips following the cursor with no Escape, spreading over content
- **Drag-only reorder** — lists sortable by drag with no button alternative (2.5.7)
- **Desktop-only testing** — layouts signed off at 1440px and broken at 320px/400% where low-vision users live

### Accessibility Notes

This guide owns WCAG 1.4.4, 1.4.10, 1.4.13, 1.3.4, 2.1.4, 2.3.1, and the 2.5.x pointer criteria - the responsive half of conformance. These criteria are cheap to satisfy at design time (rem type, fluid grids, button alternatives beside drag) and expensive to retrofit after build, which is why the zoom-first QA pattern exists: the failure is found at 400% zoom in ten minutes instead of in an audit months later. The fallback rule covers the honest exception: where 2D scroll is unavoidable (data grids, spreadsheets), provide the data in an alternative single-column view - the WCAG 1.4.10 exception explicitly requires it, so the alternative view is not optional polish but part of conformance.

## 9. Code Examples

### Example 1 — rem type with clamp() that survives 200%/400% zoom

Tokens: `assets/css/zoom-reflow.css`

```html
<article class="card">
  <h1>Quarterly billing summary</h1>
  <p>Your invoice for Q3 is ready. Total due: $248.00.</p>
  <button class="btn">Download invoice</button>
</article>
<style>
  /* Type in rem + clamp: text scales with user zoom (--a11y-zoom-strategy: rem-vw-tokens) */
  .card { max-width: 42rem; margin: 0 auto; padding: 1.5rem; }
  .card h1 { font-size: clamp(1.5rem, 1.2rem + 1.5vw, 2.25rem); line-height: 1.2; }
  .card p  { font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem); line-height: 1.6; }
  /* Single column below 320px equivalent --a11y-reflow-width; no 2D scroll at 400% */
  @media (max-width: 20rem) {
    .card { padding: 1rem; }
  }
  .btn {
    display: inline-block; min-height: 44px; padding: 0.75rem 1.25rem; /* 2.5.8: 44px preferred */
    font-size: 1rem; border: none; border-radius: 8px;
    background: #1D4ED8; color: #fff; cursor: pointer;
  }
  .btn:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; }
</style>
```

### Example 2 — 320px reflow grid + dismissible tooltip (1.4.13)

Tokens: `assets/css/zoom-reflow.css`

```html
<div class="grid">
  <section class="cell">Balance<br><strong>$1,204.55</strong></section>
  <section class="cell">Due date<br><strong>Nov 15</strong></section>
  <section class="cell actions">
    <button class="btn-icon" id="help-btn" aria-describedby="tip" aria-expanded="false">?</button>
    <span id="tip" class="tooltip" role="tooltip" hidden>Opens the billing help center in a new page.</span>
    <button class="btn-icon">⚙</button>
  </section>
</div>
<script>
  // --a11y-hover-content (dismissible-hoverable-persistent): Escape dismisses; it stays until dismissed
  const btn = document.getElementById('help-btn'), tip = document.getElementById('tip');
  btn.addEventListener('click', () => {
    const open = tip.hidden;
    tip.hidden = !open;
    btn.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !tip.hidden) { tip.hidden = true; btn.setAttribute('aria-expanded', 'false'); btn.focus(); }
  });
</script>
<style>
  /* Reflows to one column at 320px (--a11y-reflow-width: 320px) */
  .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 640px; margin: 0 auto; font: 14px/1.5 system-ui, sans-serif; }
  @media (max-width: 320px) { .grid { grid-template-columns: 1fr; } }
  .cell { padding: 12px; border: 1px solid #D4D4D4; border-radius: 8px; }
  .actions { display: flex; gap: 8px; align-items: center; }
  .btn-icon { width: 44px; height: 44px; border: 1px solid #1D4ED8; border-radius: 8px; background: #fff; color: #1D4ED8; font: 600 16px/1 system-ui, sans-serif; cursor: pointer; }
  .tooltip { position: absolute; margin-top: 6px; padding: 8px 10px; max-width: 240px; border-radius: 8px; background: #171717; color: #fff; }
</style>
```

## 10. Implementation Checklist

- [ ] All type and layout-critical dimensions use rem/clamp tokens per `--a11y-zoom-strategy: rem-vw-tokens`.
- [ ] Core flows pass at 200% text zoom with no clipped controls (`--a11y-text-zoom-tested`).
- [ ] At 320px width / 400% zoom, every reading surface is a single column with no 2D scroll (`--a11y-reflow-width`).
- [ ] Both orientations work; no CSS or JS orientation lock without an essential exception (`--a11y-orientation-policy`).
- [ ] Every drag-to-reorder control ships a button or list alternative (`--a11y-drag-alternative`).
- [ ] All pointer targets are at least 24px, preferably 44px (`--a11y-target-size-min`).
- [ ] Tooltips are dismissible via Escape, hoverable, and persistent (`--a11y-hover-content`).
- [ ] No motion, parallax, or shake triggers on scroll/hover without explicit opt-in (`--a11y-motion-trigger-policy`).