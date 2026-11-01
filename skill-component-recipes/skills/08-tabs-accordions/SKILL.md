---
name: tabs-accordions
description: Disclosure widgets per APG: tabs for peer views, accordions for progressive detail — roles, keyboard maps, and the choice rule.
tags: [tabs, accordions, disclosure, apg, keyboard]
related: [navigation-patterns, forms-inputs, accessibility-wiring]
---

# Component Recipe: Tabs & Accordions

## 1. Definition

Tabs and accordions are disclosure widgets: they swap or reveal content while keeping page structure. Tabs present peer views of one object (manual selection per APG); accordions progressively reveal detail within a page (details/summary or button+region). The recipe covers the APG contracts — roles, roving tabindex, aria-expanded/selected — and the decision rule: tabs switch peers, accordions condense, and navigation-style tabs are links instead.

## 2. Core Principles

- **Tabs for peers, accordions for detail:** tabs switch between peer views of one object; accordions reveal optional depth — misusing tabs as content condensing buries content.
- **APG tabs contract:** role=tablist/tab/tabpanel, roving tabindex with arrow keys, Home/End, aria-selected — the keymap is the standard (a11y repo guide 06).
- **Accordion = button + expanded region:** native details/summary when styling allows; otherwise button with aria-expanded + region — the trigger is always a real button.
- **Panels are labelled:** tabpanel labelled by its tab; accordion regions labelled by their trigger — AT users hear where they landed.
- **One open accordion is the default:** multiple-open needs a reason (comparison tasks) — single-open keeps scroll position stable.
- **URL state for tab views:** peer views that bookmark/refresh (tab=usage in URL) — state users can link to.
- **No lazy surprises:** tab panel content mounts on demand but announces loading; content must not shift the page when revealed.
- **Never tabs inside tabs inside accordions:** nesting disclosure widgets beyond one level is a content-architecture failure.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Tabs role set | `--comp-tabs-role-set` | tablist/tab/tabpanel | APG structure |
| Tabs keymap | `--comp-tabs-keymap` | arrows+home+end | Roving tabindex per APG |
| Tabs selection | `--comp-tabs-selection` | manual-activation | Space/Enter activates; arrows move |
| Tabs URL state | `--comp-tabs-url-state` | tab-param | Bookmarkable peer views |
| Accordion trigger | `--comp-accordion-trigger` | button+aria-expanded | Native details preferred when styleable |
| Accordion region label | `--comp-accordion-region-label` | trigger-labelled | Region named by its trigger |
| Accordion open policy | `--comp-accordion-open-policy` | single-open-default | Multi-open documented per use |
| Tabs panel label | `--comp-tabs-panel-label` | labelledby-tab | Panel narrates its tab |
| Disclosure nesting cap | `--comp-disclosure-nesting-cap` | 1-level | No tabs-in-tabs-in-accordions |
| Tabs vs links | `--comp-tabs-vs-links` | peers-vs-navigation | Site navigation is links, not tabs |

Consume them by linking `assets/css/tabs-accordions.css` once and reading `var(--comp-tabs-...)` / `var(--comp-accordion-...)` from widget CSS and the keymap implementations. These tokens are contracts as much as values: if a widget's roles, keymap, or open policy do not match the token it claims, the widget is a decoration, not a disclosure — ship it under a different name or fix the implementation.

## 4. Composition

- **Composes with accessibility-wiring (guide 11) and a11y repo guide 06:** the APG keymaps are shared contracts this recipe implements — wiring validates roles, roving tabindex, and labelled panels.
- **Composes with tables-data-grid and forms-inputs:** tab panels host full recipes; disclosure widgets are containers, not content — a grid inside a tab keeps its own contract.
- **Composes with skill-animation entrance-exit:** panel transitions use motion tokens; reduced-motion collapses them instantly, and reveal animation never delays AT availability.

## 5. Signature Patterns

- **Disclosure kit:** Tabs and Accordion components implementing the APG contracts once — products compose panels, never re-implement keymaps. One roving-tabindex implementation, one aria-expanded wiring, tested once and inherited everywhere.
- **Peer-content review:** content designed for tabs passes the 'would a user expect this as a peer view?' test at design time — buried-content checks before build, so tab 3 never quietly becomes where the important stuff lives.

## 6. Real-World Use Cases

- **Product detail views (overview/specs/reviews), settings groups, and docs** — the canonical peer-view surfaces where tabs earn their contract.
- **FAQs, release notes, and help panels** as accordions, where single-open progressive detail keeps long pages scannable.
- **Audit** — div-tabs, auto-activating arrows, accordion content invisible to find-in-page: the recurring findings this recipe's checklist targets.

## 7. Combination Notes

### With other component-recipe skills

- **Good with navigation-patterns:** the choice rule lives at the seam — navigation is links, peer views of one object are tabs; the two recipes share vocabulary so the decision is explicit, not accidental.
- **Good with forms-inputs, tables-data-grid, cards-lists, buttons-badges, dropdowns-menus, modals-dialogs, command-palette, toasts-notifications, empty-loading-error:** tab panels and accordion bodies are containers, not content — hosted recipes arrive with their own contracts intact, and the disclosure only owns reveal semantics.
- **Good with accessibility-wiring:** APG compliance is the shared deliverable — this recipe implements the keymaps, wiring verifies them.
- **No caution or avoid list:** as pure disclosure containers, tabs and accordions conflict with nothing as long as hosted content brings its own recipe.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both favor understated tab strips and hairline accordion dividers, where the selected state is carried by color-weight and border — the APG structure stays invisible.
- **Good affinity with class-morphism:** subtle raised panels and soft inset triggers map well onto accordion buttons and tab panels without disturbing the disclosure semantics.
- **Caution with neumorphism:** soft-extrusion styling tends to blur the pressed/selected boundary — a tab that does not visibly change on `aria-selected` fails the contract; strengthen the selected state with a non-shadow indicator (underline, color shift).

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit:** panel reveal/hide is the textbook entrance-exit case — height/opacity transitions on the disclosure region, implemented once in the kit.
- **Good affinity with easing-timing:** tab swaps and accordion opens should use consistent duration/easing tokens; the transition is feedback, not decoration, so it stays short and honors reduced-motion by collapsing instantly.

## 8. Anti-Patterns

- **Div-tabs** — clickable divs with no roles or keymaps
- **Auto-activation chaos** — panels swapping on every arrow pass - disorienting and slow
- **Buried content** — primary content stuffed in tab 3 where find-in-page and print cannot see it
- **Accordion-everything** — whole pages as accordions - scroll lost, content hidden

### Accessibility Notes

Disclosure widgets are APG territory (a11y repo guide 06): roles, roving tabindex, expanded/selected states, and labelled panels — a tab widget that narrates nothing is decoration, not a widget. Concretely: the tablist carries `role="tablist"`, each tab `role="tab"` with `aria-selected` and a roving tabindex so exactly one tab is in the tab order; arrow keys move focus with Home/End jumping to the ends, Space/Enter activates (manual activation — arrows move, activation is deliberate), and each panel is `role="tabpanel"` labelled by its tab via `aria-labelledby`. Accordions are simpler but just as strict: a real `<button>` with `aria-expanded` and `aria-controls`, region labelled by its trigger. The fallback rule: where the full tab contract cannot ship, use native radio-style selection or plain sections with anchor links — semantic structure beats partial widgets.

## 9. Code Examples

### Example 1 — APG-exact tabs with roving tabindex and URL state

Tokens: `assets/css/tabs-accordions.css`

```html
<div class="tabs">
  <div role="tablist" aria-label="Project documentation">
    <button role="tab" id="tab-overview" aria-selected="true"  aria-controls="panel-overview">Overview</button>
    <button role="tab" id="tab-usage"    aria-selected="false" aria-controls="panel-usage" tabindex="-1">Usage</button>
    <button role="tab" id="tab-api"      aria-selected="false" aria-controls="panel-api"   tabindex="-1">API</button>
  </div>
  <div role="tabpanel" id="panel-overview" aria-labelledby="tab-overview"><p>What this project does.</p></div>
  <div role="tabpanel" id="panel-usage" aria-labelledby="tab-usage" hidden><p>How to install and run it.</p></div>
  <div role="tabpanel" id="panel-api"   aria-labelledby="tab-api"   hidden><p>Endpoints and types.</p></div>
</div>
<script>
  const tabs = [...document.querySelectorAll('[role="tab"]')];
  const url = new URL(location); // --comp-tabs-url-state: tab=usage survives refresh and sharing
  function select(tab, focus = true) {
    tabs.forEach(t => {
      const on = t === tab;
      t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;   // roving tabindex
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tab.focus();
    url.searchParams.set('tab', tab.id.replace('tab-', '')); history.replaceState(null, '', url);
  }
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => select(tab, false));
    tab.addEventListener('keydown', e => {           // manual activation: arrows move, Enter activates
      const idx = { ArrowRight: (i + 1) % tabs.length, ArrowLeft: (i + tabs.length - 1) % tabs.length, Home: 0, End: tabs.length - 1 }[e.key];
      if (idx != null) { e.preventDefault(); select(tabs[idx]); }
    });
  });
  const initial = url.searchParams.get('tab');
  if (initial) { const t = document.getElementById('tab-' + initial); if (t) select(t, false); }
</script>
<style>
  [role="tablist"] { display: flex; gap: 4px; border-bottom: 1px solid #D4D4D4; }
  [role="tab"] { font: 500 14px/1 Inter, system-ui, sans-serif; padding: 10px 16px; border: none; background: none; border-bottom: 2px solid transparent; cursor: pointer; color: #404040; }
  [role="tab"][aria-selected="true"] { color: #171717; border-bottom-color: #2563EB; }
  [role="tab"]:focus-visible { outline: 2px solid #2563EB; outline-offset: -2px; }
  [role="tabpanel"] { padding: 16px 4px; font: 14px/1.5 Inter, system-ui, sans-serif; color: #404040; }
</style>
```

### Example 2 — Single-open accordion (button + aria-expanded + labelled region)

Tokens: `assets/css/tabs-accordions.css`

```html
<div class="accordion">
  <h3 class="acc-heading">
    <button class="acc-trigger" id="acc-t1" aria-expanded="true" aria-controls="acc-r1">Can I self-host the design tokens?<span class="acc-icon" aria-hidden="true"></span></button>
  </h3>
  <div class="acc-region" id="acc-r1" role="region" aria-labelledby="acc-t1">
    <p>Yes — tokens ship as plain CSS custom properties with no runtime.</p>
  </div>
  <h3 class="acc-heading">
    <button class="acc-trigger" id="acc-t2" aria-expanded="false" aria-controls="acc-r2">How often do tokens change?<span class="acc-icon" aria-hidden="true"></span></button>
  </h3>
  <div class="acc-region" id="acc-r2" role="region" aria-labelledby="acc-t2" hidden>
    <p>On a quarterly cadence; breaking renames go through governance review.</p>
  </div>
</div>
<script>
  const triggers = [...document.querySelectorAll('.acc-trigger')];
  triggers.forEach(trigger => trigger.addEventListener('click', () => {
    const open = trigger.getAttribute('aria-expanded') === 'true';
    triggers.forEach(t => {                       // --comp-accordion-open-policy: single-open-default
      const on = t === trigger && !open;          // clicking the open item just closes it
      t.setAttribute('aria-expanded', String(on));
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
  }));
</script>
<style>
  .acc-trigger { width: 100%; display: flex; justify-content: space-between; align-items: center; text-align: left; padding: 14px 4px;
    font: 500 15px/1.4 Inter, system-ui, sans-serif; background: none; border: none; border-bottom: 1px solid #D4D4D4; cursor: pointer; color: #171717; }
  .acc-trigger:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; }
  .acc-icon::before { content: "+"; font-weight: 600; }
  .acc-trigger[aria-expanded="true"] .acc-icon::before { content: "–"; }
  .acc-region { padding: 12px 4px 16px; font: 14px/1.5 Inter, system-ui, sans-serif; color: #404040; }
</style>
```

## 10. Implementation Checklist

- [ ] Tabs implement the full APG set (`--comp-tabs-role-set`): tablist/tab/tabpanel with `aria-selected` and panels labelled by their tab (`--comp-tabs-panel-label`).
- [ ] Keyboard map matches `--comp-tabs-keymap`: arrows move with a roving tabindex, Home/End jump to the ends, activation per `--comp-tabs-selection` (manual unless documented).
- [ ] Peer tab views persist state in the URL (`--comp-tabs-url-state`) so views are bookmarkable and refresh-safe.
- [ ] Every accordion trigger is a real button with `aria-expanded` (`--comp-accordion-trigger`) and a region labelled by its trigger (`--comp-accordion-region-label`).
- [ ] Accordions default to single-open (`--comp-accordion-open-policy`); multi-open is a documented per-use decision.
- [ ] Disclosure nesting never exceeds `--comp-disclosure-nesting-cap` (1 level) — no tabs in tabs in accordions.
- [ ] Navigation markup uses links, not tabs (`--comp-tabs-vs-links`); the peers-vs-navigation rule was applied at design time.
- [ ] Panel content mounts without layout shift, announces loading when lazy, and remains visible to find-in-page and print.
