from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.apply_data_record_templates import (
    RecordSet,
    apply_template,
    apply_templates,
)


class DataRecordTemplateTests(unittest.TestCase):
    def write_record(self, path: Path, *, template: str | None = None) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        metadata = ["---", 'title: "Record"']
        if template is not None:
            metadata.append(f'template: "{template}"')
        metadata.extend(["status: generated", 'verified_version: "6.35"', "---", "", "# Record"])
        path.write_text("\n".join(metadata) + "\n", encoding="utf-8")

    def test_assigns_template_after_title(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "record.md"
            self.write_record(path)

            changed = apply_template(path)

            self.assertTrue(changed)
            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(lines[2], 'template: "data-record.html"')

    def test_assignment_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "record.md"
            self.write_record(path)
            self.assertTrue(apply_template(path))
            once = path.read_text(encoding="utf-8")

            self.assertFalse(apply_template(path))
            self.assertEqual(path.read_text(encoding="utf-8"), once)

    def test_refuses_to_replace_an_unrelated_template(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "record.md"
            self.write_record(path, template="other.html")
            with self.assertRaises(ValueError):
                apply_template(path)

    def test_applies_to_each_configured_record_set(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            docs = Path(temp) / "docs"
            self.write_record(docs / "data/units/by-id/0001.md")
            self.write_record(docs / "data/sites/by-id/0002.md")
            sets = (
                RecordSet("Unit", "data/units/by-id", 1),
                RecordSet("Magic Site", "data/sites/by-id", 1),
            )

            result = apply_templates(docs, sets)

            self.assertEqual(result["Unit"], {"records": 1, "changed": 1})
            self.assertEqual(result["Magic Site"], {"records": 1, "changed": 1})

    def test_rejects_an_incomplete_record_set(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            docs = Path(temp) / "docs"
            directory = docs / "data/units/by-id"
            directory.mkdir(parents=True)
            with self.assertRaises(ValueError):
                apply_templates(docs, (RecordSet("Unit", "data/units/by-id", 1),))


if __name__ == "__main__":
    unittest.main()
