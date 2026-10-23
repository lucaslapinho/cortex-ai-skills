"""Plugin regressions exercise malformed packages and preservation invariants."""
import importlib.util
import json
import stat
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path

spec = importlib.util.spec_from_file_location("plugin_builder", Path(__file__).with_name("build_plugin.py"))
plugin = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plugin)


class PluginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.files = plugin.payload(cls.root)

    def mutated_manifest(self, change):
        files = self.files.copy()
        manifest = json.loads(files[plugin.MANIFEST])
        change(manifest)
        files[plugin.MANIFEST] = json.dumps(manifest).encode()
        return files

    def test_seven_skills_and_links(self):
        report = plugin.validate_payload(self.files, self.root)
        self.assertEqual(len(report["skills"]), 7)
        self.assertGreater(report["relative_references"], 200)

    def test_missing_manifest(self):
        files = self.files.copy()
        files.pop(plugin.MANIFEST)
        with self.assertRaisesRegex(ValueError, "manifest missing"):
            plugin.validate_payload(files, self.root)

    def test_manifest_skills_wrong_type(self):
        files = self.mutated_manifest(lambda value: value.update(skills=["./skills/"]))
        with self.assertRaisesRegex(ValueError, "skills must"):
            plugin.validate_payload(files, self.root)

    def test_semver_rejects_invalid_identifiers(self):
        for value in ("0.1.1-01", "0.1.1-.", "0.1.1+..", "0.1.1-alpha..1", "01.1.1"):
            files = self.mutated_manifest(lambda manifest: manifest.update(version=value))
            with self.subTest(version=value), self.assertRaisesRegex(ValueError, "version"):
                plugin.validate_payload(files, self.root)
        for value in ("0.1.1", "0.1.1-rc.1", "0.1.1+build.01"):
            self.assertIsNotNone(plugin.SEMVER.fullmatch(value))

    def test_manifest_unknown_dependency_rejected(self):
        files = self.mutated_manifest(lambda value: value.update(apps="./.app.json"))
        with self.assertRaisesRegex(ValueError, "Unsupported fields"):
            plugin.validate_payload(files, self.root)

    def test_missing_skill_entrypoint(self):
        files = self.files.copy()
        files.pop("skills/cortex-detection-engineer/SKILL.md")
        with self.assertRaisesRegex(ValueError, "entrypoint missing"):
            plugin.validate_payload(files, self.root)

    def test_yaml_duplicate_and_malformed(self):
        for data in ("name: a\nname: b\n", "name: [unterminated"):
            with self.subTest(data=data), self.assertRaises((ValueError, plugin.yaml.YAMLError)):
                plugin.parse_yaml(data)

    def test_empty_skill_body(self):
        files = self.files.copy()
        files["skills/cortex-detection-engineer/SKILL.md"] = (
            b"---\nname: cortex-detection-engineer\ndescription: A detection skill\n---\n"
        )
        with self.assertRaisesRegex(ValueError, "empty instructions"):
            plugin.validate_payload(files, self.root)

    def test_missing_referenced_resource(self):
        files = self.files.copy()
        key = "skills/cortex-detection-engineer/SKILL.md"
        files[key] += b"\nRead [required fixture](references/nonexistent-fixture.md).\n"
        with self.assertRaisesRegex(ValueError, "Missing or escaping resource"):
            plugin.validate_payload(files, self.root)

    def test_missing_presentation_icon(self):
        files = self.files.copy()
        files.pop("assets/cortex-skills.svg")
        with self.assertRaisesRegex(ValueError, "presentation asset"):
            plugin.validate_payload(files, self.root)

    def test_adapter_invalid_yaml(self):
        files = self.files.copy()
        files["skills/cortex-detection-engineer/agents/openai.yaml"] = b"interface: [bad"
        with self.assertRaises(plugin.yaml.YAMLError):
            plugin.validate_payload(files, self.root)

    def test_scorer_and_nested_zip_excluded(self):
        for name in ("tests/basic.md", "references/nested.zip"):
            files = self.files.copy()
            files["skills/cortex-detection-engineer/" + name] = b"fixture"
            with self.subTest(name=name), self.assertRaises(ValueError):
                plugin.validate_payload(files, self.root)

    def test_zip_deterministic_and_hidden_manifest_retained(self):
        first = plugin.zip_bytes(self.files)
        self.assertEqual(first, plugin.zip_bytes(dict(reversed(list(self.files.items())))))
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "plugin.zip"
            path.write_bytes(first)
            self.assertEqual(plugin.read_zip(path), self.files)
            self.assertIn(plugin.MANIFEST, plugin.read_zip(path))
            report = plugin.validate_zip(path, self.root)
            self.assertTrue(report["canonical_files_identical"])

    def test_canonical_tampering_rejected(self):
        files = self.files.copy()
        files["skills/cortex-detection-engineer/examples/tampered.md"] = b"Unreviewed fixture."
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "plugin.zip"
            path.write_bytes(plugin.zip_bytes(files))
            with self.assertRaisesRegex(ValueError, "differs from canonical"):
                plugin.validate_zip(path, self.root)

    def bad_archive(self, names):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "bad.zip"
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                with zipfile.ZipFile(path, "w") as archive:
                    for name in names:
                        info = zipfile.ZipInfo("fixture")
                        # Preserve malformed spelling; Windows ZipInfo normalizes
                        # backslashes when they are passed to its constructor.
                        info.filename = name
                        archive.writestr(info, b"fixture")
            with self.assertRaises(ValueError):
                plugin.read_zip(path)

    def test_zip_duplicates_and_case_collisions(self):
        self.bad_archive(["a.md", "a.md"])
        self.bad_archive(["a.md", "A.md"])

    def test_zip_escaping_and_type_conflicts(self):
        for names in (["../outside.md"], ["/absolute.md"], ["a\\b"], ["a", "a/b"]):
            with self.subTest(names=names):
                self.bad_archive(names)

    def test_zip_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "link.zip"
            with zipfile.ZipFile(path, "w") as archive:
                info = zipfile.ZipInfo("link")
                info.create_system = 3
                info.external_attr = (stat.S_IFLNK | 0o777) << 16
                archive.writestr(info, b"outside")
            with self.assertRaisesRegex(ValueError, "Unsupported archive member"):
                plugin.read_zip(path)

    def test_zip_original_nul_name_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "nul.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("fixtureX", b"data")
            path.write_bytes(path.read_bytes().replace(b"fixtureX", b"fixture\x00"))
            with self.assertRaises(ValueError):
                plugin.read_zip(path)

    def test_two_full_builds_have_identical_artifacts(self):
        with tempfile.TemporaryDirectory() as temporary:
            first, second = Path(temporary) / "first", Path(temporary) / "second"
            plugin.build(self.root, first)
            plugin.build(self.root, second)
            self.assertEqual({p.name: p.read_bytes() for p in first.iterdir()},
                             {p.name: p.read_bytes() for p in second.iterdir()})
            with self.assertRaisesRegex(ValueError, "new directory"):
                plugin.build(self.root, first)


if __name__ == "__main__":
    unittest.main()
