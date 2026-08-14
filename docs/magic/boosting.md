---
title: Magic Path Boosting
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# Magic Path Boosting

Magic Path Boostingとは、MageのPathを一時的または永続的に上げ、通常では届かないSpell・Item・Ritualへ到達することです。

Dominionsの魔法は、Mageの素のPathだけで評価してはいけません。

> **素Path → Item Booster → 戦闘Boost → Communion / Sabbath → Gem boost**

という階段を作ります。

---

# Boostの種類

## 1. Magic Item

装備中、対応Pathを上げるItemです。

例：

- Earth Boots
- Thistle Mace
- Skull Staff
- Winged Helmet
- Water Bracelet
- Crystal Coin
- Glamour Booster類
- Robe / Staff系の複合Booster

Item名・Construction Level・要求PathはPatchで変わる可能性があるため、ゲーム内またはMod Inspectorで確認します。

### 利点

- 戦略画面でもPathが上がる
- RitualとForgeに使える
- 戦闘開始時から有効
- 次のBoosterを作る連鎖を開く

### 欠点

- Slotを使う
- GemとForge turnを消費する
- Carrier死亡で失う
- 元々持たないPathを通常は新規取得できない

---

## 2. Combat Path Boost Spell

戦闘中だけPathを上げる自己Buffです。

代表的な考え方：

- Fire：Phoenix Power系
- Air：Storm下のStorm Power系
- Water：水中Power系やCrosspath
- Earth：Summon Earthpower
- Astral：Power of the Spheres等
- Death：Dark Knowledge系ではなく、Item・Communion依存が多い
- Nature：Item・Communion・一部自己強化
- Glamour：対応する夢・幻術系Boost
- Blood：Hell Power、Sabbath等

### 利点

- 安価なMageを一段上のBattle Mageへ変える
- Reinvigoration等の副効果を持つ場合がある
- Army-wide Spellへ届く

### 欠点

- Script slotとCasting timeを使う
- 接敵前に間に合わない場合がある
- 条件SpellやGemを要求する場合がある
- 戦略画面のRitual / Forgeには使えない

---

## 3. Gem Boost

戦闘中、対応Gemを一個追加で使い、Spell使用可能Pathを一時的に1上げる方法です。

### 重要な制約

- 不足を埋められるのは通常1レベル
- 一度に使えるGem数は現在Pathを超えられない
- Spell必須Gem costも同じ上限へ含まれる
- Mageが元々そのPathを持っている必要がある

Gem Boostは「何レベルでも買える」仕組みではありません。

---

## 4. Communion / Sabbath

Communion MasterはSlave数に応じてPathが上がります。

これにより、

- S1を大量に持つ国家
- Matrixで参加する非Astral Mage
- Blood Sabbath

が高級Spellへ到達できます。

詳細は [Communion](communions.md) を参照してください。

---

## 5. Empowerment

Gemを大量に消費し、Mageへ新しいPathまたはPath levelを永続的に与えます。

### 利点

- 国家に存在しないPathを獲得できる
- Booster chainの入口を作れる
- Unique casterをGlobal / Ritual担当へ変えられる

### 欠点

- 非常に高価
- Mage死亡で投資を失う
- 既存の独立Mage・召喚Mage・Pretenderで代替できる場合が多い

Empowermentは最後の手段ではなく、**その投資で何の連鎖が開くか**を計算できる場合に使います。

---

# Booster Chain

Booster Chainとは、一つ目のBoosterでPathを上げ、さらに上位Booster・召喚・Ritualへ到達する連鎖です。

例の考え方：

```text
E2 Mage
→ Earth BoosterでE3
→ E3要求のForge / Ritual
→ 召喚Mageまたは上位Booster
→ E4～5の戦略魔法
```

```text
N1 independent Mage
→ Nature BoosterでN2
→ Poison Ward / Site Search / 召喚
→ 新しいNature caster
```

Chainを組むときは、最終到達Pathだけでなく、各段階の、

- Construction level
- 必要Gem
- Forge turn
- Item slot
- Casterの生存
- Unique Item / Artifact制限

を確認します。

---

# 戦略Pathと戦闘Path

同じPath levelでも意味が違います。

## 戦略画面

- Ritual
- Summon
- Site Search
- Forge
- Global
- Empowerment

にはItemと素Pathが重要です。Combat boostは使えません。

## 戦闘中

- Self boost
- Communion
- Gem boost
- Battlefield condition

を使えます。

「戦闘ではE4へ届くが、E4 ItemはForgeできない」という違いを意識します。

---

# Boosterを誰へ渡すか

## Rare Path Mage

国家のMagic diversityを開くため最優先です。前線で消耗させず、Forge / Ritual担当にすることがあります。

## Army-wide Spell担当

一人のCasterがArmy全体を変えるなら、Booster投資を回収しやすくなります。

## Thug

Self Buffへ届くために使います。ただしItem slotを防具・Resistanceと競合します。

## Researcher

Boosterを持たせても研究値は通常直接増えません。Forge・Ritual用途がなければ倉庫へ戻します。

---

# Path別の考え方

## Fire

高PathでBattlefield damage、Elemental、Globalへ伸びます。Fire in a Jar等の一時Gem Itemも戦闘到達を助けます。

## Air

A2～3から機動・Shock、A4以上でArmy-wide defenseやStorm戦術が開きます。Storm条件とSummon Storm Powerの順序が重要です。

## Water

W2～3のQuickness・Cold・Elementalが実用的です。Water Boosterは複数Slotを重ねやすい場合があります。

## Earth

E2から戦闘BoostでE3へ届く構造が非常に強力です。Item Boosterと合わせてE4 Army spellへ進みます。

## Astral

ItemだけでなくCommunionが中心です。S1の数がPath深度へ変換されます。

## Death

Skull Staff等から高級召喚へ進み、召喚したDeath Mageが次のChainを開きます。

## Nature

低Path independent MageをBoosterで実用域へ引き上げやすく、Poison対策・Regeneration・召喚へつながります。

## Glamour

GlamourはDom6で追加されたため、Dom5以前のAir illusion情報をそのまま使えません。現行ItemとSpellを確認します。

## Blood

Blood Booster、Sabbath、Hell Power等で非常に高いPathへ伸びますが、Slave供給とFatigue管理が必要です。

---

# Booster計画テンプレート

```text
目的：何をCast / Forge / Summonするか
最終要求Path：
現在のCaster：
必要なItem：
Item要求Path：
必要Construction：
必要Gem：
必要Forge turn：
前提となるSite / Summon：
Casterを失った場合の代替：
```

これを書けないBoosterは、まだ作る必要がない可能性があります。

---

# よくある失敗

## Boosterを全Mageへ配る

高級Spell担当だけで十分な場合があります。普通のE2 Spellを使うMageへEarth Bootsを全配布する必要はありません。

## Item slotを忘れる

Boosterを装備すると、Resistance、Reinvigoration、Shield等を持てなくなる場合があります。

## Battle boostをRitualへ使えると思う

戦闘中だけのPath上昇はForge・Ritualへ使えません。

## Gem boostで2レベル以上埋めようとする

通常は不可能です。

## Empowermentを先に行う

Independent Mage、Pretender、召喚Mage、Item chainで代替できないか確認します。

## Rare casterを前線へ出す

国家のPath access全体を失う可能性があります。

---

## 関連ページ

- [魔法の基本](index.md)
- [Research](research.md)
- [GemとBlood Slave](gems.md)
- [Communion](communions.md)
- [Magic Item](../items/index.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [illwiki: Magic Boosting and Access](https://illwiki.com/dom5/dom6/magic-access)
