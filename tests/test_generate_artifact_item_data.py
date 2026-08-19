import unittest

from scripts.generate_artifact_item_data import (
    ARTIFACT_CONST,
    UNFORGEABLE_CONST,
    artifact_items,
    artifact_page,
    index_block,
    unforgeable_items,
)


class ArtifactItemClassificationTests(unittest.TestCase):
    def test_artifact_and_unforgeable_are_distinct_levels(self):
        self.assertEqual(ARTIFACT_CONST, 9)
        self.assertEqual(UNFORGEABLE_CONST, 12)
        self.assertNotEqual(ARTIFACT_CONST, UNFORGEABLE_CONST)

    def test_construction_nine_is_artifact(self):
        items = [
            {"const": 9, "name": "Artifact"},
            {"const": 12, "name": "Unforgeable"},
            {"const": 7, "name": "Normal"},
        ]
        self.assertEqual([x["name"] for x in artifact_items(items)], ["Artifact"])

    def test_unforgeable_does_not_include_artifact(self):
        items = [
            {"const": 9, "name": "Artifact"},
            {"const": 12, "name": "Unforgeable"},
        ]
        self.assertEqual(
            [x["name"] for x in unforgeable_items(items)],
            ["Unforgeable"],
        )

    def test_index_uses_separate_labels(self):
        block = index_block(40, 20)
        self.assertIn("Artifact — Construction 9", block)
        self.assertIn("Unforgeable Item", block)
        self.assertNotIn("Unforgeable / Artifact", block)

    def test_artifact_page_explains_yearning_cost_is_dynamic(self):
        item = {
            "id": 1,
            "name": "Test Artifact",
            "type": "misc",
            "type_title": "Miscellaneous",
            "construction": "Construction 9",
            "const": 9,
            "path": "E4",
            "cost": "20E",
            "boosters": "—",
            "base": "—",
            "traits_text": "—",
            "restriction": "Generic",
        }
        page = artifact_page([item])
        self.assertIn("unique", page)
        self.assertIn("Yearning", page)
        self.assertIn("半額化は反映しません", page)


if __name__ == "__main__":
    unittest.main()
