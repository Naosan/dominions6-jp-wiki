---
title: "Winged Helmet"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 195
---

# Winged Helmet

**Air MageのAir Pathを+1し、Battle spell・Ritual・ForgeのAir閾値を越えるConstruction 5のHelmet Booster。Flyingを与えるItemではない。**

Winged Helmetは名前に「Winged」とありますが、[Winged Shoes](winged-shoes.md)のHelmet版ではありません。

攻略上は、

```text
Winged Helmet
→ Air +1

Winged Shoes
→ Flying
```

という全く別のItemです。

- [Dominions 6.35固定データ — Item 195](../../data/items/by-id/195.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Winged Shoes](winged-shoes.md)

---

# まず何ができるか

6.35固定データでは、Winged Helmetは、

- Construction 5
- Forge要求 **A4**
- Helmet Slot
- **Air +1**
- Armor record 227

を持ちます。

Armor record 227はMagic Helmetで、Defence 0、Encumbrance 0、頭部Protection 22です。

Item descriptionは、装備者のAir magicの技能を高めるHelmetだと説明しています。

固定データと説明文のどちらにも、装備者へFlyingを与えるとは書かれていません。

したがって、

```text
Winged Helmetを装備
→ 遠いProvinceへ飛行移動できる
```

とは考えません。

---

# Air +1は「新しい役割」で評価する

Winged Helmetの価値は、Air表示が1増えたこと自体ではありません。

装備前後で、

- 新しく選べるBattle spell
- 新しく実行できるRitual
- 新しくForgeできるItem
- 同じSpellを高PathでCastした場合のFatigue
- Storm中のPath・役割
- 次のBoosterやSummonへ届く経路

がどう変わるかを確認します。

```text
A4 Mage
→ Winged Helmet
→ A5として目的Spell / Ritual / Forgeへ到達
```

のように、**あと1で重要な閾値へ届くMage**へ持たせるのが基本です。

A+1しても現在のResearchでは仕事が増えないなら、Helmetの価値はまだ発生していません。

---

# 最初の一個にはA4 Forgerが必要

Winged HelmetのForge要求はA4です。

そのため、低Air国家が、

```text
A1 Mage
→ Winged Helmet
→ 高Airへ到達
```

と直接進める最初のBoosterではありません。

最初の一個を作るには、

- native A4 Mage
- Random込みでA4へ届くMage
- Summon Mage
- Hero
- Pretender
- 別Boosterを装備したForger
- Empowerment済みMage

などが必要です。

Booster chainは、完成形だけでなく、

> **最初のWinged Helmetを誰がForgeするか**

から設計します。

A4 accessがPretenderだけなら、PretenderのForge turn、位置、Awake / Dormant / Imprisoned timingまで影響します。

---

# Winged Shoesとの最大の違い

[Winged Shoes](winged-shoes.md)はCommanderへFlyingを与え、戦略Map上の到達経路とRaid routeを変えます。

Winged HelmetはAir +1を与え、到着後に使えるMagicを変えます。

```text
Winged Shoes
→ 戦場へ行けるか

Winged Helmet
→ 戦場で目的Air Spellを使えるか
```

です。

Air Mageへ両方欲しくなることはありますが、Slotが違うため同時装備は可能です。

ただし、

- Helmet Slot
- Boots Slot
- 二つ分のGem
- 二つ分のForge turn
- Booster Carrier喪失Risk

を払います。

一人のMageへ移動とPathを集中させるより、Flying transport、前線Lab、別Casterで役割を分けた方が安い場合があります。

---

# Storm Powerとは別物

Storm Powerは、Storm中の戦闘に限定されるPath上昇です。

Winged Helmetは装備中のItem Boosterなので、

- Battle spell
- Ritual
- Forge

で使えます。

```text
Winged Helmet
→ Strategic Map上でもPathを上げる

Storm Power
→ Storm中のBattleだけ
```

という違いです。

RitualやForgeへStorm Powerを持ち込むことはできません。

一方、戦闘ではWinged HelmetとStorm Powerが同時に関係するCarrierもいます。

その場合は、

- 戦闘開始前のAir
- Helmet装備後のAir
- Storm成立後のAir
- 目的Spellの必要Path
- Gem投入

を段階ごとに確認します。

---

# Stormを成立させるCasterへ持たせる

Air戦術では、Stormそのものを成立させるCasterと、Storm後に高Air Spellを使うCasterが別の場合があります。

Winged Helmetを誰へ渡すかは、

- Storm担当がPath不足なのか
- Storm後のArmy-wide Spell担当がPath不足なのか
- Damage Spell担当がPath不足なのか
- Ritual・Forge担当が必要なのか

で変わります。

Helmet一つを最も高価なMageへ惰性で渡すのではなく、

> **HelmetがないとどのScript行が成立しないか**

を見ます。

一人が倒れるとStorm plan全体が崩れるなら、Casterの分散や予備Helmetも検討します。

---

# Battle Mageへ持たせる場合

前線で使う場合は、

- A+1で目的Spellが解禁される
- 目的Spell用Gemを持っている
- Storm時のRange・Precision・FatigueをTest済み
- Helmet Slotを使っても防御が足りる
- Lightning・Missile・Assassinationへの対策がある
- Armyと同じProvinceへ間に合う
- Retreat routeがある

ことを確認します。

Air Mageは強力なArmy-wide SpellやBattlefield effectの鍵になりやすいため、Winged Helmet Carrierは優先Targetになり得ます。

Protectionだけでなく、MR、Shock Resistance、配置、Guardも含めて保護します。

---

# 後方Ritual・Forge用では共有しやすい

Winged HelmetをLab内で使うなら、前線でのCarrier Riskは避けられます。

典型的には、

- RitualするTurnだけ装備
- 高Air ItemをForgeするTurnだけ装備
- 使用後にLabへ戻す
- 別のAir Mageへ渡す

という運用です。

```text
Winged Helmet一個
→ 複数のAir Mageが必要Turnだけ共有
```

できます。

高いA4 Forge起点を払ったItemなので、使わないTurnまで一人へ固定しない方がよい場合があります。

ただしFort間の移送にはTurnが掛かるため、次に使うMageと場所を先に決めます。

---

# Helmetとしての防御

Armor record 227は、Defence 0、Encumbrance 0、頭部Protection 22です。

つまり、Winged HelmetはPath Boosterでありながら頭部防具としても機能します。

ただし、

- 全身Protectionを22にするItemではない
- Helmetは頭部だけを守る
- MR-based effectをProtectionで防げない
- Shock Resistanceは別に必要
- Air +1がCarrierの生存を直接保証しない

ことに注意します。

「高Protection Helmetだから前線に出してよい」ではなく、Casterの任務と敵のDamage軸を見ます。

---

# Helmet Slotの機会費用

Winged Helmetを装備すると、

- Flame Helmet
- Starshine Skullcap
- Resistance Helmet
- 視覚・Stealth系Helmet
- Protection重視Helmet

と競合します。

Crosspath Mageでは、Air +1を取ることでAstral・Fire等のBoosterを外すことがあります。

```text
Air +1で得る新しいSpell
vs
別Helmetで得る別Path・MR・Resistance・Utility
```

を比較します。

一人に複数Pathの役割を集めるより、Mageを分ける方が安定する場合があります。

---

# Carrierを選ぶ

優先したいCarrierは、

- 素でAir magicを持つ
- +1で具体的なSpell・Ritual・Forgeが解禁される
- 目的Researchへ到達済み
- 必要Gemを受け取れる
- Helmet Slotを他の必須Boosterへ使わない
- 前線ならStorm planと配置が決まっている
- 倒された時の代替Casterがいる

Mageです。

すでにHelmetなしで目的を達成できるA5 Mageへ常設するより、A4→A5で役割が生えるMageへ渡し、担当Caster数を増やす方が強いことがあります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- 最初の一個を作れるA4 Forgerがいる
- A+1で具体的なBattle spell・Ritual・Forgeが増える
- 目的Researchへ到達済み
- Air Gemを確保できる
- 前線用か後方共有用か決めている
- Helmet Slot競合を解決済み
- Stormを含む場合は戦闘手順をTest済み
- Carrier喪失時の代替がある

特に、

> **Winged Helmetを装備することで、次の戦闘のScriptがどこからどこへ変わるか**

を説明できる時に優先します。

---

# Forgeしない・後回しにする条件

- A4 Forgerがいない
- A+1しても現在のResearchで仕事が増えない
- 高Air Mageがすでに必要数いる
- Air GemをBattle magicやSummonへ回したい
- Helmet Slotへ別Boosterが必須
- 目的がFlying付与である
- 前線へ到着できず、Bootsや別移動手段が先
- Booster一個への依存が高すぎる
- 一戦だけなら別Caster・Gem boostで代替できる

名前だけを見てFlying目的でForgeしないことが最重要です。

---

# Counter：Air閾値とStorm planを読む

敵のWinged Helmetを見たら、Carrierの素AirとHelmet込みAirを確認します。

見るべきなのは、

- どのSpell閾値を越えたか
- Stormを誰が起動するか
- Storm後に誰が何をCastするか
- Gem carrierは誰か
- Helmetを失うとどのScriptが止まるか

です。

Counterは、

- Shock Resistanceを用意する
- Storm planの起点Casterを狙う
- Missile・Assassination・RaidでCarrierを落とす
- Gem carrierを分断する
- Air SpellのRange外・配置外へ重要Unitを置く
- Helmet依存Casterを複数戦線へ分散させる
- Stormを利用する自軍構成へ切り替える
- CarrierではなくFort・Lab・Armyを攻め、Helmet運用を乱す

ように、**Air +1によって成立した役割**を崩します。

---

# よくある失敗

## Winged Shoesと同じ効果だと思う

Winged HelmetはAir +1です。Flying付与ではありません。

## 最初の一個を誰が作るか決めていない

Forge要求A4なので、低Air国家では入口で止まります。

## Storm PowerをRitual・Forgeへ使えると思う

Storm Powerは戦闘中限定です。

## Helmetなしでも仕事をできるMageへ固定する

あと1で役割が増える別Mageへ渡した方がよい場合があります。

## Air +1だけでStorm planが完成したと思う

Gem、Script、Storm起点、Range、Precision、Carrier保護が別に必要です。

## HelmetのProtectionだけでCarrierを守れると思う

MR-based effect、Shock、Assassination、Fatigueは別軸です。

## Research前に作る

使うSpellが未研究なら、GemとForge turnが寝ます。

---

# Test game checklist

```text
[ ] C5・A4でWinged HelmetがForge可能か確認
[ ] Item 195・Armor record 227であることを確認
[ ] 装備前後でAir +1を確認
[ ] Airを持たないCommanderでPath表示がどうなるか確認
[ ] Flyingが付与されないことを確認
[ ] 頭部Protection 22・Defence 0・Encumbrance 0を確認
[ ] Helmetなし／ありで目的Spellの選択可否を比較
[ ] Storm前／Storm後のAir Pathを確認
[ ] Storm PowerとItem Boosterの適用範囲を分けて確認
[ ] Winged Shoesとの同時装備と役割差を確認
[ ] 後方Ritual・Forgeで別Mageへ受け渡せるか確認
[ ] Carrier死亡時に止まるScriptを確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 195](../../data/items/by-id/195.md)
- [Magic Path Booster](../boosters.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [Winged Shoes](winged-shoes.md)
- [Igor Könhelm's Tome](igor-konhelms-tome.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / armors / protections_by_armor / Item description
- BaseIで確認した主要field：C5、A4、Air +1、Armor 227
- Armor record 227：Defence 0、Encumbrance 0、頭部Protection 22
- Flying付与は固定データ・Item descriptionのどちらにも確認できない
- Storm中の最終PathとSpell挙動はゲーム内Unit画面・Battle Replayを優先
