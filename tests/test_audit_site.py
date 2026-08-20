from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.audit_site import audit


HTML = """<!doctype html>
<html><head><link rel=\"canonical\" href=\"{canonical}\"></head>
<body>{navigation}<main data-md-component=\"content\">content</main>{toc}</body></html>
"""


class RenderedSiteAuditTests(unittest.TestCase):
    def make_site(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        site = root / "site"
        site.mkdir()
        config = root / "zensical.toml"
        config.write_text(
            '[project]\nsite_url = "https://example.test/wiki/"\n',
            encoding="utf-8",
        )
        return temp, site, config

    def write_page(
        self,
        site: Path,
        relative: str,
        *,
        canonical: str | None = None,
        navigation: bool = False,
        toc: bool = False,
    ) -> None:
        path = site / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if canonical is None:
            canonical = "https://example.test/wiki/" + relative.removesuffix("index.html")
        path.write_text(
            HTML.format(
                canonical=canonical,
                navigation='<aside data-md-type="navigation"></aside>' if navigation else "",
                toc='<aside data-md-type="toc"></aside>' if toc else "",
            ),
            encoding="utf-8",
        )

    def write_indexes(self, site: Path) -> None:
        (site / "search.json").write_text(
            json.dumps(
                {
                    "config": {},
                    "items": [
                        {"location": ""},
                        {"location": "data/units/by-id/0001/"},
                        {"location": "data/sites/by-id/0002/#effects"},
                        {"location": "data/items/by-id/0369/#related-data"},
                    ],
                }
            ),
            encoding="utf-8",
        )
        (site / "sitemap.xml").write_text(
            """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://example.test/wiki/</loc></url>
</urlset>
""",
            encoding="utf-8",
        )

    def clean_site(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path]:
        temp, site, config = self.make_site()
        self.write_page(site, "index.html")
        self.write_page(site, "data/units/by-id/0001/index.html")
        self.write_page(site, "data/sites/by-id/0002/index.html")
        self.write_page(site, "data/items/by-id/0369/index.html")
        self.write_indexes(site)
        return temp, site, config

    def test_clean_site_reports_metrics_without_errors(self) -> None:
        temp, site, config = self.clean_site()
        self.addCleanup(temp.cleanup)

        result = audit(site, config, warning_bytes=1_000_000, failure_bytes=2_000_000)

        self.assertEqual(result["errors"], 0)
        self.assertEqual(result["metrics"]["data_record_files"], 3)
        self.assertEqual(result["metrics"]["data_record_primary_navigation_pages"], 0)
        self.assertEqual(result["metrics"]["search"]["items"], 4)
        self.assertEqual(result["metrics"]["search"]["data_record_items"], 3)
        self.assertEqual(result["metrics"]["sitemap"]["urls"], 1)

    def test_global_navigation_on_data_record_is_an_error(self) -> None:
        temp, site, config = self.clean_site()
        self.addCleanup(temp.cleanup)
        self.write_page(site, "data/units/by-id/0001/index.html", navigation=True)

        result = audit(site, config, warning_bytes=1_000_000, failure_bytes=2_000_000)

        self.assertTrue(any(issue.code == "data-record-primary-nav" for issue in result["issues"]))

    def test_global_navigation_on_magic_item_record_is_an_error(self) -> None:
        temp, site, config = self.clean_site()
        self.addCleanup(temp.cleanup)
        self.write_page(site, "data/items/by-id/0369/index.html", navigation=True)

        result = audit(site, config, warning_bytes=1_000_000, failure_bytes=2_000_000)

        self.assertTrue(any(issue.code == "data-record-primary-nav" for issue in result["issues"]))

    def test_missing_canonical_is_an_error(self) -> None:
        temp, site, config = self.clean_site()
        self.addCleanup(temp.cleanup)
        (site / "index.html").write_text(
            '<main data-md-component="content">content</main>', encoding="utf-8"
        )

        result = audit(site, config, warning_bytes=1_000_000, failure_bytes=2_000_000)

        self.assertTrue(any(issue.code == "canonical-missing" for issue in result["issues"]))

    def test_warning_and_failure_thresholds_are_distinct(self) -> None:
        temp, site, config = self.clean_site()
        self.addCleanup(temp.cleanup)
        large = site / "large.bin"
        large.write_bytes(b"x" * 300)

        warning = audit(site, config, warning_bytes=100, failure_bytes=10_000)
        failure = audit(site, config, warning_bytes=100, failure_bytes=200)

        self.assertTrue(any(issue.code == "site-size-warning" for issue in warning["issues"]))
        self.assertFalse(any(issue.code == "site-size-limit" for issue in warning["issues"]))
        self.assertTrue(any(issue.code == "site-size-limit" for issue in failure["issues"]))

    def test_invalid_threshold_order_is_rejected(self) -> None:
        temp, site, config = self.clean_site()
        self.addCleanup(temp.cleanup)
        with self.assertRaises(ValueError):
            audit(site, config, warning_bytes=100, failure_bytes=100)


if __name__ == "__main__":
    unittest.main()
