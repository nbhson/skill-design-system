---
name: copy-audit
description: Keeping copy consistent at scale: the glossary, string inventory, linting, and the per-surface audit pass.
tags: [governance, copy-audit, glossary, linting, consistency]
related: [writing-principles, localization-i18n, accessible-writing]
---

# UX Writing Guide: Copy Audit & Governance

## 1. Definition

Copy quality decays without governance: term drift, style splits, and dead strings accumulate with every release. This guide is the governance layer that stops the decay. It defines the glossary (one concept, one term, with approved terms and banned synonyms), the string inventory (every shipped string mapped to its component, states, and locale keys), automated linting for the mechanical rules (sentence case, exclamation bans, placeholder-as-label detection), and the per-surface audit pass that scores copy against the repo's guides before release. The division of labor is explicit: machines enforce what is objective, humans judge what is not — tone, clarity, and completeness stay review dimensions, not regex targets.

## 2. Core Principles

- **One concept, one term:** the glossary is the single source — 'workspace' everywhere; synonyms are listed as banned.
- **The glossary ships with anti-terms:** approved term + banned synonyms + example sentence — definitions without bans do not enforce.
- **The string inventory is component-mapped:** every string knows its component, states, and locale keys — orphaned strings get pruned.
- **Lint what is mechanical:** sentence case, exclamation marks, title case, 'click here', double spaces — machines check rules so humans judge meaning.
- **Human review judges what lint cannot:** tone, clarity, and completeness (the three-part error contract) are review dimensions, not regex targets.
- **Audits are per-surface, scored:** the audit pass walks a surface against guides 01–11 with a scorecard — findings, not vibes.
- **Findings become tickets, audits become trends:** audit results tracked over time show copy debt shrinking — or not.
- **Governance has an owner:** a named person (or rotating pair) maintains glossary and lint rules — unowned standards decay.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Glossary | `--uxw-glossary` | `term+banned+example` | One concept, one term, anti-terms listed |
| Glossary owner | `--uxw-glossary-owner` | `named-owner` | Unowned standards decay |
| String inventory | `--uxw-string-inventory` | `component+locale-mapped` | Orphans pruned on schedule |
| Lint rules | `--uxw-lint-rules` | `case+!+click-here+caps` | Mechanical rules automated |
| Lint enforcement | `--uxw-lint-enforcement` | `PR-blocking` | Mechanical rules block, humans judge |
| Review dimensions | `--uxw-review-dimensions` | `tone+clarity+completeness` | The human review trio |
| Audit scope | `--uxw-audit-scope` | `per-surface-scorecard` | Walked against guides 01-11 |
| Audit frequency | `--uxw-audit-frequency` | `per-release+quarterly` | Release gates + trend reviews |
| Findings to tickets | `--uxw-findings-to-tickets` | `tracked-over-time` | Copy debt made visible |
| Locale audit | `--uxw-locale-audit` | `per-active-locale` | Missing keys + clipping per locale |

Consume them by linking `assets/css/copy-audit.css` and referencing `var(--uxw-...)` wherever governance surfaces render — scorecards, glossary tables, and lint reports draw their contract values from these custom properties, so the standards the UI displays are the standards the JSON and CSS own.

## 4. Composition

- **Composes with every guide in this repo:** the audit scorecard references each guide's contracts as its criteria — guides 01–11 define what good copy is; this guide defines how it is verified and kept good.
- **Composes with skill-design-review:** the review repo's content-audit section consumes this guide's scorecard format directly, so design review and copy review share one findings vocabulary.
- **Composes with localization-i18n (guide 10):** locale coverage and pseudo-loc gates are audit dimensions — a surface that passes in English but clips in German fails the audit.

## 5. Signature Patterns

- **The copy audit scorecard:** a per-surface checklist (glossary adherence, error completeness, alt text, lint status) with scores per guide — the audit's artifact, reusable across surfaces and releases so results are comparable.
- **The lint + review split:** PR-blocking mechanical rules plus human review for tone and clarity — automation where objective, judgment where subjective, and neither pretending to be the other.

## 6. Real-World Use Cases

- **Pre-release copy reviews for major surfaces,** where the scorecard is the release gate.
- **Copy debt cleanup campaigns across legacy screens,** tracked over time via the findings-to-tickets trend.
- **Design systems adding copy governance to component docs,** starting from the glossary and lint rules.

## 7. Combination Notes

### With other ux-writing skills

- **Good with writing-principles, button-labels, error-messages, empty-states, component-microcopy, forms-labels, notifications, voice-tone, and onboarding-copy:** every guide's contracts become scorecard rows — three-part errors, verb-first labels, no exclamation spam, placeholder-as-label checks — so the audit is literally the repo's standards turned into a checklist.
- **Good with accessible-writing and localization-i18n:** alt text, link text, reading order, and per-locale coverage are first-class audit dimensions; these two guides produce the findings most likely to be missed without a scorecard.
- **Caution with localization-i18n:** by design — audits must run per active locale (`--uxw-locale-audit`), which multiplies audit cost; scope it by release rather than auditing every locale every sprint.
- **No avoid list:** governance is the enforcement half of every other skill, not a competing discipline.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and class-morphism:** disciplined styles share this guide's instincts — few words, consistent terms, no decoration-as-meaning — so scorecard criteria map cleanly onto the style guide's rules.
- **No caution list:** expressive styles do not conflict with governance; the audit simply evaluates their copy against the same contracts, and style-driven wordplay is flagged for review rather than banned.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** audit tooling benefits from consistent transition tokens — scorecard UIs, lint report panels, and demo surfaces animate with the same durations the product uses, keeping review artifacts feeling like product.
- **No caution list:** motion copy (loading labels, progress text) is audited like any other string; there is no motion-specific exemption from the glossary or lint rules.

## 8. Anti-Patterns

- **Glossary without bans** — a definitions list that enforces nothing
- **Lint-only governance** — mechanical rules passing while clarity rots
- **Orphan strings** — dead keys in the catalog shipped to no surface
- **Unowned standards** — copy rules nobody maintains after the launch memo

### Accessibility Notes

The audit scorecard includes the accessibility dimensions — alt text, link text, reading order, plain language — as first-class rows, not a bonus appendix: copy governance is where accessible-writing compliance is actually enforced per release, because a scorecard row has an owner, a status, and a trend, while 'we care about a11y' does not. The fallback for teams that cannot stand up a full governance program is deliberately small: begin with two artifacts — the glossary and the lint rules — and add the audit scorecard when the surface area grows; the glossary stops term drift immediately, the linter stops mechanical regressions in CI, and both make the eventual audit cheap because most findings were prevented at the source.

## 9. Code Examples

### Example 1 — Copy audit scorecard: per-guide rows with pass/fail

Tokens: `assets/css/copy-audit.css`

```html
<table class="scorecard">
  <caption>Copy audit — Checkout surface (release 24.11)</caption>
  <thead>
    <tr><th scope="col">Guide</th><th scope="col">Criterion</th><th scope="col">Status</th><th scope="col">Finding</th></tr>
  </thead>
  <tbody>
    <tr><td>01 writing-principles</td><td>Sentence case, plain language</td><td><span class="pass">Pass</span></td><td>—</td></tr>
    <tr><td>03 error-messages</td><td>What + why + fix contract</td><td><span class="fail">Fail</span></td><td>Card error lacks the fix</td></tr>
    <tr><td>07 component-microcopy</td><td>Placeholder never the only label</td><td><span class="fail">Fail</span></td><td>Card number field</td></tr>
    <tr><td>09 notifications</td><td>No exclamation marks</td><td><span class="pass">Pass</span></td><td>—</td></tr>
    <tr><td>11 accessible-writing</td><td>Descriptive links + alt</td><td><span class="pass">Pass</span></td><td>—</td></tr>
  </tbody>
</table>
<style>
  .scorecard { font: 13px/1.5 Inter, system-ui, sans-serif; border-collapse: collapse; max-width: 560px; }
  .scorecard caption { text-align: left; font-weight: 600; padding-bottom: 8px; }
  .scorecard th, .scorecard td { text-align: left; padding: 6px 10px; border-bottom: 1px solid var(--uxw-audit-scope, #e5e5e5); }
  .scorecard th { color: var(--uxw-review-dimensions, #404040); font-weight: 600; }
  .pass, .fail { font-size: 12px; padding: 2px 8px; border-radius: 999px; }
  .pass { background: #DCFCE7; color: #166534; }
  .fail { background: #FEE2E2; color: #991B1B; }
</style>
```

### Example 2 — Mini glossary table + JS lint panel

Tokens: `assets/css/copy-audit.css`

```html
<div class="governance">
  <table class="glossary">
    <thead><tr><th>Term</th><th>Banned synonyms</th><th>Example</th></tr></thead>
    <tbody>
      <tr><td>workspace</td><td>team, project, site</td><td>“Invite people to your workspace.”</td></tr>
      <tr><td>remove</td><td>delete (soft actions), zap</td><td>“Remove member from workspace.”</td></tr>
      <tr><td>email address</td><td>e-mail, mail</td><td>“Enter your work email address.”</td></tr>
    </tbody>
  </table>
  <label class="lint-label" for="lint-input">Sample string to lint:</label>
  <input id="lint-input" class="lint-input" value="  Click HERE to continue! You have  3 new messages.">
  <button class="lint-btn" type="button" id="lint-run">Run lint</button>
  <ul id="lint-report" class="lint-report"></ul>
</div>
<script>
  // Mechanical rules only (--uxw-lint-rules) — tone/clarity stay human review
  const rules = [
    { name: 'sentence case', test: s => /^[A-Z][^A-Z]*$/.test(s.trim()) || /\b[A-Z]{2,}\b/.test(s) === false, msg: 'Use sentence case — no SHOUTING words.' },
    { name: 'no exclamation marks', test: s => !s.includes('!'), msg: 'Exclamation marks are banned in system copy (--uxw-lint-rules).' },
    { name: 'no "click here"', test: s => !/click here/i.test(s), msg: 'Links name the destination, never the mechanism (WCAG 2.4.4).' },
    { name: 'no double spaces', test: s => !s.includes('  '), msg: 'Collapse double spaces.' },
    { name: 'no leading/trailing spaces', test: s => s.trim() === s, msg: 'Trim surrounding whitespace.' }
  ];
  function lint() {
    const report = document.getElementById('lint-report');
    report.innerHTML = '';
    const failures = rules.filter(r => !r.test(document.getElementById('lint-input').value));
    const msgs = failures.length
      ? failures.map(f => `✕ ${f.msg}`)
      : ['✓ All mechanical rules pass — human review still judges tone and clarity.'];
    msgs.forEach(text => {
      const li = document.createElement('li');
      li.textContent = text;
      report.appendChild(li);
    });
  }
  document.getElementById('lint-run').addEventListener('click', lint);
  lint(); // initial run on the seeded violation
</script>
<style>
  .governance { font: 13px/1.5 Inter, system-ui, sans-serif; max-width: 560px; }
  .glossary { border-collapse: collapse; width: 100%; margin-bottom: 16px; }
  .glossary th, .glossary td { text-align: left; padding: 6px 10px; border-bottom: 1px solid var(--uxw-glossary, #e5e5e5); }
  .glossary th { font-weight: 600; color: #404040; }
  .lint-label { display: block; font-weight: 600; margin-bottom: 4px; }
  .lint-input { width: 100%; padding: 8px 10px; border: 1px solid var(--uxw-string-inventory, #ccc); border-radius: 6px; font: inherit; }
  .lint-btn { margin: 8px 0; padding: 8px 16px; border: none; border-radius: 6px; background: #2563EB; color: #fff; cursor: pointer; }
  .lint-report { margin: 0; padding-left: 18px; color: #991B1B; }
  .lint-report li:only-child { color: #166534; }
</style>
```

## 10. Implementation Checklist

- [ ] The glossary lists every approved term with banned synonyms and an example sentence (`--uxw-glossary`).
- [ ] A named owner maintains the glossary and lint rules; the owner is documented, not implied (`--uxw-glossary-owner`).
- [ ] The string inventory maps every string to its component, states, and locale keys; orphans are pruned on a schedule (`--uxw-string-inventory`).
- [ ] Mechanical rules (sentence case, exclamation marks, 'click here', ALL CAPS, double spaces) are automated and PR-blocking (`--uxw-lint-rules`, `--uxw-lint-enforcement`).
- [ ] Human review covers tone, clarity, and completeness — never reduced to regex checks (`--uxw-review-dimensions`).
- [ ] Each release walks a per-surface scorecard against guides 01–11, with findings filed as tickets (`--uxw-audit-scope`, `--uxw-findings-to-tickets`).
- [ ] The audit runs per active locale — missing keys and clipping are findings, not QA surprises (`--uxw-locale-audit`).
- [ ] Audit results are tracked over time so copy debt trends are visible (`--uxw-audit-frequency`).
