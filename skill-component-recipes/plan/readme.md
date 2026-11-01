# Plan — skill-component-recipes

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu các skill repo trước — cập nhật: 02/11/2026

## Tổng quan

Skill bộ 12 component-recipe disciplines (Buttons & Badges → Component A11y Wiring) cho OpenCode:
mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json` machine-readable + CSS spec
tokens (`--comp-*`) + validator CI. Companion repos: `skill-ui-ux` (styleAffinity),
`skill-animation` (motionAffinity), `skill-design-tokens` (color/radius/spacing contracts),
`skill-accessibility` (criteria layer), `skill-ux-writing` (copy layer).

## Phân loại 12 disciplines

1. buttons-badges — variants, sizes, loading/disabled contracts, badges
2. forms-inputs — field wiring, validation timing, choice semantics
3. tables-data-grid — sort/filter/select, native table vs ARIA grid
4. modals-dialogs — dialog contract, focus trap-and-return, when-to-modal
5. toasts-notifications — aria-live, timing, stacking, undo pattern
6. navigation-patterns — top bar, sidebar, breadcrumbs, pagination
7. cards-lists — anatomy slots, media-object, stretched-link recipe
8. tabs-accordions — APG disclosure widgets, URL state
9. dropdowns-menus — value-vs-action, combobox, popovers, tooltips
10. command-palette — Cmd-K, typed index, frecency, analytics
11. empty-loading-error — skeleton discipline, empty taxonomy, recovery
12. accessibility-wiring — per-component a11y checklist gate

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
