---
name: contrast-validation
description: WCAG contrast as a token property — annotated scales, validated alias pairings, and automated checks that fail the build on regressions.
tags: [accessibility, wcag, contrast, automation, design-systems]
related: [semantic-alias-naming, color-tokens, dark-mode]
---

# Design Token Skill: Contrast Validation

## 1. Definition

Contrast validation turns accessibility from a QA afterthought into a token property. Every primitive step carries a computed ratio on white and black; every alias pairing (text-on-bg, icon-on-surface, border-on-surface) is recorded and checked; CI fails when a change drops any pairing below its threshold. Because the alias tier is the only place product code consumes color, validating there means validating everything — once. The skill's output is not a report but a contract: a pairing manifest that ships with the tokens, diffed on every PR, so a regression to 4.2:1 is a broken build rather than an audit finding months later.

## 2. Core Token Principles

- **Know the thresholds:** 4.5:1 body text, 3:1 large text (18.66px bold / 24px regular), 3:1 UI components and graphical objects (WCAG 1.4.3/1.4.11).
- **Validate pairings, not colors:** a color has no ratio — only text-on-background does; the alias tier is where pairings live.
- **Annotate the scale once:** generated ratio tables on white and black make primitive steps self-documenting.
- **Pair-check every state axis:** hover, pressed, disabled, and focus each declare a pairing; a state that fails silently is a bug in the contract.
- **Focus indicators count:** the focus ring must hit 3:1 against adjacent colors (WCAG 2.4.13 in 2.2) — give it a dedicated alias.
- **Automate at three gates:** token pipeline (pairing lint), CI (regression diff), and component tests (rendered contrast) — manual spot checks are the exception.
- **Disabled does not mean unmeasured:** even exempt disabled states get documented ratios so no one "fixes" them blindly later.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Body minimum | `--dt-contrast-body-min` | `4.5:1` | WCAG 1.4.3 AA for body text |
| Large-text minimum | `--dt-contrast-large-text-min` | `3:1` | 24px regular / 18.66px bold text |
| UI component minimum | `--dt-contrast-ui-component-min` | `3:1` | WCAG 1.4.11: input borders, icons, control boundaries |
| AAA body target | `--dt-contrast-body-aaa` | `7:1` | AAA target for long-form reading surfaces |
| Focus ring minimum | `--dt-contrast-focus-ring-min` | `3:1` | WCAG 2.4.13 focus appearance; ring vs both sides of the boundary |
| Focus ring color | `--dt-contrast-focus-ring-color` | `#1D4ED8` | 6.3:1 on white, 4.6:1 on neutral-100 - safe nearly everywhere |
| State delta minimum | `--dt-contrast-state-delta-min` | `1.5:1` | Hover/pressed color shift users can actually perceive |
| Disabled policy | `--dt-contrast-disabled-note` | `exempt-documented` | WCAG exempts disabled controls; record ratios anyway |

Consume them by linking `assets/css/contrast-validation.css` at the app root; thresholds are read by tooling (lint rules, test runners) and the focus-ring color is used directly as `var(--dt-contrast-focus-ring-color)` in every `:focus-visible` style. Ratios themselves live in the pairing manifest, not in CSS — CSS only declares the thresholds.

## 4. Composition & Layering

- **Contrast composes with alias naming:** pairings are declared as alias relationships, so one validation covers every consumer of the alias.
- **It composes with dark mode and multi-brand:** each theme cell re-validates the same pairing table; automation makes N × M cheap.
- **It composes with component tokens:** component pairings (button-bg on button-text) inherit validation from their alias sources.

## 5. Signature Patterns

- **Pairing manifest:** a data file listing every semantic pairing with both themes' computed ratios; CI diffs it and fails on any regression.
- **Contrast-first palette build:** choose alias pairs before styling — the palette is whatever values satisfy the manifest, not the reverse.

## 6. Real-World Use Cases

- **Design systems shipping WCAG AA (or AAA)** as a build-time guarantee.
- **Dark mode and multi-brand rollouts:** validating the full pairing matrix automatically.
- **A11y remediation:** converting audit findings into token-level fixes that propagate everywhere.

## 7. Combination Notes

### With other token skills

- **Pairs well with semantic-alias-naming and color-tokens:** the alias tier is where pairings exist and the primitive scales supply the steps to fix them — validation without these two has nothing to check and nothing to fix with.
- **Pairs well with dark-mode and multi-brand-theming:** both multiply the matrix of cells that must pass; the manifest-plus-CI approach is the only way N × M stays affordable.
- **Pairs well with token-pipeline-figma and component-tokens:** the pipeline runs the pairing lint pre-codegen, and component pairings inherit validation from the aliases they derive from — rendered components stay inside the guarantee for free.
- **Pairs well with governance-migration:** a failing pairing cannot merge regardless of who proposes it — governance is the enforcement muscle behind the manifest.
- **Caution with radius-elevation:** a shadow is not a contrast strategy; depth cues may visually separate surfaces, but WCAG 1.4.3/1.4.11 obligations remain on color pairs — never let "it has a shadow" pass review.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and glassmorphism:** high-contrast, low-noise palettes satisfy thresholds naturally; flat surfaces make the ratio pairs easy to enumerate.
- **Caution with brutalism-ui and collage-art:** both lean on clashing or layered surfaces where text may sit over unpredictable backgrounds — require a defined text-container surface so pairings stay checkable.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion:** both are accessibility-as-contract skills; the same "declared, validated, automated" posture applies, and focus/hover state changes must stay perceivable (the 1.5:1 state delta) even when animations collapse.

## 8. Anti-Patterns

- **Spot-check QA:** contrast verified by screenshot eyeballing after build instead of computed in the pipeline
- **Color-only contrast:** darkening text past the brand to pass 4.5:1 when the background alias should change
- **Validating light only:** dark theme pairings assumed 'probably fine' and never computed
- **Exempt everything:** labeling failing text 'large' or 'decorative' to skip thresholds without measuring

### Accessibility Notes

This skill IS the accessibility layer of the token system: WCAG 1.4.3 (text), 1.4.11 (non-text), and 2.4.13 (focus appearance) enforced as data rather than aspiration. Ratios are computed with the WCAG relative-luminance formula against sRGB values, so results are deterministic and machine-checkable. When a pairing fails, there are three legal fixes, in order: change the paired background alias, change the text alias to a darker or lighter sibling step, or (last) add a validated primitive step via governance — never ship below threshold, and never "fix" it by shrinking or restyling the text itself.

## 9. Code Examples

### Example 1 — Runtime ratio checker validating a pairing (PASS/FAIL)

Tokens: `assets/css/contrast-validation.css`

```html
<div class="pair" style="background:#2563EB"><span style="color:#FFFFFF">White on brand-500</span></div>
<div class="pair" style="background:#22C55E"><span style="color:#FFFFFF">White on success-500</span></div>
<script>
  function srgbToLinear(c) {
    c /= 255;
    return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  }
  function luminance(hex) {
    const n = hex.replace('#', '');
    const [r, g, b] = [0, 2, 4].map(i => parseInt(n.slice(i, i + 2), 16));
    return 0.2126 * srgbToLinear(r) + 0.7152 * srgbToLinear(g) + 0.0722 * srgbToLinear(b);
  }
  function ratio(fg, bg) {
    const [l1, l2] = [luminance(fg), luminance(bg)].sort((a, b) => b - a);
    return (l1 + 0.05) / (l2 + 0.05);
  }
  function check(name, fg, bg, min = 4.5) {
    const r = ratio(fg, bg);
    console.log(`${r >= min ? 'PASS' : 'FAIL'} ${name}: ${r.toFixed(2)}:1 (min ${min}:1)`);
  }
  check('white on #2563EB', '#FFFFFF', '#2563EB'); // PASS 4.57:1
  check('white on #22C55E', '#FFFFFF', '#22C55E'); // FAIL ~2.2:1
</script>
```

### Example 2 — Focus ring and state delta using the threshold tokens

Tokens: `assets/css/contrast-validation.css`

```html
<input class="field" placeholder="Email address">
<button class="btn">Save</button>
<style>
  .field {
    padding: 10px 12px; border: 1px solid #D4D4D4; border-radius: 8px; font: 14px system-ui;
  }
  /* WCAG 1.4.11: input border is a UI component → 3:1 floor via token */
  .field:focus-visible {
    outline: 2px solid var(--dt-contrast-focus-ring-color); /* 6.3:1 on white */
    outline-offset: 2px;
  }
  .btn {
    padding: 10px 16px; border: 0; border-radius: 8px; cursor: pointer;
    background: #2563EB; color: #FFFFFF; font: 600 14px system-ui; /* 4.6:1 */
    transition: background 120ms ease;
  }
  /* WCAG state delta: hover shift must stay perceivable (≥1.5:1 class) */
  .btn:hover { background: #1D4ED8; } /* link-safe sibling step, 6.3:1 on white */
</style>
```

## 10. Implementation Checklist

- [ ] A pairing manifest exists listing every semantic pairing with computed ratios for both themes.
- [ ] CI diffs the manifest on every PR and fails when any pairing drops below `--dt-contrast-body-min` (4.5:1) or `--dt-contrast-ui-component-min` (3:1).
- [ ] Ratio tables on white/black ship beside the primitive scales — no step is undocumented.
- [ ] Every state axis (hover, pressed, disabled, focus) declares a pairing; disabled states carry the `exempt-documented` note with recorded ratios.
- [ ] Focus rings use `--dt-contrast-focus-ring-color` and hit `--dt-contrast-focus-ring-min` (3:1) against adjacent colors.
- [ ] Hover/pressed shifts clear `--dt-contrast-state-delta-min` (1.5:1) in light AND dark themes.
- [ ] Failing pairings are fixed in alias order (background → text step → governance-approved new step), never by shipping below threshold.
- [ ] No pairing is exempted as "large" or "decorative" without a measured size/type justification.
