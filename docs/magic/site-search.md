---
title: Site Search完全ガイド
status: expanding
verified_version: "6.35"
last_verified: "2026-08-15"
---

# Site Search完全ガイド

Site Searchは、Mageを一Turn止めて「何か出れば得をする」作業ではありません。

DominionsにおけるSite Searchは、

> **現在のMage turnを、将来のGem income・Magic diversity・特殊Recruit・Research bonus・戦略拠点へ変換する投資**

です。

強い国家でもSearchが遅れれば、

- Boosterを作れない
- Combat Spell用Gemが足りない
- Summon Mageへ届かない
- Remote attackやGlobalを維持できない
- Site限定Mage・Commanderを見逃す
- 敵より多く領土を持っているのに魔法経済で負ける

という状態になります。

逆に、Mageを過剰に歩かせて全Provinceを高Levelまで重複探索すると、Researchと戦争準備が遅れます。

したがって目標は「全部探す」ではなく、

> **最小のMage turnとGemで、今後の戦略を変えるSiteを十分な確率で回収すること**

です。

---

## 最初に見るページ

- [Magic Site総合索引](../data/sites/index.md)
- [Magic Site Search Level分布](../data/sites/search-levels.md)
- [Remote Site Search Spell](../data/spells/site-search.md)
- [Magic Site Terrain・Location](../data/sites/terrain.md)
- [Magic Site Gem income](../data/sites/gem-income.md)
- [Magic Site Recruit](../data/sites/recruitment.md)
- [Magic Site Research・Ritual bonus](../data/sites/research.md)
- [Site Search運用Playbook](site-search-playbook.md)

データ索引は「何が存在するか」を示し、このページは「いつ、誰で、どこまで探すか」を扱います。

---

# Siteを発見する二つの方法

## Manual Search

MageまたはPriestを対象Provinceへ移動させ、`Search for Magic Sites`を実行します。

Search orderを出したCommanderは、そのTurnを探索に使います。Commanderが持つ各Magic Pathについて、**そのPath Level以下のSite**を発見できます。

例：

```text
F2 A1 E1 Mage
```

が探索すると、同じ一Turnで概ね次を確認します。

```text
Fire：Level 0–2
Air：Level 0–1
Earth：Level 0–1
```

したがって、単一PathのF2 Mageと、F2A1E1 Mageでは、後者の方が一回のSearchから得る情報量が多くなります。

### 同じ探索を繰り返す意味

同じProvinceを、以前と同じPath・同じLevel以下だけで再探索しても、新しく確認できる範囲は増えません。

再探索に意味があるのは、

- 前回より高いPath Levelで探す
- 前回持っていなかったPathを追加する
- PriestでHolyを探す
- Remote SearchでPath全体を確定する
- PatchやMODでSite構成が変わった

場合です。

---

## Remote Search

LaboratoryからRitualをCastし、離れたProvinceを探索します。

単一Path用の代表的なRemote Searchは、対象PathのSiteをSite Levelに関係なく発見します。

現行6.35固定データでは、Fire・Air・Water・Earth・Astral・Death・Nature・Glamour・Bloodの九Pathに、単一Path用Remote Searchがあります。

- Fire：Augury
- Air：Auspex
- Water：Voice of Apsu
- Earth：Gnome Lore
- Astral：Arcane Probing
- Death：Dark Knowledge
- Nature：Haruspex
- Glamour：At the End of the Rainbow
- Blood：Bowl of Blood

さらに、

- `Voice of Tiamat`：海ProvinceのElemental Siteをまとめて探索
- `Acashic Knowledge`：対象Provinceの全Magic Siteを探索

という特殊な広域Searchがあります。

正確なResearch、要求Path、Cost、対象上の注意は[Remote Site Search Spell](../data/spells/site-search.md)を参照してください。

---

# ManualとRemoteの比較

| 観点 | Manual Search | Remote Search |
|---|---|---|
| Gem消費 | なし | あり |
| Mage turn | Search turn | Ritual turn |
| 移動 | 必要 | 不要 |
| 発見深度 | MageのPath Levelまで | 対象Pathを全Level確認 |
| 一度に見るPath | Mageが持つ複数Path | 通常は一Path、特殊Spellは複数 |
| 前線Risk | SearcherをMapへ出す | Lab内に残せる |
| 研究要求 | なし | Spellごとに必要 |
| 主な強み | 序盤・多Path Mage・Gem節約 | 後方Province・高Level取りこぼし・専門化 |
| 主な弱み | 移動とResearch損失 | Gem burn、Ritual casterの機会費用 |

どちらか一方へ統一する必要はありません。

実戦的には、

```text
序盤：多Path MageでManual Search
中盤：不足PathをRemote Search
終盤：新領土をRemoteで高速確認
```

という混合運用が安定します。

---

# Searcherをどう評価するか

Searcherの価値はPath Levelだけでは決まりません。

## 1. Path breadth

一度のSearchで何Pathを確認できるかです。

```text
F1 A1 W1 E1
```

のような広いMageは、各Pathが低くても序盤Searcherとして優秀です。

逆に、

```text
F4
```

だけの高級MageはFireを深く探せますが、他Pathは何も確認しません。

## 2. Path depth

高Level Siteを発見できる深さです。

ただし、Level 4 Siteを探せることと、Level 4まで探すことが常に経済的であることは別です。

- 高Path MageのRecruit bottleneck
- 高級MageのResearch値
- Battle Mageとしての希少性
- Search済みProvince数
- ゲーム残りTurn

を比較します。

## 3. Recruitment bottleneck

首都限定MageやSlow-to-recruit MageをSearchへ回すと、軍事・研究・Path expansionが遅れます。

安いRecruit-anywhere Mage、Indie Mage、召喚した低維持費Mageの方がSearcherとして適する場合があります。

## 4. Strategic mobility

Map Move、Flying、Stealth、Sailing、Forest Survival、Mountain Survival、水陸両用などです。

Searcherは毎Turn、

```text
移動
→ Search
→ 移動
→ Search
```

を繰り返します。

高い移動力があってもSearch自体に一Turn使うため、Route設計が重要です。

## 5. Opportunity cost

Searchに使ったTurnにできなかったことです。

- Research
- Mage recruitmentの護衛
- Forge
- Ritual
- Preach
- Army同行
- Fort建設
- Blood Hunt

特に研究初期は、一人のMageを10Turn歩かせる損失が大きくなります。

## 6. Survivabilityと情報漏洩

前線付近のSearcherは、

- Raider
- Assassin
- Remote attack
- Enemy Scoutによる発見
- Province奪取

で失われます。

高価なMageを裸で国境に置くより、安価なSearcherまたはRemote Searchを使います。

---

# Search Levelをどこまで上げるか

現在の固定データにおけるPath別・Level別record数は[Search Level分布](../data/sites/search-levels.md)で自動集計しています。

重要なのは、record数をそのままMap上の発見率と読まないことです。

実際の出現には、

- Game設定のMagic Site frequency
- Era
- Terrain
- Unique制限
- Capital / National placement
- Throne
- Event
- Plane
- Provinceに既に置かれたSite数

が影響します。

それでも、探索深度の運用原則は作れます。

## Level 1：広く早く

L1 Searchの目的は、全てを見つけることではなく、**安いMage turnでGem economyを起動すること**です。

向いている状況：

- Expansion中
- 多Path L1 Mageがいる
- Researchがまだ浅い
- Remote Search Spellが未解禁
- 首都Gem以外のIncomeを急いで欲しい

L1で何も出なくても、ProvinceにSiteがないとは確定しません。

## Level 2：標準探索

L2は、多くの国家でManual Searchの主力になります。

- 一定の深さ
- 多Path Mageを確保しやすい
- 高級MageほどOpportunity costが高くない
- Remote SearchよりGemを節約できる

というバランスがあります。

## Level 3：重要Pathの仕上げ

L3 Searchは、

- そのPathのGemが戦略の主軸
- 高Level Siteの取りこぼしが痛い
- L3 MageがRecruit-anywhere
- Search済み領土がまとまっている
- Remote SpellよりMage turnの方が安い

場合に行います。

全Provinceを全Path L3にするのではなく、必要Pathを選びます。

## Level 4以上：目的を持って行う

L4以上は「完全探索」という心理的安心のためだけに使わない方がよいです。

判断基準：

- 自国のL4 Mageが量産可能か
- そのMageを戦場から外せるか
- 対象Pathの高Level Siteに固有価値があるか
- Remote Search Spellが安く使えるか
- 残りTurnが十分か
- 新発見Siteを守れるか

高Level Siteが必ず高Gem・強Recruitとは限りません。

---

# どのProvinceから探すか

## 優先度S：安全な新領土の塊

連続した後方ProvinceをRoute化すると、Searcherの移動損失を減らせます。

Frontlineへ一Provinceずつ出入りするより、Expansion Armyが取った領土の後ろを追う形が効率的です。

## 優先度S：戦略を変える可能性があるProvince

- Cave・Underwaterなど特殊Plane
- Unique placement候補
- Throne周辺
- 特殊Recruitを既に確認したProvince
- 異常なScale・Disease・Horror Mark等が見えるProvince
- Fort候補

Siteの一部効果は、発見前からProvinceへ影響していることがあります。

## 優先度A：高Site期待Terrain

Forest、Mountain、Waste、Swamp、Cave、Seaなどは一般に探索価値が高い傾向があります。

ただし、

> ForestだからNatureだけ

のように一Pathへ限定しません。

TerrainはSite候補を変えますが、同じTerrainにも複数PathのSiteがあります。実際の配置候補は[Terrain・Location索引](../data/sites/terrain.md)で確認できます。

## 優先度A：Fort・Lab計画地

発見したSiteが、

- Mage recruitment
- Research bonus
- Ritual bonus
- Fort / Lab
- Resource / Recruitment Point

を持つ場合、建設計画が変わります。

Fortを建て終えてからSiteを見つけるより、建設判断前にSearchする価値があります。

## 優先度B：国境・前線

価値は高い一方、Searcherを失いやすい場所です。

- 先にScout ringを置く
- Search後すぐ退避する
- Cheap Mageを使う
- Remote Searchへ切り替える
- Armyと同行する

などの安全策を取ります。

## 優先度C：孤立した低価値Province

Searchしないのではなく、後回しにします。

- 戦争前のResearchが必要
- Searcherが遠回りになる
- Provinceを維持できない
- 残りTurnが少ない

場合は、未探索のままでも合理的です。

---

# Path別の探索方針

## Fire

Fire Gemは直接Damage、Elemental、Battlefield effect、Forgeへ使いやすく、戦争前に不足しやすい資源です。

F1–2の広域Mageが少ない国家では、AuguryによるRemote Searchへ移りやすいPathです。

## Air

Air Gemは移動、Lightning、Air Elemental、Storm系、装備へ集中しやすく、少量の追加収入でも戦術が増えます。

Air Mageが高価・脆弱な国家では、前線へ歩かせずAuspexを使う価値があります。

## Water

地上と水中で探索手段が分かれます。

- 地上：Manual SearchまたはVoice of Apsu
- 水中：Manual Search、各Path Remote Search、またはVoice of Tiamat

Voice of Tiamatは高コストですが、海ProvinceのElemental Pathを一度に調べられます。海領土が広いほど一Castあたりの情報価値が上がります。

## Earth

Earth GemはBooster、Forge discount、Army buff、Fort攻防へ直結します。

Mountain・Cave・高Resource Fort候補とSearch Routeを重ねると、Site発見と建設判断を同時に進められます。

## Astral

Astral PearlはAlchemy、Communion、Teleport、Dispel、Magic Duel対策など用途が広い資源です。

Arcane Probingは低要求Pathで使えますが、Pearlの用途が多いため、序盤の連打は他の戦略を圧迫します。

Acashic Knowledgeは全Pathを一度に確定できますが高価です。通常の空白Provinceへ無差別にCastするより、

- 多数のPathが未探索
- 高価値Terrain
- 遠隔地でManual Searchが困難
- 重要Fort・Throne周辺

のようなProvinceへ使います。

## Death

Death Gemは召喚、Reanimation、Remote attack、Thug chassisへつながります。

D1 Mageが安く、Dark Knowledgeも低要求であるため、ManualとRemoteの比較がしやすいPathです。

## Nature

Nature GemはSupply、Regeneration、Poison、Army buff、Vine系召喚へ使います。

Forest・Swampだけに限定せず、広い領土を多Path Searcherで先に調べ、残りをHaruspexで埋める運用が効率的です。

## Glamour

GlamourはIllusion、Stealth、Morale、Movement、特殊召喚へ関係します。

Glamour Mageを戦場や偵察から外しにくい国家では、At the End of the Rainbowによる後方Searchが有力です。

## Blood

Blood SiteはBlood economyの補助になりますが、Blood SlaveにはBlood Hunt、Summon、Sabbath、Combat Spellという競合用途があります。

Bowl of Bloodを使う際は、

- そのProvinceのBlood Searchが未確認
- Blood Slave輸送が安定
- Hunter turnよりRitual turnが余る
- 前線でない

ことを確認します。

Blood HuntとSite Searchは同じものではありません。PopulationからSlaveを取ることと、Blood PathのMagic Siteを発見することを分けて管理します。

## Holy

PriestはHoly SiteをManual Searchできます。

現行のResearch可能Spell setでは、通常の九Pathに対応するeffect 48型の**Holy専用Remote Search**を確認していません。

Holy Siteを完全に調べたい場合は、

- H1–H4 PriestのManual Search
- Acashic Knowledge等の全Path探索
- 特殊Event・Site処理

を使います。

Prophetや高位PriestのTurnはClaim、Preach、Army supportにも必要なので、Holy Searchの機会費用は高くなりやすい点に注意します。

---

# Search economyの考え方

## 単純な回収Turn

毎Turn1 Gemを生むSiteを、残り30Turnで発見したなら、理論上の総収入は30 Gemです。

ただしSearch投資には、

- Mage turn
- 移動Turn
- Remote SpellのGem
- Researchの遅れ
- SearcherのUpkeep
- Searcher喪失Risk

があります。

簡易式：

```text
期待価値
= 発見確率 ×（毎Turn収入 × 残りTurn + 特殊効果価値）
- Gem cost
- Mage turn価値
- 移動・Risk cost
```

正確な金額へ変換する必要はありません。

比較可能な形にすることが目的です。

## Gem income以外の価値

Siteの価値をGemだけで判断すると、最重要Siteを見落とします。

- 新しいMage Path
- Site限定Mage・Commander
- Research bonus
- Ritual bonus
- Forge関連
- Fort・Lab
- Province income / Resource
- Supply
- Scry / Adventure / Void Gate
- Scale / Dominion
- Throne

特に、国家が持たないPathのMageをRecruitできるSiteは、1 Gem/Turnより大きな戦略価値を持つことがあります。

---

# Search coverageを記録する

記憶だけで運用すると、重複Searchと未探索Provinceが増えます。

最低限、Provinceごとに次を記録します。

```text
Province：
所有状態：
Terrain：
Manual Search済：F2 A1 W0 E2 S0 D1 N2 G0 B0 H1
Remote Search済：A / S
発見Site：
最後にSearchしたTurn：
次に必要なSearch：W2, G2
Fort / Lab計画：
Risk：
```

重要なのは、単なる「Search済み」ではなく、

> **何Pathを何LevelまでSearch済みか**

です。

---

# Multiplayerでの注意

## Searcherは軍事情報になる

国境でF2A2 Mageが歩いていれば、敵は、

- その国家のPath access
- Research・戦闘Mageの不足
- Search Route
- 価値ある後方Province

を推測できます。

Stealthy Searcherでも、Patrolや戦闘で発見される可能性があります。

## 発見情報が共有されるSpell

一部のSearch Spellは、対象Provinceにいる他勢力へSite発見情報が伝わる特殊性があります。

特にVoice of ApsuとVoice of Tiamatは、Spell説明上、対象Province内の住民・Commanderへ発見情報が共有されます。

中立・敵対・同盟勢力が同じProvinceへ関与している状況では、情報漏洩を考えます。

## 敵領土のSearch

Remote Search Spellごとに、敵Provinceを対象にできるかが違います。

Spell説明、Targeter、Ritual rangeを確認し、

- 敵Provinceを指定できる
- Friendly Provinceのみ
- 敵Province不可
- 水中限定
- 地上限定

を混同しないでください。

## RaidとGem connection

Siteを発見しても、Provinceを失えば利益は敵へ移ります。

さらにFriendly ProvinceからLabまでの接続を切られると、Siteを保持していても回収・補給が不安定になります。

Search計画と同時に、

- Scout ring
- PD
- Fort
- Lab
- Retreat route
- Connection defence

を設計します。

---

# よくある失敗

## 全てをL3–4で探すまで満足しない

完全性のためにResearchを失います。最初は広く浅く、重要Pathだけ深くします。

## 高級MageをSearchへ出し続ける

首都限定Mage、High Priest、Communion Master、Battle Mageが不足します。

## 同じProvinceを重複Searchする

Search coverageを記録せず、同じPath・同じLevelを何度も確認します。

## Terrainを一Pathへ決めつける

ForestをNatureだけ、MountainをEarthだけと考え、他Pathを取りこぼします。

## Remote SearchをGemだけで嫌う

Mageの移動Turn、Research、前線Riskを無視します。

## Remote Searchを無差別に連打する

Pearl・Gemを使い切り、Booster、Battle Spell、Summonが止まります。

## Siteを見つけて終わる

Recruit条件、Lab、国家制限、Enter order、Fort化、守備を確認しません。

## Searchが遅すぎる

残りTurnが少ないと、1 Gem/Turn Siteを見つけても投資を回収できません。

---

# 実戦用判断フロー

```text
新しいProvinceを獲得
    ↓
安全な後方Routeに入るか？
    ├ Yes → 多Path MageでManual Search
    └ No  → Scout / Armyで安全確認、またはRemote Search
    ↓
主要PathをL1–2まで確認したか？
    ├ No  → 広いMageを優先
    └ Yes → 不足Pathだけ追加
    ↓
そのPathのGemが戦略のボトルネックか？
    ├ Yes → L3またはRemote Searchで仕上げ
    └ No  → 後回し
    ↓
Fort・Throne・特殊Terrain・異常効果があるか？
    ├ Yes → 高Level / 全Path Searchを検討
    └ No  → 次のProvinceへ
```

---

# 国家攻略へ書く項目

各国家ページには、Site Searchについて次を記載すると実用的です。

```text
主なManual Searcher：
Search breadth：
標準Search Level：
不足Path：
最初に解禁するRemote Search：
Gem bottleneck：
首都周辺Search開始Turn：
戦争前に確保したいGem income：
水中・Cave対応：
Holy Searcher：
Searcherを戦場へ戻すTiming：
```

国家の強さは、Path accessだけでなく、そのPathをMap全体へ効率よくSearchできるかでも変わります。

---

## 関連ページ

- [Site Search運用Playbook](site-search-playbook.md)
- [Magic Site Search Level分布](../data/sites/search-levels.md)
- [Remote Site Search Spell](../data/spells/site-search.md)
- [Magic Site総合索引](../data/sites/index.md)
- [Magic Site Terrain・Location](../data/sites/terrain.md)
- [Magic Site Gem income](../data/sites/gem-income.md)
- [GemとBlood Slave](gems.md)
- [Researchと研究ルート](research.md)
- [Province](../systems/province.md)
- [Forts](../systems/forts.md)
- [Throne of Ascension](../systems/thrones.md)

## 主な参照先

- [Dominions 6 Manual](https://www.illwinter.com/dom6/dom6manual.pdf)
- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- [Magic Site総合データ](../data/sites/index.md)

!!! warning "実機確認"
    Search Spellの対象可否、Ritual range、海・陸制限、発見通知、特殊Siteの可視状態、Globalによる探索はSpell・Site固有処理を含みます。最終的なTargeterと結果はゲーム内6.35の表示・実機挙動を優先してください。
