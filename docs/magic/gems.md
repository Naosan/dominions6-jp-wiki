---
title: GemとBlood Slave
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# GemとBlood Slave

Magic Gemは「魔法のMana」ではなく、**保存・輸送・奪取・投資が可能な戦略資源**です。

主な用途は次の四つです。

1. Ritual
2. Summon
3. Magic ItemのForge
4. Combat Magic

Blood Magicでは通常Gemの代わりにBlood Slaveを使います。

---

## 八種類のGem

通常Gemは次の八Pathに対応します。

- Fire
- Air
- Water
- Earth
- Astral Pearl
- Death
- Nature
- Glamour

BloodにはBlood Gemがなく、Blood Slaveを使います。

---

# Gem income

## Magic Site

Gem incomeの中心はMagic Siteです。

Siteには、

- 毎TurnのGem income
- Mage / Unit recruitment
- Ritual discount
- ScaleやProvinceへの効果
- 特殊なCommander order

などがあります。

Site Searchは単に隠し要素を探す作業ではなく、**将来の研究・召喚・Item・戦争を支える経済投資**です。

## Labへの接続

Siteから産出されたGemを国庫へ集めるには、そのProvinceがFriendly Provinceの連続によってLaboratoryへ接続されている必要があります。

Raidで経路を切られると、Site自体を失っていなくても回収に影響が出ます。

## Capital income

多くの国家は首都のSiteから固定Gem incomeを持ちます。国家攻略では、Capital incomeが最初の研究ルートとItem選択を制約します。

---

# Gemの保管と輸送

Gemは、

- Nation treasury
- Commander inventory

に存在します。

CommanderへGemを渡せるのは、基本的にLaboratoryまたは他Commanderとの受け渡しが可能な状況です。

### 攻略上の注意

- 前線ArmyがLabから離れる前に必要Gemを積む
- Rare Gemを無防備なScoutへ大量に持たせない
- Retreat・死亡・暗殺で失う量を考える
- 複数Armyへ分配し、一つの敗戦で全在庫を失わない
- Blood Slaveは戦場上のUnitとして殺される可能性がある

---

# Combat Gemの三つの役割

## 1. 必須Gem costを支払う

強力なBattle Spellの一部は、CastするためにGemを要求します。

SpellのFatigueが非常に高い場合にも、必要Gem costが設定されます。

## 2. Pathを一時的に1上げる

Casterが要求Pathへ1だけ届かない場合、対応Gemを一個追加で使い、一時的にPathを1上げられる場合があります。

例：

```text
E2 Mage
+ Earth Gemによる一時Boost
= E3 SpellをCast
```

ただし一度のSpellで使用できるGem数には、Casterの現在Pathに基づく上限があります。必須Gem costが大きいSpellでは、追加Boost分を払えない場合があります。

## 3. Fatigueを減らす

要求Pathより高いPathとして扱い、Spell Fatigueを減らすために追加Gemを使うことがあります。

この用途では複数Gemが使われる場合がありますが、Spellを使用可能にするPath boost自体は基本的に1段階までです。

---

# Combat Gemの制約

覚えるべき原則は次です。

## 自分のInventory

通常GemはCaster自身が持っていなければ使えません。

## Path上限

一回のSpellで使用できる対応Gem数は、Casterの現在Pathを超えられません。

## 一段階Boost

GemでSpell要求Pathを満たす場合、通常は不足1レベルまでです。

## Blood Slave

Blood Slaveは例外的に、Blood Mageの周辺にいるFriendly Slaveを利用できます。したがって配置、Bodyguard、AoE、Attack Rearが重要です。

---

# Gem burn

相手にGemを浪費させるため、小規模戦・Scout・Summon・Remote attackを送り込む戦術をGem burnと呼ぶことがあります。

相手が、

- Battlefield Enchantment
- Elemental summon
- 高級AoE
- Defensive buff

を毎回Scriptしているなら、安価な攻撃でも高価なGemを消費させられます。

### 対策

- 小規模戦用のGemなしScriptを用意する
- Scoutで敵規模を確認する
- Gemを必要数だけ持たせる
- 主力Spellを後半Scriptに置くか検討する
- AI Cast Spellsへ移った後の消費を確認する

---

# RitualでのGem

RitualはLaboratoryで実行し、Nation treasuryからGemを使います。

主な投資先：

- Site Search
- Summon
- Remote attack
- Scrying
- Global Enchantment
- Terrain / Scale manipulation
- Teleport / Gateway
- Dispel

Ritualは戦場に直接出ないため安全に見えますが、Casterの一Turnを消費し、研究・Forge・移動を止めます。

---

# Summonへ使う

召喚はGemを次の資産へ変換します。

- 一般兵
- Chaff
- Elite troop
- Raider
- Thug chassis
- Mage
- Commander
- Magic diversity

評価するときは「一体のStats」だけでなく、

- Gem cost
- 一回の召喚数
- Caster turn
- Leadership
- Upkeep
- Magic Being / Undead / Demon
- 対応するCounter
- 召喚Mageから次に何へ届くか

を見ます。

Mage召喚は、戦闘力より**新しいPathとBooster chain**に価値があることがあります。

---

# Forgeへ使う

Magic ItemはGemを永続資産へ変えます。

## 回収しやすいItem

- Path Booster
- Research Booster
- Forge discount
- Resistance Item
- Remote / Ritual補助

## 失いやすいItem

- 前線Thug装備
- Raider装備
- Assassin装備
- Gemを大量に持つBattle Mage

Itemは繰り返し使えますが、Carrierが死ぬと敵に奪われる可能性があります。

---

# Alchemy

LaboratoryではGemをAstral Pearlへ、Astral Pearlを他Gemへ変換できます。

Alchemyは不足Pathの緊急補填に使えますが、通常は交換効率で損をします。

### 使う場面

- 今Turnに勝敗を決めるSpellが必要
- Globalの先着争い
- Booster chain完成
- Throne claimやDispel
- Game終了前で在庫価値がない

### 避ける場面

- 目的のない常用
- Site Search前に全在庫を変換
- Astral Pearlの重要用途を忘れる

---

# Gem budget

Gemは「貯める」か「使う」かの二択ではありません。用途別に予算を分けます。

例：

```text
40%：目前の戦争
25%：Booster / Forge基盤
20%：Summon / Magic diversity
10%：緊急Ritual
 5%：予備
```

割合は国家と時期で変わります。

## 戦争前チェック

- 主力Army一戦あたり何Gem使うか
- 三連戦できる在庫があるか
- Labから離れた後に補給できるか
- 敵のGem burnへ耐えられるか
- Remote attack / Domeへ残すか
- Globalを維持・再Castする余力があるか

---

# Blood Slave

Blood Slaveは通常Gemと違い、Blood HuntでPopulationから得ます。

## Blood Huntの交換

Blood経済は、

- Population
- Income
- Unrest
- HunterのTurn
- Patrol要員
- Slave輸送

をBlood Slaveへ変換します。

## 戦場上の弱点

Blood SlaveはUnitとして戦場へ現れます。

- AoE
- Arrow
- Flying / Attack Rear
- Fear
- Slaveの配置ミス

で先に殺されると、MageがSpellを使えません。

## Sabbath

Blood Slave経済はSabbathによって低Path Mageを高級Casterへ変換できます。Communionと同様にSlave側のFatigue・死亡を管理します。

---

# よくある失敗

## Gemを貯め続けて敗北

GemはScoreではありません。領土・Fort・Mage・Throneを得るために使います。

## 小戦闘で全消費

Scriptと携行数を管理します。

## Boosterを作りすぎる

Boosterは「使うCasterと到達先」があって初めて価値があります。

## Rare GemをAlchemyで失う

次のPath BoosterやGlobalに必要でないか確認します。

## Blood Slaveを無防備に置く

CasterだけでなくSlaveの生存が必要です。

---

# Gemを使う判断式

次の問いへ答えます。

> このGemを使うことで、何を得るか？

良い答え：

- Enemy Armyを壊滅させる
- Fortを奪う
- Throneを取る
- Booster chainを開く
- 新Path Mageを得る
- Researchを加速する
- 敵のGlobalを止める

弱い答え：

- Gemが余っている
- Spellが強そう
- Item欄を埋めたい

---

## 関連ページ

- [魔法の基本](index.md)
- [Research](research.md)
- [Path Boosting](boosting.md)
- [Communion](communions.md)
- [Magic Item](../items/index.md)
- [命令とBattle Script](../basics/orders.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [illwiki: Gems](https://illwiki.com/dom5/dom6/gems)
- [illwiki: Combat Magic](https://illwiki.com/dom5/dom6/combat-magic)
