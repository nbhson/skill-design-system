---
name: ux-writing
description: Professional UX writing skill guide covering 12 disciplines (writing principles, voice & tone, button labels, error messages, empty states, onboarding copy, component microcopy, form labels & help text, notifications, localization & i18n, accessible writing, copy audit & governance). Use when writing or reviewing interface copy, error messages, microcopy, or building a copy governance program.
---

# UX Writing — Skill Router

This skill provides 12 curated UX-writing guides. Each guide covers definition, core principles, spec tokens (policies/budgets/contracts), composition, signature patterns, real-world use cases, combination notes, anti-patterns, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the writing task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Writing Principles | The foundational rules all copy inherits | One-off style debates |
| Voice & Tone | Voice dimensions + tone-by-state matrix | Jokes in error paths |
| Button & Action Labels | Verb-first, specific action strings | OK/Submit sprawl |
| Error Messages | What + why + fix contracts | Dead-end errors |
| Empty State Copy | First-use / no-results / cleared | Blank boxes |
| Onboarding & First-Run Copy | Time-to-value guidance | Mandatory tours |
| Component Microcopy | Tooltips, hints, placeholders | Placeholder-as-label |
| Form Labels & Help Text | Label phrasing + validation copy | Keystroke scolding |
| Notification & Toast Copy | Scannable, polite, self-sufficient strings | Exclamation spam |
| Localization & i18n Writing | Externalized strings, ICU, expansion | Concatenated sentences |
| Accessible & Inclusive Writing | Alt text, links, AT-read strings | 'Click here' links |
| Copy Audit & Governance | Glossary, inventory, lint, scorecards | Unowned standards |

If the user names a surface explicitly ("fix the error messages", "write the empty states"), go straight to its guide. If the task is "establish our writing standards", start with **writing-principles** + **voice-tone**, then **copy-audit** for enforcement.

## Step 2 — Read the discipline guide

Each guide lives in `skills/<NN-<skill>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Principles — mandatory rules
3. Spec Tokens — policy/budget/contract values + role of each
4. Composition — how the skill pairs with siblings and companion repos
5. Signature Patterns — the 2–3 canonical implementation patterns
6. Real-World Use Cases — suitable products/contexts
7. Combination Notes — pairing with sibling skills + affinity to skill-ui-ux / skill-animation / skill-design-tokens
8. Anti-Patterns — common mistakes (incl. Accessibility Notes)
9. Code Examples — complete HTML+CSS (±JS) snippets using the spec tokens
10. Implementation Checklist — pre-delivery quality checks

| # | Discipline | Guide |
|---|-----------|-------|
| 1 | Writing Principles | [skills/01-writing-principles/SKILL.md](./skills/01-writing-principles/SKILL.md) |
| 2 | Voice & Tone | [skills/02-voice-tone/SKILL.md](./skills/02-voice-tone/SKILL.md) |
| 3 | Button & Action Labels | [skills/03-button-labels/SKILL.md](./skills/03-button-labels/SKILL.md) |
| 4 | Error Messages | [skills/04-error-messages/SKILL.md](./skills/04-error-messages/SKILL.md) |
| 5 | Empty State Copy | [skills/05-empty-states/SKILL.md](./skills/05-empty-states/SKILL.md) |
| 6 | Onboarding & First-Run Copy | [skills/06-onboarding-copy/SKILL.md](./skills/06-onboarding-copy/SKILL.md) |
| 7 | Component Microcopy | [skills/07-component-microcopy/SKILL.md](./skills/07-component-microcopy/SKILL.md) |
| 8 | Form Labels & Help Text | [skills/08-forms-labels/SKILL.md](./skills/08-forms-labels/SKILL.md) |
| 9 | Notification & Toast Copy | [skills/09-notifications/SKILL.md](./skills/09-notifications/SKILL.md) |
| 10 | Localization & i18n Writing | [skills/10-localization-i18n/SKILL.md](./skills/10-localization-i18n/SKILL.md) |
| 11 | Accessible & Inclusive Writing | [skills/11-accessible-writing/SKILL.md](./skills/11-accessible-writing/SKILL.md) |
| 12 | Copy Audit & Governance | [skills/12-copy-audit/SKILL.md](./skills/12-copy-audit/SKILL.md) |

## Step 3 — Apply

- Treat the spec tokens as **hard standards**: reading level, length budgets, and message contracts - copy that violates them is a defect, not a preference.
- Respect the **three-part error contract**: what + why + fix - errors missing a part are incomplete.
- ALWAYS honor the guide's **Accessibility Notes**: alt text, link text, aria-labels, and narration-friendly strings are copy contracts, not polish.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing disciplines: ✅ combines well, ⚠️ conditional, ❌ do not combine.
- When the task also involves components, visual style, or motion, consult companions **skill-component-recipes**, **skill-ui-ux**, and **skill-animation** via the guides' affinity notes.

## Machine-Readable Data

For programmatic use (copy linting, CI wiring, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, affinity mappings, and per-skill accessibility contracts:

```json
{ "skills": [{ "id": "error-messages", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — spec tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--uxw-*`); sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-component-recipes (12 component recipes) — copy slots; skill-ui-ux (12 design styles) — `sections.styleAffinity`; skill-animation (12 motion disciplines) — `sections.motionAffinity`

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).
