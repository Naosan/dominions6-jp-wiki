from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.audit_wiki import LEGACY_STATUSES, audit


class RepositoryStatusTests(unittest.TestCase):
    def make_project(self, index_status: str = "draft") -> tuple[tempfile.TemporaryDirectory[str], Path, Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        docs = root / "docs"
        docs.mkdir()
        config = root / "zensical.toml"
        config.write_text('[project]\ndocs_dir = "docs"\nnav = ["index.md"]\n', encoding="utf-8")
        (docs / "index.md").write_text(
            f"---\ntitle: Home\nstatus: {index_status}\n---\n\n# Home\n",
            encoding="utf-8",
        )
        return temp, docs, config

    def test_legacy_statuses_warn_without_blocking(self) -> None:
        for status in sorted(LEGACY_STATUSES):
            with self.subTest(status=status):
                temp, docs, config = self.make_project(status)
                try:
                    result = audit(docs, config)
                    errors = [issue for issue in result["issues"] if issue.severity == "error"]
                    legacy = [issue for issue in result["issues"] if issue.code == "status-legacy"]
                    self.assertEqual(errors, [])
                    self.assertEqual(len(legacy), 1)
                    self.assertIn(status, legacy[0].message)
                finally:
                    temp.cleanup()

    def test_generated_status_is_valid_and_not_orphaned(self) -> None:
        temp, docs, config = self.make_project()
        self.addCleanup(temp.cleanup)
        generated = docs / "generated-page.md"
        generated.write_text(
            "---\ntitle: Generated\nstatus: generated\n---\n\n# Generated\n",
            encoding="utf-8",
        )

        result = audit(docs, config)
        errors = [issue for issue in result["issues"] if issue.severity == "error"]
        self.assertEqual(errors, [])
        self.assertNotIn("generated-page.md", result["orphan_pages"])
        self.assertFalse(any(issue.code == "status-legacy" for issue in result["issues"]))

    def test_unknown_status_remains_an_error(self) -> None:
        temp, docs, config = self.make_project("typo-status")
        self.addCleanup(temp.cleanup)

        result = audit(docs, config)
        invalid = [issue for issue in result["issues"] if issue.code == "status-invalid"]
        self.assertEqual(len(invalid), 1)
        self.assertEqual(invalid[0].severity, "error")


if __name__ == "__main__":
    unittest.main()
