from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.audit_wiki import audit


class RepositoryStatusTests(unittest.TestCase):
    def make_project(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        docs = root / "docs"
        docs.mkdir()
        config = root / "zensical.toml"
        config.write_text('[project]\ndocs_dir = "docs"\nnav = ["index.md"]\n', encoding="utf-8")
        (docs / "index.md").write_text(
            "---\ntitle: Home\nstatus: expanding\n---\n\n# Home\n",
            encoding="utf-8",
        )
        return temp, docs, config

    def test_accepts_existing_expanding_status(self) -> None:
        temp, docs, config = self.make_project()
        self.addCleanup(temp.cleanup)

        result = audit(docs, config)
        invalid = [issue for issue in result["issues"] if issue.code == "status-invalid"]
        self.assertEqual(invalid, [])

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


if __name__ == "__main__":
    unittest.main()
