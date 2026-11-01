---
name: component-recipes
description: Professional component recipe skill guide covering 12 disciplines (buttons & badges, forms & inputs, tables & data grids, modals & dialogs, toasts & notifications, navigation patterns, cards & lists, tabs & accordions, dropdowns & menus, command palette, empty/loading/error states, component a11y wiring). Use when building or standardizing UI components, writing component specs, or auditing component libraries.
---

# Component Recipes — Skill Router

This skill provides 12 curated component-recipe guides. Each guide covers definition, core principles, spec tokens (policies/thresholds/contracts), composition, signature patterns, real-world use cases, combination notes, anti-patterns, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the component task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Buttons & Badges | Action vocabulary, variants, states | Reinventing buttons per screen |
| Forms & Input Recipes | Field wiring, validation timing | Placeholder-as-label forms |
| Tables & Data Grids | Sort/filter/select contracts, semantics | Div-table soup |
| Modals & Dialogs | The dialog contract + when-to-modal | Modal fatigue |
| Toasts & Notifications | Polite transient feedback + undo | Toast floods |
| Navigation Patterns | Top bar/sidebar/breadcrumbs/pagination | Rebuilt nav per page |
| Cards & Lists | Content containers, stretched links | Link-in-link markup |
| Tabs & Accordions | APG disclosure widgets | Buried primary content |
| Dropdowns & Menus | Value-vs-action, popovers, tooltips | Menu-as-select |
| Command Palette | Cmd-K search over actions/objects | Static nav-only palettes |
| Empty, Loading & Error States | Skeletons, empty taxonomy, recovery | Blank boxes |
| Component A11y Wiring | The per-component a11y checklist gate | A11y-as-appendix |

If the user names a component explicitly ("build the data table", "dialog focus is broken"), go straight to its guide. If the task is "stand up the component layer", start with **buttons-badges** + **forms-inputs** (the first two components), then **accessibility-wiring** as the gate for the rest.

## Step 2 — Read the discipline guide

Each guide lives in `skills/<NN-<skill>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Principles — mandatory rules
3. Spec Tokens — policy/threshold/contract values + role of each
4. Composition — how the skill pairs with siblings and companion repos
5. Signature Patterns — the 2–3 canonical implementation patterns
6. Real-World Use Cases — suitable products/contexts
7. Combination Notes — pairing with sibling skills + affinity to skill-ui-ux / skill-animation / skill-design-tokens
8. Anti-Patterns — common mistakes (incl. Accessibility Notes)
9. Code Examples — complete HTML+CSS (±JS) snippets using the spec tokens
10. Implementation Checklist — pre-delivery quality checks

| # | Discipline | Guide |
|---|-----------|-------|
| 1 | Buttons & Badges | [skills/01-buttons-badges/SKILL.md](./skills/01-buttons-badges/SKILL.md) |
| 2 | Forms & Input Recipes | [skills/02-forms-inputs/SKILL.md](./skills/02-forms-inputs/SKILL.md) |
| 3 | Tables & Data Grids | [skills/03-tables-data-grid/SKILL.md](./skills/03-tables-data-grid/SKILL.md) |
| 4 | Modals & Dialogs | [skills/04-modals-dialogs/SKILL.md](./skills/04-modals-dialogs/SKILL.md) |
| 5 | Toasts & Notifications | [skills/05-toasts-notifications/SKILL.md](./skills/05-toasts-notifications/SKILL.md) |
| 6 | Navigation Patterns | [skills/06-navigation-patterns/SKILL.md](./skills/06-navigation-patterns/SKILL.md) |
| 7 | Cards & Lists | [skills/07-cards-lists/SKILL.md](./skills/07-cards-lists/SKILL.md) |
| 8 | Tabs & Accordions | [skills/08-tabs-accordions/SKILL.md](./skills/08-tabs-accordions/SKILL.md) |
| 9 | Dropdowns & Menus | [skills/09-dropdowns-menus/SKILL.md](./skills/09-dropdowns-menus/SKILL.md) |
| 10 | Command Palette & Search | [skills/10-command-palette/SKILL.md](./skills/10-command-palette/SKILL.md) |
| 11 | Empty, Loading & Error States | [skills/11-empty-loading-error/SKILL.md](./skills/11-empty-loading-error/SKILL.md) |
| 12 | Component A11y Wiring | [skills/12-accessibility-wiring/SKILL.md](./skills/12-accessibility-wiring/SKILL.md) |

## Step 3 — Apply

- Treat the spec tokens as **hard standards**: closed variant sets, size ramps, and per-state contracts - ad-hoc component styling is a violation.
- Respect the **recipe completeness rule**: a component spec ships with its loading/empty/error states and its a11y wiring (guide 12) - happy-path-only specs are incomplete.
- ALWAYS honor the guide's **Accessibility Notes**: keymaps, focus contracts, announcements, and 44px targets are component contracts, not polish.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing disciplines: ✅ combines well, ⚠️ conditional, ❌ do not combine.
- When the task also involves visual style, motion, or tokens, consult companions **skill-ui-ux**, **skill-animation**, and **skill-design-tokens** via the guides' affinity notes.

## Machine-Readable Data

For programmatic use (component linting, CI wiring, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, affinity mappings, and per-skill accessibility contracts:

```json
{ "skills": [{ "id": "modals-dialogs", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — spec tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--comp-*`); sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-ui-ux (12 design styles) — `sections.styleAffinity`; skill-animation (12 motion disciplines) — `sections.motionAffinity`; skill-design-tokens (12 token disciplines) — color/radius/spacing contracts

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).
