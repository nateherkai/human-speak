#!/usr/bin/env python3
"""Validate the portable Human Speak skill and plugin package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "human-speak" / "SKILL.md"
REQUIRED = [
    ROOT / ".codex-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    SKILL,
    ROOT / "skills" / "human-speak" / "references" / "patterns.md",
    ROOT / "skills" / "human-speak" / "references" / "evaluation.md",
    ROOT / "skills" / "human-speak" / "references" / "top-20.md",
    ROOT / "README.md",
    ROOT / "CHANGELOG.md",
    ROOT / "LICENSE",
    ROOT / "PRIVACY.md",
    ROOT / "TERMS.md",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


for path in REQUIRED:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")

codex = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))

for label, manifest in (("Codex", codex), ("Claude", claude)):
    if manifest.get("name") != "human-speak":
        fail(f"{label} manifest name must be human-speak")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        fail(f"{label} manifest version must use strict semver")
    if not manifest.get("description"):
        fail(f"{label} manifest description is required")

if codex["version"] != claude["version"]:
    fail("Claude and Codex plugin versions must match")

if marketplace.get("name") != "human-speak":
    fail("Claude marketplace name must be human-speak")
plugins = marketplace.get("plugins")
if not isinstance(plugins, list) or len(plugins) != 1 or plugins[0].get("name") != "human-speak":
    fail("Claude marketplace must expose exactly one human-speak plugin")
if plugins[0].get("source") != "./":
    fail("Claude marketplace source must point at the repository root")

skill_text = SKILL.read_text(encoding="utf-8")
unfinished_marker = "[" + "TODO"
todo_colon = "TODO" + ":"
if unfinished_marker in skill_text or todo_colon in skill_text:
    fail("unfinished TODO found in SKILL.md")
if not skill_text.startswith("---\n"):
    fail("SKILL.md must begin with YAML frontmatter")
frontmatter = skill_text.split("---", 2)[1]
if not re.search(r"^name:\s*human-speak\s*$", frontmatter, re.MULTILINE):
    fail("SKILL.md frontmatter must declare name: human-speak")
if not re.search(r"^description:\s*\S", frontmatter, re.MULTILINE):
    fail("SKILL.md frontmatter must include a description")

version_match = re.search(r'^\s+version:\s*"([0-9.]+)"\s*$', frontmatter, re.MULTILINE)
if not version_match or version_match.group(1) != codex["version"]:
    fail("skill metadata version must match the plugin versions")

for path in (ROOT / "skills" / "human-speak").rglob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("#"):
            continue
        destination = (path.parent / target.split("#", 1)[0]).resolve()
        if not destination.is_relative_to(ROOT.resolve()) or not destination.is_file():
            fail(f"missing or nonportable reference in {path.relative_to(ROOT)}: {target}")

for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py"}:
        text = path.read_text(encoding="utf-8")
        if unfinished_marker in text:
            fail(f"unfinished placeholder in {path.relative_to(ROOT)}")

print("Human Speak package validation passed.")
