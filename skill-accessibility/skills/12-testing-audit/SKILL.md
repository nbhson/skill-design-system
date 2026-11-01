---
name: testing-audit
description: The three-layer a11y test strategy: automated CI, manual keyboard/zoom passes, and screen reader listening scripts - plus the audit report format.
tags: [testing, audit, ci, axe-core, wcag]
related: [screen-readers, keyboard-navigation, wcag-fundamentals]
---

# Accessibility Skill: Testing & Audit Framework

## 1. Definition

Accessibility testing is a layered strategy because each layer catches what the others cannot: automated tools (axe-core, Lighthouse) catch roughly 30-40% of issues mechanically; manual keyboard and zoom passes catch operability issues; screen reader listening scripts validate the lived experience. This skill assembles the layers into a CI pipeline and audit framework - with severity ratings, a report format, and regression gates so accessibility stays fixed once found. It is the verification half of the accessibility system: without it, every sibling guide's contract is aspirational prose rather than an enforced property.

## 2. Core Principles

- **Three layers, always:** automated in CI, manual keyboard/zoom per release, screen reader scripts per core flow.
- **Automated checks run on every PR:** axe-core on component tests plus page-level scans; critical violations block merge.
- **Manual passes are scripted, not vibes:** keyboard-only task completion, 200%/400% zoom, and reflow checks with recorded outcomes.
- **Severity follows impact:** blocker (task impossible), critical (major friction), major (workaround exists), minor (polish) - blockers gate release.
- **Audit findings are tickets with evidence:** WCAG criterion, repro steps, screenshot or narration quote, suggested fix.
- **Track trend, not snapshot:** violation counts per release and open-blocker age tell whether the system is improving.
- **Test with assistive tech in the loop:** paid user testing with disabled users finds what simulations never will.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| CI tool | `--a11y-ci-tool` | `axe-core` | Component + page scans on every PR |
| CI policy | `--a11y-ci-policy` | `critical-blocks-merge` | Zero new critical violations per PR |
| Lighthouse | `--a11y-lighthouse-threshold` | `a11y-score-95+` | Release gate; trend-tracked |
| Keyboard pass | `--a11y-manual-pass-keyboard` | `per-release` | Mouse-unplugged core flows, recorded |
| Zoom pass | `--a11y-manual-pass-zoom` | `per-release` | 200% text / 400% reflow walkthroughs |
| Listening | `--a11y-listening-scripts` | `core-flows` | NVDA/VoiceOver scripts per critical journey |
| Severity | `--a11y-severity-scale` | `blocker-critical-major-minor` | Blockers gate release |
| Report | `--a11y-audit-report-format` | `criterion-evidence-fix` | Every finding cites WCAG + evidence + suggested fix |
| Regression | `--a11y-regression-watch` | `fixed-stays-fixed` | Fixed violations become automated tests |
| User testing | `--a11y-user-testing-cadence` | `quarterly` | Sessions with disabled users; findings feed roadmap |

Consume them by linking `assets/css/testing-audit.css` at the CI configuration root and referencing `var(--a11y-ci-policy)` in branch-protection rules, `var(--a11y-severity-scale)` in the issue tracker's a11y label set, and `var(--a11y-audit-report-format)` in the report template. Like the other a11y token sets, these are policy commitments enforced by process, so a gate that is not wired to CI is a token violation even if the code passes.

## 4. Composition

- **Composes with every sibling:** each provides its checklist section to the audit - contrast pairings, keyboard keymaps, form wiring, reflow passes - and this skill sequences them into a process with gates and evidence.
- **Composes with skill-design-review (companion repo):** the design-side audit (guide 12 there) runs before build; this framework runs during and after, so findings never start as "we shipped it and then checked".
- **Composes with governance (skill-design-tokens guide 12):** a11y gates are enforced by the same CI machinery as token rules - one pipeline, one merge gate, two categories of violation.

## 5. Signature Patterns

- **Fixed-stays-fixed regression tests:** every fixed violation becomes an automated assertion, so the backlog can only shrink. A regression re-opens the original ticket with the failing CI link attached.
- **Severity-weighted audit report:** executive summary + criterion-indexed findings + prioritized fix roadmap, refreshed per release. Executives read page one; engineers work from the criterion index.

## 6. Real-World Use Cases

- **Standing up an a11y practice:** CI tooling, manual scripts, and report format from zero.
- **Pre-launch and periodic conformance audits** with evidence.
- **Continuous monitoring:** trend dashboards and regression gates.

## 7. Combination Notes

### With other accessibility skills

- **Good with screen-readers:** listening scripts are a required lane in this framework; the screen-reader skill supplies the pairing matrix and keystroke knowledge, this skill supplies the schedule and gate.
- **Good with keyboard-navigation and zoom-reflow:** the mouse-unplugged and 200%/400% passes are scripted manual layers here - those skills define what to check, this one defines when and with what evidence.
- **Good with wcag-fundamentals:** the criteria-to-feature matrix from that skill is the index this audit reports against; findings without a criterion cannot be triaged.
- **Good with color-contrast, forms-errors, and aria-patterns-widgets:** each contributes checklist sections; the audit is their scheduled execution.
- **Caution/avoid: none.** Every sibling skill's contract is only as real as the test that verifies it.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** simpler surfaces produce smaller audit surface area - fewer overlapping states, fewer decorative effects that defeat automated contrast and naming checks, so CI results stay meaningful.
- **Caution: none recorded.** No style is incompatible with testing itself; the caution is that heavily decorated styles (glassmorphism, collage-art) require more manual passes because automation judges them poorly, so budget audit time accordingly.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion:** the audit includes a reduced-motion pass - verifying that every animation collapses to its static resting state - which is only meaningful when animation itself is token-driven.
- **Caution: none recorded.** Motion skills do not conflict with testing; they expand its checklist (prefers-reduced-motion, pauseability, vestibular safety) rather than undermine it.

## 8. Anti-Patterns

- **Score-chasing** — optimizing a Lighthouse number while keyboard flows stay broken
- **Audit-and-shelve** — a 90-page report nobody turns into tickets
- **One-time testing** — conformance declared at launch, regressions shipping freely after
- **Simulation-only validation** — no disabled users ever consulted, only tools and checklists

### Accessibility Notes

This is the meta-skill of verification: without a testing framework, every other guide's contract is aspirational - this is how conformance is proven, maintained, and improved. The framework itself has an equity obligation: automation over-covers what tools can parse (contrast, labels, ARIA structure) and under-covers cognitive and lived-experience criteria, so the manual and listening layers are mandatory lanes, not optional depth, and the quarterly user-testing cadence keeps real disabled users in the loop. The fallback defines coverage triage: when full coverage is impossible, test in this order - blockers on core flows first, then automation on everything, then listening scripts on the highest-traffic journeys - so constrained effort lands where task failure hurts most, with `var(--a11y-severity-scale)` recording the decision.

## 9. Code Examples

### Example 1 — axe-core in CI, blocking merge on criticals

Tokens: `assets/css/testing-audit.css`

```html
<!-- audit.html — page scanned by axe on every PR (--a11y-ci-tool: axe-core) -->
<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Billing overview</title></head>
<body>
  <a class="skip" href="#main">Skip to main content</a>
  <header><nav aria-label="Primary"><a href="/billing">Billing</a></nav></header>
  <main id="main">
    <h1>Billing overview</h1>
    <label for="account">Account number</label>
    <input id="account" name="account" type="text">
    <button type="submit">View statements</button>
  </main>
</body>
</html>
<script>
  // ci/axe-check.js — runs in Playwright on every PR; criticals block merge
  // const { AxeBuilder } = require('@axe-core/playwright');
  // test('billing page has zero critical violations', async ({ page }) => {
  //   await page.goto('/billing');
  //   const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag22aa']).analyze();
  //   const criticals = results.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
  //   expect(criticals).toEqual([]); // --a11y-ci-policy: critical-blocks-merge
  // });
</script>
```

### Example 2 — Manual pass checklist + audit report sample

Tokens: `assets/css/testing-audit.css`

```html
<section class="checklist" aria-labelledby="ck-title">
  <h2 id="ck-title">Manual release pass (keyboard + zoom)</h2>
  <ul>
    <li>Complete "pay invoice" keyboard-only, mouse unplugged (--a11y-manual-pass-keyboard)</li>
    <li>Repeat at 200% text zoom, then 400% page zoom at 320px (--a11y-manual-pass-zoom)</li>
    <li>Run the NVDA listening script for checkout (--a11y-listening-scripts)</li>
  </ul>
</section>
<table class="report">
  <caption>Q4 audit — findings per --a11y-audit-report-format (criterion-evidence-fix)</caption>
  <thead><tr><th>ID</th><th>Criterion</th><th>Severity</th><th>Evidence</th><th>Fix</th></tr></thead>
  <tbody>
    <tr><td>A-014</td><td>WCAG 2.1.1</td><td>blocker</td><td>Screenshot: card menu not tab-reachable</td><td>Replace div with button + menu pattern</td></tr>
    <tr><td>A-021</td><td>WCAG 1.4.3</td><td>major</td><td>Placeholder gray on white = 2.8:1</td><td>Use --dt-color-neutral-500 placeholder</td></tr>
    <tr><td>A-009</td><td>WCAG 2.4.7</td><td>fixed → regression test</td><td>NVDA quote: "button" (unnamed)</td><td>aria-label="Close dialog" (now asserted in CI)</td></tr>
  </tbody>
</table>
<style>
  body { font: 14px/1.6 system-ui, sans-serif; max-width: 640px; margin: 0 auto; }
  .checklist li { margin-bottom: 6px; }
  .report { width: 100%; border-collapse: collapse; margin-top: 24px; }
  .report caption { text-align: left; font-weight: 600; margin-bottom: 8px; }
  .report th, .report td { border: 1px solid #D4D4D4; padding: 8px; text-align: left; }
  .report th { background: #F5F5F5; }
</style>
```

## 10. Implementation Checklist

- [ ] axe-core runs on every PR and serious/critical violations block merge (`--a11y-ci-tool`, `--a11y-ci-policy`).
- [ ] Lighthouse a11y score is trend-tracked against the 95+ release gate (`--a11y-lighthouse-threshold`).
- [ ] Keyboard-only mouse-unplugged passes run per release with recorded outcomes (`--a11y-manual-pass-keyboard`).
- [ ] 200% text and 400% zoom reflow walkthroughs run per release (`--a11y-manual-pass-zoom`).
- [ ] Every core flow has an NVDA/VoiceOver listening script in the test plan (`--a11y-listening-scripts`).
- [ ] Findings use the criterion-evidence-fix format and the shared severity scale (`--a11y-audit-report-format`, `--a11y-severity-scale`).
- [ ] Fixed violations become automated regression assertions (`--a11y-regression-watch`).
- [ ] Quarterly sessions with disabled users are scheduled and feed the roadmap (`--a11y-user-testing-cadence`).