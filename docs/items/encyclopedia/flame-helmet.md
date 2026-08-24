---
title: "Flame Helmet"
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
item_id: 192
---

# Flame Helmet

**Fire MageのFire Pathを+1する一方、Reinvigoration -3を負わせる、重い前提条件を持つConstruction 5のHelmet Booster。**

Flame Helmetは、単に「Fireを一段上げる便利な帽子」ではありません。

攻略上は、

```text
Fire +1で新しい閾値を越える価値
－
F4 Forge起点
－
Helmet Slot
－
Reinvigoration -3
```

をまとめて評価するItemです。

- [Dominions 6.35固定データ — Item 192](../../data/items/by-id/192.md)
- [Magic Item攻略辞典](index.md)
- [Magic Path Booster](../boosters.md)
- [Amulet of Resilience](amulet-of-resilience.md)

---

# まず何ができるか

6.35固定データでは、Flame Helmetは、

- Construction 5
- Forge要求 **F4**
- Helmet Slot
- **Fire +1**
- **Reinvigoration -3**
- Armor record 80

を持ちます。

Armor record 80はDefence 0、Encumbrance 0のHelmetで、頭部Protection 21を持ちます。

Item descriptionでは、装備すると兜の上に炎が現れ、その炎が装備者の生命力を示し、Fire magicを強化すると説明されています。また、熱から装備者を守り、戦闘中の着用はかなり負担になるとも説明されています。

ただし、pin済みBaseIの通常Resistance欄からは、独立した数値のFire Resistanceを確認できません。

そのため、

> 「説明文に熱から守るとある」

ことと、

> 「Fire Resistance +Xが付く」

ことを同一視せず、最終的なUnit表示をゲーム内で確認します。

---

# Fire +1は「何が解禁されたか」で測る

Flame Helmetの価値は、Fire表示が1増えたこと自体ではありません。

装備前後で、

- 新しく選べるBattle spell
- 新しく実行できるRitual
- 新しくForgeできるItem
- 同じSpellを高PathでCastした場合のFatigue
- 次のBoosterやSummonへ届く経路

がどう変わるかを確認します。

```text
F4 Mage
→ Flame Helmet
→ F5として目的Spell / Ritual / Forgeへ到達
```

のように、**閾値を越える具体的な仕事**がある時に強いItemです。

F+1しても現在のResearchでは新しい仕事が増えないなら、Helmetは完成していても戦略上は寝ています。

---

# 最初の一個を作るためにF4が要る

Flame Helmetの最大の入口条件は、Forge要求F4です。

つまり、

```text
低Fire Mage
→ Flame Helmetを作る
→ 高Fireへ到達
```

という自己完結した最初の一段にはなりません。

最初の一個には、

- native F4 Mage
- Random込みでF4へ届くMage
- Summon Mage
- Hero
- Pretender
- 別Boosterを装備したForger
- Empowerment済みMage

などが必要です。

Booster計画では、完成後のCarrierだけでなく、

> **誰が最初のFlame HelmetをForgeするのか**

を先に決めます。

F4 accessがPretender一体だけなら、そのPretenderのForge turnを使う価値まで含めて判断します。

---

# Reinvigoration -3が前線運用の代償

Flame Helmetは装備者へReinvigoration -3を与えます。

これは、表示上のFire +1とは別の、明確な戦闘上のCostです。

特に、

- 複数のSelf-buffを使う
- 高Fatigue Spellを繰り返す
- 重いArmorを装備する
- 長期戦になる
- Cast後に近接戦へ入る
- 敵がFatigue damageを使う

Carrierでは、Fatigue収支を悪化させます。

```text
Fire +1でSpellを解禁
→ しかしReinvigoration -3でScript完走前にFatigueが増える
```

なら、Pathだけ見れば成功でも、Battle planとしては失敗です。

Flame Helmetなし／ありで、RoundごとのFatigue、予定Spellの発動回数、Fatigue 100へ達するRoundを比較します。

---

# Fire +1がFatigueを軽くする場合もある

一方で、Pathが上がることで目的SpellのFatigueが下がる場合があります。

そのため実際の収支は、

```text
Fire +1によるCast条件・Fatigue改善
vs
Reinvigoration -3による毎Roundの悪化
```

です。

どちらが勝つかは、

- CastするSpell
- 元のFire level
- Gem投入
- Spell回数
- 戦闘時間
- Armor Encumbrance
- 他のReinvigoration source

で変わります。

「Reinvigoration -3だから戦闘では必ず弱い」とも、「Fire +1だからFatigue問題は消える」とも固定化しません。

Battle Replayで予定Script全体を確認します。

---

# 後方Ritual・Forge用なら欠点が軽い

Flame HelmetをLab内だけで使う場合、Reinvigoration -3の戦闘上の欠点はほぼ問題になりません。

典型的には、

- 高Fire Ritualを行うTurnだけ装備
- 高Fire ItemをForgeするTurnだけ装備
- 使用後にLabへ戻す
- 別のFire Mageへ受け渡す

という共有運用です。

```text
Flame Helmet一個
→ 複数Mageが必要Turnだけ使用
```

とすれば、Rare Boosterを各Mageへ常設する必要はありません。

後方専用ならHelmet Slotの防御価値も重要ではなく、Itemの評価はほぼ「F+1で何を解禁するか」に集中します。

---

# Battle Mageへ持たせる場合

前線で使う場合は、次を同時に確認します。

- F+1で目的Spellが解禁される
- Scriptを最後まで実行できる
- Reinvigoration -3を含めてもFatigueが許容範囲
- Helmet Slotを使っても必要な防御が残る
- CarrierがAssassinationやMissileで早期に倒されない
- Gem carrierと同じProvinceへ移動できる
- Retreat routeがある

Flame Helmetを持つMageは、敵から見れば「高Fire Spellを成立させる鍵」です。

前列へ置くより、目的SpellのRangeと敵の攻撃手段を見て配置します。

---

# Helmetとしての防御

Armor record 80は、Defence 0、Encumbrance 0、頭部Protection 21です。

つまりFlame Helmetは、Path Boosterでありながら頭部防具としても機能します。

ただし、

- 全身Protectionを21にするItemではない
- Helmetは頭部だけを守る
- MR-based effectはProtectionで止まらない
- Reinvigoration -3はArmor recordのEncumbrance 0とは別に存在する

ことに注意します。

```text
Armor Encumbranceは0
≠
Fatigue上の負担がない
```

です。

Flame Helmetの負担は、Item本体のReinvigoration -3として現れます。

---

# Helmet Slotの機会費用

Flame Helmetを装備すると、同じSlotの、

- Winged Helmet
- Starshine Skullcap
- Resistance Helmet
- Protection重視Helmet
- 特殊視覚・特殊能力Helmet

を使えません。

したがって前線Casterでは、

```text
Fire +1
vs
別HelmetによるPath・MR・Resistance・Protection・Utility
```

を比較します。

特にCrosspath Mageでは、Fire Boosterを取ることで別Path Boosterを失う場合があります。

一人へすべての役割を集めるより、Casterを分けた方がよいこともあります。

---

# Amulet of Resilienceで補うべきか

[Amulet of Resilience](amulet-of-resilience.md)はReinvigoration +5を与えます。

組み合わせれば、Flame HelmetのReinvigoration -3を補い、差し引きでは正のReinvigorationを得られる可能性があります。

ただし、

```text
Flame Helmet
＋ Amulet of Resilience
```

はHelmet SlotとMisc Slotを使います。

その結果、

- Amulet of Antimagic
- Ring of Regeneration
- Elemental Resistance
- Penetration Item
- 別Path Booster

を失うかもしれません。

Fatigueだけを直すために装備枠を追加投入し、別の致命的弱点を作っていないか確認します。

後方RitualistならFatigue補助は不要で、前線Casterだけが比較対象です。

---

# Carrierを選ぶ

優先したいCarrierは、

- 素でFire magicを持つ
- +1で具体的なSpell・Ritual・Forgeが解禁される
- F4以上の目的へ届く
- Reinvigoration -3を許容できる
- Helmet Slotを他の必須Itemへ使わない
- 前線なら防御・配置・撤退を確保できる

Mageです。

単に最もFireが高いMageへ常設する必要はありません。

高Fire MageがHelmetなしでも目的を達成できるなら、あと1足りないMageへ渡してCaster数を増やす方が強い場合があります。

---

# Forgeする条件

次が揃うほど優先度が上がります。

- Construction 5へ到達済み
- 最初の一個を作れるF4 Forgerがいる
- F+1で具体的な仕事が増える
- 目的Researchへ到達済み
- 必要なFire Gemを継続供給できる
- 後方で共有するか、前線Carrierを明確に決めている
- Helmet Slot競合を解決済み
- Reinvigoration -3込みのScriptをTest済み
- Itemを失った場合の代替Casterがいる

「Fire Boosterだからいつか使う」ではなく、

> **完成した次のTurnに何をCast・Ritual・Forgeするか**

まで書ける時に優先します。

---

# Forgeしない・後回しにする条件

- F4 Forgerがいない
- F+1しても現在のResearchで仕事が増えない
- 高Fire Mageがすでに必要数いる
- PretenderのForge turnが他の任務より高価
- 前線CasterがFatigueでScriptを完走できない
- Helmet Slotへ別Boosterが必須
- Fire GemをBattle magicやSummonへ回す必要がある
- 一戦だけの用途で代替Casterを用意できる
- Booster喪失時に戦略全体が止まる

高いForge起点を持つItemなので、「作れるようになった」だけで惰性量産しません。

---

# Counter：Helmet込みのFire閾値を読む

敵のFlame Helmetを見たら、「Fire Mageが少し強くなった」で止めません。

確認するのは、

- Carrierの素Fire
- Helmet込みのFire
- そのResearch帯で新しく使えるSpell
- 必要Gem
- Reinvigoration -3による長期戦の弱さ
- Helmetを失うとScriptが崩れるか

です。

Counterは、

- 高Fire Spellに合わせてFire Resistanceを用意する
- CarrierをAssassination・Raid・Missileで狙う
- Gem carrierを落とす
- Fatigue pressureを掛け、Reinvigoration -3を拡大する
- 長期戦へ持ち込みScript後の失速を狙う
- Magic Duel等、Carrierの別弱点を突く
- Booster依存Casterを複数戦線へ分散させる

ように、**Flame Helmetによって成立した新しい仕事**を崩します。

---

# よくある失敗

## F+1だけを見て前線へ出す

Reinvigoration -3で、予定Spellの前にFatigueが問題になることがあります。

## Armor Encumbrance 0だから疲れないと思う

Item本体にReinvigoration -3があります。

## 説明文からFire Resistance +Xを推測する

数値はゲーム内Unit表示とgenerated recordを確認します。

## 最初の一個を誰が作るか決めていない

Forge要求F4なので、低Fire国家では計画が入口で止まります。

## Researchより先に作る

F+1しても使うSpellが未研究なら、GemとForge turnが寝ます。

## Rare Boosterを一人へ固定する

後方Ritual・Forge用途なら、Labで共有できる場合があります。

## Fatigue補助を積みすぎる

Reinvigorationを直すためにMR・Resistance・Penetrationを外し、別Counterへ弱くなることがあります。

---

# Test game checklist

```text
[ ] C5・F4でFlame HelmetがForge可能か確認
[ ] Item 192・Armor record 80であることを確認
[ ] 装備前後でFire +1を確認
[ ] Fireを持たないCommanderでPath表示がどうなるか確認
[ ] Reinvigoration -3をUnit画面で確認
[ ] 頭部Protection 21・Defence 0・Armor Encumbrance 0を確認
[ ] 説明文のheat protectionがUnit画面で何として表示されるか確認
[ ] Helmetなし／ありで目的Spellの選択可否を比較
[ ] Helmetなし／ありでRoundごとのFatigueを比較
[ ] Amulet of Resilience併用時のFatigue収支を比較
[ ] 後方Ritual・Forgeで別Mageへ受け渡せるか確認
[ ] Carrier死亡時に戦略がどこまで停止するか確認
```

---

# 関連

- [Magic Item攻略辞典](index.md)
- [Dominions 6.35固定データ — Item 192](../../data/items/by-id/192.md)
- [Magic Path Booster](../boosters.md)
- [Forge計画とConstruction Breakpoint](../forge-planning.md)
- [Amulet of Resilience](amulet-of-resilience.md)
- [Elemental Armor](elemental-armor.md)

## Source note

- pin済み`larzm42/dom6inspector` Dominions 6.35 BaseI / armors / protections_by_armor / Item description
- BaseIで確認した主要field：C5、F4、Fire +1、Reinvigoration -3、Armor 80
- Armor record 80：Defence 0、Encumbrance 0、頭部Protection 21
- heat protectionの最終表示と実挙動はゲーム内Unit画面・Battle Replayを優先
