---
name: font-pairing
description: Choosing type families that work together — contrast strategies, superfamily and companion approaches, licensing, and fallback stacks.
tags: [typography, fonts, pairing, hierarchy, webfonts]
related: [type-scale, line-height, letter-spacing]
---

# Typography Skill: Font Pairing & Selection

## 1. Definition

Font pairing is the deliberate selection of two (at most three) type families whose contrast creates hierarchy without visual conflict: a display face for headlines, a text face for reading, optionally a mono for code and data. The pairing decision compounds through every screen, so it is made once with explicit criteria — x-height compatibility, width contrast, tone match, license cost, and language coverage — rather than by browsing font sites until something looks nice. Because the pairing is the strongest single carrier of a product's visual voice, it is documented as a token contract (families, fallback stacks, weight budgets) rather than left as a designer's private preference.

## 2. Core Principles

- **Maximum two families in the product:** a superfamily (same designer, built to pair) or a display+text combo; a third slot is reserved for mono/code.
- **Pair by contrast, not similarity:** pick faces that differ in one strong axis (serif vs sans, geometric vs humanist) — two similar-but-not-identical sans faces look like a mistake.
- **Match x-heights within ~5%:** paired faces set side by side read as the same size only when x-heights agree.
- **Tone must match the brand:** a quirky display face cannot rescue a legal document; tone-fit is checked against the brand's voice before aesthetics.
- **Check language coverage before falling in love:** Vietnamese needs stacked-diacritic support (font-pairing meets multilingual-vietnamese here).
- **Verify license scope:** webfont license, app embedding, and modification rights differ per foundry — budget the license with the token (design-tokens guide 02).
- **Every selection ships with a fallback stack:** system fonts that keep metrics close so FOUT and font failures degrade gracefully.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Pairing strategy | `--type-pairing-strategy` | `display-plus-text` | Documented strategy: superfamily / display+text / mono-add-on |
| Font display | `--type-font-display` | `'Space Grotesk', Inter, sans-serif` | Headlines; contrasts with text face |
| Font text | `--type-font-text` | `'Source Sans 3', system-ui, sans-serif` | Body reading; humanist, high x-height |
| Font mono | `--type-font-mono` | `ui-monospace, 'SF Mono', Menlo, monospace` | Code, tabular data, token names |
| X-height tolerance | `--type-x-height-tolerance` | `5%` | Pairing compatibility threshold |
| Fallback metrics | `--type-fallback-metrics` | `size-adjust-matched` | Fallback stack tuned with size-adjust/ascent-override |
| License scope | `--type-license-scope` | `webfont-plus-app` | Documented per family; renewal tracked |
| Language coverage | `--type-language-coverage` | `latin-ext-vietnamese` | Must cover all product locales before adoption |
| Display max weights | `--type-display-max-weights` | `2` | Display face loads 2 weights max |
| Text max weights | `--type-text-max-weights` | `3` | Text face loads 3 weights max (400/600/700) |

Consume them by linking `assets/css/font-pairing.css` once at the app root, then referencing `var(--type-font-display)`, `var(--type-font-text)`, and `var(--type-font-mono)` from all component code. The fallback stacks in the values keep metrics close so FOUT is invisible to users; never replace a stack with a bare font name.

## 4. Composition

- **Composes with type-scale (guide 02):** the pairing defines families; the scale defines sizes — a family swap must not change the scale. When a new display face is adopted, the scale steps stay fixed; only the font-family declaration changes.
- **Composes with skill-design-tokens guide 02:** pairing decisions land as typography tokens with fallback stacks and weight budgets declared alongside the ramp.
- **Composes with styleAffinity:** the pairing is the strongest single carrier of design style — it is chosen against the skill-ui-ux style direction (minimalism: neutral sans duo; brutalism: display serif clash).

## 5. Signature Patterns

- **Pairing scorecard:** candidates rated on contrast axis, x-height match, tone fit, license cost, language coverage, and performance before adoption — every scorecard row is a documented decision, not a gut feeling.
- **Superfamily shortcut:** when in doubt, pick a superfamily (built-in pair) and spend the saved effort on scale and rhythm instead — a superfamily ships x-height-matched pairs at zero extra selection cost.

## 6. Real-World Use Cases

- **New products choosing their type system from scratch:** the scorecard gates every candidate before any design work starts.
- **Rebrands evaluating whether to keep or replace the text face:** the pairing criteria are re-applied; aesthetic preference alone does not re-open the decision.
- **Localizing products into Vietnamese or other diacritic-heavy scripts:** language coverage is checked at the pairing gate — a face without the vietnamese subset is disqualified before it reaches the scorecard.

## 7. Combination Notes

### With other typography skills

- **Pairs naturally with type-scale, line-height, and letter-spacing:** the pairing defines which families the scale steps apply to; when families are locked, scale and rhythm tuning can be rigorous without re-checking the family decision.
- **Pairs with webfont-loading, variable-fonts, and multilingual-vietnamese:** these skills consume the same token declarations (weight budgets, subset strategy, fallback chains) — the pairing token set is the single source of truth for all downstream loading decisions.
- **Caution/avoid list is empty:** no sibling skill is incompatible with font-pairing; only bypassing it (off-scale family declarations) is the failure mode to prevent.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism and flat-design:** both styles rely on a neutral sans-serif duo — Space Grotesk + Source Sans 3 carries the minimal palette without competing for attention.
- **Good affinity with brutalism-ui:** a high-contrast display+text pairing (e.g. bold slab serif + plain sans) expresses brutalist tension without decoration.
- **Caution with skeuomorphism:** skeuomorphic designs demand specific legacy faces; pairing criteria may yield to historical accuracy, which must be explicitly documented as a style exception, not a token violation.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** font loading transitions (font-display: swap) benefit from the same easing curves used for UI state changes — the system feels consistent as fonts arrive.
- **Caution/avoid list is empty:** no motion discipline conflicts with font pairing decisions directly.

## 8. Anti-Patterns

- **Font-of-the-week** — swapping families per campaign until no one recognizes the product's voice
- **Twins pairing** — two geometric sans faces at 92% similarity that read as an accident
- **Unlicensed embedding** — shipping desktop-licensed fonts as webfonts
- **Fallback-less stacks** — custom faces with no metric-matched system fallback, so failures reflow the page

### Accessibility Notes

Pairing serves accessibility directly: adequate x-height, open apertures, and unambiguous letterforms (I/l/1, O/0) reduce reading errors — and language coverage is an inclusion decision, not a nice-to-have. The 5% x-height tolerance keeps display and text faces reading at the same visual size, which helps users with low vision who rely on consistent proportional relationships across a page. The fallback rule is equally strict: if a preferred face lacks Vietnamese coverage, the fallback face takes the whole product rather than mixing per-locale — mixed systems break rhythm and disorient users who rely on consistent rendering.

## 9. Code Examples

### Example 1 — Pairing scorecard

Tokens: `assets/css/font-pairing.css`

```html
<div class="scorecard">
  <h2 class="scorecard-title">Font Pairing Scorecard</h2>
  <table class="scorecard-table">
    <thead><tr><th>Criterion</th><th>Display</th><th>Text</th><th>Mono</th></tr></thead>
    <tbody>
      <tr><td>Family</td><td>Space Grotesk</td><td>Source Sans 3</td><td>SF Mono</td></tr>
      <tr><td>Role</td><td>Headlines</td><td>Body / UI</td><td>Code / Data</td></tr>
      <tr><td>Weights</td><td>2 (500, 700)</td><td>3 (400, 600, 700)</td><td>1</td></tr>
      <tr><td>X-height match</td><td colspan="3">Within 5% — cap-height comparison verified</td></tr>
      <tr><td>Vietnamese coverage</td><td colspan="3">latin-ext + vietnamese subset confirmed</td></tr>
      <tr><td>License</td><td colspan="3">Webfont + app embedding; renewal tracked (design-tokens guide 02)</td></tr>
      <tr><td>Fallback</td><td>Inter, system-ui, sans-serif</td><td>system-ui, sans-serif</td><td>ui-monospace, Menlo, monospace</td></tr>
    </tbody>
  </table>
</div>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Source+Sans+3:wght@400;600;700&display=swap');
  .scorecard { font-family: var(--type-font-text); max-width: 680px; margin: 32px auto; padding: 24px; background: #F9FAFB; border: 1px solid #E5E7EB; border-radius: 8px; }
  .scorecard-title { font-family: var(--type-font-display); font-weight: 700; font-size: var(--type-size-xl); line-height: 1.2; margin: 0 0 20px; color: #111827; }
  .scorecard-table { width: 100%; border-collapse: collapse; font-size: var(--type-size-sm); }
  .scorecard-table th, .scorecard-table td { text-align: left; padding: 8px 12px; border-bottom: 1px solid #E5E7EB; }
  .scorecard-table th { font-weight: 600; color: #374151; letter-spacing: 0.05em; text-transform: uppercase; font-size: 0.75rem; }
  .scorecard-table tbody tr:last-child td { border-bottom: none; }
</style>
```

### Example 2 — Demo page with display / text / mono roles

Tokens: `assets/css/font-pairing.css` (plus `assets/css/type-scale.css` for sizes)

```html
<article class="demo-page">
  <header class="demo-header">
    <p class="demo-eyebrow">Typography Skill</p>
    <h1 class="demo-display">The Art of<br>Font Pairing</h1>
    <p class="demo-lead">Two families, three roles, zero guesswork.</p>
  </header>
  <div class="demo-body">
    <p>Body text uses <code>Source Sans 3</code> — a humanist sans with high x-height that reads comfortably at paragraph sizes. Its open apertures keep character forms distinct even at 16px.</p>
    <pre class="demo-code">const font = 'Space Grotesk, Inter, sans-serif';
const scale = 1.25; // major third ratio</pre>
    <p>Monospace tokens (<code>ui-monospace</code>) keep character width fixed — essential for aligned data, code, and token names like <code>--type-font-display</code>.</p>
  </div>
</article>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Source+Sans+3:wght@400;600;700&display=swap');
  .demo-page {
    font-family: var(--type-font-text);
    font-size: var(--type-size-sm);
    line-height: var(--type-line-height-body, 1.5);
    max-width: 65ch; margin: 0 auto; padding: 40px 24px; color: #111827;
  }
  .demo-eyebrow { font-size: var(--type-size-2xs, 0.75rem); font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #6B7280; margin: 0 0 12px; }
  .demo-display { font-family: var(--type-font-display); font-size: var(--type-size-3xl); font-weight: 700; line-height: 1.1; letter-spacing: -0.025em; margin: 0 0 20px; color: #111827; }
  .demo-lead { font-size: var(--type-size-md); font-weight: 600; color: #374151; margin: 0 0 32px; }
  .demo-body { color: #374151; }
  .demo-body p { margin: 0 0 16px; }
  .demo-code {
    font-family: var(--type-font-mono); font-size: var(--type-size-xs);
    background: #F3F4F6; border: 1px solid #E5E7EB; border-radius: 6px;
    padding: 12px 16px; overflow-x: auto; margin: 0 0 16px; line-height: 1.6;
  }
</style>
```

## 10. Implementation Checklist

- [ ] Pairing scorecard is filled before any family adoption — every criterion is a documented decision, not a preference.
- [ ] Families pass the ~5% x-height tolerance check via cap-height comparison at equal sizes.
- [ ] Vietnamese (latin-ext) coverage is verified for every family before the product ships to any Vietnamese locale.
- [ ] Fallback stacks carry size-adjust / ascent-override so FOUT is metric-matched and layout-stable.
- [ ] Weight budgets are closed: display face loads ≤ 2 weights, text face loads ≤ 3 weights.
- [ ] License scope (webfont + app) is documented per family with renewal tracking in the design-tokens governance log.
- [ ] The `var(--type-font-display)`, `var(--type-font-text)`, and `var(--type-font-mono)` tokens are the only declaration points for families across the entire codebase.
- [ ] No family appears in any inline style or per-component CSS — token violations are caught by a lint rule.
