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
| 9 | [Class 9 audit branch](https://github.com/Eaglesiva/tn-class-09/tree/scert/class-09/audit-2026-27) | Summary, 28-record manifest, official API snapshot, and comparison evidence package | English (224p) verified 100% exact text match in Layer 4 (commit a2c6840f); remaining 7 books (2,280p) match page count & 2024 reprint imprint with Layer 4 diff pending. |
| 10 | [Class 10 audit branch](https://github.com/Eaglesiva/tn-class-10/tree/scert/class-10/audit-2026-27/docs) | Summary, 8-record audit manifest, API snapshot, and verification evidence | Tamil exact master SHA match; Maths TM/EM Manual Review Required; English imprint matched (content diff pending); Science/Social 4 editions (1,432p) stored on update branch with validated manifests. |
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
- [Final Master Audit Status — Harmonized Metrics & Layer 4 Diff Register](https://github.com/Eaglesiva/tn-class-10/blob/scert/master-edition-tracking/docs/FINAL_MASTER_AUDIT_STATUS.md)
- [Class 11 reconciliation complete (Archived)](https://github.com/Eaglesiva/tn-class-10/blob/scert/master-edition-tracking/docs/NEXT_AUDIT_CLASS_11_TA.md)

The Master CSV has separate `github_audit_branch` and `github_edition_branch` fields. These must remain distinct when a report is stored on one branch and official split pages are on another.

## 3. Local artifact names from Antigravity run transcripts

| Local artifact name | Remote check | Action |
|---|---|---|
| `scert_tracking_class_01_report.md` | Exact filename not found in the checked Class 1 branch; equivalent source evidence exists in remote summary and manifest. | Do not duplicate unless the local report contains additional evidence. |
| `verify_class9.py`, `class9_results.json` | Committed to `scert/class-09/audit-2026-27` in commit `0146eae7`. | Reconciled and archived. |
| `class10_results.json`, `verify_class10.py` | Committed to `scert/class-10/audit-2026-27` in commit `9cb11f78`. | Reconciled and archived. |
| `class11_batch3_batch4_final_report.md` | Batch reports 1-4 and overall audit report committed to `scert/class-11`. | Reconciled and archived. |
| `class12_verification_report.md` | Present under Class 12 update branch `docs/` and audit branch. | Reconciled and archived. |

## 4. Edition page-file inventory checked

| Class | Update branch | Edition/page groups | Page PDFs |
|---:|---|---:|---:|
| 10 | `scert/class-10/official-version-updates` | 4 | 1,432 |
| 11 | `scert/class-11/official-version-updates` | 24 (Chemistry/Physics TM/EM include Vol-1 and Vol-2) | 7,832 |
| 12 | `scert/class-12/official-version-updates` | 2 (Chemistry EM Vol-1; Physics EM Vol-1) | 648 |
| **Total** | — | **30** | **9,912** |

These are Git-tree file counts. They do not automatically establish PDF structural validation or content equivalence to the existing production main edition. Check the manifests and validation artifacts for each group.

## 5. Visibility limitation — Antigravity local filesystem

The full Antigravity local working directory, untracked files, files whose contents were not pasted, and unsaved changes are not visible from this GitHub check. Therefore this inventory is evidence-bounded and must not be treated as a complete local disk scan.

## 6. Shared working-copy protocol

1. The shared source of truth is `scert/master-edition-tracking`.
2. Before editing locally, Antigravity must fetch and fast-forward from this branch.
3. After editing, it must commit and push report/index changes to the same branch.
4. ChatGPT reads committed GitHub files, not Antigravity's uncommitted local files.
5. Keep raw per-class evidence in class repositories and the normalized cross-class index here.
