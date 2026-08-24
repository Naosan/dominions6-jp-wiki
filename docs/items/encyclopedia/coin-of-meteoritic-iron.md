---
title: "Coin of Meteoritic Iron"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 372
---

# Coin of Meteoritic Iron

**Astral MageのAstral Pathを+1し、Magic Resistanceも+1する、S2E2 ForgeのConstruction 5 Misc Booster。**

Coin of Meteoritic Ironは、古い攻略で見かける`Crystal Coin`という名前をDom6へそのまま持ち込まず、**現行6.35で確認するAstral Booster**です。

攻略上は、

```text
Astral +1
＋ Magic Resistance +1
－ S2E2というCrosspath Forge条件
－ Misc Slot
```

として評価します。

- [Dominions 6.35固定データ — Item 372](../../data/items/by-id/372.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Spell Focus](spell-focus.md)

---

# まず何ができるか

6.35固定データでは、Coin of Meteoritic Ironは、

- Construction 5
- Forge要求 **S2E2**
- Miscellaneous Slot
- **Astral +1**
- **Magic Resistance +1**

を持ちます。

Item descriptionでは、流星が外側のSphereから地上へ落ちた時に得られるSky Metalで作られ、その物質がAstral magicを増幅し、Astral Mageの力を高めると説明されています。

つまり主用途はAstral Boosterであり、MR +1は付随する防御です。

---

# Astral +1は「新しい仕事」で評価する

Coinの価値は、Astral表示が1増えたこと自体ではありません。

装備前後で、

- 新しく選べるBattle spell
- 新しく実行できるRitual
- 新しくForgeできるItem
- 同じSpellを高PathでCastした場合のFatigue
- Communion外で届くPath
- Global・Teleport系Ritualへの到達
- 次のBooster chain

がどう変わるかを確認します。

```text
S2 Mage
→ Coin of Meteoritic Iron
→ S3として目的Spell / Ritual / Forgeへ到達
```

のように、**あと1で重要なAstral閾値へ届くMage**へ持たせます。

S+1しても現在のResearchで役割が増えないなら、CoinはGemとForge turnを寝かせています。

---

# S2E2 Crosspathが最大の入口条件

Coin of Meteoritic IronのForge要求はS2E2です。

Construction 5へ到達しても、

- S2はいるがE2がいない
- E2はいるがS2がいない
- SとEが別Mageに分かれている
- Random crosspathが同時成立しない

場合、最初のCoinをForgeできません。

```text
国家全体にS2とE2がある
≠
一人のMageがS2E2を持つ
```

ことに注意します。

最初の一個には、

- native S2E2 Mage
- 同時RandomでS2E2へ届くMage
- Booster込みで条件を満たすMage
- Summon Mage
- Hero
- Pretender
- Empowerment済みMage

が必要です。

Magic access計画では、各Pathの最高値ではなく、**同じCarrier上のCrosspath**を確認します。

---

# 古い「Crystal Coin」表記をそのまま使わない

Dom4・Dom5時代の攻略、会話、Build表には`Crystal Coin`という名称が出ることがあります。

Dom6 6.35の固定データで確認するItem名は**Coin of Meteoritic Iron**です。

古い名称だけで検索すると、

- 現行Itemを見つけられない
- Forge requirementを旧作値で記憶する
- Slotや副効果を誤る
- 別Itemと混同する

可能性があります。

このWikiでは、旧名称を検索手掛かりとして扱うことはあっても、見出しと固定値は現行Item名へ合わせます。

---

# Magic Resistance +1は補助防御

Coinは装備者へMR +1も与えます。

これは、

- MR-negates Spell
- Mind Control
- Soul系効果
- 敵Astral Mageからの攻撃
- AssassinのMR依存手段

に対して、わずかながら防御を補います。

ただしMR +1だけで、重要CasterのMR対策が完成するとは限りません。

```text
Coin
→ 主目的はAstral +1
→ MR +1は付随価値
```

と考えます。

敵の主CounterがMR-based effectなら、[Amulet of Antimagic](amulet-of-antimagic.md)等の専用Itemも比較します。

---

# Amulet of Antimagicとの違い

[Amulet of Antimagic](amulet-of-antimagic.md)はMR防御を主目的にするMisc Itemです。

Coin of Meteoritic IronはAstral +1が主目的で、MR +1が付随します。

```text
Coin of Meteoritic Iron
→ Astral閾値を越える
→ MRも少し増える

Amulet of Antimagic
→ MR防御を大きく優先する
→ Astral Pathは増えない
```

という違いです。

両方ともMisc Slotを使うため、同じSlotへ同時には置けません。

Astral +1がScript成立に必須ならCoinを優先し、Pathは足りていてMRだけが敗因ならAmuletを優先します。

---

# Spell Focusとの違い

[Spell Focus](spell-focus.md)は、MR-negates Spellを敵へ通しやすくするためのPenetration Itemです。

CoinはAstral Path +1です。

```text
Coin
→ Spell requirementを越える
→ 高Path CastによるFatigue・効果差を得る可能性
→ MR +1

Spell Focus
→ Penetrationを直接増やす
→ Path requirementは越えない
```

です。

目的SpellをそもそもCastできないならCoinが先です。

SpellはCastできるが高MR Targetへ通らないならSpell Focusを比較します。

両方ともMisc Slotなので、Carrier一人で同時に使うには複数Misc Slotが必要です。

---

# Eye of the Voidとの違い

[Eye of the Void](eye-of-the-void.md)はPenetration +2を与える一方、MR -2と眼の置換Riskを持ちます。

CoinはPenetrationを直接増やしませんが、

- Astral +1
- MR +1
- 眼の置換なし

です。

```text
Eye of the Void
→ 高いPenetration
→ 自分のMR低下と不可逆性Risk

Coin of Meteoritic Iron
→ Astral Pathの閾値越え
→ 小さなMR補助
```

という役割差です。

高MR Targetへ通すことだけが目的ならEyeが候補になり、Spell requirementやRitual・Forgeまで含めるならCoinが候補です。

---

# Communionとの役割分担

AstralはCommunionで戦闘中のPathを大きく上げられます。

一方、Coin of Meteoritic Ironは装備中のItem Boosterなので、

- Battle spell
- Ritual
- Forge

で使えます。

```text
Coin
→ Strategic Map上でもAstral +1
→ Ritual・Forgeにも有効

Communion
→ Battle中だけPathを上げる
→ SlaveとScriptが必要
```

という違いです。

戦闘だけならCommunionで代替できる場合があります。

Ritual・Forge・Global casterを作るなら、Communionは代替になりません。

Battle planでも、少人数戦やAssassinationではCommunionを組みにくいため、Coinの恒常的な+1が役立つことがあります。

---

# Magic Duel Riskを読む

高Astral Mageを前線へ出す場合、敵Astral Mageとの相互作用を考えます。

CoinでAstralが上がることは、目的Spellへの到達だけでなく、Astral levelを参照する対決で結果へ影響する可能性があります。

ただし、

- 敵Astral Mageの数
- 敵の素Astral
- 自軍Carrierの価値
- Coin喪失Risk
- Magic Duel以外のCounter

をまとめて見ます。

「Astral +1だから必ず安全」ではありません。

高価なCoin Carrierを前線へ出すなら、敵のAstral rosterを偵察し、Test gameで想定対決を確認します。

---

# Battle Mageへ持たせる場合

前線で使う場合は、

- S+1で目的Spellが解禁される
- 必要Gemを持っている
- Penetrationが足りる
- MR +1込みでも敵Counterへ耐えられる
- Misc Slotを使ってもFatigue・Resistanceが足りる
- Communionへ入るか、単独Casterか決まっている
- CarrierがAssassination・Raid・Missileで早期に落ちない

ことを確認します。

CoinはCasterの役割を増やしますが、生存、Range、Precision、Retreatを自動的に解決しません。

---

# 後方Ritual・Forge用では共有しやすい

Lab内で使う場合、Coinは共有Infrastructureとして扱えます。

典型的には、

- Astral Ritualを行うTurnだけ装備
- 高Astral ItemをForgeするTurnだけ装備
- GlobalをCastするMageへ一時的に渡す
- 使用後にLabへ戻す

運用です。

```text
Coin一個
→ 複数のAstral Mageが必要Turnだけ使用
```

できます。

S2E2というCrosspath Forge条件を越えて作ったItemなので、不要なTurnまで一人へ固定しない方がよい場合があります。

ただしFort間移送のTurn、敵Raid、Lab破壊Riskを管理します。

---

# Misc Slotの機会費用

CoinはMisc Slotを一つ使います。

同じSlotには、

- Amulet of Antimagic
- Spell Focus
- Eye of the Void
- Ring of Regeneration
- Amulet of Resilience
- Girdle of Might
- Water Bracelet
- Elemental Resistance Item

が入ります。

前線Casterでは、

```text
Astral +1・MR +1
vs
Penetration・大きなMR・Fatigue・Resistance・HP sustain
```

を比較します。

後方RitualistならSlot競合は軽く、Combat Casterほど重くなります。

---

# Carrierを選ぶ

優先したいCarrierは、

- 素でAstral magicを持つ
- +1で具体的なSpell・Ritual・Forgeが解禁される
- 目的Researchへ到達済み
- 必要Gemを受け取れる
- Communion外で高Astralを必要とする
- Misc Slotを他の必須Itemへ使わない
- 前線ならMR・配置・撤退を確保できる

Mageです。

すでにCoinなしで目的を達成できる高Astral Mageへ常設するより、S2→S3等で役割が生えるMageへ渡し、担当者を増やす方が強い場合があります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- 同じMage上でS2E2 Forge条件を満たせる
- S+1で具体的な仕事が増える
- 目的Researchへ到達済み
- Astral・Earth Gemを確保できる
- 前線用か後方共有用か決めている
- Misc Slot競合を解決済み
- Communionで代替できないRitual・Forge用途がある
- Carrier喪失時の代替がある

特に、

> **Coin完成後に、誰が何をCast・Ritual・Forgeするか**

が決まっている時に投資します。

---

# Forgeしない・後回しにする条件

- S2E2を同じMage上で作れない
- S+1しても仕事が増えない
- Communionだけで戦闘目的を満たせる
- 高Astral Mageがすでに必要数いる
- Misc SlotへPenetration・MR・Fatigue Itemが必須
- Astral・Earth Gemを別の重要用途へ回したい
- 一戦だけなら別CasterやGem boostで代替できる
- Coin喪失でRitual・Forge chain全体が止まる

「Astral Boosterだから必須」ではなく、Crosspath、目的、使用回数で判断します。

---

# Counter：Coin込みのAstral閾値を読む

敵のCoin of Meteoritic Ironを見たら、Carrierの素AstralとCoin込みAstralを確認します。

見るべきなのは、

- どのSpell閾値を越えたか
- Communionに入るか単独Casterか
- Ritual・Globalの準備か
- Penetration Itemを外しているか
- Coinを失うとScriptが崩れるか
- MR +1でどのCounterを補っているか

です。

Counterは、

- MRを上げ、AstralのMR-negates Spellへ備える
- CarrierをAssassination・Raid・Missileで狙う
- Magic Duel等、Astral相互作用を利用する
- Gem carrierを落とす
- CoinでMisc Slotを使っているため、Fatigue・Resistance不足を突く
- Communion Slaveを先に崩す
- Lab・Fortを攻め、共有Coinの移送を乱す
- 複数戦線を作り、一枚のCoinへ依存するCasterを分散させる

ように、**Astral +1で成立した役割**を崩します。

---

# よくある失敗

## 国家全体にS2とE2があるからForgeできると思う

S2E2は同じMage上で必要です。

## Crystal Coinという旧名称だけで探す

現行6.35のItem名はCoin of Meteoritic Ironです。

## MR Itemとしてだけ評価する

主効果はAstral +1で、MR +1は付随価値です。

## Penetrationも直接増えると思う

Coinの固定fieldはAstral +1とMR +1です。Penetration Itemとは役割が違います。

## CommunionでRitual・Forgeも代替できると思う

CommunionはBattle中限定です。

## 高Astral Mageへ常設する

後方用途なら一個を共有できる場合があります。

## Misc Slot競合を忘れる

Spell Focus、Eye of the Void、Amulet of Antimagic等を外すCostがあります。

---

# Test game checklist

```text
[ ] C5・S2E2でCoin of Meteoritic IronがForge可能か確認
[ ] Item 372であることを確認
[ ] 装備前後でAstral +1を確認
[ ] Astralを持たないCommanderでPath表示がどうなるか確認
[ ] Magic Resistance +1を確認
[ ] Penetrationが直接増えないことを確認
[ ] Coinなし／ありで目的Spellの選択可否を比較
[ ] Ritual・Forge requirementを越えられるか確認
[ ] Communion時と単独時の役割を比較
[ ] Spell Focus・Eye of the Void・Amulet of AntimagicとのSlot競合を比較
[ ] Magic Duel等のAstral相互作用を想定相手で確認
[ ] 後方Labで別Mageへ共有できるか確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 372](../../data/items/by-id/372.md)
- [Magic Path Booster](../boosters.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [Spell Focus](spell-focus.md)
- [Eye of the Void](eye-of-the-void.md)
- [Amulet of Antimagic](amulet-of-antimagic.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / Item description
- BaseIで確認した主要field：C5、S2E2、Miscellaneous、Astral +1、Magic Resistance +1
- Item descriptionはAstral Mageの力を増幅するSky Metal Itemとして説明
- Pathless Carrier、Spell Fatigue、Magic Duel等の最終挙動はゲーム内表示・Battle Replayを優先
