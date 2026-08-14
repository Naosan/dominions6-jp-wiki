#!/usr/bin/env python3
"""Generate Dominions 6 nation recruit and mage-access reference pages.

Source: a pinned Dominions 6.35 snapshot from larzm42/dom6inspector.
Generated pages are factual indexes; strategy remains in docs/nations/.
"""
from __future__ import annotations

import argparse, csv, re, sys, time, unicodedata
import urllib.error, urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data/nations.tsv"
OUT = ROOT / "docs/data/recruitment"
MAGE_OUT = ROOT / "docs/data/mage-access.md"
COMMIT = "cfac4311bc0b58053b8dead7bffbc036ba9bd5dc"
BASE = f"https://raw.githubusercontent.com/larzm42/dom6inspector/{COMMIT}/gamedata"
CACHE = ROOT / ".cache/dom6inspector" / COMMIT
FILES = (
    "BaseU.csv", "fort_troop_types_by_nation.csv",
    "fort_leader_types_by_nation.csv", "nonfort_troop_types_by_nation.csv",
    "nonfort_leader_types_by_nation.csv", "coast_troop_types_by_nation.csv",
    "coast_leader_types_by_nation.csv",
)
ERAS = {"1": ("EA", "ea", "Early Age"), "2": ("MA", "ma", "Middle Age"), "3": ("LA", "la", "Late Age")}
BY_CODE = {v[0]: v for v in ERAS.values()}
PATHS = "FAWESDNGBH"
MASKS = ((128,"F"),(256,"A"),(512,"W"),(1024,"E"),(2048,"S"),(4096,"D"),(8192,"N"),(16384,"G"),(32768,"B"),(65536,"H"))


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"['’]", "", s.replace("&", " and "))).strip("-")


def esc(v) -> str:
    return str(v or "").replace("|", "\\|").replace("\n", " ")


def num(r, k, default=0) -> int:
    try: return int(float(r.get(k) or default))
    except ValueError: return default


def yes(r, k) -> bool:
    return r.get(k) not in (None, "", "0", "0.0")


def tsv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def source(name: str, refresh: bool, offline: bool) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / name
    if p.exists() and p.stat().st_size and not refresh: return p
    if offline: raise FileNotFoundError(f"offline cache missing: {p}")
    req = urllib.request.Request(f"{BASE}/{name}", headers={"User-Agent":"dominions6-jp-wiki/1.0"})
    err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as response: data = response.read()
            if not data: raise RuntimeError("empty download")
            p.write_bytes(data); return p
        except (urllib.error.URLError, TimeoutError, RuntimeError) as ex:
            err = ex; time.sleep(2 ** attempt)
    raise RuntimeError(f"download failed: {name}: {err}")


def nations():
    rows = tsv(CATALOG); out = []
    for r in rows:
        raw = r["era"].strip()
        code, directory, title = ERAS.get(raw, BY_CODE.get(raw, (None,None,None)))
        if not code: raise ValueError(f"unknown era: {raw}")
        out.append({**r, "id":int(r["id"]), "code":code, "dir":directory, "era_name":title, "slug":slugify(r["name"])})
    if len({r["id"] for r in out}) != len(out): raise ValueError("duplicate nation id")
    if len({(r["code"],r["slug"]) for r in out}) != len(out): raise ValueError("duplicate nation slug")
    return out


def unit_data(path: Path):
    data = {int(r["id"]):r for r in tsv(path) if r.get("id")}
    if len(data) < 4000: raise ValueError(f"BaseU incomplete: {len(data)}")
    return data


def mapping(path: Path):
    d = defaultdict(list)
    for r in tsv(path):
        if r.get("monster_number") and r.get("nation_number"):
            d[int(r["nation_number"])].append(int(r["monster_number"]))
    return d


def fixed(r):
    return {p:num(r,p) for p in PATHS if num(r,p)>0}


def randoms(r):
    out=[]
    for i in range(1,7):
        mask=num(r,f"mask{i}")
        pool="".join(p for bit,p in MASKS if mask & bit)
        if pool: out.append((max(1,num(r,f"nbr{i}",1)), num(r,f"rand{i}",100) or 100, max(1,num(r,f"link{i}",1)), pool))
    return out


def fixed_text(r):
    return " ".join(f"{p}{v}" for p,v in fixed(r).items()) or "—"


def random_text(r):
    return "; ".join(f"{n}×{chance}% +{level} [{'/'.join(pool)}]" for n,chance,level,pool in randoms(r)) or "—"


def cap(r): return yes(r,"capitalhome")

def mage(r): return bool(fixed(r) or randoms(r) or yes(r,"researchbonus"))


def tags(r):
    specs=(("holy","Sacred"),("mounted","Mounted"),("flying","Flying"),("spy","Spy"),("assassin","Assassin"),("heal","Healer"),("mastersmith","Master Smith"),("undead","Undead"),("demon","Demon"),("magicbeing","Magic Being"),("inanimate","Lifeless"),("animal","Animal"),("aquatic","Aquatic"),("amphibian","Amphibious"),("pooramphibian","Poor Amphibian"),("glamour","Glamour"),("spellsinger","Spellsinger"))
    out=[label for key,label in specs if yes(r,key)]
    if num(r,"mor")==50 and "Mindless" not in out: out.append("Mindless")
    for key,label in (("stealthy","Stealth"),("forgebonus","Forge"),("douse","Blood Search"),("formationfighter","Formation Fighter"),("bodyguard","Bodyguard"),("patrolbonus","Patrol"),("siegebonus","Siege"),("castledef","Castle Def"),("resources","Resources"),("supplybonus","Supply"),("reclimit","Rec limit")):
        if yes(r,key): out.append(f"{label} {num(r,key):+d}")
    if num(r,"rt")==2 or yes(r,"slowrec"): out.append("Slow to recruit")
    return out[:8]


def rows(ids, units):
    out=[]; seen=set()
    for uid in ids:
        if uid in seen: continue
        seen.add(uid)
        if uid not in units: raise KeyError(f"mapped unit {uid} missing from BaseU")
        out.append(units[uid])
    return out


def val(r,k): return r.get(k) or "—"


def troop_table(items):
    if not items: return "該当データなし。\n"
    out=["| Unit | ID | Size | HP | Prot | MR | Mor | Str | Att | Def | 主な属性 |","|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for r in items:
        out.append(f"| {esc(r.get('name','(unnamed)'))} | {r['id']} | {val(r,'size')} | {val(r,'hp')} | {val(r,'prot')} | {val(r,'mr')} | {val(r,'mor')} | {val(r,'str')} | {val(r,'att')} | {val(r,'def')} | {esc(', '.join(tags(r)) or '—')} |")
    return "\n".join(out)+"\n"


def commander_table(items):
    if not items: return "該当データなし。\n"
    out=["| Commander | ID | Leadership N/U/M | Guaranteed | Random | 主な属性 |","|---|---:|---|---|---|---|"]
    for r in items:
        lead=f"{val(r,'leader')}/{val(r,'undeadleader')}/{val(r,'magicleader')}"
        out.append(f"| {esc(r.get('name','(unnamed)'))} | {r['id']} | {lead} | {esc(fixed_text(r))} | {esc(random_text(r))} | {esc(', '.join(tags(r)) or '—')} |")
    return "\n".join(out)+"\n"


def section(title, troop_ids, leader_ids, units, split=False):
    troops,leaders=rows(troop_ids,units),rows(leader_ids,units); out=[f"## {title}",""]
    if split:
        for heading,items,renderer in (("Recruit-anywhere troops",[r for r in troops if not cap(r)],troop_table),("Capital-only troops",[r for r in troops if cap(r)],troop_table),("Recruit-anywhere commanders",[r for r in leaders if not cap(r)],commander_table),("Capital-only commanders",[r for r in leaders if cap(r)],commander_table)):
            out += [f"### {heading}","",renderer(items)]
    else:
        out += ["### Troops","",troop_table(troops),"### Commanders","",commander_table(leaders)]
    return "\n".join(out).rstrip()+"\n"


def mage_summary(items):
    out=[]
    for r in items:
        if not mage(r): continue
        text=f"{r.get('name','(unnamed)')}: {fixed_text(r)}"
        if random_text(r)!="—": text += f"; {random_text(r)}"
        out.append(text)
    return " / ".join(out) or "—"


def nation_page(n, units, maps):
    ft,fl=maps["ft"].get(n["id"],[]),maps["fl"].get(n["id"],[])
    nt,nl=maps["nt"].get(n["id"],[]),maps["nl"].get(n["id"],[])
    ct,cl=maps["ct"].get(n["id"],[]),maps["cl"].get(n["id"],[])
    fort_leaders=rows(fl,units); all_leaders=rows(fl+nl+cl,units)
    any_fort=[r for r in fort_leaders if not cap(r)]; capital=[r for r in fort_leaders if cap(r)]
    s=f'''---
title: "{n['code']} {n['name']} Recruitデータ"
status: generated
verified_version: "6.35"
nation_id: {n['id']}
generated_from: "dom6inspector {COMMIT}"
---

# {n['code']} {n['name']} — Recruitデータ

> **{n['epithet']}**

[国家攻略ページへ戻る](../../../nations/{n['dir']}/{n['slug']}.md)

!!! info "自動生成データ"
    Dominions 6.35対応の固定スナップショットから生成した「何を雇えるか」の索引です。Unitの評価・生産比率・研究方針は国家攻略で扱います。

## 概要

| 項目 | 内容 |
|---|---|
| Era | {n['era_name']}（{n['code']}） |
| Nation | {n['name']} |
| Epithet | {n['epithet']} |
| Nation ID | {n['id']} |
| Any-fort magic | {esc(mage_summary(any_fort))} |
| Capital magic | {esc(mage_summary(capital))} |
| 全Recruit commander数 | {len(all_leaders)} |

### 表の読み方

- **Leadership N/U/M**: 通常 / Undead / Magic leadership。
- **Guaranteed**: 固定Magic Path。
- **Random**: `1×20% +1 [F/A/W/E]`は、20%で候補Pathの一つを1得るRandom pickを1回持つ。
- **Capital-only**: `capitalhome`属性による分類。
- Gold costは自動計算・Mount・Holy・Slow recruitment等の補正が複雑なため表示しない。

'''
    s += section("Fort recruitment",ft,fl,units,True)
    if nt or nl: s += "\n"+section("Fort不要・地形・外国Recruit",nt,nl,units)
    if ct or cl: s += "\n"+section("Coastal recruitment",ct,cl,units)
    return s+f'''\n## データ上の注意

- Hero、Event、Freespawn、国家固有召喚、Magic Site限定Unitは別扱い。
- 地形・建物・季節・Plane・Dominion条件で実際の候補が制限される場合がある。
- 抽出値とゲームUI上の最終CostやMount込み能力が一致しない場合がある。

## 出典

- [Dominions 6 Mod Inspector](https://larzm42.github.io/dom6inspector/)
- Data snapshot: `{COMMIT}`（Dominions 6.35）
'''


def fixed_max(items):
    top={p:0 for p in PATHS}
    for r in items:
        for p,v in fixed(r).items(): top[p]=max(top[p],v)
    return " ".join(f"{p}{v}" for p,v in top.items() if v) or "—"


def random_max(items):
    out=[]
    for r in items:
        for x in randoms(r):
            text=f"{x[0]}×{x[1]}% +{x[2]} [{'/'.join(x[3])}]"
            if text not in out: out.append(text)
    return "; ".join(out) or "—"


def write_indexes(ns,units,maps):
    idx=["---",'title: "国家Recruitデータ"',"status: generated",'verified_version: "6.35"',f'generated_from: "dom6inspector {COMMIT}"',"---","","# 国家Recruitデータ","","全vanilla国家のFort / Capital / Fort不要 / Coastal Recruitを自動生成した索引です。","","- [Mage access早見表](../mage-access.md)","- [国家攻略一覧](../../nations/index.md)",""]
    magepage=["---",'title: "Mage access早見表"',"status: generated",'verified_version: "6.35"',f'generated_from: "dom6inspector {COMMIT}"',"---","","# Mage access早見表","","Recruit commanderの固定PathとRandom poolを比較します。Booster、Hero、Summon、Site Mage、Communionは含みません。","","- [国家Recruitデータ](recruitment/index.md)","- [Magic Path Boosting](../magic/boosting.md)",""]
    for era in ("EA","MA","LA"):
        era_ns=[n for n in ns if n["code"]==era]
        idx += [f"## {BY_CODE[era][2]}（{era}）","","| ID | Nation | Epithet | Recruit data | 攻略 |","|---:|---|---|---|---|"]
        magepage += [f"## {era}","","| Nation | Any-fort fixed max | Any-fort random | Capital fixed max | Capital random |","|---|---|---|---|---|"]
        for n in era_ns:
            idx.append(f"| {n['id']} | {n['name']} | {n['epithet']} | [表示]({n['dir']}/{n['slug']}.md) | [攻略](../../nations/{n['dir']}/{n['slug']}.md) |")
            leaders=rows(maps["fl"].get(n["id"],[]),units)
            anyf=[r for r in leaders if not cap(r) and mage(r)]; capital=[r for r in leaders if cap(r) and mage(r)]
            magepage.append(f"| [{n['name']}](recruitment/{n['dir']}/{n['slug']}.md) | {esc(fixed_max(anyf))} | {esc(random_max(anyf))} | {esc(fixed_max(capital))} | {esc(random_max(capital))} |")
        idx.append(""); magepage.append("")
    idx += ["## 更新方針","",f"生成元: `{COMMIT}`。Patch更新時はCommitを変更し、未解決IDとMagic access差分を確認します。",""]
    magepage += ["## 読み方","","`F2 E1`は、その区分のCommander群に固定F2と固定E1へのアクセスがあることを示します。同じ一体が両方を持つとは限りません。",""]
    OUT.mkdir(parents=True,exist_ok=True); (OUT/"index.md").write_text("\n".join(idx),encoding="utf-8")
    MAGE_OUT.parent.mkdir(parents=True,exist_ok=True); MAGE_OUT.write_text("\n".join(magepage),encoding="utf-8")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--refresh",action="store_true"); ap.add_argument("--offline",action="store_true"); args=ap.parse_args()
    p={name:source(name,args.refresh,args.offline) for name in FILES}
    ns=nations(); units=unit_data(p["BaseU.csv"])
    maps={"ft":mapping(p["fort_troop_types_by_nation.csv"]),"fl":mapping(p["fort_leader_types_by_nation.csv"]),"nt":mapping(p["nonfort_troop_types_by_nation.csv"]),"nl":mapping(p["nonfort_leader_types_by_nation.csv"]),"ct":mapping(p["coast_troop_types_by_nation.csv"]),"cl":mapping(p["coast_leader_types_by_nation.csv"])}
    unknown=sorted(set().union(*(set(x) for x in maps.values()))-{n["id"] for n in ns})
    if unknown: print("warning: unmapped catalog nation IDs: "+", ".join(map(str,unknown)),file=sys.stderr)
    for n in ns:
        path=OUT/n["dir"]/f"{n['slug']}.md"; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(nation_page(n,units,maps),encoding="utf-8")
    write_indexes(ns,units,maps)
    total=sum(len(v) for m in maps.values() for v in m.values())
    print(f"source commit: {COMMIT}\nunits loaded: {len(units)}\nnations generated: {len(ns)}\nmapped recruitment entries: {total}")

if __name__ == "__main__": main()
