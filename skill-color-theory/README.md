# 🎨 Professional Color Theory Skill Set — 12 Color Disciplines

A professional reference guide for 12 color disciplines, each covering: definition, core principles, spec tokens (policies/thresholds/contracts), composition, signature patterns, real-world applications, combination notes, anti-patterns, accessibility notes, code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles), **skill-animation** (12 motion disciplines), **skill-design-tokens** (12 token disciplines). This repo answers *"what do the colors mean and how are they built?"* — the palette layer beneath the token system. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Color Harmony & Schemes](./skills/01-color-harmony/SKILL.md) | 01-color-harmony | The classical scheme machinery - complementary, analogous, triadic, split-complementary - applied as starting constraints, not rules. |
| 2 | [OKLCH & Perceptual Spaces](./skills/02-oklch-perceptual/SKILL.md) | 02-oklch-perceptual | Working in perceptually uniform spaces: OKLCH/OKLab for ramp math, interpolation, and adjustments that look how the numbers say they look. |
| 3 | [Color Psychology & Brand Fit](./skills/03-color-psychology/SKILL.md) | 03-color-psychology | What hues signal and when signals misfire: emotion, category conventions, and matching brand personality to palette temperature. |
| 4 | [Gray Ramps & Tinted Neutrals](./skills/04-gray-ramp-neutrals/SKILL.md) | 04-gray-ramp-neutrals | Building the neutral backbone: pure gray vs tinted gray philosophy, elevation steps, and the chroma whisper that ties neutrals to the brand. |
| 5 | [Brand Ramp Construction](./skills/05-brand-ramp-construction/SKILL.md) | 05-brand-ramp-construction | One brand hue becomes a 9-11 step ramp: chroma curves, lightness anchors, and the per-step contrast contracts that make it usable. |
| 6 | [Semantic Status & Feedback Color](./skills/06-semantic-color-system/SKILL.md) | 06-semantic-color-system | Success, warning, danger, info - the conventional status hues, their ramps, multi-signal delivery, and protection from brand drift. |
| 7 | [Dark Mode Palette](./skills/07-dark-mode-palette/SKILL.md) | 07-dark-mode-palette | Dark themes as designed, not inverted: desaturated tints, lightness-scaled elevation, and surface roles that survive low-light viewing. |
| 8 | [Data Visualization Palettes](./skills/08-data-viz-palettes/SKILL.md) | 08-data-viz-palettes | Categorical, sequential, and diverging palettes built for comprehension: distinguishability, colorblind safety, and 3:1 against surfaces. |
| 9 | [Gradient Design](./skills/09-gradient-theory/SKILL.md) | 09-gradient-theory | Gradients as designed objects: interpolation space, stop placement, hue travel, and the modern mesh/aurora looks without mud or banding. |
| 10 | [Contrast Models & Math](./skills/10-contrast-models/SKILL.md) | 10-contrast-models | WCAG luminance ratios vs APCA: what each model measures, when each applies, and the computation discipline behind every validated pairing. |
| 11 | [Color Vision Deficiency Safety](./skills/11-cvd-safe-design/SKILL.md) | 11-cvd-safe-design | Designing for the 8% who see color differently: CVD types, simulation testing, safe hue pairs, and palettes that survive deuteranopia. |
| 12 | [Cultural Color Meaning](./skills/12-cultural-color-meaning/SKILL.md) | 12-cultural-color-meaning | Color connotations by market: red's three meanings, white's weddings and funerals, and localization discipline for global palettes. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, spec tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "brand-ramp-construction",
    "sections": {
      "tokens": [{ "role": "ramp-step-count", "value": "11", "notes": "..." }],
      "combinations": { "good": [], "caution": [], "avoid": [] },
      "styleAffinity": { "good": [], "caution": [], "avoid": [] },
      "motionAffinity": { "good": [], "caution": [], "avoid": [] },
      "antiPatterns": ["..."],
      "accessibility": { "required": true, "notes": "...", "fallback": "..." }
    }
  }]
}
```

## 📚 References

[`assets/references.md`](./skills/assets/references.md) — curated spec links (OKLCH, color gamuts), tool docs (Sim Daltonism, viridis palettes), and color theory learning resources.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the color task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** treat the spec tokens from `assets/css/<skill-id>.css` as hard standards — ramps are generated curves with per-step contracts. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | harmony | oklch | psy | gray | ramp | semantic | dark | viz | gradient | contrast | cvd | culture |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Color Harmony & Schemes** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **OKLCH & Perceptual Color Spaces** | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Color Psychology & Brand Fit** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Gray Ramps & Tinted Neutrals** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Brand Ramp Construction** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Semantic Status & Feedback Color** | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Dark Mode Palette** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Data Visualization Palettes** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **Gradient Design** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ |
| **Contrast Models & Math** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **Color Vision Deficiency Safety** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| **Cultural Color Meaning** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux / skill-design-tokens)

| Skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Color Harmony & Schemes | minimalism, flat-design, maximalism | skeuomorphism |
| OKLCH & Perceptual Color Spaces | minimalism, flat-design, aurora-ui | retro |
| Color Psychology & Brand Fit | minimalism, flat-design, retro | brutalism-ui |
| Gray Ramps & Tinted Neutrals | minimalism, flat-design, glassmorphism | — |
| Brand Ramp Construction | minimalism, flat-design, class-morphism | collage-art |
| Semantic Status & Feedback Color | minimalism, flat-design | collage-art, brutalism-ui |
| Dark Mode Palette | glassmorphism, aurora-ui, minimalism | skeuomorphism |
| Data Visualization Palettes | minimalism, flat-design, class-morphism | collage-art |
| Gradient Design | aurora-ui, glassmorphism, maximalism | minimalism, brutalism-ui |
| Contrast Models & Math | minimalism, flat-design | collage-art, maximalism |
| Color Vision Deficiency Safety | minimalism, flat-design | collage-art |
| Cultural Color Meaning | minimalism, flat-design, retro | collage-art |

## 🏃 Motion Affinity (skill-animation)

| Skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| Color Harmony & Schemes | easing-timing, entrance-exit | — |
| OKLCH & Perceptual Color Spaces | easing-timing, data-animation | — |
| Color Psychology & Brand Fit | micro-interactions, feedback-confirmation | — |
| Gray Ramps & Tinted Neutrals | easing-timing | — |
| Brand Ramp Construction | easing-timing, feedback-confirmation | — |
| Semantic Status & Feedback Color | feedback-confirmation, micro-interactions | — |
| Dark Mode Palette | easing-timing, ambient-motion | — |
| Data Visualization Palettes | data-animation | ambient-motion |
| Gradient Design | ambient-motion, easing-timing | — |
| Contrast Models & Math | easing-timing | — |
| Color Vision Deficiency Safety | easing-timing | — |
| Cultural Color Meaning | feedback-confirmation | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--clr-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene
