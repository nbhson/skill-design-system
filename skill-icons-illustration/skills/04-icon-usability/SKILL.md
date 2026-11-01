---
name: icon-usability
description: Recognition over recall — when icons need labels, the familiar-glyph rule, target sizes, and testing that catches mystery icons.
tags: [icons, usability, touch-targets, recognition, labels]
related: [icon-style-selection, icon-grid-sizing, accessible-icons]
---

# Visual Asset Guide: Icon Usability

## 1. Definition

Icons work when users recognize them instantly — and most custom icons fail that test. This guide covers the usability contracts that keep icons functional rather than decorative: the familiar-glyph rule (only universally recognized glyphs go unlabeled), the icon+label pairing for ambiguous actions, touch target sizing with a 44px effective floor, spacing that prevents mis-taps, and the testing protocol — 5-second recognition tests and first-use comprehension — that catches mystery icons before they ship. A glyph that needs explanation in a hallway test is a usability bug, no matter how elegant the stroke work.

## 2. Core Principles

- **Familiar glyphs only, or labeled:** a bare icon must be universally recognized (home, search, settings) — anything else pairs with a label.
- **Icon + label beats icon alone in navigation:** labels remove interpretation cost; icon-only nav is a statement, not a default.
- **44px effective targets:** the clickable area, not the glyph, meets the touch floor (WCAG 2.5.8) — visual size and target size are separate.
- **Spacing scales with density:** adjacent icon targets keep 8px+ separation — crowded icon rows cause mis-taps.
- **Recognition is tested, not assumed:** 5-second tests ("what does this do?") on new icons — designer certainty is not user recognition.
- **Consistency with platform conventions:** save = floppy disk survives by convention; inventing new metaphors for standard actions confuses.
- **Tooltips supplement recognition, never replace it:** the accessible name exists without hover (WCAG 1.4.13 + 2.4.6).
- **Icon-only is a budget:** icon-only controls are rationed to toolbars and nav where space is real — forms and dialogs use labels.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Familiar-glyph rule | `--icon-familiar-glyph-rule` | `universal-or-labeled` | Mystery icons banned |
| Icon-label pairing | `--icon-icon-label-pairing` | `default-for-ambiguous` | Nav items labeled by default |
| Touch target | `--icon-touch-target` | `44px-effective` | WCAG 2.5.8 effective floor |
| Target spacing | `--icon-target-spacing` | `8px-min-between` | Mis-tap prevention |
| Recognition test | `--icon-recognition-test` | `5-second-test` | New icons tested, not assumed |
| Tooltip role | `--icon-tooltip-role` | `supplement-only` | Name exists without hover |
| Icon-only budget | `--icon-icon-only-budget` | `toolbars+nav-only` | Forms/dialogs use labels |
| Platform conventions | `--icon-platform-conventions` | `standard-glyphs-standard` | Save/print/share use convention |
| Visual vs target | `--icon-visual-vs-target` | `decoupled` | Hit area >= visual size |
| Press feedback | `--icon-press-feedback` | `visible-state` | Active states confirm the press |

Consume them by linking `assets/css/icon-usability.css` once at the app root, then reading `var(--icon-...)` from component CSS and review scripts — for example, a lint rule asserting every nav link exposes a visible label unless `--icon-icon-only-budget` explicitly covers the surface. These are behavioral tokens: most are enforced in markup and tests rather than painted, but they are versioned and referenced exactly like color or spacing tokens.

## 4. Composition

- **Composes with accessible-icons (guide 05):** the naming/aria contracts pair with the recognition contracts here — a glyph that is recognizable visually and named for AT covers both audiences with one markup structure.
- **Composes with component-recipes dropdowns-menus + navigation-patterns:** icon placement in menus and nav consumes this guide's pairing rules, so icon decisions are made once, not per-component.
- **Composes with skill-design-tokens spacing:** target padding comes from the spacing scale, keeping the 44px floor and 8px gaps derived from tokens rather than magic numbers.

## 5. Signature Patterns

- **The recognition test protocol:** every new icon gets a 5-second comprehension check with 5+ users ("what does this do?"); below-threshold glyphs get labels or redesigns — the test result, not designer intuition, decides.
- **The icon+label default:** navigation and action bars ship with labels visible; icon-only is an explicit space-driven exception, documented where the trade-off was made.

## 6. Real-World Use Cases

- **Toolbars, bottom navs, and action bars** where icons dominate and the 44px/8px/target contracts carry the most interaction weight.
- **Products with novel domain concepts** that lack familiar glyphs — pipelines, workspaces, niche workflows — where labels are not optional.
- **Audit:** mystery icons, sub-44px targets, tooltip-only labels — the three most common icon-usability failures in shipped products.

## 7. Combination Notes

### With other icons-illustration skills

- **Pairs naturally with icon-style-selection and icon-grid-sizing:** style and grid decide what a glyph looks like; this guide decides whether it communicates — the contracts stack cleanly because they govern different questions.
- **Pairs with accessible-icons:** recognition (visual) and naming (AT) are two halves of one contract; the icon+label pattern from this guide is also the strongest accessible-name pattern from guide 05.
- **Pairs with icon-library-management, icon-system-audit, and svg-optimization:** the recognition test feeds the audit checklist, the library stores the passing glyphs, and optimization must not shrink targets or strip states.
- **Pairs with illustration-direction, mascot-character, and empty-error-illustrations:** illustrations follow the same recognition discipline — a decorative drawing never carries the only meaning of a control.
- **Pairs with animation-integration and favicon-app-icons:** press feedback (visible-state) is delivered by motion; app icons at small sizes obey the same familiar-glyph rule.
- **No caution or avoid list:** this guide's contracts are additive — nothing in icon work conflicts with labeling, testing, or target sizing.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles favor clean, convention-shaped glyphs that read instantly — exactly the familiar-glyph economy this guide rewards, with flat fills keeping 44px targets visually honest.
- **No caution list:** even maximalist or expressive styles benefit from labeled nav and tested glyphs; style changes the artwork, never the recognition contract.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions and feedback-confirmation:** `--icon-press-feedback: visible-state` is delivered through motion — a scale/opacity dip on press confirms the tap without moving the target under the finger.
- **No caution list:** press feedback and label reveals are short, user-initiated transitions; they do not conflict with reduced-motion when implemented as opacity/transform shifts.

## 8. Anti-Patterns

- **Mystery meat icons** — unlabeled novel glyphs users must hover-hunt
- **Tiny targets** — 24px glyphs as the entire touch surface
- **Crowded icon rows** — adjacent targets under 8px apart
- **Reinvented metaphors** — a custom 'save' glyph that means nothing

### Accessibility Notes

Icon usability implements WCAG 2.5.8 (target size), 2.4.6 (headings and labels), and 1.4.13: 44px effective targets, a visible name/label or accessible name, and tooltips that never carry the only meaning — recognition must not require hover precision. This is why the tooltip token is `supplement-only`: the accessible name must exist in the DOM without any pointer interaction, which is also what makes the icon+label pattern the safest default, since the visible label doubles as the accessible name. The fallback rule: where labels cannot fit (dense toolbars), ensure aria-labels + tooltips + a documented icon legend — and schedule recognition testing before wide release, because a dense toolbar that fails the 5-second test fails sighted and AT users in different but equally real ways.

## 9. Code Examples

### Example 1 — Icon+label navigation with 44px targets

Tokens: `assets/css/icon-usability.css`

```html
<nav class="tabbar" aria-label="Primary">
  <a class="tab is-active" href="#home" aria-current="page">
    <svg class="tab-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path d="M3 11.5 12 4l9 7.5V21h-6v-6H9v6H3z"/>
    </svg>
    <span class="tab-label">Home</span>
  </a>
  <a class="tab" href="#search">
    <svg class="tab-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path d="M10.5 3a7.5 7.5 0 1 1 0 15 7.5 7.5 0 0 1 0-15zm5.8 12.7 4.5 4.5-1.6 1.6-4.5-4.5z"/>
    </svg>
    <span class="tab-label">Search</span>
  </a>
  <a class="tab" href="#settings">
    <svg class="tab-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path d="M12 8a4 4 0 1 1 0 8 4 4 0 0 1 0-8zm0 2.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"/>
    </svg>
    <span class="tab-label">Settings</span>
  </a>
</nav>
<style>
  .tabbar {
    display: flex;
    gap: var(--icon-target-spacing, 8px); /* 8px-min-between */
    padding: 8px;
    background: #fff;
    border-top: 1px solid #e5e5e5;
    font: 12px/1 system-ui, sans-serif;
  }
  .tab {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    min-height: 44px; /* --icon-touch-target: 44px-effective */
    min-width: 44px;
    color: #737373;
    text-decoration: none;
    border-radius: 8px;
  }
  .tab-icon { width: 22px; height: 22px; fill: currentColor; }
  .tab:hover { color: #171717; }
  .tab.is-active { color: #2563eb; }
  .tab:active { background: #f5f5f5; } /* --icon-press-feedback: visible-state */
  .tab:focus-visible { outline: 2px solid #2563eb; outline-offset: 2px; }
</style>
```

### Example 2 — 5-second recognition test harness

```html
<div class="test-card">
  <p class="test-step" id="stepLabel">Step 1 of 3 — study the icon</p>
  <div class="test-stage">
    <svg id="testIcon" class="test-icon" viewBox="0 0 24 24" role="img" aria-label="Test icon under review">
      <path d="M4 5h16v3H4zm0 5.5h16v3H4zm0 5.5h10v3H4z"/>
    </svg>
  </div>
  <button class="test-btn" id="revealBtn" type="button">Reveal intended meaning</button>
  <p class="test-verdict" id="verdict" hidden>Intended meaning: <strong>Activity log</strong></p>
</div>
<style>
  .test-card { max-width: 320px; padding: 24px; border: 1px solid #e5e5e5; border-radius: 8px; font: 14px/1.5 system-ui, sans-serif; }
  .test-step { margin: 0 0 16px; color: #737373; }
  .test-stage { display: grid; place-items: center; height: 88px; margin-bottom: 16px; background: #f5f5f5; border-radius: 8px; }
  .test-icon { width: 44px; height: 44px; fill: #171717; }
  .test-btn { min-height: 44px; padding: 0 16px; border: none; border-radius: 8px; background: #2563eb; color: #fff; font-weight: 600; cursor: pointer; }
  .test-verdict { margin: 16px 0 0; color: #171717; }
</style>
<script>
  // --icon-recognition-test: 5-second-test — show the glyph 5s, then reveal. Pass >= 4/5 correct guesses with 5+ participants; otherwise label or redesign.
  let started = Date.now();
  document.getElementById('revealBtn').addEventListener('click', () => {
    const elapsed = Math.round((Date.now() - started) / 1000);
    document.getElementById('verdict').hidden = false;
    document.getElementById('stepLabel').textContent =
      'Guessed at ' + elapsed + 's — log the guess before revealing to the next participant.';
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every unlabeled icon is a universally familiar glyph (`--icon-familiar-glyph-rule`) — anything novel ships with a visible label.
- [ ] Navigation and action bars default to icon+label (`--icon-icon-label-pairing`); icon-only surfaces are documented exceptions under `--icon-icon-only-budget`.
- [ ] All clickable icon areas meet `--icon-touch-target` (44px effective); the hit area is decoupled from visual glyph size.
- [ ] Adjacent icon targets keep `--icon-target-spacing` (8px minimum) on every density.
- [ ] Each new icon passes the `--icon-recognition-test` (5-second test, 5+ users) before merge.
- [ ] Tooltips are `supplement-only`: the accessible name exists without hover, and tooltip text matches the label string.
- [ ] Standard actions (save/print/share) use conventional glyphs per `--icon-platform-conventions`.
- [ ] Press feedback is a visible state on every icon control, per `--icon-press-feedback`.
