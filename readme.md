# Design System Skills

Bộ skill thiết kế hoàn chỉnh cho AI agents (OpenCode) — mỗi skill là một repo
độc lập theo cùng convention: router `SKILL.md` + 12 sub-skill guides +
`data.json` machine-readable + CSS tokens + validator CI.

## Hiện trạng

| Repo | Trục | Trạng thái |
|---|---|---|
| [skill-ui-ux](./skill-ui-ux/) | 12 design styles (minimalism → glassmorphism) | ✅ v1.0 |
| [skill-animation](./skill-animation/) | 12 motion disciplines (easing → reduced-motion) | ✅ v1.0 |
| [skill-design-tokens](./skill-design-tokens/) | Design tokens & theming | ✅ v1.0 |
| [skill-accessibility](./skill-accessibility/) | WCAG, ARIA, keyboard, screen reader | ✅ v1.0 |
| [skill-typography](./skill-typography/) | Type scale, pairing, tiếng Việt có dấu | ✅ v1.0 |
| [skill-responsive-layout](./skill-responsive-layout/) | Grid, breakpoints, container queries, layout patterns | ✅ v1.0 |
| [skill-color-theory](./skill-color-theory/) | Harmony, palette từ brand color, data-viz color | ✅ v1.0 |
| [skill-component-recipes](./skill-component-recipes/) | Công thức tables, forms, modals, toasts, command palette | ✅ v1.0 |
| [skill-ux-writing](./skill-ux-writing/) | Microcopy, error messages, voice & tone, i18n | ✅ v1.0 |
| [skill-icons-illustration](./skill-icons-illustration/) | Icon system, illustration direction, SVG | ✅ v1.0 |
| [skill-design-review](./skill-design-review/) | Checklist audit UI theo từng trục | ✅ v1.0 |

Plan chi tiết (12 sub-skills mỗi repo, tiến độ, quy trình build): [plan/readme.md](./plan/readme.md)

## Ưu tiên

Logic: mỗi skill là một trục độc lập, build theo dependency:

1. **Design Tokens** — nền tảng chung, mọi skill khác tiêu thụ tokens
2. **Accessibility** — a11y hiện chỉ rải rác trong skill-ui-ux, cần tầng chuyên sâu
3. **Typography** / **Responsive Layout** — vùng UI cơ bản còn thiếu, agent hỏi nhiều nhất
4. Color → Components → Writing → Icons → **Design Review** (tổng hợp, làm cuối)

## Cách dùng

- Cài skill repo vào agent; router `SKILL.md` sẽ dẫn tới guide đúng theo task.
- Khi task chạm nhiều trục (vd: "làm trang landing đẹp + có motion"):
  ghép guide theo bảng Combination Matrix trong README từng repo
  (✅ ghép tốt · ⚠️ có điều kiện · ❌ không ghép).
- Dữ liệu cấu trúc cho tooling/AI: `skills/data.json` trong mỗi repo.
