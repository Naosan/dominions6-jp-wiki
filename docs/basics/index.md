---
title: 戦闘の基礎
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# 戦闘の基礎

Dominions 6の戦闘は、「兵数」やUnitの総合点だけでは決まりません。

相手の防御を、

- 命中回避
- 盾
- Protection
- Resistance
- Magic Resistance
- HP・Regeneration
- Fatigue
- Morale

という複数の層へ分解し、自軍が最も突破しやすい層を攻撃します。

## 最初に読むページ

1. [戦闘ルール](combat-rules.md)
2. [両手武器・片手武器・盾](weapons-and-shields.md)
3. [命令とBattle Script](orders.md)

## Unitを見る順番

### 1. 生存方法

- Defenceで避けるのか
- Protectionで耐えるのか
- Shieldで受けるのか
- HP・Regenerationで粘るのか
- Luck・Mistform・Ethereal等の特殊防御か

### 2. 敵を倒す方法

- 高Damage
- 高Attack
- 多段攻撃
- 長武器・Repel
- AP / AN
- Elemental damage
- MR attack
- Poison / Fatigue

### 3. 戦線での役割

- 受け部隊
- 火力部隊
- Flanker
- Archer
- Bodyguard
- Chaff
- Sacred
- Summon

一体のUnitがすべてを担当する必要はありません。Army内で役割を分けます。

## 主要能力

| 能力 | 主な意味 |
|---|---|
| Attack Skill | 近接攻撃を当てる |
| Defence Skill | 近接攻撃を避ける |
| Protection | 命中後のDamageを軽減 |
| Strength | 近接Damage、投擲等の土台 |
| Weapon Length | Repel、間合い |
| Morale | Fear・損害・Routへの耐性 |
| Fatigue | 行動継続、回避、Armor-defeating hit |
| Magic Resistance | MR Negates系効果への防御 |
| Elemental Resistance | Fire / Cold / Shock / Poison / Acid等への防御 |
| Combat Speed | 接敵TimingとFlank能力 |
| Encumbrance | 長期戦でのFatigue蓄積 |

## 戦闘設計の基本形

```text
受ける兵
   ↓ 敵を固定する
火力兵・Mage
   ↓ 敵の弱い防御層を攻撃する
機動兵
   ↓ 後衛・退路・側面へ圧力をかける
```

Armyを「強いUnitの塊」ではなく、**複数の役割が連動する仕組み**として作ります。

## Battle Replayの見方

- 最初にどのSquadが接敵したか
- 何のDamage typeで死んだか
- Clean HitかShield Hitか
- Protectionを抜かれたのか、ANだったのか
- Mageが指定Spellを使ったか
- Fatigue 100へ何Roundで達したか
- Commander死亡とRoutの順番
- Friendly Fire
- Gem消費

負けた原因が分からない場合は、[戦闘ルールのBattle Replay分析手順](combat-rules.md)を参照してください。
