# Generated-data source lock

`sources/dom6inspector.toml` is the authoritative lock file for every upstream
Dom6 Inspector file consumed by the canonical Wiki build.

The lock records:

- upstream repository, commit, tree, and Dominions game version;
- the complete set of CSV/JavaScript inputs used by generators;
- each input's expected Git blob SHA;
- its stable local cache name and the generator groups that consume it.

## Normal build

```bash
python scripts/build_wiki.py
```

The build begins by running `scripts/audit_sources.py`. Missing files are
fetched from the pinned commit, every cache entry is verified against its Git
blob SHA, and `build/source-audit.json` is written. All generators then run with
`--offline`, so no later stage can silently fetch different bytes.

## Offline and refresh modes

```bash
# Require a complete, valid cache and make no network requests.
python scripts/build_wiki.py --offline

# Re-download every locked input, verify it, then build offline.
python scripts/build_wiki.py --refresh
```

The source audit can also be run independently:

```bash
python scripts/audit_sources.py --report build/source-audit.json
python scripts/audit_sources.py --offline --report build/source-audit.json
```

## Patch-impact report

After generating the current docs, run:

```bash
python scripts/report_patch_impact.py \
  --report build/patch-impact.json
```

The report records generated-page counts, Markdown table-row counts, bytes, and
content fingerprints by dataset. In a Pull Request, the default baseline is the
target branch. When that revision contains the canonical source lock and build
pipeline, the tool creates a temporary detached worktree, regenerates the base
revision, and reports added, removed, and changed generated pages plus per-
dataset metric deltas.

The same report compares every game-versioned hand-written page with
`source.game_version`. Generator-owned pages, nation stubs, project policy, and
templates are excluded. Older or uncomparable `verified_version` values are
shown as GitHub warnings; missing versions remain visible as non-blocking
editorial debt. Use `--fail-on-stale` only after the selected content area has
been fully migrated.

For local or fixture comparisons, a pre-generated directory can replace the Git
worktree:

```bash
python scripts/report_patch_impact.py \
  --baseline-docs ../previous-build/docs \
  --report build/patch-impact.json
```

## Updating the pinned snapshot

A source-version change is an explicit lock-file review, not a replacement of a
single commit constant.

1. Change `source.commit`, `source.tree`, and `source.game_version`.
2. Re-enumerate all consumed files and update their `blob` values.
3. Run `python scripts/build_wiki.py --refresh`.
4. Run `python scripts/report_patch_impact.py` and review generated dataset deltas.
5. Review `build/source-audit.json`, `build/patch-impact.json`, and the generated Wiki diff.
6. Re-verify hand-written pages reported as older than the locked game version.

GitHub Actions compares the current manifest with the base revision and writes
source metadata, added/removed/changed inputs, and every verified SHA-256 to the
job summary. Validation also writes the generated-data and article-freshness
impact report, then uploads all JSON reports as the `wiki-audits` artifact.

During migration, several direct generator entry points still expose their old
module-level `COMMIT` constant. `scripts/audit_sources.py` parses those modules
and fails when any value differs from the manifest. The canonical build remains
the source of truth and performs all network access through the manifest audit.
