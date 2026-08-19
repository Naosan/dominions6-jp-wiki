import unittest

from scripts.generate_item_effect_data import (
    DIRECT_EFFECT_FIELDS,
    RISK_RESTRICTION_FIELDS,
    SUMMON_FIELDS,
    armor_summary,
    explicit_features,
    index_block,
)


class ItemEffectProfileTests(unittest.TestCase):
    def test_start_battle_and_auto_combat_are_separate(self):
        row = {
            "startbattlespell": "Storm",
            "autocombatspell": "Lightning Bolt",
        }
        self.assertEqual(
            explicit_features(row, DIRECT_EFFECT_FIELDS),
            ["Start battle spell: Storm", "Auto combat spell: Lightning Bolt"],
        )

    def test_summon_count_is_preserved(self):
        row = {"sumauto": "Imp", "#sumauto": "3"}
        self.assertEqual(
            explicit_features(row, SUMMON_FIELDS),
            ["Automatic summon: Imp", "Automatic summon count: 3"],
        )

    def test_poison_resistance_is_not_a_disease_drawback(self):
        row = {"poisonres": "15", "disease": "1"}
        self.assertEqual(
            explicit_features(row, RISK_RESTRICTION_FIELDS),
            ["Disease"],
        )

    def test_restriction_value_is_not_collapsed(self):
        row = {"minstrtoequip": "18", "nomindless": "1"}
        self.assertEqual(
            explicit_features(row, RISK_RESTRICTION_FIELDS),
            ["Minimum Strength: 18", "No mindless"],
        )

    def test_shield_profile_keeps_parry_and_defense_penalty_separate(self):
        armor = {
            "type": 4,
            "shield": 16,
            "parry": 7,
            "defense": -2,
            "enc": 3,
            "attributes": [],
        }
        text = armor_summary(armor)
        self.assertIn("Shield Prot 16", text)
        self.assertIn("Parry 7", text)
        self.assertIn("Def -2", text)

    def test_generated_index_links_all_effect_pages(self):
        block = index_block()
        for filename in (
            "weapon-profiles.md",
            "armor-profiles.md",
            "active-effects.md",
            "summoning-effects.md",
            "risk-restrictions.md",
        ):
            self.assertIn(filename, block)


if __name__ == "__main__":
    unittest.main()
