# 🧩 Professional Component Recipes Skill Set — 12 Component Disciplines

A professional reference guide for 12 component disciplines, each covering: definition, core principles, spec tokens (policies/thresholds/contracts), composition, signature patterns, real-world applications, combination notes, anti-patterns, accessibility notes, code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles), **skill-animation** (12 motion disciplines), **skill-design-tokens** (12 token disciplines). This repo answers *"how is this component built?"* — the recipe layer that consumes tokens and renders inside layouts. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Buttons & Badges](./skills/01-buttons-badges/SKILL.md) | 01-buttons-badges | The action vocabulary: button variants and sizes, loading/disabled contracts, icon buttons with names, and badge/status chips. |
| 2 | [Forms & Input Recipes](./skills/02-forms-inputs/SKILL.md) | 02-forms-inputs | Text fields, selects, checkboxes, and validation layouts: the label-hint-error wiring recipe and forgiving-validation timing. |
| 3 | [Tables & Data Grids](./skills/03-tables-data-grid/SKILL.md) | 03-tables-data-grid | Sortable, filterable, paginated tables: column semantics, sticky headers, selection models, and the grid-vs-table decision. |
| 4 | [Modals & Dialogs](./skills/04-modals-dialogs/SKILL.md) | 04-modals-dialogs | The dialog contract done once: role/label, focus trap-and-return, Escape, scrim, and the when-NOT-to-modal decision table. |
| 5 | [Toasts & Notifications](./skills/05-toasts-notifications/SKILL.md) | 05-toasts-notifications | Transient feedback done politely: aria-live narration, timing that respects reading speed, stacking, and the undo pattern. |
| 6 | [Navigation Patterns](./skills/06-navigation-patterns/SKILL.md) | 06-navigation-patterns | Top bars, sidebars, breadcrumbs, and pagination: the wayfinding components, current-page semantics, and responsive collapse contracts. |
| 7 | [Cards & Lists](./skills/07-cards-lists/SKILL.md) | 07-cards-lists | Content containers: card anatomy, list-item patterns, media-object rows, and the whole-card-clickable done accessibly. |
| 8 | [Tabs & Accordions](./skills/08-tabs-accordions/SKILL.md) | 08-tabs-accordions | Disclosure widgets per APG: tabs for peer views, accordions for progressive detail - roles, keyboard maps, and the choice rule. |
| 9 | [Dropdowns & Menus](./skills/09-dropdowns-menus/SKILL.md) | 09-dropdowns-menus | Selects, menus, popovers, and tooltips: the value-vs-action distinction, keyboard contracts, and positioning that stays in viewport. |
| 10 | [Command Palette & Search](./skills/10-command-palette/SKILL.md) | 10-command-palette | Cmd-K overlays: fuzzy search over actions and objects, keyboard-first UX, recent/frecency ranking, and the analytics loop. |
| 11 | [Empty, Loading & Error States](./skills/11-empty-loading-error/SKILL.md) | 11-empty-loading-error | The states most components forget: skeletons that match layout, empty states that teach, error states that recover. |
| 12 | [Component A11y Wiring](./skills/12-accessibility-wiring/SKILL.md) | 12-accessibility-wiring | The cross-cutting a11y layer every recipe shares: focus contracts, announcements, target sizes, and reduced-motion - checked per component. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, spec tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "modals-dialogs",
    "sections": {
      "tokens": [{ "role": "dialog-focus-policy", "value": "trap-and-return", "notes": "..." }],
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

[`assets/references.md`](./skills/assets/references.md) — curated spec links (ARIA APG patterns, `<dialog>`), tool docs (floating-ui, command palette references), and component library inspiration.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the component task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** treat the spec tokens from `assets/css/<skill-id>.css` as hard standards — closed variant sets, size ramps, per-state contracts. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | buttons | forms | tables | dialogs | toasts | nav | cards | tabs | menus | palette | states | wiring |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Buttons & Badges** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Forms & Input Recipes** | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Tables & Data Grids** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Modals & Dialogs** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Toasts & Notifications** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Navigation Patterns** | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Cards & Lists** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Tabs & Accordions** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **Dropdowns & Menus** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ |
| **Command Palette & Search** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **Empty, Loading & Error States** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| **Component A11y Wiring** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux / skill-design-tokens)

| Skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Buttons & Badges | minimalism, flat-design, neumorphism | collage-art |
| Forms & Input Recipes | minimalism, flat-design, class-morphism | brutalism-ui |
| Tables & Data Grids | minimalism, flat-design, class-morphism | collage-art, maximalism |
| Modals & Dialogs | minimalism, flat-design, glassmorphism | brutalism-ui |
| Toasts & Notifications | minimalism, flat-design, glassmorphism | collage-art |
| Navigation Patterns | minimalism, flat-design, class-morphism | collage-art |
| Cards & Lists | minimalism, flat-design, glassmorphism, neumorphism | brutalism-ui |
| Tabs & Accordions | minimalism, flat-design, class-morphism | neumorphism |
| Dropdowns & Menus | minimalism, flat-design, glassmorphism | skeuomorphism |
| Command Palette & Search | minimalism, glassmorphism, class-morphism | skeuomorphism |
| Empty, Loading & Error States | minimalism, flat-design, collage-art | — |
| Component A11y Wiring | minimalism, flat-design | — |

## 🏃 Motion Affinity (skill-animation)

| Skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| Buttons & Badges | micro-interactions, feedback-confirmation | — |
| Forms & Input Recipes | feedback-confirmation, micro-interactions | — |
| Tables & Data Grids | easing-timing | data-animation |
| Modals & Dialogs | entrance-exit, easing-timing | — |
| Toasts & Notifications | feedback-confirmation, entrance-exit | — |
| Navigation Patterns | page-transitions, micro-interactions | — |
| Cards & Lists | entrance-exit, micro-interactions | — |
| Tabs & Accordions | entrance-exit, easing-timing | — |
| Dropdowns & Menus | entrance-exit, micro-interactions | — |
| Command Palette & Search | entrance-exit, micro-interactions | — |
| Empty, Loading & Error States | loading-states, easing-timing | — |
| Component A11y Wiring | reduced-motion, micro-interactions | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--comp-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene
