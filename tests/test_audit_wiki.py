from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.audit_wiki import (
    audit,
    markdown_links,
    front_matter,
    resolve_link,
)


class FrontMatterTests(unittest.TestCase):
    def test_reads_top_level_fields(self) -> None:
        present, values, error = front_matter(
            '---\ntitle: "Example"\nstatus: draft\n---\n\n# Example\n'
        )
        self.assertTrue(present)
        self.assertIsNone(error)
        self.assertEqual(values["title"], "Example")
        self.assertEqual(values["status"], "draft")

    def test_reports_missing_closing_delimiter(self) -> None:
        present, _values, error = front_matter("---\ntitle: Broken\n")
        self.assertTrue(present)
        self.assertIsNotNone(error)


class LinkTests(unittest.TestCase):
    def test_ignores_fenced_code_and_keeps_real_link(self) -> None:
        text = """[real](guide.md)

```markdown
[fake](missing.md)
```
"""
        self.assertEqual(list(markdown_links(text)), [(1, "guide.md")])

    def test_resolves_directory_index(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            docs = Path(temp) / "docs"
            section = docs / "section"
            section.mkdir(parents=True)
            source = docs / "index.md"
            source.write_text("# Home\n", encoding="utf-8")
            target = section / "index.md"
            target.write_text("# Section\n", encoding="utf-8")

            self.assertEqual(resolve_link(source, "section/", docs), target.resolve())


class AuditTests(unittest.TestCase):
    def make_project(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        docs = root / "docs"
        docs.mkdir()
        config = root / "zensical.toml"
        config.write_text(
            '[project]\ndocs_dir = "docs"\nnav = ["index.md", "guide.md"]\n',
            encoding="utf-8",
        )
        return temp, docs, config

    def test_clean_project_has_no_errors(self) -> None:
        temp, docs, config = self.make_project()
        self.addCleanup(temp.cleanup)
        (docs / "index.md").write_text(
            "---\ntitle: Home\nstatus: draft\n---\n\n[Guide](guide.md)\n",
            encoding="utf-8",
        )
        (docs / "guide.md").write_text(
            "---\ntitle: Guide\nstatus: draft\n---\n\n# Guide\n",
            encoding="utf-8",
        )

        result = audit(docs, config)
        errors = [issue for issue in result["issues"] if issue.severity == "error"]
        self.assertEqual(errors, [])
        self.assertEqual(result["orphan_pages"], [])

    def test_broken_link_is_an_error(self) -> None:
        temp, docs, config = self.make_project()
        self.addCleanup(temp.cleanup)
        (docs / "index.md").write_text(
            "---\ntitle: Home\nstatus: draft\n---\n\n[Missing](missing.md)\n",
            encoding="utf-8",
        )
        (docs / "guide.md").write_text(
            "---\ntitle: Guide\nstatus: draft\n---\n",
            encoding="utf-8",
        )

        result = audit(docs, config)
        self.assertTrue(any(issue.code == "link-broken" for issue in result["issues"] if issue.severity == "error"))


if __name__ == "__main__":
    unittest.main()
