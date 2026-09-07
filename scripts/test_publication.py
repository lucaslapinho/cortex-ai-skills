"""Focused regression tests for publication validation, using synthetic data."""
import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "publication_validation", Path(__file__).with_name("validate_publication.py")
)
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


class PublicationTests(unittest.TestCase):
    def test_paths_reject_escapes(self):
        for name in ("../escape", "/absolute", "a\\b", "a/../b", "C:/path", "a//b"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                validation.safe_relative(name)

    def test_safe_path(self):
        self.assertEqual(validation.safe_relative("skill/references/a.md").as_posix(),
                         "skill/references/a.md")

    def test_secret_pattern_and_safe_placeholder(self):
        self.assertTrue(validation.sensitive(("ghp_" + "a" * 40).encode()))
        self.assertFalse(validation.sensitive(b"Use [API_KEY] as an unresolved placeholder."))

    def archive_fixture(self, directory, content):
        path = Path(directory) / "fixture.zip"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("skill/SKILL.md", content)
        return path

    def test_valid_archive(self):
        content = b"synthetic skill"
        expected = [{"path": "SKILL.md", "bytes": len(content),
                     "sha256": validation.sha256(content)}]
        with tempfile.TemporaryDirectory() as directory:
            path = self.archive_fixture(directory, content)
            self.assertEqual(validation.validate_archive(path, "skill", expected), 1)

    def test_tampered_archive_rejected(self):
        expected = [{"path": "SKILL.md", "bytes": 8,
                     "sha256": validation.sha256(b"original")}]
        with tempfile.TemporaryDirectory() as directory:
            path = self.archive_fixture(directory, b"tampered")
            with self.assertRaises(ValueError):
                validation.validate_archive(path, "skill", expected)

    def test_extra_archive_member_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.archive_fixture(directory, b"extra")
            with self.assertRaises(ValueError):
                validation.validate_archive(path, "skill", [])


if __name__ == "__main__":
    unittest.main()
