# 🎨 Professional Design Token Skill Set — 12 Token Disciplines

A professional reference guide for 12 design-token disciplines, each covering: definition, core principles, token set (role/value/notes), composition & layering, signature patterns, real-world applications, combination notes, anti-patterns, accessibility contracts (WCAG contrast), code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles — *"how should it look?"*) and **skill-animation** (12 motion disciplines — *"how should it move?"*). This repo answers *"what are the legal values?"* — the token layer both companions consume. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Color Token Scales](./skills/01-color-tokens/SKILL.md) | 01-color-tokens | Primitive color scales built as perceptually-even ramps (neutral, brand, feedback), the raw material every semantic color decision draws from. |
| 2 | [Typography Token System](./skills/02-typography-tokens/SKILL.md) | 02-typography-tokens | Font families, a modular type scale, weights, and line-height tokens that make text hierarchy systematic instead of per-screen improvisation. |
| 3 | [Spacing & Sizing Tokens](./skills/03-spacing-sizing/SKILL.md) | 03-spacing-sizing | A 4px-base spacing scale, icon sizing, and touch-target minimums that give every layout decision a legal value. |
| 4 | [Radius & Elevation Tokens](./skills/04-radius-elevation/SKILL.md) | 04-radius-elevation | Border-radius steps, shadow elevation levels, and z-index layers — the depth system that says what floats above what. |
| 5 | [Semantic & Alias Naming](./skills/05-semantic-alias-naming/SKILL.md) | 05-semantic-alias-naming | The three-tier naming architecture — primitive, semantic alias, component — that lets themes swap values without code ever changing. |
| 6 | [Dark Mode Theming](./skills/06-dark-mode/SKILL.md) | 06-dark-mode | Re-pointing semantic aliases into a dark theme: surface inversion, elevation physics, saturation control, and contrast that survives inversion. |
| 7 | [Multi-Brand Theming](./skills/07-multi-brand-theming/SKILL.md) | 07-multi-brand-theming | White-label theming at the alias tier: per-brand primitive overrides, locked shared vocabulary, and a brand matrix that does not explode. |
| 8 | [Contrast Validation](./skills/08-contrast-validation/SKILL.md) | 08-contrast-validation | WCAG contrast as a token property: annotated scales, validated alias pairings, and automated checks that fail the build on regressions. |
| 9 | [Cross-Platform Mapping](./skills/09-platform-mapping/SKILL.md) | 09-platform-mapping | One token source translated to CSS custom properties, iOS, Android, and utility frameworks — with values that survive unit and paradigm differences. |
| 10 | [Token Pipeline & Figma Sync](./skills/10-token-pipeline-figma/SKILL.md) | 10-token-pipeline-figma | Design-tool-to-code automation: Figma variables as the source, W3C DTCG as the interchange format, CI as the referee. |
| 11 | [Component Tokens](./skills/11-component-tokens/SKILL.md) | 11-component-tokens | Per-component token slots (component-button-bg, component-input-border) derived from aliases — the layer that gives components flexibility without forking the system. |
| 12 | [Governance & Migration](./skills/12-governance-migration/SKILL.md) | 12-governance-migration | The process layer: contribution rules, semantic versioning, deprecation windows, linting, and adoption tracking that keep the token system alive. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "color-tokens",
    "sections": {
      "tokens": [{ "role": "color-brand-500", "value": "#2563EB", "notes": "..." }],
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

[`assets/references.md`](./skills/assets/references.md) — curated spec links (W3C Design Tokens Community Group, WCAG contrast, CSS custom properties), tool docs (Style Dictionary, Tokens Studio, Figma variables), and color/contrast tooling.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the token task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** consume the tokens from `assets/css/<skill-id>.css` as hard standards — components reference `var(--dt-*)` aliases, never raw values. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | color | typo | space | radius | naming | dark | brand | contrast | platform | pipeline | component | gov |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Color Token Scales** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ |
| **Typography Token System** | ✅ | — | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ✅ |
| **Spacing & Sizing Tokens** | ✅ | ✅ | — | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Radius & Elevation Tokens** | ✅ | ⚠️ | ✅ | — | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ |
| **Semantic & Alias Naming** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Dark Mode Theming** | ✅ | ✅ | ⚠️ | ✅ | ✅ | — | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Multi-Brand Theming** | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | — | ✅ | ⚠️ | ✅ | ❌ | ✅ |
| **Contrast Validation** | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **Cross-Platform Mapping** | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | — | ✅ | ⚠️ | ✅ |
| **Token Pipeline & Figma Sync** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **Component Tokens** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ⚠️ | ✅ | — | ✅ |
| **Governance & Migration** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux)

| Token skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Color Token Scales | minimalism, flat-design, glassmorphism | collage-art, brutalism-ui |
| Typography Token System | minimalism, flat-design, class-morphism | collage-art, maximalism |
| Spacing & Sizing Tokens | minimalism, flat-design | maximalism, collage-art |
| Radius & Elevation Tokens | claymorphism, neumorphism, glassmorphism | brutalism-ui, flat-design |
| Semantic & Alias Naming | minimalism, flat-design | collage-art, maximalism |
| Dark Mode Theming | minimalism, aurora-ui, glassmorphism | skeuomorphism |
| Multi-Brand Theming | minimalism, flat-design | retro, skeuomorphism |
| Contrast Validation | minimalism, flat-design, glassmorphism | brutalism-ui, collage-art |
| Cross-Platform Mapping | flat-design, minimalism | skeuomorphism, neumorphism |
| Token Pipeline & Figma Sync | minimalism, flat-design | collage-art, skeuomorphism |
| Component Tokens | minimalism, flat-design, glassmorphism | collage-art, brutalism-ui |
| Governance & Migration | minimalism, flat-design | maximalism, collage-art |

## 🏃 Motion Affinity (skill-animation)

| Token skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| Color Token Scales | easing-timing, data-animation | ambient-motion |
| Typography Token System | easing-timing | ambient-motion |
| Spacing & Sizing Tokens | entrance-exit, easing-timing | — |
| Radius & Elevation Tokens | feedback-confirmation, micro-interactions | — |
| Semantic & Alias Naming | easing-timing | — |
| Dark Mode Theming | easing-timing | illustration-lottie |
| Multi-Brand Theming | — | illustration-lottie |
| Contrast Validation | reduced-motion | — |
| Cross-Platform Mapping | page-transitions, gesture-drag | illustration-lottie |
| Token Pipeline & Figma Sync | easing-timing | — |
| Component Tokens | micro-interactions, loading-states, feedback-confirmation | — |
| Governance & Migration | easing-timing, reduced-motion | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--dt-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene
