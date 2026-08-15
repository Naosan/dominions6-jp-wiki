---
title: 拡張Magic Accessの読み方
status: expanding
verified_version: "6.35"
last_verified: "2026-08-15"
---

# 拡張Magic Accessの読み方

国家のMagic Pathは、通常RecruitできるMageだけでは決まりません。

Dominionsでは、

- 国家Start SiteのCommander
- Hero
- Pretender
- Spellで召喚するMage
- 一般Magic Siteから得るMage
- EventやMercenary
- Booster、Empowerment、Communion

によって、ゲーム中のMagic Accessが変化します。

しかし、これらをすべて一つの表へ足して、

> この国家はF5A4W4E5S6D6N5G4B5H4を使える

と書くだけでは、攻略としてほとんど役に立ちません。

理由は、**確度、Timing、再現性、量産性がまったく違う**からです。

このWikiではMagic AccessをLayerに分けます。

---

## 関連ページ

- [国家別拡張Magic Access](../data/extended-magic-access/index.md)
- [Path gain比較](../data/extended-magic-access/path-gains.md)
- [Nation Start / Future Site mage](../data/extended-magic-access/start-sites.md)
- [Hero mage](../data/extended-magic-access/heroes.md)
- [一段召喚Mage](../data/extended-magic-access/summon-mages.md)
- [Pretender base magic](../data/extended-magic-access/pretenders.md)
- [通常Recruit Mage access](../data/mage-access.md)
- [国家別Site Search能力](../data/site-search/index.md)
- [Magic Path Boosting](boosting.md)
- [Communion・Sabbath](communions.md)

---

# Access Layer

## Layer 1：通常Recruit

もっとも再現性が高い基礎です。

- Any-fort Mage
- Capital-only Mage
- Fort不要・地形Recruit
- Coastal Recruit

を含みます。

通常Recruitの強みは、Pathの高さだけでなく、**繰り返し雇えること**です。

たとえば、首都限定S4が一人いる国家と、各FortでS1を毎Turn雇える国家では、同じAstral国家でも運用が異なります。

```text
高Path一人
→ Booster、Global、強いRitual

低Path量産
→ Communion、Magic Duel、Site Search、Army support
```

拡張Accessを評価するときも、通常Recruitをbaselineにします。

---

## Layer 2：国家Start Site

国家属性によって首都などへ配置されるMagic Siteが、CommanderをRecruit可能にする場合があります。

これは一般のRandom Siteより再現性が高く、国家固有Rosterの一部に近いAccessです。

ただし、次を確認します。

- Start SiteかFuture Siteか
- Commander recruit fieldかSite summonか
- Fort、Laboratory、Templeが必要か
- Capital Recruitment Pointを使うか
- 通常Recruit rosterと同じUnitか
- 国家限定Recruitか

Start SiteのMageが通常Recruit mappingにも含まれている場合、Pathを二重加算してはいけません。

### Future Site

Future Siteは、データ上で国家に紐付いていても、ゲーム開始直後から利用できるとは限りません。

- Turn
- Event
- Dominion
- 国家内部処理
- 建物
- 時代・Scenario

などが関係する可能性があります。

そのためStart SiteとFuture Siteを別列にしています。

---

## Layer 3：Hero

Heroは国家固有Magic diversityを大きく広げることがあります。

一方で、Heroは通常Recruit Mageとは違います。

- 出現Turnを選べない
- 必要な戦争までに来る保証がない
- Unique Heroは一体だけ
- Late Heroはさらに遅い
- 死亡時の代替が難しい

したがってHero Accessは、

> 来れば戦略を拡張できるOption

として扱い、

> First Warまでに必ず使える国家Path

とは扱いません。

### Heroが来たら最初に考えること

1. 新PathのSite Search
2. Booster作成
3. Mage summonへの接続
4. National SpellのCaster
5. Global Enchantment
6. Battle Mageとして失うRisk

Heroが唯一のD3である場合、そのHeroを前線へ出すより、最初にDeath Site SearchやBoosterを行う方が国家全体の上限を上げることがあります。

---

## Layer 4：Pretender

Pretenderは国家のMagic Accessをゲーム開始前に設計するLayerです。

Pretender欄の基礎Pathは、Chassisが最初から持つPathです。

最終Pathは、

- Chassis
- Path cost
- Design Point
- Scales
- Bless
- Dominion Strength
- Awake / Dormant / Imprisoned

との交換で決まります。

したがって、Pretender base magicの表は、

> この国家はこのPathを必ず持つ

という表ではありません。

> どのChassisから設計を始められるか

を見る表です。

### PretenderでAccessを補う判断

Pretenderに不足Pathを買う価値が高い例：

- 重要Booster chainの入口になる
- 国家固有Spellの唯一Casterになる
- Early Site SearchでGem economyを起動する
- Summon Mageへ接続する
- Bless設計と同じPathを使える

価値が低い例：

- 一回だけ使う低価値Ritualのために高いPath costを払う
- 通常RecruitのRandomで十分補える
- PretenderがImprisonedで必要Timingに間に合わない
- Pathを買った結果、ScalesやBlessが崩れる

---

## Layer 5：一段召喚Mage

召喚Mageは、GemをMagic diversityへ変換する主要な方法です。

このWikiの「一段召喚Mage」は、次の条件で計算します。

```text
通常Recruit Mage
        ↓
要求Pathを満たす
        ↓
Research可能なRitualをCast
        ↓
Mage Unitを得る
```

含まないもの：

- Boosterを装備したCaster
- Communion / Sabbath
- Hero Caster
- Pretender Caster
- Start Site Mage Caster
- 召喚Mageが別のMageを召喚する再帰Chain

この制限によって、

> 国家が素のRosterから直接どこへ伸びるか

を確認できます。

### Fixed target

Spellが固定Unit IDを直接召喚する場合です。

結果Unitの種類は明確ですが、実際には、

- Research
- Gem
- Laboratory
- Uniqueが既に存在するか
- CasterのPath
- National / Realm restriction

が必要です。

### Candidate pool

Unique summon、Terrain summon、Tartarian等、候補集合から結果が選ばれる処理です。

候補にMageが含まれていても、

> そのMageを一回で必ず得る

とは限りません。

そのためFixed summonとは別列にします。

### Random-assisted caster

通常Recruit MageのRandom結果次第でSpell要求を満たせる場合です。

これは、

> その国家なら理論上Castできる

という意味であって、

> 必要なTurnまでにCasterが必ず出る

という意味ではありません。

Random個体の出現率、Recruit数、Capital bottleneckを別に考えます。

---

# Path gainの読み方

拡張Access表では、通常Recruitの保証最大を超える場合だけ`gain`として表示します。

例：

```text
Native：E2
Start Site Mage：E3S1
```

表示：

```text
E3（native E2） S1（new）
```

これは、

- Earthの深度がE2からE3へ増える
- Astralが新しく開く

という意味です。

ただし、E3S1 Mageが毎Fortで量産できるとは限りません。

Layerの供給源も確認してください。

---

# 「国家が使えるPath」の四段階

攻略では、Path Accessを次の四段階へ分けると整理しやすくなります。

## Native

通常Recruitだけで再現可能。

国家戦略の基礎にできます。

## Planned

Start Site、Pretender設計、保証Casterによる固定召喚など、事前計画でかなり再現できます。

ただしResearchやGemのTimingが必要です。

## Conditional

Random Mage、Hero、Future Site、Candidate summonなど、条件が揃えば使えます。

主計画ではなく副計画にします。

## Opportunistic

一般Magic Site、Event、Mercenary、Wish結果などです。

発見後に戦略を更新します。

---

# BoosterとCommunionは別Layer

今回の自動生成表は、BoosterとCommunionを含みません。

これは弱点ではなく、意図的な分離です。

例えば、

```text
Native E2
Boots of Earth
Summon Earthpower
```

で戦闘中E4へ届く場合でも、

- Construction Research
- Earth Gem
- Forge turn
- Item slot
- 戦闘中のScript

が必要です。

同様にCommunionは、Mageの人数とFatigue管理をPathへ変換します。

したがって、

```text
Chassis access
→ Booster access
→ Communion access
→ Spell access
```

を段階的に確認します。

---

# 実戦での確認手順

## 1．通常Recruitを見る

- Any-fort固定Path
- Capital-only Path
- Random pool
- Commander Point
- MageのResearch価値

## 2．Start Siteを見る

通常Recruitに含まれないCommanderがいるか確認します。

## 3．HeroはOptionとして記録する

Heroが来なければ成立しない第一戦争計画は避けます。

## 4．Pretenderの役割を決める

Pretenderを、

- Bless
- Scales
- Expander
- Magic diversity
- Global caster

のどれに使うか決めます。

## 5．一段召喚を確認する

Native guaranteed casterでCastできるMage summonを優先します。

## 6．Booster chainを接続する

召喚Mageを得た後、次のBoosterやSummonへ進めるか確認します。

## 7．Timingへ落とす

```text
Research完成Turn：
必要Gem：
Caster Recruit Turn：
召喚Turn：
Booster作成Turn：
実戦投入Turn：
```

まで書きます。

---

# 典型的な失敗

## 全Layerの最大Pathを足す

Hero、Pretender、召喚候補の最大を足しても、実際のCasterは存在しないことがあります。

## Heroを国家の保証Pathとして扱う

必要なHeroが出ないまま戦争が始まる可能性があります。

## Candidate poolを固定召喚として扱う

候補表は結果保証ではありません。

## National Spellだけを見てCasterを確認しない

国家固有Spellでも、その国家の通常Mageが要求Pathを満たさない場合があります。

Pretender、Hero、Empowerment、召喚Mageを前提としている可能性があります。

## 召喚ChainのTurnを無視する

```text
Research
→ Booster
→ 第一召喚
→ 第二Booster
→ 第二召喚
```

は数Turnかかります。

「最終的に届く」と「次の戦争に間に合う」は別です。

---

# 国家攻略へ書く形式

国家ページでは、次の形式が使いやすいです。

```text
Native magic
- Any-fort：E2
- Capital：F1E3S1
- Random：20% FAWE

Planned extension
- Start Site：S1 Mage
- Pretender：N3を設計候補
- Fixed summon：E3からD2 Mageへ接続

Conditional
- Hero：A3G2
- Random caster：N2個体で召喚Spell
- Candidate pool：高級召喚にS Mage候補

First warまで
- Native E spellのみ
- Hero・高級召喚は前提にしない
```

この形式なら、国家の理論上限と実戦Timingを同時に説明できます。

---

# 最後の原則

Magic Accessは、Path記号の集合ではありません。

> **誰が、いつ、どの確度で、何Turnと何Gemを使い、そのPathへ到達するか**

まで含めてAccessです。

通常Recruit、Start Site、Hero、Pretender、召喚を分離して読むと、

- 序盤に本当に使える魔法
- 中盤に計画できる拡張
- 来れば強い偶発Option
- 終盤だけの理論上限

を混同せずに済みます。
