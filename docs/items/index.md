---
title: Magic Item
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# Magic Item

Magic Itemは、Commander一体を強くする装備であると同時に、**Magic Path・Research・Gem economy・Army counterを接続する技術ツリー**です。

Itemを評価するときは、効果だけでなく次を見ます。

- Construction level
- Forge要求Path
- 基礎Gem costと実際のForge cost
- Forge Bonus / 国家割引
- 装備Slot
- Carrierの素Stats
- Forge担当Mageの一Turn
- 何Turn・何戦使えば投資を回収するか
- Carrier死亡時の喪失Risk
- そのItemで新しく何が可能になるか

正確な現行Itemの要求Path・効果・Constructionは[Magic Itemデータ索引](../data/items/index.md)と[Dom6 Mod Inspector](https://larzm42.github.io/dom6inspector/)を使い、この手書き領域では**どの状況でForgeするか**を扱います。

---

# 目的別ページ

- [Forge計画とConstruction Breakpoint](forge-planning.md)
- [Magic Path Booster](boosters.md)
- [Research Item](research-items.md)
- [Resistance・Utility Item](resistance-items.md)
- [Thug / Supercombatant装備](thug-equipment.md)

---

# 初心者向け：Itemを作る・探す

## Forge Item

Magic Itemは、自国のLaboratoryがあるProvinceでMageへ`Forge Item` orderを出して作ります。

そのMageはForgeに一Turn使うため、そのTurnはResearchやRitual等へ使えません。

## Shift + O — Monthly Forge

同じItemを毎Turn繰り返し作る場合は、Commanderを選択して**Shift + O**でmonthly forgeを設定できます。

Research Item等の量産に便利ですが、戦況が変わっても資源を使い続けるので、開戦時には不要なmonthly orderを止めます。

## F7 — Magic item treasury

Treasuryに保管中のItemを確認します。

## F8 — Magic item overview

Treasuryだけでなく、**Commanderが装備中のItemを含めて王国全体の所在**を確認できます。

「Boosterを誰に渡したか分からない」「Research Itemを前線Mageが付けたまま」という事故を減らすため、戦争前や大規模な装備組み替え時に使います。

---

# 装備Slot

## One-handed Weapon

片手武器です。Shield、二本目のWeapon、Extra Arm装備と組み合わせられます。

主な用途：

- Magic Weaponの付与
- Armor Piercing / Armor Negating
- Life Drain
- Fire / Frost / Shock AoE
- Armor破壊
- Anti-undead / Anti-demon
- MR / Soul attack

## Two-handed Weapon

両手を占有します。

高Damage、長武器、強力な特殊効果を得やすい代わりにShieldを失います。

CarrierのStrength、Attack、素のProtectionを確認します。

## Shield

Parry、Shield Protection、射撃防御を与えます。

重いShieldはDefence・Encumbranceへ不利を与える場合があります。

## Armor

Body ProtectionとEncumbranceを決めます。

Mageへ重装Armorを着せるとSpellcasting Encumbranceで早く気絶する場合があります。

## Helmet

Head Protectionを補います。

良いBody Armorだけを装備しても、Head Hitで倒される場合があります。

## Boots

- Path Booster
- Strength
- Quickness
- Flying
- Reinvigoration
- Resistance
- Strategic movement

など重要Itemが競合するSlotです。

## Miscellaneous

Booster、Resistance、Regeneration、Reinvigoration、Luck、MR、Leadership等を持つItemが集まります。

CommanderごとのMisc slot数を確認します。

## Extra Slot / Mount / Special

多腕、Mount、特殊Chassisは通常と異なるSlot構成を持ちます。Itemを作る前に装備可能か確認します。

---

# Forgeの基本

## Laboratory

Magic ItemはLaboratoryでForgeします。

ForgeするMageは、そのTurnにResearch、Ritual、移動を行えません。

## Construction Breakpoint

Dom6の通常Itemは主にConstruction **1 / 3 / 5 / 7 / 9**で解禁されます。

次のlevelへ進む前に「そのBreakpointで何を作るか」を決めます。詳しくは[Forge計画とConstruction Breakpoint](forge-planning.md)を参照してください。

## 要求Path

通常、Itemが要求するPathをMageが持つ必要があります。

- 素Path
- 装備Booster
- Empowerment

は利用できますが、戦闘中だけのPath boostやGem boostはForgeへ使えません。

## Gem cost

ItemのPathに対応するGemを使います。

複合Path Itemは複数種類のGemを要求する場合があります。

自動生成表のGem欄は基礎Costを示します。Forge Bonus、国家割引、Item固有Cost等を含む**最終支払額はゲーム内Forge画面を優先**します。

## Forge Bonus

国家能力、Mage能力、Forge discount Item等でGem costを減らせます。

ただしdiscount基盤自体にもGemとForge turnが必要です。大量生産するほど回収しやすくなります。

---

# Itemの四つの価値

## 1. 新しいPathへ届く

Boosterから高級Spell、Summon、Global、次のBoosterへ進みます。

これは戦闘Itemより国家全体への影響が大きい場合があります。

## 2. Researchを増やす

Research ItemはMage turnあたりの研究量を増やし、将来のBreakpointを早めます。

## 3. Counterを作る

Enemy Shock、Poison、Soul Slay、Ethereal、Regeneration等へ必要なItemを少数だけ作ります。

## 4. Commanderへ任務を与える

普通のCommanderを、

- Raider
- Anti-Thug
- Siege breaker
- Assassin
- Battlefield caster
- Gem carrier
- Scout / mobile support

へ変えます。

---

# Itemを大量生産する前の質問

1. 誰へ装備させるか
2. 何に勝てるようになるか
3. Itemなしでは何に負けるか
4. 同じGemでBattle Spellを使う方が強くないか
5. Carrierは何Turn・何戦使う見込みか
6. Carrierを失った場合の損失は何か
7. Slot競合はないか
8. Forge担当MageのTurnを使う価値があるか
9. Constructionへ寄り道するResearch costを回収できるか
10. F8で後から回収・再配備できるか

---

# 装備セットの考え方

Thug装備は「空Slotを全部埋める」作業ではありません。

次の役割を必要な分だけ揃えます。

## Offense

- Magic Weapon
- 命中
- Damage
- AoE
- Armor counter

## Defence

- Protection
- Shield
- Defence
- Mistform / Luck / Ethereal
- Elemental Resistance
- MR

## Sustain

- Regeneration
- Reinvigoration
- Life Drain
- Recuperation

## Mobility

- Flying
- Teleport
- Strategic movement
- Amphibious / Water Breathing

## Utility

- Leadership
- Supply
- Patrol
- Siege
- Stealth
- Scout

Carrierが元から持つ役割はItemで重複させず、欠けている部分だけ補います。

---

# ItemとBattlefield Spellの比較

## Itemが向く場合

- 同じCommanderが何度も使う
- Ritual / Forge Pathを上げる
- 毎戦必要なResistance
- 少数の重要Casterを守る
- Raiderが複数Provinceを取る

## Spellが向く場合

- Army全体へ作用する
- 一戦だけ必要
- Itemを全員へ配るGemがない
- Casterを守れる
- Slotを空けたい

例：Shock Resistance Itemを前衛100人へ配ることはできません。Army-wide Wardを使い、Casterなど少数だけItemで補います。

---

# Item lossと回収

**RoutしただけでItemを失うわけではありません。** Commanderが生還して退却できれば装備は継続して使えます。

本当に警戒するのは、Carrierの死亡、暗殺、退却不能、敵へ装備を渡す形になる戦闘などです。高価なItemほど、ItemそのものだけでなくRare MageやHero等のCarrier価値も含めてRiskを考えます。

### Riskを下げる

- Rare Booster carrierを不要に前線へ出さない
- Itemを一人へ集中しすぎない
- Retreat先を確保する
- Soul Slay / Magic Duel / AN等、Carrierの弱点を補う
- Gem carrierとThugを分ける
- 戦闘後に不要ItemをTreasury / 後方Carrierへ戻す
- F8で重要Itemの所在を定期確認する

---

# Artifact

Construction 9のArtifactはUnique Itemです。

- 世界に一つだけ
- 高いConstruction / Path要求
- 特殊なGlobal・Summon・Commander能力
- 先着競争
- Carrierを失ったときの大きなRisk

を持ちます。

「作れるから作る」のではなく、そのArtifactがゲーム終了までに何を生むかを評価します。

---

# 国家攻略でのItem記述形式

| 優先 | Itemの役割 | 目的 | Carrier | 敵 / 戦況 | 備考 |
|---|---|---|---|---|---|
| S | Booster | Path access | Rare Mage | 常時 | 国家技術基盤 |
| A | Resistance | Counter | Battle Mage | 特定Enemy | 必要数のみ |
| B | Weapon | Raider | Commander | PD / Thug | 損失Risk |

Itemを一律Tier化せず、国家・Carrier・敵との組み合わせで評価します。

---

# よくある失敗

## Item欄を全部埋める

Gem costが増え、HPの低い人間Commanderへ過剰投資します。

## 武器だけ強くする

Attack、MR、Resistance、Fatigue不足で一度も攻撃できず死にます。

## 防具だけ重ねる

AN、Poison、MR attack、Fatigueに負けます。

## Boosterを戦場へ持ち出す

国家唯一のPath accessとItemを同時に失うRiskを取ります。

## Research Itemを前線Mageへ付けたままにする

戦闘中は研究していないため、Research bonusの価値を使っていません。F8で確認します。

## Monthly Forgeを止め忘れる

Shift + Oで量産中のItemが、戦争用Gemまで消費します。

## 古いItem表を使う

Dom6ではConstruction level、Path、Glamour移行、Item名等が旧作と異なる場合があります。6.35 Inspectorとゲーム内表示を優先します。

---

## 関連ページ

- [Forge計画とConstruction Breakpoint](forge-planning.md)
- [Magic Path Booster](boosters.md)
- [Research Item](research-items.md)
- [Resistance・Utility Item](resistance-items.md)
- [Thug / SC装備](thug-equipment.md)
- [Magic Itemデータ索引](../data/items/index.md)
- [Magic Path Boosting](../magic/boosting.md)
- [Gem](../magic/gems.md)
- [両手武器・片手武器・盾](../basics/weapons-and-shields.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
