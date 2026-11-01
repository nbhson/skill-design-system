---
name: color-psychology
description: What hues signal and when signals misfire - emotion, category conventions, and matching brand personality to palette temperature.
tags: [color, psychology, branding, personality, conventions]
related: [color-harmony, oklch-perceptual, semantic-color-system]
---

# Color Theory Skill: Color Psychology & Brand Fit

## 1. Definition

Color psychology maps the associations hues carry - red's urgency and danger, blue's trust and distance, green's growth and permission - and, more usefully, how context modulates them: red is passion on a dating app, errors in a dashboard, and prosperity in Chinese markets. The craft is matching palette temperature and saturation to brand personality and product category, then verifying the signal survives the actual UI contexts.

## 2. Core Principles

- **Associations are probabilistic, not universal:** hues prime feelings; they do not guarantee them - context and category set the final meaning.
- **Category conventions are user expectations:** blue fintech, green health, red food - breaking convention demands a reason and earns a cost.
- **Temperature sets the room:** warm palettes energize, cool palettes calm - match the product's session mood (banking calm, gaming hot).
- **Saturation communicates maturity:** high-chroma palettes read young/playful, muted chroma reads premium/serious.
- **Brand personality scores first:** map adjectives (trustworthy, playful, bold) to hue/temp/chroma targets before palette work.
- **Signal roles are sacred:** danger-red, success-green, warning-amber conventions (guide 06) override brand palette - brand never recolors status.
- **Verify in context, not swatches:** a color's psychological signal is tested inside real screens, next to real copy and real actions.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Brief | `--clr-brand-personality-map` | `adjectives-to-hue-temp-chroma` | Documented mapping before palette design |
| Temp | `--clr-temperature-fit` | `product-session-mood` | Warm energizes; cool calms; chosen per product |
| Chroma | `--clr-chroma-personality` | `high-playful-low-premium` | The chroma-to-maturity axis |
| Category | `--clr-category-convention-check` | `required` | Fintech blue / health green / food red audited consciously |
| Signal | `--clr-signal-role-protection` | `status-hues-locked` | Danger/success/warning hues never brand-swapped |
| CTA | `--clr-cta-energy` | `warm-or-high-chroma` | Primary actions earn attention via temperature/chroma |
| Test | `--clr-context-test` | `in-real-screens` | Psychology verified in UI, not swatch grids |
| Media | `--clr-photography-harmony` | `palette-complements-media` | Brand palette chosen to harmonize with real content imagery |
| Drift | `--clr-palette-drift-guard` | `campaigns-derive` | Campaigns derive from the brand scheme, never fork it |
| Rebrand | `--clr-rebrand-audit` | `association-refresh` | Psychology mapping re-validated at every rebrand |

Consume them by linking `assets/css/color-psychology.css` once at the app root, then referencing `var(--clr-...)` wherever a psychological decision needs to be traceable in code - the personality map token documents which adjective targets the palette was built from, and the protection token marks status hues as off-limits to theming. The tokens are mostly policy rather than pigment: they encode the decisions (convention check done, context test run) that a palette audit will ask for, so psychology survives personnel changes.

## 4. Composition

- **Composes with color-harmony:** psychology picks the hue intent; harmony structures its relationships. "Blue, trustworthy, calm" is a psychology output that the harmony workshop turns into an analogous-plus-neutral scheme.
- **Composes with cultural-color-meaning:** psychology gives the (Western-biased) baseline; culture localizes it per market. The personality map is validated once per launch market, not assumed portable.
- **Composes with semantic-color-system:** psychology explains why status hues are what they are - and why they are protected. The conventions users learned elsewhere are the same ones the semantic system locks in code.

## 5. Signature Patterns

- **Personality-to-palette brief:** adjectives scored against temperature/chroma axes produce the palette brief the harmony workshop consumes. The brief is a table - each brand adjective maps to a hue angle band, a temperature, and a chroma level - so palette decisions trace to positioning instead of founder taste.
- **First-impression test:** five users, five seconds, one screen - the words they say back are the palette's real signal. If the brief says "trustworthy" and the five-second words are "playful app," the palette, not the copy, is what spoke; the test catches the mismatch before launch.

## 6. Real-World Use Cases

- **New brands choosing palette direction from personality, not founder taste.** The scored brief converts "we want to feel premium but approachable" into concrete temperature and chroma targets a design team can execute against.
- **Products entering categories with strong color conventions.** A challenger fintech choosing anything but blue must do it consciously - the convention check token documents the reason and the compensating trust signals the deviation demands.
- **Rebrands: auditing whether the palette still signals the positioning.** The rebrand-audit token forces the personality mapping to be re-validated: palettes outlive their positioning, and yesterday's "playful startup green" can read as unserious for today's enterprise product.

## 7. Combination Notes

### With other color-theory skills

- **Good with color-harmony, oklch-perceptual, semantic-color-system, cultural-color-meaning, brand-ramp-construction, gray-ramp-neutrals, data-viz-palettes, contrast-models, dark-mode-palette, gradient-theory, and cvd-safe-design:** psychology supplies the intent layer - why these hues - while harmony structures them, perceptual math makes them usable, ramps make them practical, and semantic/CVD work keeps their meaning legible for everyone. It is the first skill in the palette pipeline and the reason the rest of it has a direction.
- **No caution list:** psychological verification never conflicts with the other skills - it only strengthens their rationale. Where tension appears (brand hue vs status hue), the semantic-color-system protection policy resolves it by rule.
- **No avoid list:** the associations this skill documents are consumed by every downstream palette skill; nothing in the stack is better off without them.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and retro:** minimalism lets a small palette carry the full psychological load - one temperature, one chroma level, nowhere to hide, so the personality signal is pure. Flat design's unmodulated color reads personality directly, and retro styles arrive with strong, well-understood psychological associations the brief can inherit deliberately.
- **Caution with brutalism-ui:** brutalism deliberately destabilizes conventions - harsh contrast, raw layouts, aggressive type - which can invert the psychological signal a palette intends (a calm temperature inside an aggressive frame reads as irony). If pairing them, run the first-impression test twice, because the style may shout louder than the hues.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions and feedback-confirmation:** psychological signal is reinforced by motion - a success confirmation that springs with a warm-toned flourish feels rewarding in a way color alone cannot, and micro-interactions let the CTA's "energy" token express as anticipation on hover. Motion is the temporal half of the personality the palette states spatially.
- **No caution list:** the skills this guide pairs with animate within validated pairings and status roles, so motion amplifies rather than distorts the intended associations - as long as feedback animations never recolor status hues.

## 8. Anti-Patterns

- **Color-by-zodiac** — 'purple is creative' applied as law without category or context testing
- **Convention-breaking bravado** — orange bank app with no compensating trust signals
- **Status hue hijack** — brand recoloring error states to match the campaign palette
- **Swatch-grid validation** — approving psychology from a color grid instead of real screens

### Accessibility Notes

Psychological signals must not rely on hue alone: 'red = danger' reaches color-blind users as the text, icon, and position around the hue (guide 11) - psychology informs, multi-signal design delivers. A palette chosen for its emotional signal still has to survive the constraint that a meaningful fraction of users decode it without the hue, which is why every psychological role in the brief is paired with a non-color channel before it ships. The fallback rule resolves the hardest conflicts: when brand personality and category convention conflict, convention wins on status/safety hues and brand expresses through non-status surfaces - personality yields where misreading costs. A brand may want its signature purple everywhere, but the destructive button stays danger-red; the brand voice lives in the primary action, the surfaces, and the accent, not in the safety vocabulary.

## 9. Code Examples

### Example 1 — Personality-to-palette brief rendered as a table

Tokens: `assets/css/color-psychology.css`

```html
<table class="brief">
  <caption>Brand brief: fintech challenger - adjectives scored to palette targets</caption>
  <thead>
    <tr><th scope="col">Adjective</th><th scope="col">Hue target</th><th scope="col">Temperature</th><th scope="col">Chroma</th></tr>
  </thead>
  <tbody>
    <tr><td>Trustworthy</td><td>210-250 (blue)</td><td>Cool</td><td>Muted (C 0.10-0.15)</td></tr>
    <tr><td>Approachable</td><td>60-90 (warm neutral tint)</td><td>Warm</td><td>Low (C 0.02-0.05)</td></tr>
    <tr><td>Bold</td><td>Accent only</td><td>Warm</td><td>High (C 0.18+)</td></tr>
  </tbody>
</table>
<p class="verdict">Convention check: fintech blue honored - deviation not justified.</p>
<style>
  .brief {
    border-collapse: collapse; font: 13px/1.5 Inter, system-ui, sans-serif;
    max-width: 560px; color: #171717;
  }
  .brief caption { text-align: left; font-weight: 600; padding: 8px 0; }
  .brief th, .brief td { border: 1px solid #d4d4d4; padding: 8px 12px; text-align: left; }
  .brief thead th { background: #f5f5f5; }
  .verdict { font: 13px/1.4 Inter, system-ui, sans-serif; color: #1D4ED8; margin-top: 8px; }
</style>
```

### Example 2 — First-impression test card

Tokens: `assets/css/color-psychology.css`

```html
<div class="test" data-phase="view">
  <div class="screen">
    <div class="screen-nav"></div>
    <h3 class="screen-title">Grow your savings</h3>
    <p class="screen-text">Set aside money automatically, every week.</p>
    <button class="screen-cta">Start saving</button>
  </div>
  <div class="controls" hidden>
    <p>In one word, how does this product feel?</p>
    <button class="chip" data-word="Trustworthy">Trustworthy</button><button class="chip" data-word="Playful">Playful</button>
    <button class="chip" data-word="Cheap">Cheap</button><button class="chip" data-word="Premium">Premium</button>
  </div>
  <output class="result" aria-live="polite"></output>
</div>
<script>
  const test = document.querySelector('.test');
  const controls = test.querySelector('.controls');
  const result = test.querySelector('.result');
  // Five seconds of exposure - then the palette's real signal is collected
  const timer = setTimeout(() => { controls.hidden = false; }, 5000);
  controls.addEventListener('click', e => {
    const chip = e.target.closest('.chip');
    if (!chip) return;
    clearTimeout(timer);
    controls.hidden = true;
    result.textContent = `Response: "${chip.dataset.word}" - brief target: "Trustworthy" -> `
      + (chip.dataset.word === 'Trustworthy' ? 'signal holds' : 'palette misfires, revisit temperature');
  });
</script>
<style>
  .test { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 380px; }
  .screen {
    border-radius: 12px; padding: 24px;
    /* Cool, muted, trustworthy: the brief's targets as an actual screen */
    background: oklch(0.97 0.015 230);
    color: oklch(0.25 0.04 230);
    border: 1px solid oklch(0.90 0.02 230);
  }
  .screen-nav { height: 6px; width: 48px; border-radius: 3px;
    background: oklch(0.66 0.10 230); margin-bottom: 16px; }
  .screen-title { margin: 0 0 8px; font-size: 18px; }
  .screen-text { margin: 0 0 16px; }
  .screen-cta {
    background: oklch(0.50 0.14 230); color: oklch(0.99 0.005 230);
    border: none; border-radius: 8px; padding: 10px 18px;
    font: 600 14px/1 Inter, system-ui, sans-serif; cursor: pointer;
  }
  .controls p { margin: 12px 0 8px; font-weight: 600; }
  .chip {
    margin: 0 6px 6px 0; padding: 6px 12px; border-radius: 999px;
    border: 1px solid #d4d4d4; background: #fff; font: inherit; cursor: pointer;
  }
  .chip:hover { border-color: #171717; }
  .result { display: block; margin-top: 8px; font-size: 13px; color: #404040; }
</style>
```

## 10. Implementation Checklist

- [ ] The personality-to-palette brief exists as `--clr-brand-personality-map` before any palette work starts.
- [ ] Temperature and chroma targets are chosen per product session mood (`--clr-temperature-fit`, `--clr-chroma-personality`).
- [ ] Category conventions were audited consciously (`--clr-category-convention-check: required`) with documented reasons for any deviation.
- [ ] Status hues are locked (`--clr-signal-role-protection`) - no theming, campaign, or brand recolor touches danger/success/warning.
- [ ] The primary CTA earns attention via temperature or chroma within the brief's targets (`--clr-cta-energy`).
- [ ] Psychological signal was verified in real screens via a first-impression test (`--clr-context-test`), not swatch grids.
- [ ] The palette harmonizes with real content imagery (`--clr-photography-harmony`), not just with itself.
- [ ] Campaign palettes derive from the brand scheme (`--clr-palette-drift-guard`), and rebrands trigger a fresh association audit (`--clr-rebrand-audit`).
