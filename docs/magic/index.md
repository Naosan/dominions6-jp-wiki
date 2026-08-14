---
title: 魔法の基本
status: expanding
verified_version: "6.35"
last_verified: "2026-08-14"
---

# 魔法の基本

Dominions 6の魔法は、次の要素を組み合わせて考えます。

> **Research × MageのMagic Path × Gem / Blood Slave × Script × 対象の防御**

研究しただけでは使えず、要求Pathを持つMageだけでも使えません。Gemが必要なSpell、戦場条件を要求するSpell、対象が存在しなければScriptから飛ばされるSpellもあります。

魔法を覚えるときはSpell名の暗記ではなく、

1. 何を勝利条件にするSpellか
2. 誰がCastできるか
3. いつResearchが完成するか
4. 一戦で何Gem使うか
5. 相手がどうCounterするか

を一つの組として覚えます。

---

# Magic Path

Dominions 6には九つのArcane Magic Pathがあります。

## Elemental Magic

- Fire
- Air
- Water
- Earth

## Sorcery

- Astral
- Death
- Nature
- Glamour

## 独立系統

- Blood

HolyはArcane Magicとは別枠で、主にPriest levelとDivine Spellに関係します。

詳細は [Magic Path総論](paths/index.md) を参照してください。

---

# Research School

通常の研究は七つのSchoolへ分かれます。

- Conjuration
- Alteration
- Evocation
- Construction
- Enchantment
- Thaumaturgy
- Blood Magic

## PathとSchoolは別物

FireだからEvocationだけ、EarthだからAlterationだけ、というわけではありません。

例えば一つのPathでも、

- Conjuration：召喚・Path boost
- Alteration：能力・身体・Protectionの変化
- Evocation：直接Damage
- Construction：Item・Booster
- Enchantment：Army buff・Battlefield effect
- Thaumaturgy：精神・魂・特殊操作

へ重要Spellが分散します。

したがって研究計画は、

> 「Fireを使うからEvocation」

ではなく、

> 「次の戦争でFire Elementalを投入する」
> 「弓兵をFire damage化する」
> 「Fire Resistance差を作ってBattlefield effectを使う」

のように、具体的な勝ち筋から決めます。

詳しくは [Researchと研究ルート](research.md) を参照してください。

---

# Battle SpellとRitual

## Battle Spell

戦闘中にCastします。

- Self buff
- Squad / Army buff
- 直接Damage
- Summon
- Control / Debuff
- Battlefield Enchantment

Battle Spellは、Researchだけでなく初期配置、Script順、Range、Precision、Fatigue、Gem携行数、Caster生存が重要です。

## Ritual

LaboratoryでCommander orderとして実行します。

- Site Search
- 召喚
- 遠隔攻撃
- Scrying
- Teleport / Gateway
- Global Enchantment
- Dispel
- Province / Scale操作

Ritualは戦場で詠唱しませんが、Mageの一TurnとGemを使います。Research、Forge、移動との機会費用を考えます。

---

# GemとBlood Slave

通常の八Pathには対応Gemがあります。BloodはGemではなくBlood Slaveを使います。

Gemの主用途は、

1. Ritual
2. Summon
3. Forge
4. Combat Magic

です。

Combatでは必須Costだけでなく、一時的なPath boostやFatigue軽減に使える場合があります。

詳しくは [GemとBlood Slave](gems.md) を参照してください。

---

# Magic Pathを上げる

Mageの素Pathが要求値に足りない場合でも、次で到達できることがあります。

- Magic Item
- 戦闘中の自己Boost
- Gemによる一時Boost
- Communion / Sabbath
- Empowerment
- 召喚Mage
- Pretender

この到達経路をBooster Chainとして設計します。

詳しくは [Magic Path Boosting](boosting.md) を参照してください。

---

# Fatigue

MageはSpellを無限にCastできません。

Spell Fatigueは主に、

- Spell固有のFatigue
- CasterのPathと要求Pathの差
- Armor Encumbrance
- Battlefield環境
- Communion
- Gem追加消費
- Reinvigoration

で変わります。

通常、要求Pathより高いMageほど同じSpellを低Fatigueで使えます。一方、重装MageはArmorのSpellcasting Encumbranceによって早く気絶する場合があります。

Fatigue 100以上では通常行動できず、さらに蓄積するとHPへ危険が及びます。

詳しくは [戦闘ルール：Fatigue](../basics/combat-rules.md#fatigue) を参照してください。

---

# 魔法が攻撃する防御層

「Magic damage」という一種類の攻撃があるわけではありません。

| 攻撃方法 | 主に見る防御 |
|---|---|
| 通常Fire / Cold等 | Protection、対応Resistance、Spell属性 |
| Shock系AN | Shock Resistance、HP |
| MR Negates | Magic Resistance、Penetration |
| Poison | Poison Resistance、HP、Regeneration |
| Fatigue damage | Resistance、Reinvigoration、Undead / Lifeless等の性質 |
| Armor Piercing物理 | Protectionの一部 |
| Armor Negating | Protectionを無視 |
| Mind effect | MR、Mindless等 |
| Holy / Banishment | Undead、Demon等の分類 |

敵のProtectionが高いからEvocationが必要、とは限りません。SpellがProtectionを参照するか、AP / ANか、MR判定かを確認します。

---

# Magic ResistanceとPenetration

Soul、Mind、Control系Spellの多くはMR判定を要求します。

Caster側はPath、Spell、Item、Scale等からPenetrationを得ます。対象側はMR、Antimagic、Bless、Item等で抵抗します。

攻略上は、

- 高Protection・低MR → Astral / Death / Glamour系のMR攻撃
- 高MR・低Protection → 通常Damage、Elemental、物理強化
- Mindless → Mind effect以外
- Antimagicを確認 → MR攻撃一本から分散

と判断します。

---

# Battlefield Enchantment

戦場全体へ作用するSpellです。

- Weather
- Darkness
- Heat / Cold / Fatigue
- Army-wide defense
- 継続Damage
- Summon / Illusion生成
- Battlefield terrainへの作用

などがあります。

一部はCasterが死亡すると解除されます。CasterをBodyguard、射撃対策、Rear attack対策で守ります。

敵のArmy-wide効果が一人のCasterに依存しているなら、そのMageを倒すことが最短のCounterです。

---

# Global Enchantment

世界全体または国家全体へ長期効果を与えるRitualです。

Globalを評価するときは、

- 発動Cost
- 毎Turnの利益
- Global slot
- Dispel耐性
- Caster Path
- Caster暗殺への耐性
- 他Playerへの外交的影響
- ゲーム終了までの残りTurn

を見ます。

「強いGlobal」でも、発動が遅ければ回収できません。先着・上書き・Dispelを含めた競争です。

---

# Spell AIとScript

Mage Scriptは勝利条件を発動する順番です。

基本形：

```text
1. Path boost / 自己防御
2. Army defense
3. Army offense
4. Control / Debuff
5. Damage / Summon
6. Cast Spells
```

一人に全役割を詰め込むと、主力Spellが間に合いません。複数Mageへ役割を分けます。

ScriptされたSpellが使われない場合は、

- Path
- Gem
- 一度に使えるGem上限
- Range
- Target
- Battlefield condition
- CasterのFatigue・移動・Interrupt

を確認します。

詳しくは [命令とBattle Script](../basics/orders.md) を参照してください。

---

# CommunionとSabbath

低Path Mageを多数接続し、MasterのPathを上げ、FatigueをSlaveへ分散します。

AstralのS1 Mageが多い国家や、Blood Mageを持つ国家の上限を大きく引き上げます。

ただし、

- Master数
- Slave数
- MasterとSlaveのPath差
- Crosspath Spell
- Heavy armor
- Slave防御
- Communion終了時のfeedback

を誤るとSlaveが死亡します。

詳しくは [Communion・Sabbath](communions.md) を参照してください。

---

# 魔法を学ぶ順番

初心者は次の順に読むと理解しやすくなります。

1. [Researchと研究ルート](research.md)
2. [Magic Path総論](paths/index.md)
3. 自国が主に使うPathページ
4. [GemとBlood Slave](gems.md)
5. [Magic Path Boosting](boosting.md)
6. [命令とBattle Script](../basics/orders.md)
7. Astral / Blood国家なら [Communion](communions.md)
8. [Magic Item](../items/index.md)

---

# 実戦での質問

Spellを採用する前に、次へ答えます。

- このSpellで何に勝つのか
- 誰がCastするのか
- 研究完成Turnはいつか
- 一戦何Gem使うか
- Rangeと初期配置は合っているか
- Friendly Fireはあるか
- Casterを何Round守る必要があるか
- 相手のResistance / MR / Unit typeは何か
- Counterされた場合の第二案は何か

これへ答えられれば、研究とArmyが一つの計画になります。

---

## 関連ページ

- [Researchと研究ルート](research.md)
- [Magic Path総論](paths/index.md)
- [GemとBlood Slave](gems.md)
- [Magic Path Boosting](boosting.md)
- [Communion・Sabbath](communions.md)
- [Magic Item](../items/index.md)

## 主な参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6公式変更点](https://www.illwinter.com/dom6/changes.html)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [illwiki: Magic](https://illwiki.com/dom5/dom6/magic)
