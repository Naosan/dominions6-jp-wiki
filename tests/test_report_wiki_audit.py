from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.report_wiki_audit import annotation, append_summary, repository_path


class AnnotationTests(unittest.TestCase):
    def test_formats_error_with_file_line_and_escaping(self) -> None:
        command = annotation(
            {
                "severity": "error",
                "code": "link-broken",
                "path": "docs/a,b.md",
                "line": 12,
                "message": "missing: 100%\nnext",
            }
        )
        self.assertEqual(
            command,
            "::error file=docs/a%2Cb.md,title=Wiki audit%3A link-broken,line=12,endLine=12::missing: 100%25%0Anext",
        )

    def test_formats_warning_without_line(self) -> None:
        command = annotation(
            {
                "severity": "warning",
                "code": "page-orphan",
                "path": "guide.md",
                "message": "no incoming link",
            },
            "docs",
        )
        self.assertEqual(
            command,
            "::warning file=docs/guide.md,title=Wiki audit%3A page-orphan::no incoming link",
        )

    def test_repository_path_keeps_repository_level_config(self) -> None:
        self.assertEqual(repository_path("zensical.toml", "docs"), "zensical.toml")
        self.assertEqual(repository_path("basics/orders.md", "docs"), "docs/basics/orders.md")
        self.assertEqual(repository_path("docs/basics/orders.md", "docs"), "docs/basics/orders.md")


class SummaryTests(unittest.TestCase):
    def test_writes_compact_job_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "summary.md"
            report = {
                "files": 10,
                "front_matter_files": 8,
                "local_links": 20,
                "navigation_targets": 5,
                "orphan_pages": ["one.md"],
                "statuses": {"draft": 2, "generated": 6},
            }
            with patch.dict("os.environ", {"GITHUB_STEP_SUMMARY": str(path)}):
                append_summary(report, [{"severity": "error"}], [{"severity": "warning"}])

            text = path.read_text(encoding="utf-8")
            self.assertIn("| Errors | 1 |", text)
            self.assertIn("| Warnings | 1 |", text)
            self.assertIn("`draft`: 2", text)


if __name__ == "__main__":
    unittest.main()
