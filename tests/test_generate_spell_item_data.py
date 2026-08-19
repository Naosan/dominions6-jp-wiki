import unittest

from scripts.generate_spell_item_data import FORGE_COST, item_gem_cost


class MagicItemForgeCostTests(unittest.TestCase):
    def test_dom6_path_level_cost_table(self):
        self.assertEqual(
            FORGE_COST,
            {1: 5, 2: 10, 3: 15, 4: 20, 5: 30, 6: 40, 7: 55, 8: 70},
        )

    def test_high_path_item_cost(self):
        row = {
            "constlevel": "9",
            "mainpath": "E",
            "mainlevel": "5",
        }
        self.assertEqual(item_gem_cost(row), "30E")

    def test_mixed_path_item_cost(self):
        row = {
            "constlevel": "9",
            "mainpath": "G",
            "mainlevel": "4",
            "secondarypath": "F",
            "secondarylevel": "2",
        }
        self.assertEqual(item_gem_cost(row), "20G + 10F")

    def test_item_specific_cost_modifier_is_preserved(self):
        row = {
            "constlevel": "5",
            "mainpath": "D",
            "mainlevel": "2",
            "itemcost1": "-20",
        }
        self.assertEqual(item_gem_cost(row), "8D")


if __name__ == "__main__":
    unittest.main()
