# SCERT Audit Artifacts — Local vs GitHub Inventory

**Checked:** 2026-11-05 (updated after Class 9 and Class 10 commits)  
**Scope:** GitHub repositories/branches and local artifact names explicitly shown in the Antigravity run transcript shared in this conversation. This is not a full filesystem scan of the Antigravity Windows workspace.

## 1. Already on GitHub — shared evidence exists

| Artifact | GitHub location | Finding |
|---|---|---|
| Class 1 summary, manifest and API snapshot | [Class 1 audit branch](https://github.com/Eaglesiva/tn-class-01/tree/scert/class-01/audit-2026-27-term1-vol1) | Present. Summary and manifest corrected on 2026-11-05. |
| Class 2 summary, manifest and API snapshot | [Class 2 audit branch](https://github.com/Eaglesiva/tn-class-02/tree/scert/class-02/audit-2026-27) | Present. Term-III 403 interpretation qualified. |
| Class 3 summary, manifest and API snapshot | [Class 3 audit branch](https://github.com/Eaglesiva/tn-class-03/tree/scert/class-03/audit-2026-27) | Present. Term-III 403 interpretation qualified. |
| Class 4 summary, manifest and API snapshot | [Class 4 audit branch](https://github.com/Eaglesiva/tn-class-04/tree/scert/class-04/audit-2026-27) | Present. Term-II sale-announced / CDN-403 distinction added. |
| Class 5 summary, manifest and API snapshot | [Class 5 audit branch](https://github.com/Eaglesiva/tn-class-05/tree/scert/class-05/audit-2026-27) | Present. Term-II sale-announced / CDN-403 distinction added. |
| Class 6 summary, manifest and API snapshot | [Class 6 audit branch](https://github.com/Eaglesiva/tn-class-06/tree/scert/class-06/audit-2026-27) | Present. Term-II sale-announced / CDN-403 distinction added. |
| Class 7 summary, manifest and API snapshot | [Class 7 audit branch](https://github.com/Eaglesiva/tn-class-07/tree/scert/class-07/audit-2026-27) | Present. Term-II sale-announced / CDN-403 distinction added. |
| Class 8 summary, manifest and API snapshot | [Class 8 audit branch](https://github.com/Eaglesiva/tn-class-08/tree/scert/class-08/audit-2026-27) | Present. No re-upload needed. |
| Class 10 audit documents and blueprint | [Class 10 docs on main](https://github.com/Eaglesiva/tn-class-10/tree/main/docs) | Master audit report, API/local comparison, CSV manifests and canonical blueprint are present. |
| Class 11 updated editions | [Class 11 official-version-updates branch](https://github.com/Eaglesiva/tn-class-11/tree/scert/class-11/official-version-updates) | Edition folders/workflow are present. No consolidated report was found in a docs folder on the checked branch. |
| Class 12 updated editions | [Class 12 official-version-updates branch](https://github.com/Eaglesiva/tn-class-12/tree/scert/class-12/official-version-updates) | Update branch exists; full official-catalog reconciliation remains pending. |


| Class 9 audit | [Class 9 audit branch](https://github.com/Eaglesiva/tn-class-09/tree/scert/class-09/audit-2026-27) | Summary, 28-row manifest and official API snapshot are committed. The run's comparison output/log files were not present in the checked docs directory; the summary's 8/8 page-match claim is retained as reported, but independent reproduction evidence is still pending. |
| Class 10 audit summary and manifest | [Class 10 audit branch](https://github.com/Eaglesiva/tn-class-10/tree/scert/class-10/audit-2026-27/docs) | Added during this audit: 8-record manifest, audit summary and normalized source catalog extract. |
| Class 10 edition updates | [Class 10 update branch](https://github.com/Eaglesiva/tn-class-10/tree/scert/class-10/official-version-updates) | Four 2026–27 official editions are stored (Science TM/EM, Social Science TM/EM), totaling 1,432 page files. Manifests/page lists/Git tree sequence counts agree. No separate `split_validation.json` or all-pages main comparison report was found. |
| Class 10 Tamil pilot | [Class 10 pilot branch](https://github.com/Eaglesiva/tn-class-10/tree/feature/scert-edition-pilot/tamil/editions/2026-27-scert-official) | Contains 248-page official Tamil edition metadata and SHA-256/MD5 that match the local master hashes. |

## 2. Local artifact names from the run transcript

| Local artifact name | Remote status | Action |
|---|---|---|
| class_01_audit_summary.md | Exact file exists on Class 1 audit branch. | Do not duplicate; link to remote source. |
| class_02_audit_summary.md through class_08_audit_summary.md | Exact files exist on their respective Class 2–8 audit branches. | Do not recreate; link from master tracker. |
| scert_tracking_class_01_report.md | Creation shown in local transcript; exact filename not found in checked Class 1 audit branch. Equivalent source evidence exists in Class 1 remote summary and manifest. | Central index/report is now in this Class 10 tracker branch. Upload the local version only if it has extra evidence. |
| scert_class11_batch3_batch4_final_report.md | Creation shown in local transcript. Underlying edition directories/commits/runs exist on Class 11 branch, but no docs directory/report was found on the checked branch. | Add a central copy only if the local file contains useful data not already in source manifests. |
| preflight_batch3.py and preflight_batch4.py | Local creation shown in transcript; these exact files were not found in the checked Class 11 branch root or scripts directory. | Review and upload if useful; remove secrets and machine-specific paths first. |
| dispatch_and_monitor_batch3.py and dispatch_and_monitor_batch4.py | Local creation shown in transcript; exact files were not found in the checked Class 11 branch root or scripts directory. | Review and upload if useful; remove secrets and machine-specific paths first. |
| emis3_scert_books.json and official_api_scert_books_raw | Names appear in local transcript; exact filenames not confirmed in checked repository roots. Class 1–8 already have class-specific official API snapshots on GitHub with the same reported raw snapshot SHA-256. | Compare local SHA-256 before uploading; avoid unnecessary duplicate snapshots. |
| class_08_audit_summary.md | Already exists on Class 8 audit branch. | No upload needed. |


| `verify_class9.py` and `class9_results.json` | Their creation/inspection is shown in the Antigravity run transcript; the exact files were not found in the Class 9 audit branch `docs` directory (which contains only summary, manifest and API snapshot). | These are supporting audit artifacts; upload them (plus page-2 images and comparison detail) after removing machine-specific paths/secrets, or regenerate a clean portable report in the Class 9 branch. |
| Class 10 local update/edition source | The remote update branch contains `scripts/cloud_runner_c10_update.py`, workflow `scert_class10_cloud_update.yml`, edition manifests and page PDFs. | These files are already remote; do not re-upload. Add the missing split structural validation and main-vs-official page comparison evidence as new audit artifacts. |

## 3. Class 9 and Class 10 artifact reconciliation

### Class 9

- Remote branch: [`Eaglesiva/tn-class-09` / `scert/class-09/audit-2026-27`](https://github.com/Eaglesiva/tn-class-09/tree/scert/class-09/audit-2026-27)
- Present remote files: `docs/class_09_audit_summary.md`, `docs/class_09_2026_27_audit_manifest.csv`, `docs/class_09_official_api_snapshot.json`.
- The summary/manifest report eight core books (2,504 pages) as 100% identical to GitHub main. The transcript mentions `verify_class9.py` and `class9_results.json`; these exact files were not found in the checked remote docs folder. The central CSV therefore preserves the reported outcome but flags that the supporting comparison package is not yet independently reproducible from the remote evidence.
- Do not re-download the eight Class 9 books simply to recreate the audit. First upload or regenerate the omitted comparison evidence, page-2 visual evidence and master checksum records if available.

### Class 10

- Audit branch: [`scert/class-10/audit-2026-27`](https://github.com/Eaglesiva/tn-class-10/tree/scert/class-10/audit-2026-27/docs). Present: `class_10_audit_summary.md`, `class_10_2026_27_audit_manifest.csv`, `class_10_source_catalog_extract.json`.
- Official edition update branch: [`scert/class-10/official-version-updates`](https://github.com/Eaglesiva/tn-class-10/tree/scert/class-10/official-version-updates). Four new edition page sets (Science TM/EM, Social Science TM/EM) total 1,432 page files. Their manifests, page lists and Git tree counts agree; no separate `split_validation.json` or main-vs-official all-pages comparison file was found.
- Tamil's 248-page official master SHA-256/MD5 match local master hashes in `feature/scert-edition-pilot`. No need to re-download or replace it.
- Seven other Class 10 core titles remain pending/manual review until their source-level contradictory labels are resolved and actual official-vs-main content comparison is documented.
- The prior Class 10 audit CSV is contradictory for seven books: `verdict=PENDING_CONTENT_AND_EDITION_REVIEW` while `standardized_status=VERIFIED_CONTENT_EQUIVALENT`. The new central Class10 audit manifest does not accept the latter as proof.

## 4. Class 11 and Class 12 edition inventory found remotely

| Class | Update branch | Edition/page sets visible in Git tree | Page PDFs |
|---:|---|---:|---:|
| 11 | `scert/class-11/official-version-updates` | 24 (Chemistry and Physics TM/EM each have Vol-1/Vol-2) | 7,832 |
| 12 | `scert/class-12/official-version-updates` | 2 (Chemistry EM Vol-1; Physics EM Vol-1) | 648 |

These counts are Git-tree observations, not proof that each PDF is content-equivalent to the live current official API or to any existing `main` copy. The next audits should refresh the official API and compare the stored manifests/page inventories before deciding whether to download anything.

## 5. Visibility limitation

The full Antigravity local working directory, untracked files, files whose contents were not pasted, and unsaved changes are not visible from this GitHub check. This inventory is evidence-bounded, not a complete local disk scan.

To complete the local-vs-GitHub reconciliation, Antigravity should generate a local file inventory from its project root that includes:

- git status (including modified and untracked files)
- all local audit/report/manifest/snapshot/preflight/dispatch files
- exact relative path, file size and modified time
- SHA-256 for JSON, CSV, Markdown and Python source files

Save that inventory to this shared branch, compare every local path with the corresponding GitHub branch, and upload only useful reproducible files. Never upload temporary master PDFs, credentials, tokens, .env files, cache folders or machine-specific secrets.

## 6. Shared working-copy protocol

1. The shared source of truth is the GitHub branch scert/master-edition-tracking.
2. Before editing locally, Antigravity must fetch and fast-forward from that branch.
3. After editing, commit and push report/index changes to the same branch.
4. ChatGPT reads committed GitHub files, not Antigravity's uncommitted local files.
5. Keep raw per-class evidence in class repositories and the normalized cross-class index here.
