import unittest

from scripts.generate_item_purpose_data import (
    CONSTRUCTION_LEVELS,
    booster_features,
    matches_purpose,
    purpose_features,
)


class ItemPurposeClassificationTests(unittest.TestCase):
    def test_construction_breakpoints_are_dom6_forge_levels(self):
        self.assertEqual(CONSTRUCTION_LEVELS, (1, 3, 5, 7, 9))

    def test_plain_weapon_is_offense_candidate(self):
        row = {"type": "1-h wpn"}
        self.assertTrue(matches_purpose(row, "offense"))
        self.assertFalse(matches_purpose(row, "sustain"))

    def test_resistance_and_regeneration_can_overlap(self):
        row = {"type": "misc", "shockres": "10", "regeneration": "10"}
        self.assertTrue(matches_purpose(row, "defense"))
        self.assertTrue(matches_purpose(row, "sustain"))

    def test_mobility_uses_explicit_fields(self):
        row = {"type": "misc", "waterbreathing": "1", "mapmovebonus": "2"}
        self.assertTrue(matches_purpose(row, "mobility"))
        self.assertIn("Water Breathing", purpose_features(row, "mobility"))
        self.assertIn("Map Move 2", purpose_features(row, "mobility"))

    def test_magic_booster_is_mage_support(self):
        row = {"type": "misc", "A": "1", "researchbonus": "6"}
        self.assertTrue(matches_purpose(row, "mage-support"))
        self.assertEqual(booster_features(row), ["A+1"])
        features = purpose_features(row, "mage-support")
        self.assertIn("Research 6", features)
        self.assertIn("A+1", features)

    def test_operations_does_not_treat_sight_as_ethereal_counter(self):
        row = {"type": "misc", "truesight": "1"}
        self.assertTrue(matches_purpose(row, "vision"))
        self.assertFalse(matches_purpose(row, "operations"))
        self.assertFalse(matches_purpose(row, "defense"))


if __name__ == "__main__":
    unittest.main()
