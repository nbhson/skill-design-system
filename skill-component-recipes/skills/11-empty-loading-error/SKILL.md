---
name: empty-loading-error
description: The states most components forget — skeletons that match layout, empty states that teach, error states that recover.
tags: [empty-states, loading, skeletons, error-handling, states]
related: [toasts-notifications, tables-data-grid, accessibility-wiring]
---

# Component Recipe: Empty, Loading & Error States

## 1. Definition

Every component has more states than its happy path: loading (first load, refetch, inline), empty (first-use, no-results, cleared), and error (network, permission, not-found). Products fail here most visibly — a blank box communicates nothing while a designed empty state onboards. The recipe covers skeleton discipline, empty-state taxonomy with next actions, and error-state recovery paths, and treats the triad as part of the component spec itself: a component without its loading, empty, and error states is an incomplete spec, not a finished component.

## 2. Core Principles

- **Skeletons match the final layout:** the skeleton is the component's own geometry — a generic gray blob that swaps into a different shape causes a jarring shift.
- **Never skeleton past 3 seconds:** long loads switch to progress indication (bar, percentage) — skeletons are for sub-3s waits.
- **Empty states are taxonomy-driven:** first-use (teach + CTA), no-results (relax-the-query suggestion), cleared (restore action) — each has its own copy and action.
- **Empty states carry the next action:** "Create your first project" with the button — an empty state without an action is a dead end.
- **Errors are specific and recoverable:** what failed, why (in user terms), and the recovery action (retry, contact, alternative path).
- **Offline is a designed state:** detect and message degraded connectivity with the retry contract — not a browser error.
- **Permission errors explain the unlock:** "Ask your admin for access" with the request action — not a bare 403.
- **All states are announced:** loading/empty/error narrate via live regions or focus moves — state changes AT users can hear.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Skeleton policy | `--comp-skeleton-policy` | `matches-final-layout` | Component-own geometry; no generic blobs |
| Skeleton duration cap | `--comp-skeleton-duration-cap` | `3s` | Longer waits switch to progress |
| Empty taxonomy | `--comp-empty-taxonomy` | `first-use,no-results,cleared` | Each with own copy + action |
| Empty CTA | `--comp-empty-cta` | `required` | Empty states carry the next action |
| Error format | `--comp-error-format` | `what+why+recovery` | The three-part error message |
| Error recovery | `--comp-error-recovery-action` | `retry-or-alternative` | Every error has a path forward |
| Offline state | `--comp-offline-state` | `designed+retry` | Connectivity degradation handled |
| Permission error | `--comp-permission-error` | `explain-unlock` | 403s request access, not just refuse |
| State announce | `--comp-state-announce` | `live-region-or-focus` | State changes narrated |
| State coverage | `--comp-state-coverage` | `component-spec-includes-states` | Recipes ship with all states designed |

Consume them by linking `assets/css/empty-loading-error.css` and referencing `var(--comp-...)` — as with most recipes in this repo, several tokens are behavioral policies enforced in component code and review (taxonomy, error format, announcement), while the skeleton surface itself resolves to CSS. The `--comp-state-coverage` token is the contract that pulls this recipe into every component spec: states are designed with the component, never bolted on after.

## 4. Composition

- **Composes with every recipe in this repo:** each component's spec includes its loading/empty/error states — states are part of the recipe, and this guide supplies the shared discipline for all of them.
- **Composes with toasts-notifications:** async failures land as persistent toasts with retry; inline errors stay in-component — the boundary is whether the user needs the failure in context or globally.
- **Composes with ux-writing (skill-ux-writing):** empty and error copy follows the voice/tone and error-message guides — this recipe owns the structure (taxonomy, what+why+recovery), ux-writing owns the words.

## 5. Signature Patterns

- **State triad per component:** every recipe ships (loading, empty, error) alongside default — a component without its triad is an incomplete spec, and the triad is reviewed at design time.
- **Error taxonomy:** network/permission/not-found/validation each get their approved copy pattern — engineers pick from the taxonomy, not from scratch, so error quality stops depending on who wrote the handler.

## 6. Real-World Use Cases

- **First-run experiences:** empty states are the onboarding surface — teach the feature and hand over the first action.
- **Async-heavy dashboards:** loading and error choreography across tables, cards, and charts.
- **Audit:** blank boxes, skeleton-to-content layout jumps, bare 403s, "Something went wrong" dead ends.

## 7. Combination Notes

### With other component-recipe skills

- **Pairs naturally with toasts-notifications, tables-data-grid, cards-lists, and forms-inputs:** tables and cards consume skeleton rows and empty states; async failures route to persistent toasts with retry; forms use the error summary contract — the triad is expressed inside these recipes.
- **Pairs with buttons-badges and dropdowns-menus:** every empty-state CTA is a button-contract control, and filtered menus/listboxes use the no-results empty pattern.
- **Pairs with command-palette, tabs-accordions, modals-dialogs, navigation-patterns, and accessibility-wiring:** palettes need teaching empty states, tab panels announce lazy loading, dialogs keep skeleton geometry stable, and every state transition passes the wiring checklist. The caution/avoid lists are empty — every recipe needs its states.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and collage-art:** empty states are the one place personality pays — a flat, restrained layout with a single accent illustration teaches without noise, and minimalism keeps the CTA unmissable.
- **Caution is empty, with one boundary:** illustrations live in empty and error states only — never in skeletons, which must stay neutral geometry that predicts the real layout.

### With motion skills (companion repo skill-animation)

- **Good affinity with loading-states and easing-timing:** skeleton shimmer, spinner-to-progress handoffs, and content fade-in on resolve all use duration tokens; easing keeps the skeleton→content swap feeling like reveal, not replacement.
- **Caution is empty, with one hard rule:** state-change motion collapses under `prefers-reduced-motion` (shimmer becomes static opacity), and content must not shift layout when it replaces the skeleton.

## 8. Anti-Patterns

- **Blank-box states** — unstyled empty/loading/error surfaces shipping to production
- **Skeleton-forever** — spinners-as-skeletons hanging past 3s with no progress
- **Dead-end errors** — 'Something went wrong' with no cause and no path
- **Layout-jump loads** — skeleton geometry that doesn't match the content it becomes

### Accessibility Notes

State changes are WCAG 4.1.3 surface: loading/empty/error transitions announce politely, error focus moves to summaries (the forms contract), and empty-state CTAs are keyboard-reachable — states designed without AT are half-designed. Announce deliberately: a `role="status"` live region narrates "Loading projects…" and then "5 projects loaded" or the empty/error headline; skeleton regions are `aria-hidden` with an `aria-busy="true"` container so screen readers hear the state, not the shimmer. The fallback rule: if a live-region announcement cannot be wired for a state, move focus to the state's heading instead — focus movement is the fallback narration channel.

## 9. Code Examples

### Example 1 — Skeleton that matches final layout (and announces itself)

Tokens: `assets/css/empty-loading-error.css`

```html
<div class="panel" id="panel" aria-busy="true">
  <p class="sr" id="panelStatus" role="status" aria-live="polite">Loading projects…</p>
  <table class="tbl" aria-hidden="true">
    <thead><tr><th class="sk sk-h w40"></th><th class="sk sk-h w20"></th><th class="sk sk-h w20"></th><th class="sk sk-h w20"></th></tr></thead>
    <tbody>
      <tr><td class="sk"></td><td class="sk"></td><td class="sk"></td><td class="sk right"></td></tr>
      <tr><td class="sk"></td><td class="sk"></td><td class="sk"></td><td class="sk right"></td></tr>
    </tbody>
  </table>
  <table class="tbl real" id="real" hidden>
    <thead><tr><th>Project</th><th>Owner</th><th>Status</th><th class="right">Spend</th></tr></thead>
    <tbody>
      <tr><td>Acme rollout</td><td>S. Nguyen</td><td>Active</td><td class="right">$12,400</td></tr>
      <tr><td>Globex pilot</td><td>R. Ito</td><td>Planning</td><td class="right">$3,100</td></tr>
      <tr><td>Initech audit</td><td>M. Diaz</td><td>Blocked</td><td class="right">$8,750</td></tr>
    </tbody>
  </table>
</div>
<style>
  .panel { font: 14px/1.5 system-ui, sans-serif; max-width: 560px; border: 1px solid var(--comp-border, #e5e5e5); border-radius: 12px; padding: 16px; }
  .tbl { width: 100%; border-collapse: collapse; }
  .tbl th { text-align: left; font-size: 12px; color: var(--comp-muted, #737373); padding: 8px 12px; border-bottom: 1px solid var(--comp-border, #e5e5e5); }
  .tbl td { padding: 14px 12px; border-bottom: 1px solid var(--comp-border, #f0f0f0); }
  .right { text-align: right; font-variant-numeric: tabular-nums; }
  /* Skeleton geometry = the component's own geometry: same table, same columns */
  .sk { height: 14px; border-radius: 6px; background: var(--comp-skeleton, #ececec); animation: pulse 1.2s ease-in-out infinite; }
  .sk-h { height: 10px; }
  .w40 { width: 40%; } .w20 { width: 20%; }
  @keyframes pulse { 50% { opacity: 0.55; } }
  @media (prefers-reduced-motion: reduce) { .sk { animation: none; } }
  .sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
</style>
<script>
  // Skeleton cap: past 3s switch to progress indication; here we resolve and swap
  setTimeout(() => {
    document.querySelector('.tbl:not(.real)').remove();
    document.getElementById('real').hidden = false;
    const p = document.getElementById('panel');
    p.setAttribute('aria-busy', 'false');
    document.getElementById('panelStatus').textContent = '3 projects loaded';
  }, 1200); // skeleton cap: real waits past 3s switch to progress indication
</script>
```

### Example 2 — Empty-state taxonomy cards + the error triad

```html
<div class="states">
  <section class="state-card">
    <h3>No projects yet</h3>
    <p>Projects group your work and let you invite your team. Create your first one to get started.</p>
    <button class="btn">Create your first project</button>
  </section>
  <section class="state-card">
    <h3>No results for "acme acount"</h3>
    <p>Nothing matches that spelling. Try a shorter search or check the account ID.</p>
    <button class="btn ghost">Clear search</button>
  </section>
  <section class="state-card">
    <h3>All notifications cleared</h3>
    <p>Everything you cleared in the last 30 days is still recoverable.</p>
    <button class="btn ghost">Restore cleared items</button>
  </section>
  <section class="state-card error">
    <h3>Couldn't load projects</h3>
    <p><strong>What:</strong> the request timed out. <strong>Why:</strong> a partial outage in your region. <strong>Recovery:</strong> retry now — your data is safe.</p>
    <button class="btn" id="retry">Retry</button> <a style="margin-left:12px; color: var(--comp-cta, #2563eb)" href="/status">Check status page</a>
  </section>
</div>
<p class="sr" id="stateLive" role="status" aria-live="polite"></p>
<style>
  .states { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; font: 14px/1.5 system-ui, sans-serif; max-width: 860px; }
  .state-card { border: 1px solid var(--comp-border, #e5e5e5); border-radius: 12px; padding: 20px; }
  .state-card.error { border-color: var(--comp-error-border, #fecaca); background: var(--comp-error-bg, #fef2f2); }
  .state-card h3 { margin: 0 0 8px; font-size: 15px; color: var(--comp-ink, #171717); }
  .state-card p { margin: 0 0 16px; color: var(--comp-muted, #525252); }
  .btn { font: 600 14px system-ui, sans-serif; padding: 10px 16px; border: none; border-radius: 8px; background: var(--comp-cta, #2563eb); color: #fff; cursor: pointer; }
  .btn.ghost { background: transparent; color: var(--comp-cta, #2563eb); border: 1px solid var(--comp-cta, #2563eb); }
</style>
<script>
  // Retry runs the recovery action; result narrates via the polite live region
  document.getElementById('retry').addEventListener('click', () =>
    document.getElementById('stateLive').textContent = 'Retrying… projects loaded successfully.');
</script>
```

## 10. Implementation Checklist

- [ ] Every component spec ships its state triad — loading, empty, error — alongside the default state (`--comp-state-coverage`).
- [ ] Skeletons mirror the final layout's geometry; no generic blobs or spinner substitutes (`--comp-skeleton-policy`).
- [ ] Waits past 3 seconds switch from skeleton to progress indication (`--comp-skeleton-duration-cap`).
- [ ] Empty states pick from the taxonomy — first-use, no-results, cleared — each with its own copy and CTA (`--comp-empty-taxonomy`, `--comp-empty-cta`).
- [ ] Every error message states what failed, why in user terms, and the recovery path (`--comp-error-format`, `--comp-error-recovery-action`).
- [ ] Offline and permission failures have designed copy — retry contract and explain-the-unlock (`--comp-offline-state`, `--comp-permission-error`).
- [ ] Loading/empty/error transitions announce via live region or focus move (`--comp-state-announce`).
