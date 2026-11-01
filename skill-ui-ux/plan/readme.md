# Plan — skill-ui-ux

> Kế hoạch nâng cấp chuẩn enterprise — cập nhật: 28/10/2026

## Tổng quan

Skill bộ 12 design styles (Minimalism → Glassmorphism) cho OpenCode: mỗi style
có SKILL.md đầy đủ 8 sections + `data.json` machine-readable + validator CI.

## Đánh giá

| Hạng mục | Kết quả |
|----------|---------|
| 12 SKILL.md — đủ 8 sections chuẩn | ✅ Pass |
| data.json hợp lệ, 12 styles | ✅ |
| Anti-patterns khớp giữa JSON ↔ MD | ✅ |
| 91 palette hex hợp lệ | ✅ |
| Ma trận combination đối xứng | ✅ |
| Figma URLs well-formed | ✅ |
| `scripts/validate_skills.py` CI check | ✅ Có sẵn, pass toàn bộ |

## Vấn đề phát hiện & đã sửa

1. **[BUG-DOCS] Schema data.json bị mô tả sai trong README.md + root SKILL.md**
   - Docs hứa: `{ "styles": [{ "id", "palette", "combinations", "antiPatterns" }] }`
   - Thực tế: các field nằm trong `styles[].sections.*`
   - Hậu quả: AI agent đọc theo spec sẽ nhận `undefined` → fail silently
   - **Fix:** cập nhật JSON snippet trong `README.md` + `SKILL.md` phản ánh đúng schema `sections: { palette, combinations, antiPatterns }`

## Kiểm chứng

```
python3 scripts/validate_skills.py  →  All checks passed ✓
```

## Backlog đề xuất

- [x] GitHub Actions workflow chạy `validate_skills.py` tự động (`.github/workflows/validate.yml`)
- [x] Thêm ví dụ CSS tokens khởi động cho từng style vào `assets/`
- [x] Kiểm tra tương thích phiên bản: thêm section "Version" vào root SKILL.md

### Chi tiết vòng 29/10

- `assets/css/<style-id>.css` × 12: starter tokens sinh từ `skills/data.json`
  (nguồn truth) — mỗi hex kèm role + notes, font tokens từ typography section
- `scripts/validate_skills.py` thêm **check #8**: file token phải tồn tại cho
  mọi style, hex phải khớp data.json (chống drift), không có file thừa.
  Đã test negative case: sửa hex → FAIL; restore → pass
- `SKILL.md`: thêm section **Version** (schema version, styles count,
  compatibility, hướng dẫn bump version khi đổi schema)
- `figma-references.md`: liên kết tới full token files

### Chi tiết vòng 29/10 (lần 2 — sections 9/10 + contrast + validator thật)

- `scripts/validate_skills.py`: check #6 giờ là so sánh THẬT — parse ký hiệu
  ma trận README (✅/⚠️/❌/—) từng cell, đối chiếu với `data.combinations` của
  từng style, bắt thiếu cell (phủ đủ 12×12), bắt lệch đối xứng, exit 1 khi mismatch.
  Check #5 cũng được sửa: vòng lặp cũ dùng `sid in good` (luôn false) nên
  reciprocity chưa bao giờ chạy — giờ kiểm good↔good / caution↔caution /
  avoid↔avoid (132 entries, 0 lệch). Biến `SKIP_STYLES` không dùng đã bị xóa.
  Check #9: `.DS_Store` nay là FAIL (validator tự xóa file tìm thấy); thiếu
  coverage .gitignore cũng FAIL. Thêm **check #10**: mọi SKILL.md phải có
  section 9 + 10; `data.json` phải có `sections.contrast` (≥2 pairs có ratio).
- `scripts/add_contrast.py` chạy lần đầu: thêm `sections.contrast` (WCAG
  relative luminance, 2 pairs/style) + `notes` cho 12 styles; `meta.version`
  → 1.1. Hai ghi chú được sửa cho đúng số liệu: retro (#D01F1F chỉ đạt 4.43:1 →
  đổi khuyến nghị sang #B91C1C = 5.32:1), glassmorphism note nêu rõ ngưỡng 4.5:1.
- `skills/*/SKILL.md` × 12: thêm **9. Code Examples** (1–2 snippet HTML+CSS
  hoàn chỉnh dùng đúng palette/font + token file), **10. Implementation
  Checklist** (5–7 items), và **Accessibility Notes** (bảng contrast + lưu ý
  prefers-reduced-motion cho aurora/retro/collage, prefers-reduced-transparency
  cho glass/class-morphism, focus-visible cho các style không dùng border).
- `scripts/generate_css_tokens.py` (mới): sinh lại 12 file `assets/css/*.css`
  từ data.json — format giữ nguyên như bản cũ, kèm block comment contrast
  (PASS/FAIL từng pair). Chạy idempotent, đã verify.
- `README.md` + root `SKILL.md`: cập nhật mô tả từ 8 → 10 sections, schema
  version 1.1, ví dụ JSON có `contrast`.
- Validator: PASS 100% (10/10 checks).
