---
name: notifications
description: Scannable, non-alarming, self-sufficient toast and notification strings that work when skimmed for two seconds and when read aloud by a screen reader.
tags: [notifications, toasts, alerts, copy, ux-writing]
related: [error-messages, voice-tone, component-microcopy]
---

# UX Writing Guide: Notification & Toast Copy

## 1. Definition

Notification copy is read in two hostile conditions: skimmed for 1–2 seconds, and read aloud by a screen reader without context. The discipline covers toast copy (object + result: `Invitation sent to Lan`), notification center entries (title + body + time, self-sufficient out of context), the quiet-success/loud-error split, and the anti-alarm principle: exclamation marks, urgency words, and ALL CAPS are banned except for genuine system-critical alerts. Because toasts are transient and notification center entries are permanent, the same event often needs both — a one-line toast for the moment, and a durable entry that still makes sense days later when the moment has passed.

## 2. Core Principles

- **Toast copy is object + result:** `Invitation sent to Lan`, `Project Acme archived` — what happened and to/from whom, in one line; a verb with no object (`Saved`) makes the user do the parsing.
- **Self-sufficiency for notification center:** entries must make sense days later, out of context — no `It's done!`; write as if the reader never saw the screen it happened on.
- **Quiet success, loud error:** success is subtle and brief — no celebration theater; errors persist, carry the fix, and link to recovery.
- **The anti-alarm rules:** no exclamation marks in system copy, no urgency words (`URGENT`, `IMPORTANT`), no ALL CAPS — alarm is earned by genuine critical events only, and is spent sparingly enough to stay meaningful.
- **Notifications narrate politely:** toast strings pass through `aria-live=polite` — copy is written to be heard without seeing, so it cannot lean on position, color, or iconography.
- **Timing is part of the copy:** a 4–8s read budget means one line for toasts — longer content goes to the notification center, not into an auto-dismissing paragraph.
- **Actions are named in the copy:** `Archived — Undo`, not a bare undo icon — the action is offered in words, which also makes it narratable.
- **Notification copy respects the inbox:** titles summarize, bodies carry detail, and previews truncate gracefully — front-load meaning so the cut falls on detail, never on the point.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Toast structure | `--uxw-toast-structure` | `object+result` | 'Invitation sent to Lan' |
| Toast length | `--uxw-toast-length` | `1-line` | 4-8s read budget; detail goes to center |
| Self-sufficiency | `--uxw-self-sufficiency` | `out-of-context-readable` | Center entries stand alone |
| Success policy | `--uxw-success-policy` | `quiet-brief` | No celebration theater |
| Error policy | `--uxw-error-policy` | `persist+fix+link` | Errors carry recovery |
| Anti-alarm | `--uxw-anti-alarm` | `no-!-no-caps-no-urgent` | Alarm earned by critical events only |
| Narration | `--uxw-narration` | `aria-live-polite` | Written to be heard (4.1.3) |
| Action in copy | `--uxw-action-in-copy` | `named-undo` | 'Archived - Undo' not bare icons |
| Front-load | `--uxw-front-load` | `meaning-first-40-chars` | Previews truncate at the wrong end otherwise |
| Center entry | `--uxw-center-entry` | `title+body+time` | The notification center structure |

Consume these spec tokens by linking `assets/css/notifications.css` at the app root and reading `var(--uxw-...)` from the toast service, the notification center templates, and any copy linting — they encode behavior and copy shape as named contracts, so a toast that auto-dismisses an error or a preview that truncates to `Your project has been...` is a token violation, not an edge case.

## 4. Composition

- **Composes with the component-recipes toasts-notifications recipe:** that recipe owns the service, timing, and stacking; this guide owns the strings the service renders — one layer animates, the other speaks.
- **Composes with error-messages (guide 03):** error toasts follow the three-part contract, persisted — what happened, why, the fix — compressed and given a link to recovery.
- **Composes with voice-tone (guide 02):** the tone matrix's success and error rows govern these strings; toasts are the tone system's most exposed surface because everyone reads them and no one rereads them.

## 5. Signature Patterns

- **The toast formula:** `[object] + [result verb] + optional [undo/fix action]` — one line, self-sufficient, polite. `Project Acme archived — Undo` shows all three slots; drop a slot and the toast stops working on skim.
- **The front-load pass:** write the string, then cut it to 40 characters and check it still communicates — that is what the preview shows. If the 40-char cut reads as `Your project has been...`, rewrite so the first 40 characters carry the meaning and the tail carries detail.

## 6. Real-World Use Cases

- **Any async feedback surface:** saves, sends, uploads, syncs — every operation that finishes out of the user's direct attention needs an object+result string.
- **Notification centers and email digests** — the durable sibling of the toast, where self-sufficiency, title+body+time structure, and graceful preview truncation decide usefulness.
- **Audits hunting exclamation-toast spam, context-free `Done!` results, and auto-dismissing errors** — three findings that convert a notification system from a service into noise.

## 7. Combination Notes

### With other ux-writing skills

- **Pairs naturally with error-messages (guide 03):** error toasts are the taxonomy's most compressed form — the three-part contract persists, gains a recovery link, and drops everything else to fit one line.
- **Pairs with writing-principles and voice-tone:** brevity rules and the tone matrix's success/error rows are the source of the toast formula; this guide is their application under a read budget.
- **Pairs with component-microcopy (guide 07) and button-labels:** toast actions are labeled buttons following verb rules, and `Archived — Undo` is microcopy's action-naming principle applied to a transient surface.
- **Pairs with forms-labels, onboarding-copy, and empty-states:** form submissions, onboarding steps, and empty-state recoveries all end in toasts or center entries — the endings must share the system's voice.
- **Pairs with accessible-writing and copy-audit:** narration copy (4.1.3) is an accessibility deliverable, and the toast library is a high-leverage audit target because a handful of strings covers every async event.
- **Pairs with localization-i18n:** the 1-line budget must survive 30% expansion — toasts are often written with the localization buffer built in, and the 40-char front-load check doubles as a truncation check across locales.
- **No avoid list:** notification copy composes with every outcome-producing skill; the failure mode is a toast service that ships strings ad hoc, bypassing the formula.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** quiet success is naturally minimal — a single line on a flat surface with no ornament matches both the visual style and the anti-alarm rules.
- **Good affinity with glassmorphism:** translucent toast surfaces suit brief, one-line copy; glass emphasizes the transient nature of toasts, which reinforces the timing budget.
- **Caution with collage-art:** its expressive, layered aesthetic may invite decorative toasts with personality-forward copy; keep the object+result formula regardless — personality lives in voice-tone, not in the notification system.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation:** the toast entrance is the confirmation moment; animation should be quick and settle fast so the 4–8s read budget starts when the string is legible, not when it starts moving.
- **Good affinity with entrance-exit:** toast entrances and exits use these tokens directly — the exit must never begin before a slow reader's budget elapses, and prefers-reduced-motion applies to both.
- **Caution, generally:** long cinematic entrances effectively shorten the read budget and stacked toasts animating over each other can drop entries visually; the stacking layer (component-recipes) and copy layer must agree on duration.

## 8. Anti-Patterns

- **Exclamation spam:** 'Saved!' 'Sent!' 'Updated!' - punctuated enthusiasm as system voice
- **Context-free results:** 'Done!' with no object - done with what?
- **Auto-dismissing errors:** critical failures vanishing on a timer
- **Back-loaded meaning:** previews that truncate to 'Your project has been...'

### Accessibility Notes

Notification copy is WCAG 4.1.3 surface: polite narration, durations a reader can meet, and copy written to be heard — strings must survive being the only thing announced, with no reliance on visual position. Concretely, toast containers are live regions with `aria-live=polite` (status changes) or `aria-live=assertive` reserved for genuine emergencies, toasts that appear in response to a user action stay within the polite channel, error toasts persist until dismissed rather than timing out, and the copy itself avoids pronouns and positional references (`this`, `here`) that mean nothing when heard in isolation. The fallback rule covers legacy stacks: if a toast cannot narrate (legacy stack), pair the action with an inline status line on the page - somewhere, the outcome must be text, because a result the user never learns about is indistinguishable from a failure.

## 9. Code Examples

### Example 1 — Toast with object+result copy and quiet-success/loud-error split

Tokens: `assets/css/notifications.css`

```html
<button id="archiveBtn">Archive project</button>
<button id="inviteBtn">Send invitation</button>
<button id="uploadBtn">Upload (fails)</button>
<div id="toasts" class="toasts" aria-live="polite" role="region" aria-label="Notifications"></div>
<script>
  const host = document.getElementById('toasts');
  function toast({ msg, kind, undo, fix }) {
    const el = document.createElement('div');
    el.className = 'toast ' + kind; // quiet-brief success / persisting error
    el.innerHTML = kind === 'error'
      ? `<strong>Upload failed</strong> - File exceeds the 25 MB limit. <a href="#settings">Adjust plan limits</a>`
      : `<span>${msg}</span>${undo ? `<button class="undo">${undo}</button>` : ''}`;
    if (undo) el.querySelector('.undo').onclick = () => { el.remove(); /* revert */ };
    host.appendChild(el);
    if (kind === 'success') setTimeout(() => el.remove(), 6000); // 4-8s budget; errors persist
  }
  document.getElementById('inviteBtn').onclick  = () => toast({ msg: 'Invitation sent to Lan', kind: 'success' });
  document.getElementById('archiveBtn').onclick = () => toast({ msg: 'Project Acme archived', kind: 'success', undo: 'Archived - Undo' });
  document.getElementById('uploadBtn').onclick  = () => toast({ msg: '', kind: 'error' }); // persists, carries fix + link
</script>
<style>
  :root { /* production: var(--uxw-...) from assets/css/notifications.css */
    --uxw-toast-structure: object+result; --uxw-error-policy: persist+fix+link; --uxw-narration: aria-live-polite; }
  body { font: 14px/1.5 Inter, system-ui, sans-serif; padding: 24px; }
  button { padding: 8px 14px; margin-right: 8px; border: 1px solid #d4d4d4; border-radius: 8px; background: #fff; cursor: pointer; }
  .toasts { position: fixed; bottom: 24px; right: 24px; display: flex; flex-direction: column; gap: 8px; max-width: 340px; }
  .toast { padding: 10px 14px; border-radius: 8px; font-size: 13px; box-shadow: 0 2px 8px rgba(0,0,0,.12); }
  .success { background: #171717; color: #fff; }            /* quiet, dark, one line */
  .error { background: #fef2f2; color: #171717; border: 1px solid #b91c1c; border-left: 4px solid #b91c1c; }
  .error a { color: #b91c1c; }
  .undo { margin-left: 8px; border: 0; background: none; color: #93c5fd; text-decoration: underline; cursor: pointer; }
</style>
```

### Example 2 — Notification center list with front-loaded previews

Tokens: `assets/css/notifications.css`

```html
<section class="center" aria-label="Notification center">
  <h3>Notifications</h3>
  <ul>
    <li><a href="#">
      <span class="title">Comment on Landing page v2</span>
      <span class="body">Lan Nguyen: "Hero headline still uses the old tagline..."</span>
      <time datetime="2026-11-01T09:14">Yesterday 09:14</time>
    </a></li>
    <li><a href="#">
      <span class="title">Export ready - Q4 report</span>
      <span class="body">Your CSV export of 1,240 rows finished and expires in 7 days.</span>
      <time datetime="2026-10-30T17:02">Oct 30, 17:02</time>
    </a></li>
    <li><a href="#">
      <span class="title">Access granted - Acme workspace</span>
      <span class="body">Priya Sharma added you as an editor. Open Acme to start.</span>
      <time datetime="2026-10-28T11:40">Oct 28, 11:40</time>
    </a></li>
  </ul>
</section>
<script>
  // Front-load pass: cut each body to 40 chars and confirm the meaning survives.
  document.querySelectorAll('.body').forEach(el =>
    console.assert(el.textContent.trim().slice(0, 40).length === 40, 'meaning survives the 40-char cut'));
</script>
<style>
  :root { --uxw-center-entry: title+body+time; --uxw-front-load: meaning-first-40-chars; }
  body { font: 14px/1.5 Inter, system-ui, sans-serif; padding: 24px; }
  .center { max-width: 420px; border: 1px solid #d4d4d4; border-radius: 8px; padding: 8px 0; }
  .center h3 { font-size: 13px; font-weight: 600; margin: 0; padding: 8px 16px; }
  ul { list-style: none; margin: 0; padding: 0; }
  li + li { border-top: 1px solid #f0f0f0; }
  a { display: block; padding: 10px 16px; text-decoration: none; color: inherit; }
  a:hover { background: #f5f5f5; }
  .title { display: block; font-weight: 600; }
  .body { display: block; color: #404040; font-size: 13px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
  time { display: block; color: #737373; font-size: 12px; margin-top: 2px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every toast follows the `--uxw-toast-structure` formula — object + result, optional named action — and stays one line per `--uxw-toast-length`.
- [ ] Success toasts are quiet and brief per `--uxw-success-policy`; error toasts persist, show the fix, and link to recovery per `--uxw-error-policy` — no error auto-dismisses.
- [ ] The toast container is `aria-live=polite` per `--uxw-narration`, and every string reads cleanly aloud with no positional references (4.1.3).
- [ ] Actions are named in copy per `--uxw-action-in-copy` — `Archived - Undo`, never a bare icon.
- [ ] No system copy uses exclamation marks, urgency words, or ALL CAPS per `--uxw-anti-alarm`, except reviewed critical alerts.
- [ ] Notification center entries use title + body + time per `--uxw-center-entry` and stand alone out of context per `--uxw-self-sufficiency`.
- [ ] Every preview passes the 40-char front-load check per `--uxw-front-load` — truncation never lands on the point.
- [ ] Toast durations sit inside the 4–8s read budget and honor prefers-reduced-motion in the entrance-exit layer.
