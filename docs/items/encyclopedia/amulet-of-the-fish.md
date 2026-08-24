---
title: "Amulet of the Fish"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 363
---

# Amulet of the Fish

**Aquatic Commanderの周囲の空気を水へ変え、陸上で呼吸・移動できるようにするConstruction 5の進出用Misc Item。**

Amulet of the Fishは陸上Unitを海へ入れるItemではありません。方向は逆で、**本来は水中から出られないAquatic Carrierを陸上へ持ち出すItem**です。

この一点を取り違えると、Forgeしたのに目的の侵攻へ使えません。

- [Dominions 6.35固定データ — Item 363](../../data/items/by-id/363.md)
- [Magic Item攻略辞典](index.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)
- [Winged Shoes](winged-shoes.md)

---

# まず何ができるか

6.35固定データでは、Amulet of the FishはConstruction 5、Forge要求**W1A1**のMiscellaneous Itemです。

Item descriptionでは、装備者の周囲の空気を水へ変え、Aquatic beingが乾いた陸地でも呼吸し、移動できるようになると説明されています。

整理すると、

```text
Aquatic Commander
＋ Amulet of the Fish
→ 陸上で活動できる
```

です。

```text
陸上Commander
＋ Amulet of the Fish
→ 水中へ侵入できる
```

とは限りません。

水中侵入Itemを探す時は、効果の方向をItem descriptionとゲーム内表示で必ず確認します。

---

# 「Aquaticを陸へ出す」ためのItem

Amuletの主な価値は、海中限定のCommanderを陸上戦略へ接続することです。

対象になり得るのは、

- Aquatic Mageを陸上Labへ移す
- 海中国家の高Path Mageを陸上戦争へ投入する
- Aquatic Commanderを陸上Forge hubへ連れていく
- 海中で得た特殊Commanderを陸上Researchへ回す
- Aquatic PretenderやHeroの活動範囲を広げる

といった場面です。

Itemの価値はCarrierの戦闘Statsより、**そのCommanderしか持たないMagic access・Forge access・特殊能力を陸上へ輸送できるか**で決まります。

---

# Bearer一人へ作用する

Amulet of the Fishは装備者へ作用するItemです。

そのため、Aquatic Commanderが陸へ出られても、同行するAquatic troops全体が自動で陸上行動できるとは限りません。

確認すべきなのは、

- Commander本人が陸へ移動できるか
- 連れている各Unitが陸上移動可能か
- Army全体として同じRouteを通れるか
- Land province到着後に再編成できるか

です。

```text
Commanderだけ陸上可能
＋ Aquatic troopsは不可
→ Army orderが成立しない
```

という状況があり得ます。

Amulet一個をArmy-wide transportとして扱わない方が安全です。

---

# 戦闘Itemより物流Itemとして見る

Amulet自体は、Damage、Protection、MR、Reinvigoration等を直接補うための装備ではありません。

価値は、

```text
海中限定Commanderを陸へ出す
→ 新しいLab / Fort / Armyへ到達
→ Research・Forge・Ritual・Battle magicを行う
```

という経路から発生します。

したがって、戦闘に持ち込む必要がないCarrierなら、

- 安全な後方へ移動する時だけ装備
- 到着後も外してよいか確認
- 必要なら次のAquatic Commanderへ受け渡す
- F8等で所在を管理する

という物流運用を考えます。

ただし陸上でAmuletを外した時にCarrierがどう扱われるかは、実際のUnit状態とゲーム内制約を確認してから行います。

---

# 海中国家のMagic accessを陸上へ接続する

海中国家や水中Siteから得られるCommanderは、強いWater accessや特殊なCrosspathを持っていても、Aquaticであるため陸上戦争へ参加しにくいことがあります。

Amulet of the Fishは、

- Water Mageを陸上へ出す
- Booster chainの途中へ組み込む
- 陸上Labで別ItemをForgeする
- Coastal frontのArmyへBattle magicを供給する
- 陸上のGem stockpileを利用する

ことで、**地形によって分断されたMagic economyを接続**します。

一方でAmulet自身にW1A1 accessが必要なので、海中国家でもAir accessが薄い場合はForge routeを先に作る必要があります。

---

# Carrier選択は戦闘力より希少性

優先すべきCarrierは、単に強いAquatic Commanderではありません。

陸上へ出すことで、

- 新しいPath thresholdへ届く
- 重要BoosterをForgeできる
- 陸上ArmyにないBattle spellを使える
- Rare Ritualを行える
- Research効率の高いMageを安全な陸上Fortへ移せる

Commanderです。

Aquatic Commanderが陸へ出ても、同じ役割を陸上native Mageが安く代替できるなら、Amuletと移動Turnの投資価値は下がります。

---

# Misc Slotの機会費用

AmuletはMisc Slotを一つ使います。

陸上戦闘へそのまま投入する場合、

- Amulet of Antimagic
- Ring of Regeneration
- Girdle of Might
- Spell Focus
- Elemental Resistance Item
- Path Booster

等との競合が発生します。

つまりAquatic Carrierは、陸上に存在するためのSlotを一つ払いながら戦うことになります。

```text
陸上へ出られる価値
vs
戦闘用Misc Slotを一つ失うCost
```

を比較します。

後方Mageとして使うならSlot競合は軽く、ThugやCombat Casterとして使うなら重くなります。

---

# Itemの受け渡し計画

Amulet of the Fishは、Aquatic Commanderを一人ずつ陸上へ運ぶInfrastructureとして使える可能性があります。

ただし、

- 誰がどのProvinceで装備するか
- 海岸を越えるTurn
- 陸上到着後に外せるか
- 次のCarrierへどう戻すか
- Itemを持たないAquatic Commanderが取り残されないか

を先に設計します。

特に一個しかないAmuletを前線Carrierへ固定すると、次のAquatic Mageを輸送できません。

Dwarven Hammerと同様に貸し回す発想は使えますが、こちらは**地形境界を越える時点でItemが必須**になるため、handoff失敗の影響が大きくなります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- W1A1 Forge Mageを確保できる
- 陸上へ出したいAquatic Commanderがいる
- そのCommanderのMagic accessや能力が陸上で希少
- Coastから目的地まで安全なRouteがある
- 同行Unitも移動可能、またはCommander単独でよい
- Misc Slotを使っても任務が成立する
- Amuletを誰へいつ渡すか計画できる
- Test gameで陸上移動と装備解除の挙動を確認済み

「海にいる強いMageだから」ではなく、**陸上で何をさせるか**まで書ける時にForgeします。

---

# Forgeしない・別Itemを選ぶ条件

- 目的が陸上Unitの水中侵入である
- Aquatic Commanderを陸へ出す必要がない
- 陸上native Mageで同じ役割を代替できる
- Air accessが重くForge chainが割に合わない
- Commanderだけ移動できてもArmyが同行できない
- 前線戦闘でMisc Slot不足が致命的
- Coast routeが敵に封鎖されている
- Item loss時にCarrierが取り残されるRiskが高い

Amuletは戦闘Statsを直接増やさないため、**移動によって新しい役割を作れないなら価値は低い**です。

---

# Counter：Carrierではなく接続経路を狙う

敵がAmulet of the FishでAquatic Mageを陸へ出している場合、Itemそのものを正面からCounterする必要はありません。

価値は海中Magic accessと陸上戦線の接続から生まれるため、

- Coast provinceを奪う
- Handoff地点をRaidする
- Aquatic MageをAssassinationで狙う
- 陸上Labを破壊・占領する
- Amulet Carrierへ戦闘を強制しItem loss Riskを上げる
- 海と陸のGem輸送を分断する

ことで、接続を壊せます。

**物流ItemへのCounterは、能力を無効化するよりRouteを切る方が効率的**な場合があります。

---

# よくある失敗

## 陸上Unitを海へ入れるItemだと思う

Item descriptionはAquatic beingを乾いた陸地で活動させる方向を説明しています。

## Army全体へ作用すると思う

基本はBearer用Itemです。同行Unitごとの移動能力を確認します。

## 戦闘用Misc Slotを計算しない

陸上でCombat Carrierとして使う場合、MRやResistance Itemを一つ失います。

## Coastを越えた後のhandoffを考えない

Itemを外したCarrierや次のAquatic Mageが取り残される可能性があります。

## Rare Mageを無防備に単独移動させる

Aquatic Mage本体とAmuletを同時に失うRiskがあります。

---

# Test game checklist

```text
[ ] C5・W1A1でAmulet of the FishがForge可能か確認
[ ] Item 363であることを確認
[ ] Aquatic Commanderが装備後に陸上へ移動できることを確認
[ ] 陸上Unitの水中侵入Itemではないことを確認
[ ] Aquatic troopsが自動で陸上移動可能にならないことを確認
[ ] Coastを越える時のArmy orderを確認
[ ] 陸上でAmuletを外した時のCarrier状態を確認
[ ] 別Commanderへのhandoff経路を確認
[ ] 陸上戦闘時のMisc Slot不足を比較
[ ] Item loss・Retreat時にCarrierがどう扱われるか確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 363](../../data/items/by-id/363.md)
- [Winged Shoes](winged-shoes.md)
- [Boots of Quickness](boots-of-quickness.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)
- [Dwarven Hammer](dwarven-hammer.md)
- [任務別Magic Item Loadout](../mission-loadouts.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- 効果の方向はItem descriptionの「Aquatic beingをdry landで活動させる」記述を正本とする
- Army移動、装備解除、Retreat、Item loss後の扱いはゲーム内Map orderとTest gameを優先
