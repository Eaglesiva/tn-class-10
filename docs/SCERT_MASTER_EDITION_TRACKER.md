# SCERT Master Edition Tracker — 2026–27

**Status:** Central register updated through Class 10; Classes 1–10 consolidated, Classes 11–12 pending reconciliation  
**Last consolidated:** 2026-11-05 (Asia/Kolkata)  
**Class 1–8 API snapshot date:** 2026-11-04  
**Temporary canonical home:** Eaglesiva/tn-class-10, branch scert/master-edition-tracking

This repository document is the shared navigation and normalized index. Per-class raw API snapshots, detailed manifests and page-split evidence remain in their respective class repositories. Do not create duplicate class reports where a verified remote report already exists.

## 1. Shared files

- [Master Edition Index CSV — 99 in-scope records, Classes 1–10](./SCERT_MASTER_EDITION_INDEX.csv)
- [Local vs GitHub Artifact Inventory](./LOCAL_VS_GITHUB_ARTIFACT_INVENTORY.md)
- [Class 9 audit instructions (completed/archive)](./NEXT_AUDIT_CLASS_09_TA.md)
- [Class 10 audit summary](https://github.com/Eaglesiva/tn-class-10/blob/scert/class-10/audit-2026-27/docs/class_10_audit_summary.md)
- [Class 10 audit manifest](https://github.com/Eaglesiva/tn-class-10/blob/scert/class-10/audit-2026-27/docs/class_10_2026_27_audit_manifest.csv)
- [Next task: Class 11 reconciliation](./NEXT_AUDIT_CLASS_11_TA.md)
- [Canonical verification blueprint](https://github.com/Eaglesiva/tn-class-10/blob/main/docs/SCERT_CLASSWISE_EDITION_VERIFICATION_BLUEPRINT.md)

This documentation branch was created from the current Class 10 main branch. It does not modify production code, book files, viewer routing or the live site.

## 2. Consolidated Class 1–8 status

The class audit manifests contain 83 in-scope State Board Tamil/English academic records. Across the same snapshots, Classes 1–8 have 289 total API records, including minority-language, CBSE, supplementary and teacher-resource entries that are excluded from this core register.

| Class | All API records | In-scope | Official GET 200 | Official GET 403 | Pages in GET-200 master PDFs | Audit branch |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 34 | 9 | 6 | 3 | 848 | scert/class-01/audit-2026-27-term1-vol1 |
| 2 | 34 | 9 | 6 | 3 | 824 | scert/class-02/audit-2026-27 |
| 3 | 35 | 9 | 6 | 3 | 1,016 | scert/class-03/audit-2026-27 |
| 4 | 30 | 9 | 3 | 6 | 472 | scert/class-04/audit-2026-27 |
| 5 | 30 | 9 | 3 | 6 | 544 | scert/class-05/audit-2026-27 |
| 6 | 49 | 15 | 5 | 10 | 864 | scert/class-06/audit-2026-27 |
| 7 | 49 | 15 | 5 | 10 | 880 | scert/class-07/audit-2026-27 |
| 8 | 28 | 8 | 8 | 0 | 2,208 | scert/class-08/audit-2026-27 |
| **Total** | **289** | **83** | **42** | **41** | **7,656** | **8 class audit branches** |

The 7,656 figure is the sum of official master-PDF page counts in 42 GET-200 records. It is not the printed-page total and does not, on its own, prove content equivalence with the existing GitHub copy.

## 3. Critical HTTP 403 interpretation

HTTP 403 is a retrieval result, not a publication decision.

- Classes 1–3: the three Term-III State Board API records returned 403 in the 2026-11-04 audit. The sales notices checked announce Term-I and Term-II. The general price list contains Term-III titles for Classes 1–5, but this alone does not establish a 2026–27 Term-III release date. These records are CDN_UNAVAILABLE_AT_CHECK / RELEASE_STATUS_UNCONFIRMED.
- Classes 4–7: Term-II and Term-III URLs returned 403. Term-II sales for Classes 1–7 were officially announced from 22-09-2026. Therefore a Class 4–7 Term-II 403 is a CDN/URL access problem, not evidence that the books were not released.
- Term-III: the API records exist, but the current 2026–27 sales notices checked do not give a Term-III release date. Keep the state unconfirmed until an official notice or accessible official PDF establishes it.
- Class 8: all eight in-scope annual textbook URLs returned GET 200 in the audit manifest.

Official sources:
- [Textbook Corporation — 2026–27 sale notices](https://www.textbookcorp.in/schools)
- [Textbook Corporation — textbook price list](https://textbookcorp.in/textbook/schools/books)
- [SCERT official textbook listing](https://tnschools.gov.in/scert-textbook)
- [Official SCERT listing API](https://emis3.tnschools.gov.in/api/get_scert_books)

## 4. Academic year versus printed edition

Keep four separate facts for every book:

1. Academic/distribution year (for this register: 2026–27).
2. Printed first edition, revised edition or reprint, extracted from the actual book, usually page 2.
3. Date checked and source API record.
4. Exact GitHub stored edition: repository, branch and immutable edition path.

A book distributed in 2026–27 may still show a printed imprint such as First Edition 2018/2019 or Reprint 2024. This does not automatically mean the book is obsolete. Do not label every 2026–27 download as a 2026 printed edition or Reprint 2024.

The CSV preserves the raw page-2 text. IMAGE_ONLY_OR_NO_TEXT means the imprint has not been read from the image and needs visual inspection. An extracted text fragment also needs interpretation before assigning a printed year.

## 5. Class 1 corrections already committed

The Class 1 audit evidence was re-read before centralization. Corrections were committed to the Class 1 audit branch:

- Removed the blanket claim that all six Term-I/Term-II volumes are Reprint 2024. The official page-2 extraction shows © SCERT 2026 for Term-I Vol-I and First Edition - 2026 for Term-I Vol-II Tamil. Other volumes have incomplete or image-only extraction and need visual review.
- Changed the three Term-III conclusions from confirmed not released to CDN HTTP 403 / release status unconfirmed.
- Corrected two Term-I Vol-II CSV validation strings from 176/176 to 144/144. Their split_validation.json files report 144 master pages processed and all 144 passing.

Updated source files:
- [Class 1 summary](https://github.com/Eaglesiva/tn-class-01/blob/scert/class-01/audit-2026-27-term1-vol1/class_01_audit_summary.md)
- [Class 1 audit manifest](https://github.com/Eaglesiva/tn-class-01/blob/scert/class-01/audit-2026-27-term1-vol1/class_01_2026_27_audit_manifest.csv)
- [Class 1 API snapshot](https://github.com/Eaglesiva/tn-class-01/blob/scert/class-01/audit-2026-27-term1-vol1/class_01_official_api_snapshot.json)

## 6. Existing class audit reports — do not recreate

Classes 1–8 already have separate GitHub audit branches. Each contains a class summary, audit manifest CSV, official API snapshot JSON and an official_editions directory.

| Class | Summary | Manifest | API snapshot |
|---:|---|---|---|
| 1 | [summary](https://github.com/Eaglesiva/tn-class-01/blob/scert/class-01/audit-2026-27-term1-vol1/class_01_audit_summary.md) | [CSV](https://github.com/Eaglesiva/tn-class-01/blob/scert/class-01/audit-2026-27-term1-vol1/class_01_2026_27_audit_manifest.csv) | [JSON](https://github.com/Eaglesiva/tn-class-01/blob/scert/class-01/audit-2026-27-term1-vol1/class_01_official_api_snapshot.json) |
| 2 | [summary](https://github.com/Eaglesiva/tn-class-02/blob/scert/class-02/audit-2026-27/class_02_audit_summary.md) | [CSV](https://github.com/Eaglesiva/tn-class-02/blob/scert/class-02/audit-2026-27/class_02_2026_27_audit_manifest.csv) | [JSON](https://github.com/Eaglesiva/tn-class-02/blob/scert/class-02/audit-2026-27/class_02_official_api_snapshot.json) |
| 3 | [summary](https://github.com/Eaglesiva/tn-class-03/blob/scert/class-03/audit-2026-27/class_03_audit_summary.md) | [CSV](https://github.com/Eaglesiva/tn-class-03/blob/scert/class-03/audit-2026-27/class_03_2026_27_audit_manifest.csv) | [JSON](https://github.com/Eaglesiva/tn-class-03/blob/scert/class-03/audit-2026-27/class_03_official_api_snapshot.json) |
| 4 | [summary](https://github.com/Eaglesiva/tn-class-04/blob/scert/class-04/audit-2026-27/class_04_audit_summary.md) | [CSV](https://github.com/Eaglesiva/tn-class-04/blob/scert/class-04/audit-2026-27/class_04_2026_27_audit_manifest.csv) | [JSON](https://github.com/Eaglesiva/tn-class-04/blob/scert/class-04/audit-2026-27/class_04_official_api_snapshot.json) |
| 5 | [summary](https://github.com/Eaglesiva/tn-class-05/blob/scert/class-05/audit-2026-27/class_05_audit_summary.md) | [CSV](https://github.com/Eaglesiva/tn-class-05/blob/scert/class-05/audit-2026-27/class_05_2026_27_audit_manifest.csv) | [JSON](https://github.com/Eaglesiva/tn-class-05/blob/scert/class-05/audit-2026-27/class_05_official_api_snapshot.json) |
| 6 | [summary](https://github.com/Eaglesiva/tn-class-06/blob/scert/class-06/audit-2026-27/class_06_audit_summary.md) | [CSV](https://github.com/Eaglesiva/tn-class-06/blob/scert/class-06/audit-2026-27/class_06_2026_27_audit_manifest.csv) | [JSON](https://github.com/Eaglesiva/tn-class-06/blob/scert/class-06/audit-2026-27/class_06_official_api_snapshot.json) |
| 7 | [summary](https://github.com/Eaglesiva/tn-class-07/blob/scert/class-07/audit-2026-27/class_07_audit_summary.md) | [CSV](https://github.com/Eaglesiva/tn-class-07/blob/scert/class-07/audit-2026-27/class_07_2026_27_audit_manifest.csv) | [JSON](https://github.com/Eaglesiva/tn-class-07/blob/scert/class-07/audit-2026-27/class_07_official_api_snapshot.json) |
| 8 | [summary](https://github.com/Eaglesiva/tn-class-08/blob/scert/class-08/audit-2026-27/class_08_audit_summary.md) | [CSV](https://github.com/Eaglesiva/tn-class-08/blob/scert/class-08/audit-2026-27/class_08_2026_27_audit_manifest.csv) | [JSON](https://github.com/Eaglesiva/tn-class-08/blob/scert/class-08/audit-2026-27/class_08_official_api_snapshot.json) |

Class 2, 3 and 4 reports therefore do not need to be generated again. The source manifests and summaries have been amended to qualify HTTP 403 interpretations.

## 7. Classes 9–12: consolidation status and remaining work

| Class | Central-index records | Audit evidence located | Current result | Remaining work |
|---:|---:|---|---|---|
| 9 | 8 | `Eaglesiva/tn-class-09`, branch `scert/class-09/audit-2026-27`; summary, manifest and API snapshot are committed | The per-class report states 8/8 matched (2,504 pages). The central CSV preserves that reported result but flags `REPORTED_MATCH_EVIDENCE_PACKAGE_PENDING`, because the underlying per-page comparison output, official master hashes and page-2 image proof were not attached to the checked remote docs. | Upload or regenerate the comparison evidence package before treating the result as independently reproducible. No redownload/re-split is indicated by the current report. |
| 10 | 8 | Existing audit CSVs and blueprints on `main`; Class10 audit branch `scert/class-10/audit-2026-27`; update branch `scert/class-10/official-version-updates`; pilot branch `feature/scert-edition-pilot` | Tamil has an exact master SHA-256 match (248 pages). English and Maths TM/EM remain manual review because source verdict says `PENDING_CONTENT_AND_EDITION_REVIEW` despite a conflicting standardized label. Science/Social TM/EM have four official split editions (1,432 pages) on the update branch; manifest/file sequence counts match, but split validation and all-page comparison against main are not yet attached. | Reconcile the seven remaining books with official masters and attach comparison/validation evidence. Keep all work off production main. |
| 11 | Not yet added | `scert/class-11/official-version-updates` contains the four-batch official edition ingestion | The earlier batch report states 24 updated books / 7,832 split pages. This is an ingestion record, not yet a complete official catalog reconciliation. | Next audit: compare every live official API State Board record to the stored editions and previous main editions; no duplicate download unless evidence requires it. |
| 12 | Not yet added | `scert/class-12/official-version-updates` exists; earlier report states two updated books / 648 pages | Edition update branch exists; full official catalog reconciliation is pending. | Reconcile live official API records and every stored edition. |

### Class 9 source files

- [Class 9 summary](https://github.com/Eaglesiva/tn-class-09/blob/scert/class-09/audit-2026-27/docs/class_09_audit_summary.md)
- [Class 9 manifest](https://github.com/Eaglesiva/tn-class-09/blob/scert/class-09/audit-2026-27/docs/class_09_2026_27_audit_manifest.csv)
- [Class 9 official API snapshot](https://github.com/Eaglesiva/tn-class-09/blob/scert/class-09/audit-2026-27/docs/class_09_official_api_snapshot.json)

### Class 10 source files

- [Class 10 audit summary](https://github.com/Eaglesiva/tn-class-10/blob/scert/class-10/audit-2026-27/docs/class_10_audit_summary.md)
- [Class 10 audit manifest](https://github.com/Eaglesiva/tn-class-10/blob/scert/class-10/audit-2026-27/docs/class_10_2026_27_audit_manifest.csv)
- [Class 10 normalized source catalog extract](https://github.com/Eaglesiva/tn-class-10/blob/scert/class-10/audit-2026-27/docs/class_10_source_catalog_extract.json)
- [Class 10 official-version update branch](https://github.com/Eaglesiva/tn-class-10/tree/scert/class-10/official-version-updates)
- [Class 10 Tamil pilot edition metadata](https://github.com/Eaglesiva/tn-class-10/blob/feature/scert-edition-pilot/tamil/editions/2026-27-scert-official/edition.md)

### Class 10 reconciliation details

- `main` has eight ordered `pages.json` inventories and matching Git tree page PDF counts: **2,624 existing page PDFs**.
- The separate update branch has four 2026–27 official editions: Science TM/EM and Social Science TM/EM. Their edition manifests contain **1,432 entries**, their `pages.json` files contain the same counts, and the GitHub tree contains continuous page files 1..N.
- Those counts prove that the split files exist in sequence; they do **not** prove that every split PDF opens, renders and contains exactly one page, because no `split_validation.json` was found.
- They also do not prove that the newly split files are content-equivalent to the old `main` page sets. That comparison is still pending.
- Class 10 Tamil is a stronger exception: the stored official master SHA-256/MD5 matches the local master hashes, and the feature branch stores the 248-page official 2024 Revised Edition. Keep it; no re-download needed.
- The old 184-page / 7-unit Tamil 2025 candidate remains `UNMAPPED_CANDIDATE`; no official API record/master hash was found for it in the checked sources. Do not replace the 248-page official copy on this basis.
- The old Class 10 source CSV has an internal contradiction on seven rows: `verdict=PENDING_CONTENT_AND_EDITION_REVIEW` while `standardized_status=VERIFIED_CONTENT_EQUIVALENT`. The central index follows the explicit pending verdict and does not accept the contradictory standardized label as proof.

### Central CSV structure note

The Master CSV now has a separate `github_edition_branch` column in addition to `github_audit_branch`. This is necessary because the audit manifest may be stored on one branch while the actual edition pages are stored on another branch (for example, Class 10's four Science/Social editions).


## 8. Status vocabulary

- API_LISTED — exact official API record exists.
- SALE_ANNOUNCED — current official notice covers that class/term/year.
- CDN_HTTP_200 — official URL returned a successful PDF response.
- CDN_HTTP_403 — URL returned 403 at check time; do not infer publication status from this alone.
- PRINT_IMPRINT_TEXT_EXTRACTED — page-2 text extracted; interpretation still required.
- PRINT_IMPRINT_IMAGE_ONLY — page 2 needs visual inspection before recording imprint.
- AUDIT_BRANCH_SPLIT_VALIDATED — audit manifest and split-validation artifact report structural validation.
- TOC_MAPPING_PENDING — combined volume still needs verified subject/unit boundaries before viewer routing.
- GITHUB_MAIN_NOT_UPDATED — files exist on audit branch only; this does not mean production main or live site changed.
- GITHUB_MISSING — use only after checking correct repository, branch, subject/medium/term mapping and page manifests.
- OFFICIAL_NOT_IN_API — use only after checking a refreshed official API snapshot.
- RELEASE_STATUS_UNCONFIRMED — official record exists but release timing/publication is not established by notices checked.
- MANUAL_REVIEW_REQUIRED — evidence is incomplete, ambiguous or contradictory.

## 9. Shared update rules

1. Before editing, fetch the latest scert/master-edition-tracking branch.
2. Work class-by-class; preserve exact API record, filename, URL, term, medium and timestamp.
3. Keep academic year and printed imprint separate.
4. Record HTTP status separately from official sale-announcement status.
5. For HTTP 403, check exact URL/encoding, redirects, API mapping and sale notices. Do not call it unreleased automatically.
6. Keep official master PDFs in temporary runner storage; do not commit them.
7. During catalog-first audit, do not permanently split/upload new editions or change production viewer/main without explicit approval.
8. Keep raw per-class evidence in class repositories and the normalized cross-class index here.
9. Antigravity must commit and push its updates to this same branch so ChatGPT and Antigravity read the same version.
10. Do not merge this documentation branch into Class 10 main until reviewed. A dedicated tracker repository can be created later and the documents migrated.

## 10. Immediate sequence

- Classes 1–8: source audits and manifests already exist; avoid duplicate audits.
- Class 9: catalog report and 8 records are committed; attach the detailed comparison evidence package before independently certifying the 8/8 result.
- Class 10: the 8-record audit manifest is committed; finish the seven pending/partial comparisons without touching production main.
- Class 11: next class-wise catalog reconciliation. Reuse its existing 2026–27 edition branch and compare it to the live API; do not redownload existing editions without evidence.
- Class 12: reconcile its existing update branch after Class 11.
- Only after Classes 1–12 are reconciled, decide which books are genuinely missing/older/mis-mapped and which official or alternate retrieval source should be investigated.