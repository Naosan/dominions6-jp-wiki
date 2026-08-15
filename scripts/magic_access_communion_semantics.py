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

    def communion_page(profiles, matrix_items):
        lines = generator.front_matter("全国家Communion・Sabbath battle reach")
        lines.extend(
            [
                "# 全国家Communion・Sabbath battle reach",
                "",
                "通常Recruit Mageの保証S1 / B1を使い、Slave数ごとの戦闘中Path最大を計算します。HolyはMasterが通常Mageでもある場合だけ含めます。",
                "",
                "[国家別到達経路へ戻る](index.md)",
                "",
                "| Nation | Structure | Slave-capable types | 2 slaves | 4 slaves | 8 slaves | 16 slaves | 32 slaves | 64 slaves |",
                "|---|---|---:|---|---|---|---|---|---|",
            ]
        )
        for profile in profiles:
            nation = profile["nation"]
            for structure in (profile["communion"], profile["sabbath"]):
                values = [
                    generator.level_text(item["levels"])
                    if structure["guaranteed"]
                    else "—"
                    for item in structure["breakpoints"]
                ]
                lines.append(
                    f"| [{nation['code']} {generator.esc(nation['name'])}]"
                    f"({nation['dir']}/{nation['slug']}.md) | "
                    f"{structure['label']} | {len(structure['guaranteed']) or '—'} | "
                    + " | ".join(generator.esc(value) for value in values)
                    + " |"
                )
        lines.extend(
            [
                "",
                "## Matrix / Communion related Item",
                "",
                "| Item | Type | Research | Req | Boost |",
                "|---|---|---|---|---|",
            ]
        )
        for item in matrix_items:
            lines.append(
                f"| {generator.esc(item['name'])} | "
                f"{generator.esc(item['type_title'])} | "
                f"{generator.esc(item['construction'])} | "
                f"{generator.esc(item['requirement_text'])} | "
                f"{generator.esc(item['boost_text'])} |"
            )
        if not matrix_items:
            lines.append("| — | — | — | — | 自動Booster集合内の該当Itemなし |")
        lines.extend(
            [
                "",
                "Path reachだけの比較です。Fatigue、安全なMaster数、Self-buff共有、Matrix装備者のPath差は[Communion・Sabbath](../../magic/communions.md)で確認してください。",
                "",
            ]
        )
        return "\n".join(lines)

    generator.boosted_master_levels = boosted_master_levels
    generator.communion_profile = communion_profile
    generator.path_master_text = path_master_text
    generator.communion_page = communion_page
