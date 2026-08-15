from __future__ import annotations

import sys
import unittest

from scripts.build_wiki import SOURCE_REPORT, Step, source_command, step_command


class BuildCommandTests(unittest.TestCase):
    def test_source_stage_owns_refresh_and_offline_modes(self) -> None:
        refresh = source_command(offline=False, refresh=True)
        offline = source_command(offline=True, refresh=False)
        normal = source_command(offline=False, refresh=False)

        self.assertEqual(refresh[-1], "--refresh")
        self.assertEqual(offline[-1], "--offline")
        self.assertNotIn("--refresh", normal)
        self.assertNotIn("--offline", normal)
        self.assertIn(str(SOURCE_REPORT.name), " ".join(normal))

    def test_every_external_generator_is_forced_offline(self) -> None:
        step = Step("external", ("scripts/example.py",), supports_offline=True)
        self.assertEqual(
            step_command(step),
            [sys.executable, "scripts/example.py", "--offline"],
        )

    def test_repository_only_generator_receives_no_source_flag(self) -> None:
        step = Step("local", ("scripts/local.py",))
        self.assertEqual(step_command(step), [sys.executable, "scripts/local.py"])


if __name__ == "__main__":
    unittest.main()
