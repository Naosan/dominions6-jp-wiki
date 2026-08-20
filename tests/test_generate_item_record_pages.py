from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.apply_data_record_templates import RECORD_SETS
from scripts.generate_item_record_pages import (
    acquisition_label,
    display_cost,
    index_block,
    item_record_link,
    link_generated_item_tables,
    record_page,
    records_index_page,
)


def sample_item(**overrides):
    item = {
        "id": 369,
        "name": "Amulet of Antimagic",
        "type": "misc",
        "type_title": "Miscellaneous",
        "type_slug": "miscellaneous",
        "construction": "Construction 5",
        "const": 5,
        "path": "S1",
        "cost": "5S",
        "boosters": "—",
        "base": "—",
        "traits_text": "MR +4, Antimagic",
        "restriction": "Generic",
        "research": 0,
        "has_resistance": True,
        "has_utility": False,
    }
    item.update(overrides)
    return item


def sample_raw(**overrides):
    row = {
        "id": "369",
        "weapon": "0",
        "armor": "0",
        "spelleffect": "0",
        "startbattlespell": "0",
        "autocombatspell": "0",
        "itemspell": "0",
        "ritual": "0",
        "sumrit": "0",
        "#sumrit": "0",
        "sumauto": "0",
        "#sumauto": "0",
        "sumbat": "0",
        "#sumbat": "0",
        "batstartsum2": "0",
        "batstartsum3": "0",
        "batstartsum5d6": "0",
        "retinue": "0",
        "summoner1d6": "0",
        "summoner2d6": "0",
        "mustfightinarena": "0",
        "arenareward": "0",
    }
    row.update(overrides)
    return row


class ItemRecordPageTests(unittest.TestCase):
    def test_construction_nine_is_labeled_as_forgeable_artifact(self):
        item = sample_item(const=9, construction="Construction 9")
        self.assertIn("Artifact", acquisition_label(item))
        self.assertIn("forgeable", acquisition_label(item))

    def test_unforgeable_classes_are_not_presented_as_construction_levels(self):
        for const in (11, 13, 15):
            with self.subTest(const=const):
                label = acquisition_label(sample_item(const=const, construction=f"Construction {const}"))
                self.assertIn("Unforgeable", label)
                self.assertNotIn(f"Construction {const}", label)

    def test_unforgeable_classes_never_show_a_normal_forge_cost(self):
        for const in (11, 13, 15):
            with self.subTest(const=const):
                item = sample_item(const=const, cost="5S")
                self.assertEqual(display_cost(item), "—")
                page = record_page(item, sample_raw())
                self.assertIn("| Base Gem cost | — |", page)

    def test_record_page_links_specialized_indexes_only_when_relevant(self):
        page = record_page(
            sample_item(),
            sample_raw(
                weapon="76",
                startbattlespell="Storm",
                sumauto="Wolf",
                disease="1",
            ),
        )
        self.assertIn("Magic Item Weapon profile", page)
        self.assertIn("Item Spell・自動効果", page)
        self.assertIn("Summon・Retinue効果", page)
        self.assertIn("副作用・装備制限", page)
        self.assertNotIn("Artifact一覧", page)

    def test_core_crown_label_is_normalized_on_record_page(self):
        page = record_page(
            sample_item(traits_text="Artifact / Crown, MR +2"),
            sample_raw(),
        )
        self.assertIn("Crown, MR +2", page)
        self.assertNotIn("Artifact / Crown", page)

    def test_records_index_links_each_item(self):
        page = records_index_page([sample_item()])
        self.assertIn("[Amulet of Antimagic](by-id/369.md)", page)

    def test_index_block_exposes_record_count(self):
        block = index_block(529)
        self.assertIn("529 records", block)
        self.assertIn("records.md", block)

    def test_nested_table_rows_link_to_by_id_and_are_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            item_out = Path(temp) / "items"
            page = item_out / "by-purpose" / "defense.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "| Item | ID | Research |\n"
                "|---|---:|---|\n"
                "| Amulet of Antimagic | 369 | Construction 5 |\n"
                "| Not an item | 369 | unchanged |\n",
                encoding="utf-8",
            )
            items = [sample_item()]

            changed_files, linked_rows = link_generated_item_tables(items, item_out)
            once = page.read_text(encoding="utf-8")
            second_files, second_rows = link_generated_item_tables(items, item_out)

            self.assertEqual((changed_files, linked_rows), (1, 1))
            self.assertIn("[Amulet of Antimagic](../by-id/369.md)", once)
            self.assertIn("| Not an item | 369 | unchanged |", once)
            self.assertEqual((second_files, second_rows), (0, 0))
            self.assertEqual(page.read_text(encoding="utf-8"), once)

    def test_root_table_relative_link(self):
        with tempfile.TemporaryDirectory() as temp:
            item_out = Path(temp) / "items"
            page = item_out / "research.md"
            page.parent.mkdir(parents=True)
            self.assertEqual(item_record_link(369, page, item_out), "by-id/369.md")

    def test_magic_item_record_set_uses_lightweight_template(self):
        configured = {(record.label, record.relative_dir) for record in RECORD_SETS}
        self.assertIn(("Magic Item", "data/items/by-id"), configured)


if __name__ == "__main__":
    unittest.main()
