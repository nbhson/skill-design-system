---
name: governance-migration
description: The process layer — contribution rules, semantic versioning, deprecation windows, linting, and adoption tracking that keep a token system alive past its first hundred contributors.
tags: [governance, versioning, deprecation, linting, design-systems]
related: [token-pipeline-figma, component-tokens, semantic-alias-naming]
---

# Design Token Skill: Governance & Migration

## 1. Definition

Governance is how a token system survives contact with hundreds of contributors: it defines who may add tokens, how changes are reviewed and versioned, how renames migrate without breakage, and how adoption is measured in practice rather than claimed in slides. It is the skill that keeps the other eleven honest — lint rules that reject primitives in component code, deprecation windows that retire old aliases gracefully, and dashboards that show real token-tier usage instead of aspirations.

## 2. Core Token Principles

- **Tokens are an API:** every addition, rename, or removal goes through review, semver, and a changelog — no exceptions for "small" changes, because consumers cannot see the difference between small and large from outside.
- **Contribution is centralized but open:** anyone proposes; token stewards approve; proposals ship as PRs with evidence — use cases, contrast data, and the alias slot they fill.
- **Deprecation is a window, not a deletion:** deprecated tokens warn (lint + runtime dev-mode), get migrated, and are removed only after a published window (e.g. 2 releases).
- **Lint at the code boundary:** component code consuming primitives or raw hexes fails stylelint/eslint — the alias rule is *enforced*, not suggested in a wiki page.
- **Measure adoption, not intent:** a dashboard of primitive-vs-alias usage per codebase tells you the real migration state; installed-package counts tell you nothing.
- **Semantic versioning communicates impact:** new token = minor; rename or removal with deprecation = major; value-only fixes = patch.
- **One migration at a time:** overlapping deprecation windows collapse into review fatigue; sequence them through the same queue.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Governance | `--dt-governance-versioning` | `semver` | MAJOR.MINOR.PATCH per token release; consumers pin ranges |
| Governance | `--dt-governance-deprecation-window` | `2-releases` | Warn then remove; window published in changelog |
| Governance | `--dt-governance-coverage-target` | `90%` | Share of color/space/type usage flowing through alias+ tiers |
| Governance | `--dt-governance-lint-css` | `stylelint-declaration-strict-value` | Rejects raw hex/px where tokens are required |
| Governance | `--dt-governance-review-sla` | `5-days` | Token proposal review turnaround; keeps contributions flowing |
| Governance | `--dt-governance-changelog` | `keep-a-changelog` | Every token change is a changelog entry with migration notes |
| Governance | `--dt-governance-owners` | `design-dsg` | Named steward group in CODEOWNERS for token paths |
| Migration | `--dt-migration-stride` | `one-tier-per-release` | Big migrations sliced by tier; each release ships a working state |

Consume them by linking `assets/css/governance-migration.css` once at the app root; these values configure the process tooling (lint configs, CI jobs, dashboards) and are referenced as `var(--dt-governance-<role>)` so policy stays as diffable and reviewable as the tokens it governs. The deprecation window and review SLA should be quoted verbatim in contributor docs — policy that lives only in people's heads is policy that does not apply.

## 4. Composition & Layering

- **Governance sits above every other skill.** Naming conventions, contrast gates, and pipeline rules are all enforced through the same review + lint machinery — one enforcement point, many policies.
- **It composes with the pipeline:** deprecation warnings and semver bumps are pipeline events, and the changelog is generated from token diffs rather than written from memory.
- **It composes with component-tokens:** the slot list is versioned here — adding a component slot without review is the canonical governance violation, because slots are public API.

## 5. Signature Patterns

- **Deprecation machine:** deprecate (lint `warn` + docs strikethrough) → migrate (codemod + tracking issue) → remove (lint `error`, next major) — the same three-stage conveyor for every retirement, so nobody has to guess where a token is in its lifecycle.
- **Adoption dashboard:** CI counts token-tier usage per repo and publishes the trend over time; migration work deliberately targets the lowest-adoption surfaces first instead of preaching to the converted.

## 6. Real-World Use Cases

- **Design systems past the first 20 components,** where informal governance and hallway agreements stop scaling.
- **Renaming a token vocabulary** without breaking consuming products — deprecation window plus codemod, not a big-bang find-and-replace.
- **Proving system health:** adoption metrics that give stakeholders evidence for roadmap and staffing decisions.

## 7. Combination Notes

### With other token skills

- **Pairs with color-tokens, typography-tokens, spacing-sizing, and radius-elevation:** these primitive layers change most often (new steps, new families), and governance is what routes those changes through review and semver instead of letting ramps drift via drive-by commits.
- **Pairs with semantic-alias-naming:** the alias tier is governance's primary lint target — component code referencing primitives (`var(--dt-color-neutral-900)`) should be a build failure, and that rule is only real if this skill enforces it.
- **Pairs with token-pipeline-figma:** deprecation warnings, semver bumps, and changelog entries are pipeline events generated from token diffs, so "what changed" is never reconstructed from memory after the fact.
- **Pairs with component-tokens:** the slot list is a versioned API surface here; every new slot is a documented, reviewable promise with a deprecation path — the alternative is silent API churn.
- **Pairs with contrast-validation, dark-mode, and multi-brand-theming:** pairing manifests, theme cells, and brand overrides all ship through the same CI gates this skill operates, which is what makes "a pairing without a dark ratio is not done" enforceable rather than aspirational.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism and flat-design:** restrained styles keep the token vocabulary small and stable, which is the regime where governance overhead is lowest and lint rules stay legible.
- **Caution with maximalism and collage-art:** expressive styles multiply one-off values and variant counts; when a style legitimately needs more tokens, route the growth through proposals and versioning — the process bends, the vocabulary does not splinter.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing and reduced-motion:** duration/curve tokens and the reduced-motion fallback are versioned and lint-enforced like any other token layer, so a motion-token rename deprecates with a window instead of silently breaking every transition.

## 8. Anti-Patterns

- **Cowboy tokens:** additions dropped into a shared file with no review until the vocabulary is unrecognizable
- **Hard deletion:** removing a token in a patch release and letting consumer builds break as the notification system
- **Lint-less governance:** written conventions nobody enforces, honored only by the conscientious
- **Vanity adoption metrics:** counting installed packages instead of actual token-tier usage

### Accessibility Notes

Governance enforces the accessibility contract at scale: contrast pairing manifests, reduced-motion fallback presence, and a11y lint rules are CI gates, meaning a token change that degrades accessibility cannot merge regardless of who proposes it — seniority is not a bypass. The fallback rule is explicit about emergencies: when a fix must bypass the normal window (security, legal), it ships as a patch with a retroactive review within the 5-day SLA — governance bends the *process*, never the *thresholds*. Deprecations also carry a11y obligations: a deprecated alias must keep its validated pairing functioning (and its lint warning visible) for the full window, so migration pressure never becomes an accessibility regression.

## 9. Code Examples

### Example 1 — Stylelint enforcing the alias rule with a deprecation warning pattern

Tokens: `assets/css/governance-migration.css`

```html
<p class="card">Card text styled only through the alias tier.</p>
<style>
  /* .stylelintrc.json (sketch)
  {
    "plugins": ["stylelint-declaration-strict-value"],
    "rules": {
      "declaration-property-value-allowed-list": {
        "/^color$|^background$|^border/": ["/^var\\(--dt-/"]
      },
      "declaration-property-value-disallowed-list": {
        "/.*/": ["/#[0-9a-fA-F]{3,8}/", "/^var\\(--dt-color-neutral-[0-9]+\\)$/"]
      },
      "custom-property-pattern": "^--dt-(component|color|space|radius)-[a-z0-9-]+$"
    }
  }
  --dt-color-brand-700 is DEPRECATED (window: 2 releases) -> use --dt-color-action-primary-hover */
  :root { --dt-deprecated--dt-color-brand-700: true; } /* deprecation marker for dev-mode warn */
  .card {
    color: var(--dt-color-text-primary, #171717);   /* alias tier: passes lint */
    background: var(--dt-color-bg-subtle, #F5F5F5); /* alias tier: passes lint */
    padding: var(--dt-space-4, 16px);
    border-left: 3px solid var(--dt-color-action-primary, #2563EB);
    font: 14px/1.5 system-ui;
  }
  /* .legacy { color: #2563EB; }  <- FAILS: raw hex where a token is required */
  /* .legacy { color: var(--dt-color-neutral-900); } <- FAILS: primitive in product code */
</style>
<script>
  // Dev-mode runtime warning for tokens inside their deprecation window
  if (import.meta.env?.DEV) {
    const root = getComputedStyle(document.documentElement);
    for (const prop of root) {
      if (prop.startsWith('--dt-deprecated--')) {
        console.warn(`[tokens] ${prop.slice(16)} is deprecated; see CHANGELOG for migration.`);
      }
    }
  }
</script>
```

### Example 2 — Codemod for a token rename across a codebase

Tokens: `assets/css/governance-migration.css`

```html
<p class="note">Migration: --dt-color-brand-500 → --dt-color-action-primary (window: 2 releases).</p>
<style>
  .note {
    font: 13px/1.6 ui-monospace, Menlo, monospace;
    color: #171717; background: #F5F5F5;
    padding: 12px 16px; border-left: 3px solid #F59E0B;
  }
</style>
<script>
  // migrate.mjs — codemod sketch, run as: node migrate.mjs src/
  // Rename plan (generated from the token diff, ships in the changelog):
  const renames = [
    { from: '--dt-color-brand-500', to: '--dt-color-action-primary' },
    { from: '--dt-color-brand-600', to: '--dt-color-action-primary-hover' },
  ];

  async function migrate(files) {
    for (const file of files) {
      let src = await read(file);
      for (const { from, to } of renames) {
        src = src.replaceAll(from, to);
      }
      await write(file, src); // lint (now on `error` for the old names) verifies the sweep
    }
    // Post-conditions, checked in CI:
    // 1. grep finds zero occurrences of the deprecated names
    // 2. adoption dashboard re-counts alias-tier usage (target: 90%)
    // 3. changelog entry "Changed" section references this codemod
  }
  // Release discipline (semver): the rename lands as MAJOR after the 2-release
  // warn window; the window itself was announced in a MINOR that added the lint
  // `warn` + the runtime dev-mode warning above.
</script>
```

## 10. Implementation Checklist

- [ ] Token paths are owned by a steward group (`--dt-governance-owners`) in CODEOWNERS, and every addition/rename/removal lands as a reviewed PR — no cowboy tokens.
- [ ] Semver is mechanical: new token = minor, rename/removal = major, value-only fix = patch, with a keep-a-changelog entry per change.
- [ ] Every deprecation follows the 2-release window: lint `warn` + docs strikethrough → codemod + tracking issue → lint `error` on removal.
- [ ] Stylelint (or equivalent) rejects raw hexes and primitive references in product code — the alias rule is a build failure, not documentation.
- [ ] A deprecated token emits a dev-mode runtime warning so consumers still on the old name see it in their console.
- [ ] The adoption dashboard counts real token-tier usage against the 90% coverage target and drives which surfaces get migration work first.
- [ ] Only one migration is open per token family at a time; new deprecations queue behind the current window.
- [ ] CI gates for contrast pairings and reduced-motion fallbacks are wired through this same machinery — an a11y-degrading token change cannot merge.
