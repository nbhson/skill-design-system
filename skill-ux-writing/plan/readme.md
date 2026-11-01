# Plan — skill-ux-writing

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu các skill repo trước — cập nhật: 02/11/2026

## Tổng quan

Skill bộ 12 UX-writing disciplines (Writing Principles → Copy Audit & Governance) cho OpenCode:
mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json` machine-readable + CSS spec
tokens (`--uxw-*`) + validator CI. Companion repos: `skill-component-recipes` (copy slots),
`skill-ui-ux` (styleAffinity), `skill-animation` (motionAffinity),
`skill-accessibility` (criteria layer cho alt text, link text, plain language).

## Phân loại 12 disciplines

1. writing-principles — clarity-first, plain language, active voice
2. voice-tone — voice dimensions + tone-by-state matrix
3. button-labels — verb-first, specific, destructive-with-count
4. error-messages — what+why+fix, blame-free, taxonomy
5. empty-states — first-use / no-results / cleared formulas
6. onboarding-copy — time-to-value, show-don't-tour, checklists
7. component-microcopy — tooltips, hints, placeholders, budgets
8. forms-labels — label phrasing, optional marking, forgiving validation
9. notifications — object+result, anti-alarm, front-load
10. localization-i18n — externalization, ICU, expansion, pseudo-loc
11. accessible-writing — alt text, links, reading order, aria-label voice
12. copy-audit — glossary, string inventory, lint, scorecards

## Tiến độ

- [x] plan/readme.md
- [x] skills/data.json (12 skills, matrix đối xứng, affinity hợp lệ)
- [x] SKILL.md router
- [x] 12 guides 10 sections (01→12)
- [x] assets/css × 12 (generated)
- [x] scripts (generate + validate, adapted từ skill-color-theory)
- [x] README.md (skill list, matrix, affinity tables)
- [x] skills/assets/references.md
- [x] CI workflow + LICENSE + .gitignore
- [x] Validator pass 100%
