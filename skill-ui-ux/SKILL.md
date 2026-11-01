---
name: ui-ux-design-styles
description: Professional UI/UX design style guide covering 12 styles (minimalism, maximalism, flat design, neumorphism, claymorphism, aurora UI, brutalism, collage art, skeuomorphism, retro, class morphism, glassmorphism). Use when designing or building any UI, choosing a design direction, applying a named design style, or reviewing a UI for style consistency.
---

# UI/UX Design Styles — Skill Router

This skill provides 12 curated design-style guides. Each style has a detailed guide with definition, principles, color palette (hex), typography, signature visual elements, real-world use cases, combination notes, anti-patterns, accessibility notes (WCAG contrast), code examples, and an implementation checklist.

## Step 1 — Choose a style

Match the product/brand context to a style:

| Style | Best for | Avoid for |
|---|---|---|
| Minimalism | SaaS, fintech, dashboards, premium brands | Entertainment, youth brands |
| Maximalism | Entertainment, fashion/streetwear, campaigns | Data-dense tools, banking |
| Flat Design | Cross-platform apps, dashboards, corporate sites | Products needing depth/texture appeal |
| Neumorphism | Fitness/wellness, IoT controls, light portfolios | Data-heavy dashboards, accessibility-critical UI |
| Claymorphism | iOS/macOS widgets, health apps, playful dashboards | Large data tables, dense enterprise UI |
| Aurora UI | OS-level UI, streaming/gaming, premium AI/Web3 landing | Print-like content, long-form reading |
| Brutalism UI | Creative portfolios, dev tools, rebellious brands | Banking, healthcare, enterprise |
| Collage Art | Editorial/magazines, art brands, event landing | Productivity tools, data UI |
| Skeuomorphism | Audio/music apps, games, nostalgic products | Modern minimal products, high-density UI |
| Retro | Indie games, vintage brands, nostalgia campaigns | Modern SaaS, enterprise software |
| Class Morphism | Luxury brands, real estate, weddings, premium editorial | Utility apps, youth brands |
| Glassmorphism | Media overlays, maps/weather, hero sections, control panels | Flat white backgrounds, dense data tables |

If the user names a style explicitly (e.g., "neumorphic", "glassmorphism", "brutalist"), go straight to its guide.

## Step 2 — Read the style guide

Each style guide lives in `skills/<NN-<style>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Design Principles — mandatory rules
3. Suggested Color Palette — hex codes + role of each color
4. Typography — font pair + reference sizes
5. Signature Visual Elements — shapes, effects, textures
6. Real-World Use Cases — suitable industries/products
7. Combination Notes — pairing tips with other styles
8. Anti-Patterns — common mistakes that violate the style (incl. accessibility notes with WCAG contrast)
9. Code Examples — complete HTML+CSS snippets using the style's palette and tokens
10. Implementation Checklist — pre-delivery quality checks (contrast, color budget, grid, motion)

| # | Style | Guide |
|---|-------|-------|
| 1 | Minimalism | [skills/01-minimalism/SKILL.md](./skills/01-minimalism/SKILL.md) |
| 2 | Maximalism | [skills/02-maximalism/SKILL.md](./skills/02-maximalism/SKILL.md) |
| 3 | Flat Design | [skills/03-flat-design/SKILL.md](./skills/03-flat-design/SKILL.md) |
| 4 | Neumorphism | [skills/04-neumorphism/SKILL.md](./skills/04-neumorphism/SKILL.md) |
| 5 | Claymorphism | [skills/05-claymorphism/SKILL.md](./skills/05-claymorphism/SKILL.md) |
| 6 | Aurora UI | [skills/06-aurora-ui/SKILL.md](./skills/06-aurora-ui/SKILL.md) |
| 7 | Brutalism UI | [skills/07-brutalism-ui/SKILL.md](./skills/07-brutalism-ui/SKILL.md) |
| 8 | Collage Art | [skills/08-collage-art/SKILL.md](./skills/08-collage-art/SKILL.md) |
| 9 | Skeuomorphism | [skills/09-skeuomorphism/SKILL.md](./skills/09-skeuomorphism/SKILL.md) |
| 10 | Retro | [skills/10-retro/SKILL.md](./skills/10-retro/SKILL.md) |
| 11 | Class Morphism | [skills/11-class-morphism/SKILL.md](./skills/11-class-morphism/SKILL.md) |
| 12 | Glassmorphism | [skills/12-glassmorphism/SKILL.md](./skills/12-glassmorphism/SKILL.md) |

## Step 3 — Apply

- Use the style's **hex palette + font pair + visual rules** as hard standards when generating designs, code, or Figma specs.
- Respect the **Anti-Patterns** section — these are the mistakes that most often make a style look wrong.
- Check the **Combination Matrix** in [README.md](./README.md) before mixing two styles: ✅ combines well, ⚠️ conditional (follow the pairing tips in section 7), ❌ do not combine.

## Machine-Readable Data

For programmatic use (design linting, design-token generation, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 styles as structured JSON with a fully symmetric combination matrix and precomputed WCAG contrast data:

```json
{ "styles": [{ "id": "neumorphism", "sections": { "palette": [...], "combinations": {...}, "antiPatterns": [...], "contrast": { "pairs": [...], "notes": "..." } } }] }
```

## Version

- **Schema version:** 1.1 (xem `skills/data.json` → `meta.version`) — v1.1 adds `sections.contrast` (precomputed WCAG contrast pairs + notes) to every style and sections 9–10 (Code Examples, Implementation Checklist) to every guide
- **Styles:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `styles[].id`)
- **Compatibility:** hoạt động độc lập, không phụ thuộc framework; CSS tokens ở `assets/css/` dùng CSS custom properties chuẩn (mọi browser hiện đại), sinh lại bằng `scripts/generate_css_tokens.py`
- **Changelog:** xem [plan/readme.md](./plan/readme.md)

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated Figma Community search links, real-world reference sites, stock asset sources, and quick-start CSS tokens per style: [`skills/assets/figma-references.md`](./skills/assets/figma-references.md).
