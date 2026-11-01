---
name: mobile-navigation
description: Bottom bars, drawers, and the thumb zone — navigation patterns that work at 360px with one thumb, and when to collapse what.
tags: [mobile, navigation, drawers, touch, bottom-bar]
related: [breakpoints-strategy, layout-compositions, data-tables-responsive]
---

# Responsive Layout Skill: Mobile Navigation

## 1. Definition

Mobile navigation reorganizes for a 360px viewport and a thumb-reachable zone: top bars shrink to logo + actions, primary destinations move to a bottom bar (3–5 items), everything else tucks into drawers or full-screen menus. The craft is deciding what earns a bottom-bar slot, what collapses, and how the drawer preserves focus and context (a11y repo guides 03/04). Navigation is the highest-traffic surface of any product, so its mobile adaptation is not a styling exercise — it is an information-architecture decision backed by usage data, wrapped in a dialog-contract implementation for anything that slides in. Get it right and the whole product feels native to the hand; get it wrong and users discover features only by accident.

## 2. Core Principles

- **3–5 items in the bottom bar:** thumb-reachable, icon + label, current item visually and semantically marked (`aria-current`) — the double signal serves sighted and assistive users alike.
- **Thumb zone rules:** primary actions bottom-right for right-handed reach; destructive actions away from the thumb's resting arc so accidents require intent.
- **Top bar shrinks, never stacks:** 56px max; logo + title + one-two actions; everything else moves down — the top bar is not a storage unit.
- **Drawers and sheets for secondary nav:** slide-in panels with focus trap, Escape/scrim close, and focus return (dialog contract) — a drawer without focus management is a keyboard trap waiting to ship.
- **Menus collapse by importance, not alphabet:** the nav audit ranks destinations by frequency; the cut line is data-driven, so the bar holds what users actually touch.
- **Breadcrumb or back over deep menus:** mobile hierarchy favors back-stack and breadcrumbs over mega-menus — depth is traversed linearly, not scanned laterally.
- **44px targets everywhere:** nav items meet the touch floor; icon-only items get labels or aria-label (a11y repo 2.5.8) — fingers are not cursors.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Bottom bar items | `--layout-mobnav-bottom-bar-items` | `3-5` | Thumb-zone primary destinations |
| Bar height | `--layout-mobnav-bar-height` | `56px` | Top bar ceiling on mobile |
| Target size | `--layout-mobnav-target-size` | `44px` | WCAG 2.5.8 floor for nav items |
| Drawer width | `--layout-mobnav-drawer-width` | `min(84vw, 360px)` | Slide-in drawer width cap |
| Drawer motion | `--layout-mobnav-drawer-motion` | `240ms ease-standard` | Motion tokens from skill-animation |
| Current mark | `--layout-mobnav-current-mark` | `aria-current+visual` | Current page: semantic + visual (double signal) |
| Icon + label | `--layout-mobnav-icon-plus-label` | `always` | Bottom bar icons carry labels (recognition over recall) |
| Scrim | `--layout-mobnav-scrim` | `rgba(0,0,0,0.60)` | Drawer scrim; dismiss on tap |
| Collapse rank | `--layout-mobnav-collapse-rank` | `by-usage-data` | Cut line from analytics, not alphabet |
| Safe area | `--layout-mobnav-safe-area` | `env(safe-area-inset-*)` | Notched-device bottom padding |

Consume them by linking `assets/css/mobile-navigation.css` at the app root, then referencing `var(--layout-mobnav-...)` in the shell components — bar height, drawer width, target size, and scrim are policy, not per-screen choices. The safe-area token in particular must wrap every bottom-anchored surface, or notched devices clip the very controls users reach for most.

## 4. Composition

- **Composes with breakpoints-strategy:** nav collapse is the lg-tier change — the bottom bar appears and the desktop sidebar becomes a drawer; the tier map and the nav contract must name the same widths.
- **Composes with layout-compositions:** the shell composition declares its mobile nav contract (which composition collapses to what) so pages never invent their own collapse behavior.
- **Composes with a11y focus-management:** drawers implement the trap-and-return dialog contract exactly — open moves focus in, Escape/scrim closes, focus returns to the trigger, and the background is inert.

## 5. Signature Patterns

- **Bottom-bar + drawer stack:** primary destinations in the bar, the long tail in a "More" sheet — the standard mobile IA that keeps discovery alive without cramming the bar.
- **Nav-collapse contract:** the layout catalog documents where each nav tier lives (desktop sidebar / tablet drawer / mobile bar+sheet); the collapse is designed once, not rediscovered per page.

## 6. Real-World Use Cases

- **Responsive web apps adapting desktop IA to mobile:** the sidebar hierarchy becomes bar + drawer without changing destination URLs.
- **PWA/mobile-first products designing thumb-first from the start:** navigation born in the bottom zone rather than retrofitted from desktop.
- **Audit:** unlabeled icon nav, unreachable menus, trap-less drawers — the three findings that define a failing mobile nav.

## 7. Combination Notes

### With other responsive-layout skills

- **Good with grid-systems, breakpoints-strategy, fluid-container-queries, flexbox-patterns, css-grid-patterns, layout-compositions, responsive-images, intrinsic-design, rtl-i18n-layout, responsive-testing:** the mobile shell is built from the same vocabulary — flex for the bar itself, grid for the shell, breakpoints for the collapse tier, RTL mirroring for the drawer, and responsive-testing to verify the collapse at each width. Composition is seamless because navigation collapse is just the most visible tier-driven change.
- **Caution with data-tables-responsive:** both skills fight for the same scarce vertical space on small screens. A bottom bar plus a table's sticky header plus its scroll container can leave almost no viewport for rows — the failure is *uncoordinated* stickiness, two components each claiming the bottom of the screen, discovered only in device QA. Coordinate: the bar and the table's chrome must share a height budget, and table-heavy screens may justify hiding the bar on scroll (never stacking two sticky layers without a plan).

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and glassmorphism:** a 3–5 item bar with labels is inherently minimal; flat-design keeps bar chrome cheap to render; glassmorphism suits the floating bar/drawer treatment (backdrop blur over the scrim) — all three styles flatter a restrained, labeled, thumb-first nav.
- **Caution with skeuomorphism:** heavy bevels, textured bars, and faux-3D chrome inflate the visual weight of a 56px bar and fight the 44px target discipline (padding eaten by ornament). If a skeuomorphic direction is required, apply it to surfaces, never to hit-target geometry.

### With motion skills (companion repo skill-animation)

- **Good affinity with page-transitions and feedback-confirmation:** drawer/sheet slides use the drawer motion token (240ms ease-standard, from the animation repo's easing family), and navigation taps confirm with a brief feedback cue — transition timing makes the IA legible, showing where the drawer came from and where focus landed.
- **No caution list:** because all drawer motion is dismissible by Escape/scrim and duration-bounded by tokens; the one standing rule is to honor `prefers-reduced-motion` by swapping the slide for an instant reveal, which the animation repo's motion tokens encode.

## 8. Anti-Patterns

- **Hamburger everything** — all navigation hidden behind one icon - discovery dies
- **Icon-only bottom bars** — unlabeled glyphs users must memorize
- **Top-bar overflow** — 8 actions crammed into a 56px bar
- **Trap-less drawers** — slide-ins without focus management or Escape

### Accessibility Notes

Mobile nav is an a11y hotspot: bottom-bar items need `aria-current` plus labels, drawers need the full dialog contract (focus trap, Escape, focus return), and 44px targets (WCAG 2.5.8) are the floor — see a11y repo guides 03/04/06. The double-signal rule (semantic + visual current mark) and label-always rule exist because icon-only navigation fails both low-vision users and users meeting the icons for the first time. The fallback rule is pragmatic: if drawer focus management cannot be built in time, use a full-page menu — normal document flow, no trap, accessible by default. A simpler accessible pattern always beats a fancier broken one.

## 9. Code Examples

### Example 1 — Bottom bar with labels, aria-current, and safe-area padding

Tokens: `assets/css/mobile-navigation.css`

```html
<nav class="bottombar" aria-label="Primary">
  <a href="/" class="bar-item" aria-current="page">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11l9-8 9 8v10a1 1 0 01-1 1h-5v-6h-6v6H4a1 1 0 01-1-1z"/></svg>
    <span>Home</span>
  </a>
  <a href="/search" class="bar-item">
    <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/></svg>
    <span>Search</span>
  </a>
  <a href="/orders" class="bar-item">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h12l1 20H5z"/></svg>
    <span>Orders</span>
  </a>
  <button class="bar-item" aria-expanded="false" aria-haspopup="dialog" id="moreTrigger">
    <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="12" r="2"/></svg>
    <span>More</span>
  </button>
</nav>
<style>
  .bottombar {
    position: fixed; inset-inline: 0; bottom: 0; display: flex;
    height: 56px; background: #fff; border-top: 1px solid #e5e5e5; /* var(--layout-mobnav-bar-height) */
    padding-bottom: env(safe-area-inset-bottom, 0px); /* var(--layout-mobnav-safe-area) */
  }
  .bar-item {
    flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 2px; min-width: 44px; min-height: 44px; /* var(--layout-mobnav-target-size) */
    border: none; background: none; text-decoration: none; cursor: pointer;
    font: 11px/1 system-ui, sans-serif; color: #525252;
  }
  .bar-item svg { width: 22px; height: 22px; } .bar-item[aria-current="page"] { color: #171717; font-weight: 600; } /* visual half of the double signal */
</style>
```

### Example 2 — Drawer with full trap-and-return focus contract

```html
<button id="menuTrigger" aria-expanded="false" aria-haspopup="dialog">Menu</button>
<div class="scrim" id="scrim" hidden></div>
<aside class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Site menu" hidden>
  <h2>Site menu</h2>
  <a href="/pricing">Pricing</a> <a href="/docs">Docs</a> <a href="/support">Support</a>
  <button id="drawerClose">Close menu</button>
</aside>
<style>
  .scrim { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.60); } /* var(--layout-mobnav-scrim) */
  .drawer {
    position: fixed; top: 0; bottom: 0; inset-inline-start: 0;
    width: min(84vw, 360px); background: #fff; padding: 24px 16px; /* var(--layout-mobnav-drawer-width) */
    transform: translateX(-100%); transition: transform 240ms ease-standard; /* var(--layout-mobnav-drawer-motion) */
    display: flex; flex-direction: column; gap: 4px; font: 15px/1.4 system-ui, sans-serif;
  }
  .drawer.open { transform: translateX(0); } [dir="rtl"] .drawer { transform: translateX(100%); }
  .drawer a { display: flex; align-items: center; min-height: 44px; padding: 12px 8px; } /* target floor */
  .drawer h2 { margin: 0 8px 8px; font-size: 16px; }
</style>
<script>
  const trigger = document.getElementById('menuTrigger'), scrim = document.getElementById('scrim');
  const drawer = document.getElementById('drawer'), closeBtn = document.getElementById('drawerClose');
  let lastFocused = null;
  function openDrawer() {
    lastFocused = document.activeElement;
    scrim.hidden = drawer.hidden = false;
    requestAnimationFrame(() => drawer.classList.add('open'));
    trigger.setAttribute('aria-expanded', 'true');
    closeBtn.focus();                        // move focus in
    document.addEventListener('keydown', onKeydown);
  }
  function closeDrawer() {
    drawer.classList.remove('open');
    trigger.setAttribute('aria-expanded', 'false');
    scrim.hidden = drawer.hidden = true;
    lastFocused?.focus();                    // return focus
    document.removeEventListener('keydown', onKeydown);
  }
  function onKeydown(e) {
    if (e.key === 'Escape') return closeDrawer();
    if (e.key === 'Tab') {                   // focus trap
      const items = [...drawer.querySelectorAll('a, button')], first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
      else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
    }
  }
  trigger.addEventListener('click', openDrawer); closeBtn.addEventListener('click', closeDrawer);
  scrim.addEventListener('click', closeDrawer);
</script>
```

## 10. Implementation Checklist

- [ ] The bottom bar holds 3–5 destinations (var(--layout-mobnav-bottom-bar-items)), ranked by usage data (var(--layout-mobnav-collapse-rank)) — not alphabet, not org chart.
- [ ] Every bar item is icon + label (var(--layout-mobnav-icon-plus-label)); icon-only items elsewhere carry aria-label.
- [ ] The current destination is marked with `aria-current="page"` AND a visual style (var(--layout-mobnav-current-mark)) — the double signal.
- [ ] All nav targets meet the 44px floor (var(--layout-mobnav-target-size)); the top bar stays at or under 56px (var(--layout-mobnav-bar-height)).
- [ ] Drawers implement the full dialog contract: focus trap, Escape close, scrim dismiss (var(--layout-mobnav-scrim)), and focus return to the trigger.
- [ ] Drawer width is capped at var(--layout-mobnav-drawer-width) and motion uses var(--layout-mobnav-drawer-motion) with a `prefers-reduced-motion` instant path.
- [ ] Every bottom-anchored surface pads for var(--layout-mobnav-safe-area) (env(safe-area-inset-*)).
- [ ] The nav-collapse contract is documented in the layout catalog: desktop sidebar / tablet drawer / mobile bar + More sheet.
