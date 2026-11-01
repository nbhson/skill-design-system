#!/usr/bin/env python3
"""
generate_css_tokens.py — regenerate assets/css/<skill-id>.css from skills/data.json.

data.json is the single source of truth (verified by scripts/validate_skills.py).
Each animation skill's `sections.tokens` becomes a set of CSS custom properties
named --motion-<role> in assets/css/<skill-id>.css, plus a reduced-motion
fallback comment block. Idempotent: safe to re-run any time data.json changes.
"""

import json, pathlib, re

ROOT = pathlib.Path(__file__).parent.parent
OUT = ROOT / "assets" / "css"

ORDER = [
    "easing-timing", "micro-interactions", "entrance-exit", "page-transitions",
    "loading-states", "feedback-confirmation", "scroll-animation", "gesture-drag",
    "data-animation", "ambient-motion", "illustration-lottie", "reduced-motion",
]


def css_var(role: str) -> str:
    return "--motion-" + role.strip().lower().replace("_", "-")


def render(skill: dict, index: int) -> str:
    sid = skill["id"]
    sec = skill["sections"]
    lines = [
        "/* ============================================================",
        f" * {skill['name']} — starter motion tokens (CSS custom properties)",
        f" * Skill id: {sid} (#{index:02d} of {len(ORDER)})",
        " *",
        f" * {skill['summary']}",
        " *",
        " * Sinh tu dong tu skills/data.json (nguon truth da duoc",
        " * scripts/validate_skills.py kiem chung). KHONG sua tay token values —",
        " * sua data.json roi chay lai script sinh token.",
        " * ============================================================ */",
        "",
        ":root {",
    ]
    for t in sec.get("tokens", []):
        notes = t.get("notes", "")
        lines.append(f"  {css_var(t['role'])}: {t['value']}; /* {notes} */")
    lines.append("}")
    rm = sec.get("reducedMotion", {})
    if rm:
        lines += [
            "",
            "/* Reduced motion (prefers-reduced-motion: reduce) */",
            f"/* {rm.get('notes', '')} */",
            f"/* Fallback: {rm.get('fallback', '')} */",
            "",
            "@media (prefers-reduced-motion: reduce) {",
            "  *, *::before, *::after {",
            "    animation-duration: 1ms !important;",
            "    animation-iteration-count: 1 !important;",
            "    transition-duration: 1ms !important;",
            "    scroll-behavior: auto !important;",
            "  }",
            "}",
        ]
    return "\n".join(lines) + "\n"


def main():
    data = json.loads((ROOT / "skills" / "data.json").read_text())
    by_id = {s["id"]: s for s in data["skills"]}
    missing = [sid for sid in ORDER if sid not in by_id]
    if missing:
        raise SystemExit(f"data.json missing skills: {missing}")
    OUT.mkdir(parents=True, exist_ok=True)
    for i, sid in enumerate(ORDER, 1):
        (OUT / f"{sid}.css").write_text(render(by_id[sid], i))
        print(f"  ✓ assets/css/{sid}.css")
    print(f"Regenerated {len(ORDER)} token files from skills/data.json")


if __name__ == "__main__":
    main()
