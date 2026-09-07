"""Unit tests for the release tool; no tenant, credentials or network required."""
import hashlib
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import release
import evaluate


class ReleaseTests(unittest.TestCase):
    def test_runtime_excludes_oracles(self):
        for path in ("SKILL.md", "VERSION", "references/a.md", "templates/a.md", "examples/a.md", "agents/openai.yaml"):
            self.assertTrue(release.runtime(Path(path)), path)
        for path in ("tests/basic.md", "README.md", "VALIDATION.md", "reviews/a.md", "CHANGELOG.md", "research/a.md", "references.md"):
            self.assertFalse(release.runtime(Path(path)), path)

    def test_identity_ordinal_no_terminal_newline(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "b.md").write_bytes(b"b")
            (root / "A.md").write_bytes(b"A")
            expected = "\n".join(hashlib.sha256(v).hexdigest() + "  " + n for n, v in (("A.md", b"A"), ("b.md", b"b")))
            result = release.identity(root, [root / "b.md", root / "A.md"])
            self.assertEqual(result["sha256"], hashlib.sha256(expected.encode()).hexdigest())
            self.assertEqual(result["bytes"], 2)

    def test_archives_deterministic_and_exclusive(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            source.mkdir()
            (source / "SKILL.md").write_bytes(b"example")
            a, b = root / "a.zip", root / "b.zip"
            for output in (a, b):
                release.write_zip(output, source, [source / "SKILL.md"], "sample")
            self.assertEqual(a.read_bytes(), b.read_bytes())
            with self.assertRaises(FileExistsError):
                release.write_zip(a, source, [], "sample")
            with zipfile.ZipFile(a) as archive:
                self.assertEqual(archive.namelist(), ["sample/SKILL.md"])
                self.assertIsNone(archive.testzip())

    def test_output_scope_checked_before_writes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "source"
            root.mkdir()
            for bad in (root, root / "release", root.parent):
                with self.assertRaises(ValueError):
                    release.package(root, bad)
            with patch.object(release, "audit", return_value={"errors": ["not approved"]}):
                output = root.parent / "new-output"
                with self.assertRaises(ValueError):
                    release.package(root, output)
                self.assertFalse(output.exists())

    def test_markdown_anchors(self):
        self.assertEqual(release.anchors("# Example `value()`\n## Same\n## Same\n```\n# Not a heading\n```\n"),
                         {"example-value", "same", "same-1"})

    def test_all_case_inputs_exclude_oracle_sections(self):
        root = Path(__file__).resolve().parents[1]
        total = 0
        for skill_name, expected in zip(release.SKILLS, release.COUNTS):
            skill = root / skill_name
            ids = []
            for category in release.CATEGORIES:
                ids.extend(release.CASE.findall((skill / f"tests/{category}.md").read_text(encoding="utf-8")))
            inputs = evaluate.case_inputs(skill, ids)
            self.assertEqual(len(inputs), expected)
            for case in inputs:
                self.assertEqual(set(case), {"id", "Fixture", "Prompt"})
                self.assertTrue(case["Fixture"] and case["Prompt"])
                for excluded in ("### Expected observations", "**Expected observations**", "### Authored result", "**Authored result**"):
                    self.assertNotIn(excluded, case["Fixture"] + case["Prompt"])
            total += len(inputs)
        self.assertEqual(total, 253)

    def test_publication_link_rebase_keeps_label(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill = root / "skill"
            skill.mkdir()
            (skill / "SKILL.md").write_bytes(b"example")
            response = "Read [SKILL.md](SKILL.md)."
            self.assertEqual(evaluate.publication_links(response, skill, root / "reviews/output.md"),
                             "Read [SKILL.md](../skill/SKILL.md).")


if __name__ == "__main__":
    unittest.main()
