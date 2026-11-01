---
name: localization-i18n
description: Writing for translation: externalized strings, ICU plurals, expansion room, pseudo-localization, and tone that survives translation.
tags: [localization, i18n, translation, icu, rtl]
related: [writing-principles, copy-audit, voice-tone]
---

# UX Writing Guide: Localization & i18n Writing

## 1. Definition

Localization-aware writing starts at the source string, not at the translation vendor. The discipline is: externalize every string (no user-visible copy hardcoded in components), use message formats (ICU MessageFormat) for plurals, gender, and selection instead of concatenation, leave room for expansion (German runs roughly 35% longer than English), avoid embedding numbers and units mid-sentence, and never bake word order into string assembly. Beyond mechanics, it covers tone-risky strings (puns, idiom, cultural references) flagged for translator adaptation, RTL handled as a layout contract built on logical properties, locale-correct formatting via Intl APIs, and pseudo-localization as the build-time smoke test that surfaces hard-coded text and clipped layouts before real locales do.

## 2. Core Principles

- **Externalize everything:** no user-visible copy hardcoded in components — every string lives in the message catalog.
- **Message formats over concatenation:** ICU plurals/select ('{count, plural, one {# item} other {# items}}') — concatenated fragments shatter in translation.
- **No mid-sentence number splicing:** '{count} files selected' as one string, not 'You have ' + n + ' files' — word order differs per language.
- **Plan for expansion:** layout reserves ~35% over English; buttons and labels auto-size — fixed-width English layouts break German.
- **Pseudo-localization is a build gate:** accented-padded strings ('[Ýõû àré ¡n thê ÚÌ!]') surface hard-coded text and clipping before real locales do.
- **Tone-risky strings are flagged:** humor, idiom, and wordplay are marked in the catalog for translator adaptation, not literal translation.
- **Dates, times, numbers are locale-formatted:** the copy layer never formats dates by hand — Intl APIs or format tokens only.
- **RTL is a layout contract:** mirrored layout with logical properties; icons with direction (arrows, progress) are un-mirrored deliberately.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Externalization | `--uxw-externalization` | `all-strings-catalogued` | Zero hardcoded copy in components |
| Message format | `--uxw-message-format` | `icu-plural-select` | No concatenation, ever |
| Expansion budget | `--uxw-expansion-budget` | `35%-over-english` | Layout headroom for de/ru/fi |
| Pseudo-localization | `--uxw-pseudo-localization` | `build-gate` | Accented-padding smoke test in CI |
| Number splicing | `--uxw-number-splicing` | `interpolation-not-concat` | '{count} files' as one string |
| Tone-risk flags | `--uxw-tone-risk-flags` | `humor-idiom-marked` | Translator adaptation notes in catalog |
| Locale formatting | `--uxw-locale-formatting` | `intl-apis-only` | Dates/numbers never hand-formatted |
| RTL policy | `--uxw-rtl-policy` | `logical-properties+mirror` | Directional icons un-mirrored deliberately |
| Translation context | `--uxw-translation-context` | `screenshots+notes` | Strings ship with usage context |
| Locale coverage | `--uxw-locale-coverage` | `audit-per-locale` | copy-audit runs per active locale |

Consume them by linking `assets/css/localization-i18n.css` once at the app root and referencing `var(--uxw-...)` wherever copy policy drives styling — expansion headroom, RTL logical properties, and catalog contract notes all resolve through these custom properties, so no surface re-encodes its own i18n policy.

## 4. Composition

- **Composes with voice-tone (guide 02):** tone-risky strings (humor/idiom) are flagged for adaptation — the caution pairing is by design, since brand wordplay is exactly what literal translation destroys.
- **Composes with copy-audit (guide 12):** locale coverage is an audit dimension — missing keys and clipping are audit findings, not late-stage surprises.
- **Composes with skill-responsive-layout rtl-i18n-layout:** that guide owns the layout mirror; this guide owns the strings — the two contracts meet at logical properties and locale-formatted content.

## 5. Signature Patterns

- **The localization-ready string review:** new strings are checked for ICU usage, context notes, length budget, and tone-risk flags before merge — i18n debt is caught at the string level, where it is cheapest.
- **The pseudo-loc CI pass:** build with pseudo-localized catalogs and compare screenshots for overflow and hardcoded text — catching untranslated strings and clipping at build time, not in QA three weeks after launch.

## 6. Real-World Use Cases

- **Products serving multiple locales from day one,** where concatenation and hardcoded copy become untranslatable at scale.
- **Vietnamese/global products where diacritics and string length matter,** and font/render budgets are real constraints.
- **Auditing an internationalized product** for concatenated strings, clipped German buttons, and hand-formatted dates.

## 7. Combination Notes

### With other ux-writing skills

- **Good with writing-principles, button-labels, error-messages, component-microcopy, forms-labels, notifications, empty-states, onboarding-copy, and accessible-writing:** every one of those surfaces produces strings, and every string is a translation unit — their contracts (three-part errors, verb-first labels, destination-named links) hold in every locale, which is what makes a catalog coherent.
- **Caution with voice-tone:** deliberately — humor, puns, and idiom are the strings that literal translation turns into noise; they are flagged `--uxw-tone-risk-flags` for adaptation, and tone decisions must be re-made per locale, not copied.
- **Caution with copy-audit:** the audit must run per active locale (`--uxw-locale-coverage`) — an audit that only checks English strings passes a product whose German catalog is missing keys and whose Vietnamese text is clipped.
- **No avoid list:** this guide is a constraint on every other copy skill, not a rival — nothing in this repo is exempt from externalization.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and class-morphism:** short strings, generous whitespace, and auto-sizing components leave the ~35% expansion headroom that German, Russian, and Finnish demand; disciplined styles and disciplined strings reinforce each other.
- **Caution with retro:** retro styles often fix ornamental type sizes, decorative banners, and text-in-image compositions — all expansion-hostile and untranslatable; if used, decorative text must be re-examined per locale.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** locale-formatted dates, counts, and list lengths change the geometry animated elements traverse — duration and easing tokens keep transitions smooth when expansion changes layout mid-animation.
- **No caution list:** motion does not conflict with i18n directly; the one rule is that animated text reveals must not clip expanded strings mid-animation.

## 8. Anti-Patterns

- **Concatenated sentences** — 'You have ' + n + ' new messages' - untranslatable word order
- **Hardcoded copy** — strings buried in JSX/components escaping the catalog
- **Fixed-width English** — buttons that clip the moment German arrives
- **Literal tone translation** — puns carried word-for-word into languages where they are noise

### Accessibility Notes

Localization is accessibility at scale: WCAG 3.1.1 and 3.1.2 (language of page and parts) require `lang` attributes per locale, and translated alt text, labels, and headings are part of the same contract — an untranslated string left in the English catalog is an accessibility gap for that locale's users, not just a style defect. The fallback for teams that cannot adopt full ICU immediately is deliberately minimal: adopt one rule now — never concatenate sentence fragments — and externalize incrementally; the fragment rule prevents the worst breakage (shattered word order, missing plural forms) while the rest of the catalog migrates. Vietnamese adds a concrete rendering dimension: diacritics increase line height needs, so clipped accents are both an i18n and an accessibility failure.

## 9. Code Examples

### Example 1 — ICU plurals/select in en + vi, with an expansion-budget check

Tokens: `assets/css/localization-i18n.css`

```html
<div class="i18n-demo" lang="en">
  <p id="msg-files" class="i18n-msg">—</p><p id="msg-scope" class="i18n-msg">—</p>
  <div class="btn-row">
    <button id="btn-en" class="btn" type="button">Save changes</button>
    <button id="btn-de" class="btn" type="button" lang="de">Änderungen speichern</button>
  </div>
  <p id="budget-report" class="budget"></p>
</div>
<script>
  // Catalog: complete ICU messages, never concatenation (--uxw-message-format)
  const catalog = {
    en: { filesSelected: '{count, plural, one {# file selected} other {# files selected}}',
          scope: '{scope, select, team {Shared with your team} personal {Private to you} other {Unknown scope}}' },
    vi: { filesSelected: '{count, plural, other {Đã chọn # tệp}}',
          scope: '{scope, select, team {Dùng chung với nhóm} personal {Riêng tư} other {Không rõ}}' }
  };
  // Minimal ICU plural/select renderer — real projects use @formatjs/intl-messageformat
  function formatICU(pattern, args, locale) {
    return pattern.replace(/\{(\w+), (plural|select), ([^}]+\{[^}]*\}[^}]*)\}/, (m, key, type, body) => {
      const category = type === 'plural' ? new Intl.PluralRules(locale).select(args[key]) : String(args[key]);
      const branch = body.match(new RegExp(category + ' \\{([^}]*)\\}')) || body.match(/other \{([^}]*)\}/);
      return branch ? branch[1].replace('#', new Intl.NumberFormat(locale).format(args[key])) : '';
    });
  }
  function render(locale, count, scope) {
    const el = (id, msg, args) => document.getElementById(id).textContent = formatICU(msg, args, locale);
    el('msg-files', catalog[locale].filesSelected, { count });
    el('msg-scope', catalog[locale].scope, { scope });
  }
  render('en', 1, 'team');   render('vi', 5, 'team');  // en: "1 file selected" / vi: "Đã chọn 5 tệp" (one plural form)
  // Expansion budget: de must fit within 35% over en (--uxw-expansion-budget)
  const w = (id) => document.getElementById(id).getBoundingClientRect().width;
  const [en, de] = [w('btn-en'), w('btn-de')];
  document.getElementById('budget-report').textContent =
    `en ${Math.round(en)}px / de ${Math.round(de)}px — ${de <= en * 1.35 ? 'within' : 'OVER'} the 35% budget`;
</script>
<style>
  .i18n-demo { font: 14px/1.6 Inter, system-ui, sans-serif; padding: 16px; max-width: 420px;
               border: 1px solid var(--uxw-externalization, #ddd); border-radius: 8px; }
  .i18n-msg { margin: 0 0 12px; }
  .btn-row { display: flex; gap: 8px; }
  .btn { padding: 8px 16px; border-radius: 6px; border: none; cursor: pointer; }
  #btn-de { background: #f5f5f5; }
  .budget { font-size: 12px; color: #555; }
</style>
```

### Example 2 — Pseudo-localization toggle that surfaces clipping

Tokens: `assets/css/localization-i18n.css`

```html
<div class="pseudoloc">
  <label><input type="checkbox" id="psl-toggle"> Pseudo-localize (accented padding)</label>
  <p class="fixed-width" data-i18n="Save changes">Save changes</p>
  <p class="fixed-width" data-i18n="3 files selected">3 files selected</p>
  <p id="psl-report" class="psl-report">Toggle on to run the smoke test.</p>
</div>
<script>
  const map = { a:'à', e:'é', i:'ì', o:'ò', u:'ù', A:'À', E:'É', I:'Ì', O:'Ò', U:'Ù' };
  // Accented padding + bracketing: hardcoded strings become obvious, and the
  // added width simulates expansion so clipped text shows before locales ship
  const pseudoLocate = (s) => '[' + [...s].map(c => map[c] ?? c).join('') + '!]';
  const originals = [...document.querySelectorAll('[data-i18n]')].map(el => el.textContent);
  document.getElementById('psl-toggle').addEventListener('change', (e) => {
    document.querySelectorAll('[data-i18n]').forEach((el, i) => {
      el.textContent = e.target.checked ? pseudoLocate(originals[i]) : originals[i];
      // CI gate: flag any element that clips under pseudo-loc (--uxw-pseudo-localization)
      el.classList.toggle('clipped', el.scrollWidth > el.clientWidth);
    });
    const clipped = document.querySelectorAll('.clipped').length;
    document.getElementById('psl-report').textContent = clipped === 0
      ? 'Pass: no clipping, no hardcoded text detected.'
      : `Fail: ${clipped} element(s) clip — widen or externalize.`;
  });
</script>
<style>
  .pseudoloc { font: 14px/1.6 Inter, system-ui, sans-serif; padding: 16px; max-width: 420px; }
  .fixed-width { width: 160px; /* deliberately tight to demo the gate */ overflow: hidden;
                 white-space: nowrap; border-radius: 6px; padding: 6px 10px;
                 border: 1px solid var(--uxw-number-splicing, #ccc); }
  .fixed-width.clipped { outline: 2px solid #ef4444; }
  .psl-report { font-size: 12px; color: #555; }
</style>
```

## 10. Implementation Checklist

- [ ] Zero user-visible copy is hardcoded in components (`--uxw-externalization`), and all plurals/gender/selection use ICU formats — no sentence concatenation anywhere (`--uxw-message-format`).
- [ ] Numbers interpolate into complete strings ('{count} files selected'), never spliced mid-sentence (`--uxw-number-splicing`).
- [ ] Layout reserves 35% expansion headroom over English; buttons and labels auto-size (`--uxw-expansion-budget`).
- [ ] A pseudo-localization pass runs in CI and fails the build on clipping or untranslated text (`--uxw-pseudo-localization`).
- [ ] Dates, times, and numbers format only through Intl APIs — no hand-formatted locale content (`--uxw-locale-formatting`).
- [ ] Tone-risky strings carry adaptation notes for translators, and strings ship with screenshots + usage context (`--uxw-tone-risk-flags`, `--uxw-translation-context`).
- [ ] RTL locales render via logical properties with deliberate un-mirroring of directional icons (`--uxw-rtl-policy`), and the copy audit runs per active locale (`--uxw-locale-coverage`).
