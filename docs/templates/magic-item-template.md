---
title: Magic Item個別攻略Template
page_type: template
status: reviewed
---

# Magic Item個別攻略Template

Magic ItemをItem名から引く手書き攻略辞典へ追加するときのTemplateです。

固定値を大量に転記せず、該当するgenerated recordへ接続した上で、**仕様 → 攻略上の意味 → Counter**を書きます。

## Front Matter

新しい個別攻略には`title`、`status`、確認した`verified_version`、そしてgenerated recordと接続する`item_id`を持たせます。

`item_id`はItem名の表記揺れに依存しない識別子です。同じItem IDを複数の個別攻略ページへ割り当てません。

## 一言要約

冒頭に、そのItemが**何を可能にするか**を一文で書きます。

「強力なArtifact」だけでは不足です。「高いA/F accessを高Path Mageへ変換し、Earth / Astral側へMagic ceilingを伸ばす」のように、用途と判断軸が一文でも分かることを目標にします。

## まず何ができるか

要求Path、Construction、主要効果など、判断に必要な固定値を最小限だけ説明します。

完全な表はgenerated recordへ任せ、Patchで変わる数値を手書きページへ大量複製しません。

## 効果の実戦上の意味

能力名の言い換えではなく、次を説明します。

- 何に勝てるようになるか
- 何が新しく可能になるか
- どの弱点を埋めるか
- どの条件では能力が働かないか

## 誰に持たせるか

Carrierを単純なStats順ではなく、Raider、Battlefield caster、Forge / Ritual carrier、Army support、Thug / SC、特殊作戦などの役割で考えます。

Slot競合とCarrier死亡時のRiskも書きます。

## 組み合わせ

Spell、Unit、別Item、Army、Research route、Magic accessとのsynergyを書きます。

固定Buildを唯一解として扱わず、成立条件と代替手段を残します。

## Forgeする条件

「どんな国家・戦況なら、このItemへResearch、Gem、Forge turnを払う価値が高いか」を書きます。

## Forgeしない・後回しにする条件

代替Item、Research timing、Carrier不足、Enemy composition、Gem economyなど、価値が消える条件も同じ重さで扱います。

## Counter

敵が使った場合に、Carrierを倒す、効果条件を外す、Resistance / MRを積む、Slot競合を突く、Research / Gem / Forge hubを攻める、といった別軸からの崩し方を書きます。

## よくある失敗

仕様の読み違い、過剰投資、Carrier選択、Timing、Scriptなど、実際に起きる失敗を具体化します。

## Test game checklist

少なくとも、ゲーム内Item表示、Forge要求Path、実支払Cost、特殊効果の発動条件、Carrierとの相互作用、Counter条件を小さなTest gameで確認します。

## Source note

情報源は、ゲーム内表示と実挙動、Illwinter公式Manual・Patch notes、pin済みDom6 Inspector、Community資料の順に区別します。

Community資料を使った特殊挙動は、固定仕様と断定せずTest対象を明示します。

## 書かないこと

- 旧作Wiki本文のコピー
- Patchで変わる数値表の大量複製
- 根拠のない固定Tier
- 「とにかく強い」で終わる評価
- Carrier・Research・Gem economyを無視したBuild推奨
- Counterのない一方向の紹介

[Magic Item攻略辞典へ戻る](../items/encyclopedia/index.md)
