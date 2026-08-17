#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

BRANCH_FILES = {
    "docs/nations/ea/index.md": [
        (
            "- [EA Mictlan — Reign of Blood](mictlan.md) — Restricted Dominion、Blood Hunt、Blood Sacrifice、Sacred、首都Priest、Sabbathを扱う基準記事\n",
            "- [EA Mictlan — Reign of Blood](mictlan.md) — Restricted Dominion、Blood Hunt、Blood Sacrifice、Sacred、首都Priest、Sabbathを扱う基準記事\n"
            "- [EA Vanheim — Age of Vanir](vanheim.md) — Glamour、Stealth、Sailing、Vanherse・Vanjarl、Dwarven Smithを扱う基準記事\n",
        ),
        (
            "| 30 | [EA Vanheim](vanheim.md) | Age of Vanir | 骨組み |",
            "| 30 | [EA Vanheim](vanheim.md) | Age of Vanir | **攻略あり** |",
        ),
    ],
    "docs/nations/ma/index.md": [
        (
            "- [MA Pythium — Emerald Empire](pythium.md) — Legion、Communion、Astral、Mage量産、Slave Fatigue、Missing Pathを扱う基準記事\n",
            "- [MA Pythium — Emerald Empire](pythium.md) — Legion、Communion、Astral、Mage量産、Slave Fatigue、Missing Pathを扱う基準記事\n"
            "- [MA Caelum — Reign of the Seraphim](caelum.md) — Flying、Storm、Air・Water、Ice装備、広域集中を扱う基準記事\n",
        ),
        (
            "| 71 | [MA Caelum](caelum.md) | Reign of the Seraphim | 骨組み |",
            "| 71 | [MA Caelum](caelum.md) | Reign of the Seraphim | **攻略あり** |",
        ),
    ],
    "docs/nations/la/index.md": [
        (
            "- [LA Man — Towers of Chelms](man.md) — Longbow・Crossbow、Drain研究、Mason、Fort network、Random Mageを扱う基準記事\n\nLA Manは選択肢が多く、単純な初心者国家ではありません。兵種を役割で分け、研究者・Fort・射撃を一つの国家エンジンとして読むための学習記事です。",
            "- [LA Man — Towers of Chelms](man.md) — Longbow・Crossbow、Drain研究、Mason、Fort network、Random Mageを扱う基準記事\n- [LA Bogarus — Age of Heroes](bogarus.md) — 多Path Mage、Research、Communion・Sabbath、召喚・Global・遠隔Ritualを扱う基準記事\n\nLA ManはCombined ArmsとFort運営、LA BogarusはResearch優位を戦略魔法へ変換する学習記事です。どちらも選択肢が多いため、役割とResearch Timingを先に決めます。",
        ),
        (
            "| 116 | [LA Bogarus](bogarus.md) | Age of Heroes | 骨組み |",
            "| 116 | [LA Bogarus](bogarus.md) | Age of Heroes | **攻略あり** |",
        ),
    ],
    "docs/nations/index.md": [
        (
            "| Blood economy・宗教Network | [EA Mictlan — Reign of Blood](ea/mictlan.md) | Restricted Dominion、Blood Hunt、Blood Sacrifice、Slave輸送、Sabbath |\n",
            "| Blood economy・宗教Network | [EA Mictlan — Reign of Blood](ea/mictlan.md) | Restricted Dominion、Blood Hunt、Blood Sacrifice、Slave輸送、Sabbath |\n| Glamour・Stealth・Sailing | [EA Vanheim — Age of Vanir](ea/vanheim.md) | Glamoured兵、Stealth Raider、Vanherse・Vanjarl、Dwarven Smith、情報戦 |\n",
        ),
        (
            "| Communion | [MA Pythium — Emerald Empire](ma/pythium.md) | Legion、Master / Slave、Astral、Communion Fatigue、Missing Path |\n",
            "| Communion | [MA Pythium — Emerald Empire](ma/pythium.md) | Legion、Master / Slave、Astral、Communion Fatigue、Missing Path |\n| Flying・Storm・Air機動 | [MA Caelum — Reign of the Seraphim](ma/caelum.md) | Flying集中、Storm、Air・Water、Ice装備、Mammoth |\n",
        ),
        (
            "| 射撃Combined Arms | [LA Man — Towers of Chelms](la/man.md) | Longbow・Crossbow、Drain研究、Random Mage、Mason、Fort network |",
            "| 射撃Combined Arms | [LA Man — Towers of Chelms](la/man.md) | Longbow・Crossbow、Drain研究、Random Mage、Mason、Fort network |\n| Research・戦略魔法 | [LA Bogarus — Age of Heroes](la/bogarus.md) | 多Path Mage、Communion・Sabbath、召喚、Global、Remote Ritual |",
        ),
        (
            "EA Mictlan    ：Blood economyと宗教Network\nMA Atlantis   ：UnderwaterからLandfall\nLA Man        ：Combined Armsと研究・Fort管理",
            "EA Mictlan    ：Blood economyと宗教Network\nEA Vanheim    ：Glamour・Stealth・Sailingによる情報戦\nMA Caelum     ：Flying集中とStormによる戦場制御\nMA Atlantis   ：UnderwaterからLandfall\nLA Man        ：Combined Armsと研究・Fort管理\nLA Bogarus    ：Research優位から召喚・Global・遠隔Ritualへ移行",
        ),
        (
            "| Blood Huntから前線投入までつなげたい | EA Mictlan | Blood Economy・Blood Sacrifice |\n",
            "| Blood Huntから前線投入までつなげたい | EA Mictlan | Blood Economy・Blood Sacrifice |\n| Glamour・Stealthで情報差を作りたい | EA Vanheim | Stealth・Glamour・特殊作戦 |\n| Flying ArmyとStormを使い分けたい | MA Caelum | Flying・Storm・Air機動戦 |\n",
        ),
        (
            "| 射撃・前衛・Mageを統合したい | LA Man | EA Ulm、MA Pythium |",
            "| 射撃・前衛・Mageを統合したい | LA Man | EA Ulm、MA Pythium |\n| Researchを召喚・Global・遠隔攻撃へ変換したい | LA Bogarus | 召喚・Global・遠隔Ritual |",
        ),
        (
            "- [海・Underwater・Amphibious攻略](../systems/underwater.md) — Aquatic、Amphibious、Water Breathing、海中戦、Landfall、Retreat\n",
            "- [海・Underwater・Amphibious攻略](../systems/underwater.md) — Aquatic、Amphibious、Water Breathing、海中戦、Landfall、Retreat\n- [Stealth・Glamour・特殊作戦](../systems/stealth-glamour.md) — Sneak、Raider、Patrol、Assassination、Sailing、情報戦\n- [Flying・Storm・Air機動戦](../systems/flying-storm.md) — Strategic Flying、Attack Rear、Storm、Air Magic、迎撃\n- [召喚・Global・遠隔Ritual](../magic/strategic-rituals.md) — Summon Mage、Access chain、Global、Dispel、Remote attack、Monthly order\n",
        ),
        (
            "第3陣でUndead・Popkill、Blood economy、Underwaterを追加しました。次は、既存九記事でまだ基準化できていない次の類型を優先します。\n\n- Glamour・Stealthへ強く依存する国家\n- Flying・Sailing・Magic Phase機動国家\n- Nature・Poison・Regeneration中心国家\n- Late-game召喚・Global中心国家\n- Disciple Gameで役割分担が明確な国家Pair",
            "第4陣でGlamour・Stealth、Flying・Storm、Late-game戦略魔法を追加しました。次は、既存十二記事でまだ基準化できていない次の類型を優先します。\n\n- Nature・Poison・Regeneration中心国家\n- Assassination・Seduction・特殊作戦へ強く依存する国家\n- Magic Phase・Sailingを主戦略にする国家\n- Disciple Gameで役割分担が明確な国家Pair\n- Legendary Spell・複数Planeを勝利条件へ使う国家",
        ),
    ],
    "docs/nations/choose-a-nation.md": [
        (
            "- Province Defenceを抜く小部隊\n\n### 7. Underwater国家を選ぶか",
            "- Province Defenceを抜く小部隊\n\nGlamour・Stealth・Sailingを国家Engineとして学ぶ基準は[EA Vanheim](ea/vanheim.md)、共通仕様は[Stealth・Glamour・特殊作戦](../systems/stealth-glamour.md)です。Flying集中とStormは[MA Caelum](ma/caelum.md)と[Flying・Storm・Air機動戦](../systems/flying-storm.md)を参照してください。\n\n### 7. Underwater国家を選ぶか",
        ),
        (
            "| Glamour / Stealth | 情報戦、Raid、Illusion | True Sight、Mindless | 今後整備 |",
            "| Glamour / Stealth | 情報戦、Raid、Illusion、Sailing | True Sight、Mindless、AoE、Patrol | [EA Vanheim](ea/vanheim.md) |\n| Flying / Storm | 広域集中、Attack Rear、Storm、Air Magic | 射撃、AoE、Stormの両刃、過伸展 | [MA Caelum](ma/caelum.md) |\n| Strategic Magic | Research、Summon Mage、Global、Remote Ritual | 早期Rush、Gem不足、Caster喪失 | [LA Bogarus](la/bogarus.md) |",
        ),
        (
            "国家の難易度を一つの数字で決めず、何を学びたいかで次の九記事を使い分けます。",
            "国家の難易度を一つの数字で決めず、何を学びたいかで次の十二記事を使い分けます。",
        ),
        (
            "| [EA Mictlan](ea/mictlan.md) | Blood Hunt、Blood Sacrifice、Sacred、首都Crosspath | Unrest、Population、Slave輸送、首都Queue |\n",
            "| [EA Mictlan](ea/mictlan.md) | Blood Hunt、Blood Sacrifice、Sacred、首都Crosspath | Unrest、Population、Slave輸送、首都Queue |\n| [EA Vanheim](ea/vanheim.md) | Glamour、Stealth、Sailing、Vanir、Dwarven Smith | AoE、Fatigue、True Sight、高価な損失、Role競合 |\n",
        ),
        (
            "| [MA Pythium](ma/pythium.md) | Legion、Communion、Astral、Mage量産、Fort scaling | Slave過労死、Magic Duel、Missing Path、操作量 |\n",
            "| [MA Pythium](ma/pythium.md) | Legion、Communion、Astral、Mage量産、Fort scaling | Slave過労死、Magic Duel、Missing Path、操作量 |\n| [MA Caelum](ma/caelum.md) | Flying集中、Storm、Air・Water、Ice兵、Mammoth | 低HP、射撃、Fire、Stormの両刃、High Seraph供給 |\n",
        ),
        (
            "| [LA Man](la/man.md) | Longbow・Crossbow、Friendly Fire、Drain研究、Mason、Fort network | 兵種選択の多さ、Mage個体差、Nature・Water不足 |",
            "| [LA Man](la/man.md) | Longbow・Crossbow、Friendly Fire、Drain研究、Mason、Fort network | 兵種選択の多さ、Mage個体差、Nature・Water不足 |\n| [LA Bogarus](la/bogarus.md) | 多Path Mage、Research、Communion・Sabbath、戦略Ritual | 弱い序盤、Mage防護、Gold、操作量、Missing Path |",
        ),
        (
            "### Stealthと多様な兵を学ぶ\n\nEA Ulmは、正面ArmyとStealth Armyを使い分ける練習に向きます。国家兵は強い一方、射撃とMR攻撃への対策が必要です。",
            "### Glamour・Stealth・Sailingを学ぶ\n\nEA Vanheimでは、見えないArmyを増やすこと自体ではなく、正面Armyで敵を固定し、Stealth RaiderとSailingで守備先を増やします。\n\n```text\nScout\n→ 潜入\n→ Raid / Assassination\n→ 敵Reserveを移動\n→ Main ArmyがFortを取る\n```\n\n高DefenceはAoE・Fatigue・True Sightへ崩れるため、通常兵・Item・Air・Bloodへ切り替える第二案も学びます。\n\n### Flying・Stormを学ぶ\n\nMA Caelumでは、Flyingを移動距離ではなく局地的集中として扱います。Stormは敵Flying・Archerを止める一方、自軍Flying・射撃も壊し得ます。\n\n```text\nNo Storm plan\nvs\nStorm plan\n```\n\nを敵ごとに切り替える教材です。\n\n### ResearchからStrategic Magicへ進む\n\nLA Bogarusでは、早いResearchをFirst warへ使った後、Summon Mage、Global、Remote attackへPivotします。\n\n```text\nResearch\n→ Caster\n→ Booster\n→ Gem budget\n→ Ritual\n→ 次のAccess\n```\n\nまで接続し、研究量だけが高い国家で終わらないことを学びます。\n\n### Stealthと多様な兵を学ぶ\n\nEA Ulmは、正面ArmyとStealth Armyを使い分ける練習に向きます。国家兵は強い一方、射撃とMR攻撃への対策が必要です。",
        ),
        (
            "- Popkill・Blood・Underwaterのどの資源が通常国家と違うか説明できる",
            "- Popkill・Blood・Underwaterのどの資源が通常国家と違うか説明できる\n- Glamour・Flying・Strategic Ritualで、情報・Timing・Accessのどれを買っているか説明できる",
        ),
    ],
    "zensical.toml": [
        ('      "nations/ea/mictlan.md",\n', '      "nations/ea/mictlan.md",\n      "nations/ea/vanheim.md",\n'),
        ('      "nations/ma/pythium.md",\n', '      "nations/ma/pythium.md",\n      "nations/ma/caelum.md",\n'),
        ('    { "Late Age" = ["nations/la/index.md", "nations/la/man.md"] },', '    { "Late Age" = [\n      "nations/la/index.md",\n      "nations/la/man.md",\n      "nations/la/bogarus.md",\n    ] },'),
        ('    "magic/blood-economy.md",\n', '    "magic/blood-economy.md",\n    "magic/strategic-rituals.md",\n'),
        ('  { "特殊能力" = "reference/special-abilities.md" },\n', '  { "特殊能力" = "reference/special-abilities.md" },\n  { "Stealth・Glamour" = "systems/stealth-glamour.md" },\n  { "Flying・Storm" = "systems/flying-storm.md" },\n'),
    ],
}


def apply(path: Path, replacements: list[tuple[str, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for index, (old, new) in enumerate(replacements, 1):
        if new in text:
            continue
        count = text.count(old)
        if count != 1:
            raise RuntimeError(f"{path}: replacement {index}: expected 1 old match, found {count}")
        text = text.replace(old, new, 1)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    changed: list[str] = []
    for rel, replacements in BRANCH_FILES.items():
        path = root / rel
        if apply(path, replacements):
            changed.append(rel)
    print("changed files:")
    for rel in changed:
        print(" -", rel)
    if not changed:
        print(" - none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
