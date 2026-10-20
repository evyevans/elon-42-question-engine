"""Read-only static checks for the Elon Frame package; Python standard library only."""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
required = ["SKILL.md", "README.md", "LICENSE", "references/question-framework.md", "references/investigation-guide.md", "references/architecture-layers.md", "references/safety-governance.md", "references/evaluation-rubric.md", "tests/ambiguity-tests.md", "tests/adversarial-tests.md", "tests/edge-cases.md"]
for name in required:
    if not (root / name).is_file():
        errors.append("Missing: " + name)
text = (root / "SKILL.md").read_text(encoding="utf-8") if (root / "SKILL.md").exists() else ""
parts = text.split("---", 2)
fields = {}
if len(parts) != 3 or parts[0].strip():
    errors.append("Missing YAML frontmatter")
else:
    for line in parts[1].splitlines():
        if line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            fields[key] = value.strip()
name = fields.get("name", "")
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
    errors.append("Invalid name")
if name != root.name:
    errors.append("Name must match directory")
if not 1 <= len(fields.get("description", "")) <= 1024:
    errors.append("Invalid description length")
if len(text.splitlines()) >= 500:
    errors.append("Main skill exceeds preferred line budget")
count = 0
for path in root.rglob("*"):
    # Root Git metadata belongs to the checkout, not the skill package.
    if path.relative_to(root).parts[0] == ".git":
        continue
    if not path.is_file():
        continue
    count += 1
    if ".git" in path.parts or path.name.startswith(".env") or path.suffix in {".zip", ".pyc"}:
        errors.append("Forbidden artifact: " + str(path.relative_to(root)))
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append("Unexpected non-UTF-8 artifact: " + str(path))
        continue
    if path.suffix == ".md":
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            target = target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append("Broken or escaping link: " + str(path.relative_to(root)) + " -> " + target)
ids = []
for path in (root / "tests").glob("*.md"):
    ids.extend(re.findall(r"^\| ([QAE]\d{2}) \|", path.read_text(), re.M))
if len(ids) != len(set(ids)):
    errors.append("Duplicate scenario IDs")
report = {"status": "pass" if not errors else "fail", "files_checked": count, "manual_scenarios": len(ids), "behavioral_evaluations_run": 0, "errors": errors}
print(json.dumps(report, indent=2))
sys.exit(1 if errors else 0)
