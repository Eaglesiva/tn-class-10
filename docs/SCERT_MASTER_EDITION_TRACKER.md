# SCERT Master Edition Tracker — 2026–27

**Status:** Interim central register; Classes 1–8 consolidated, Classes 9–12 pending reconciliation  
**Last consolidated:** 2026-11-05 (Asia/Kolkata)  
**Class 1–8 API snapshot date:** 2026-11-04  
**Temporary canonical home:** Eaglesiva/tn-class-10, branch scert/master-edition-tracking

This repository document is the shared navigation and normalized index. Per-class raw API snapshots, detailed manifests and page-split evidence remain in their respective class repositories. Do not create duplicate class reports where a verified remote report already exists.

## 1. Shared files

- [Master Edition Index CSV — 83 in-scope records, Classes 1–8](./SCERT_MASTER_EDITION_INDEX.csv)
- [Local vs GitHub Artifact Inventory](./LOCAL_VS_GITHUB_ARTIFACT_INVENTORY.md)
- [Next task: Class 9 audit instructions](./NEXT_AUDIT_CLASS_09_TA.md)
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

## 7. Classes 9–12: remaining consolidation

| Class | GitHub evidence located | Central tracker action |
|---:|---|---|
| 9 | No SCERT audit branch found in branch search; class repository exists. | Next audit. Create a class-09 audit branch, refresh official API records, compare with existing GitHub content and write evidence report. |
| 10 | Existing docs on main include MASTER_EDITION_AUDIT_REPORT.md, OFFICIAL_API_VS_LOCAL_PDF_AUDIT.md, API/local CSVs and the canonical blueprint. An official-version-updates branch also exists. | Reconcile these pilot/audit records with the live official API and actual stored editions. |
| 11 | scert/class-11/official-version-updates contains four-batch edition ingestion. Previous report records 24 updated books and 7,832 split pages. | Reconcile all official API records against stored 2026–27 and older/newer editions. Ingestion alone is not a full catalog audit. |
| 12 | scert/class-12/official-version-updates exists; previous summary recorded two updated books and 648 pages. | Reconcile the live official API and every stored edition with the current catalog. |

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

- Classes 1–8: reports already exist and are linked above; avoid duplicate audits.
- Class 9: next catalog-vs-GitHub audit; no permanent edition ingestion yet.
- Class 10: reconcile existing Class 10 audit/pilot docs against the same schema.
- Classes 11–12: reconcile existing update branches against the live official catalog.
- Only after the 1–12 index is complete, decide which books are truly missing/old/mis-mapped and where an official source or alternate retrieval route is needed.
