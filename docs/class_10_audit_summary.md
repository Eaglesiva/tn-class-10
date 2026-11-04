# SCERT Class 10 — 2026–27 Official Catalog vs GitHub Edition Audit

**Audit branch:** `scert/class-10/audit-2026-27`  
**Edition update branch examined:** `scert/class-10/official-version-updates`  
**Production baseline examined:** `main`  
**Existing API/local audit record date:** 2026-11-03  
**Cloud Runner edition downloads:** 2026-11-04  
**Current official release notice checked:** 2026-11-05

## 1. Scope and evidence sources

Class 10 has eight State Board annual core books in the pre-existing official API/local audit CSV: Tamil, English, Mathematics TM/EM, Science TM/EM and Social Science TM/EM. The same CSV has 25 Class 10 records total, of which 17 are outside the core Tamil/English scope (minority-language and other reader records).

**Important limitation:** The Class 10 repository has `docs/official_api_local_match_manifest.csv` and `docs/local_master_pdf_reverse_audit.csv`, but no raw Class 10 API response JSON was found in the checked docs directory. This report is based on those 2026-11-03 records plus the Class 10 Cloud Runner edition metadata downloaded on 2026-11-04. The live SCERT API was not freshly re-fetched during this consolidation. Therefore the 2026-11-03 API record and HTTP results are a dated evidence snapshot, not a claim about a fresh 2026-11-05 API response.

Official sale notice: Textbook Corporation states that annual textbooks for Classes 9, 10 and 12 for academic year 2026–27 went on sale from **10-04-2026**. <https://www.textbookcorp.in/schools>

## 2. GitHub inventory checked

### Production `main` branch

The eight production subject `pages.json` files and corresponding Git tree page PDFs were checked. Each has unique ordered entries from page 1 to the recorded final page; the actual Git tree contains the same number of PDF pages.

| Subject / medium | Main pages | Last listed page |
|---|---:|---|
| Tamil | 248 | 248 |
| English | 224 | 224 |
| Mathematics TM | 368 | 368 |
| Mathematics EM | 352 | 352 |
| Science TM | 360 | 360 |
| Science EM | 360 | 360 |
| Social Science TM | 368 | 368 |
| Social Science EM | 344 | 344 |
| **Total** | **2,624** | |

### Separate 2026–27 edition update branch

Four Cloud Runner edition directories exist in `scert/class-10/official-version-updates`:

| Subject / medium | Official PDF pages | Manifest entries | Actual GitHub page files | Sequence |
|---|---:|---:|---:|---|
| Science TM | 360 | 360 | 360 | 1–360 complete |
| Science EM | 360 | 360 | 360 | 1–360 complete |
| Social Science TM | 368 | 368 | 368 | 1–368 complete |
| Social Science EM | 344 | 344 | 344 | 1–344 complete |
| **Total** | **1,432** | **1,432** | **1,432** | **No numbering gaps** |

The `edition.json` files record download timestamps on 2026-11-04 and the official URLs. Their page-2 imprint extracts identify First Edition 2019, Revised Edition 2020/2022/2023 and Reprint 2021/2024 (with minor OCR/Text Extraction noise in Tamil lines). This separates the academic distribution year 2026–27 from the printed reprint year 2024.

**Validation limitation:** These four edition folders have `manifest.json` and `pages.json`, and their manifest counts match the GitHub page-file counts. A `split_validation.json` was not found. The checked workflow script does not perform a recorded post-split openability/one-page/renderability validation, and it does not store the downloaded master PDF SHA-256. The new branch editions have not yet been compared page-by-page against the production `main` copies. Matching page counts do not prove matching content.

## 3. Eight-book decision table

| Book | Official GET / bytes | Main page set | Stored 2026–27 edition branch | Evidence-based status |
|---|---|---:|---|---|
| Tamil | 200; 57,588,385 bytes; ETag equals recorded local MD5 | 248 | `feature/scert-edition-pilot` contains 248-page official-edition metadata and matching master SHA-256/MD5 | **EXACT MASTER SHA-256 MATCH** |
| English | 200; 68,655,845 bytes | 224 | No separate 2026–27 immutable edition folder found | **MANUAL_REVIEW_REQUIRED** — prior verdict is still `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Mathematics TM | 200; 41,595,088 bytes | 368 | No separate 2026–27 immutable edition folder found | **MANUAL_REVIEW_REQUIRED** — prior verdict is still `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Mathematics EM | 200; 40,902,163 bytes | 352 | No separate 2026–27 immutable edition folder found | **MANUAL_REVIEW_REQUIRED** — prior verdict is still `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Science TM | 200; 109,570,656 bytes | 360 | 360-page official split stored in update branch | **OFFICIAL_SPLIT_STORED; MAIN_COMPARISON_PENDING** |
| Science EM | 200; 105,478,878 bytes | 360 | 360-page official split stored in update branch | **OFFICIAL_SPLIT_STORED; MAIN_COMPARISON_PENDING** |
| Social Science TM | 200; 95,349,305 bytes | 368 | 368-page official split stored in update branch | **OFFICIAL_SPLIT_STORED; MAIN_COMPARISON_PENDING** |
| Social Science EM | 200; 85,480,497 bytes | 344 | 344-page official split stored in update branch | **OFFICIAL_SPLIT_STORED; MAIN_COMPARISON_PENDING** |

### Important correction to the older Class 10 summary

In `docs/official_api_local_match_manifest.csv`, the seven non-Tamil core rows have:

- `verdict = PENDING_CONTENT_AND_EDITION_REVIEW`
- but `standardized_status = VERIFIED_CONTENT_EQUIVALENT`

Those two fields conflict. The `VERIFIED_CONTENT_EQUIVALENT` label is not accepted here. Until the full-page comparison evidence is attached, those seven rows remain pending/manual review.

For Tamil, the checked `feature/scert-edition-pilot` `edition.md` records official master SHA-256 `f638511d...` and MD5 `47d5859a...`; these match the local reverse-audit SHA-256/MD5 and the official ETag/byte size. The stored Tamil edition has 248 pages and page 2 records First Edition 2019 / Revised Editions through 2024.

## 4. Three decision buckets

### Bucket 1 — Official listed and GitHub edition proven identical

- **Tamil only (1 of 8).** The official master SHA-256 and MD5 in the recorded edition metadata match the local master hashes. Retain existing book; no download or replacement needed.

### Bucket 2 — Official listed; GitHub copy exists or official split is stored, but complete equivalence is not proven

- **English, Mathematics TM, Mathematics EM:** existing main page sets exist, but the old audit CSV's source verdict is pending. Re-fetch and compare the official masters before labeling equivalent.
- **Science TM, Science EM, Social Science TM, Social Science EM:** the official 2026–27 Cloud Runner splits are stored on the update branch, and the file inventory is complete. Their main-branch copies have the same page counts, but no all-pages comparison is attached. Do not duplicate-ingest or merge yet.

### Bucket 3 — Official record/release unresolved

- No in-scope Class 10 book was marked HTTP 403 in the existing 2026-11-03 audit manifest; all eight existing source rows record HTTP 200.
- The API itself was not freshly refreshed during this consolidation, so current live API presence must be rechecked before final yearly sign-off.

## 5. Candidate edition that must not be treated as official yet

The older `MASTER_EDITION_AUDIT_REPORT.md` and `CLASS_10_TAMIL_2024_VS_2025_DIFF_ANALYSIS.md` refer to a 184-page / 7-unit 2025 Tamil candidate. The checked GitHub `feature/scert-edition-pilot` branch's official Tamil edition metadata instead records a 248-page 2024 Revised Edition, matching the official API master hash. No official API/CDN URL plus master hash for the 184-page candidate was found in the checked Class 10 evidence. Keep the 184-page candidate as **UNMAPPED_CANDIDATE — NOT OFFICIALLY MATCHED**; do not replace the proven 248-page official copy with it.

## 6. Next actions — catalog-first, no production changes

1. Refresh the live Class 10 API and retain the raw API JSON snapshot, timestamp and SHA-256.
2. Temporarily download the English and Mathematics TM/EM official masters to the Cloud Runner; capture final URL, byte length, SHA-256, PDF page count, page-2 image and exact imprint.
3. Reconstruct/compare every existing main page against the official master for English and both Mathematics editions. Do not accept page count alone.
4. For the four already-split Science/Social editions, add a `split_validation.json` and compare every official split page with the existing main page set; record differing pages and metrics.
5. Keep all work on audit/update branches. Do not overwrite `main`, switch the active edition, merge, deploy or download/re-split already proven-identical books.
