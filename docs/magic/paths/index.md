---
title: Magic Path総論
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Magic Path総論

Magic Pathは「何属性のDamageを出すか」だけではありません。

各Pathは、

- 敵のどの防御層を攻撃するか
- 自軍をどう変えるか
- Gemを何へ変換するか
- 戦略マップで何ができるか
- 低Path Mageと高Path Mageをどう分担するか

という戦略体系です。

---

# 一覧

| Path | 主な勝ち筋 | 主に攻撃する防御 | 理想的なMage構成 |
|---|---|---|---|
| [Fire](fire.md) | 範囲火力、熱、射撃強化、短期決戦 | Fire Resistance、HP、Fatigue | F2～3量産＋高Pathの戦場担当 |
| [Air](air.md) | Shock、射撃防御、飛行、Magic Phase攻撃 | Shock Resistance、HP | A2機動＋A3砲兵＋A4以上のArmy spell |
| [Water](water.md) | Quickness、Cold、Slow、Fatigue、Tempo | Cold Resistance、Fatigue、行動回数 | W2～3支援＋高PathのCold戦術 |
| [Earth](earth.md) | Protection、Strength、武器強化、拘束 | 通常物理、Defence、Fatigue | E2量産＋Boost後E3～4担当 |
| [Astral](astral.md) | Communion、MR攻撃、転移、対Mage | Magic Resistance、Mindless等 | 多数S1＋S2～4 Master |
| [Death](death.md) | Undead、Skeleton、Darkness、消耗戦 | Holy耐性、Fatigue、生命分類 | 多数D2＋D4以上の戦場担当 |
| [Nature](nature.md) | Regeneration、Poison、回復、Supply | Poison Resistance、Burst damage | N2～3支援＋N4～5 Army spell |
| [Glamour](glamour.md) | Luck、Illusion、Confusion、欺瞞 | MR、True Sight、Mindless等 | G2～3支援＋G4～5戦場支配 |
| [Blood](blood.md) | Blood Hunt、Demon、Sabbath、終盤Scaling | Holy、運用経済、Slave物流 | 多数B1～2 Hunter＋高Path Caster |
| [Holy](holy.md) | Bless、Banishment、Morale、宗教戦 | Sacred / Undead / Demon分類 | 多数H1＋H3以上の全軍担当 |

---

# 防御層から選ぶ

## 高Protection

候補：

- AirのArmor Negating Shock
- Astral / Death / GlamourのMR攻撃
- NatureのPoison
- Earthの高Damage・Armor Piercing化
- Water / Death / FireのFatigue戦
- Bloodの特殊Damage・Demon

Protectionをさらに上回るDamageを出す方法と、Protectionを参照しない方法があります。

## 高Defence

候補：

- Earth / Natureの拘束
- AstralのParalyze・Control
- GlamourのConfusion
- Fire / AirのAoE
- 多段攻撃を支援するWater / Earth

一発のAttackを上げるだけでなく、回避不能状態、範囲攻撃、手数を使います。

## 高Magic Resistance

候補：

- Fire / Air / Earth / Waterの通常Damage
- Army buffを受けた一般兵
- Armor Piercing射撃
- PoisonやBattlefield環境

MR攻撃を無理に貫通させるより、別の防御層へ切り替えます。

## 大量の低HP兵

候補：

- FireのAoE
- AirのShock・Storm
- DeathのSkeletonで拘束しDarkness / Fatigue
- NatureのPoison / Howl
- GlamourのFalse Horror / Confusion
- BloodのImp / Demon / Battlefield effect

## Giant・高HP

候補：

- 高Damage Earth buff
- Astral / Deathの即死・MR攻撃
- NatureのPoison / Disease
- AirのAN Shock
- Fatigue戦

低Damage AoEを大量に撃つだけではHPを削り切れないことがあります。

## Undead / Demon

候補：

- Holy
- Fire / Astralの対Undead・Demon Spell
- 高Damage Magic Weapon
- Control Undead等の専用効果

通常のPoison、Mind effect、Fatigue等は対象分類によって効き方が変わります。

---

# 自軍から選ぶ

## 安価な一般兵が多い

優先しやすいPath：

- Earth：Strength、Protection、武器強化
- Nature：Regeneration、Resistance、Fatigue支援
- Air：射撃防御、Mist / Flight
- Fire：射撃強化、範囲火力

Army-wide Spell一回の価値が兵数に比例します。

## 高HP Giant

優先しやすいPath：

- Nature：割合Regeneration
- Earth：Protection、Strength、Reinvigoration
- Water：Quickness
- Air / Astral / Glamour：別防御層を追加

## 高価な少数Sacred

- Nature：Regeneration
- Glamour：Luck / Illusion
- Water：Quickness
- Earth：Protection / Strength
- Air：Mist /射撃防御
- Astral：Ethereal / Antimagic

Blessとの重複・上書き・弱点を確認します。

## Cheap Mageが多い

- Astral：Communion
- Death：Skeleton spam
- Fire / Air / Earth：同一Spellの大量Cast
- Blood：Sabbath / Hunter

MageのPath深度より、人数とCommander Point効率が勝利条件になります。

## 国家兵が弱い

- Death / Blood / Nature / Conjurationによる召喚Army
- GlamourのIllusion
- Astral / BloodのMage network
- Remote attack / Raiding

Gold兵の正面戦だけを避けます。

---

# Path levelの意味

Path level 1が「弱いMage」、4が「強いMage」と単純には言えません。

## Fire

高Pathほど範囲・Battlefield火力へ伸びます。F1はResistance、Forge、Crosspath用途が中心になりやすいです。

## Air

A2から機動・自己防御、A3から砲兵、A4以上からArmy-wide支援へ伸びやすくなります。

## Water

W2～3のQuickness・Cold支援が実用的で、中Path Mageを複数並べる価値があります。

## Earth

E2が重要な土台です。戦闘BoostやBoosterでE3～4へ届きやすく、量産Mageが強力です。

## Astral

S1はCommunion Slave、Magic Duel、支援として価値があります。人数がPath depthへ変換されます。

## Death

D2はSkeleton生成の基準になりやすく、多数雇えるD2はArmyの形を変えます。高PathはDarkness、Rigor、召喚Mageへ進みます。

## Nature

N2～3がResistance・Regeneration・召喚支援に有用で、N4～5からArmy-wide勝利条件が増えます。

## Glamour

G2～3からLuck・Confusion・Illusion支援が実用化し、高Pathで戦場全体・夢・欺瞞へ伸びます。

## Blood

B1～2はHunterとして価値があり、高Path MageはSabbath、Demon、Ritual担当になります。

## Holy

H1の数はBless / Banishment回数、H3以上はArmy全体のBlessや高度なDivine Spellへつながります。

---

# 中盤と終盤

## 中盤Army戦で強い傾向

- Earth
- Nature
- Fire
- Air
- Water
- Glamour

Army-wide Buff、Battlefield Damage、Resistance差を利用し、研究Timingで敵軍を壊します。

## 終盤の上限が高い傾向

- Astral
- Death
- Blood

Communion、高級召喚、Teleport、世界規模Ritual、増加可能なBlood経済により、通常Army以外の勝ち筋が増えます。

ただし中盤で領土差を失えば、終盤Pathの上限へ到達できません。Pathの「最終的な強さ」だけでPretenderや研究を決めないでください。

---

# Pathの組み合わせ

## Earth＋Nature

Protection、Strength、Regeneration、Reinvigoration。Thugと高HP Armyの基礎です。

## Air＋Water

Quickness、Storm、飛行、Cold / Shock。Tempoと機動を支配します。

## Fire＋Earth

高Damage、武器強化、Protection、Forge。通常Armyを火力化します。

## Astral＋他Path

Communionで他Pathの高級Spellへ到達します。Magic DuelやMR攻撃も加わります。

## Death＋Nature

Regeneration、Disease、Poison、Undead、Life Drain。生死・消耗戦を扱います。

## Glamour＋Air / Astral

Illusion、Luck、機動、MR攻撃。高価な少数精鋭と情報戦に向きます。

## Blood＋Crosspath

Demon召喚から国家にないPathを獲得し、Sabbathで高級Spellへ進みます。

---

# PretenderでPathを補う

Pretender PathはBlessだけでなく、

- Site Search
- Booster Forge
- 国家にないResistance
- Global caster
- 高級召喚
- Empowerment不要のMagic diversity

を開きます。

国家MageがE2までしかいないならPretenderのE4が何を開くか、NatureがないならN2でPoison Wardへの経路を作れるか、というようにChainで評価します。

---

# Researchを決める質問

1. 最も多く雇えるMageは何Pathか
2. 最初の戦争まで何Research入るか
3. 自軍の兵士は何を強化すると最も伸びるか
4. 敵の最も薄い防御層は何か
5. Gem incomeはどのPathが多いか
6. Boosterで何段階上がるか
7. Counterされた後の第二Pathは何か
8. Mageを前線へ出したとき研究がどれだけ落ちるか

---

# 初心者向けの覚え方

- **Fire**：敵軍を早く減らす
- **Air**：鎧を無視し、戦う場所を選ぶ
- **Water**：行動回数とFatigueを操作する
- **Earth**：兵士の物理性能を作り変える
- **Astral**：Mageの人数を高Pathへ変換する
- **Death**：Gold以外から軍を作り、消耗戦を制する
- **Nature**：Living Armyを回復・毒・持久戦で支える
- **Glamour**：敵の命中・判断・行動を壊す
- **Blood**：Populationを別の魔法経済へ変える
- **Holy**：Sacredを起動し、Undead / Demonを処理する

---

## 関連ページ

- [魔法の基本](../index.md)
- [Research](../research.md)
- [GemとBlood Slave](../gems.md)
- [Magic Path Boosting](../boosting.md)
- [Communion](../communions.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [illwiki: Magic](https://illwiki.com/dom5/dom6/magic)
