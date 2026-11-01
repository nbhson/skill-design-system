# ✍️ Professional UX Writing Skill Set — 12 Writing Disciplines

A professional reference guide for 12 UX-writing disciplines, each covering: definition, core principles, spec tokens (policies/budgets/contracts), composition, signature patterns, real-world applications, combination notes, anti-patterns, accessibility notes, code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles), **skill-animation** (12 motion disciplines), **skill-design-tokens** (12 token disciplines), **skill-component-recipes** (12 component recipes). This repo answers *"what do the words say?"* — the copy layer above components and styles. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Writing Principles](./skills/01-writing-principles/SKILL.md) | 01-writing-principles | The foundation: clarity-first, user-first, plain language, active voice, and brevity - the rules every other copy discipline inherits. |
| 2 | [Voice & Tone](./skills/02-voice-tone/SKILL.md) | 02-voice-tone | Voice is constant, tone flexes: defining the brand voice dimensions and the tone matrix that shifts with user emotional state. |
| 3 | [Button & Action Labels](./skills/03-button-labels/SKILL.md) | 03-button-labels | Verb-first, specific, outcome-visible labels: what the button does, phrased in the user's terms - never 'OK', 'Submit', or 'Yes'. |
| 4 | [Error Messages](./skills/04-error-messages/SKILL.md) | 04-error-messages | The three-part contract: what went wrong, why (in user terms), and the fix - blame-free, specific, and never a stack trace. |
| 5 | [Empty State Copy](./skills/05-empty-states/SKILL.md) | 05-empty-states | First-use, no-results, and cleared states as teaching moments: explain the value, then hand over the next action. |
| 6 | [Onboarding & First-Run Copy](./skills/06-onboarding-copy/SKILL.md) | 06-onboarding-copy | First-run guidance that respects intelligence: progressive disclosure, show-don't-tour, and copy that gets users to value fast. |
| 7 | [Component Microcopy](./skills/07-component-microcopy/SKILL.md) | 07-component-microcopy | The small strings with big jobs: tooltips, hints, placeholders, helper text, toggle labels - and the placeholder-is-not-a-label rule. |
| 8 | [Form Labels & Help Text](./skills/08-forms-labels/SKILL.md) | 08-forms-labels | The form copy layer: label phrasing, hint placement, required/optional marking, and validation copy timed to forgive. |
| 9 | [Notification & Toast Copy](./skills/09-notifications/SKILL.md) | 09-notifications | Scannable, non-alarming, self-sufficient: toast and notification strings that work when skimmed and when read by AT. |
| 10 | [Localization & i18n Writing](./skills/10-localization-i18n/SKILL.md) | 10-localization-i18n | Writing for translation: externalized strings, ICU plurals, expansion room, pseudo-localization, and tone that survives translation. |
| 11 | [Accessible & Inclusive Writing](./skills/11-accessible-writing/SKILL.md) | 11-accessible-writing | Writing for assistive tech and cognition: alt text as copy, descriptive links, reading order, and plain-language inclusion. |
| 12 | [Copy Audit & Governance](./skills/12-copy-audit/SKILL.md) | 12-copy-audit | Keeping copy consistent at scale: the glossary, string inventory, linting, and the per-surface audit pass. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, spec tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "error-messages",
    "sections": {
      "tokens": [{ "role": "error-structure", "value": "what+why+fix", "notes": "..." }],
      "combinations": { "good": [], "caution": [], "avoid": [] },
      "styleAffinity": { "good": [], "caution": [], "avoid": [] },
      "motionAffinity": { "good": [], "caution": [], "avoid": [] },
      "antiPatterns": ["..."],
      "accessibility": { "required": true, "notes": "...", "fallback": "..." }
    }
  }]
}
```

## 📚 References

[`assets/references.md`](./skills/assets/references.md) — curated spec links (WCAG plain language, ICU MessageFormat), tool docs (pseudo-localization, linting), and UX-writing learning resources.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the writing task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** treat the spec tokens from `assets/css/<skill-id>.css` as hard standards — reading level, length budgets, and message contracts. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | principles | tone | buttons | errors | empty | onboard | micro | forms | notifs | i18n | a11y | audit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Writing Principles** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Voice & Tone** | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Button & Action Labels** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Error Messages** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Empty State Copy** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Onboarding & First-Run Copy** | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Component Microcopy** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Form Labels & Help Text** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **Notification & Toast Copy** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ |
| **Localization & i18n Writing** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **Accessible & Inclusive Writing** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| **Copy Audit & Governance** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux / skill-design-tokens)

| Skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Writing Principles | minimalism, flat-design, class-morphism | maximalism |
| Voice & Tone | minimalism, retro, maximalism | brutalism-ui |
| Button & Action Labels | minimalism, flat-design, class-morphism | collage-art |
| Error Messages | minimalism, flat-design, class-morphism | collage-art |
| Empty State Copy | minimalism, flat-design, collage-art | — |
| Onboarding & First-Run Copy | minimalism, flat-design, glassmorphism | brutalism-ui |
| Component Microcopy | minimalism, flat-design, class-morphism | — |
| Form Labels & Help Text | minimalism, flat-design, class-morphism | brutalism-ui |
| Notification & Toast Copy | minimalism, flat-design, glassmorphism | collage-art |
| Localization & i18n Writing | minimalism, flat-design, class-morphism | retro |
| Accessible & Inclusive Writing | minimalism, flat-design, class-morphism | — |
| Copy Audit & Governance | minimalism, flat-design, class-morphism | — |

## 🏃 Motion Affinity (skill-animation)

| Skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| Writing Principles | micro-interactions, feedback-confirmation | — |
| Voice & Tone | feedback-confirmation, micro-interactions | — |
| Button & Action Labels | micro-interactions, feedback-confirmation | — |
| Error Messages | feedback-confirmation, easing-timing | — |
| Empty State Copy | entrance-exit, illustration-lottie | — |
| Onboarding & First-Run Copy | entrance-exit, illustration-lottie | — |
| Component Microcopy | micro-interactions, easing-timing | — |
| Form Labels & Help Text | feedback-confirmation, micro-interactions | — |
| Notification & Toast Copy | feedback-confirmation, entrance-exit | — |
| Localization & i18n Writing | easing-timing | — |
| Accessible & Inclusive Writing | reduced-motion, easing-timing | — |
| Copy Audit & Governance | easing-timing | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--uxw-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene
