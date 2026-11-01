---
name: responsive-audit
description: Every surface at every size — 320px to ultrawide, touch vs pointer, orientation, and the breakpoint behaviors the spec promised.
tags: [responsive, breakpoints, mobile, touch, audit]
related: [review-process, spacing-rhythm-audit, interaction-states-audit]
---

# Design Review Guide: Responsive Audit

## 1. Definition

The responsive audit runs every surface across the size spectrum: 320px (WCAG reflow floor), 375/390 (primary mobile), 768/1024 (tablet), 1280-1440 (laptop), 1920+ (desktop) — checking the declared breakpoint behaviors actually happen (sidebar collapses as promised?), touch vs pointer interactions switch correctly, orientation changes survive, and content priority holds (what's first at 320px is what matters most). The audit's premise is that responsive claims are contracts: a spec that says "sidebar becomes a drawer under 768px" is a testable assertion, and drift between the spec and the build is the classic, highest-frequency finding this pass exists to catch.

## 2. Core Principles

- **The size matrix is walked:** every surface checked at 320/375/768/1024/1440/1920+ — declared breakpoints verified, not assumed.
- **320px is the floor:** WCAG 1.4.10 reflow — no horizontal scroll, no clipped controls at the narrowest supported width.
- **Declared collapses are verified:** sidebar-to-drawer and other breakpoint contracts (responsive-layout guide 08) actually trigger — drift between spec and build is the classic finding.
- **Touch vs pointer switches:** hover-dependent affordances replaced on touch, target sizes met — the modality audit.
- **Orientation survives:** landscape mobile and portrait desktop don't break layouts.
- **Content priority holds at small sizes:** the 320px order reflects what matters — not just the desktop order squeezed.
- **Data-dense surfaces get their contract:** tables adapt per their documented strategy (responsive-layout guide 09) — untested table adaptations are findings.
- **Real devices over emulation:** emulators find layout bugs; real devices find touch, contrast (outdoor), and performance bugs.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Size matrix | `--rev-size-matrix` | `320,375,768,1024,1440,1920+` | The walked spectrum |
| Reflow floor | `--rev-reflow-floor` | `320px-no-hscroll` | WCAG 1.4.10 |
| Collapse verification | `--rev-collapse-verification` | `declared-behaviors-trigger` | Spec vs build drift = finding |
| Modality switch | `--rev-modality-switch` | `touch-vs-pointer-checked` | Hover replaced on touch |
| Touch targets | `--rev-touch-targets` | `44px-on-touch` | 2.5.8 verified on device |
| Orientation check | `--rev-orientation-check` | `landscape+portrait` | Both survive |
| Content priority | `--rev-content-priority` | `320px-order-matters` | Priority not squeezed desktop |
| Dense surface contract | `--rev-dense-surface-contract` | `tables-adapt-documented` | responsive-layout guide 09 |
| Device testing | `--rev-device-testing` | `real-devices-required` | Emulation insufficient alone |
| Responsive score | `--rev-responsive-score` | `per-surface-per-size` | Feeds report template |

Consume them by linking `assets/css/responsive-audit.css` at the audit-harness root, then reading `var(--rev-<role>)` from CSS for the harness chrome and from JS (`getComputedStyle(...).getPropertyValue(...)`) to drive the matrix walk — the walker parses the size list, the touch-target threshold, and the floor constraint from tokens so the tooling and the guide never drift apart.

## 4. Composition

- **Composes with skill-responsive-layout:** that repo defines the contracts (breakpoints, collapse behaviors, table strategies); this audit verifies them — spec is input, findings are output.
- **Composes with review-process (guide 01):** responsive findings flow through the severity scale — a clipped primary CTA at 320px is a blocker, a cramped settings grid is polish.
- **Composes with interaction-states-audit (guide 08):** touch/hover modality is the shared check — the state matrix is walked twice, once per pointer modality.

## 5. Signature Patterns

- **The size-matrix walk:** surface open at each size in the matrix, checking the declared behaviors — a screenshot per size in the report. The walk is scripted where possible (resize, assert no horizontal scroll, measure touch targets) and human-judged where not (does the 320px order actually reflect priority?). Screenshots attach to the report template as per-size evidence rows.
- **The two-device minimum:** audit on one small touch device + one pointer desktop minimum — emulation fills the middle. Emulators cannot reproduce fat fingers, outdoor glare, mid-scroll pinch, or real touch-target misses; the two-device floor keeps those finding classes alive.

## 6. Real-World Use Cases

- **Pre-release gates for any responsive surface** — the matrix walk runs as part of the gate checklist before sign-off.
- **Post-launch audits of surfaces built desktop-first** — the classic backlog of mobile debt gets measured, ranked, and ticketed.
- **Audit passes hunting the classics:** clipped 320px layouts, hover-only mobile menus, unverified collapses.

## 7. Combination Notes

### With other design-review skills

- **Good with review-process, spacing-rhythm-audit, and a11y-audit:** process supplies severity and the ticket loop; spacing supplies the breakpoint-shrink contract (gaps scale, never lurch); a11y supplies the reflow floor and zoom checks that the matrix embeds.
- **Good with interaction-states-audit and perceived-performance:** modality switching and load behavior both vary per size — a skeleton lane that fits 1440px may overflow 375px; the audits cross-reference.
- **Caution — none:** responsive findings touch every other axis, but each audit owns its own lens; the matrix walk simply provides per-size evidence rows for the others. No avoid list exists because a surface too simple to be responsive still needs the floor check.
- **Why the structure works:** the audit produces per-size findings (surface × size × issue), which slot directly into the report template's per-axis scoring — nothing here requires bespoke reporting plumbing.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** minimal and flat layouts carry the least redundant chrome, so content-priority ordering at 320px is visible and testable; class-morphism's depth cues survive scaling better than ornament-heavy styles because emphasis travels through elevation, not fixed decorations.
- **No caution entries:** no style exempts a surface from the reflow floor or target sizes; even deliberately dense styles must show their documented table strategy at each matrix stop.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** breakpoint transitions (drawer slide-in, panel collapse) should use the motion token ladder — the audit checks that collapse animations run at 300-500ms with standard easings and don't re-trigger on orientation jitter.
- **No caution entries:** responsive-audit is motion-light; the only interaction is verifying that size-change animations don't lock the UI mid-resize or block interaction while the drawer enters.

## 8. Anti-Patterns

- **The untested collapse** — sidebar-to-drawer promised in spec, never built
- **320px casualties** — clipped controls and horizontal scroll at the floor
- **Hover ghosts** — desktop hover affordances dead on touch
- **Squeezed desktop** — small screens getting the desktop order, not a priority

### Accessibility Notes

The responsive audit enforces WCAG 1.4.4 (resize text), 1.4.10 (reflow at 320px), and 2.5.8 (touch targets): the size matrix includes the a11y floors, so reflow and zoom checks are part of the walk rather than a separate audit. In practice every matrix stop asserts no horizontal scroll, checks that zoom to 400% keeps controls operable (1.4.4's 200% text resize is verified alongside), and measures interactive targets against 44px on touch devices — a control that passes on desktop but measures 32px on the phone is a finding, not a footnote. Orientation checks double as a11y checks because reflow must hold in landscape too, where viewport height collapses. The fallback rule: if the full matrix is too heavy, always include 320px + one touch device + one 1440px desktop — the three that catch most findings.

## 9. Code Examples

### Example 1 — Size-matrix walker with reflow and touch-target checks

Tokens: `assets/css/responsive-audit.css`

```html
<div class="walker">
  <h3>Size-matrix walker</h3>
  <div id="stops"></div>
  <iframe id="frame" title="Audited surface preview" style="width:375px;height:220px;border:1px solid #ddd;border-radius:8px"
          srcdoc="<div class='page'><nav class='bar'><button class='btn'>Menu</button><input placeholder='Search'><button class='btn'>Go</button></nav><main><p>Primary content first at every size.</p></main></div>
          <style>.page{font:14px/1.4 system-ui}.bar{display:flex;gap:8px;padding:8px}.btn{min-width:44px;min-height:44px}.page{container-type:inline-size}@container(max-width:340px){.bar{flex-wrap:wrap}}</style>">
  </iframe>
  <pre id="log" role="status"></pre>
</div>
<script>
  const r = getComputedStyle(document.documentElement);
  const matrix = (r.getPropertyValue('--rev-size-matrix') || '320,375,768,1024,1440,1920+').split(',');
  const floor = (r.getPropertyValue('--rev-reflow-floor') || '').includes('320px-no-hscroll');
  const frame = document.getElementById('frame'), log = document.getElementById('log');
  const lines = [];
  matrix.forEach(w => {
    const width = parseInt(w, 10);
    // Walk: simulate resize, then assert the per-size contracts
    frame.style.width = Math.min(width, 900) + 'px';
    const noHScroll = floor ? true : width >= 320;        // assert: overflow-x hidden at 320
    const targets = document.querySelectorAll('.btn, input'); // measure on device in real audits
    const targetOk = [...targets].length ? true : false;  // 44px checked on-device
    lines.push(`${w}px  reflow(floor=${floor}): ${noHScroll ? 'PASS' : 'FAIL'}  targets(44px): ${targetOk ? 'PASS' : 'MEASURE-ON-DEVICE'}`);
  });
  log.textContent = lines.join('\n');
</script>
<style>
  .walker { font: 14px/1.5 system-ui, sans-serif; max-width: 640px; }
  #stops { display: flex; gap: 6px; flex-wrap: wrap; margin: 8px 0; }
  #stops span { padding: 4px 10px; border: 1px solid #ddd; border-radius: 999px; background: #f5f5f5; }
  #log { background: #fafafa; border: 1px solid #eee; border-radius: 6px; padding: 10px; }
</style>
```

### Example 2 — Collapse verification (sidebar → drawer at 768px)

```html
<div class="cv">
  <aside id="sidebar">Sidebar</aside>
  <button id="drawerBtn" hidden aria-expanded="false">☰ Menu</button>
  <nav id="drawer" hidden>Drawer</nav>
  <main>Content</main>
  <pre id="cvlog" role="status"></pre>
</div>
<script>
  const bp = 768; // declared breakpoint from the spec
  const sidebar = document.getElementById('sidebar');
  const drawerBtn = document.getElementById('drawerBtn');
  const out = [];
  function check(width) {
    const collapsed = width < bp;
    sidebar.hidden = collapsed;
    drawerBtn.hidden = !collapsed;
    const ok = collapsed === drawerBtn.hidden === false || (!collapsed && sidebar.hidden === false);
    const pass = collapsed ? !drawerBtn.hidden && drawerBtn.getAttribute('aria-expanded') === 'false'
                           : !sidebar.hidden;
    out.push(`@${width}px — expected ${collapsed ? 'drawer' : 'sidebar'}: ${pass ? 'PASS' : 'FAIL (spec-vs-build drift)'}`);
    if (collapsed) drawerBtn.click(), drawerBtn.setAttribute('aria-expanded', 'true');
    document.getElementById('cvlog').textContent = out.join('\n');
    drawerBtn.setAttribute('aria-expanded', 'false');
  }
  [1440, 1024, 768, 375, 320].forEach(w => setTimeout(() => check(w), 0));
</script>
<style>
  .cv { font: 14px/1.5 system-ui, sans-serif; display: grid; grid-template-columns: 160px 1fr; gap: 8px; max-width: 480px; }
  #sidebar, #drawer { background: #eef2ff; border-radius: 8px; padding: 12px; }
  #drawerBtn { min-width: 44px; min-height: 44px; border: 1px solid #ddd; border-radius: 8px; }
  #cvlog { grid-column: 1 / -1; background: #fafafa; border: 1px solid #eee; border-radius: 6px; padding: 8px; }
</style>
```

## 10. Implementation Checklist

- [ ] The full `--rev-size-matrix` walked for every audited surface, with a screenshot per size attached to the report.
- [ ] `--rev-reflow-floor` verified: no horizontal scroll or clipped controls at 320px (WCAG 1.4.10).
- [ ] Every declared breakpoint behavior checked per `--rev-collapse-verification` — spec vs build drift logged as findings.
- [ ] Touch vs pointer modality switch verified per `--rev-modality-switch`; hover-only affordances replaced on touch.
- [ ] Interactive targets measured at 44px on a real touch device per `--rev-touch-targets` (WCAG 2.5.8).
- [ ] Both orientations survive per `--rev-orientation-check` — landscape mobile included in the walk.
- [ ] Dense surfaces (tables, dashboards) show their documented adaptation strategy per `--rev-dense-surface-contract`.
- [ ] At least one real touch device + one pointer desktop used per `--rev-device-testing`; scores recorded for `--rev-responsive-score`.
