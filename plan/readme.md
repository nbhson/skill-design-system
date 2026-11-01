# Plan tổng — Design System Skills

> Kế hoạch mở rộng từ 2 skill (ui-ux, animation) lên bộ 11 skill design system hoàn chỉnh.
> Cập nhật: 01/11/2026

## Mục tiêu

Xây dựng đầy đủ bộ skill thiết kế cho AI agents theo đúng convention hiện có
(mỗi repo = 1 trục độc lập, 12 sub-skills, router + data.json + CSS tokens + validator CI).

## Hiện trạng

| Repo | Trục | Trạng thái |
|---|---|---|
| `skill-ui-ux` | 12 design styles | ✅ Hoàn thành (v1.0) |
| `skill-animation` | 12 motion disciplines | ✅ Hoàn thành (v1.0) |
| 9 repos còn lại | xem roadmap trong [readme.md](../readme.md) | 📋 Đã lên kế hoạch |

## Chuẩn cấu trúc mỗi skill repo (bắt buộc)

```
skill-<name>/
├── SKILL.md                      # router: frontmatter (name, description) + Step 1/2/3
├── README.md                     # tổng quan + Combination Matrix (✅/⚠️/❌ khớp data.json)
├── skills/
│   ├── data.json                 # machine-readable: meta + sections per skill + combinations
│   ├── assets/references.md      # link spec, tool docs, inspiration
│   └── NN-<id>/SKILL.md  × 12    # chuẩn 10 sections, frontmatter name/tags/related
├── assets/css/<id>.css           # tokens chuẩn hoá (CSS custom properties)
├── scripts/
│   ├── validate_skills.py        # 10 checks CI (khớp data.json ↔ SKILL.md ↔ README ↔ CSS)
│   └── generate_css_tokens.py    # sinh lại tokens từ data.json
├── .github/workflows/validate.yml
├── plan/readme.md                # plan khởi tạo của repo
├── LICENSE
└── .gitignore
```

### Chuẩn 10 sections trong từng guide

1. Definition — 2–3 câu
2. Core Principles — quy tắc bắt buộc
3. Tokens — giá trị chuẩn + vai trò từng giá trị
4. Choreography / Composition — thứ tự, phối hợp
5. Signature Patterns — 2–3 pattern kinh điển
6. Real-World Use Cases
7. Combination Notes — ghép với skill cùng repo + `styleAffinity` sang skill-ui-ux / skill-animation
8. Anti-Patterns (kèm Accessibility Notes)
9. Code Examples — HTML+CSS (±JS) hoàn chỉnh, dùng tokens của skill
10. Implementation Checklist

### Liên kết chéo giữa các repo

- Mỗi `data.json` khai báo `meta.companionRepos` và `sections.styleAffinity` (towards ui-ux styles) / `motionAffinity` (towards animation disciplines).
- Router SKILL.md ở mỗi repo có bảng "When to use this repo vs companion repos".
- Validator phải check tính đối xứng của combination graph + khớp matrix trong README.

## Roadmap 9 skill còn lại — 3 đợt build

### Wave 1 — Nền tảng (chặn đường các skill sau)

| # | Repo | 12 sub-skills | Ghi chú |
|---|---|---|---|
| 1 | `skill-design-tokens` | color-tokens, typography-tokens, spacing-sizing, radius-elevation, semantic-alias-naming, dark-mode, multi-brand-theming, contrast-validation, platform-mapping, token-pipeline-figma, component-tokens, governance-migration | "Chất keo" nối mọi skill; làm đầu tiên |
| 2 | `skill-accessibility` | wcag-fundamentals, color-contrast, keyboard-navigation, focus-management, aria-fundamentals, aria-patterns-widgets, forms-errors, screen-readers, media-alt-text, cognitive-content, zoom-reflow, testing-audit | Tách sâu từ a11y đang rải trong skill-ui-ux |
| 3 | `skill-typography` | font-pairing, type-scale, line-height, letter-spacing, visual-hierarchy, fluid-responsive, multilingual-vietnamese, readability-legibility, webfont-loading, numeric-tabular, variable-fonts, accessible-typography | Bao gồm case tiếng Việt có dấu |

### Wave 2 — Bề mặt UI

| # | Repo | 12 sub-skills | Ghi chú |
|---|---|---|---|
| 4 | `skill-responsive-layout` | grid-systems, breakpoints-strategy, fluid-container-queries, flexbox-patterns, css-grid-patterns, layout-compositions, responsive-images, mobile-navigation, data-tables-responsive, intrinsic-design, rtl-i18n-layout, responsive-testing | Vùng agent hỏi nhiều nhất |
| 5 | `skill-color-theory` | color-fundamentals-oklch, harmony-rules, palette-from-brand, semantic-colors, dark-mode-palettes, contrast-automation, color-psychology, cultural-meaning, gradients-mesh, data-viz-color, accessible-color-systems, palette-audit | Phần "tự tạo palette" mà skill-ui-ux chưa có |
| 6 | `skill-component-recipes` | buttons, forms-inputs, tables, modals-dialogs, toasts-notifications, navigation-menus, command-palettes, cards-lists, tabs-accordions, dropdowns-selects, date-pickers, charts-timelines | Công thức chi tiết; phụ thuộc design-tokens + ui-ux + animation |

### Wave 3 — Nội dung & hệ thống

| # | Repo | 12 sub-skills | Ghi chú |
|---|---|---|---|
| 7 | `skill-ux-writing` | writing-principles, button-labels, error-messages, empty-states, onboarding-copy, component-microcopy, notifications, forms-labels, voice-tone, localization-i18n, accessible-writing, copy-audit | Microcopy tách khỏi skill-ui-ux |
| 8 | `skill-icons-illustration` | icon-style-selection, icon-grid-sizing, icon-library-management, icon-usability, accessible-icons, illustration-direction, empty-error-illustrations, mascot-character, svg-optimization, animation-integration, favicon-app-icons, icon-system-audit | `animation-integration` liên kết skill-animation |
| 9 | `skill-design-review` | review-process, visual-hierarchy-audit, consistency-audit, a11y-audit, motion-audit, typography-audit, spacing-rhythm-audit, interaction-states-audit, content-microcopy-audit, perceived-performance, responsive-audit, report-template | Làm cuối — tổng hợp checklist audit từ mọi skill trên |

## Tiến độ build

| Repo | Plan | Router SKILL.md | 12 guides | data.json | CSS tokens | Validator + CI | README matrix |
|---|---|---|---|---|---|---|---|
| design-tokens | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| accessibility | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| typography | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| responsive-layout | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| color-theory | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| component-recipes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ux-writing | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| icons-illustration | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| design-review | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Quy trình build 1 repo (lặp lại cho từng skill)

1. `plan/readme.md` — chốt 12 sub-skills, tokens, affinity
2. `SKILL.md` router + `skills/data.json` (đủ sections, combination matrix đối xứng)
3. 12 guide `skills/NN-<id>/SKILL.md` theo 10 sections (viết theo cụm 3–4 guide/lượt)
4. `assets/css/*.css` + `scripts/generate_css_tokens.py`
5. `scripts/validate_skills.py` (10 checks) + CI workflow
6. README.md Combination Matrix + references.md + LICENSE + .gitignore
7. Chạy validator pass 100% trước khi chuyển repo kế tiếp

## Tiêu chí hoàn thành bộ

- 11 repos, mỗi repo validator CI pass, matrix khớp data.json
- Mỗi repo liên kết `styleAffinity`/`motionAffinity` chéo với các repo liên quan
- Root readme.md cập nhật trạng thái sau mỗi repo hoàn thành
