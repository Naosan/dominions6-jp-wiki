---
title: 情報源
last_verified: "2026-08-14"
---

# 情報源

攻略記事を書く際の主要な参照先です。

## 優先順位

1. Dominions 6 ゲーム内表示・実機挙動
2. Illwinter公式Manual・Change log・Patch notes
3. ゲームデータ抽出
4. Community Wiki・Guide
5. Battle Replay・Test game・対戦知見

## 公式資料

- Illwinter Game Design公式サイト
- Dominions 6 Manual
- Dominions 6 Change log / Steam公式Announcement
- Dominions 6 Modding Manual

## データ索引

- Dominions 6 Mod Inspector
- Inspectorのvanilla CSV data
- ゲーム内Unit / Spell / Item popup

自動生成索引は、Dominions 6.35対応のDom6 Inspector commit
`cfac4311bc0b58053b8dead7bffbc036ba9bd5dc` を固定データ源として生成します。

### 国家カタログ

国家名、Epithet、Nation ID、Eraは、Mod Inspectorの `gamedata/nations.csv` と照合し、リポジトリ内の `data/nations.tsv` にスナップショットとして保存します。

現在の登録数:

- Early Age: 35
- Middle Age: 37
- Late Age: 31
- 合計: 103

### Recruit・Commander・Mage索引

主に利用するファイル:

- `gamedata/BaseU.csv`
- `gamedata/fort_troop_types_by_nation.csv`
- `gamedata/fort_leader_types_by_nation.csv`
- `gamedata/nonfort_troop_types_by_nation.csv`
- `gamedata/nonfort_leader_types_by_nation.csv`
- `gamedata/coast_troop_types_by_nation.csv`
- `gamedata/coast_leader_types_by_nation.csv`

生成物には、Unit ID、基礎能力値、固定Magic Path、Random Path、Sacred・Flying・Stealthyなどの主要タグを掲載します。

### Spell索引

主に利用するファイル:

- `gamedata/spells.csv`
- `gamedata/effects_spells.csv`
- `gamedata/attributes_by_spell.csv`

生成物にはSpell ID、Research、要求Path、Combat / Ritual、Cost、Fatigue、Range、AoE、主要Effect、National / Realm restrictionを掲載します。

Range、AoE、Fatigueは抽出上の数式を読みやすく整形したものです。複合Effect、特殊Target、Caster level依存、Battlefield条件は表だけで完全に表現できない場合があります。

### Magic Item索引

主に利用するファイル:

- `gamedata/BaseI.csv`
- `gamedata/weapons.csv`
- `gamedata/armors.csv`

生成物にはItem ID、Slot / Type、Construction、Forge要求Path、基礎Gem Cost、Booster、参照武器・防具、主要能力、National restrictionを掲載します。

Gem CostはInspector本体と同じ基礎Forge Cost表とItem固有modifierを使います。実際の消費量はForge Bonus、Dwarven Hammer、国家割引などで変わります。

### Weapon・Armor・Damage索引

主に利用するファイル:

- `gamedata/weapons.csv`
- `gamedata/effects_weapons.csv`
- `gamedata/effect_modifier_bits.csv`
- `gamedata/effects_info.csv`
- `gamedata/special_damage_types.csv`
- `gamedata/attributes_by_weapon.csv`
- `gamedata/armors.csv`
- `gamedata/protections_by_armor.csv`
- `gamedata/attributes_by_armor.csv`
- `gamedata/attribute_keys.csv`

Weapon索引では、Damage、Attack / Precision、Defence、Length / Range、攻撃回数、Strength加算、Slash / Pierce / Blunt、Elemental属性、AP / AN、MR判定、Secondary effect等を整理します。

Armor索引では、Protection zoneからInspectorと同じ表示用Body Protectionを算出し、Shield Protection、Parry、Defence penalty、Encumbrance、Map movement penaltyを分離して掲載します。

!!! note "Magic weaponとMagic damage"
    Weapon modifier上の`Nonmagical`の有無と、`Magic Damage` modifierは別項目です。前者はEthereal等への命中、後者はDamage分類へ関係します。自動索引でも別々に表示します。

!!! warning "自動生成データの限界"
    - Unit Costは自動計算、Mount、形態変化、特殊Recruit条件が複雑なため、Recruit索引では表示しません。
    - Spellの複合効果、特殊Range / AoE、Target制限はゲーム内詳細を優先します。
    - Itemの発動Spell、特殊な装備条件は自動表だけでは完全に表せません。
    - Weapon recordだけでは装備者のStrength、Ambidextrous、Mount、Bless、Buff、Fatigueを含む最終性能は分かりません。
    - Armor recordはUnitのNatural Protection、複数装備、Shield Hit、Buffを含みません。
    - National / Realm restriction、Event、Hero、Site限定、形態変化は追加確認が必要です。
    - Inspectorは非常に有用ですが、抽出・表示上の不具合があり得ます。最終的な数値・挙動はゲーム内表示と実機テストを優先します。

## Community資料

- illwiki Dominions 6
- 旧Dominions日本語Wiki
- プレイヤーGuide、動画、対戦記録

Community資料は戦術の発見に有用ですが、Dom4 / Dom5の数値やResearch LevelをDom6へそのまま移植しません。

## 出典の書き方

重要な数値・Research Level・Path要求など、Patchで変わりやすい情報には次を残します。

- 確認Version
- 確認日
- ゲーム内か外部データか
- 必要なら検証方法

攻略評価では、前提となるMap、相手、研究時期、Gem消費、Scriptも併記します。
