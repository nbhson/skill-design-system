# 🎨 Professional UI/UX Skill Set — 12 Design Styles

A professional reference guide for 12 UI/UX design styles, each with full coverage of: definition, design principles, color palette (hex), typography, visual elements, real-world applications, combination notes, anti-patterns, accessibility notes (WCAG contrast), code examples, and an implementation checklist.

## 📂 Skill List

| # | Style | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Minimalism](./skills/01-minimalism/SKILL.md) | 01-minimalism | Less is more — white space, single focal point, strict grid |
| 2 | [Maximalism](./skills/02-maximalism/SKILL.md) | 02-maximalism | More is more — vibrant colors, patterns, bold typography |
| 3 | [Flat Design](./skills/03-flat-design/SKILL.md) | 03-flat-design | Pure 2D — flat colors, no heavy gradients, no shadows |
| 4 | [Neumorphism](./skills/04-neumorphism/SKILL.md) | 04-neumorphism | Soft UI — symmetrical shadows, same hue, soft tactile feel |
| 5 | [Claymorphism](./skills/05-claymorphism/SKILL.md) | 05-claymorphism | Clay material — internal gradients, super-rounded, corner highlight |
| 6 | [Aurora UI](./skills/06-aurora-ui/SKILL.md) | 06-aurora-ui | Aurora borealis — multi-layer gradients, high blur, smooth motion |
| 7 | [Brutalism UI](./skills/07-brutalism-ui/SKILL.md) | 07-brutalism-ui | Raw, bare — thick black borders, system fonts, bright colors |
| 8 | [Collage Art](./skills/08-collage-art/SKILL.md) | 08-collage-art | Cut-and-paste — multi-layer, textures, diverse typography |
| 9 | [Skeuomorphism](./skills/09-skeuomorphism/SKILL.md) | 09-skeuomorphism | Mimic real materials — leather, wood, metal, clear depth |
| 10 | [Retro](./skills/10-retro/SKILL.md) | 10-retro | Past decades — 50s/70s/80s/90s, era-specific palettes |
| 11 | [Class Morphism](./skills/11-class-morphism/SKILL.md) | 11-class-morphism | Classic + Morphic — golden ratio, warm palette, serif typography |
| 12 | [Glassmorphism](./skills/12-glassmorphism/SKILL.md) | 12-glassmorphism | Frosted glass — transparency, backdrop blur, 1px light border |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, palettes, typography, combinations, anti-patterns, precomputed WCAG contrast pairs, tags). The root [`SKILL.md`](./SKILL.md) also serves as a router for AI agents to identify the right style and drill into the appropriate guide.

```json
{
  "styles": [{
    "id": "neumorphism",
    "sections": {
      "palette": [{ "role": "...", "hex": "#..." }],
      "combinations": { "good": [...], "caution": [...], "avoid": [...] },
      "antiPatterns": ["..."]
    }
  }]
}
```

## 🖼 References & Inspiration

[`assets/figma-references.md`](./skills/assets/figma-references.md) — curated Figma Community search links, real-world reference sites, stock asset sources, and quick-start CSS tokens for each style.

## 🎯 How to Use

1. **Select a style:** use the summary table to choose the skill that fits your product/brand.
2. **Read SKILL.md:** each file follows 10 standard sections (definition → principles → colors → font → visual → applications → combinations → anti-patterns → code examples → implementation checklist).
3. **Apply:** use the hex palette + font pair + visual rules as standards when designing. For AI agents: use the root `SKILL.md` router to select a style, then the appropriate `SKILL.md` guide for detailed implementation.

## 🤖 AI Agent Usage

The root [`SKILL.md`](./SKILL.md) acts as a skill router — it describes all 12 styles, their ideal use cases, and links to individual guides. Load it when the task involves UI/UX design, style selection, or design review. Each style's `SKILL.md` file follows a 10-section standard, including accessibility notes with precomputed WCAG contrast pairs (available in `data.json` under `sections.contrast`).

## 🔄 Quick Combination Matrix

| | min | max | flat | neu | clay | aurora | brutal | collage | skeuo | retro | class | glass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Minimalism** | — | ❌ | ✅ | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ✅ |
| **Maximalism** | ❌ | — | ❌ | ❌ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | ⚠️ | ❌ | ⚠️ |
| **Flat Design** | ✅ | ❌ | — | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| **Neumorphism** | ⚠️ | ❌ | ⚠️ | — | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ✅ | ⚠️ |
| **Claymorphism** | ⚠️ | ⚠️ | ⚠️ | ❌ | — | ⚠️ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ✅ |
| **Aurora UI** | ✅ | ⚠️ | ✅ | ⚠️ | ⚠️ | — | ❌ | ⚠️ | ❌ | ❌ | ✅ | ✅ |
| **Brutalism UI** | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | — | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Collage Art** | ❌ | ✅ | ❌ | ❌ | ❌ | ⚠️ | ✅ | — | ❌ | ⚠️ | ❌ | ⚠️ |
| **Skeuomorphism** | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | — | ✅ | ⚠️ | ❌ |
| **Retro** | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ✅ | ⚠️ | ✅ | — | ⚠️ | ❌ |
| **Class Morphism** | ⚠️ | ❌ | ⚠️ | ✅ | ⚠️ | ✅ | ❌ | ❌ | ⚠️ | ⚠️ | — | ✅ |
| **Glassmorphism** | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ❌ | ⚠️ | ❌ | ❌ | ✅ | — |
