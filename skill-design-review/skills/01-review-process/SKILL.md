---
name: review-process
description: The design review operating system: critique formats, severity scales, roles, cadence, and decisions that stick.
tags: [review, process, critique, severity, decisions]
related: [visual-hierarchy-audit, consistency-audit, a11y-audit]
---

# Design Review Guide: Review Process

## 1. Definition

Design review fails without process: feedback becomes taste debates, findings die in screenshots, and the same issues return every sprint. This guide is the operating system for all audit guides in this repo: the critique formats (design critique vs QA pass vs release gate), the severity scale (blocker/major/minor/polish), the role separation (presenter, facilitator, scribe), the cadence (per-milestone critiques, per-release gates), and the decision record — reviews produce decisions with owners, or they produce nothing.

## 2. Core Principles

- **Format matches purpose:** critique (early, divergent) vs QA pass (pre-release, convergent) vs release gate (binary go/no-go) — mixing formats breaks all three.
- **Critique the work against criteria, not taste:** every finding cites a standard (a token, a guide, a WCAG criterion) — 'I don't like it' is not feedback.
- **Severity is a shared scale:** blocker (ships broken), major (fix before release), minor (fix in cadence), polish (backlog) — shared severity enables shared prioritization.
- **Roles are separated:** presenter shows, facilitator runs the room, scribe records — un facilitated reviews drift into tangents.
- **Findings leave the room as tickets:** every finding gets owner + severity + due state — screenshots without tickets are decoration.
- **Cadence is scheduled:** per-milestone critiques and per-release gates on the calendar — review-on-request catches nothing.
- **Decisions are recorded:** what was decided, by whom, why — the decision record ends relitigation.
- **The review closes the loop:** prior findings verified fixed at the next gate — the loop is what makes review a system.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Review Formats | `--rev-review-formats` | `critique,qa-pass,release-gate` | Three formats, three purposes |
| Severity Scale | `--rev-severity-scale` | `blocker,major,minor,polish` | Shared prioritization vocabulary |
| Criteria Rule | `--rev-criteria-rule` | `findings-cite-standards` | No taste-only feedback |
| Role Separation | `--rev-role-separation` | `presenter,facilitator,scribe` | Structured rooms |
| Cadence | `--rev-cadence` | `milestone+release-gates` | Scheduled, not on-request |
| Findings To Tickets | `--rev-findings-to-tickets` | `owner+severity+state` | Mandatory follow-through |
| Decision Record | `--rev-decision-record` | `what+who+why` | Ends relitigation |
| Loop Closure | `--rev-loop-closure` | `verify-prior-findings` | Next gate re-checks |
| Timebox | `--rev-timebox` | `45-60min` | Longer reviews degrade |
| Scope Rule | `--rev-scope-rule` | `one-surface-per-session` | Depth over breadth |

Consume them by linking `assets/css/review-process.css` once at the review tooling root, then referencing `var(--rev-<role>)` wherever review collateral is rendered — packets, scorecards, and decision records read the same constants. The tokens are process contracts, not decoration: the severity scale token is the vocabulary the scribe writes in, and the timebox token is what the facilitator schedules against.

## 4. Composition

- **Composes with every audit guide in this repo:** the process defines how their checklists run; they define what it checks.
- **Composes with skill-design-tokens + skill-component-recipes:** token and component contracts are the criteria findings cite.
- **Composes with skill-accessibility:** the release gate includes the a11y criteria as blocking checks.

## 5. Signature Patterns

- **The review packet:** surface + context + specific questions sent 24h ahead — reviews start prepared or don't start. The packet names the format (critique vs gate), lists the open questions as citable criteria, and gives attendees time to form findings before the room opens, which converts gut reactions into standard-cited feedback.
- **The gate checklist:** the release gate runs every audit guide's scorecard in order with a blocker check — one artifact, binary outcome. Each audit guide contributes its scored section; the gate simply asks "any blockers?" per section, making the go/no-go mechanical instead of negotiable.

## 6. Real-World Use Cases

- **Teams establishing their first structured design review:** installing the formats, severity scale, and cadence before bad habits (screenshot culture, taste debates) calcify.
- **Scaling reviews from one designer to a design org:** role separation and decision records are what let reviews survive more participants without degrading into tangents.
- **Audit: taste debates, unactioned findings, review fatigue:** the classic symptoms of missing process — audit against the principles above to locate which piece is absent.

## 7. Combination Notes

### With other design-review skills

- **Good with visual-hierarchy-audit and consistency-audit:** these are the highest-frequency audit guides, and they run as formats inside this process — the critique opens a surface, these audits provide the checklist, and their findings enter the severity scale. The process without audits is empty ritual; the audits without the process are checklist theater.
- **Good with a11y-audit and motion-audit:** audit guides whose findings carry binary consequences (blockers) — the release gate is the mechanism that enforces them.
- **Good with typography-audit, spacing-rhythm-audit, interaction-states-audit, content-microcopy-audit, perceived-performance, and responsive-audit:** each contributes a scored section to the gate checklist; running them under one cadence prevents audit sprawl.
- **Good with report-template:** the report is the decision record's output format — findings, owners, severity, and status flow from the room into the template.
- **No caution or avoid list:** as the operating system, this skill is compatible with every sibling — the failure mode to prevent is running any audit outside the process (findings without owners, decisions without records).

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism:** minimalist surfaces have few elements, so review findings concentrate on the criteria that matter (hierarchy, spacing, type) — the process's criteria-cited rule pairs naturally with a style whose judgments are token-checkable.
- **Good affinity with class-morphism and flat-design:** both styles lean on systematic token application, which makes findings mechanically citable and the severity scale unambiguous — reviews run faster when the standard is written down.
- **No caution list:** process is style-agnostic; the review formats apply equally to maximalist or brutalist work — only the criteria being cited change.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** motion tokens are exactly the kind of standard findings must cite — a review saying "the transition is wrong" becomes actionable when it points at a duration-ladder value from easing-timing.
- **No caution list:** the process neither generates nor consumes motion directly; it only verifies motion against skill-animation's contracts at QA passes and release gates.

## 8. Anti-Patterns

- **Taste debates:** 'I don't like it' without a cited standard
- **Screenshot graveyards:** findings captured but never ticketed
- **Review-on-request:** ad-hoc reviews that catch nothing systemic
- **Relitigated decisions:** the same debate every sprint, no record

### Accessibility Notes

The review process itself is the a11y enforcement mechanism: WCAG criteria enter as blocking checks at the release gate (a11y-audit guide) — a review process without a11y as a gate produces retrofitted accessibility. This is the structural reason a11y belongs in the process definition rather than as a courtesy mention: a gate that asks "any blockers?" and includes the a11y-audit scorecard turns conformance from an aspiration into a binary condition of shipping. The fallback rule keeps adoption realistic: if the full process is too heavy, start with the release gate + severity scale alone — the binary gate carries most of the value, and critique formats can be layered in once the gate habit exists.

## 9. Code Examples

### Example 1 — Review packet page (surface context + specific questions + severity legend)

Tokens: `assets/css/review-process.css`

```html
<article class="packet">
  <header class="packet-head">
    <h1>Review Packet — Checkout v2, Step 3</h1>
    <p class="packet-meta">Format: <span data-rev="qa-pass">QA pass</span> · Timebox: <span data-rev="timebox">45-60min</span> · Scope: <span data-rev="scope">one surface</span></p>
  </header>
  <section class="packet-context">
    <h2>Context</h2>
    <p>Payment step rebuilt on the new form recipe. Prior findings F-104 (focus order) and F-107 (error copy) verified fixed at last gate per <code>var(--rev-loop-closure)</code>.</p>
  </section>
  <section class="packet-questions">
    <h2>Specific questions</h2>
    <ol>
      <li>Does every error carry what+why+fix?</li>
      <li>Is the primary action dominant, or competing with the promo banner?</li>
      <li>Any raw values escaping <code>var(--rev-*)</code> tokens?</li>
    </ol>
  </section>
  <section class="packet-legend" aria-label="Severity scale legend">
    <h2>Severity legend — <code>var(--rev-severity-scale)</code></h2>
    <ul>
      <li class="sev sev-blocker"><strong>Blocker</strong> — ships broken</li>
      <li class="sev sev-major"><strong>Major</strong> — fix before release</li>
      <li class="sev sev-minor"><strong>Minor</strong> — fix in cadence</li>
      <li class="sev sev-polish"><strong>Polish</strong> — backlog</li>
    </ul>
  </section>
</article>
<style>
  .packet { max-width: 560px; font: 14px/1.5 Inter, system-ui, sans-serif; padding: 24px; border: 1px solid #D4D4D4; border-radius: 8px; }
  .packet h1 { font-size: 18px; margin: 0 0 4px; }
  .packet h2 { font-size: 14px; margin: 16px 0 6px; }
  .packet-legend ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 4px; }
  .sev { padding: 6px 10px; border-radius: 6px; }
  .sev-blocker { background: var(--rev-severity-blocker, #EF4444); color: #fff; }
  .sev-major   { background: var(--rev-severity-major, #F59E0B); color: #171717; }
  .sev-minor   { background: var(--rev-severity-minor, #2563EB); color: #fff; }
  .sev-polish  { background: var(--rev-severity-polish, #F5F5F5); color: #404040; }
</style>
```

### Example 2 — Decision-record demo (findings → tickets with owner/severity/status)

```html
<section class="record">
  <h1>Decision Record — Gate 2026-11-02</h1>
  <p class="record-note">Recorded per <code>var(--rev-decision-record)</code>: what + who + why.</p>
  <table class="tickets">
    <thead>
      <tr><th scope="col">Finding</th><th scope="col">Decision</th><th scope="col">Owner</th><th scope="col">Severity</th><th scope="col">Status</th></tr>
    </thead>
    <tbody>
      <tr><td>Double primary buttons on payment step</td><td>Merge into single CTA; promo demoted to link</td><td>@mira</td><td><span class="pill pill-blocker">blocker</span></td><td>open</td></tr>
      <tr><td>Cancel link 3px off column line</td><td>Fix in cadence — spacing token sweep</td><td>@jules</td><td><span class="pill pill-minor">minor</span></td><td>ticketed</td></tr>
      <tr><td>Focus ring missing on promo link</td><td>Blocker — gate cannot pass until fixed</td><td>@sana</td><td><span class="pill pill-blocker">blocker</span></td><td>in-progress</td></tr>
    </tbody>
  </table>
  <p class="record-why"><strong>Why recorded:</strong> every row has owner + severity + state (<code>var(--rev-findings-to-tickets)</code>); blockers re-verified at the next gate (<code>var(--rev-loop-closure)</code>).</p>
</section>
<style>
  .record { max-width: 640px; font: 14px/1.5 Inter, system-ui, sans-serif; padding: 24px; border: 1px solid #D4D4D4; border-radius: 8px; }
  .record h1 { font-size: 18px; margin: 0 0 4px; }
  .tickets { width: 100%; border-collapse: collapse; margin: 12px 0; }
  .tickets th, .tickets td { text-align: left; padding: 8px; border-bottom: 1px solid #D4D4D4; }
  .tickets th { font-weight: 600; color: #171717; }
  .pill { padding: 2px 8px; border-radius: 999px; font-size: 12px; font-weight: 600; }
  .pill-blocker { background: var(--rev-severity-blocker, #EF4444); color: #fff; }
  .pill-minor   { background: var(--rev-severity-minor, #2563EB); color: #fff; }
  .record-why { color: #404040; margin: 0; }
</style>
```

## 10. Implementation Checklist

- [ ] Review formats declared per session using `--rev-review-formats` — critique, QA pass, and release gate never mixed in one room.
- [ ] Every finding cites a standard (token, guide, WCAG SC) per `--rev-criteria-rule` — taste-only feedback rejected at the scribe's table.
- [ ] Severity vocabulary matches `--rev-severity-scale` exactly across tickets, reports, and gates.
- [ ] Roles per `--rev-role-separation` assigned before the session: presenter, facilitator, scribe — no self-facilitated reviews.
- [ ] Cadence from `--rev-cadence` on the calendar: per-milestone critiques and per-release gates, not review-on-request.
- [ ] Every finding ticketed with `--rev-findings-to-tickets` fields (owner + severity + state) before the room closes.
- [ ] Decision records capture `--rev-decision-record` (what + who + why) and are linked from the report.
- [ ] Each session timeboxed to `--rev-timebox` and scoped to `--rev-scope-rule`; prior blockers verified per `--rev-loop-closure`.
