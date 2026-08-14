---
title: 情報源
last_verified: "2026-08-14"
---

# 情報源

攻略記事を書く際の主要な参照先です。

## 優先順位

1. Dominions 6 ゲーム内表示・実機挙動
2. Illwinter公式Manual・Change log・Patch notes・Modding Manual
3. ゲームデータ抽出
4. Community Wiki・Guide
5. Battle Replay・Test game・対戦知見

## 公式資料

- Illwinter Game Design公式サイト
- Dominions 6 Manual
- Dominions 6 Change log / Steam公式Announcement
- Dominions 6 Modding Manual

Unit生成系Commandの意味は、公式Modding ManualのMonster Summoning、Shape Changing、Nation Reanimation節を優先します。とくに`domsummon`、`makemonsters`、`summon`、`battlesum`、`batstartsum`、`templetrainer`、`reanimator`、`autoundead`等は、CSV列名だけでTimingや確率を推測しません。

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

### Unit装備・Mount結合

Recruitページでは`BaseU.csv`の次の参照をWeapon・Armor・Unit dataへ結合します。

- `wpn1`～`wpn7`: Weapon record
- `armor1`～`armor4`: Armor record
- `mountmnr`: Mount側のUnit record

結合に利用する主な追加ファイル:

- `gamedata/weapons.csv`
- `gamedata/effects_weapons.csv`
- `gamedata/effects_info.csv`
- `gamedata/special_damage_types.csv`
- `gamedata/attributes_by_weapon.csv`
- `gamedata/armors.csv`
- `gamedata/protections_by_armor.csv`
- `gamedata/attributes_by_armor.csv`
- `gamedata/attribute_keys.csv`

生成物では、Unit基礎能力とは別に、WeaponのDamage・Attack / Precision・Length / Range・AP / AN・Secondary effect、ArmorのProtection・Parry・Encumbrance、MountのHP・Protection・攻撃・防具を表示します。

!!! note "RiderとMount"
    Mountは装備品ではなく別Unit recordです。RiderとMountのHP、Protection、Defence、武器、防具を分離して表示します。Dismount後の完全なShape切替やTarget分配は自動表だけでは再構成しません。

### Unit総合・入手経路索引

BaseUの全4,091 Unit recordを個別ページ化し、明示的な参照を取得・利用経路として結合します。

#### 通常Recruit

- Fort troop / commander mapping
- Fort不要・地形・外国Recruit mapping
- Coastal Recruit mapping

#### Hero

- `gamedata/attributes_by_nation.csv`
- Attribute 139～144: `hero1`～`hero6`
- Attribute 145～146: `multihero1`～`multihero2`

Hero属性名は`gamedata/attribute_keys.csv`で確認します。

#### Pretender chassis

- `gamedata/pretender_types_by_nation.csv`

`monster_number`と`nation_number`を対応付け、国家ごとの選択可能Chassisを逆引きします。

#### Spell summon

- `gamedata/spells.csv`
- `gamedata/effects_spells.csv`
- `gamedata/attributes_by_spell.csv`

Research可能なroot Spellから`next_spell` chainを辿り、Summon、Summon commander、Farsummon等の明示effectが正の固定Unit IDを参照するときだけ対応付けます。負値のRandom pool、内部sentinel、未解明effectは推測で補完しません。

#### Magic Site Unit

- `gamedata/MagicSites.csv`
- `mon1..5` / `com1..5`
- `hmon1..5` / `hcom1..5`
- `sum1..4` / `n_sum1..4`
- `natmon` / `natcom`

抽出列名とUnit IDを事実として掲載します。Siteの発見条件、国家制限、特殊出現処理はゲーム内Site詳細を優先します。

### Unit自身の生成・召喚・Recruit解禁

`BaseU.csv`の次の固定Target参照を追跡します。

#### Strategic Map

- `domsummon` / `domsummon2` / `domsummon20` / `raredomsummon`
- `templetrainer`
- `makemonster` + `n_makemonster`
- `summon` + `n_summon`
- `summon5`
- `autosum` + `n_autosum`
- `coldsummon` / `turmoilsummon`
- `slaver` + `slaverbonus`

#### Battle

- `batstartsum1..5`
- `batstartsum1d3`
- `batstartsum1d6..9d6`
- `battlesum1..5`
- `battlesum1d2` / `battlesum1d3`
- `battlesumwarm`

同系統Fieldにsuffixが付く複数Slotも抽出します。

#### Recruit unlock

- `ownsmonrec`
- `monpresentrec`

#### 固定変換・復活

- `mummify` / `mummification`
- `twiceborn`
- `lich`
- `animatemnr`
- `raiseshape`

正の値がBaseUのUnit IDへ解決できる場合だけ、生成先・変換先Unitへ逆引きします。

#### Random pool

公式Modding Manualが定義するNegative Monster Number（`-2`～`-26`）と、`-1000`以下のMontag参照はRandom poolです。単一Unitへは結び付けず、raw valueとpool名を別索引に残します。

### Targetを直接指定しないUnit能力

固定生成先を安全に確定できないため、能力Flagとして掲載します。

- `reanimator` / `preanimator` / `dreanimator`
- `raiseonkill`
- `onisummon`
- `ivylord` / `dragonlord` / `lamialord` / `corpselord`
- `faysummon`
- Elemental summon bonus

Reanimation先、corpse条件、Priest level、国家固有結果を能力Flagだけから推測しません。

### 国家Freespawn・Reanimation

`gamedata/attributes_by_nation.csv`のAttribute番号を、`gamedata/attribute_keys.csv`に含まれる`{Ntn: #command}`表記へ接続します。

対象Command:

- `autoundead`
- `guardspirit`
- `priestreanim` / `undeadreanim`
- `horsereanim` / `wightreanim`
- `tombwyrmreanim` / `manikinreanim`
- `supayareanim` / `greekreanim` / `ghostreanim`

`guardspirit`が正の固定Unit IDを指す場合だけUnitへ逆引きします。負値Montagやhard-coded Reanimation結果は固定Unitとして扱いません。

### Mount・Shape relation

#### 直接Unit IDを持つShape

- `shapechange`
- `firstshape` / `secondshape` / `secondtmpshape`
- `landshape` / `watershape`
- `forestshape` / `plainshape`
- `homeshape` / `foreignshape`
- `domshape` / `notdomshape`
- `springshape` / `summershape` / `autumnshape` / `wintershape`
- `battleshape` / `worldshape`
- `prophetshape`
- `twiceborn` / `lich` / `animatemnr` / `raiseshape`

#### Targetが別Field・規則で決まるShape

- `xpshape` / `labxpshape`: 値はXP threshold。Targetは`xpshapemon`、未指定なら次のUnit ID
- `growhp`: 値はHP threshold。Targetは一つ前のUnit ID
- `shrinkhp`: 値はHP threshold。Targetは次のUnit ID

以前の単純抽出のように、`xpshape`のthresholdや`cleanshape`のbooleanをUnit IDとして扱いません。

MountとShapeは直接入手経路とは区別し、Unit間関係として掲載します。

!!! note "未分類Unit"
    現在の索引で入手経路を確認できないUnitを「入手不能」とは断定しません。Event、Wish、Random summon table、hard-coded Reanimation、Scenario、特殊国家内部処理等が未索引である可能性があります。未解決参照は[Unit索引データ品質](../data/units/data-quality.md)へ残します。

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

!!! warning "自動生成データの限界"
    - Unit Costは自動計算、Mount、形態変化、特殊Recruit条件が複雑なため、自動Unit索引では表示しません。
    - Unit loadoutはWeapon / Armor参照を示しますが、最終Damage、二刀流Penalty、攻撃順、Conditional attackを完全には再構成しません。
    - Hero・Pretender・Spell・Site・Unit generationの対応は明示参照だけを採用し、名前や説明文から推測しません。
    - Event、Wish、Random table、hard-coded Reanimation等は未分類に残る場合があります。
    - Spellの複合効果、特殊Range / AoE、Target制限はゲーム内詳細を優先します。
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
