---
name: token-pipeline-figma
description: Design-tool-to-code automation — Figma variables as the source, W3C DTCG as the interchange format, and CI as the referee that catches drift at PR time.
tags: [tokens, figma, pipeline, codegen, design-systems]
related: [platform-mapping, contrast-validation, governance-migration]
---

# Design Token Skill: Token Pipeline & Figma Sync

## 1. Definition

The token pipeline is the automated path from design tools (Figma variables and modes) to code (CSS, iOS, Android): design exports in W3C DTCG JSON, a transform step validates and renders platform outputs, and CI gates every change behind review. Its real product is not the generated files — it is **trust**. Designers and engineers edit the same declared source of truth, so any drift between Figma and code surfaces as a failing check in a pull request rather than as a mismatch discovered in production screenshots months later. Without this layer, every other token skill degrades into manually-synced spreadsheets of hexes that quietly disagree.

## 2. Core Token Principles

- **One source of truth, declared:** Figma variables (design-edited) or the JSON repo (code-edited) — pick one, document it, and forbid the other from drifting. "Both, depending on the change" is the failure mode.
- **W3C DTCG as the interchange format:** `$value`/`$type` JSON is the neutral ground both Figma (via Tokens Studio) and codegen (Style Dictionary and friends) understand.
- **Naming survives the round trip:** Figma variable names (`color/action/primary`) map mechanically to token ids (`color-action-primary`) — there is no manual translation step where typos can breed.
- **Modes map to themes:** Figma modes (Light/Dark, per-brand collections) are the design-side twin of `data-theme`/`data-brand` — one axis, expressed identically on both sides.
- **Validation lives in the pipeline:** naming conventions, contrast pairings, and symmetry checks run *before* codegen, not as a QA pass after the fact.
- **Sync is PR-gated:** changes land as reviewable diffs with semantic version bumps — never as silent midnight syncs that bypass review.
- **Generated files are never hand-edited:** a header comment plus a CI diff makes any manual edit fail loudly instead of being overwritten or forked.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Pipeline | `--dt-pipeline-source-of-truth` | `figma-variables` | Declared owner; the JSON repo is the mirrored build artifact |
| Pipeline | `--dt-pipeline-format` | `w3c-dtcg` | $value/$type interchange; readable by Style Dictionary and Tokens Studio |
| Pipeline | `--dt-pipeline-naming-pattern` | `{category}.{group}.{role}` | color.action.primary -> --dt-color-action-primary |
| Pipeline | `--dt-pipeline-modes` | `light,dark,brand-a,brand-b` | Figma modes = theme axes; 1:1 with data-theme/data-brand |
| Pipeline | `--dt-pipeline-export-targets` | `css,ios,android,docs` | Renderers; css is the reference output |
| Pipeline | `--dt-pipeline-sync-trigger` | `pull-request` | Human-reviewed diffs; no auto-commit to main |
| Pipeline | `--dt-pipeline-validation-gate` | `pre-codegen` | Naming + contrast + symmetry checks before render |
| Pipeline | `--dt-pipeline-versioning` | `semver` | Token releases tagged; consumers pin and migrate (governance) |

Consume them by linking `assets/css/token-pipeline-figma.css` once at the app root, then referencing `var(--dt-pipeline-<role>)` — these values are configuration data for the pipeline itself (build scripts, sync bots, and docs), so they live as custom properties to stay greppable and diffable. Every generated CSS file must carry the "do not edit" header and the token release version it was rendered from.

## 4. Composition & Layering

- **The pipeline composes with platform-mapping.** This skill moves the data; mapping defines each renderer's contract — prefixes (`--dt-`), units (rem/pt/dp), and font-scaling behavior — so renderers stay interchangeable.
- **It composes with contrast-validation.** Pairing manifests are generated and diffed as part of the same PR, meaning design and code change their a11y posture together and a new failing mode cannot merge silently.
- **It composes with governance-migration.** Deprecations, renames, and version bumps are pipeline events with changelog entries — not chat messages or wiki edits that nobody connects to a token release.

## 5. Signature Patterns

- **Figma variables + Tokens Studio export:** designers manage collections and modes in Figma; a PR bot turns the DTCG export into validated platform outputs, so designers work where they already work and code never receives a hand-typed value.
- **Bidirectional diff report:** every sync emits "what changed in design" vs "what changed in code" side by side, letting reviewers see theme-affecting changes at a glance instead of spelunking raw JSON.

## 6. Real-World Use Cases

- **Design systems with a dedicated design team** actively maintaining Figma variables as the living source.
- **Multi-brand products:** per-brand Figma collections flowing through one pipeline into one set of renderers.
- **Auditing a manual handoff:** locating the copy-paste steps where design and code drift today, and closing each one with automation.

## 7. Combination Notes

### With other token skills

- **Pairs with color-tokens, typography-tokens, spacing-sizing, and radius-elevation:** these primitive layers are exactly what the pipeline exports; defining them as DTCG JSON with mechanical name mapping is what makes their Figma-to-code round trip lossless.
- **Pairs with semantic-alias-naming and dark-mode:** Figma modes are the design twin of `data-theme`/`data-brand` — the pipeline validates that mode collections and alias tiers agree before either side renders, so theming never forks into "design dark" and "code dark."
- **Pairs with contrast-validation:** the pairing manifest is generated in-pipeline, so a designer adding a brand mode gets failing ratios at PR time — the gate is the contract, not the code review.
- **Pairs with platform-mapping and governance-migration:** mapping defines the renderer contracts this skill feeds, and governance turns deprecations and semver bumps into pipeline events with changelogs instead of tribal-knowledge renames.
- **Caution with component-tokens:** component slots are usually code-authored; keep them out of the Figma-synced source (or in a read-only downstream collection) so designers and code are not both editing the same tier with different tools.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism and flat-design:** restrained styles have small, stable token sets — the sweet spot where a pipeline's overhead pays for itself within one or two syncs.
- **Caution with collage-art and skeuomorphism:** both trend toward bespoke, per-surface values that resist tokenization; if a style needs many one-off textures, model them as deliberate primitive groups through the pipeline, never as values pasted straight into components.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** durations and curves are tokens too — exporting `--motion-duration-*`/`--motion-ease-*` through the same DTCG source means designers tune timing in Figma and the change arrives as a reviewable, versioned diff.

## 8. Anti-Patterns

- **Screenshot-driven sync:** designers re-creating tokens in code from pictures of Figma
- **Two sources of truth:** Figma and code both edited, reconciled by whoever notices first
- **Silent sync bots:** auto-commits to main that bypass review and semver
- **Format drift:** bespoke JSON shapes per tool version that break codegen on upgrade

### Accessibility Notes

The pipeline is what makes accessibility **continuous** instead of periodic: because contrast pairings are validated pre-codegen (the `--dt-pipeline-validation-gate` value), a designer's new mode or brand collection cannot merge with failing ratios — the gate is the contract, not the code review. When the design tool cannot express a validation itself (for example, per-state deltas like hover shifts), the pipeline computes it from the exported values and blocks the PR with the exact failing pairing listed, so nothing waits for a QA pass to discover it. This is the mechanism behind dark-mode's promise that "a pairing without a dark ratio is not done": the diffed pairing manifest turns that slogan into a red build.

## 9. Code Examples

### Example 1 — DTCG source, generated CSS, and a Style Dictionary-style transform

Tokens: `assets/css/token-pipeline-figma.css`

```html
<!-- ===== tokens.colors.dtcg.json — exported from Figma (Tokens Studio) =====
{
  "color": {
    "action": {
      "primary": { "$type": "color", "$value": "#2563EB" },
      "primary-hover": { "$type": "color", "$value": "#1D4ED8" }
    },
    "bg": {
      "default": { "$type": "color", "$value": "#FFFFFF" }
    }
  }
}
===== generated by pipeline — DO NOT EDIT (tokens@1.4.0) ===== -->
<button class="btn">Deploy</button>
<style>
  /* Rendered output: {category}.{group}.{role} -> --dt-<category>-<group>-<role> */
  :root {
    --dt-color-action-primary: #2563EB;       /* from color.action.primary */
    --dt-color-action-primary-hover: #1D4ED8; /* from color.action.primary-hover */
    --dt-color-bg-default: #FFFFFF;           /* from color.bg.default */
  }
  .btn {
    background: var(--dt-color-action-primary);
    color: #fff; /* pairing validated pre-codegen by the contrast gate */
    border: none; border-radius: 8px; padding: 10px 20px;
    font: 600 14px/1 system-ui; cursor: pointer;
  }
  .btn:hover { background: var(--dt-color-action-primary-hover); }
</style>
<script>
  // Mini Style Dictionary-style transform sketch (build step, simplified)
  const dtcg = {
    color: { action: { primary: { $type: 'color', $value: '#2563EB' } } }
  };
  const flatten = (obj, path = []) =>
    Object.entries(obj).flatMap(([k, v]) =>
      '$value' in v ? [{ id: [...path, k].join('-'), ...v }] : flatten(v, [...path, k]));
  const cssVar = (t) =>
    `--dt-${t.id.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase()}: ${t.$value};`;
  console.log(flatten(dtcg).map(cssVar).join('\n'));
  // -> --dt-color-action-primary: #2563EB;
</script>
```

### Example 2 — PR-gated sync script with a pre-codegen validation gate

Tokens: `assets/css/token-pipeline-figma.css`

```html
<p class="sync-status">Token sync runs on <code>pull_request</code> only — never auto-commit.</p>
<style>
  .sync-status {
    font: 13px/1.5 ui-monospace, Menlo, monospace;
    color: #404040; background: #F5F5F5;
    padding: 12px 16px; border-left: 3px solid #2563EB;
  }
  .sync-status code { background: #D4D4D4; padding: 1px 4px; border-radius: 4px; }
</style>
<script>
  // sync.mjs — invoked by CI on a pull request branch (sketch)
  async function sync(figmaExport) {
    // Gate 1: naming — every id must match {category}.{group}.{role}
    const bad = figmaExport.filter(t => !/^[a-z-]+\.[a-z-]+\.[a-z-]+$/.test(t.name));
    if (bad.length) throw new Error(`Naming gate failed: ${bad.map(t => t.name).join(', ')}`);

    // Gate 2: contrast — pairings from the manifest, pre-codegen
    const pairings = [{ fg: '#FFFFFF', bg: '#2563EB', min: 4.5 }];
    for (const p of pairings) {
      const ratio = contrastRatio(p.fg, p.bg); // WCAG relative luminance (not shown)
      if (ratio < p.min) throw new Error(`Contrast gate failed: ${p.fg} on ${p.bg} = ${ratio}`);
    }

    // Gate 3: render + diff — hand-edited generated files make this fail
    await render(['css', 'ios', 'android', 'docs']);
    const drift = await gitDiff('assets/css/**.css');
    if (drift.includesHandEdits()) throw new Error('Generated file was hand-edited');

    await commitAndRequestReview(); // semver bump + changelog entry (governance-migration)
  }
</script>
```

## 10. Implementation Checklist

- [ ] The source of truth (`--dt-pipeline-source-of-truth`) is declared in the README and exactly one side edits it — no parallel hand-maintained token files.
- [ ] All token JSON is W3C DTCG (`$value`/`$type`) and codegen runs against it — no bespoke formats per tool version.
- [ ] Figma variable names map mechanically to `--dt-*` ids via `--dt-pipeline-naming-pattern`; zero manual rename steps exist in the flow.
- [ ] Every Figma mode (light/dark/brand) has a 1:1 theme counterpart, and mode additions flow through the same sync.
- [ ] Naming, contrast, and symmetry gates run pre-codegen and fail the PR with the specific offending token or pairing listed.
- [ ] Sync lands only via pull request (`--dt-pipeline-sync-trigger`) with a semver bump and changelog entry — no auto-commits to main.
- [ ] Every generated file carries a "DO NOT EDIT" header plus its token release version, and a CI diff rejects hand-edits.
- [ ] Each sync emits the bidirectional diff report so reviewers see theme-affecting changes without reading raw JSON.
