from __future__ import annotations


COMMUNION_PATHS = tuple("FAWESDNGBH")


def install(generator) -> None:
    generator.COMMUNION_BREAKPOINTS = (
        (2, 1),
        (4, 2),
        (8, 3),
        (16, 4),
        (32, 5),
        (64, 6),
    )

    def boosted_master_levels(levels, bonus):
        has_arcane_magic = any(
            int(levels.get(path, 0)) > 0
            for path in generator.ARCANE_PATHS
        )
        output = {}
        for path, level in levels.items():
            if int(level) <= 0:
                continue
            if path in generator.ARCANE_PATHS:
                output[path] = int(level) + int(bonus)
            elif path == "H" and has_arcane_magic:
                output[path] = int(level) + int(bonus)
        return output

    def communion_profile(candidates, path, label):
        guaranteed = [
            candidate
            for candidate in candidates
            if int(candidate["guaranteed"].get(path, 0)) >= 1
        ]
        possible = [
            candidate
            for candidate in candidates
            if int(candidate["guaranteed"].get(path, 0)) < 1
            and int(candidate["possible"].get(path, 0)) >= 1
        ]
        breakpoints = []
        for slaves, bonus in generator.COMMUNION_BREAKPOINTS:
            best_levels = {magic_path: 0 for magic_path in COMMUNION_PATHS}
            best_masters = {}
            for candidate in guaranteed:
                levels = boosted_master_levels(candidate["guaranteed"], bonus)
                for magic_path, level in levels.items():
                    if level > best_levels[magic_path]:
                        best_levels[magic_path] = level
                        best_masters[magic_path] = candidate
            breakpoints.append(
                {
                    "slaves": slaves,
                    "bonus": bonus,
                    "levels": best_levels,
                    "masters": best_masters,
                }
            )
        return {
            "label": label,
            "path": path,
            "guaranteed": guaranteed,
            "possible": possible,
            "breakpoints": breakpoints,
        }

    def path_master_text(masters, levels):
        values = []
        for magic_path in COMMUNION_PATHS:
            if not levels.get(magic_path, 0):
                continue
            master = masters.get(magic_path)
            name = f"{master['name']} #{master['id']}" if master else "—"
            values.append(f"{magic_path}{levels[magic_path]}: {name}")
        return "; ".join(values) or "—"

    generator.boosted_master_levels = boosted_master_levels
    generator.communion_profile = communion_profile
    generator.path_master_text = path_master_text
