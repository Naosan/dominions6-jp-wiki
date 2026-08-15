from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.report_patch_impact import verification_inventory


class RepositoryPatchImpactCompatibilityTests(unittest.TestCase):
    def test_legacy_and_directory_templates_are_not_versioned_articles(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            docs = Path(temporary)
            (docs / "templates").mkdir()
            (docs / "guide.md").write_text(
                "---\ntitle: Guide\nstatus: draft\n---\n",
                encoding="utf-8",
            )
            (docs / "legacy-template.md").write_text(
                "---\ntitle: Legacy template\nstatus: template\n---\n",
                encoding="utf-8",
            )
            (docs / "templates" / "draft-template.md").write_text(
                "---\ntitle: Draft template\nstatus: draft\n---\n",
                encoding="utf-8",
            )

            inventory = verification_inventory(docs, "6.35")

            self.assertEqual(inventory["hand_written_pages"], 1)
            self.assertEqual(inventory["excluded_non_game_pages"], 2)
            self.assertEqual(
                [record["path"] for record in inventory["missing"]],
                ["guide.md"],
            )


if __name__ == "__main__":
    unittest.main()
