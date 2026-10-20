"""Exercise package validation in isolated directories without changing the checkout."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "elon-frame"
        source = Path(__file__).resolve().parents[1]
        shutil.copytree(source, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def validate(self):
        result = subprocess.run(
            [sys.executable, str(self.root / "scripts/validate.py")],
            capture_output=True, text=True, check=False,
        )
        return result.returncode, json.loads(result.stdout)

    def test_source_package_passes(self):
        code, report = self.validate()
        self.assertEqual(code, 0, report)
        self.assertEqual(report["status"], "pass")

    def test_checkout_metadata_does_not_change_package_result(self):
        _, source_report = self.validate()
        metadata = self.root / ".git"
        metadata.mkdir()
        (metadata / "index").write_bytes(b"\xff\x00")
        code, report = self.validate()
        self.assertEqual(code, 0, report)
        self.assertEqual(report, source_report)
        shutil.rmtree(metadata)
        metadata.write_text("gitdir: /not-part-of-the-package\n")
        code, report = self.validate()
        self.assertEqual(code, 0, report)
        self.assertEqual(report, source_report)

    def test_sensitive_files_and_archives_are_rejected(self):
        for name in (".env", "accidental.zip"):
            with self.subTest(name=name):
                path = self.root / name
                path.write_text("synthetic fixture only\n")
                code, report = self.validate()
                self.assertNotEqual(code, 0)
                self.assertIn("Forbidden artifact: " + name, report["errors"])
                path.unlink()

    def test_broken_reference_is_rejected(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text() + "\n[Missing reference](references/missing.md)\n")
        code, report = self.validate()
        self.assertNotEqual(code, 0)
        self.assertTrue(any("Broken or escaping link:" in e for e in report["errors"]))


    def test_discovery_fixtures_are_counted(self):
        cases = json.loads((self.root / "tests/discovery-cases.json").read_text())["cases"]
        code, report = self.validate()
        self.assertEqual(code, 0, report)
        self.assertEqual(report["manual_scenarios"], 42 + len(cases))

    def test_required_discovery_reference_is_checked(self):
        (self.root / "references/underlying-variables.md").unlink()
        code, report = self.validate()
        self.assertNotEqual(code, 0)
        self.assertIn("Missing: references/underlying-variables.md", report["errors"])

    def test_duplicate_fixture_id_is_rejected(self):
        path = self.root / "tests/discovery-cases.json"
        data = json.loads(path.read_text())
        data["cases"][0]["id"] = "Q01"
        path.write_text(json.dumps(data))
        code, report = self.validate()
        self.assertNotEqual(code, 0)
        self.assertIn("Duplicate scenario IDs", report["errors"])

    def test_invalid_fixture_json_is_reported(self):
        (self.root / "tests/discovery-cases.json").write_text("{broken")
        code, report = self.validate()
        self.assertNotEqual(code, 0)
        self.assertTrue(any("Invalid discovery cases:" in e for e in report["errors"]))


if __name__ == "__main__":
    unittest.main()
