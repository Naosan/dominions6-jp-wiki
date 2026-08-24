---
title: Magic Item攻略辞典
status: reviewed
verified_version: "6.35"
last_verified: "2026-08-24"
---

# Magic Item攻略辞典

Magic Itemを**Item名から引くための手書き攻略辞典**です。

このWikiにはすでに、全Itemを機械的に扱う[Magic Item個別record一覧](../../data/items/records.md)、欲しい機能から探す[用途別Magic Item辞典](../purpose-dictionary.md)、Commanderへさせたい仕事から組む[任務別Magic Item Loadout](../mission-loadouts.md)があります。

このページ群はそれらとは別に、

> 「このItemを拾った／Forgeできるようになった。結局、何に使うのか？」

という**名前起点の検索**へ答えます。

旧Dominions 4 Wikiの個別Itemページにあった「一覧で一言の用途が分かり、個別ページで実戦上の意味まで読める」情報配置を参考にします。ただし旧作の文章・数値は移植せず、Dominions 6の現行仕様を固定データ、公式Manual、Patch notes、ゲーム内表示から確認して書き直します。

---

# この辞典で扱うこと

個別Itemページは、可能な限り次の順で読み切れるようにします。

1. **一言で何をするItemか**
2. **正確な事実データへのLink**
3. **効果が実戦で何を変えるか**
4. **誰に持たせるか**
5. **どんな戦略・Spell・Unitと組み合わせるか**
6. **Forgeする条件／しない条件**
7. **失敗例**
8. **Counter・敵が使った場合の崩し方**
9. **Test gameで確認する項目**

単なる効果一覧ではなく、**仕様 → 攻略上の意味 → Counter**までを一つの見出し語にまとめます。

---

# 数値は個別攻略へ複製しすぎない

要求Path、Construction、Gem cost、Slot、特殊fieldなどの固定値は、原則としてgenerated recordを正本にします。

手書き記事では必要な値だけを文脈として引用し、Patchで変わりやすい表を529ページへ複製しません。

```text
Item名を検索
→ 手書き攻略：何に使うかを理解
→ generated record：現在の固定値を確認
→ 関連する用途別・任務別記事：Build全体へ広げる
```

という役割分担です。

---

# 固定Tier表にはしない

Magic Itemの価値は、

- Nationのnative Magic access
- Forge Bonus
- Research timing
- Gem income
- Mapと地形
- CarrierのStats・Slot
- EnemyのDamage type・MR・Resistance
- Artifactの先着状況
- Multiplayerの外交と戦争Timing

で大きく変わります。

そのため「S Tierだから必ずForge」のような唯一解ではなく、**価値が発生する条件と、価値が消える条件**を書きます。

---

# 掲載Item

現在は、Itemの価値軸が偏らないように、Forge経済・Research・MR攻防・機動・地形接続・Magic Path Booster・Bless転用・属性耐性・Luck・HP / Fatigue継戦・行動Tempo・Battle summon・Thug装備・Artifactの代表例から個別攻略を整備しています。

| 分類 | Item | 一言 | 個別攻略 | 6.35 data |
|---|---|---|---|---|
| Forge経済 | Dwarven Hammer | Forge Bonusを繰り返し使い、将来の総Gem支出を圧縮する | [攻略](dwarven-hammer.md) | [Item 29](../../data/items/by-id/29.md) |
| Research / early | Owl Quill | 5AとForge turnをResearch +6の継続収入へ変換する | [攻略](owl-quill.md) | [Item 322](../../data/items/by-id/322.md) |
| Research / Death | Skull Mentor | C5以降にResearch +14の継続出力を得る | [攻略](skull-mentor.md) | [Item 374](../../data/items/by-id/374.md) |
| Research / high output | Lightless Lantern | Research +12とHorror-related riskを交換する | [攻略](lightless-lantern.md) | [Item 399](../../data/items/by-id/399.md) |
| MR防御 | Amulet of Antimagic | 重要CarrierのMRを補い、MR依存Counterへ備える | [攻略](amulet-of-antimagic.md) | [Item 369](../../data/items/by-id/369.md) |
| MR攻撃 | Spell Focus | MR-negates Spellを高MR Targetへ通しやすくする | [攻略](spell-focus.md) | [Item 370](../../data/items/by-id/370.md) |
| MR攻撃 / high risk | Eye of the Void | Penetration +2とMR -2、眼の置換を交換する | [攻略](eye-of-the-void.md) | [Item 371](../../data/items/by-id/371.md) |
| 機動 / Flying | Winged Shoes | CommanderへFlyingを与え、到達可能性とRaid routeを変える | [攻略](winged-shoes.md) | [Item 294](../../data/items/by-id/294.md) |
| 機動 / Map Move | Boots of the Messenger | Map Move +9とReinvigoration +3で急行と継戦を両立する | [攻略](boots-of-the-messenger.md) | [Item 297](../../data/items/by-id/297.md) |
| 地形接続 / Aquatic | Amulet of the Fish | Aquatic Commanderを陸上へ出し、海中Magic accessを接続する | [攻略](amulet-of-the-fish.md) | [Item 363](../../data/items/by-id/363.md) |
| Path Booster / Death | Skull Staff | Death +1をSpell / Ritual / Summonの新しい閾値へ変える | [攻略](skull-staff.md) | [Item 62](../../data/items/by-id/62.md) |
| Path Booster / Earth | Earth Boots | Earth +1をBattle spell・Ritual・Forgeの閾値へ変える | [攻略](earth-boots.md) | [Item 295](../../data/items/by-id/295.md) |
| Path Booster / Nature | Thistle Mace | Nature +1を片手Slotで組み込み、Nature accessを一段伸ばす | [攻略](thistle-mace.md) | [Item 65](../../data/items/by-id/65.md) |
| Bless転用 | Shroud of the Battle Saint | 非Sacred Carrierへ自国Blessを常時適用する | [攻略](shroud-of-the-battle-saint.md) | [Item 252](../../data/items/by-id/252.md) |
| 属性耐性 / Armor | Elemental Armor | Fire・Cold・Shock Resistance +10をArmor Slotへまとめる | [攻略](elemental-armor.md) | [Item 249](../../data/items/by-id/249.md) |
| Luck / Shield | Lucky Coin | 軽いShield性能とLuckを一つの手Slotへまとめる | [攻略](lucky-coin.md) | [Item 168](../../data/items/by-id/168.md) |
| 継戦 / HP | Ring of Regeneration | Regeneration 10で生物Carrierの生存時間を伸ばす | [攻略](ring-of-regeneration.md) | [Item 382](../../data/items/by-id/382.md) |
| 継戦 / Damage + Fatigue | Girdle of Might | Strength +3とReinvigoration +3を一枠で足す | [攻略](girdle-of-might.md) | [Item 366](../../data/items/by-id/366.md) |
| 継戦 / Fatigue専用 | Amulet of Resilience | Reinvigoration +5で有効行動Roundを伸ばす | [攻略](amulet-of-resilience.md) | [Item 383](../../data/items/by-id/383.md) |
| 行動Tempo | Boots of Quickness | 近接移動と攻撃を速めるが、Spell詠唱は速めない | [攻略](boots-of-quickness.md) | [Item 299](../../data/items/by-id/299.md) |
| Battle summon | Bottle of Living Water | BattleへWater Elemental一体を追加する | [攻略](bottle-of-living-water.md) | [Item 404](../../data/items/by-id/404.md) |
| Thug / Damage | Frost Brand | 一回の命中へAP Cold副次ダメージを重ね、近接火力を増やす | [攻略](frost-brand.md) | [Item 54](../../data/items/by-id/54.md) |
| Thug / Control | Vine Shield | close combatの敵を拘束し、Carrierへ集中する近接行動を乱す | [攻略](vine-shield.md) | [Item 176](../../data/items/by-id/176.md) |
| Thug / Contact punish | Charcoal Shield | Shield防御とFire Resistanceを足し、近接攻撃へ熱反撃を返す | [攻略](charcoal-shield.md) | [Item 173](../../data/items/by-id/173.md) |
| Artifact / maintenance | Igor Könhelm's Tome | Corporeal Undeadの維持とStorm戦を一つのArtifactへまとめる | [攻略](igor-konhelms-tome.md) | [Item 431](../../data/items/by-id/431.md) |
| Artifact / Magic access | The Magic Lamp | 高いA/F accessをAl Khazimという高Path Mageへ変換する | [攻略](the-magic-lamp.md) | [Item 433](../../data/items/by-id/433.md) |

この一覧は固定Tier表ではありません。今後も特殊作戦Item、召喚・変身Item、別PathのBooster、Army支援Item、さらに別のWeapon・Shield・Armor・Crownを、**個別Itemの解説として**順次広げます。

---

# 探し方

## Item名が分かっている

この攻略辞典、または[Magic Item個別record一覧](../../data/items/records.md)から探します。

## Item名が分からない

「Shock Resistanceが欲しい」「Magic Weaponが欲しい」「Reinvigorationが欲しい」なら[用途別Magic Item辞典](../purpose-dictionary.md)から逆引きします。

## 任務が決まっている

「PD Raiderを作る」「Casterを守る」「水中へ侵入する」なら[任務別Magic Item Loadout](../mission-loadouts.md)から必要機能を組みます。

## Artifactを選びたい

先着、Yearning、Carrier Risk、C9 Research投資は[Artifact・Unique Item攻略](../artifacts.md)で判断します。

---

# 執筆時の確認順

個別Itemを追加するときは、少なくとも次を確認します。

1. ゲーム内Item表示・実挙動
2. Illwinter公式Manual / Patch notes
3. pin済みDominions 6.35 Inspector data
4. Community Wiki・実戦知見
5. Test game

古いDom4 / Dom5記事は**論点を発見する資料**として使えますが、Dom6の仕様根拠にはしません。

新しい個別記事は[Magic Item個別攻略Template](../../templates/magic-item-template.md)を起点にできます。
