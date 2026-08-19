---
title: 任務別Magic Item Loadout
status: expanding
verified_version: "6.35"
last_verified: "2026-08-20"
---

# 任務別Magic Item Loadout

Magic Itemの装備セットは、固定Buildを暗記するためのものではありません。

同じCommanderでも、

- 弱いProvince DefenceをRaidする
- Enemy Thugだけを狩る
- Main ArmyのMageを一戦守る
- 海へ潜入する
- Storm下で戦う
- Artifactを安全に運ぶ

では必要なItemが変わります。

このページでは、

> **任務 → 最小成立条件 → 足りない機能 → 候補Item → 追加投資条件 → Counter**

の順にLoadoutを組みます。

正確なItemの要求Path、Construction、Gem Cost、Weapon / Armor profile、発動Spell、副作用は次を使います。

- [用途別Magic Item辞典](purpose-dictionary.md)
- [Magic Itemデータ索引](../data/items/index.md)
- [Magic Item Weapon profile](../data/items/weapon-profiles.md)
- [Magic Item Armor profile](../data/items/armor-profiles.md)
- [Item Spell・自動効果](../data/items/active-effects.md)
- [Summon・Retinue Item](../data/items/summoning-effects.md)
- [Item副作用・装備制限](../data/items/risk-restrictions.md)
- [Artifact一覧](../data/items/artifacts.md)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)

このページのItem名は**候補例**です。最終的な値はゲーム内Forge画面とInspectorで確認してください。

---

# Loadoutより先に「任務契約」を書く

装備を作る前に、Commanderへ何をさせるかを一行で書きます。

悪い例：

```text
強いThugを作る
```

良い例：

```text
BorderのPD 6～10を二Province連続でRaidし、
敵Main Armyが戻る前にFriendly Provinceへ退却する
```

```text
Enemyの高Protection Thugを一戦だけ迎撃し、
自軍Main Armyへ合流する
```

```text
Thunder Strikeが飛ぶ決戦で、
重要なCommunion MasterをScript終了まで生存させる
```

任務契約には最低でも次を入れます。

1. **Target** — 何と戦うか
2. **勝利条件** — Province取得、Commander kill、Script完走など
3. **Exposure** — 何戦・何Turn危険に晒すか
4. **Support** — Army、Bodyguard、Mage、Scoutの支援があるか
5. **Retreat / Exit** — 負けたときどこへ帰るか
6. **Loss ceiling** — 失ってよいGemとCarrier価値
7. **Upgrade trigger** — 何が見えたら追加装備するか

任務が書けない段階では、ItemをForgeしません。

---

# Loadoutの五層

任務ごとの装備は、五層に分けて考えると過剰投資を防げます。

## 1. Access / Mobility

そもそも戦場へ届けるか。

- Map Move
- Flying
- Stealth
- Water Breathing
- Gift of Water Breathing
- Sailing等

です。

戦闘性能が十分でも、目標Provinceへ届かなければ任務は失敗です。

## 2. Offense

Targetを倒せるか。

- Magic Weapon
- Attack
- Damage
- AP / AN
- AoE
- Multiple attack
- Armor破壊
- MR / Soul系
- Anti-undead / Anti-demon

を見ます。

## 3. Defence

Targetの主攻撃を一回以上受けられるか。

- Protection
- Shield
- Defence
- HP
- Fire / Cold / Shock / Poison Resistance
- MR / Antimagic
- Air Shield
- Luck等

です。

## 4. Sustain

勝つまで動き続けられるか。

- Reinvigoration
- Regeneration
- Life Drain
- Fatigue管理
- Affliction Risk

を見ます。

## 5. Exit / Reuse

勝った後も再利用できるか。

- Friendly退却先
- Strategic movement
- 次の目標までの距離
- Item回収
- F8で所在管理

まで含めてLoadoutです。

---

# 三段階の投資

固定Gem予算ではなく、任務に対して三段階で投資します。

## Minimal — 最小成立

欠けている機能を一つだけ足します。

```text
素で硬いCommander
+ 必要なMagic Weaponだけ
```

のような形です。

Minimalで勝てるなら、それ以上のGemは別戦線へ使います。

## Reinforced — 負け筋を一つ消す

ScoutやReplayで確認したCounterだけを追加します。

例：

```text
Minimal Raider
+ Enemy Crossbow対策
```

```text
Anti-Thug
+ Enemy Fire Shield対策
```

です。

## Decisive — 一戦の価値が大きい

Throne、Capital、重要Artifact Carrier、決戦等では複数のCounterへ投資します。

ただし、

```text
高価 = Decisive
```

ではありません。

重要戦闘で勝率を実際に上げるItemだけを追加します。

---

# Chassis監査

Itemを一個も作る前にCommander本体を確認します。

| 項目 | 質問 |
|---|---|
| HP | Burstを一回受けられるか |
| Protection | Armorを買う必要が本当にあるか |
| Defence | 多数攻撃に囲まれたとき残るか |
| Attack | 高価なWeaponを当てられるか |
| Strength | Weapon Damageを活かせるか |
| MR | Control / Soul attackの標的にならないか |
| Encumbrance | 長期戦やSelf Buffで気絶しないか |
| Morale | Awe / Fear / Routへ耐えられるか |
| Size | 包囲、Trample、装備制限に影響しないか |
| Natural abilities | Regen、Reinvig、Flying、Stealth等を重複購入していないか |
| Slot | 必要なBoosterと防御Itemが競合しないか |
| Strategic movement | 勝った後に次へ届くか |

Chassisが任務の七割を既に満たしているCommanderほど、安いItemで成立します。

---

# 任務1：PD Raider

PD Raiderの目的は、敵主力を倒すことではありません。

- Incomeを奪う
- Fort建設を止める
- Temple / Labを壊す
- Retreat routeを切る
- Enemy Armyを後方へ戻す

ことです。

## 最小成立条件

```text
□ 想定PDを倒すDamageがある
□ 必要ならMagic Weaponがある
□ 小Damage多数で崩れない
□ Fatigueで止まらない
□ Rout / Retreat先がある
□ 次Turnに逃げるか次を取れる
```

## 最初のItem

まずWeaponを買うとは限りません。

Chassisが素で十分なDamageを持つなら、

- Missile protection
- Reinvigoration
- Mobility
- MR

の方が任務成功率を上げる場合があります。

低ConstructionのWeaponが必要なら、C1のEnchanted Sword等を候補にし、[Weapon profile](../data/items/weapon-profiles.md)でMagic weapon、Damage、Attack、Secondaryを確認します。

## 射撃PDが痛い

6.35では**Amulet of Missile Protection**はConstruction 3 / A2の候補です。

ただし、Item一個を見て「射撃無効」とは判断しません。

- Air Shield値
- Enemy射撃数
- Crossbow等の一撃Damage
- Mage攻撃
- Chassis HP

を合わせます。

## Upgrade trigger

次のどれかが見えたらReinforcedへ上げます。

- Crossbow / Arbalestが多い
- Priest / Sacred PDが入る
- Mage付きPD
- Cavalry Charge
- Poison / Elemental Weapon
- Enemyが迎撃Thugを置き始めた

最後のケースでは、PD Raiderのまま装備を積み増すより**Anti-Thug部隊を別に用意する**方が安いことがあります。

## Counter

敵Raiderに対しては、同額Itemで殴り返す必要はありません。

- PDを一段だけ上げる
- Scoutで進路を読む
- Cheap Mageを置く
- Retreat routeを切る
- Fast reinforcementを送る

など、任務そのものを失敗させます。

---

# 任務2：Strategic Raider / 後方破壊

戦闘能力より**到達範囲**が主役のRaiderです。

Targetは、

- Lab
- Temple
- 未完成Fort
- 低PD Income Province
- Gem Site Province
- Retreat route

です。

## Mobilityを先に買う

戦闘装備を三つ積んでも、一Provinceしか届かなければ後方破壊になりません。

6.35の候補例として、

- **Flying Ointment** — C3 / A2N1
- **Winged Shoes** — C5 / A2

があります。

これらを使う場合も、Commander本人だけが速くなっているのか、同行Unitまで同じ移動をできるのかを分けます。

[ Flying・Storm・Air機動戦 ](../systems/flying-storm.md)のStrategic Flyingと合わせて確認してください。

## Minimal

```text
Mobility
+ PDを倒せる素戦闘力
```

で成立するなら、ArmorやMiscを追加しません。

## Reinforced

- Missile protection
- 主Elemental Resistance
- Magic Weapon
- Reinvigoration

のうち、実際に見えたCounterだけを追加します。

## Abort条件

- 目標の隣接Provinceに敵Fast Armyがいる
- Friendly retreat先がない
- 同行Bodyguardが移動能力を壊す
- Enemy LabにBattle Mageが集まった
- Raiderを失うと国家唯一のBoosterまで失う

この場合は任務を中止します。

---

# 任務3：Anti-Thug

Anti-Thugは「自分もThugになる」ことではありません。

Enemy Thugの防御層を一枚だけ破ればよい場合があります。

## 最初に敵を分解する

```text
Physical defence
- Protection
- Defence
- Shield
- Ethereal / Mistform等

Sustain
- Regeneration
- Reinvigoration
- Life Drain

Magic defence
- Elemental Resistance
- MR
- Antimagic

Control
- Awe
- Fear
- Fire Shield
- Summons
```

## Counter選択

| Enemyの強み | Item側で探す方向 |
|---|---|
| 高Protection | AP / AN、高Damage、Armor破壊、Protectionを使わない攻撃 |
| 高Defence | Attack、多段、拘束支援 |
| Ethereal | Magic Weapon / Magic Damage |
| 高Regeneration | Burst、継続高Damage、Fatigue / Control |
| Fire Shield | Fire Resistance、Range、別Damage source |
| 高MR | Physical / Elementalへ戻す |
| 低MR | MR attack / Control候補 |
| Awe / Fear | Morale、Berserk等の別対策 |
| Chaff summon | AoE、多段、Army支援 |

同じ防御をMirrorして殴り合うのではなく、相手が買っていない防御へ回ります。

## Minimal

```text
専用Weapon
+ Targetの主DamageへのResistance
```

だけで足りる場合があります。

## Supportを買う

Itemを三個追加する前に、

- Cheap Chaff
- Crossbow
- Priest
- Battle Mage
- Bodyguard

を一緒に使う方が安いか比較します。

Anti-Thugは**一人で勝つ必要がない**任務です。

---

# 任務4：Anti-SC team

Supercombatantへ一人の高価Commanderをぶつけると、SC側の得意な交換になります。

Anti-SCでは、役割を分散します。

```text
Commander A: 命中・Armor破壊
Commander B: Finish用高Damage / AP / AN
Mage: Fatigue / MR / Control
Chaff: 足止め
Priest: Sacred / Undead / Demon対策
```

Itemはチーム全体の一部です。

## Loadout原則

1. 一つのCarrierへ全部のGemを集中しない
2. Enemy SCが既に持つResistanceへDamage typeを合わせない
3. Regenを止めることより、回復量を上回る勝ち筋を作る
4. High MRならMR attackへさらに投資しない
5. SCを倒した後に装備を回収・再利用できる形にする

## Counter側

SCを運用する側は、敵がAnti-SC Itemを見せたら役割を変えます。

- Main Armyと合流
- 別戦線へ移動
- Chaffを増やす
- Resistanceを入れ替える
- Mage supportを付ける

SCの価値は「絶対に死なない」ことではなく、EnemyへCounter投資を強制することです。

---

# 任務5：Assassin / 小戦闘

Assassinは通常Army戦と同じLoadoutにしません。

小規模戦では、

- 最初の数Round
- Bodyguard
- Summon
- Fatigue
- Poison
- Fear / Awe
- MR
- 装備したWeaponがTargetへ本当に通るか

の比重が上がります。

特殊戦闘の正確なTiming・Retreat・対象選択は[Stealth・Glamour・特殊作戦](../systems/stealth-glamour.md)とゲーム内表示を優先してください。

## Minimal

```text
Targetを倒せるOffense
+ Targetの一番危険な反撃へのDefense
```

です。

通常Army用の重いSustain装備を全部持ち込む必要はありません。

## Mageを狙う

Battle Mageを狙うなら、

- Script開始前に圧力をかけられるか
- Bodyguardを処理できるか
- Elemental / MR attackを受けるか

を見ます。

## Thugを狙う

Enemy ThugならAnti-Thugと同じく、まず防御層を一枚抜きます。

## 過剰投資を避ける

Assassinは失敗時に高価ItemとCarrierを同時に失うRiskがあります。

国家唯一のBooster、Artifact、Rare Mageを一対一任務へ流用しないのが基本です。

---

# 任務6：Battlefield Caster保護

Battlefield Casterの勝利条件はEnemyを殴り倒すことではありません。

> **必要なScriptを撃ち切るまで生きる**

ことです。

## 脅威を分ける

- Archer / Crossbow
- Flying / Attack Rear
- Shock / Fire / Cold AoE
- MR attack
- Assassin
- Fatigue
- Friendly Storm / Darkness等

## Missile対策

6.35では**Amulet of Missile Protection**がC3 / A2の候補です。

ただし、Caster一人のMisc slotを使う価値があるか、

- Army-wide Arrow defence
- Bodyguard
- 配置
- Screen

と比較します。

## MR対策

6.35では**Amulet of Antimagic**がC5 / S1の候補です。

Enemyの主勝ち筋がMR Negates系なら価値があります。

一方、敵がPhysical / Elemental中心ならMR Itemは空振りになります。

## Armor

MageへArmorを渡す場合は、Protectionだけでなく、

- Encumbrance
- Spellcasting Fatigue
- Map Move
- Defence

を確認します。

CasterがScript Round 4で気絶するなら、生存用Armorが逆に任務失敗を作っています。

## Exit

決戦後にResearch / Ritualへ戻すMageなら、高価な戦闘ItemをF8で回収し、次戦線へ再配備します。

---

# 任務7：Communion Master / Slave支援

CommunionはItemだけで安全になるsystemではありません。

正確なFatigue transfer、Path、Master / Slave数は[Communion](../magic/communions.md)を優先してください。

Itemで扱うのは、

- Masterを射撃・Assassinから守る
- 必要Pathへ届く
- Slave / Masterの役割を明示する
- 戦闘後にMatrix系Itemを回収する

部分です。

6.35では**Sky Metal Matrix**と**Slave Matrix**がC5 / E1S1のItem候補として存在します。

これらを「Communionは人数不足でもItemで解決できる」とは扱いません。

## Master protection

重要Masterは、

- Missile
- MR attack
- Attack Rear
- Fatigue

のどれでScriptが止まるかを見ます。

## Slave protection

Slaveへ高価な防御Itemを大量配布する前に、Communion設計そのものを見直します。

```text
Itemを増やす
```

より、

```text
Master数
Slave数
Spell順
Path差
```

を直す方が大きい場合があります。

---

# 任務8：Booster / Ritual / Forge Carrier

国家唯一のMagic accessを持つCommanderは、戦闘力ではなく**技術基盤**です。

## 任務

- Booster chainを繋ぐ
- High Path Ritualを撃つ
- ArtifactをForgeする
- Globalを維持する
- Rare Itemを量産する

## Loadout原則

Battlefieldへ出さないなら、戦闘装備を積む必要はありません。

必要なのは、

- Path Booster
- Forge discount
- 必要ならStrategic mobility
- 安全なLab
- Item在庫管理

です。

## Earth BootsのようなBooster

6.35では**Earth Boots**はC5 / E2のBooster候補です。

重要なのはItem単体ではなく、

```text
E2 Mage
→ Earth Boots
→ 次のForge / Ritual
```

のようなaccess chainです。

## Risk

Enemyから見ると、Booster carrierはArmyより価値あるTargetになる場合があります。

- Assassination
- Raid
- Lab Province奪取
- Magic Phase攻撃

へ備えます。

F8で国家唯一のBoosterが誰に付いているか定期確認します。

---

# 任務9：Artifact Carrier

Artifact Carrierは「一番強いCommander」ではなく、**そのArtifactの価値を最も安全に出せるCommander**を選びます。

[Artifact・Unique Item攻略](artifacts.md)で、YearningとArtifact raceを含めて確認してください。

## 判断項目

```text
□ Artifactの主価値は戦闘かStrategicか
□ Carrierを前線へ出す必要があるか
□ Slot競合はないか
□ Assassin / Soul / MR counterへ耐えるか
□ Retreat先があるか
□ Carrier死亡で国家accessまで失わないか
□ 別Commanderへ渡した方が価値が高くないか
```

## Combat Artifact

Combat用でも、全部の防御を一人へ積むとは限りません。

ArtifactがOffenseを完成させているなら、残りSlotはDefence / Sustainへ使います。

## Strategic Artifact

Strategic能力、Forge、Summon、Research等が主価値なら、前線へ持ち出さない方がよい場合があります。

## Counter

Enemy Artifact Carrierへは、ArtifactのStatsだけでなく、

- Carrier本体
- Retreat route
- Bodyguard
- Support Mage
- Artifactを外した後の国家access

まで狙います。

---

# 任務10：Underwater侵入

Underwater任務は「Commanderが水中へ入れる」だけでは成立しません。

[海・Underwater・Amphibious攻略](../systems/underwater.md)のChecklistと合わせます。

## 一人だけ潜る

6.35では**Ring of Water Breathing**がC3 / W1の候補です。

Scout、Mage、単独Commanderを水中へ送るような任務では、個人用Water Breathingが作戦を開く場合があります。

## Squadを連れて潜る

個人用ItemだけではArmy全体を運べない場合があります。

6.35では**Manual of Water Breathing**がC5 / N3W1で、BaseI上`giftofwater`を持つ候補です。

実際に何Size / 何Unitを運べるかはゲーム内Commander表示と移動Arrowで確認します。

## 水中戦闘

移動できても、

- Weapon
- Missile
- Fire系効果
- Mount
- Poor Amphibian penalty
- Darkvision

は別問題です。

Itemで水中へ入れたことと、水中で勝てることを同一視しません。

## Exit

海へ入ったCommanderがItemを外すと帰れなくなる場合があります。

Treasuryへ戻す前に、

```text
現在Province
次の移動
退却先
Itemを外した後の能力
```

を確認します。

---

# 任務11：Storm環境

Stormは一人のCommanderではなくBattlefield全体へ影響します。

[ Flying・Storm・Air機動戦 ](../systems/flying-storm.md)を先に確認してください。

## Staff of Storms

6.35の固定データでは**Staff of Storms**はC7 / A5で、Start battle側に`Storm`、Auto combat側に`Lightning Bolt`が明示されています。

したがって、このItemは単なるWeaponではありません。

## 自軍への影響

Forge前に、

- 自軍Flying
- Archer
- Air Mage
- Storm Power
- Storm Immunity
- Enemy Air access

を確認します。

Enemy Flyingを止めるつもりで、自軍主力Flyingまで止めるなら失敗です。

## Carrier

Staff本体を持つCommanderの生存だけでなく、Battle開始時に必要な条件を作れるかを見ます。

Start battle effectはCarrierを後から倒しても既に戦場条件が成立している場合があるため、Counter側は戦闘前から構成を変えます。

---

# 任務12：Stealth / 特殊作戦Carrier

Stealth Itemは、単独のStealth値より**作戦全体の見えにくさ**を作るために使います。

[Stealth・Glamour・特殊作戦](../systems/stealth-glamour.md)と合わせます。

## 任務例

- Scout
- Spy
- Assassin
- Hidden Raider
- Lab / Temple脅威
- Retreat route切断

## Item判断

```text
Stealthを足す
→ Targetへ潜入できる
→ その後何をするか
```

まで書きます。

潜入だけ成功して、攻撃力も情報価値もないならItem投資は回収できません。

## Counter

EnemyがStealth Itemを使う場合、

- Patrol
- PD
- Scout network
- chokepointではなく価値Province防衛

で任務を潰します。

True Sight / Spirit Sight等の**戦闘中の視認**と、Strategic Stealth detectionを同一視しません。

---

# 任務13：Siege / Fort assault支援

Siege用ItemはBattle Damageを増やさなくてもTurnを短縮します。

価値は、

```text
Fortを一Turn早く落とす
→ 敵救援Armyより先にBreached
→ Capital / Throneを取る
```

という時間差です。

## 判断

- Siege bonus
- Carrierの安全性
- Fort strength
- Army size
- 敵救援までのTurn
- Forge turn

を比較します。

一Turn短縮できないSiege Itemなら、そのGemをBattle Itemへ使う方がよい場合があります。

## Counter

敵は、

- Relief Army
- Fort defence
- RaiderでSiege Armyの補給切断
- Siege bonus Carrierの暗殺

で時間を稼ぎます。

---

# 任務14：Vision / Darkness対策

視認問題とEthereal問題を混ぜません。

目的は、

- Invisible / Glamour系を認識する
- Darkness環境で戦う
- Scout / Perceptionを補う

ことです。

[視認・Darkness・偵察Item](../data/items/by-purpose/vision.md)から候補を出し、ゲーム内説明で対象能力を確認します。

```text
True Sight / Spirit Sight
≠
Magic Weapon
```

です。

Etherealへ通常攻撃を当てたいならWeapon propertyを見ます。

---

# 任務15：Research / Economy Carrier

Research Itemは戦闘Loadoutではありません。

Researcherの任務は、

```text
できるだけ長く安全にResearchする
```

ことです。

## Owl Quill

6.35では**Owl Quill**はC3 / A1でResearch bonus 6の候補です。

価値は「+6が強い」ではなく、

```text
ForgeしたTurn
→ 使用開始Turn
→ 戦争開始
→ ゲーム終了
```

まで何Turn回収するかで決まります。

## 前線へ持って行かない

Battle MageへResearch Itemを付けたまま前線へ送ると、戦闘中はResearch bonusを使っていません。

F8で回収し、後方Researcherへ付け替えます。

---

# 任務ごとのSlot競合

良いItem同士でも同じSlotなら同時に使えません。

## Boots

典型的な競合：

- Path Booster
- Flying / Mobility
- Reinvigoration
- Quickness
- Strength

です。

例えば6.35では、

- Earth Boots — C5 / E2
- Winged Shoes — C5 / A2
- Boots of Quickness — C7 / W2

がすべてBoot slotを競合します。

```text
一番強いBoots
```

ではなく、

```text
この任務でBoot slotに何をさせるか
```

を決めます。

## Misc

MR、Resistance、Regeneration、Research、Mobility等が競合します。

Misc slotが少ないCommanderは、Army-wide SpellやBodyguardへ役割を移します。

## Weapon / Shield

両手Weaponを使うとShieldを失います。

高Damageを得ても、Enemy Archer / Chaffへ弱くなるなら任務に合いません。

---

# Upgradeは「負けた理由」から一個ずつ

Test battleに負けたら、Itemを全部上位化しません。

Replayを見て敗因を一つ書きます。

```text
Round 4でFatigue 100
→ Reinvig / Enc / Scriptを見直す
```

```text
Crossbow Head hitで死亡
→ Missile / Head protection / 配置を見直す
```

```text
Enemy Etherealへ攻撃が通らない
→ Magic Weapon確認
```

```text
Soul Slayで死亡
→ MR / Antimagic / Target pressure
```

次のTestでは、その敗因だけを修正します。

これを繰り返すと、国家・Chassis・敵に合ったLoadoutになります。

---

# LoadoutをTest Gameで検証する

## PD Raider

最低でも、

```text
PD 1
PD 6
PD 11
PD 21
```

を複数の国家PDへ当てます。

見るもの：

- HP残量
- Fatigue
- Rout
- Affliction
- 勝利Round
- 次戦へ出せる状態か

## Anti-Thug

Enemy Thug側の防御を一つずつ変えます。

```text
Protectionだけ
→ Regen追加
→ MR追加
→ Resistance追加
```

どの追加で勝敗が反転するかを見ます。

## Caster protection

Casterを、

- Archer
- Flying attacker
- Elemental AoE
- MR attack

へ別々に当てます。

万能装備を作るのではなく、どのCounterに弱いかを把握します。

## Underwater / Storm

BattleだけでなくMap MoveからTestします。

```text
Item装備
→ 移動Arrow
→ Army同行可否
→ Battle
→ Retreat
→ Itemを外した後の帰還
```

まで確認します。

---

# Enemy Loadoutを読む

Enemy Itemは「強さ」だけでなく意図を教えます。

| 見えたItem / 能力 | 読める可能性 | Counter候補 |
|---|---|---|
| MR / Antimagic | MR attackを警戒 | Physical / Elementalへ変更 |
| High FR / SR / CR | 特定Elementalを警戒 | Damage type変更 |
| Air Shield | Missile警戒 | Melee / Magicへ変更 |
| Magic Weapon | Ethereal / Invulnerability対策 | Defence / Chaff / Fatigueへ移る |
| Reinvig | 長期戦前提 | Burst / Control |
| Mobility | Raid / interception | Destination防衛 |
| Water Breathing | Underwater作戦 | Coast / Sea接続監視 |
| Staff of Storms系 | Storm前提 | Flying / Archer構成を再計算 |
| Booster集中 | High Path Ritual / Battlefield spell | Carrier / Forge hubを狙う |
| Artifact | 高価なCarrier集中 | Mission denial / Carrier kill |

一個のItemだけでEnemy Researchを断定はしません。

しかし、Scout reportと合わせると次の作戦を読む材料になります。

---

# Army-wide SpellとItemの役割分担

Itemで全員を守ろうとするとGemとSlotが足りません。

## Item向き

- Rare Caster一人
- Raider一人
- Artifact Carrier
- Booster carrier
- Assassin
- 毎戦必要なResistance

## Spell向き

- 前衛全体
- 一戦だけのResistance
- Army全体のBuff
- Item slotを空けたい場合

## 両方使う

Army-wide protectionで大部分を守り、重要CommanderだけItemで不足分を補います。

これは特に、

- Shock
- Fire
- Poison
- Missile
- MR

対策で有効な考え方です。

---

# Inventoryを「Kit」として管理する

固定Buildを作るのではなく、Treasuryに機能別Kitを作ると再利用しやすくなります。

例：

```text
Anti-Missile kit
MR kit
Underwater kit
Raider mobility kit
Anti-Thug weapon kit
Caster protection kit
```

F7 / F8で所在を確認し、戦線ごとにCarrierへ付け替えます。

重要なのは、

> ItemはCommander専用品ではなく、国家在庫

として扱うことです。

---

# Forge queueへ落とす

任務が決まったら、最後にForge担当へ落とします。

```text
Turn 1: Booster
Turn 2: Minimal Raider weapon
Turn 3: Caster MR protection
Turn 4: Underwater utility
```

のように、GemだけでなくMage turnを予約します。

Rare Mageが、

- Research
- Ritual
- Site Search
- Battle
- Forge

を同時にできないことを忘れないでください。

[Forge計画とConstruction Breakpoint](forge-planning.md)と一緒に管理します。

---

# 国家攻略へ書くときの形式

Nation guideでは固定Buildを推奨せず、次の形にします。

| 任務 | 最小条件 | 候補Item機能 | Upgrade trigger | Counter |
|---|---|---|---|---|
| PD Raider | PDを倒す / 退路 | Magic Weapon、Sustain | Crossbow / Mage PD | Interception |
| Anti-Thug | 防御層を一枚抜く | AP / AN、MR、Resistance | Enemy loadout変更 | 別Damage type |
| Caster保護 | Script完走 | Missile、MR、Resistance | Attack Rear等 | Carrier pressure |
| Underwater | 移動＋帰還 | Water Breathing | Army輸送必要 | Sea control |

具体的なItem名は6.35 Inspectorとgenerated dataへリンクし、本文では**なぜ必要か**を説明します。

---

# よくある失敗

## 固定Buildをコピーする

Map、Enemy、Patch、Chassisが違えば同じ装備は同じ価値を持ちません。

## 空Slotを埋める

任務に不要なItemはGemだけでなく、Carrier死亡時の損失を増やします。

## Defenceを買い続ける

Enemyを倒せずFatigueで負けます。

## Offenseを買い続ける

一度も攻撃する前に死にます。

## Mobilityを最後に考える

勝てるCommanderが戦場へ届きません。

## Retreatを考えない

勝率90%でも、残り10%でCarrierと全Itemを失います。

## Army-wide問題を個人Itemで解く

100UnitへResistance Itemを配るのではなく、SpellやArmy構成を使います。

## Booster carrierを流用する

Raid一回のために国家唯一のHigh Path accessを危険へ晒します。

## 水中移動と水中戦闘を同じ問題にする

入れることと勝てることは別です。

## SightとEthereal Counterを混同する

視認能力とMagic Weaponは別systemです。

## Item effectの名前だけ見る

Weapon Secondary、Start battle spell、Summon、副作用を見落とします。

---

# 実戦用チェックリスト

```text
□ 任務を一行で書いたか
□ TargetをScoutしたか
□ Chassisだけで既に満たす機能を確認したか
□ Mobilityは足りるか
□ OffenseはTargetへ通るか
□ 主DamageへのDefenceがあるか
□ Fatigueは持つか
□ Retreat / Exitはあるか
□ Carrierを失ってよいか
□ Slot競合を見たか
□ 同じGemをSpellへ使う選択と比較したか
□ Forge MageのTurnを予約したか
□ Weapon / Armor profileを確認したか
□ Secondary / Start battle / Summon / Riskを確認したか
□ Test Gameで敗因を確認したか
□ F8で戦後に回収する計画があるか
```

---

## 関連ページ

- [Magic Item総論](index.md)
- [用途別Magic Item辞典](purpose-dictionary.md)
- [Forge計画とConstruction Breakpoint](forge-planning.md)
- [Item固有効果・Weapon proc・副作用](effects-and-procs.md)
- [Thug・Supercombatant装備](thug-equipment.md)
- [Resistance・Utility Item](resistance-items.md)
- [Magic Path Booster](boosters.md)
- [Artifact・Unique Item攻略](artifacts.md)
- [海・Underwater・Amphibious攻略](../systems/underwater.md)
- [Flying・Storm・Air機動戦](../systems/flying-storm.md)
- [Stealth・Glamour・特殊作戦](../systems/stealth-glamour.md)
- [Communion](../magic/communions.md)
- [Magic Itemデータ索引](../data/items/index.md)

## 参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- pinned `larzm42/dom6inspector` commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc` — Dominions 6.35
