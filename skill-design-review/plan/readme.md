# Plan — skill-design-review

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu các skill repo trước — cập nhật: 02/11/2026

## Tổng quan

Skill bộ 12 design-review disciplines (Review Process → Audit Report Template) cho OpenCode:
mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json` machine-readable + CSS spec
tokens (`--rev-*`) + validator CI. Companion repos: `skill-ui-ux` (styleAffinity),
`skill-animation` (motionAffinity), `skill-design-tokens` / `skill-accessibility` /
`skill-component-recipes` / `skill-ux-writing` — các nguồn criteria mà review audit.

## Phân loại 12 disciplines

1. review-process — critique formats, severity scale, ticket loop
2. visual-hierarchy-audit — squint test, scan path, primary action
3. consistency-audit — token adherence, pattern parity, drift map
4. a11y-audit — keyboard/SR/contrast/zoom passes, WCAG findings
5. motion-audit — purpose classification, duration ladder, reduced-motion
6. typography-audit — scale adherence, type crimes
7. spacing-rhythm-audit — 4/8px grid, proximity, alignment
8. interaction-states-audit — full state matrix per element
9. content-microcopy-audit — error completeness, labels, glossary
10. perceived-performance — response bands, skeletons, optimism
11. responsive-audit — size matrix, reflow floor, collapse checks
12. report-template — scorecard, findings table, trend tracking

## Tiến độ

- [x] plan/readme.md
- [x] skills/data.json (12 skills, matrix đối xứng, affinity hợp lệ)
- [x] SKILL.md router
- [x] 12 guides 10 sections (01→12)
- [x] assets/css × 12 (generated)
- [x] scripts (generate + validate, adapted từ skill-ux-writing)
- [x] README.md (skill list, matrix, affinity tables)
- [x] skills/assets/references.md
- [x] CI workflow + LICENSE + .gitignore
- [x] Validator pass 100%
