---
title: Resistance・Utility Item
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# Resistance・Utility Item

Resistance Itemは、Commanderの弱点を埋め、特定のEnemy Spell・Battlefield effect・Terrainへ対応する装備です。

「万能に硬くする」のではなく、**次の戦闘で受けるDamage typeを予測して必要なResistanceだけを付ける**のが基本です。

正確な現行Itemは[Resistance・MR Item一覧](../data/items/resistance.md)と[Utility Item一覧](../data/items/utility.md)、個々の効果は[Dom6 Mod Inspector](https://larzm42.github.io/dom6inspector/)で確認してください。

---

# 主なResistance

## Fire Resistance

対策するもの：

- Fire Evocation
- Fire Shield
- Fire Storm
- Heat battlefield
- Flaming weapon
- Fire Elemental

### 向くCarrier

- Fire battlefieldのCaster
- Fire Shield持ちへ接近するThug
- Phoenix Pyre等を使うMage
- 素のFire Resistanceが低い、またはFire Vulnerabilityを持つ重要Commander

種族名だけで「Plant / UndeadだからFireに弱い」と決めず、Unit詳細のResistanceとVulnerabilityを確認します。

## Cold Resistance

対策するもの：

- Cold Evocation
- Grip of Winter
- Frost weapon
- Cold Aura
- Water / Ice Elemental

Quickness Armyや重装ArmyはFatigue対策としてもCold Resistanceが重要になる場合があります。

## Shock Resistance

対策するもの：

- Lightning Bolt
- Thunder Strike
- Shock Wave
- Wrathful Skies
- Shock weapon
- Air Elemental / Storm unit

ProtectionはArmor Negating Shockを止めません。高Protection CommanderほどShock Resistanceの優先度が高い場合があります。

## Poison Resistance

対策するもの：

- Foul Vapors
- Poison cloud
- Poison weapon
- Snake / Spider / Plant unitのPoison attack
- その他Poison Damage

高HP・高ProtectionのLiving CommanderはPoisonを長く蓄積するため、対Nature戦で重要になる場合があります。

!!! warning "DiseaseはPoisonと別"
    Poison ResistanceはPoison DamageへのResistanceです。Disease / Plague / Disease Cloud等を自動的に防ぐものとして扱わないでください。Disease対策はDisease Resistance、Healer、戦闘時間、発生源除去など別の仕組みを確認します。

## Acid Resistance

Acid Damageを軽減します。

Acid系攻撃はArmorへ影響する効果を伴う場合もあるため、Item名だけでなく個々の攻撃効果をInspectorやBattle Replayで確認します。

## Magic Resistance

対策するもの：

- Soul Slay
- Paralyze
- Charm / Enslave
- Confusion
- Control Undead
- 各種MR Negates

MR Itemは高価なThug、Pretender、Battlefield caster、Unique Mageへ優先します。

---

# Resistanceの重ね方

Resistanceは一個のItemで十分とは限りません。

- 素Resistance
- Bless
- Spell
- Item
- Scale
- Unit classification

を合計します。

Dom6ではElemental Resistanceは単純な固定値軽減だけではなく、Incoming Damageに対する割合軽減も含む仕組みへ変更されています。したがって「Damage 20ならResistance 20で完全無効」という単純な引き算として扱わず、ゲーム内表示と実戦結果を確認します。

## Itemだけで全員を守らない

Army全体へ必要なResistanceはWard系Spellで配り、

- Caster
- Thug
- Prophet
- Communion Master
- Rare Mage

だけItemで補います。

## 過剰Resistance

Enemy Damageを十分抑えられる値を超えてItem slotを使うと、MR、Reinvigoration、Mobility等が不足します。

Enemy SpellのDamageと回数をReplayで確認します。

---

# Damage Prevention系Utility

## Air Shield

Arrow、Bolt等の射撃命中を減らします。

通常近接、AoE、必中Spellには別対策が必要です。

## Luck

致命的な攻撃を確率で無効化します。

多段攻撃、持続Damage、Fatigue、Morale、Controlへは別防御が必要です。

## Ethereal

非Magic attackを通しにくくします。

**True Sight / Spirit Sightを持つだけではEtherealを無効化しません。** Etherealへの基本CounterはMagic Weapon、Spell、Magic Damage等です。

## Mistform / Damage reduction

大Damageを小さくしますが、特定Damage・Magic attack・一定条件で解除されます。

True Sight / Spirit SightはBlurやDisplacement等、一部のGlamour系視認妨害をCounterしますが、すべてのGlamour効果やMistformそのものを一括無効化する能力として扱わないでください。

## Invulnerability

通常物理へ強力ですが、Magic Weapon、Elemental、MR攻撃を防ぎません。

---

# Fatigue Utility

## Reinvigoration

毎RoundFatigueを減らします。

重要なCarrier：

- Heavy armor Mage
- Quickness Thug
- Earth / Fire battlefield caster
- Berserker
- 長期戦SC

Reinvigorationがあっても、Spell一発のFatigueが大きすぎれば気絶します。Path boostと併用します。

## Encumbrance軽減

Armorを軽くする、Armorを交換する、Natural Protectionへ移すなど、Fatigue発生源自体を減らす方法があります。

## Fatigue回復手段

Life Drain、Reinvigoration Spell、Blood系のFatigue回復などとItemを組み合わせます。

---

# Regeneration・HP

## Regeneration

毎RoundHPを回復します。

高HP Commanderほど一回の回復量が大きくなり、継続的な小DamageやPoison Damageを受ける長期戦でも生存時間を延ばせます。

ただしPoison Resistanceの代替ではありません。Poison蓄積がRegenerationの回復を上回れば死亡します。一撃死、AN Burst、Soul Slay、Decay、Disease等にも別対策が必要です。

## HP増加

- Burst耐性
- Regeneration回復量
- Affliction発生Risk

へ影響します。

しかしHPだけ増やしてDefence・Protection・ResistanceがないとDamageを受け続けます。

---

# Mobility Utility

## Flying

- Mountain / River等のStrategic movement
- Attack Rear
- Battlefield obstacle回避
- Raid

を助けます。

Storm、Enemy Air control、着地点、Flying制限を確認します。

## Water Breathing / Amphibious

地上Commanderを水中へ移動させます。

- Armor・Combat Speedの水中penalty
- Itemを外すと帰れない
- Army全員の水中適性
- Sea ProvinceのLab

を確認します。

## Teleport / Magic Phase Item

奇襲・迎撃へ使いますが、到着後に勝てる装備と帰還手段が必要です。

## Strategic movement bonus

ArmyとCommanderのMap Moveを揃えます。一人だけ速くてもArmy全体は遅いUnitへ制限されます。

---

# Vision Utility

## Darkvision

Darkness、Cave、Night environmentで視界Penaltyを減らします。

## True Sight / Spirit Sight

Invisibility、Unseen、Blur、Displacement等の**視認・Glamour由来のPenalty**へ対処します。

Spirit SightはDarknessへの視界も強力ですが、True SightとSpirit Sightの対象範囲を「Illusionなら全部」「Etherealにも有効」と一般化しないでください。Spell / Abilityごとの説明を確認します。

## Etherealは別問題

Etherealは視認できるかではなく、非Magic Weaponが有効に当たりにくい防御です。Magic WeaponやMagic Damageを用意します。

## Blindness prevention

BlindnessやEye Lossへの耐性・無効化はSight能力と同一ではありません。個々のItem / Abilityの説明を確認します。

---

# Leadership Utility

## Inspirational / Leadership

通常兵のMoraleとSquad sizeを改善します。

## Undead Leadership

Undead Armyを率います。

## Magic Leadership

Magic Beingを率います。

## Taskmaster

Slave UnitのMoraleと管理を改善します。

強いSummonを作ってもLeadershipがなければArmyへできません。

---

# Supply・Siege・Patrol

## Supply

大軍、Winter、Waste、Enemy territoryでStarvationを防ぎます。

## Siege bonus

Fort攻略を早め、敵救援前にStormできます。

## Patrol bonus

Stealthy Raider、Blood Hunt Unrest、Assassin対策へ使います。

## Scout / Scrying

Commanderを戦闘以外の情報役へ変えます。

---

# Enemy別の優先Item

| Enemyの主力 | 優先するもの |
|---|---|
| Fire Evocation | Fire Resistance、HP、Fire Shield対策 |
| Thunder Strike | Shock Resistance、HP、分散 |
| Foul Vapors | Poison Resistance、Regeneration、Caster狩り |
| Soul Slay | MR、Antimagic、Duel / Caster狩り |
| Crossbow | Shield、Air Shield、Mist、Flying圧力 |
| Darkness | Darkvision、Spirit Sight、Light spell |
| Skeleton spam | Reinvigoration、AoE、Holy、Undead counter |
| Invisibility / Unseen / Blur | True Sight / Spirit Sight、AoE、視認不要の攻撃 |
| Ethereal | Magic Weapon、Magic Damage |
| Cold / Grip | Cold Resistance、Reinvigoration |
| Fire Shield Thug | Fire Resistance、射撃、MR attack |

---

# 装備前チェック

```text
Enemy Damage type：
一発Damage / 回数：
Carrierの素Resistance：
Army-wide Spell：
必要な追加Resistance：
Item slot競合：
Carrier死亡時の損失：
別Counterの方が安いか：
```

---

# よくある失敗

## Protection Itemだけ積む

AN、Poison、MR attack、Fatigueで死にます。

## 全Resistanceを少しずつ積む

主力Damageへ十分な値がなく、すべてに中途半端です。

## Poison ResistanceでDiseaseまで防げると思う

PoisonとDiseaseは別の仕組みです。相手の能力欄とBattle effectを分けて確認します。

## True Sight / Spirit Sightを万能Counterと思う

視認系Glamour効果には有効でも、Ethereal、Mistform、False Damage、すべてのIllusionを自動的に消す能力ではありません。

## Casterへ重装Armor

Resistanceは増えてもSpellcasting Encumbranceで気絶します。

## Army-wide Wardと重複

既にSpellで十分なResistanceを得るなら、Item slotをMR・Reinvigorationへ使います。

## Enemyを見ずに固定セット

Thug装備は相手ごとに組み替えます。

---

## 関連ページ

- [Magic Item](index.md)
- [Forge計画とConstruction Breakpoint](forge-planning.md)
- [Thug / SC装備](thug-equipment.md)
- [Magic Path Booster](boosters.md)
- [Resistance・MR Item一覧](../data/items/resistance.md)
- [Utility Item一覧](../data/items/utility.md)
- [戦闘ルール](../basics/combat-rules.md)
- [Magic Path総論](../magic/paths/index.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
