#!/usr/bin/env python3
"""
validate_skills.py - CI check for skill-animation repository.

Checks:
  1. All 12 animation SKILL.md files exist and parseable
  2. data.json is valid JSON and has all 12 skill IDs
  3. Anti-patterns in data.json match SKILL.md section 8
  4. Token values are well-formed (durations, easings, springs, budgets)
  5. data.json combination graph is symmetric (good/good, caution/caution, avoid/avoid)
  6. README Combination Matrix symbols match data.json combinations exactly
  7. Reference links are well-formed URLs
  8. CSS token files in assets/css/ exist per skill and match data.json token values
  9. .gitignore covers noise files and no .DS_Store exists (auto-removed if found)
  10. SKILL.md guides expose sections 9 & 10; data.json exposes a `reducedMotion`
      section per skill

Exit 0 on success, non-zero on any failure.
"""

import json, re, sys, urllib.parse, pathlib

ROOT = pathlib.Path(__file__).parent.parent
EXIT_CODE = 0

def fail(msg: str):
    global EXIT_CODE
    print(f"FAIL: {msg}")
    EXIT_CODE = 1

def norm_key(text: str) -> str:
    return re.sub(r'\s+', ' ', re.sub(r'\*\*|`', '', text)).strip()[:60]

expected_skills = [
    "easing-timing", "micro-interactions", "entrance-exit", "page-transitions",
    "loading-states", "feedback-confirmation", "scroll-animation", "gesture-drag",
    "data-animation", "ambient-motion", "illustration-lottie", "reduced-motion",
]

print("1. SKILL.md existence check:")
skills_dir = ROOT / "skills"
md_by_id = {}
for p in skills_dir.glob("*/SKILL.md"):
    fm = re.search(r"^name:\s*(\S+)\s*$", p.read_text(), re.M)
    if fm:
        md_by_id[fm.group(1)] = p
for sid in expected_skills:
    print(f"  {'✓' if sid in md_by_id else '✗'} {sid}")
    if sid not in md_by_id:
        fail(f"missing SKILL.md for {sid}")

print("\n2. data.json validity:")
try:
    data = json.loads((skills_dir / "data.json").read_text())
    ids = {s["id"] for s in data["skills"]}
    missing = set(expected_skills) - ids
    extra = ids - set(expected_skills)
    if missing: fail(f"Missing skills in data.json: {missing}")
    if extra:   fail(f"Extra skills in data.json: {extra}")
    if not missing and not extra:
        print(f"  ✓ valid JSON, all {len(expected_skills)} skills present")
except Exception as e:
    fail(f"data.json is not valid JSON: {e}")
    sys.exit(1)

by_id = {s["id"]: s for s in data["skills"]}

print("\n3. Anti-patterns consistency:")
for sid in expected_skills:
    s = by_id[sid]
    ap_json = [norm_key(x) for x in s["sections"].get("antiPatterns", [])]
    md_text = md_by_id[sid].read_text()
    m = re.search(r'\n## 8\. Anti-Patterns\s*\n(.*?)(?=\n## |\Z)', md_text, re.S)
    ap_md = []
    if m:
        for line in m.group(1).splitlines():
            line = line.strip()
            if line.startswith('- **'):
                cleaned = re.sub(r'^- \*\*', '', line)
                cleaned = re.sub(r'\*\*$', '', cleaned).strip()
                cleaned = re.sub(r':\s*$', '', cleaned).strip()
                ap_md.append(norm_key(cleaned))
            elif line.startswith('- '):
                ap_md.append(norm_key(line[2:].strip()))
    if set(ap_md) != set(ap_json):
        fail(f"  {sid}: anti-patterns mismatch — {set(ap_md) ^ set(ap_json)}")
    else:
        print(f"  ✓ {sid} ({len(ap_md)} items)")

print("\n4. Token value format:")
TOKEN_RE = re.compile(r'^[0-9.]+(ms|s|px|%|deg|KB|px/s)$|^cubic-bezier\([0-9., -]+\)$|^linear$|^scale\([0-9.]+\)$|^translate[YX3d]*\(-?[0-9.]+(px|%)*\)$|^rotate\(-?[0-9.]+deg\)$|^[0-9.]+$|^[a-z\-]+ [0-9]+(, [a-z\-]+ [0-9]+)*$|^[0-9]+px/s$|^-?[0-9.]+[a-z%]*(-[0-9.]+[a-z%]*)?$|^translate3d\(-?[0-9.]+%, -?[0-9.]+%, 0\)$|^scaleX$|^stiffness [0-9]+, damping [0-9]+$|^paused$|^[0-9.]+ms cubic-bezier\([0-9., -]+\)$|^0 [0-9]+px [0-9]+px rgba\(0, ?0, ?0, ?0\.[0-9]+\)')
bad = 0
for sid in expected_skills:
    for t in by_id[sid]["sections"].get("tokens", []):
        v = t.get("value", "")
        if not v or not TOKEN_RE.match(v):
            fail(f"  {sid}/{t['role']}: suspicious token value '{v}'")
            bad += 1
if not bad:
    total = sum(len(s["sections"].get("tokens", [])) for s in data["skills"])
    print(f"  ✓ All {total} token entries well-formed")

print("\n5. Combination graph symmetry:")
sym_errors = 0
for sid in expected_skills:
    com = by_id[sid]["sections"].get("combinations", {})
    for tier in ("good", "caution", "avoid"):
        for other in com.get(tier, []):
            if other not in ids:
                fail(f"  {sid} → {other}: target not in skill list"); continue
            rev = by_id[other]["sections"].get("combinations", {}).get(tier, [])
            if sid not in rev:
                fail(f"  {sid} —{tier}→ {other}: not reciprocated")
                sym_errors += 1
if sym_errors == 0:
    n = sum(len(by_id[s]["sections"]["combinations"].get(t, []))
            for s in expected_skills for t in ("good", "caution", "avoid"))
    print(f"  ✓ All {n} combination entries are mutually symmetric")

print("\n6. README matrix ↔ data.json consistency:")
readme = (ROOT / "README.md").read_text()
m_heading = re.search(r'^#+.*Combination Matrix.*$', readme, re.M)
if not m_heading:
    fail("  README: Combination Matrix heading not found")
else:
    after = readme[m_heading.end():]
    m_matrix = re.search(r'((?:^\|.*\|\s*$\n?)+)', after, re.M)
    MATRIX_ABBS = {
        "ease": "easing-timing", "micro": "micro-interactions", "enter": "entrance-exit",
        "page": "page-transitions", "load": "loading-states", "feed": "feedback-confirmation",
        "scroll": "scroll-animation", "drag": "gesture-drag", "data": "data-animation",
        "amb": "ambient-motion", "lottie": "illustration-lottie", "rm": "reduced-motion",
    }
    FULL = {s["name"].lower(): s["id"] for s in data["skills"]}
    SYMBOL_TO_TIER = {"✅": "good", "⚠": "caution", "❌": "avoid"}
    def norm_symbol(cell):
        cell = cell.strip().replace("\ufe0f", "")
        for sym, tier in SYMBOL_TO_TIER.items():
            if cell.startswith(sym): return tier
        return None if cell in ("—", "-", "") else "UNKNOWN"
    def tier_of(row_id, col_id):
        com = by_id[row_id]["sections"].get("combinations", {})
        for tier in ("good", "caution", "avoid"):
            if col_id in com.get(tier, []): return tier
        return None
    if not m_matrix:
        fail("  README: matrix table not found")
    else:
        rows = m_matrix.group(1).strip().splitlines()
        header = [c.strip() for c in rows[0].strip().strip("|").split("|")]
        col_ids = [MATRIX_ABBS.get(c.lower()) for c in header[1:]]
        if any(c is None for c in col_ids):
            fail(f"  README: unrecognized matrix columns: {[c for c in header[1:] if c.lower() not in MATRIX_ABBS]}")
        row_errors = 0; checked = 0; seen = set(); cells = {}
        for row in rows[2:]:
            cs = [c.strip() for c in row.strip().strip("|").split("|")]
            row_id = FULL.get(cs[0].replace("*", "").strip().lower())
            if row_id is None:
                fail(f"  README: unrecognized matrix row '{cs[0]}'"); row_errors += 1; continue
            for i, col_id in enumerate(col_ids):
                if col_id is None: continue
                t = norm_symbol(cs[i + 1])
                cells[(row_id, col_id)] = t
                if col_id == row_id:
                    if t is not None:
                        fail(f"  README: diagonal {row_id}×{row_id} should be '—'"); row_errors += 1
                    continue
                if t == "UNKNOWN":
                    fail(f"  README: {row_id}×{col_id}: unknown symbol"); row_errors += 1; continue
                expected = tier_of(row_id, col_id)
                checked += 1; seen.add((row_id, col_id))
                if t != expected:
                    fail(f"  README: {row_id}×{col_id} shows '{t or '—'}' but data.json says '{expected or 'none'}'")
                    row_errors += 1
        for (a, b), t in cells.items():
            if a != b and (a, b) in seen and cells.get((b, a)) != t:
                fail(f"  README: matrix not symmetric {a}×{b}='{t}' vs {b}×{a}='{cells.get((b, a))}'")
                row_errors += 1
        missing_pairs = [(a, b) for a in ids for b in ids if a != b and (a, b) not in seen]
        if missing_pairs:
            fail(f"  README: matrix missing {len(missing_pairs)} pair(s): {missing_pairs[:4]}")
            row_errors += 1
        if row_errors == 0:
            print(f"  ✓ All {checked} matrix cells match data.json (full 12×12 coverage, symmetric)")

print("\n7. Reference URLs:")
fr = skills_dir / "assets" / "references.md"
if fr.exists():
    urls = re.findall(r'https?://[^\s\)]+', fr.read_text())
    bad_urls = [u for u in urls if not urllib.parse.urlparse(u).netloc]
    if bad_urls: fail(f"  Malformed URLs: {bad_urls}")
    else: print(f"  ✓ {len(urls)} URL(s) well-formed")
else:
    fail("  skills/assets/references.md not found")

print("\n8. CSS token files (assets/css):")
css_dir = ROOT / "assets" / "css"
for sid in expected_skills:
    css_path = css_dir / f"{sid}.css"
    if not css_path.exists():
        fail(f"missing assets/css/{sid}.css"); continue
    css_text = css_path.read_text()
    for t in by_id[sid]["sections"].get("tokens", []):
        var = "--motion-" + t["role"].strip().lower().replace("_", "-")
        if var not in css_text:
            fail(f"assets/css/{sid}.css missing variable {var} ({t['role']})")
        elif t["value"] not in css_text:
            fail(f"assets/css/{sid}.css value drift for {var}: expected '{t['value']}'")
    print(f"  ✓ {sid}.css matches data.json tokens")
extra_css = {p.stem for p in css_dir.glob("*.css")} - set(expected_skills)
if extra_css:
    fail(f"CSS files without matching skill in data.json: {extra_css}")

print("\n9. .gitignore coverage & .DS_Store:")
gi_path = ROOT / ".gitignore"
gi = gi_path.read_text() if gi_path.exists() else ""
for f in [".DS_Store", "*.pyc", "__pycache__"]:
    if f in gi or f.replace("*", "") in gi: print(f"  ✓ '{f}' covered")
    else: fail(f"  '{f}' not covered in .gitignore")
ds = [p for p in ROOT.rglob(".DS_Store") if ".git/" not in str(p.relative_to(ROOT))]
for p in ds:
    try:
        p.unlink(); print(f"  🗑 removed {p.relative_to(ROOT)}")
    except OSError as e:
        fail(f"  could not delete {p}: {e}")
if ds: fail(f"{len(ds)} .DS_Store file(s) found and deleted")
else: print("  ✓ no .DS_Store files in repo")

print("\n10. Extended sections & reducedMotion data:")
for sid in expected_skills:
    md_text = md_by_id[sid].read_text()
    for heading, label in ((r"## 9\. Code Examples", "9. Code Examples"),
                           (r"## 10\. Implementation Checklist", "10. Implementation Checklist")):
        if not re.search(heading, md_text):
            fail(f"  {sid}: SKILL.md missing section '{label}'")
    rm = by_id[sid]["sections"].get("reducedMotion", {})
    if not rm.get("notes") or not rm.get("fallback"):
        fail(f"  {sid}: data.json `reducedMotion` missing notes/fallback")
    else:
        print(f"  ✓ {sid}: sections 9+10 present, reducedMotion declared")

print(f"\n{'─'*40}")
if EXIT_CODE == 0:
    print("All checks passed ✓")
else:
    print(f"FAILED — {EXIT_CODE} check(s) failed")
sys.exit(EXIT_CODE)
