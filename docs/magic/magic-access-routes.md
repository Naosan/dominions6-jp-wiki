---
title: Magic Access到達経路
status: expanding
verified_version: "6.35"
last_verified: "2026-08-15"
---

# Magic Access到達経路

国家のMagic Accessは、最終的なPathだけを一覧にすると誤解しやすくなります。

たとえば同じ`E4`でも、

```text
固定E4を通常Recruitできる
E2がBoosterを二段ForgeしてE4へ届く
E2がCommunionで戦闘中だけE4になる
E2がEmpowermentを受けてE3になりBoosterでE4へ届く
E2がMage召喚を二段つないでE4 Mageを得る
```

では、必要Research、Gem、Turn、再現性、利用可能な局面が異なります。

このWikiではMagic Accessを、**到達Pathではなく経路付きのLayer**として扱います。

---

## 最初に見るページ

- [国家別Magic Access到達経路](../data/magic-access-routes/index.md)
- [Booster route](../data/magic-access-routes/booster-routes.md)
- [再帰Mage summon chain](../data/magic-access-routes/summon-chains.md)
- [Communion・Sabbath battle reach](../data/magic-access-routes/communion-sabbath.md)
- [Empowerment gap](../data/magic-access-routes/empowerment-gaps.md)
- [国家別拡張Magic Access](../data/extended-magic-access/index.md)
- [Magic Path Boosting](boosting.md)
- [Communion・Sabbath](communions.md)

---

# 戦略Pathと戦闘Pathを分ける

## 戦略Path

次に使えます。

- Ritual
- Mage summon
- Global Enchantment
- Forge
- Remote Site Search
- Empowerment

戦略Pathへ寄与する主な手段は、

```text
素Path
＋装備中のMagic Item
＋Empowerment
＋別Mageの召喚
```

です。

## 戦闘Path

戦闘中はさらに、

- Communion / Sabbath
- 戦闘中の自己Path boost
- Gem boost
- Storm等のBattlefield条件

を使えます。

しかし、これらは通常RitualやForgeには使えません。

したがって、

> CommunionでE5へ届くからE5召喚Spellを使える

という計画は成立しません。Communionは戦闘用、Mage summonは戦略画面のRitualです。

---

# Routeの確度

## Guaranteed

固定Path、固定Target、明示された国家条件だけで再現できる経路です。

例：

```text
固定E2 Mage
→ Earth BoosterをForge
→ E3
```

## Random-assisted

MageのRandomが必要な経路です。

```text
固定E2
＋100% +1 [F/A/W/E]
→ Eへ当たった個体だけE3
```

実現可能性と出現確率は別です。

## Candidate-pool

特殊召喚の候補集合に目的Mageが含まれる経路です。

一回のCastでそのMageを得る保証はありません。

## Manual bridge

Empowerment、Pretender設計、一般Magic Site、Eventなど、データだけでは自動経路として確定しにくい手段です。

---

# Booster route

## 何を計算するか

自動生成Profileでは、通常Recruit Mage一体を起点に、Forge可能なPath Boosterを最大三段までつなぎます。

```text
Mageの固定Path
→ 既に作ったBoosterを装備
→ 次のBooster要求Pathを満たす
→ Forge
→ 最終装備を選び直す
```

同じMageがForgeを担当する**single-forger chain**です。

## Standard slot仮定

計算では標準的な装備枠を仮定します。

| Slot group | 容量 |
|---|---:|
| Hand | 2 |
| Head / Crown | 1 |
| Body | 1 |
| Boots | 1 |
| Miscellaneous | 2 |

- 片手武器・盾はHand 1
- 両手武器・射撃武器はHand 2
- Bardingは標準Chassisの計算から除外

実際のUnitには、装備不可、Extra Arms、手がない、Size・Strength制限などがあります。

したがって自動Routeは、**Pathと標準Slot上の到達可能性**を示し、最終的な装備可否はUnit詳細とゲーム内表示で確認します。

## ForgeしたItemと最終装備は別

Booster chainでは、途中のItemを使って次のItemをForgeし、その後に持ち替える場合があります。

```text
Booster Aを装備
→ Booster BをForge
→ Aを外してBを装備
```

そのためProfileでは、

- Forge route
- 最終装備

を分けて表示します。

## 含まれない補正

- Forge Bonus
- Dwarven Hammer等のGem割引
- 国家固有Rebate
- Unit固有Slot数
- ItemのUnique / Artifact競合
- Boosterを別MageがForgeして渡す国家全体の分業

国家全体で分業すれば、自動表示より強い経路が成立する場合があります。

---

# 再帰Mage summon chain

一段召喚だけでなく、召喚したMageが次のMageを召喚する経路を追います。

```text
Native Mage
→ Spell A
→ Summoned Mage A
→ Spell B
→ Summoned Mage B
```

## Guaranteed chain

- 通常Recruit Mageの保証Pathを起点にする
- 固定TargetのRitual summonだけを使う
- 召喚Mageも保証Pathだけで次の要求を判定する
- 最大三段まで追跡する

## Random-assisted chain

- Native Mageまたは召喚MageのRandomが要求Pathへ当たる可能性を使う
- 出現確率は計算しない
- 国家計画の主線ではなく、条件付きOptionとして扱う

## Candidate pool

Unique pool、Terrain pool、Tartarian系などは別です。

候補Mageを固定Targetとして再帰Chainへ投入しません。

## 深さ制限

自動生成は三段までです。

これは「四段目が存在しない」という意味ではなく、経路が長くなるほど、

- Research
- Gem
- Unique状態
- Random個体
- Caster保護
- Ritual turn

の不確実性が増えるためです。

---

# Communion・Sabbath battle reach

Communion / Sabbathは戦闘中のPath到達を計算します。

| Slave数 | Path bonus |
|---:|---:|
| 2 | +1 |
| 4 | +2 |
| 8 | +3 |
| 16 | +4 |
| 32 | +5 |

自動Profileでは、通常Recruit Mageのうち、

- Communion: 保証S1以上
- Sabbath: 保証B1以上

をMaster / Slave候補として扱います。

Masterが元から持つArcane Pathだけにbonusを加えます。HolyはCommunion bonus対象として計算しません。

## 表が示さないもの

- Slaveが安全に何回Castへ耐えられるか
- Master数
- Fatigue倍率
- Self-only Buff共有
- Matrix Item
- Blood Slaveの消費と生存
- Communion終了時feedback

したがって、到達可能Pathと安全なScriptは別に設計します。

---

# Empowerment gap

Boosterと固定召喚Chainを使っても残るPathを、Empowerment gapとして表示します。

これは、

> EmpowermentすべきPath

ではありません。

次のどれかが必要になる可能性がある、という警告です。

- Empowerment
- Pretender設計
- Hero
- Start / Future Site Mage
- 一般Magic Site Mage
- Candidate-pool summon
- Event・Mercenary
- Boosterを別MageがForgeして渡す分業

Empowermentの実際のGem / Blood Slave costは、対象Mageの現在Pathやゲーム仕様に依存するため、自動表で固定値を断定しません。ゲーム内のEmpowerment画面を優先します。

---

# 国家ページの読み方

国家別ページは次の順で読みます。

## 1. Native baseline

通常Recruit Mageで確実に使えるPathです。

## 2. Booster best route

戦略画面で使えるPathを、single-forger chainでどこまで伸ばせるか確認します。

## 3. Fixed summon chain

ResearchとGemを投資した後に、どのMageへ到達できるか確認します。

## 4. Communion / Sabbath

戦闘中だけ必要なPathを確認します。

## 5. Empowerment gap

残るPathを、国家設計・Hero・Site・Empowermentのどれで補うか考えます。

---

# Route計画テンプレート

```text
目的Spell / Item：
必要Path：
戦略Pathか戦闘Pathか：
開始Mage：
Booster route：
必要Construction：
必要Gem：
召喚Spell：
必要Research：
召喚深度：
Random依存：
Communion Slave数：
Empowermentが必要か：
代替経路：
```

---

# よくある誤り

## 国家最大Pathを一体のMageへ足す

国家全体にF3とE3があっても、F3E3の一体が存在するとは限りません。

## Boosterを装備できる前提で考える

Hand、Head、Misc、Body、Bootsの競合があります。

## CommunionをRitualへ使う

Communion / Sabbathは戦闘中の仕組みです。

## Candidate summonを保証扱いする

候補集合に含まれることと、一回で得ることは別です。

## HeroをResearch計画の前提にする

Heroは来た後に戦略を拡張するOptionです。

## Empowermentを最初に選ぶ

Booster、Pretender、Start Site、固定召喚、一般Site Mageで代替できないか先に確認します。

---

## 関連ページ

- [Magic Path Boosting](boosting.md)
- [Communion・Sabbath](communions.md)
- [拡張Magic Access](extended-magic-access.md)
- [Magic Item Boosterデータ](../data/items/boosters.md)
- [Spell summon Unit](../data/units/spell-summons.md)
- [Wish・Unique・Terrain特殊召喚](../data/units/special-summons.md)
