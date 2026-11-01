---
name: contrast-models
description: WCAG luminance ratios vs APCA: what each model measures, when each applies, and the computation discipline behind every validated pairing.
tags: [contrast, wcag, apca, accessibility, color-math]
related: [oklch-perceptual, dark-mode-palette, data-viz-palettes]
---

# Color Theory Skill: Contrast Models & Math

## 1. Definition

Contrast models are the math that turns color pairs into pass/fail numbers: the WCAG relative-luminance ratio (4.5:1 / 3:1) is the legal standard; APCA (Advanced Perceptual Contrast Algorithm) is the newer model that better predicts readability across dark surfaces and light text. This skill covers computing both, their blind spots, and the pairing-manifest discipline that makes contrast a designed property instead of a QA surprise.

## 2. Core Principles

- **WCAG ratio is the compliance floor:** 4.5:1 body text, 3:1 large text and UI components - computed with the relative-luminance formula, never estimated.
- **APCA predicts readability better on dark:** WCAG under-rewards light-text-on-dark; APCA's Lc values (75 body, 60 large, 45 UI) model dark surfaces more honestly.
- **Contrast belongs to pairs:** only text-on-background has a value - palettes are validated as pairing manifests, not as individual swatches.
- **Validate every role pair per theme:** text/bg, text/surface, icon/surface, border/surface, focus/surface - the manifest enumerates them and computes both models.
- **Gamma matters:** luminance math uses gamma-encoded sRGB values correctly - hand-rolled formulas that skip gamma produce wrong ratios.
- **Contrast is adjustable on the L axis:** failing pairs are fixed by lightness moves in OKLCH, keeping hue identity (guide 02's leverage point).
- **Both models, one source of truth:** the manifest computes WCAG for compliance and APCA for quality - conflicts are resolved in favor of the stricter readable outcome.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Contrast | `--clr-wcag-body-min` | `4.5:1` | WCAG 1.4.3 AA body text |
| Contrast | `--clr-wcag-large-min` | `3:1` | Large text (24px/19px bold) |
| Contrast | `--clr-wcag-ui-min` | `3:1` | WCAG 1.4.11 components/graphics |
| Contrast | `--clr-apca-body-lc` | `Lc-75` | APCA body text quality target |
| Contrast | `--clr-apca-large-lc` | `Lc-60` | APCA large text target |
| Contrast | `--clr-apca-ui-lc` | `Lc-45` | APCA UI component target |
| Contrast | `--clr-contrast-pairing-manifest` | `all-roles-all-themes` | The enumerated, computed pairing table |
| Contrast | `--clr-luminance-formula` | `wcag-rel-luminance-gamma` | Gamma-correct relative luminance |
| Contrast | `--clr-fix-axis` | `oklch-lightness` | Contrast fixes move L, keep hue |
| Contrast | `--clr-conflict-policy` | `stricter-readable-wins` | WCAG/APPCA disagreement resolves to readable |

Consume them by linking `assets/css/contrast-models.css` once at the app root, then referencing `var(--clr-...)` from lint rules, CI scripts, and documentation — the thresholds are configuration, not tribal knowledge. Any pairing not in the manifest has no contrast value; adding one requires running the math, not eyeballing the swatch.

## 4. Composition

- **Composes with skill-accessibility guide 02 (color-contrast):** that guide owns the WCAG practice; this one owns the models and math.
- **Composes with every palette guide in this repo:** harmony, ramps, semantic, viz, and gradients all pass through the manifest.
- **Composes with skill-design-tokens guide 08 (contrast validation):** the token layer stores validated pairings; this guide computes them.

## 5. Signature Patterns

- **Pairing manifest as CI:** a script enumerates role pairs from data, computes WCAG + APCA, and fails the build on new failures - contrast regression is prevented, not found.
- **L-axis fix workflow:** failing pair → OKLCH L adjust → regenerate ramp → re-run manifest - the loop is minutes, not meetings.

## 6. Real-World Use Cases

- **Palette sign-off:** computing every pair in both themes before adoption.
- **Dark-mode construction:** APCA-guided re-tuning where WCAG under-warns.
- **Audit:** un-manifested pairs, contrast-by-eye, WCAG-passing-but-unreadable dark UI.

## 7. Combination Notes

### With other color-theory skills

- **Good with oklch-perceptual, gray-ramp-neutrals, brand-ramp-construction, semantic-color-system, dark-mode-palette, data-viz-palettes, gradient-theory, cvd-safe-design, color-harmony, color-psychology, and cultural-color-meaning:** this skill is the mathematical gate every palette guide passes through — harmony picks relationships, ramps pick steps, and the manifest proves the resulting pairs are readable. The reason it composes with all of them without exception is that contrast belongs to pairs, and every one of those guides ultimately ships pairs.
- **Good with dark-mode-palette specifically:** WCAG under-rewards light-text-on-dark, so APCA's Lc targets are the honest referee for dark-theme re-tuning — the two skills share the conflict policy "stricter readable wins".
- **Good with oklch-perceptual for the fix loop:** failing pairs are repaired on the L axis while hue identity stays intact; the manifest detects, OKLCH fixes, the manifest re-verifies.
- **No caution or avoid entries:** contrast math is compatible with every palette strategy — the only incompatible behavior is skipping the math, which is the failure mode this skill exists to prevent.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both styles run on disciplined text/surface pairings and visible control boundaries — exactly the pairs the manifest computes, and their restrained palettes keep the manifest small and complete.
- **Caution with collage-art and maximalism:** layered textures, overlapping planes, and dense palettes multiply pairing surfaces and create unknown-contrast zones; if a style demands them, every text zone still needs a computed pairing — the manifest grows, it never shrinks.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** hover/pressed transitions move between validated pairs on the manifest; the transition itself carries no contrast obligation, only its endpoints do — so timing and contrast compose without conflict.
- **Caution with ambient-motion:** animated backgrounds and shifting color fields can move surfaces away from the pairs validated at rest; any animated surface must hold its text pairing passing across the full motion path, not just at its endpoints.

## 8. Anti-Patterns

- **Contrast-by-eye** — judging ratios on a calibrated-less screen in a sunlit room
- **Gamma-broken math** — hand-rolled luminance formulas skipping sRGB gamma
- **Dark-mode WCAG complacency** — 4.5:1 passes that APCA shows are barely readable
- **Swatch validation** — computing contrast on palette colors instead of actual pairings

### Accessibility Notes

This guide IS the mathematical layer of WCAG 1.4.3/1.4.11 and the APCA modernization of it: every pairing decision in every other guide traces back to these formulas and the manifest that applies them. Treat the manifest as the contract — a pairing that appears in product code but not in the manifest is an unaudited pairing, and unaudited pairings are where regressions live. The fallback is strict: when models disagree irreconcilably on a pair, the pair is rejected — a pairing that one model says is unreadable is not shipped with the other model's blessing. Compute with gamma-correct relative luminance (or a vetted library), enumerate all roles in all themes, and remember the fix axis: contrast problems are solved by moving lightness in OKLCH, never by re-picking hues.

## 9. Code Examples

### Example 1 — Contrast checker: WCAG ratio + APCA-style Lc approximation

```html
<div class="checker">
  <h2>Pairing check</h2>
  <table id="pairs">
    <thead><tr><th>Text</th><th>Surface</th><th>WCAG</th><th>Lc (approx)</th><th>Verdict</th></tr></thead>
    <tbody></tbody>
  </table>
</div>
<style>
  .checker { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 560px; padding: 16px;
             background: var(--clr-contrast-pairing-manifest, #fff); }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #d4d4d4; padding: 6px 8px; text-align: left; }
  .pass { color: #15803d; font-weight: 600; }
  .fail { color: #b91c1c; font-weight: 600; }
</style>
<script>
  // Gamma-correct WCAG relative luminance
  function lum(hex) {
    const [r, g, b] = [1, 3, 5].map(i => parseInt(hex.slice(i, i + 2), 16) / 255)
      .map(c => c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4));
    return 0.2126 * r + 0.7152 * g + 0.0722 * b;
  }
  function wcag(fg, bg) {
    const [a, b] = [lum(fg), lum(bg)].sort((x, y) => y - x);
    return (a + 0.05) / (b + 0.05);
  }
  // APCA-style Lc approximation (simplified; full spec uses SAPC-4/Lc-3 ranges)
  function apcaLc(text, bg) {
    const ytxt = Math.pow(lum(text), 0.65), ybg = Math.pow(lum(bg), 0.65);
    const raw = ybg > ytxt ? (ybg - ytxt) * 100 : (ytxt - ybg) * -110;
    return Math.abs(raw) < 8 ? 0 : Math.round(Math.pow(Math.abs(raw), 0.85) * Math.sign(raw));
  }
  const pairs = [
    ['#171717', '#FFFFFF', '4.5:1 body'], ['#404040', '#FFFFFF', '4.5:1 body'],
    ['#FFFFFF', '#2563EB', 'button'],   ['#F8FAFC', '#0F172A', 'dark body'],
  ];
  const body = document.querySelector('#pairs tbody');
  for (const [fg, bg, label] of pairs) {
    const ratio = wcag(fg, bg), lc = apcaLc(fg, bg);
    const wcagPass = ratio >= 4.5 || (label !== '4.5:1 body' && ratio >= 3);
    const lcPass = Math.abs(lc) >= (label === '4.5:1 body' ? 75 : label === 'button' ? 45 : 60);
    body.insertAdjacentHTML('beforeend', `<tr>
      <td><span class="swatch" style="background:${fg}"></span>${fg}</td>
      <td><span class="swatch" style="background:${bg}"></span>${bg}</td>
      <td>${ratio.toFixed(2)}:1</td><td>Lc ${lc}</td>
      <td class="${wcagPass && lcPass ? 'pass' : 'fail'}">${wcagPass && lcPass ? 'PASS' : 'REVIEW'}</td></tr>`);
  }
</script>
```

### Example 2 — Rendered pairing manifest from validated tokens

```html
<div class="manifest">
  <h2>Pairing manifest — light theme</h2>
  <div class="row" data-pair="text-primary / surface"><span class="chip text-primary">Primary text</span><span class="chip surface">Surface</span><output></output></div>
  <div class="row" data-pair="text-secondary / surface"><span class="chip text-secondary">Secondary text</span><span class="chip surface">Surface</span><output></output></div>
  <div class="row" data-pair="text-on-brand / brand"><span class="chip text-on-brand">On brand</span><span class="chip brand">Brand</span><output></output></div>
</div>
<style>
  .manifest { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 480px; }
  .row { display: flex; gap: 8px; align-items: center; padding: 8px; border-bottom: 1px solid #e5e5e5; }
  .chip { padding: 4px 10px; border-radius: 6px; font-size: 12px; }
  .text-primary   { color: var(--clr-wcag-body-min, #171717); background: #fff; }
  .text-secondary { color: #525252; background: #fff; }
  .text-on-brand  { color: #fff; }
  .surface { color: #171717; background: #fafafa; border: 1px solid #d4d4d4; }
  .brand   { background: #1d4ed8; color: #fff; }
  output { margin-left: auto; font-variant-numeric: tabular-nums; font-weight: 600; }
</style>
<script>
  // Standalone manifest check: rendered pairs re-computed, swatch validation banned
  const lum = h => [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255)
    .map(c => c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4))
    .reduce((y, c, i) => y + [0.2126, 0.7152, 0.0722][i] * c, 0);
  const wcag = (fg, bg) => { const [a, b] = [lum(fg), lum(bg)].sort((x, y) => y - x); return (a + 0.05) / (b + 0.05); };
  const get = el => getComputedStyle(el).color.match(/\d+/g).slice(0, 3);
  const rgb2hex = a => '#' + a.map(n => (+n).toString(16).padStart(2, '0')).join('');
  document.querySelectorAll('.row').forEach(row => {
    const chips = row.querySelectorAll('.chip');
    const ratio = wcag(rgb2hex(get(chips[0])), rgb2hex(get(chips[1])));
    const out = row.querySelector('output');
    out.textContent = ratio.toFixed(2) + ':1';
    out.className = ratio >= 4.5 ? 'pass' : ratio >= 3 ? 'warn' : 'fail';
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every text/bg, text/surface, icon/surface, border/surface, and focus/surface pair is enumerated in the pairing manifest for all themes.
- [ ] WCAG ratios are computed with the gamma-correct relative-luminance formula (or a vetted library) — no hand-rolled math, no estimates.
- [ ] Body-text pairs meet `--clr-wcag-body-min` (4.5:1); large text and UI components meet 3:1.
- [ ] Dark-theme pairs additionally meet the APCA targets (`--clr-apca-body-lc` Lc-75, large Lc-60, UI Lc-45).
- [ ] A CI script recomputes the manifest and fails the build on new contrast failures.
- [ ] Failing pairs are fixed on the OKLCH lightness axis; hue identity is preserved.
- [ ] WCAG/APCA disagreements resolve per `--clr-conflict-policy` (stricter-readable-wins) or the pair is rejected.
- [ ] No pairing ships in product code without a manifest entry — swatch-only validation is banned.
