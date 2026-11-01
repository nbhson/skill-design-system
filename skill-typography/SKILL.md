---
name: typography
description: Professional typography skill guide covering 12 disciplines (font pairing & selection, modular type scale, line-height & rhythm, letter-spacing & tracking, typographic hierarchy, fluid & responsive type, Vietnamese & multilingual typography, readability & measure, webfont loading, numeric & tabular figures, variable fonts, accessible typography). Use when choosing fonts, building type scales, fixing reading comfort or diacritic rendering, or auditing typography quality and accessibility.
---

# Typography — Skill Router

This skill provides 12 curated typography-discipline guides. Each guide covers definition, core principles, spec tokens (values/policies), composition, signature patterns, real-world use cases, combination notes, anti-patterns, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the typography task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Font Pairing & Selection | Choosing the product's families + fallbacks | Swapping fonts per campaign |
| Modular Type Scale | The size ramp (root 16, ratio ~1.25) | One-off sizes (17px, 22px) |
| Line-Height & Rhythm | Leading per role, grid rhythm, diacritic headroom | Px line-heights |
| Letter-Spacing & Tracking | Display tracking, uppercase labels | Tracked-out body text |
| Typographic Hierarchy | Ranking text via size/weight/color/position | Everything-emphasized pages |
| Fluid & Responsive Type | clamp() interpolation between scale stops | Fluid body text |
| Multilingual & Vietnamese | Diacritics, subsets, fallback chains | English-only QA |
| Readability & Measure | 45-75ch measure, paragraph rhythm, legibility | Full-width walls of text |
| Webfont Loading | Subsets, font-display, CLS prevention | Monolithic font files |
| Numeric & Tabular Figures | Aligned tables, count-ups, codes | Proportional digits in tables |
| Variable Fonts | One-file multi-axis type | Axis playgrounds |
| Accessible Typography | Contrast/zoom/spacing floors (WCAG) | Gray-on-gray de-ranking |

If the user names a task explicitly ("hero font too big on mobile", "Vietnamese marks clipped"), go straight to its guide. If the task is "set up typography", start with **font-pairing** → **type-scale**, then pull the rest as needed.

## Step 2 — Read the discipline guide

Each guide lives in `skills/<NN-<skill>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Principles — mandatory rules
3. Spec Tokens — value/policy tokens + role of each
4. Composition — how the skill pairs with siblings and companion repos
5. Signature Patterns — the 2–3 canonical implementation patterns
6. Real-World Use Cases — suitable products/contexts
7. Combination Notes — pairing with sibling skills + affinity to skill-ui-ux / skill-animation / skill-design-tokens
8. Anti-Patterns — common mistakes (incl. Accessibility Notes)
9. Code Examples — complete HTML+CSS (±JS) snippets using the spec tokens
10. Implementation Checklist — pre-delivery quality checks

| # | Discipline | Guide |
|---|-----------|-------|
| 1 | Font Pairing & Selection | [skills/01-font-pairing/SKILL.md](./skills/01-font-pairing/SKILL.md) |
| 2 | Modular Type Scale | [skills/02-type-scale/SKILL.md](./skills/02-type-scale/SKILL.md) |
| 3 | Line-Height & Rhythm | [skills/03-line-height/SKILL.md](./skills/03-line-height/SKILL.md) |
| 4 | Letter-Spacing & Tracking | [skills/04-letter-spacing/SKILL.md](./skills/04-letter-spacing/SKILL.md) |
| 5 | Typographic Hierarchy | [skills/05-visual-hierarchy/SKILL.md](./skills/05-visual-hierarchy/SKILL.md) |
| 6 | Fluid & Responsive Typography | [skills/06-fluid-responsive/SKILL.md](./skills/06-fluid-responsive/SKILL.md) |
| 7 | Multilingual & Vietnamese Typography | [skills/07-multilingual-vietnamese/SKILL.md](./skills/07-multilingual-vietnamese/SKILL.md) |
| 8 | Readability & Measure | [skills/08-readability-legibility/SKILL.md](./skills/08-readability-legibility/SKILL.md) |
| 9 | Webfont Loading & Performance | [skills/09-webfont-loading/SKILL.md](./skills/09-webfont-loading/SKILL.md) |
| 10 | Numeric & Tabular Figures | [skills/10-numeric-tabular/SKILL.md](./skills/10-numeric-tabular/SKILL.md) |
| 11 | Variable Fonts | [skills/11-variable-fonts/SKILL.md](./skills/11-variable-fonts/SKILL.md) |
| 12 | Accessible Typography | [skills/12-accessible-typography/SKILL.md](./skills/12-accessible-typography/SKILL.md) |

## Step 3 — Apply

- Treat the spec tokens as **hard standards**: one scale, closed weights, unitless leading, rem sizes - off-scale values are token violations.
- Respect the **reading floors**: 16px body, 1.5 leading, 4.5:1 contrast - floors beat aesthetics.
- ALWAYS honor the guide's **Accessibility Notes**; when brand choices conflict with WCAG floors, floors win.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing disciplines: ✅ combines well, ⚠️ conditional, ❌ do not combine.
- When the task also involves visual style, motion, or tokens, consult companions **skill-ui-ux**, **skill-animation**, and **skill-design-tokens** via the guides' affinity notes.

## Machine-Readable Data

For programmatic use (type linting, CI checks, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, affinity mappings, and per-skill accessibility contracts:

```json
{ "skills": [{ "id": "type-scale", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — spec tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--type-*`); sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-ui-ux (12 design styles) — `sections.styleAffinity`; skill-animation (12 motion disciplines) — `sections.motionAffinity`; skill-design-tokens (12 token disciplines) — typography tokens + contrast contracts

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).
