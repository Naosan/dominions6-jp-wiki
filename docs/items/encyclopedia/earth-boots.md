---
title: "Earth Boots"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 295
---

# Earth Boots

**Earth MageのEarth Pathを+1し、Battle spell・Ritual・Forgeの必要Pathを一段越えるためのConstruction 5 Boots。**

Earth Bootsは移動装備ではありません。攻略上は、**Mage一人のEarth accessを一段上へ移し、今まで実行できなかった仕事を解禁するPath Booster**として評価します。

- [Dominions 6.35固定データ — Item 295](../../data/items/by-id/295.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

---

# まず何ができるか

6.35固定データでは、Earth BootsはConstruction 5、Forge要求**E2**のBootsで、装備者の**Earthを+1**します。

典型的には、

```text
E2 Mage
→ Earth Bootsを装備
→ E3としてEarth magicを使う
```

という閾値越えに使います。

Item descriptionでも、Earth Mageが地面から力を引き出し、Earth magicでより強くなるItemとして説明されています。

重要なのは表示上のEarthが1増えることではなく、

```text
E+1で何が新しく可能になるか
```

です。

---

# E0へ新しいPathを与えるItemとして考えない

Item descriptionは対象を**Earth Mage**として説明しています。

そのため、Earth accessを持たないCommanderへ装備して、任意のE0をE1 Mageへ変える用途として計画するのは危険です。

実戦計画では、

- 素でEarthを持つか
- 装備前後でEarth表示がどう変わるか
- 目的Spell・Ritual・Forgeが選択可能になるか

をゲーム内で確認します。

Earth Bootsは、原則として**既存のEarth accessを伸ばすBooster**として扱う方が安全です。

---

# E2でForgeしてE3へ届く

Earth Bootsの基本的な橋は、

```text
native E2
→ Earth BootsをForge
→ E3運用
```

です。

この一段によって、

- より高いEarth Battle spell
- Earth Ritual
- 高Pathを要求するMagic Item
- 次のBooster chain

へ届く可能性があります。

ただし、最初の一本を作るには**E2 Forge Mage**が必要です。

native E1しかいない国家が、Earth Bootsだけを前提に自己完結してE2へ上がれるわけではありません。

最初の一本を誰がForgeするかまで含めてaccess routeを設計します。

---

# Boosterは「新しい仕事」が生まれた時に強い

Earth Boots装備後に確認するのは、単なるPath表示ではありません。

```text
装備前: E2で実行できる仕事
装備後: E3で新しく実行できる仕事
```

の差です。

価値が高い例は、

- 戦闘Scriptへ重要なEarth spellを追加できる
- Ritual requirementをちょうど越える
- 必要なArmor・Weapon・BoosterをForgeできる
- 高Path casterを別任務から解放できる
- Gem消費やFatigueを抑えたCastへ届く

場合です。

逆に、E+1しても現在のResearchでは選択肢が増えないなら、その時点のBootsは寝ています。

---

# Battle Mageへ持たせる場合

前線Earth Mageへ装備すると、Battle spellの選択肢やCast条件が変わります。

確認する項目は、

- 目的Spellの必要Earth
- 現在のResearch
- Spell Gemの有無
- Earth Boots装備時のFatigue
- Script完走までCarrierが生存できるか
- Boots Slotを使っても戦場へ到達できるか

です。

Pathが上がることで、単に新Spellを選べるだけでなく、同じSpellをより高PathでCastできる場合があります。

ただし具体的なFatigue変化はSpell、Gem投入、Battlefield effectで変わるため、Battle Replayで確認します。

---

# 後方Ritual・Forge用では共有しやすい

Earth Bootsは前線専用品ではありません。

Lab内で、

- RitualするTurnだけ装備する
- 高Path ItemをForgeするTurnだけ装備する
- 使用後に別Mageへ渡す

という運用ができます。

後方運用なら、Boots Slotの戦闘上の機会費用は小さくなります。

```text
Earth Boots一足
→ 複数のEarth Mageが必要Turnだけ共有
```

という形で、Mage個人の常設装備ではなく**Labの共有Infrastructure**として扱えます。

誰が現在持っているかを管理しないと、必要Turnに別Fortへ置き忘れるため、Item移送も計画します。

---

# Forge用Boosterとしての価値

Earth magicはArmor、Weapon、Booster、Forge economyに関係するItemが多く、Earth Boots自身が次のForge requirementへ届く橋になることがあります。

評価順は、

1. BootsなしでForgeできない目的Itemがある
2. Boots装備で必要Earthへ届く
3. Construction requirementも満たしている
4. 必要Gemを確保できる
5. そのForge turnを払う価値がある

です。

「E3になれる」だけでは不足で、

```text
E3になったTurnに何をForgeするか
```

まで決めます。

---

# Boots Slotが最大の機会費用

Earth BootsはBoots Slotを使います。

同じSlotには、

- [Winged Shoes](winged-shoes.md)
- [Boots of the Messenger](boots-of-the-messenger.md)
- [Boots of Quickness](boots-of-quickness.md)
- Terrain・movement補助Boots
- 戦闘用の特殊Boots

を装備できます。

そのため前線Carrierでは、

```text
Earth +1で得るSpell access
vs
Flying・Map Move・Quickness等を失うCost
```

を比較します。

後方RitualistやForgerではSlot競合が軽く、Raid MageやCombat Casterでは重くなります。

---

# Winged Shoesとの違い

Winged ShoesはCommanderへFlyingを与え、**戦場へ到達する経路**を変えます。

Earth BootsはEarth +1を与え、**到達後に行える魔法**を変えます。

```text
Winged Shoes
→ そのProvinceへ行けるか

Earth Boots
→ そのProvinceで目的Spellを使えるか
```

という違いです。

目的SpellをCastできても前線へ間に合わなければ意味がなく、前線へ飛べても必要Pathが足りなければ役割を果たせません。

両方必要な任務では、Carrier分割、別の移動手段、前線Labでの受け渡しを検討します。

---

# Boots of the Messengerとの違い

Boots of the MessengerはMap Move BonusとReinvigorationを与えます。

Earth Bootsは戦略移動もFatigue sustainも直接増やしません。

そのため、

- 急行・追随・長期戦が任務の上限ならBoots of the Messenger
- Earth Path requirementが任務の上限ならEarth Boots

です。

Earth Mageが重装や高Fatigue spellで疲れる場合、Earth +1とReinvigorationのどちらが実際の敗因を解決するかをTestします。

---

# 誰に持たせるか

優先したいCarrierは、

- 素でEarth accessを持つ
- +1で具体的なSpell・Ritual・Forgeが解禁される
- 目的Researchへ到達済み
- 必要Gemを受け取れる
- Boots Slotを他の必須Itemへ使わない
- 前線なら生存と移動を確保できる

Mageです。

単に最も高価なEarth Mageへ常設する必要はありません。

E2→E3で役割が生える安いMageの方が、すでにE4で必要な仕事をこなせる高価なMageより効率的な場合があります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- 最初の一本をForgeできるE2 Mageがいる
- E+1で具体的な仕事が解禁される
- その仕事を使うResearchが終わっている
- Earth Gemを確保できる
- Boots Slotの競合を許容できる
- 戦争・Ritual・Forge予定へ間に合う
- 一足を複数Mageで共有できる

特に、

```text
Earth Boots完成
→ 次Turnに目的Ritual / Forge / Battle
```

まで繋がる時は投資理由が明確です。

---

# Forgeしない・後回しにする条件

- E+1しても新しい仕事が増えない
- 目的Researchが未完了
- 最初のE2 Forge Mageがいない
- Earth GemをBattle magicや別Itemへ回す必要がある
- Boots SlotへFlying・Map Move・Quicknessが必須
- すでに高Path Mageだけで必要数を賄える
- 前線への輸送が戦争Timingに間に合わない
- 理論上のBooster chainだけで、最終目的がない

Path Boosterは将来性がありますが、**使うTurnが決まっていない在庫**を増やしすぎるとGemとForge turnが眠ります。

---

# Counter：Earth +1で何が解禁されたかを見る

敵がEarth Bootsを装備していたら、「Eが1増えた」で止めません。

読むべきなのは、

- Carrierの素Earth
- Boots込みのEarth
- 現在のResearch帯
- 新しく使えるBattle spell
- Bootsを失うとScriptが崩れるか
- Boots Slotのために何を諦めているか

です。

Counterは、

- CarrierをAssassination・Raid・Missileで狙う
- Spell Gem carrierを落とす
- Boots依存のSpellへResistanceやFormationを合わせる
- FlyingやMap Moveを持てないSlot競合を突く
- 前線Lab・受け渡しProvinceを攻撃する
- Ritual・Forge hubを封鎖する

ように、**Earth Bootsで新しく成立した役割**へ向けます。

---

# よくある失敗

## E+1だから自動的に強いと思う

新しいSpell・Ritual・Forgeが解禁されなければ、表示だけ増えることがあります。

## E0 Commanderへ新Pathを与える前提にする

Item descriptionはEarth Mageを対象にしています。実際の装備前後表示を確認します。

## Boots Slotを忘れる

前線MageがWinged ShoesやBoots of the Messengerを失い、目的地へ届かなくなることがあります。

## 最初の一本を誰がForgeするか決めない

native E1しかおらず、計画したTurnにE2 Forgerがいない場合があります。

## Researchより先に作る

Bootsは完成したのに、目的Spell・Ritualが未研究で眠ります。

## 高Path Mageへ常設する

必要Turnだけ共有できる場合、常設は在庫効率を下げます。

---

# Test game checklist

```text
[ ] C5・E2でEarth BootsがForge可能か確認
[ ] Item 295であることを確認
[ ] Earth Mageの装備前後でEarthが+1されることを確認
[ ] Earthを持たないCommanderで表示がどうなるか確認
[ ] 目的Battle spellが装備後に選択可能か確認
[ ] 目的Ritual / Forge requirementを越えられるか確認
[ ] SpellのFatigueとGem消費を装備前後で比較
[ ] Boots Slotの他Itemと競合を確認
[ ] 一足を別Mageへ渡して共有運用できるか確認
[ ] 前線への輸送Turnを確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 295](../../data/items/by-id/295.md)
- [Skull Staff](skull-staff.md)
- [Thistle Mace](thistle-mace.md)
- [Winged Shoes](winged-shoes.md)
- [Boots of the Messenger](boots-of-the-messenger.md)
- [Magic Path Booster](../boosters.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- Dominions 6 Main Manual — Forge Item / Magic Path / Battle magic
- Spell・Ritual・Forgeの実際の選択可否はゲーム内表示を最終確認
