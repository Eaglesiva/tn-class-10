# SCERT Audit Artifacts — Local vs GitHub Inventory

**Checked:** 2026-11-05  
**Scope:** The GitHub repositories/branches and local artifact names explicitly shown in Antigravity run transcripts shared in this conversation. This is not a full filesystem scan of the Antigravity Windows workspace.

## 1. Already on GitHub — class audit source evidence

| Class | GitHub location | Source evidence found | Current note |
|---:|---|---|---|
| 1 | [Class 1 audit branch](https://github.com/Eaglesiva/tn-class-01/tree/scert/class-01/audit-2026-27-term1-vol1) | Summary, audit CSV, raw API snapshot, official edition folders and split-validation files | Summary/manifest correction notes were committed for page validation counts and Term-III 403 interpretation. |
| 2 | [Class 2 audit branch](https://github.com/Eaglesiva/tn-class-02/tree/scert/class-02/audit-2026-27) | Summary, audit CSV, raw API snapshot and official editions | Term-III 403 status was qualified as unconfirmed release status. |
| 3 | [Class 3 audit branch](https://github.com/Eaglesiva/tn-class-03/tree/scert/class-03/audit-2026-27) | Summary, audit CSV, raw API snapshot and official editions | Term-III 403 status was qualified as unconfirmed release status. |
| 4 | [Class 4 audit branch](https://github.com/Eaglesiva/tn-class-04/tree/scert/class-04/audit-2026-27) | Summary, audit CSV, raw API snapshot and official editions | Term-II sale-announced / CDN-403 distinction was recorded. |
| 5 | [Class 5 audit branch](https://github.com/Eaglesiva/tn-class-05/tree/scert/class-05/audit-2026-27) | Summary, audit CSV, raw API snapshot and official editions | Term-II sale-announced / CDN-403 distinction was recorded. |
| 6 | [Class 6 audit branch](https://github.com/Eaglesiva/tn-class-06/tree/scert/class-06/audit-2026-27) | Summary, audit CSV, raw API snapshot and official editions | Term-II sale-announced / CDN-403 distinction was recorded. |
| 7 | [Class 7 audit branch](https://github.com/Eaglesiva/tn-class-07/tree/scert/class-07/audit-2026-27) | Summary, audit CSV, raw API snapshot and official editions | Term-II sale-announced / CDN-403 distinction was recorded. |
| 8 | [Class 8 audit branch](https://github.com/Eaglesiva/tn-class-08/tree/scert/class-08/audit-2026-27) | Summary, audit CSV, raw API snapshot and official editions | No re-upload needed. |
| 9 | [Class 9 audit branch](https://github.com/Eaglesiva/tn-class-09/tree/scert/class-09/audit-2026-27) | Summary, 28-record manifest and official API snapshot | The report claims 8/8 core books match (2,504 pages). The verification script/results file and detailed page-comparison evidence mentioned in Antigravity's transcript were not found in the checked remote `docs` folder. The central index records the result as reported, with independent reproduction evidence pending. |
| 10 | [Class 10 audit branch](https://github.com/Eaglesiva/tn-class-10/tree/scert/class-10/audit-2026-27/docs) | New summary, 8-record audit manifest and normalized source catalog extract | Added in this audit. Tamil has exact master SHA-256/MD5 match; seven other books remain pending or comparison-incomplete. |
| 11 | [Class 11 audit branch](https://github.com/Eaglesiva/tn-class-11/tree/scert/class-11/audit-2026-27) & [update branch](https://github.com/Eaglesiva/tn-class-11/tree/scert/class-11/official-version-updates) | Summary, 32-record manifest, fresh raw API snapshot (SHA: `404f2834...`), and 24 edition folders | Reconciliation complete. 32 books: 4 GITHUB_IS_NEWER (1,152p), 4 SAME_VERSION (1,304p), 23 OFFICIAL UPDATES (7,528p), 1 API_MAPPING_UNRESOLVED (304p). Total 10,288 pages. |
| 12 | [Class 12 audit branch](https://github.com/Eaglesiva/tn-class-12/tree/scert/class-12/audit-2026-27) & [update branch](https://github.com/Eaglesiva/tn-class-12/tree/scert/class-12/official-version-updates) | Summary, 34-record manifest, fresh raw API snapshot (SHA: `404f2834...`), and 2 edition folders | Reconciliation complete. 34 books: 32 SAME_VERSION (9,872p), 2 OFFICIAL UPDATES (648p: Physics EM Vol 1 352p, Chemistry EM Vol 1 296p). Total 10,520 pages. |

### Existing Class 11 / Class 12 report files

- Class 11 [overall verification report](https://github.com/Eaglesiva/tn-class-11/blob/scert/class-11/official-version-updates/docs/class11_verification_report.md)
- Class 11 [Batch 1](https://github.com/Eaglesiva/tn-class-11/blob/scert/class-11/official-version-updates/docs/class_11_batch_1_report.md), [Batch 2](https://github.com/Eaglesiva/tn-class-11/blob/scert/class-11/official-version-updates/docs/class_11_batch_2_report.md), [Batch 3](https://github.com/Eaglesiva/tn-class-11/blob/scert/class-11/official-version-updates/docs/class_11_batch_3_report.md), [Batch 4](https://github.com/Eaglesiva/tn-class-11/blob/scert/class-11/official-version-updates/docs/class_11_batch_4_report.md)
- Class 12 [overall verification report](https://github.com/Eaglesiva/tn-class-12/blob/scert/class-12/official-version-updates/docs/class12_verification_report.md)
- Class 12 [cloud edition update report](https://github.com/Eaglesiva/tn-class-12/blob/scert/class-12/official-version-updates/docs/class_12_cloud_edition_update_report.md)

## 2. Central shared tracker files

The temporary central tracker is stored on `Eaglesiva/tn-class-10`, branch `scert/master-edition-tracking`:

- [Master Edition Tracker](https://github.com/Eaglesiva/tn-class-10/blob/scert/master-edition-tracking/docs/SCERT_MASTER_EDITION_TRACKER.md)
- [Master Edition Index CSV — 165 records, Classes 1–12](https://github.com/Eaglesiva/tn-class-10/blob/scert/master-edition-tracking/docs/SCERT_MASTER_EDITION_INDEX.csv)
- [Class 11 reconciliation complete (Next: Class 12 reconciliation)](https://github.com/Eaglesiva/tn-class-10/blob/scert/master-edition-tracking/docs/NEXT_AUDIT_CLASS_11_TA.md)

The Master CSV has separate `github_audit_branch` and `github_edition_branch` fields. These must remain distinct when a report is stored on one branch and official split pages are on another.

## 3. Local artifact names from Antigravity run transcripts

| Local artifact name | Remote check | Action |
|---|---|---|
| `scert_tracking_class_01_report.md` | Exact filename not found in the checked Class 1 branch; equivalent source evidence exists in remote summary and manifest. | Do not duplicate unless the local report contains additional evidence. |
| `verify_class9.py`, `class9_results.json` | Transcript says created/inspected; exact files not found in the Class 9 audit branch docs folder. | Upload a clean portable script/results package and page-comparison evidence if available; otherwise regenerate them from the stored manifest. |
| `scert_class11_batch3_batch4_final_report.md` | Exact filename not found, but the four batch reports and the overall Class 11 verification report are already remote. | Do not upload a duplicate unless it has evidence not covered by the four batch reports. |
| `preflight_batch3.py`, `preflight_batch4.py` | Exact files not found in the checked Class 11 branch root or scripts folder. | Review for secrets and machine-specific paths, then upload if still useful/reproducible. |
| `dispatch_and_monitor_batch3.py`, `dispatch_and_monitor_batch4.py` | Exact files not found in the checked Class 11 branch root or scripts folder. | Review for secrets and machine-specific paths, then upload if still useful/reproducible. |
| `emis3_scert_books.json`, `official_api_scert_books_raw` | Exact filenames not confirmed in checked repository roots. Class 1–8 have class-specific API snapshot JSON files with the same reported raw SHA-256. Class 9 also has its own raw API snapshot. | Compare local SHA-256 before uploading; avoid duplicates. Class 10–12 still need fresh raw snapshots in their audit evidence. |
| Class 10 `cloud_runner_c10_update.py` and workflow | Present on Class 10 update branch under `scripts/` and `.github/workflows/`. | Do not re-upload. Add validation and comparison outputs as new evidence. |
| Class 11 batch report files | Present under Class 11 update branch `docs/`. | Already shared. |
| Class 12 verification/update reports | Present under Class 12 update branch `docs/`. | Already shared. |

## 4. Edition page-file inventory checked

| Class | Update branch | Edition/page groups | Page PDFs |
|---:|---|---:|---:|
| 10 | `scert/class-10/official-version-updates` | 4 | 1,432 |
| 11 | [Class 11 audit branch](https://github.com/Eaglesiva/tn-class-11/tree/scert/class-11/audit-2026-27) & [update branch](https://github.com/Eaglesiva/tn-class-11/tree/scert/class-11/official-version-updates) | Summary, 32-record manifest, fresh raw API snapshot (SHA: `404f2834...`), and 24 edition folders | Reconciliation complete. 32 books: 4 GITHUB_IS_NEWER (1,152p), 4 SAME_VERSION (1,304p), 23 OFFICIAL UPDATES (7,528p), 1 API_MAPPING_UNRESOLVED (304p). Total 10,288 pages. |
| 12 | [Class 12 audit branch](https://github.com/Eaglesiva/tn-class-12/tree/scert/class-12/audit-2026-27) & [update branch](https://github.com/Eaglesiva/tn-class-12/tree/scert/class-12/official-version-updates) | Summary, 34-record manifest, fresh raw API snapshot (SHA: `404f2834...`), and 2 edition folders | Reconciliation complete. 34 books: 32 SAME_VERSION (9,872p), 2 OFFICIAL UPDATES (648p: Physics EM Vol 1 352p, Chemistry EM Vol 1 296p). Total 10,520 pages. |

These are Git-tree file counts. They do not automatically establish PDF structural validation or content equivalence to the existing production main edition. Check the manifests and validation artifacts for each group.

## 5. Visibility limitation — Antigravity local filesystem

The full Antigravity local working directory, untracked files, files whose contents were not pasted, and unsaved changes are not visible from this GitHub check. Therefore this inventory is evidence-bounded and must not be treated as a complete local disk scan.

To finish the local-vs-GitHub reconciliation, Antigravity should generate a local file inventory from its project root that includes:

- `git status --short` and untracked file paths
- all local audit/report/manifest/snapshot/preflight/dispatch files
- exact relative path, file size and modified time
- SHA-256 for JSON, CSV, Markdown and Python source files

Save that inventory to the shared tracker branch, compare every local path with the corresponding GitHub branch, and upload only useful reproducible files. Never upload temporary master PDFs, credentials, tokens, `.env` files, caches or machine-specific secrets.

## 6. Shared working-copy protocol

1. The shared source of truth is `scert/master-edition-tracking`.
2. Before editing locally, Antigravity must fetch and fast-forward from this branch.
3. After editing, it must commit and push report/index changes to the same branch.
4. ChatGPT reads committed GitHub files, not Antigravity's uncommitted local files.
5. Keep raw per-class evidence in class repositories and the normalized cross-class index here.
