---
name: empty-states
description: First-use, no-results, and cleared states as teaching moments: explain the value, then hand over the next action.
tags: [empty-states, microcopy, ux-writing, onboarding, ctas]
related: [onboarding-copy, writing-principles, notifications]
---

# UX Writing Guide: Empty State Copy

## 1. Definition

Empty states are copy with a job: convert a blank box into an orientation moment. The taxonomy is threefold - first-use (no data yet: teach the value, provide the create action), no-results (data exists but the query matched nothing: explain, then suggest relaxing the search), and cleared (data existed and was removed: offer restore). Each state has its own copy formula, and all three share one rule: never leave the user without a next action.

## 2. Core Principles

- **Every empty state carries an action:** "Create your first project" with the button - a blank panel with only text is a dead end.
- **First-use teaches value, not features:** "Projects keep your work organized by client" - the why before the how.
- **No-results explains and relaxes:** "No projects match \"acme projct\". Try fewer words or clear filters."
- **Cleared offers restore:** "You deleted all notifications" + "Undo" - cleared states acknowledge what happened.
- **One idea per empty state:** value statement + action - onboarding essays do not belong in panels.
- **Empty copy is the tone-safe zone:** personality is allowed here (voice-tone guide) - it is a low-stakes, high-visibility moment.
- **Illustrations support, text carries:** the image sets mood; the copy carries the instruction - never illustration-only.
- **Empty states are announced:** AT users hear the state change - the region is labelled and the CTA keyboard-reachable.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Taxonomy | `--uxw-empty-taxonomy` | `first-use,no-results,cleared` | Three states, three copy formulas |
| CTA required | `--uxw-empty-cta-required` | `every-state-has-action` | No dead-end blanks |
| First use | `--uxw-empty-first-use` | `value-teaching` | Why the feature matters, briefly |
| No results | `--uxw-empty-no-results` | `explain+relax-suggestion` | Query echo + relaxation tip |
| Cleared | `--uxw-empty-cleared` | `acknowledge+restore` | Undo path for cleared content |
| Length | `--uxw-empty-length` | `1-2-lines` | Panel copy budget |
| Illustration role | `--uxw-empty-illustration-role` | `mood-only` | Text carries the instruction |
| Tone | `--uxw-empty-tone` | `personality-allowed` | The voice-tone safe zone |
| Announce | `--uxw-empty-announce` | `labelled-region` | State change narrated |
| Coverage | `--uxw-empty-coverage` | `every-collection-surface` | Lists/tables/dashboards ship empties |

Consume them by linking `assets/css/empty-states.css` at the app root and reading `var(--uxw-empty-<role>)` wherever an empty surface is specified - the taxonomy key selects the copy formula, the length budget constrains the panel, and the coverage token is the review gate: a collection surface without an empty state fails audit.

## 4. Composition

- **Composes with onboarding-copy (guide 05):** first-use empties are onboarding's atomic unit - the contracts are shared, so a first-use empty state and a first-run welcome card should read as one voice.
- **Composes with component-recipes empty-loading-error:** that recipe owns the state components (structure, spacing, illustration slots); this guide owns the strings that fill them - component and copy specs ship together.
- **Composes with skill-icons-illustration:** empty-state illustrations are the most common illustration surface - direction is shared, and the mood-only rule keeps the illustration from carrying meaning the text must own.

## 5. Signature Patterns

- **The empty-state formula:** [value statement] + [next action button] + optional [illustration] - every empty surface composes the same three parts, which makes audits mechanical and gaps obvious.
- **The no-results recipe:** echo the query, explain the mismatch, offer one relaxation ("Clear filters" / "Try fewer words") - never a bare zero; the echo proves the system heard the user, the relaxation gives them a way out.

## 6. Real-World Use Cases

- **First-run products:** where empty states are the onboarding surface - the first thing a new user sees is an empty dashboard.
- **Search-heavy products:** where no-results quality drives retention - a dead-end zero sends users to a competitor's search box.
- **Audit:** blank boxes, empty states without CTAs, illustration-only panels that leave AT users nothing to act on.

## 7. Combination Notes

### With other ux-writing skills

- **Good with writing-principles, notifications, button-labels, and component-microcopy:** brevity and user-first ordering shape the 1-2-line budget, cleared states pair with undo toasts ("You deleted all notifications" + Undo), the CTA is a full button-label contract (verb-first, specific), and supporting hints follow microcopy budgets.
- **Good with error-messages, voice-tone, accessible-writing, copy-audit, forms-labels, localization-i18n:** not-found errors often resolve into no-results empties, the tone-safe zone is defined by voice-tone, labelled regions and keyboard-reachable CTAs come from accessible-writing, and the string inventory plus i18n flags keep all three formulas consistent. There is no avoid list: every sibling discipline has a role in some empty state.
- **Caution with onboarding-copy:** the skills share the first-use surface, and the boundary must stay deliberate - empty states teach one feature's value with one action; onboarding copy orchestrates the sequence. If a first-use empty starts growing onboarding prose, it has crossed the line (see the empty-essay anti-pattern): guide 05 decides what comes next, this guide writes the panel.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and collage-art:** minimalism enforces the one-idea rule, flat-design keeps the CTA prominent, and collage-art's illustrative freedom suits the mood-only illustration role - empty states are the one surface where expressive visuals are welcome, because the text carries the instruction. There is no caution list: the formula (value + action + optional illustration) survives any style - only the illustration register changes.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit and illustration-lottie:** empty panels transition in with a short entrance at token durations, and looping Lottie illustrations are the natural mood layer - both stay subordinate to the value statement and CTA. There is no caution list: motion never competes with the copy here, but the CTA must be keyboard-reachable and present from the first frame.

## 8. Anti-Patterns

- **The blank box** — unstyled empty surfaces shipping to production
- **Empty essay** — three paragraphs of feature tour in an empty panel
- **Illustration-only** — a drawing with no text and no action
- **Dead-end zero** — 'No results' with no suggestion and no escape

### Accessibility Notes

Empty states are state-change announcements (WCAG 4.1.3): labelled regions, keyboard-reachable CTAs, and text that does not depend on the illustration for meaning (1.1.1) - the copy must fully stand alone, because an AT user hears the region's label and text and never sees the mood image. The announce token makes the labelled region a build requirement, and the illustration-role token keeps the drawing decorative (`aria-hidden`) so no meaning leaks out of it. The fallback is concrete: if labelled-region wiring is unavailable, move focus to the empty-state heading on state change - focus movement is the narration fallback, and it must land on a heading that carries the value statement, not on the illustration container.

## 9. Code Examples

### Example 1 — The three-state gallery (first-use / no-results / cleared)

```html
<main class="gallery">
  <section class="empty" data-state="first-use" aria-labelledby="eu1-h">
    <svg class="art" aria-hidden="true" viewBox="0 0 48 48"><rect x="8" y="12" width="32" height="24" rx="4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M24 20v10M19 25h10" stroke="currentColor" stroke-width="2"/></svg>
    <h2 id="eu1-h">Projects keep client work in one place</h2>
    <p>Create your first project and invite your team.</p>
    <button type="button" class="btn-primary" onclick="setState('no-results')">Create your first project</button>
  </section>
  <section class="empty" data-state="no-results" aria-labelledby="eu2-h" hidden>
    <svg class="art" aria-hidden="true" viewBox="0 0 48 48"><circle cx="21" cy="21" r="11" fill="none" stroke="currentColor" stroke-width="2"/><path d="M29 29l9 9" stroke="currentColor" stroke-width="2"/></svg>
    <h2 id="eu2-h">No projects match "acme projct"</h2>
    <p>Nothing matches that spelling. Try fewer words or clear your filters.</p>
    <button type="button" class="btn" onclick="setState('cleared')">Clear filters</button>
  </section>
  <section class="empty" data-state="cleared" aria-labelledby="eu3-h" hidden>
    <svg class="art" aria-hidden="true" viewBox="0 0 48 48"><path d="M14 18h20l-2 20H16L14 18zM19 18v-4h10v4" fill="none" stroke="currentColor" stroke-width="2"/></svg>
    <h2 id="eu3-h">You deleted all notifications</h2>
    <p>Your list is clear. Changed your mind?</p>
    <button type="button" class="btn" onclick="setState('first-use')">Undo</button>
  </section>
</main>
<style>
  :root { --uxw-empty-taxonomy: first-use,no-results,cleared; --uxw-empty-illustration-role: mood-only; --color-text: #171717; --color-muted: #525252; --color-brand: #2563eb; }
  .gallery { font: 15px/1.5 system-ui, sans-serif; max-width: 360px; margin: 24px auto; }
  .empty { border: 1px solid #e5e5e5; border-radius: 12px; padding: 28px 20px; text-align: center; color: var(--color-text); }
  .art { width: 48px; height: 48px; color: #a3a3a3; margin-bottom: 10px; } /* mood only, aria-hidden */
  .empty h2 { margin: 0 0 4px; font-size: 16px; } .empty p { margin: 0 0 14px; color: var(--color-muted); }
  .btn-primary, .btn { border-radius: 6px; padding: 8px 16px; font: 600 14px system-ui, sans-serif; cursor: pointer; }
  .btn-primary { background: var(--color-brand); color: #fff; border: none; } .btn { background: #fff; color: var(--color-brand); border: 1px solid #d4d4d4; }
  .btn:focus-visible, .btn-primary:focus-visible { outline: 2px solid var(--color-brand); outline-offset: 2px; }
</style>
<script>
  // The three states must match --uxw-empty-taxonomy exactly.
  const states = getComputedStyle(document.documentElement).getPropertyValue('--uxw-empty-taxonomy').split(',');
  console.assert(states.length === 3, 'empty taxonomy must ship all three states');
  function setState(next) { // taxonomy drive: first-use -> no-results -> cleared
    document.querySelectorAll('.empty').forEach(el => { el.hidden = el.dataset.state !== next; });
  }
</script>
```

### Example 2 — No-results driven by a live query (echo + relax suggestion)

```html
<div class="finder">
  <label for="q">Search projects</label>
  <input id="q" type="search" placeholder="e.g. website redesign" />
  <p id="count" class="count" role="status">3 projects</p>
  <ul id="list" class="list">
    <li>Website redesign</li>
    <li>Mobile app v2</li>
    <li>Brand refresh</li>
  </ul>
</div>
<style>
  :root { --uxw-empty-no-results: explain+relax-suggestion; --uxw-empty-announce: labelled-region; --color-danger: #b91c1c; --color-brand: #2563eb; }
  .finder { font: 15px/1.5 system-ui, sans-serif; max-width: 340px; margin: 24px auto; }
  label { display: block; font-weight: 600; margin-bottom: 4px; }
  input { width: 100%; box-sizing: border-box; padding: 8px 10px; border: 1px solid #d4d4d4; border-radius: 6px; font: inherit; }
  .count { color: #525252; font-size: 13px; margin: 8px 0 6px; } .list, .empty-search { margin: 0; padding: 0; list-style: none; }
  .list li { padding: 8px 10px; border: 1px solid #eee; border-radius: 6px; margin-bottom: 6px; }
  .empty-search { border: 1px dashed #d4d4d4; border-radius: 10px; padding: 20px; text-align: center; }
  .empty-search p { margin: 0 0 4px; color: #404040; } .empty-search .query { color: var(--color-danger); font-weight: 600; } .empty-search .tip { color: #525252; font-size: 13px; }
  .empty-search button { background: none; border: none; color: var(--color-brand); font: inherit; font-weight: 600; cursor: pointer; padding: 0; text-decoration: underline; }
</style>
<script>
  const PROJECTS = ['Website redesign', 'Mobile app v2', 'Brand refresh'];
  const input = document.getElementById('q'), list = document.getElementById('list'), count = document.getElementById('count');
  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    const hits = PROJECTS.filter(p => p.toLowerCase().includes(q));
    count.textContent = q ? hits.length + ' of ' + PROJECTS.length + ' projects' : PROJECTS.length + ' projects';
    if (hits.length) { // results view
      list.innerHTML = hits.map(p => '<li>' + p + '</li>').join('');
      list.hidden = false; document.getElementById('none').remove();
    } else { // --uxw-empty-no-results: echo the query, then one relaxation
      list.hidden = true;
      let none = document.getElementById('none');
      if (!none) {
        none = document.createElement('div');
        none.id = 'none'; none.className = 'empty-search'; none.setAttribute('role', 'status');
        input.closest('.finder').appendChild(none);
      }
      none.innerHTML = '<p>No projects match <span class="query">"' + input.value.trim() +
        '"</span>.</p><p class="tip">Try fewer words, or <button type="button" onclick="' +
        'document.getElementById(\'q\').value=\'\'; document.getElementById(\'q\').dispatchEvent(new Event(\'input\'))' +
        '">clear the search</button>.</p>';
    }
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every list, table, and dashboard ships an empty state per `--uxw-empty-coverage` - no blank boxes in production.
- [ ] Each surface's state is classified against `--uxw-empty-taxonomy` (first-use / no-results / cleared) and uses that formula.
- [ ] Every empty panel carries a keyboard-reachable CTA per `--uxw-empty-cta-required`.
- [ ] No-results states echo the query and offer one relaxation per `--uxw-empty-no-results`, and cleared states acknowledge + offer restore per `--uxw-empty-cleared`.
- [ ] Panel copy stays within `--uxw-empty-length` (1-2 lines) - value statement plus action, nothing more.
- [ ] Illustrations are `aria-hidden` and mood-only per `--uxw-empty-illustration-role` - text stands alone.
- [ ] Empty regions are labelled and announced per `--uxw-empty-announce`, with focus fallback to the heading.
