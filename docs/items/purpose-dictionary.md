---
title: 用途別Magic Item辞典
status: expanding
verified_version: "6.35"
last_verified: "2026-08-19"
---

# 用途別Magic Item辞典

このページは、Item名を覚えている人のための一覧ではなく、

> **困っていること → 必要な能力 → 候補Item → Slot / Path / Gem / Carrierを比較する**

ための逆引きです。

正確なItem recordは[Magic Itemデータ索引](../data/items/index.md)と[Dom6 Mod Inspector](https://larzm42.github.io/dom6inspector/)を使います。このページでは「何を検索するか」「候補をどう落とすか」「敵はどうCounterするか」を扱います。

今回追加した自動生成索引はBaseIの明示fieldから候補集合を作ります。同じItemが複数ページへ重複するのは正常です。例えばFlyingとShock Resistanceを両方持つItemなら、MobilityとDefenseの両方から見つかる方が実戦では便利です。

---

# まず使う逆引き

## Construction別

- [Construction 1 Item一覧](../data/items/by-construction/c1.md)
- [Construction 3 Item一覧](../data/items/by-construction/c3.md)
- [Construction 5 Item一覧](../data/items/by-construction/c5.md)
- [Construction 7 Item一覧](../data/items/by-construction/c7.md)
- [Construction 9 Item一覧](../data/items/by-construction/c9.md)

これらは**そのBreakpointで解禁されるItem**を確認するページです。

「C5まで研究したからC1～5を全部眺める」のではなく、まず目的別ページで必要能力を決め、次にConstruction別ページで研究到達時点の候補を確認します。

## 機能・目的別

- [攻撃・Weapon支援](../data/items/by-purpose/offense.md)
- [防御・Resistance](../data/items/by-purpose/defense.md)
- [Sustain・疲労・回復](../data/items/by-purpose/sustain.md)
- [移動・Flying・水中](../data/items/by-purpose/mobility.md)
- [Mage・Research・Forge支援](../data/items/by-purpose/mage-support.md)
- [指揮・偵察・Siege・特殊作戦](../data/items/by-purpose/operations.md)
- [視認・Darkness・偵察](../data/items/by-purpose/vision.md)

既存の専用索引も併用します。

- [Magic Path Booster一覧](../data/items/boosters.md)
- [Research Item一覧](../data/items/research.md)
- [Resistance / MR Item一覧](../data/items/resistance.md)
- [Utility Item一覧](../data/items/utility.md)
- [Unforgeable / Artifact](../data/items/unforgeable.md)

---

# 症状から探す

| 症状・目的 | まず見るもの | 次に確認するもの | Counter視点 |
|---|---|---|---|
| Ethereal相手へ通常攻撃が当たらない | Magic Weapon候補、Weapon data | WeaponのMagic属性・Attack・Damage | 敵はWeapon slotを使わせている |
| 高ProtectionへDamageが通らない | 攻撃Item、AP / AN Weapon data | Damage、AP / AN、Armor damage、命中 | DefenceやMR等の別防御へ移る可能性 |
| Chaffに囲まれて殴れない | AoE / multiple attack / Fire Shield系 | Weapon特殊効果、Fatigue、Friendly Fire | 敵は少数高価Commanderへ集中Counter可能 |
| Thunder Strike等で高価Commanderが死ぬ | Defense / Resistance | Shock Resistance、HP、Slot | Damage typeを変えると装備が腐る |
| Foul Vaporsで後から死ぬ | Poison Resistance | PR、Regen、Caster位置 | Disease対策とは別問題 |
| Soul Slay / Charmが怖い | MR / Antimagic | MR、Antimagic、Returning、Caster保護 | 高MRなら物理・Elementalへ切り替える |
| Heavy armor Mageがすぐ気絶する | Sustain | Reinvigoration、Encumbrance、Path boost | Itemだけでなく軽装・Spell選択も見る |
| Thugが長期戦で削り負ける | Sustain + Defense | Regen、Reinvig、HP、Resistance | Burst / Fatigue / Soul系は別対策 |
| Armyに追いつけない | Mobility | Map Move、Flying、Army側の最遅Unit | Commander一人だけ速くしてもArmyは速くならない |
| 地上Commanderを水中へ送りたい | Mobility | Water Breathing、Army全体の適性 | Itemを外すと帰れない状況に注意 |
| 新しい高Path Ritualへ届きたい | Mage support + Booster | Booster chain、Slot、Forge担当 | Booster carrierを狙えば国家accessを壊せる |
| Researchを加速したい | Research Item | Bonus、Construction、回収Turn、Forge turn | 開戦Timingを早めて回収前に圧力をかける |
| Siegeが間に合わない | Operations | Siege bonus、Army size、Fort、防衛救援Turn | 敵は救援到着まで耐えればよい |
| Supply不足 | Operations | Supply bonus、Province supply、Army size | RaiderでSupply routeを壊す方が安いこともある |
| Invisible / Glamour系を見たい | Vision | Spirit Sight / True Sight等の視認能力 | Ethereal対策とは別 |
| Assassinへ装備を渡したい | Operations + Offense/Defense | 小戦闘、Bodyguard、Fatigue、逃走 | 高価Itemを一対一戦へ晒すRisk |

症状からItemを探すときは、**一つのItemで全部解決しようとしない**ことが重要です。

例えば「Shockで死ぬ」ならShock Resistanceを探しますが、同時にSoul Slayも飛んでくるならMRも必要です。Misc slotが二つしかないなら、Itemだけで両方を解決できない可能性があります。その場合はArmy-wide Spell、Bodyguard、配置、Caster killへ分担します。

---

# Construction 1で何を探すか

C1は「安いから全部作る」段階ではありません。**最小の穴埋めが一個で成立するか**を見るBreakpointです。

現行6.35データではFire Sword、Ice Sword、Enchanted Swordなど低要求のWeaponがあり、安いMagic Weaponを必要とする場面の候補になります。

C1へ到達したら次を確認します。

1. Magic Weapon一個でRaiderの対象が増えるか
2. 小さなResistanceやMorale補助で重要Commanderが生き残るか
3. そのItemを作るためにRare Mageを一Turn止める価値があるか
4. C3まで待つとより効率のよい解決策が出ないか

C1は特に**Carrierの素能力が既に高い国**で価値が上がります。完成されたChassisの欠点が一つだけなら、安いItemで任務を成立させられます。

Counter側から見ると、C1 Itemへ過剰投資していない相手は交換効率がよいので、「Itemを壊す」よりCarrierの任務自体を読んで迎撃します。

---

# Construction 3で何を探すか

C3から「装備」だけでなく**国家経済と特殊任務**へItemが入り始めます。

6.35の代表的な確認例には、

- Owl Quill — Air系Research Item
- Ring of Water Breathing — 水中移動Utility
- Boots of Giant Strength — Strength補助
- Amulet of Missile Protection — 射撃防御候補
- Flying Ointment — Mobility系複合Path Item

などがあります。

ここで重要なのはItem名ではなく、C3到達時に次の三問をすることです。

```text
1. 10Turn以上使う経済Itemがあるか
2. 最初の戦争を変えるCounter Itemがあるか
3. Raider / Scout / Assassinの到達範囲を変えるUtilityがあるか
```

例えばOwl QuillのようなResearch Itemは、早く作るほど使用Turnが増えます。ただしC3へ寄るせいで最初のBattle Spellが遅れるなら、そのResearch bonusは戦争敗北を取り返しません。

水中・Flying・射撃防御などは一戦のDamage期待値より**新しい任務が可能になること**に価値があります。

---

# Construction 5で何を探すか

C5は多くの国家でItem戦略の中心です。

6.35ではEarth Boots、Winged Helmet、Amulet of Antimagic、Skull Mentor、Spider Amuletなど、Booster・Research・MR / Resistance・Utilityの重要候補が同じBreakpointへ集まります。

C5到達時は一覧を上から作るのではなく、次の優先順位で絞ります。

```text
A. 国家全体のMagic accessを開くもの
B. 次の戦争の負け筋を消すもの
C. 何度もProvinceを取るCommanderを成立させるもの
D. 長期Research / Forge economy
E. 便利だが今すぐ不要なUtility
```

この順番が重要なのは、C5では**GemよりForge turnが不足しやすい**からです。

Earth / Air / Death等の高Path Mageが一人しかいない場合、そのMageはBooster、Battlefield caster、Ritual、Site Search、Forgeを全部担当できません。「作れるItem数」ではなく「誰が何TurnForgeするか」を表にします。

Counter側はC5以降、敵Commanderの装備から研究方向を読みやすくなります。Boosterが見えたら高Path spell、MR Itemが見えたら自分のMR-negates攻撃を警戒している、と推測できます。ただしItem一個だけで敵Researchを断定しないでください。

---

# Construction 7で何を探すか

C7は「より強いC5」ではなく、**高額Itemを具体的な作戦へ結びつける段階**です。

6.35ではLightless Lantern、Water Bracelet、Boots of Quickness等が確認候補になります。

ここでは、

- 高級Booster chainを完成させる
- Research raceを加速する
- SC / ThugのLoadoutを一段上げる
- 大Armyを一戦で支えるUtilityを用意する
- 最終戦に近いCounterへ即応する

といった用途が競合します。

Research Itemはまだ強力でも、ゲーム終了までの残りTurnが短いほど回収価値が下がります。一方、Throne戦を一回勝つためのCounter Itemは一戦で回収できます。

C7 Itemを作る前に、必ず「このItemは何Turn装備されるか」ではなく、**何回の重要戦闘・Ritual・Forgeで価値を出すか**を考えます。

---

# Construction 9で何を探すか

C9はArtifact raceです。

ここでは通常Itemの比較より、

- 世界で一つのItemへ先着できるか
- 要求Pathへ誰が届くか
- Booster chainを完成済みか
- 必要Gemを今からReserveできるか
- Forge担当が前線から離れてもよいか
- 完成後に誰が持つか
- 敵に奪われた場合の被害

を見ます。

C9研究が完成してからArtifactを考えると遅いことがあります。C7付近から「C9到達Turn」「Forge Mage」「Booster」「Gem reserve」を一つの計画として作ります。

CounterはArtifactそのものだけではありません。研究競争中に戦争を始める、Forge hubをRaidする、Gem incomeを奪う、CarrierをAssassinateする、といった**完成前後の経済を攻撃する**方法があります。

---

# Weaponを目的から選ぶ

WeaponはDamageだけで評価しません。

見る順番は、

```text
相手の防御
→ Magic / Mundane
→ Protection
→ Defence
→ Size / Length
→ Regeneration / HP
→ Resistance
→ 自分のAttack / Strength
→ Shieldを持てるか
```

です。

## Etherealへ当てたい

必要なのは原則としてMagic Weaponです。

ここでTrue Sight / Spirit Sightと混同しないでください。SightはInvisible等を認識する問題、Etherealはmundane attackが当たりにくい問題です。

[攻撃Item索引](../data/items/by-purpose/offense.md)からWeapon候補を出し、[Combat data](../data/combat/weapons/index.md)でWeapon propertyを確認します。

## 高Protectionへ通したい

候補は、

- 高Damage
- Armor Piercing
- Armor Negating
- Armor damage / destruction
- MR / Soul系などProtectionを使わない攻撃

です。

「最もDamageが高いWeapon」を選ぶのではなく、相手の防御層を飛ばすWeaponを探します。

## 高Defenceへ当てたい

DamageよりAttack bonusや攻撃回数が重要になることがあります。

高価なAN Weaponでも当たらなければ働きません。Carrier自身のAttack、Quickness、Harassment、味方の拘束やDebuffも合わせます。

## Chaffを処理したい

AoE、multiple attack、Fire Shield、Dancing Weapon等を候補にします。

ただしAoE Weaponは高HP単体CommanderへのDPSが弱い場合があります。PD Raid用とAnti-SC用を同じWeaponで済ませない方がよいことがあります。

## Life Drain / Sustainが欲しい

Weapon側のLife DrainやSoul Vortex系能力は、攻撃とSustainを同時に解決できる可能性があります。

ただし相手がUndead、Lifeless、Drain耐性等なら期待どおり働くとは限りません。特殊効果はInspectorとゲーム内Item詳細を確認します。

## 片手か両手か

Two-handed WeaponはWeapon単体の性能だけでなく、**Shield slotを失うCost**を含めて評価します。

相手がCrossbow / Archer / 多数の通常攻撃ならShield喪失が致命的になる場合があります。逆に素のNatural ProtectionやDefenceが高くShield依存が小さいChassisなら両手武器を活かしやすくなります。

---

# Armor・Shield・Helmetを目的から選ぶ

防具はProtection最大化ゲームではありません。

## 通常兵を受ける

Protection、Defence、Shield、Head Protectionを揃えます。

Body Armorだけ高くしてもHead Hitで倒れます。Shieldは多数の通常攻撃や射撃へ有効ですが、AN / MR / Poison等を別に見る必要があります。

## Mageを守る

重ArmorのProtectionだけを見ると失敗します。

確認するのは、

- Spellcasting Encumbrance
- Reinvigoration
- Elemental Resistance
- MR
- Air Shield / 射撃防御
- Retreat route

です。

Mageは「最後まで立っている」より、**必要SpellをCastし終えるまで生きる**装備を目指します。

## Elemental対策

[防御・Resistance索引](../data/items/by-purpose/defense.md)または[Resistance専用索引](../data/items/resistance.md)を使います。

Fire / Cold / Shock / Poison / Acidは別々です。万能Resistanceを探すより、ScoutとReplayから敵Damage typeを特定します。

## Poison対策

Poison ResistanceとRegenerationを分けて考えます。

PRはPoisonへの直接対策、Regenerationは受けたHP damageを回復するSustainです。Diseaseはさらに別mechanicなので「Poison Itemを付けたからDiseaseも安全」と考えません。

## MR攻撃対策

MR ItemやAntimagicはSoul Slay、Charm等への候補です。

しかし敵が高MRを見て物理・Elementalへ切り替えれば、そのMisc slotは別Counterを失っています。Item戦は**slotを使わせること自体がCounter**になります。

---

# Misc・Bootsを目的から選ぶ

MiscとBootsはItem設計で最も競合しやすいSlotです。

## Booster

Boosterは「Battle Mageを少し強くするItem」ではなく、Ritual / Forge / Summon / Globalへ届く国家accessです。

[Booster一覧](../data/items/boosters.md)から候補を出し、[Magic Access Route](../magic/magic-access-routes.md)と組み合わせます。

Boosterを前線Thugへ常用すると、Commander死亡時に戦闘力だけでなく国家のMagic accessを失います。

## Research

[Research Item一覧](../data/items/research.md)を使います。

Research bonusだけでなく、

```text
Gem
+ Forge turn
+ Construction寄り道
+ Carrier数
+ 残りTurn
```

を回収できるか見ます。

## Reinvigoration

Heavy armor Mage、Quickness Thug、長期戦SCではReinvigorationがDamage Itemより重要になることがあります。

[継戦能力索引](../data/items/by-purpose/sustain.md)から候補を出し、戦闘Replayで「死因がHPかFatigueか」を確認します。

## Regeneration

高HP Chassisほど絶対回復量が大きくなります。

ただしBurst、Fatigue、Soul / Control、即死系へは別防御が必要です。RegenだけでSC設計を完成させないでください。

## Mobility

[移動索引](../data/items/by-purpose/mobility.md)を使います。

Flying、Map movement、水中移動、Sailingは「戦闘Stats」ではなく、

- どのProvinceへ届くか
- 何Armyを運べるか
- Retreatできるか
- 迎撃できるか

を変えます。

一個のMobility Itemで一Turn早くThroneへ着くなら、高Damage Weapon以上の価値があります。

## Vision

[視認索引](../data/items/by-purpose/vision.md)を使います。

Darkvision、Spirit Sight、True Sight等は同じではありません。Darkness下のCombat penalty、Invisible / Glamour等の認識、Ethereal attack問題を分離します。

## Leadership / Supply / Siege / Patrol

[特殊作戦索引](../data/items/by-purpose/operations.md)を使います。

強いSummonを持っていてもLeadershipがなければArmy化できません。大軍を持っていてもSupplyで崩れれば戦闘前に弱ります。Siege bonusでFort攻略Turnが一つ短くなれば敵救援を間に合わせないことがあります。

これらはDamage計算へ直接出ないため、初心者ほど過小評価しやすいItem効果です。

---

# Dom6 Mod Inspectorでの確認手順

公開Inspectorでは`Item`を選び、Item名検索とproperty key検索を使えます。

まずItem名を検索し、次を確認します。

```text
type
constlevel
mainpath / mainlevel
secondarypath / secondarylevel
Item固有Cost modifier
Weapon / Armor参照
F A W E S D N G B H のBooster field
shockres / fireres / coldres / poisonres / acidres
mr
reinvigoration / regeneration
researchbonus
forge / fixforge
fly / waterbreathing / mapmovebonus
ldr-* / patrolbonus / siegebonus / supplybonus
truesight / spiritsight / darkvision
```

必要な効果が名前から分からない場合は、advancedなproperty key検索で候補を絞ります。

例として「Poison対策Item」という名前を覚えるより、`poisonres`を持つItemを検索する方がPatchや新Itemへ強い調べ方です。

同様に、

```text
Researchが欲しい → researchbonus
疲労対策 → reinvigoration
MR → mr / antimagic
Flying → fly / flyingmapmove
Booster → F/A/W/E/S/D/N/G/B/H
```

という形で**能力名からrecordを探す**習慣をつけます。

---

# Generated purpose indexの限界

今回の目的別索引は、BaseIの明示fieldだけを安全に分類します。

そのため、次は完全ではありません。

- Weapon参照先にだけ書かれているDamage type
- Itemが発動するSpellの複合効果
- hard-codedな特殊挙動
- 使用回数や特殊発動条件
- Carrier size / hand / mount等の装備制限の実戦評価
- Nation固有discountの最終Cost
- Unique / Arena / Event等の入手条件全体

つまり目的別索引は、

> **候補を漏らさず探しやすくする入口**

です。

候補が3～10個に絞れたら、InspectorのItem詳細、Weapon / Armor data、ゲーム内Forge画面へ進みます。

---

# Counter：敵のItemを逆に読む

敵CommanderのItemを見たら「強い装備だ」で終わらせず、そのItemが埋めている弱点を考えます。

```text
MR Item
→ Soul / Charmを警戒している
→ Physical / Elementalへ切替可能か

Shock Resistance
→ Lightningを警戒している
→ Fire / Cold / Poison / MRへ切替可能か

Reinvigoration
→ 長期戦・Heavy armor・Quicknessを疑う
→ Burst / Controlで長期戦をさせない

Magic Weapon
→ Ethereal等を警戒している
→ Weapon slotを使わせた価値を確認

Mobility Item
→ Raid / Intercept範囲が広がる
→ Map上の安全距離を一Province広く取る
```

Item Counterの基本は「さらに高級Itemを作る」ことではありません。

- Damage typeを変える
- MRとPhysicalの軸を切り替える
- Slot競合を起こさせる
- Carrierを狙う
- Forge Mageを止める
- Gem incomeを奪う
- Research回収前に戦争する

ことでItem投資そのものを不利にできます。

---

# Item選択テンプレート

```text
症状 / 任務：
敵の主防御：Prot / Def / MR / Resistance / Ethereal / Regen
必要能力：
目的別索引：
候補Item：
Construction：
要求Path：
基礎Gem：
ゲーム内実Cost：
Slot：
Carrierが元から持つ能力：
重複していないか：
Forge担当：
Forge担当を一Turn止めるCost：
使用予定戦闘 / Turn：
敵がCounterするなら何をするか：
失ってよいか：
```

この表で答えられないItemは、まだForgeする理由が固まっていません。

---

## 関連ページ

- [Magic Item総論](index.md)
- [Forge計画とConstruction Breakpoint](forge-planning.md)
- [Magic Path Booster](boosters.md)
- [Research Item](research-items.md)
- [Resistance・Utility Item](resistance-items.md)
- [Thug / Supercombatant装備](thug-equipment.md)
- [Weapon・Shield](../basics/weapons-and-shields.md)
- [Combat data](../data/combat/index.md)
- [Magic Access Route](../magic/magic-access-routes.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- Wiki固定Dom6 Inspector snapshot: `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc` / Dominions 6.35
