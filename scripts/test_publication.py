"""Focused regression tests for publication validation, using synthetic data."""
import importlib.util
import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "publication_validation", Path(__file__).with_name("validate_publication.py")
)
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)
plugin_spec = importlib.util.spec_from_file_location("publication_plugin", Path(__file__).with_name("build_plugin.py"))
plugin = importlib.util.module_from_spec(plugin_spec)
plugin_spec.loader.exec_module(plugin)


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

    def test_historical_release_validates_own_snapshot(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(validation.validate_plugin_release(
            root / "packages/0.1.1", plugin,
            pinned_manifest=validation.PLUGIN_011_MANIFEST_SHA256), 8)

    def test_current_source_drift_rejected(self):
        root = Path(__file__).resolve().parents[1]
        with self.assertRaisesRegex(ValueError, "canonical source"):
            validation.validate_plugin_release(root / "packages/0.1.1", plugin, canonical={})

    def test_historical_pin_rejects_mutation(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "0.1.1"
            shutil.copytree(root / "packages/0.1.1", directory)
            with (directory / "release-manifest.json").open("ab") as stream:
                stream.write(b"\n")
            with self.assertRaisesRegex(ValueError, "Historical plugin manifest changed"):
                validation.validate_plugin_release(directory, plugin, pinned_manifest=validation.PLUGIN_011_MANIFEST_SHA256)

    def test_release_checksum_detects_tampered_zip(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "0.1.1"
            shutil.copytree(root / "packages/0.1.1", directory)
            archive = next(directory.glob("*.zip"))
            with archive.open("ab") as stream:
                stream.write(b"changed")
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                validation.validate_plugin_release(directory, plugin)

    def test_release_directory_version_checked(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "wrong-version"
            shutil.copytree(root / "packages/0.1.1", directory)
            with self.assertRaisesRegex(ValueError, "version/directory mismatch"):
                validation.validate_plugin_release(directory, plugin)


if __name__ == "__main__":
    unittest.main()
