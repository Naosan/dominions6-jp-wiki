from __future__ import annotations


def install(generator) -> None:
    """Make ordinary path boosters increase only paths already possessed.

    BaseI path bonus columns are treated as path boosters, not as a generic
    source of a new magic path from zero. Explicit empower-style item effects
    use separate fields and are outside the automatic booster chain.
    """

    def add_existing_paths(base, items):
        levels = dict(base)
        for item in items:
            for path, bonus in item["boosts"].items():
                if int(levels.get(path, 0)) <= 0:
                    continue
                levels[path] = int(levels[path]) + int(bonus)
        return {
            path: level
            for path, level in levels.items()
            if int(level) > 0
        }

    generator.add_levels = add_existing_paths
