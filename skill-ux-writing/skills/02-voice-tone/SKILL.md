---
name: voice-tone
description: Voice is constant, tone flexes — define the brand voice dimensions and the tone matrix that shifts with user emotional state, from celebration to frustration.
tags: [ux-writing, voice, tone, brand, personality]
related: [writing-principles, error-messages, empty-states]
---

# UX Writing Guide: Voice & Tone

## 1. Definition

Voice is the personality that never changes; tone is how it bends to context. A product can be confident and warm in celebration, quieter and more direct in an error. This guide defines the voice dimensions (formal–casual, playful–serious, concise–elaborate), the tone matrix keyed to user emotional state (neutral, stressed, celebrating, frustrated), and the guardrails that stop "brand personality" from undermining comprehension when users are anxious. The unit of decision is the matrix row, not the writer's mood: each user state has documented, allowed tone traits with do/don't examples, so personality becomes a system like any other — constant where it should be, deliberate where it flexes.

## 2. Core Principles

- **Voice is constant, tone flexes:** the personality dimensions hold across every surface; intensity is what changes.
- **Tone tracks user state, not brand mood:** match energy to the user's emotional context — success celebrates, errors reassure and instruct.
- **Stress kills humor:** error, payment, and destructive paths drop jokes entirely — clarity is the only voice under stress.
- **Humor has a home:** empty states, loading, and success moments may carry personality; forms and errors carry precision.
- **Tone range is documented per state:** the matrix lists allowed traits (e.g. errors: calm, specific, no blame) — writers pick from the matrix, not from mood.
- **Never at comprehension's expense:** a personality flourish that adds reading effort has failed, whatever the brand deck says.
- **Localization checks tone:** wordplay, slang, and formality registers rarely translate — the tone matrix flags tone-risky strings for i18n review.
- **The voice charter is versioned:** tone decisions ship as docs with examples — tribal voice knowledge does not survive team growth.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Voice dimensions | `--uxw-voice-dimensions` | `formal-casual,playful-serious,concise-elaborate` | Three axes; products mark their point |
| Tone states | `--uxw-tone-matrix-states` | `neutral,stressed,celebrating,frustrated` | Tone keyed to user emotional state |
| Error tone policy | `--uxw-tone-error-policy` | `calm-specific-noblame` | No humor in error paths |
| Success tone policy | `--uxw-tone-success-policy` | `quiet-warm` | Celebrate briefly; do not gloat |
| Empty tone policy | `--uxw-tone-empty-policy` | `personality-allowed` | Empty states carry brand warmth |
| Stress rule | `--uxw-tone-stress-rule` | `humor-off` | Payments, deletes, outages: precision only |
| Localization flag | `--uxw-tone-localization-flag` | `wordplay-marked` | Tone-risky strings tagged for i18n review |
| Voice charter | `--uxw-voice-charter` | `versioned-doc` | One page, with example rewrites |
| Tone examples | `--uxw-tone-examples-required` | `per-state` | Matrix ships with do/dont examples |
| Consistency owner | `--uxw-voice-consistency-owner` | `copy-audit-guide` | Audit checks charter adherence |

Consume them by linking `assets/css/voice-tone.css` at the app root and reading `var(--uxw-...)` values from the voice charter and string inventory — each shipped string carries its tone-state tag, and lint checks humor-bearing strings against the stress rule. If a new surface does not map to an existing state row, add the row through charter review; writers do not invent tone ad hoc.

## 4. Composition

- **Composes with writing-principles (guide 01):** the charter implements those principles as personality — voice-tone can change how warm or playful a string is, never whether it is clear, active, and user-first.
- **Composes with error-messages (guide 03):** the error tone row (calm, specific, no blame) is this guide's contract applied — the three-part error structure is written in the error row's voice, and humor is structurally off there.
- **Composes with localization-i18n (guide 10):** tone-risky strings (humor, puns, idiom) are flagged in the string inventory with the `--uxw-tone-localization-flag` marker so translators see tone intent — or get permission to flatten it — before they translate.

## 5. Signature Patterns

- **The tone matrix:** rows = user states, columns = tone traits + example do/don't strings — the single reference writers keep open. One matrix prevents the two failure directions at once: mechanical tonelessness and unbounded whimsy.
- **Voice charter with rewrite pairs:** real before/after examples per state — "Welcome aboard!" vs "Your account is ready" teaches faster than adjectives. Every trait in the matrix ships with at least one concrete pair.

## 6. Real-World Use Cases

- **Brand relaunches where voice decisions were implicit tribal knowledge** — the charter converts one writer's instincts into a versioned, teachable document.
- **Support-heavy products where frustrated users meet tone daily** — the stressed/frustrated rows are the highest-leverage copy in the product.
- **Audit: jokes in error paths, gloating success messages, toneless mechanical copy** — the matrix makes each failure a checkable deviation, not a matter of taste.

## 7. Combination Notes

### With other ux-writing skills

- **Good with writing-principles, error-messages, and empty-states:** writing-principles sets the baseline this guide flexes; error-messages applies the stressed row (calm-specific-noblame) verbatim; empty-states is the sanctioned home of personality per `--uxw-tone-empty-policy`.
- **Good with onboarding-copy, notifications, component-microcopy, and button-labels:** each surface maps to a matrix row — onboarding reads neutral-warm, toasts quiet-warm, labels stay precise — so the matrix becomes the shared vocabulary across guides.
- **Good with copy-audit and accessible-writing:** the audit enforces charter adherence string-by-string; accessible-writing guarantees tone never costs comprehension, which is this guide's own hard limit.
- **Caution with localization-i18n (appears in both good and caution):** the partnership is essential but tightrope — tone is exactly what breaks in translation. The rule: collaborate on flagging and flattening tone-risky strings, never let i18n pressure silently erase the voice, and never let voice pressure translators into untranslatable wordplay.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, retro, and maximalism:** minimalism and tone share the restraint instinct (quiet-warm success, no gloating); retro and maximalism carry visual personality that well-aimed textual personality completes — in all three, voice and visuals reinforce one identity instead of competing.
- **Caution with brutalism-ui:** brutalism's abrasive, confrontational register reads as blame in error paths; where the style demands edge, confine it to neutral-state surfaces and keep the stress rows calm.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation and micro-interactions:** tone and motion are the two halves of emotional feedback — a quiet-warm success message pairs with a subtle confirmatory animation, and micro-interactions carry playfulness so the copy itself can stay short.
- **Caution with celebratory over-motion:** full-screen confetti motion plus gloating copy violates `--uxw-tone-success-policy` together; spec tone and motion from the same matrix row so neither escalates past it.

## 8. Anti-Patterns

- **Humor in error paths** — 'Oops, we broke something!' while the user's work is gone
- **Tone-void copy** — personality stripped everywhere until the product reads as a manual
- **Gloating success** — over-celebrating trivial actions with full-screen confetti copy
- **Undocumented voice** — personality that lives in one writer's head

### Accessibility Notes

Tone serves cognition: under stress, plain language and predictability are the accessible choice (WCAG 3.1.5, the a11y cognitive-content guide) — which means the stress rule (humor off in payment, delete, and outage paths) is also an accessibility rule, not just a brand preference. Anxiety narrows working memory; a joke the user must parse before the fix is a cognitive tax levied at the worst moment, and screen reader users hear strings in isolation where playful framing can obscure the actionable content. The fallback is deliberate: if the tone matrix is unwritten, adopt the default row — neutral-calm, active voice, no humor in error/payment/delete paths — then document from there; a conservative default ships today while the charter matures, and no string waits on a workshop.

## 9. Code Examples

### Example 1 — Tone matrix demo: one event, four states

Tokens: `assets/css/voice-tone.css`

```html
<div class="matrix">
  <div class="cell" data-state="neutral">
    <h3>Neutral</h3>
    <p class="do">Upload complete. 12 photos added to Summer trip.</p>
    <p class="dont">Photos have been ingested into the asset store.</p>
  </div>
  <div class="cell" data-state="celebrating">
    <h3>Celebrating</h3>
    <p class="do">All 12 photos are in. Take a look.</p>
    <p class="dont">🎉 SPECTACULAR! Your photos have achieved upload greatness! 🎉</p>
  </div>
  <div class="cell" data-state="stressed">
    <h3>Stressed (failure)</h3>
    <p class="do">We couldn't upload 2 photos. They may be too large. Try files under 25 MB.</p>
    <p class="dont">Oops, we broke something!</p>
  </div>
  <div class="cell" data-state="frustrated">
    <h3>Frustrated (repeated failure)</h3>
    <p class="do">Still failing on those 2 photos. Skip them for now, or contact support with error E-412.</p>
    <p class="dont">Are you sure your internet is working?</p>
  </div>
</div>
<style>
  .matrix { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 640px; }
  .cell { border: 1px solid #E5E5E5; border-radius: 8px; padding: 12px; }
  .cell h3 { margin: 0 0 8px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.04em; color: #525252; }
  .do   { margin: 4px 0; padding-left: 12px; border-left: 3px solid #22C55E; }
  .dont { margin: 4px 0; padding-left: 12px; border-left: 3px solid #EF4444; color: #525252; }
  /* stressed + frustrated rows: --uxw-tone-stress-rule is humor-off; copy is calm, specific, no blame */
</style>
```

### Example 2 — Error path (humor off) vs empty state (personality on)

Tokens: `assets/css/voice-tone.css`

```html
<div class="panel error" role="alert">
  <strong>Payment failed</strong>
  <p>We couldn't charge your card. The issuer declined the 3-digit security code. Check it and try again.</p>
  <button class="primary">Try again</button>
</div>
<div class="panel empty">
  <strong>No projects yet</strong>
  <p>Your projects will live here. Create the first one and see what a tidy workspace feels like.</p>
  <button class="primary">Create project</button>
</div>
<style>
  .panel { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 400px; border-radius: 8px; padding: 16px; margin-bottom: 12px; border: 1px solid #E5E5E5; }
  .error { border-left: 4px solid #EF4444; }
  .error strong { display: block; margin-bottom: 4px; }
  .error p { margin: 0 0 12px; color: #404040; }
  .empty p { margin: 0 0 12px; color: #404040; }   /* personality allowed here per --uxw-tone-empty-policy */
  .primary { padding: 8px 16px; border: none; border-radius: 6px; background: #171717; color: #fff; font-weight: 600; cursor: pointer; }
</style>
```

## 10. Implementation Checklist

- [ ] The voice charter is a versioned doc (`--uxw-voice-charter`) marking the product's point on all three `--uxw-voice-dimensions` axes.
- [ ] The tone matrix covers all four `--uxw-tone-matrix-states` rows, each with allowed traits and do/don't example pairs.
- [ ] Error, payment, and delete paths enforce `--uxw-tone-stress-rule: humor-off` — lint blocks humor markers on tagged strings.
- [ ] Success copy follows `--uxw-tone-success-policy: quiet-warm`; no confetti copy on trivial actions.
- [ ] Empty states and loading carry personality per `--uxw-tone-empty-policy` — and nowhere else by default.
- [ ] Tone-risky strings carry the `--uxw-tone-localization-flag` marker and are reviewed before translation.
- [ ] Every matrix row ships examples per `--uxw-tone-examples-required`; no trait exists without a rewrite pair.
- [ ] The copy audit checks charter adherence per `--uxw-voice-consistency-owner` and files drift as bugs, not opinions.
