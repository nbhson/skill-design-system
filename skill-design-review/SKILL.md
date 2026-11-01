---
name: design-review
description: Professional design review skill guide covering 12 disciplines (review process, visual hierarchy audit, consistency audit, accessibility audit, motion audit, typography audit, spacing & rhythm audit, interaction states audit, content & microcopy audit, perceived performance, responsive audit, report template). Use when running design critiques, pre-release design gates, or full surface audits.
---

# Design Review — Skill Router

This skill provides 12 curated design-review guides. Each guide covers definition, core principles, spec tokens (protocols/thresholds/contracts), composition, signature patterns, real-world use cases, combination notes, anti-patterns, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the review task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Review Process | Critique formats, severity, ticket loop | Taste debates |
| Visual Hierarchy Audit | Squint test, scan path, primary action | Box-everything layouts |
| Consistency Audit | Token adherence, pattern parity | Token theater |
| Accessibility Audit | Keyboard/SR/contrast/zoom passes | Scan-only audits |
| Motion Audit | Purpose, duration ladder, reduced-motion | Flarb-everything |
| Typography Audit | Scale adherence, type crimes | Off-ramp sizes |
| Spacing & Rhythm Audit | 4/8px grid, proximity, alignment | Almost-aligned elements |
| Interaction States Audit | The full state matrix per element | outline:none regressions |
| Content & Microcopy Audit | Error completeness, labels, glossary | Unaudited hidden strings |
| Perceived Performance | Response bands, skeletons, optimism | Blank freezes |
| Responsive Audit | Size matrix, reflow floor, collapse checks | Untested collapses |
| Audit Report Template | Scorecards, findings tables, trends | Screenshot graveyards |

If the user names an axis explicitly ("audit accessibility", "check the spacing"), go straight to its guide. If the task is "review this surface before release", run the release gate: **review-process** + the per-axis checklists in order, reported through **report-template**.

## Step 2 — Read the discipline guide

Each guide lives in `skills/<NN-<skill>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Principles — mandatory rules
3. Spec Tokens — protocol/threshold/contract values + role of each
4. Composition — how the skill pairs with siblings and companion repos
5. Signature Patterns — the 2–3 canonical implementation patterns
6. Real-World Use Cases — suitable products/contexts
7. Combination Notes — pairing with sibling skills + affinity to skill-ui-ux / skill-animation / skill-design-tokens
8. Anti-Patterns — common mistakes (incl. Accessibility Notes)
9. Code Examples — complete HTML+CSS (±JS) snippets using the spec tokens
10. Implementation Checklist — pre-delivery quality checks

| # | Discipline | Guide |
|---|-----------|-------|
| 1 | Review Process | [skills/01-review-process/SKILL.md](./skills/01-review-process/SKILL.md) |
| 2 | Visual Hierarchy Audit | [skills/02-visual-hierarchy-audit/SKILL.md](./skills/02-visual-hierarchy-audit/SKILL.md) |
| 3 | Consistency Audit | [skills/03-consistency-audit/SKILL.md](./skills/03-consistency-audit/SKILL.md) |
| 4 | Accessibility Audit | [skills/04-a11y-audit/SKILL.md](./skills/04-a11y-audit/SKILL.md) |
| 5 | Motion Audit | [skills/05-motion-audit/SKILL.md](./skills/05-motion-audit/SKILL.md) |
| 6 | Typography Audit | [skills/06-typography-audit/SKILL.md](./skills/06-typography-audit/SKILL.md) |
| 7 | Spacing & Rhythm Audit | [skills/07-spacing-rhythm-audit/SKILL.md](./skills/07-spacing-rhythm-audit/SKILL.md) |
| 8 | Interaction States Audit | [skills/08-interaction-states-audit/SKILL.md](./skills/08-interaction-states-audit/SKILL.md) |
| 9 | Content & Microcopy Audit | [skills/09-content-microcopy-audit/SKILL.md](./skills/09-content-microcopy-audit/SKILL.md) |
| 10 | Perceived Performance | [skills/10-perceived-performance/SKILL.md](./skills/10-perceived-performance/SKILL.md) |
| 11 | Responsive Audit | [skills/11-responsive-audit/SKILL.md](./skills/11-responsive-audit/SKILL.md) |
| 12 | Audit Report Template | [skills/12-report-template/SKILL.md](./skills/12-report-template/SKILL.md) |

## Step 3 — Apply

- Treat the spec tokens as **hard standards**: severity scales, duration ladders, response bands, and size matrices - audit findings cite these, not taste.
- Respect the **criteria rule**: every finding cites a standard (token, guide contract, WCAG SC) - findings without criteria are opinions.
- ALWAYS honor the guide's **Accessibility Notes**: the a11y axis gates releases - blocker-severity a11y findings block shipping.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing disciplines: ✅ combines well, ⚠️ conditional, ❌ do not combine.
- When the audit needs the criteria themselves, consult companions **skill-ui-ux** (styles), **skill-animation** (motion tokens), **skill-design-tokens** (token contracts), **skill-accessibility** (WCAG guides), **skill-component-recipes**, and **skill-ux-writing**.

## Machine-Readable Data

For programmatic use (audit tooling, CI wiring, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, affinity mappings, and per-skill accessibility contracts:

```json
{ "skills": [{ "id": "a11y-audit", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — spec tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--rev-*`); sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-ui-ux (12 design styles) — `sections.styleAffinity`; skill-animation (12 motion disciplines) — `sections.motionAffinity`; skill-design-tokens / skill-accessibility / skill-component-recipes / skill-ux-writing — criteria sources the audits check against

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).
