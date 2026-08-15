from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.report_patch_impact import (
    BaselineSnapshot,
    build_report,
    collect_generated_metrics,
    compare_versions,
    metric_diff,
    parse_version,
    summary_markdown,
    table_row_count,
    verification_inventory,
)


class PatchImpactTests(unittest.TestCase):
    def test_versions_compare_numerically_and_support_hotfix_suffixes(self) -> None:
        self.assertIsNotNone(parse_version("6.35"))
        self.assertEqual(compare_versions("6.9", "6.35"), -1)
        self.assertEqual(compare_versions("6.35", "6.35"), 0)
        self.assertEqual(compare_versions("6.35", "6.35a"), -1)
        self.assertEqual(compare_versions("v6.35b", "6.35a"), 1)
        self.assertIsNone(compare_versions("current", "6.35"))

    def test_table_rows_exclude_headers_and_separator(self) -> None:
        text = """| A | B |
|---|---:|
| 1 | 2 |
| 3 | 4 |

paragraph
| C |
|:---:|
| 5 |
"""
        self.assertEqual(table_row_count(text), 3)

    def test_generated_metrics_are_bucketed_and_diffed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            before = root / "before"
            after = root / "after"
            (before / "data" / "units").mkdir(parents=True)
            (after / "data" / "units").mkdir(parents=True)
            (after / "data" / "spells").mkdir(parents=True)
            (before / "data" / "units" / "1.md").write_text(
                "---\ntitle: Unit\nstatus: generated\n---\n\n| ID | Name |\n|---:|---|\n| 1 | A |\n",
                encoding="utf-8",
            )
            (after / "data" / "units" / "1.md").write_text(
                "---\ntitle: Unit\nstatus: generated\n---\n\n| ID | Name |\n|---:|---|\n| 1 | B |\n| 2 | C |\n",
                encoding="utf-8",
            )
            (after / "data" / "spells" / "index.md").write_text(
                "---\ntitle: Spells\nstatus: generated\n---\n",
                encoding="utf-8",
            )
            # Authored pages do not contribute to generated metrics.
            (after / "guide.md").write_text(
                "---\ntitle: Guide\nstatus: draft\n---\n",
                encoding="utf-8",
            )

            old = collect_generated_metrics(before)
            new = collect_generated_metrics(after)
            diff = metric_diff(new, old)

            self.assertEqual(old["totals"]["pages"], 1)
            self.assertEqual(new["totals"]["pages"], 2)
            self.assertEqual(new["datasets"]["data/units"]["table_rows"], 2)
            self.assertEqual(diff["files"]["added"], 1)
            self.assertEqual(diff["files"]["changed"], 1)
            datasets = {entry["dataset"]: entry for entry in diff["datasets"]}
            self.assertEqual(datasets["data/spells"]["pages"]["delta"], 1)
            self.assertEqual(datasets["data/units"]["table_rows"]["delta"], 1)

    def test_verification_inventory_excludes_generated_and_project_pages(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            docs = Path(temporary)
            pages = {
                "stale.md": "---\ntitle: Old\nstatus: reviewed\nverified_version: \"6.34\"\nlast_verified: \"2026-01-01\"\n---\n",
                "current.md": "---\ntitle: Current\nstatus: verified\nverified_version: \"6.35\"\n---\n",
                "ahead.md": "---\ntitle: Ahead\nstatus: draft\nverified_version: \"6.36\"\n---\n",
                "missing.md": "---\ntitle: Missing\nstatus: draft\n---\n",
                "invalid.md": "---\ntitle: Invalid\nstatus: draft\nverified_version: current\n---\n",
                "generated.md": "---\ntitle: Generated\nstatus: generated\nverified_version: \"6.10\"\n---\n",
                "project.md": "---\ntitle: Policy\npage_type: project\nstatus: reviewed\n---\n",
                "needs.md": "---\ntitle: Needs\nstatus: needs-update\nverified_version: \"6.34\"\n---\n",
            }
            for name, text in pages.items():
                (docs / name).write_text(text, encoding="utf-8")

            inventory = verification_inventory(docs, "6.35")
            self.assertEqual(inventory["hand_written_pages"], 6)
            self.assertEqual([item["path"] for item in inventory["stale"]], ["needs.md", "stale.md"])
            self.assertEqual([item["path"] for item in inventory["current"]], ["current.md"])
            self.assertEqual([item["path"] for item in inventory["ahead"]], ["ahead.md"])
            self.assertEqual([item["path"] for item in inventory["missing"]], ["missing.md"])
            self.assertEqual([item["path"] for item in inventory["invalid"]], ["invalid.md"])
            self.assertEqual([item["path"] for item in inventory["needs_update"]], ["needs.md"])
            self.assertEqual(inventory["excluded_non_game_pages"], 1)

    def test_report_and_summary_expose_metric_and_freshness_deltas(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            docs = Path(temporary)
            (docs / "data").mkdir()
            (docs / "data" / "index.md").write_text(
                "---\ntitle: Data\nstatus: generated\n---\n",
                encoding="utf-8",
            )
            (docs / "guide.md").write_text(
                "---\ntitle: Guide\nstatus: reviewed\nverified_version: \"6.34\"\n---\n",
                encoding="utf-8",
            )
            metrics = collect_generated_metrics(docs)
            verification = verification_inventory(docs, "6.35")

            class Manifest:
                repository = "example/source"
                commit = "a" * 40
                tree = "b" * 40
                game_version = "6.35"

            baseline = BaselineSnapshot(
                available=True,
                ref="origin/main",
                note=None,
                metrics=metrics,
                source={
                    "repository": "example/source",
                    "commit": "0" * 40,
                    "tree": "1" * 40,
                    "game_version": "6.34",
                },
            )
            report = build_report(Manifest(), metrics, baseline, verification)
            markdown = summary_markdown(report)
            self.assertEqual(report["summary"]["stale_pages"], 1)
            self.assertIn("Patch impact", markdown)
            self.assertIn("guide.md", markdown)
            self.assertIn("origin/main", markdown)


if __name__ == "__main__":
    unittest.main()
