import unittest

from scripts.generate_artifact_item_data import (
    ARTIFACT_CONST,
    UNFORGEABLE_LEVELS,
    artifact_items,
    artifact_page,
    index_block,
    normalized_unforgeable_item,
    unforgeable_items,
)


class ArtifactItemClassificationTests(unittest.TestCase):
    def test_artifact_and_unforgeable_are_distinct_levels(self):
        self.assertEqual(ARTIFACT_CONST, 9)
        self.assertEqual(
            UNFORGEABLE_LEVELS,
            {
                11: "Unforgeable",
                13: "Unforgeable unique artifact",
                15: "Unforgeable unique per nation artifact",
            },
        )
        self.assertNotIn(ARTIFACT_CONST, UNFORGEABLE_LEVELS)

    def test_construction_nine_is_forgeable_artifact(self):
        items = [
            {"const": 9, "name": "Artifact"},
            {"const": 11, "name": "Unforgeable"},
            {"const": 7, "name": "Normal"},
        ]
        self.assertEqual([x["name"] for x in artifact_items(items)], ["Artifact"])

    def test_all_three_unforgeable_classes_are_included(self):
        items = [
            {"const": 9, "name": "Forgeable Artifact"},
            {"const": 11, "name": "Unforgeable"},
            {"const": 13, "name": "Unique"},
            {"const": 15, "name": "Nation Unique"},
        ]
        self.assertEqual(
            [x["name"] for x in unforgeable_items(items)],
            ["Unforgeable", "Unique", "Nation Unique"],
        )

    def test_unforgeable_display_has_no_forge_cost(self):
        item = {
            "const": 13,
            "construction": "Construction 13",
            "cost": "20D",
        }
        normalized = normalized_unforgeable_item(item)
        self.assertEqual(normalized["construction"], "Unforgeable unique artifact")
        self.assertEqual(normalized["cost"], "—")

    def test_index_uses_separate_labels_and_counts(self):
        block = index_block(118, {11: 30, 13: 10, 15: 2})
        self.assertIn("Forgeable Artifact — Construction 9", block)
        self.assertIn("Unforgeable Item", block)
        self.assertIn("11: 30", block)
        self.assertIn("13: 10", block)
        self.assertIn("15: 2", block)
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
