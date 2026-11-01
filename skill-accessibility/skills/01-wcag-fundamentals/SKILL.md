---
name: wcag-fundamentals
description: The POUR principles, conformance levels, and the WCAG 2.2 success-criteria map that anchors every other accessibility decision.
tags: [wcag, conformance, pour, policy, accessibility]
related: [color-contrast, keyboard-navigation, focus-management]
---

# Accessibility Skill: WCAG Fundamentals

## 1. Definition

WCAG (Web Content Accessibility Guidelines) is the shared legal and technical contract for accessibility: four POUR principles (Perceivable, Operable, Understandable, Robust), three conformance levels (A, AA, AAA), and versioned success criteria. This skill is the map layer — it does not replace the specialized skills (contrast, keyboard, ARIA) but tells you which criteria apply to which UI situation and which level your product must claim. Most laws (EN 301 549, Section 508, ADA case law) reference WCAG 2.1/2.2 AA as the practical bar, so pinning the version and level once — and enforcing it through design review, code review, and CI — is what turns accessibility from a values statement into an engineering discipline.

## 2. Core Principles

- **Target AA, treat AAA as selective upgrades:** AA is the legal and contractual norm; AAA criteria (7:1 contrast, no timing) apply per-criterion where feasible.
- **POUR is a checklist of questions, not poetry:** can users perceive it, operate it, understand it — and does assistive tech parse it robustly?
- **WCAG 2.2 is the current bar:** new criteria — target size (2.5.8), focus appearance (2.4.13), dragging movements (2.5.7), accessible authentication (3.3.8) — are now in scope.
- **Conformance is per-page and honest:** one failing component fails the page; partial-conformance claims must say exactly what fails.
- **Level A failures are blockers:** missing alt, no keyboard path, or unlabeled inputs fail nearly everyone — ship nothing that fails A.
- **Accessibility is a release criterion, not a cleanup phase:** criteria are checked at design review, code review, and CI.
- **An accessibility statement documents the position:** conformance claim, known limitations, and a feedback channel — not a badge.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Conformance | `--a11y-conformance-target` | `WCAG 2.2 AA` | The product-wide claim; AAA is per-criterion upgrades |
| Conformance | `--a11y-level-a-policy` | `blocker` | Level A failures block release without exception |
| Conformance | `--a11y-level-aa-policy` | `blocker` | AA failures block release or ship with documented exceptions |
| Conformance | `--a11y-level-aaa-policy` | `selective` | Applied where cheap: contrast 7:1 on reading surfaces |
| Conformance | `--a11y-review-gate-design` | `a11y-design-review` | Designs pass an a11y checklist before build |
| Conformance | `--a11y-review-gate-code` | `a11y-code-review` | PRs touch aria/semantics - a11y reviewer required |
| Conformance | `--a11y-review-gate-ci` | `axe-ci` | Automated axe-core run on every PR; zero critical violations |
| Conformance | `--a11y-statement-required` | `published` | Public accessibility statement with feedback channel |
| Conformance | `--a11y-criteria-version-pin` | `2.2` | Pinned WCAG version; re-map criteria on major updates |
| Conformance | `--a11y-legal-baselines` | `EN 301 549, Section 508, ADA` | All reference WCAG AA - one target covers the law |

These are policy tokens, not pixels: declare them once by loading `assets/css/wcag-fundamentals.css` (or the config manifest it generates) at the app root, then reference `var(--a11y-<role>)` from review templates, CI configuration, and the published accessibility statement so the conformance claim has exactly one source of truth. When the pinned version changes, re-map the criteria matrix through governance — never by editing gates piecemeal.

## 4. Composition

- **This skill composes with every sibling:** contrast-validation, keyboard-navigation, and aria-patterns each own the criteria this map points to — the map tells you where to look, the siblings tell you how to fix.
- **It composes with design-tokens:** contrast thresholds and focus tokens are enforced as token properties (skill-design-tokens guide 08), so WCAG numbers become lintable values instead of tribal knowledge.
- **It composes with reduced-motion (skill-animation guide 12):** motion accessibility is the animation-side twin of this repo's map — same governance, different criteria.

## 5. Signature Patterns

- **Criteria-to-feature matrix:** for each feature, list applicable WCAG criteria and their test method (automated, manual, screen reader) before build — the matrix becomes the review checklist and the audit scope in one artifact.
- **Three-gate enforcement:** design review checklist + PR review labels + CI axe run — one gate alone always leaks, because designs reach code unreviewed and code reaches prod untested; overlapping gates catch what each other's blind spots miss.

## 6. Real-World Use Cases

- **Products establishing their first formal accessibility conformance target:** pick the level, pin the version, and publish the gates before the first audit.
- **Legal/procurement review:** EN 301 549, Section 508, or enterprise VPAT documentation demands an honest, current conformance claim.
- **Auditing an existing product:** mapping features to criteria to find untested surfaces — the matrix exposes whole features nobody ever checked.

## 7. Combination Notes

### With other accessibility skills

- **Good with everything — color-contrast, keyboard-navigation, focus-management, aria-fundamentals, aria-patterns-widgets, forms-errors, screen-readers, media-alt-text, cognitive-content, zoom-reflow, testing-audit:** this skill is the map, the others are the territory; every specialized guide resolves its practices back to criteria this skill scopes and gates.
- **No caution or avoid list:** nothing contradicts a conformance map; the only failure mode is a team that keeps the map and ignores the gates.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** restrained palettes, clear hierarchy, and solid boundaries make Perceivable/Operable criteria cheap to satisfy — the styles do most of the conformance work for free.
- **Caution with neumorphism and brutalism-ui:** soft-on-soft shadows destroy 3:1 non-text contrast and deliberately raw type breaks readability thresholds; if a style choice fights a criterion, the criterion wins or the exception is documented.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion and easing-timing:** reduced-motion maps directly to WCAG 2.3.3 and vestibular safety, and disciplined timing keeps animations inside perceivable, interruptible bounds.
- **Caution with ambient-motion:** continuously animated backgrounds risk 2.2.2 (pause/stop/hide) failures; anything ambient needs a documented stop control.

## 8. Anti-Patterns

- **Badge accessibility** — an audit passed once and a badge displayed forever while the product regresses
- **AAA theater** — chasing AAA headlines while Level A basics like alt text and labels fail
- **Retro-fit phase** — deferring accessibility to a pre-launch sprint where it becomes a rewrite
- **Statement as shield** — publishing a conformance claim that CI results would immediately falsify

### Accessibility Notes

The meta-skill: everything here exists to serve disabled users — screen reader, keyboard-only, low-vision, motor, and cognitive-needs users are the primary personas for every sibling guide. The map layer's specific duty is honesty: conformance is claimed per page, one failing component fails the page, and partial claims must name exactly what fails. The fallback rule is equally strict: when a criterion cannot be met, ship the documented exception with an alternative access path and a public known-issue — never silently, because an undocumented failure is indistinguishable from negligence in an audit.

## 9. Code Examples

### Example 1 — Feature conformance matrix card

Tokens: `assets/css/wcag-fundamentals.css`

```html
<article class="matrix-card">
  <h2 class="matrix-title">Checkout flow — criteria map</h2>
  <ul class="matrix-list">
    <li><span class="crit">1.4.3 Contrast</span><span class="method" data-method="auto">Automated</span></li>
    <li><span class="crit">2.1.1 Keyboard</span><span class="method" data-method="manual">Manual</span></li>
    <li><span class="crit">3.3.1 Error ID</span><span class="method" data-method="sr">Screen reader</span></li>
  </ul>
  <p class="matrix-status" role="status">Target: <strong>WCAG 2.2 AA</strong> — Level A failures block release.</p>
</article>
<style>
  .matrix-card {
    border: 1px solid var(--a11y-review-gate-design, #ccc);
    border-left: 4px solid currentColor;
    border-radius: 8px;
    padding: 16px;
    max-width: 420px;
    font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .matrix-title { margin: 0 0 12px; font-size: 15px; }
  .matrix-list { list-style: none; margin: 0 0 12px; padding: 0; }
  .matrix-list li {
    display: flex; justify-content: space-between;
    padding: 6px 0; border-bottom: 1px solid #eee;
  }
  .method { font-size: 12px; opacity: 0.75; }
  .matrix-status { margin: 0; color: var(--a11y-level-aa-policy, #333); }
</style>
```

### Example 2 — CI gate wiring from policy tokens

Tokens: `assets/css/wcag-fundamentals.css`

```html
<form class="gate-panel">
  <fieldset>
    <legend>Release gate configuration</legend>
    <label><input type="checkbox" checked> axe-ci: zero critical violations required</label>
    <label><input type="checkbox" checked> Level A failures are blockers</label>
    <label><input type="checkbox" checked> a11y-code-review on ARIA/semantics PRs</label>
  </fieldset>
  <button type="submit">Save gates</button>
  <p class="gate-note" role="status">Pinned version: WCAG 2.2 — re-map criteria on major updates.</p>
</form>
<script>
  document.querySelector('.gate-panel').addEventListener('submit', (e) => {
    e.preventDefault();
    const css = getComputedStyle(document.documentElement);
    const target = css.getPropertyValue('--a11y-conformance-target').trim();
    const version = css.getPropertyValue('--a11y-criteria-version-pin').trim();
    console.assert(target === 'WCAG 2.2 AA', 'conformance target must stay pinned to 2.2 AA');
    console.assert(version === '2.2', 'version pin drives every criteria re-map');
  });
</script>
<style>
  .gate-panel {
    border: 1px solid #ddd; border-radius: 8px; padding: 16px;
    max-width: 420px; font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .gate-panel label { display: block; margin: 8px 0; }
  .gate-panel button {
    background: #171717; color: #fff; border: none; border-radius: 6px;
    padding: 8px 16px; cursor: pointer;
  }
  .gate-panel button:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; }
  .gate-note { color: #404040; font-size: 13px; }
</style>
```

## 10. Implementation Checklist

- [ ] The conformance claim is pinned via `var(--a11y-conformance-target)` to WCAG 2.2 AA and stated in one place.
- [ ] `var(--a11y-level-a-policy)` and `var(--a11y-level-aa-policy)` are wired as release blockers in the issue tracker, not just in docs.
- [ ] All three gates exist: design checklist (`--a11y-review-gate-design`), PR reviewer requirement (`--a11y-review-gate-code`), and CI axe run (`--a11y-review-gate-ci`).
- [ ] A criteria-to-feature matrix exists for every core flow, naming criteria and test methods before build.
- [ ] AAA upgrades are applied selectively per `var(--a11y-level-aaa-policy)` — 7:1 contrast on long-form reading surfaces at minimum.
- [ ] A public accessibility statement is published per `var(--a11y-statement-required)` with known limitations and a feedback channel.
- [ ] The WCAG version pin (`--a11y-criteria-version-pin`) triggers a criteria re-map task on any major WCAG update.
- [ ] Legal baselines (`--a11y-legal-baselines`) are cross-checked against the claim so one AA target covers EN 301 549, Section 508, and ADA.
