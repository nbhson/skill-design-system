---
name: dark-mode
description: Re-pointing semantic aliases into a dark theme — surface inversion, elevation physics, saturation control, and contrast that survives the swap; not "invert the colors."
tags: [dark-mode, theming, tokens, contrast, accessibility]
related: [semantic-alias-naming, color-tokens, contrast-validation]
---

# Design Token Skill: Dark Mode Theming

## 1. Definition

Dark mode is a theme expressed as a **second alias mapping**: the same semantic vocabulary (`color-bg-surface`, `color-text-primary`) points at different primitive values. Done well, it is not "invert the colors" — dark themes need desaturated brand steps, elevated surfaces that get lighter as they rise, shadows replaced by borders, and every alias pairing re-validated for contrast. The token architecture decides whether dark mode is a one-sprint job or a code-wide rewrite: with a disciplined alias tier, dark mode is one re-pointing block; without it, it is a per-component archaeology project.

## 2. Core Token Principles

- **Never invert, re-map:** rebuild alias values against dark-surface physics; inverting #111 text gives #EEE text but breaks every feedback hue in between.
- **Elevated surfaces get lighter, not shadowed:** dark cards rise from #1C1C1E toward #2C2C2E; lightness carries altitude where shadows cannot.
- **Desaturate by altitude:** brand-500's dark-theme sibling is lighter and less saturated (e.g. #60A5FA) so it does not vibrate on dark surfaces.
- **Shadows become borders:** pair every elevation level with a subtle border alias; pure shadows disappear on dark backgrounds.
- **Avoid pure white text on pure black:** #FAFAFA on #0A0A0A reduces halation and glare while still passing AAA.
- **Dark mode is a user setting, not a schedule:** respect prefers-color-scheme as default, expose an explicit toggle, and persist the choice.
- **Every state axis re-validates:** hover/pressed/disabled pairings pass contrast in BOTH themes — a 3:1 hover delta in light may vanish in dark.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Scheme | `--dt-color-scheme` | `light dark` | Declares both schemes; enables native form/scrollbar adaptation |
| Background | `--dt-color-bg-default-dark` | `#0A0A0A` | Page background; never pure #000 for long sessions |
| Background | `--dt-color-bg-surface-dark` | `#1C1C1E` | Cards, sheets at elevation-1 |
| Background | `--dt-color-bg-elevated-dark` | `#2C2C2E` | Dropdowns/modals; lightness carries altitude |
| Text | `--dt-color-text-primary-dark` | `#FAFAFA` | Body text; 17.9:1 on bg-default-dark, no halation |
| Text | `--dt-color-text-secondary-dark` | `#A3A3A3` | Meta text; 7.1:1 on bg-default-dark |
| Border | `--dt-color-border-dark` | `#2E2E30` | Replaces shadows as the depth cue at every elevation |
| Action | `--dt-color-action-primary-dark` | `#60A5FA` | Desaturated brand step; #0A0A0A text on it passes 8.9:1 |
| Overlay | `--dt-color-overlay-scrim` | `rgba(0, 0, 0, 0.60)` | Modal scrim; lighten to 0.40 in dark to avoid pitch-black |
| Elevation | `--dt-elevation-2-dark` | `0 0 0 1px #2E2E30, 0 4px 12px rgba(0,0,0,0.50)` | Border-led shadow variant for dark elevation-2 |

Consume them by linking `assets/css/dark-mode.css` after the light theme's alias file, then referencing the *semantic* aliases (`var(--dt-color-bg-surface)`, `var(--dt-color-text-primary)`) as usual — the `-dark` values above are what those aliases re-point to inside `[data-theme='dark']`. Components never read a `-dark` token directly; the theme attribute decides which value an alias resolves to.

## 4. Composition & Layering

- Dark mode composes with alias naming: it re-points the semantic tier and adds -dark elevation/border aliases; primitives and component tokens stay untouched.
- It composes with contrast-validation: every alias pairing ships with both light and dark ratios; a pairing without a dark ratio is not done.
- It composes with component-tokens: components consume semantic aliases so they inherit the theme with zero component changes — any component requiring dark overrides is a bug.

## 5. Signature Patterns

- **data-theme attribute + CSS custom properties:** `[data-theme='dark'] { --dt-color-bg-default: ... }` — one block re-points all aliases; OS sync via prefers-color-scheme default.
- **color-scheme per theme:** set `color-scheme: dark` on the dark root so scrollbars, form controls, and rendering adapt natively.

## 6. Real-World Use Cases

- **Adding dark mode to an existing product** built on semantic aliases.
- **Developer tools, media apps, and dashboards** where long sessions demand dark ergonomics.
- **Audit:** verifying every semantic pairing's contrast in both themes, not just light.

## 7. Combination Notes

### With other token skills

- **Pairs well with semantic-alias-naming, color-tokens, and contrast-validation:** this skill is the proof-of-concept for the alias architecture — it re-points the tier color-tokens provides and depends on contrast-validation to certify both theme cells of every pairing.
- **Pairs well with radius-elevation, typography-tokens, platform-mapping, token-pipeline-figma, component-tokens, and governance-migration:** elevation re-maps for dark physics, type tokens stay theme-invariant so text metrics never shift, and the pipeline generates and validates both theme cells through the same governance flow.
- **Caution with spacing-sizing:** dark mode does not change layout, so spacing should be untouched — if a dark layout needs different spacing, something else is wrong; resist "fixing" density while theming.
- **Caution with multi-brand-theming:** the matrix is brands x themes, so each brand's primitives need their own validated dark pairings — budget for it rather than assuming a dark theme ports across brands for free.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, aurora-ui, and glassmorphism:** dark surfaces reward restrained palettes and luminous accent glows — these styles read best when elevation is carried by lightness and desaturated brand steps, exactly the dark-mode token physics.
- **Caution with skeuomorphism:** texture- and realism-heavy styles assume light-surface shadow rendering; dark physics flatten those cues, so a skeuomorphic dark theme needs a deliberate re-interpretation, not a value swap.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** theme switches themselves should animate on motion tokens — a short (~240ms) opacity or color transition between theme cells keeps the swap from flashing; both themes share the same duration/easing scale.
- **Caution with illustration-lottie:** baked illustrations authored for light backgrounds (dark outlines, white fills) break on dark surfaces; assets need dark variants or theme-aware compositions before the theme ships.

## 8. Anti-Patterns

- **Filter inversion:** hue-rotate/invert hacks that turn brand colors neon and photos eerie
- **Pure black + pure white:** #000/#FFF maximizes halation and eye strain in long sessions
- **Light-theme shadows on dark surfaces:** invisible depth; dark elevation needs lightness + borders
- **Dark mode as afterthought:** bolted-on dark colors with unvalidated pairings, broken state axes, and unreadable feedback hues

### Accessibility Notes

Dark mode is an accessibility feature and an accessibility risk at once: it serves photosensitive and low-vision users, but every alias pairing must re-pass WCAG 1.4.3/1.4.11 in the dark theme, and state axes (hover/focus) must keep a visible delta — a hover cue that relied on a light-theme shadow vanishes on dark surfaces. The fallback is explicit: if a component's dark pairing fails contrast, ship the component in light-forced mode behind an explicit ticket rather than shipping a failing dark pairing. Always sync with `prefers-color-scheme` so the OS-level accessibility setting (including system-wide high-contrast or dimmed-screen preferences) is honored as the default, while an explicit in-app toggle with persistence wins once the user has expressed a choice.

## 9. Code Examples

### Example 1 — data-theme alias re-pointing with prefers-color-scheme sync

Tokens: `assets/css/dark-mode.css`

```html
<article class="card">
  <h2>Deploy complete</h2>
  <p>Build #482 shipped to production in 3m 12s.</p>
  <button class="btn">View release</button>
</article>
<style>
  :root {
    color-scheme: light dark; /* native scrollbars/forms adapt per scheme */
    /* Light aliases */
    --dt-color-bg-surface: #FFFFFF;      --dt-color-text-primary: #171717;
    --dt-color-text-secondary: #404040;  --dt-color-action-primary: #2563EB;
    --dt-color-text-on-action: #FFFFFF;  --dt-color-border-default: #E4E7EC;
    --dt-elevation-2: 0 2px 4px rgba(16,24,40,0.06), 0 4px 8px rgba(16,24,40,0.10);
  }
  /* Explicit toggle wins over OS preference; values re-pointed, not inverted */
  [data-theme='dark'] {
    --dt-color-bg-surface: #1C1C1E;      --dt-color-text-primary: #FAFAFA;
    --dt-color-text-secondary: #A3A3A3;  --dt-color-action-primary: #60A5FA; /* desaturated brand step */
    --dt-color-text-on-action: #0A0A0A;  --dt-color-border-default: #2E2E30; /* borders replace shadows */
    --dt-elevation-2: 0 0 0 1px #2E2E30, 0 4px 12px rgba(0,0,0,0.50);
  }
  /* OS sync: when the user has NOT chosen a theme, follow the system */
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme='light']) {
      --dt-color-bg-surface: #1C1C1E;      --dt-color-text-primary: #FAFAFA;
      --dt-color-text-secondary: #A3A3A3;  --dt-color-action-primary: #60A5FA;
      --dt-color-text-on-action: #0A0A0A;  --dt-color-border-default: #2E2E30;
      --dt-elevation-2: 0 0 0 1px #2E2E30, 0 4px 12px rgba(0,0,0,0.50);
    }
  }
  body { margin: 0; padding: 24px; background: #F5F5F5; }
  .card {
    max-width: 340px; padding: 16px; border-radius: 8px; font: 14px/1.5 system-ui;
    background: var(--dt-color-bg-surface);
    border: 1px solid var(--dt-color-border-default); box-shadow: var(--dt-elevation-2); /* border-led depth */
  }
  .card h2 { margin: 0 0 4px; font-size: 16px; font-weight: 600; color: var(--dt-color-text-primary); }
  .card p  { margin: 0 0 12px; color: var(--dt-color-text-secondary); }
  .btn {
    border: 0; cursor: pointer; padding: 10px 16px; border-radius: 8px; font: 500 14px system-ui;
    background: var(--dt-color-action-primary); color: var(--dt-color-text-on-action);
  }
</style>
```

### Example 2 — Theme toggle with persistence and OS default

Tokens: `assets/css/dark-mode.css`

```html
<header class="bar">
  <span>Dashboard</span>
  <button class="toggle" id="theme-toggle" aria-label="Toggle dark mode">🌙</button>
</header>
<script>
  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  const systemDark = matchMedia('(prefers-color-scheme: dark)');

  // Initial theme: saved choice > OS preference. data-theme set ONLY for explicit choice.
  const saved = localStorage.getItem('theme');
  apply(saved || (systemDark.matches ? 'dark' : 'light'));

  function apply(theme) {
    if (saved) root.dataset.theme = theme; else root.removeAttribute('data-theme');
    toggle.textContent = theme === 'dark' ? '☀️' : '🌙';
  }

  toggle.addEventListener('click', () => {
    const next = getComputedStyle(root).colorScheme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', next);
    apply(next);
  });
</script>
<style>
  :root { color-scheme: light; --dt-color-bg-default: #FFFFFF; --dt-color-text-primary: #171717; }
  [data-theme='dark'] { --dt-color-bg-default: #0A0A0A; --dt-color-text-primary: #FAFAFA; }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme]) { --dt-color-bg-default: #0A0A0A; --dt-color-text-primary: #FAFAFA; }
  }
  body { margin: 0; font: 14px/1.5 system-ui; background: var(--dt-color-bg-default); color: var(--dt-color-text-primary); }
  .bar { display: flex; justify-content: space-between; align-items: center; padding: 12px 24px; font-weight: 600; }
  .toggle { border: 1px solid currentColor; background: transparent; border-radius: 8px; padding: 6px 10px; cursor: pointer; font-size: 16px; }
</style>
```

## 10. Implementation Checklist

- [ ] All dark values live in one `[data-theme='dark']` alias re-pointing block — zero component-level dark overrides.
- [ ] `color-scheme: light dark` is declared at the root so native controls and scrollbars adapt per theme.
- [ ] OS default via `prefers-color-scheme` is the initial state; the explicit toggle persists via localStorage and wins once chosen.
- [ ] Dark surfaces use `#0A0A0A`-range defaults, never pure `#000`; text is `#FAFAFA`, never pure `#FFF`.
- [ ] Every elevation level pairs a border alias (`--dt-color-border-dark`) with a border-led `--dt-elevation-*-dark` shadow.
- [ ] Brand/action steps are desaturated for dark (e.g. `#60A5FA`), not reused from light.
- [ ] Every alias pairing has a computed contrast ratio in BOTH themes; a missing dark ratio blocks ship.
- [ ] Hover/focus/disabled state deltas are visually verified in dark, with motion tokens animating the transition.
