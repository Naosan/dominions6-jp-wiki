---
title: Communion・Sabbath
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Communion・Sabbath

Communionは、複数のMageをMasterとSlaveへ分け、

- MasterのMagic Pathを上げる
- Spell Fatigueを分散する
- Self-only BuffをSlaveへ共有する

仕組みです。

AstralのCommunion、BloodのSabbath、特定UnitのChorusなど、似た仕組みが複数あります。

!!! warning
    Communionは強力ですが、Scriptを誤るとSlaveが気絶・Affliction・死亡し、Army全体の魔法計画が崩れます。まず小規模なテスト戦で確認してください。

---

# MasterとSlave

## Communion Master

Masterが実際にSpellをCastします。

MasterはSlave数に応じて、**元から持っているすべてのMagic Path**が上昇します。

## Communion Slave

SlaveはMasterのSpellを支え、Fatigueの一部を引き受けます。

Communion中のSlaveは通常行動できず、非常に無防備です。Attack Rear、Arrow、AoE、Earthquake等から守る必要があります。

---

# Path Boost

MasterのPath bonusはSlave数で決まります。

| Slave数 | MasterのPath bonus |
|---:|---:|
| 2 | +1 |
| 4 | +2 |
| 8 | +3 |
| 16 | +4 |
| 32 | +5 |
| 64 | +6 |

必要数は指数的に増えます。

### 攻略上の意味

- S1 Mageを2人用意すれば、複数Masterが+1を得る
- 4人なら+2となり、低Path国家でも高級Spellへ届く
- Master数を増やしてもPath bonus自体は減らない
- しかしMasterが多いほどSlaveへ流れるSpell回数が増え、死亡しやすくなる

「何人SlaveがいればPathへ届くか」と「何人Masterを安全に動かせるか」は別問題です。

---

# Fatigue分散

MasterがSpellをCastすると、計算されたFatigueがMasterとSlaveへ分散されます。

単純には参加人数が多いほど、一人あたりのFatigueは減ります。しかしSlaveが受けるFatigueには、**MasterとSlaveの該当Path差**による倍率があります。

## Slave Fatigue multiplierの考え方

SpellのPrimary Pathについて、Communion bonusを除いたMasterのPathとSlaveのPathを比べます。

| MasterとSlaveの関係 | Slave側の傾向 |
|---|---|
| SlaveのPathがMasterより高い | Fatigueが少ない |
| 同程度 | 標準 |
| Masterの方が高い | Fatigueが増える |
| MasterがSlaveの約2倍以上 | 非常に重いFatigue |

したがって、S1 SlaveでAstral Spellを支えるのは比較的自然ですが、同じS1 Slaveへ高いFire MasterがFire Spellを連打させると、Slaveが急速に壊れることがあります。

---

# Communion bonusとFatigue計算

MasterはCommunion bonus込みの高PathとしてSpell Fatigueを軽減します。

一方、Slaveへの倍率を決めるPath比較では、Communion bonusを除いたMasterの素Path・Item・その他Boostが重要になります。

このため、

- MasterだけへPath Boosterを積む
- GemでMaster Pathを上げる
- Slaveが持たないCrosspath Spellを連打する

とSlave負担が急増する場合があります。

---

# Self-only Buffの共有

MasterがCaster自身だけを対象にするSpellをCastすると、Communion Slaveにも同じ効果が適用されます。

代表的な用途：

- Personal Regeneration
- Elemental Resistance
- Air Shield
- Personal Luck
- Summon Earthpower等のPath boost / Reinvigoration
- ReinvigorationによるFatigue reset

### 重要な意味

Slaveへ個別Scriptを入れられなくても、Master一人がSelf BuffをCastすることで全Slaveを保護できます。

ただしBuffのPathがSlaveに低い場合、そのBuffをCastする過程自体で大きなFatigueが流れる可能性があります。

---

# 基本構成

## 小型Communion：2 Slave

```text
Slave ×2
Master ×1～3
```

用途：

- +1 Pathで届くSpell
- 小規模なResistance / Buff
- Gem節約
- Communion操作の練習

Masterを増やしすぎると、SlaveがSpell回数に耐えません。

## 標準Communion：4 Slave

```text
Slave ×4
Master ×2～5
```

+2 Pathで多くの中級・高級Spellへ届きます。

Masterを役割分担し、同時に同じBuffを重複Castしないようにします。

## 大型Communion：8 Slave以上

Army-wide spell、Battlefield Enchantment、複数Pathの高級魔法を並列化できます。

ただし、

- Slave保護
- Master数
- Fatigue reset
- Gem budget
- Enemy assassination / Earthquake / battlefield damage

が必須になります。

---

# Script例

## Astral基本型

### Slave

```text
Communion Slave
```

以後はCommunionが続く限り行動しません。

### Master A：防御

```text
Communion Master
Antimagic / Resistance / Defensive buff
Cast Spells
```

### Master B：攻撃

```text
Communion Master
Path boost
Soul / Mind / Elemental attack
Cast Spells
```

### Master C：Slave保護

```text
Communion Master
Personal Regeneration等
Reinvigoration可能ならFatigue reset
Cast Spells
```

---

# Sabbath

SabbathはBlood版Communionです。

特徴として、

- 加入にBlood Slaveを使う場合がある
- Astral CommunionとCasting time・Fatigue配分が異なる
- Master側の負担が軽く、Slave側の負担が重い傾向
- Blood 1のReinvigorationをSlave全体へ共有できる

ことがあります。

Blood国家ではSabbath MasterがReinvigorationをScriptへ挟み、Slave Fatigueを周期的に消す戦術が重要です。

ただしBlood Slaveが戦場で殺されると、加入やSpell costを支払えません。

---

# Matrix Item

Magic Itemによって、Astral Pathを持たないMageをMasterまたはSlaveとしてCommunionへ参加させられる場合があります。

これにより、

- Earth Mageを高Path Army buff担当へする
- Fire / Air / Nature MageをAstral Slaveで支える
- National Mageの狭いPathを統合する

ことができます。

### 注意

非Astral Masterが持つPathをAstral Slaveが支える場合、Path差によるFatigue倍率が非常に危険です。

Matrixを装備できることと、安全にSpellを連打できることは別です。

---

# Slaveを守る方法

## 配置

- 中央後方
- Masterと同じ側
- Bodyguard付き
- Blood Slaveと混同しない位置

## Buff

- Elemental Resistance
- Air Shield
- Regeneration
- Luck
- Reinvigoration
- HP増加

## Army設計

- Rear attackを止める左右後方Squad
- Flying対策
- Arrow Fend / Storm
- Earthquake等を撃つ相手へのCounter
- Slaveを一か所へ密集しすぎない

---

# Slaveが死ぬ主な原因

## Masterが多すぎる

一CastあたりのFatigueが小さくても、Spell回数で200へ到達します。

## Crosspath差

Slaveが持たないPathの高級SpellをMasterが連打し、Fatigue倍率が上がります。

## Heavy armor

Spellcasting Encumbranceも分配されます。重装Masterの大量CastはCommunion全体へ負担をかけます。

## Innate Spellcaster Master

Innate SpellcasterはSlave負担を増やす特殊な挙動があります。

## Communion終了時

Masterが全滅・退却してCommunionが終わると、Slaveへ大きなFatigue feedbackが発生します。敵がMasterだけを暗殺すると、Slaveも機能停止する場合があります。

## Enemy attack

Slaveは行動不能なので、接近されるとほぼ抵抗できません。

---

# 安全運用の手順

1. 使いたいSpellと要求Pathを決める
2. 必要なSlave数を計算する
3. MasterごとのPrimary Pathを確認する
4. SlaveとのPath差を確認する
5. 各Masterが何回Castするか数える
6. SlaveへResistance / Regeneration / Reinvigorationを配る
7. Bodyguardと後方迎撃を置く
8. 小規模テストでReplayを見る
9. Fatigue 100 / 200へ到達するRoundを記録する
10. Master数またはSpellを減らす

---

# Communionの強み

- Cheap S1を高Pathへ変換
- 一つのSlave poolで複数MasterをBoost
- Army-wide Spellを並列化
- Gem boost依存を減らす
- Crosspath国家の全Pathを統合
- Self BuffをSlaveへ共有
- Late gameの高Path要求へ届く

---

# Communionの弱み

- Slaveが無防備
- Scriptが複雑
- Master死亡で全構造が崩れる
- Fatigue計算ミスが致命的
- Earthquake・Rain of Stones・遠隔Damageに弱い
- Anti-magicやMR強化で主力Spellが止まる場合がある
- Magic Duel等でAstral Masterが狙われる

---

# よくある失敗

## 「4 SlaveならMasterを何人でも置ける」

Path bonusは全Masterへ付きますが、Slaveが受けるSpell回数もMaster数に比例します。

## Slaveへ高価なItemを積む

守る価値はありますが、全滅すると大量Itemを失います。必要なResistance・Reinvigorationへ絞ります。

## Master全員へ同じScript

Buff重複とFatigue浪費が起きます。役割を分けます。

## SlaveとMasterのPath差を見ない

Communion bonusだけを見ているとSlaveが即死します。

## Reinvigoration一回で安全だと思う

AIがScriptを飛ばす、Blood Slaveが死ぬ、Master自身のFatigue状態で選択が変わる等があります。

## Masterを前へ置く

Master死亡でCommunionが終わり、Slaveへfeedbackが入ります。

---

# 初心者向け最小形

まずは同系統のAstral Mageだけで、

```text
S1 Slave ×2
S2前後 Master ×1～2
```

を使い、

- +1 Path
- 低FatigueのBuff
- GemなしSpell

から試します。

いきなりMatrix、Crosspath、Turbo communionへ進むより、ReplayでFatigue分配を理解する方が安全です。

---

## 関連ページ

- [魔法の基本](index.md)
- [Research](research.md)
- [GemとBlood Slave](gems.md)
- [Magic Path Boosting](boosting.md)
- [Astral](paths/astral.md)
- [Blood](paths/blood.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [illwiki: Communions](https://illwiki.com/dom5/dom6/communion)
- [illwiki: Combat Magic](https://illwiki.com/dom5/dom6/combat-magic)
