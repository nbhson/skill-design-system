---
name: content-microcopy-audit
description: The strings pass for design reviews — error completeness, label specificity, reading level, and glossary adherence, checked per surface.
tags: [microcopy, content, ux-writing, strings, audit]
related: [typography-audit, review-process, a11y-audit]
---

# Design Review Guide: Content & Microcopy Audit

## 1. Definition

The content audit walks every string on a surface against the ux-writing contracts: errors carry what+why+fix, buttons are verb-first and specific, labels aren't placeholders, links name destinations, terminology matches the glossary, and reading level holds. Because the contracts are mechanical (three-part errors, verb-first labels), much of this pass is scriptable — the human pass judges tone and clarity. Hidden strings (aria-labels, alt text, tooltips) get exactly the same treatment as visible copy, which is what distinguishes a content audit from a proofread: it inventories the surface's entire string layer, visible and not, and scores each class against a named contract rather than a reviewer's mood.

## 2. Core Principles

- **Errors are complete:** every error string on the surface carries what+why+fix (ux-writing error-messages) — missing parts are findings.
- **Buttons are verb-first and specific:** the OK/Submit family on consequential actions is a named finding.
- **No placeholder-as-label:** fields checked for vanishing instructions (3.3.2) — a mechanical check with high user cost.
- **Links name destinations:** "click here" links are mechanical findings (2.4.4).
- **Terminology matches the glossary:** one concept, one term — drift logged per string (copy-audit contract).
- **Reading level holds:** long strings sampled against the grade-8 target — overloaded sentences are findings.
- **Tone matches the state:** humor in error paths, gloating success — the tone matrix is the criteria (voice-tone).
- **Every string is findable in context:** alt text, aria-labels, and tooltips get the same audit as visible copy.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Error completeness | `--rev-error-completeness` | `what+why+fix-required` | Missing parts = finding |
| Button specificity | `--rev-button-specificity` | `verb-first-no-generic` | OK/Submit on consequential = finding |
| Placeholder check | `--rev-placeholder-check` | `no-placeholder-labels` | Mechanical, high-cost |
| Link text | `--rev-link-text` | `destination-named` | 2.4.4; "click here" = finding |
| Glossary adherence | `--rev-glossary-adherence` | `one-concept-one-term` | Drift logged |
| Reading level | `--rev-reading-level` | `grade-8-sampled` | Long strings sampled |
| Tone match | `--rev-tone-match` | `tone-matrix-criteria` | voice-tone contract |
| Hidden strings audited | `--rev-hidden-strings-audited` | `alt+aria+tooltip` | Same audit as visible copy |
| Front-load check | `--rev-front-load-check` | `meaning-first-40-chars` | Truncation-safe strings |
| Content score | `--rev-content-score` | `per-surface` | Feeds report template |

Consume them by linking `assets/css/content-microcopy-audit.css` at the review harness root; the string-walk tooling reads `var(--rev-...)` values as its rule set, so tightening a contract (for example, adding front-load checking) changes the audit everywhere without touching its scripts.

## 4. Composition

- **Composes with skill-ux-writing:** that repo owns the copy contracts; this audit scores adherence per surface. The split of labor is strict — ux-writing defines what a complete error is, this audit counts the surfaces that fail the definition.
- **Composes with review-process (guide 01):** content findings flow through the severity scale and ticket loop — a dead-end error on a checkout path is a blocker there exactly as a focus-ring removal is in the states audit.
- **Composes with typography-audit (guide 06):** copy and its typography reviewed in the same pass — a sentence flagged for reading level and a heading flagged for scale are one rework ticket, not two, because both get fixed in the same text block.

## 5. Signature Patterns

- **The string walk:** every visible + hidden string on the surface listed and checked against the ux-writing token contracts — the audit's data layer. The walk produces the inventory (selectors, text, contract, verdict) that the human pass annotates with tone and clarity judgments.
- **The lint + judgment split:** mechanical checks (verb-first, click-here, placeholders) scripted; tone/clarity judged by reviewers — same split as copy-audit. Scripts catch the objective half deterministically so the human pass spends its attention where machines are weak.

## 6. Real-World Use Cases

- **Pre-release gates on copy-bearing surfaces,** where error completeness and button specificity are release-blocking checks.
- **Localization readiness audits,** where strings are checked pre-translation — front-loaded meaning and glossary-consistent terms survive translation; puns and truncated-by-design strings do not.
- **Audit deliverables:** dead-end errors, mystery buttons, and placeholder labels reported per surface with the content score.

## 7. Combination Notes

### With other design-review skills

- **Good with review-process and report-template:** mechanical string findings carry objective severity and feed the per-surface content score into the final report.
- **Good with typography-audit and consistency-audit:** copy and its rendering are reworked together, and glossary drift is the consistency check applied to language instead of pixels.
- **Good with a11y-audit, interaction-states-audit, spacing-rhythm-audit, visual-hierarchy-audit, perceived-performance, responsive-audit, and motion-audit:** the string walk feeds them — aria-labels to the a11y and states audits, empty-state copy to spacing and hierarchy, loading strings to perceived-performance — and their findings return as copy that needs rewriting.
- **Caution with visual-hierarchy-audit:** it appears in both the good and caution lists deliberately. The pairing is good because layout hierarchy and copy review inform each other; the caution is sequencing — hierarchy fixes (shortening, truncating, relocating copy) can invalidate string-walk verdicts mid-review, so run content findings to completion before layout rework begins, or re-walk the changed strings.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three strip decoration, which shifts expressive weight onto the words — a minimalist surface with vague copy has nothing else carrying meaning, so the audit's contracts are load-bearing rather than cosmetic in these styles.
- **No caution entries:** none of the audited styles rely on verbose or decorative copy that would fight the verb-first, grade-8 contracts; the string rules are style-neutral.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** strings and their transitions are a unit — toast messages, inline error reveals, and button label swaps animate with easing/duration tokens, and the audit verifies the string front-loads meaning within the first 40 characters so the message reads before the motion completes.

## 8. Anti-Patterns

- **Dead-end errors shipped:** what+why+fix missing on live surfaces
- **Mystery buttons:** 'OK' on consequential actions
- **Unaudited hidden strings:** aria-labels and tooltips exempted from review
- **Copy-late culture:** strings written after layout freezes

### Accessibility Notes

The content audit covers the copy side of WCAG 3.3.1-3.3.3, 2.4.4, 2.4.6, and 1.1.1: complete errors (3.3.1 error suggestion, 3.3.3 error prevention), named links (2.4.4) and labels or instructions (2.4.6), and alt text for meaningful images (1.1.1) — hidden strings (aria, alt) are first-class audit targets, not exemptions, because for screen-reader users they are the visible copy. Placeholder-as-label fails 3.3.2 (labels or instructions) the moment the placeholder vanishes on input; color-of-link is never sufficient since link text must name its destination out of context. The fallback rule: if the full string walk is too heavy, audit errors + links + icon names first — those three string classes carry the highest a11y and trust impact, and the remaining contracts (reading level, tone, front-load) can follow in a second pass without losing blocker coverage.

## 9. Code Examples

### Example 1 — String walk: visible + hidden strings checked against contracts

Tokens: `assets/css/content-microcopy-audit.css`

```html
<form class="walk-demo" novalidate>
  <input class="email" type="email" placeholder="Enter your email" aria-label="Email address" />
  <p class="error" role="alert">Invalid input.</p>
  <a class="docs" href="/docs/tokens">click here</a>
  <img class="logo" src="logo.png" alt="" />
  <button class="save" type="button">OK</button>
</form>
<pre id="walk-out"></pre>
<style>
  :root {
    /* mirrors assets/css/content-microcopy-audit.css */
    --rev-error-completeness: what+why+fix-required;
    --rev-placeholder-check: no-placeholder-labels;
    --rev-link-text: destination-named;
    --rev-button-specificity: verb-first-no-generic;
    --rev-hidden-strings-audited: alt+aria+tooltip;
  }
  .walk-demo { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 340px; }
  .error { color: #DC2626; margin: 8px 0; }
  pre { font: 12px/1.6 ui-monospace, monospace; }
</style>
<script>
  // The string walk: every visible + hidden string, checked against its contract.
  const findings = [];
  const err = document.querySelector('.error');
  if (!/\bfix\b|try|correct/i.test(err.textContent)) // crude what+why+fix probe
    findings.push('FAIL error: lacks why+fix (--rev-error-completeness)');
  if (document.querySelector('.email').placeholder && !document.querySelector('label[for]'))
    findings.push('FAIL field: placeholder-as-label (--rev-placeholder-check, WCAG 3.3.2)');
  if (/click here/i.test(document.querySelector('.docs').textContent))
    findings.push('FAIL link: destination not named (--rev-link-text, WCAG 2.4.4)');
  if (!document.querySelector('.logo').alt)
    findings.push('WARN img: empty alt on meaningful logo (--rev-hidden-strings-audited)');
  if (/^OK$|^Submit$/.test(document.querySelector('.save').textContent.trim()))
    findings.push('FAIL button: generic on consequential action (--rev-button-specificity)');
  document.getElementById('walk-out').textContent =
    findings.length ? findings.join('\n') : 'All string contracts pass.';
</script>
```

### Example 2 — Glossary adherence checker: term drift finder

```html
<article class="gloss-demo">
  <p>Add a member to your <span data-term>workspace</span>.</p>
  <p>Invite teammates to your <span data-term>organization</span>.</p>
  <p>Members see everything in the <span data-term>org</span>.</p>
</article>
<pre id="gloss-out"></pre>
<style>
  :root { --rev-glossary-adherence: one-concept-one-term; }
  .gloss-demo { font: 14px/1.6 Inter, system-ui, sans-serif; max-width: 360px; }
  .gloss-demo .drift { background: #FEF3C7; outline: 1px solid #F59E0B; }
  pre { font: 12px/1.6 ui-monospace, monospace; }
</style>
<script>
  // Per --rev-glossary-adherence: one concept, one term — drift logged per string.
  const GLOSSARY = { workspace: ['organization', 'org', 'team', 'tenant'] };
  const findings = [];
  document.querySelectorAll('[data-term]').forEach((el) => {
    const t = el.textContent.trim().toLowerCase();
    for (const [canonical, variants] of Object.entries(GLOSSARY)) {
      if (variants.includes(t)) {
        el.classList.add('drift');
        findings.push('DRIFT: "' + t + '" → canonical "' + canonical + '" (--rev-glossary-adherence)');
      }
    }
  });
  document.getElementById('gloss-out').textContent =
    findings.length ? findings.join('\n') : 'Glossary adherence: no drift found.';
</script>
```

## 10. Implementation Checklist

- [ ] Every error string passes `var(--rev-error-completeness)` — what happened, why, and how to fix it, with no dead ends.
- [ ] Consequential buttons pass `var(--rev-button-specificity)` — verb-first, named actions; no OK/Submit family members.
- [ ] Fields pass `var(--rev-placeholder-check)` — real labels, no instructions that vanish on input (WCAG 3.3.2).
- [ ] Links pass `var(--rev-link-text)` — destinations named out of context; zero "click here" strings (WCAG 2.4.4).
- [ ] Terminology passes `var(--rev-glossary-adherence)` — the drift finder reports zero unresolved variants.
- [ ] Long strings sampled against `var(--rev-reading-level)` (grade-8) and `var(--rev-front-load-check)` (meaning in the first 40 chars).
- [ ] Hidden strings pass `var(--rev-hidden-strings-audited)` — alt text, aria-labels, and tooltips in the same inventory as visible copy.
- [ ] Tone checked against `var(--rev-tone-match)` and the per-surface `var(--rev-content-score)` recorded in the report template.
