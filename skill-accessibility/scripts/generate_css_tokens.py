#!/usr/bin/env python3
"""
generate_css_tokens.py - sinh assets/css/<skill-id>.css tu skills/data.json.

data.json la nguon truth duy nhat (da duoc validate_skills.py kiem chung).
KHONG sua tay file CSS sinh ra - sua data.json roi chay lai script nay.

Cach dung:
    python3 scripts/generate_css_tokens.py            # sinh toan bo 12 file
    python3 scripts/generate_css_tokens.py dark-mode  # sinh 1 skill
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "skills" / "data.json"
OUT = ROOT / "assets" / "css"
PREFIX = "--a11y-"

HEADER = """/* ============================================================
 * {name} - starter design tokens (CSS custom properties)
 * Skill id: {sid} (#{nn} of 12)
 *
 * {summary}
 *
 * Sinh tu dong tu skills/data.json (nguon truth da duoc
 * scripts/validate_skills.py kiem chung). KHONG sua tay token values -
 * sua data.json roi chay lai script sinh token.
 * ============================================================ */
"""


def render_skill(idx: int, skill: dict) -> str:
    sid = skill["id"]
    sec = skill["sections"]
    lines = [
        HEADER.format(
            name=skill["name"],
            sid=sid,
            nn=f"{idx + 1:02d}",
            summary=skill["summary"],
        ),
        ":root {",
    ]
    for tok in sec["tokens"]:
        lines.append(f"  {PREFIX}{tok['role']}: {tok['value']}; /* {tok['notes']} */")
    lines.append("}")
    lines.append("")
    acc = sec["accessibility"]
    lines.append("/* Accessibility contract (required) */")
    lines.append(f"/* Notes: {acc['notes']} */")
    lines.append(f"/* Fallback: {acc['fallback']} */")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    data = json.loads(DATA.read_text())
    skills = data["skills"]
    wanted = sys.argv[1:] or [s["id"] for s in skills]
    OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for i, skill in enumerate(skills):
        if skill["id"] not in wanted:
            continue
        path = OUT / f"{skill['id']}.css"
        path.write_text(render_skill(i, skill))
        written.append(path.name)
    print(f"Generated {len(written)} token file(s): {', '.join(written)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
