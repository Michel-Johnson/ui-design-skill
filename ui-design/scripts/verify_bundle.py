#!/usr/bin/env python3
"""Verify bundled upstream bytes and local Markdown references without networking."""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def verify(root):
    errors = []
    manifest = json.loads((root / "references/upstream.json").read_text())
    vendor = root / manifest["bundled_path"]
    files = sorted(path for path in vendor.rglob("*") if path.is_file())
    digest = hashlib.sha256()
    for path in files:
        record = (
            path.relative_to(vendor).as_posix()
            + "\0"
            + hashlib.sha256(path.read_bytes()).hexdigest()
            + "\n"
        )
        digest.update(record.encode("utf-8"))
    if len(files) != manifest["file_count"]:
        errors.append(f"Upstream file count: {len(files)}, expected {manifest['file_count']}")
    if digest.hexdigest() != manifest["content_sha256"]:
        errors.append("Upstream contents differ from the pinned snapshot")
    skills = list((vendor / "skills").glob("*/SKILL.md"))
    if len(skills) != manifest["skill_count"]:
        errors.append(f"Upstream skill count: {len(skills)}, expected {manifest['skill_count']}")
    for required in ("SKILL.md", "agents/openai.yaml", "references/workflow.md", "references/design-standards.md"):
        if not (root / required).is_file():
            errors.append(f"Missing required file: {required}")

    checked = 0
    for path in root.rglob("*.md"):
        fence = None
        for number, line in enumerate(path.read_text().splitlines(), 1):
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if marker:
                value = marker.group(1)
                if fence is None:
                    fence = value
                elif value[0] == fence[0] and len(value) >= len(fence):
                    fence = None
                continue
            if fence:
                continue
            for link in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", line):
                parsed = urlsplit(link)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = path.parent / unquote(parsed.path)
                checked += 1
                if not target.exists():
                    errors.append(f"{path.relative_to(root)}:{number}: missing {link}")
    return errors, len(skills), len(files), checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors, skills, files, links = verify(args.root.resolve())
    except (OSError, ValueError, KeyError) as error:
        print(f"Verification failed: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Verified {skills} bundled skills, {files} upstream files and {links} local references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
