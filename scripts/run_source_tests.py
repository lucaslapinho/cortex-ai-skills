"""Run unchanged 0.1.0 tests with a canonical temporary directory.

Windows runners can expose an 8.3 alias through TEMP. The historical link
helper expects a canonical base, as supplied by its production CLI. Normalize
the fixture location without rewriting source bytes, skipping tests or patches.
"""
from pathlib import Path
import tempfile
import unittest


def main():
    original = Path(tempfile.gettempdir())
    canonical = original.resolve(strict=True)
    print(f"Canonical temporary-directory spelling changed: {str(original) != str(canonical)}", flush=True)
    tempfile.tempdir = str(canonical)
    test_root = Path(__file__).resolve().parents[1] / "source/tools"
    suite = unittest.defaultTestLoader.discover(str(test_root), pattern="test_release.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
