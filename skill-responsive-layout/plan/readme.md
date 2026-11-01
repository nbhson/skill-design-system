# Plan — skill-responsive-layout

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu các skill repo trước — cập nhật: 02/11/2026

## Tổng quan

Skill bộ 12 responsive-layout disciplines (Grid Systems → Responsive Testing & QA) cho OpenCode:
mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json` machine-readable + CSS spec
tokens (`--layout-*`) + validator CI. Companion repos: `skill-ui-ux` (styleAffinity),
`skill-animation` (motionAffinity), `skill-design-tokens` (spacing/grid contracts).

## Phân loại 12 disciplines

1. grid-systems — 12-col, gutters, max-width, margin tiers
2. breakpoints-strategy — mobile-first, content-driven tiers (640→1536)
3. fluid-container-queries — @container, cqi units, compact/standard/expanded
4. flexbox-patterns — nav, media object, toolbar, truncation, rails
5. css-grid-patterns — template-areas shells, auto-fill minmax, subgrid
6. layout-compositions — sidebar/split/stack/cluster/bento/holy-grail catalog
7. responsive-images — srcset/sizes, picture, AVIF/WebP, lazy/LCP, zero CLS
8. mobile-navigation — bottom bar, drawers, thumb zone, 44px targets
9. data-tables-responsive — priority columns, sticky scroll, card fallback
10. intrinsic-design — min/max/fit-content, clamp, Every Layout, query budget
11. rtl-i18n-layout — logical properties, RTL mirroring, text expansion, locales
12. responsive-testing — viewport matrix, visual regression, zoom/RTL/locale passes

## Tiến độ

- [x] plan/readme.md
- [x] skills/data.json (12 skills, matrix đối xứng, affinity hợp lệ)
- [x] SKILL.md router
- [x] 12 guides 10 sections (01→12)
- [x] assets/css × 12 (generated)
- [x] scripts (generate + validate, adapted từ skill-typography)
- [x] README.md (skill list, matrix, affinity tables)
- [x] skills/assets/references.md
- [x] CI workflow + LICENSE + .gitignore
- [x] Validator pass 100%
