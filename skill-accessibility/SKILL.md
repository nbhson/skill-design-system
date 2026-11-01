---
name: accessibility
description: Professional accessibility skill guide covering 12 disciplines (WCAG fundamentals, color & contrast, keyboard navigation, focus management, ARIA fundamentals, ARIA widget patterns, forms & errors, screen reader testing, images & media alt text, cognitive content, zoom & reflow, testing & audit framework). Use when building or reviewing any UI for WCAG conformance, fixing accessibility bugs, wiring ARIA, or auditing a product for a11y.
---

# Accessibility — Skill Router

This skill provides 12 curated accessibility-discipline guides. Each guide covers definition, core principles, spec tokens (policies/thresholds/contracts), composition, signature patterns, real-world use cases, combination notes, anti-patterns, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the accessibility task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| WCAG Fundamentals | Setting conformance targets, legal mapping | Deep-dives on one criterion (→ its guide) |
| Color & Contrast | Palettes that pass 1.4.3/1.4.11 by construction | Fixing contrast by eye |
| Keyboard Navigation | Tab order, skip links, keymaps (2.1.1) | Mouse-only prototypes |
| Focus Management | Where focus lands/returns on UI change | Static pages with no state change |
| ARIA Fundamentals | Roles, states, names, live regions | Replacing native HTML |
| ARIA Widget Patterns | Tabs, menus, combobox, dialog per APG | Inventing custom keymaps |
| Forms & Errors | Labels, hints, error wiring (3.3.x) | Placeholder-as-label forms |
| Screen Reader Testing | NVDA/JAWS/VoiceOver listening passes | Axe-only validation |
| Images, Media & Alt Text | Alt writing, captions, transcripts (1.1.1/1.2.x) | Decorative-image noise |
| Cognitive & Content | Plain language, consistency, timeouts (3.x) | Automated-only checking |
| Zoom, Reflow & Responsive A11y | 200%/400% zoom, 320px reflow (1.4.4/1.4.10) | Desktop-only sign-off |
| Testing & Audit Framework | CI gates + manual passes + reports | One-time badge audits |

If the user names a task explicitly ("make the modal accessible", "fix contrast"), go straight to its guide. If the task is "make X accessible", start with **wcag-fundamentals** to map criteria, then pull the specialized guides.

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
| 1 | WCAG Fundamentals | [skills/01-wcag-fundamentals/SKILL.md](./skills/01-wcag-fundamentals/SKILL.md) |
| 2 | Color & Contrast | [skills/02-color-contrast/SKILL.md](./skills/02-color-contrast/SKILL.md) |
| 3 | Keyboard Navigation | [skills/03-keyboard-navigation/SKILL.md](./skills/03-keyboard-navigation/SKILL.md) |
| 4 | Focus Management | [skills/04-focus-management/SKILL.md](./skills/04-focus-management/SKILL.md) |
| 5 | ARIA Fundamentals | [skills/05-aria-fundamentals/SKILL.md](./skills/05-aria-fundamentals/SKILL.md) |
| 6 | ARIA Widget Patterns | [skills/06-aria-patterns-widgets/SKILL.md](./skills/06-aria-patterns-widgets/SKILL.md) |
| 7 | Forms & Error Handling | [skills/07-forms-errors/SKILL.md](./skills/07-forms-errors/SKILL.md) |
| 8 | Screen Reader Testing | [skills/08-screen-readers/SKILL.md](./skills/08-screen-readers/SKILL.md) |
| 9 | Images, Media & Alt Text | [skills/09-media-alt-text/SKILL.md](./skills/09-media-alt-text/SKILL.md) |
| 10 | Cognitive & Content Accessibility | [skills/10-cognitive-content/SKILL.md](./skills/10-cognitive-content/SKILL.md) |
| 11 | Zoom, Reflow & Responsive A11y | [skills/11-zoom-reflow/SKILL.md](./skills/11-zoom-reflow/SKILL.md) |
| 12 | Testing & Audit Framework | [skills/12-testing-audit/SKILL.md](./skills/12-testing-audit/SKILL.md) |

## Step 3 — Apply

- Treat the spec tokens as **hard standards**: WCAG AA is the release gate; Level A failures block without exception.
- Respect the **native-HTML-first rule**: ARIA adds semantics only where native elements genuinely cannot go.
- ALWAYS honor the guide's **Accessibility Notes** — every guide's fallback states what ships when a criterion cannot be met (documented exception + alternative path, never silence).
- Check the **Combination Matrix** in [README.md](./README.md) before pairing disciplines: ✅ combines well, ⚠️ conditional, ❌ do not combine.
- When the task also involves visual style, motion, or tokens, consult companions **skill-ui-ux**, **skill-animation**, and **skill-design-tokens** via the guides' affinity notes.

## Machine-Readable Data

For programmatic use (a11y linting, CI wiring, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, affinity mappings, and per-skill accessibility contracts:

```json
{ "skills": [{ "id": "color-contrast", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — spec tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--a11y-*`); WCAG 2.2 criteria được pin ở guide 01; sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-ui-ux (12 design styles) — `sections.styleAffinity`; skill-animation (12 motion disciplines) — `sections.motionAffinity`; skill-design-tokens (12 token disciplines) — contrast/focus/target-size contracts

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and testing resources: [`skills/assets/references.md`](./skills/assets/references.md).
