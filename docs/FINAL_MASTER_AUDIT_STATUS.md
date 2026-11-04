# SCERT Master Textbook Audit & Tracking Status — Classes 1 to 12

**Authoritative Review Date:** 2026-11-05 (Asia/Kolkata)  
**Project Status:** **CATALOG RECONCILIATION IN PROGRESS — NOT COMPLETE**  
**Core Scope:** 165 State Board Tamil & English Medium Academic Textbooks (Classes 1–12)  
**Official GET/HEAD 200 Accessible:** **124 Books**  
**Official GET/HEAD 403 CDN Failed / Unconfirmed:** **41 Books** (16 Officially Released Term-II + 25 Term-III Unconfirmed)  
**Zero Local Master PDF Download:** **100% Compliant (0 bytes downloaded)**  
**Zero Production Main Overwrite:** **100% Compliant**  

---

## 1. Executive Summary & Critical Findings

1. **Classes 4–7 Term-II Missing Download Alert (16 Books)**:
   * **Official Corporation Notification**: On `textbookcorp.in`, sales for Term-II (Classes 1–7) officially commenced on **22 September 2026**.
   * **Current CDN Status**: While Classes 1–3 Term-II are accessible (HTTP 200), the 16 Term-II URLs for Classes 4, 5, 6, and 7 return HTTP 403 on CloudFront.
   * **Classification**: Formally designated as `OFFICIALLY_RELEASED_SALE_COMMENCED; CDN_ACCESS_FAILED_403; RECOVERY_PENDING`. They are confirmed released but require URL/CDN recovery.

2. **Classes 1–7 Term-III Release Watch (25 Books)**:
   * **Status**: 25 Term-III records in the API return HTTP 403.
   * **Release Status**: Price lists list titles for Classes 1–5, but no official 2026–27 release date notification has been published.
   * **Classification**: `RELEASE_STATUS_UNCONFIRMED; CDN_UNAVAILABLE_AT_CHECK; OFFICIAL_WATCH`. Third-party downloads are strictly prohibited until official publication.

3. **Class 10 Discrepancy & Verification Requirements**:
   * **Maths TM, Maths EM, English**: Formally remain `MANUAL_REVIEW_REQUIRED` per Class 10's own audit summary. They must not be prematurely certified as final `GITHUB_IS_NEWER` without full master page comparison.
   * **Science & Social Science (4 books, 1,432 pages)**: Currently stored in unit-level folders on update branch; require restructuring into canonical `editions/2026-27-scert-official/` with formal `split_validation.json` to match Class 11 and Class 12 standards.

4. **Layer 4 Full Content Diff Pending (41 Books — 12,600 Pages)**:
   * Matching page count and Page 2 imprint (Layers 2 & 3) does **not** prove word-for-word textual equivalence.
   * Full textual/visual diff against legacy GitHub `main` editions remains `FULL_DIFF_PENDING` for:
     * **Class 9**: 8 books (2,504 pages)
     * **Class 10**: 1 book — English (224 pages)
     * **Class 12**: 32 books (9,872 pages)

5. **Scope Boundary**:
   * The 165 records cover core State Board Tamil and English medium books. Excluded from this register: CBSE Tamil books, minority language books (Telugu, Kannada, Malayalam, Urdu, Hindi), Classes 1–3 teacher handbooks, and Physical Education guides.

---

## 2. Harmonized Global Page & Status Accounting (Classes 1–12)

| Class | In-Scope Books | Tracked Pages on GitHub | Pages on Update Branch | GitHub Is Newer (2025 Revised) | Same Version on Main (2024 Match) | Audit Branch Split Validated | Term-II Sale Commenced (CDN 403) | Term-III Unconfirmed (403) | Layer 4 Content Diff Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | 9 | 848 | 0 | 0 | 0 | 6 (848p) | 0 | 3 (0p) | Audit Branch Verified |
| **2** | 9 | 824 | 0 | 0 | 0 | 6 (824p) | 0 | 3 (0p) | Audit Branch Verified |
| **3** | 9 | 1,016 | 0 | 0 | 0 | 6 (1,016p) | 0 | 3 (0p) | Audit Branch Verified (Mapping fixed) |
| **4** | 9 | 472 | 0 | 0 | 0 | 3 (472p) | **3 (0p)** | 3 (0p) | Term-II Recovery Pending |
| **5** | 9 | 544 | 0 | 0 | 0 | 3 (544p) | **3 (0p)** | 3 (0p) | Term-II Recovery Pending |
| **6** | 15 | 864 | 0 | 0 | 0 | 5 (864p) | **5 (0p)** | 5 (0p) | Term-II Recovery Pending |
| **7** | 15 | 880 | 0 | 0 | 0 | 5 (880p) | **5 (0p)** | 5 (0p) | Term-II Recovery Pending |
| **8** | 8 | 2,208 | 0 | 0 | 0 | 8 (2,208p) | 0 | 0 | Audit Branch Verified |
| **9** | 8 | 2,504 | 0 | 0 | 0 | 0 | 0 | 0 | **8 Books Pending Diff (2,504p)** |
| **10** | 8 | 2,624 | 1,432 (4 books)* | 2 (720p) | 0 | 0 | 0 | 0 | **3 Manual Review (Maths/Eng)** / 4 Stored Updates (1,432p) |
| **11** | 32 | 10,288 | 7,832 (24 books)** | 4 (1,152p) | 4 (1,304p) | 0 | 0 | 0 | 4 Newer / 4 Same / 23 Stored Updates / 1 Mapping Unresolved |
| **12** | 34 | 10,520 | 648 (2 books) | 0 | 32 (9,872p) | 0 | 0 | 0 | **32 Books Pending Diff (9,872p)** / 2 Stored Updates (648p) |
| **TOTAL** | **165** | **33,592** | **9,912 (30 books)** | **6 (1,872p)** | **36 (11,176p)** | **42 (7,656p)** | **16 (0p)** | **25 (0p)** | **41 Books Pending Diff (12,600p)** |

*\* Class 10 Note: 1,432 pages exist across unit folders; canonical `editions/` restructuring and formal split_validation.json pending.*  
*\*\* Class 11 Note: 7,832 stored pages = 23 Validated Official Updates (7,528p) + 1 API Mapping Unresolved (Chemistry EM Vol 1: 304p).*

---

## 3. Five Core Action Priorities

1. **Priority 1: Official Downloads Recovery (16 Term-II Books)**
   * Classes 4, 5, 6, 7 Term-II books were officially released for sale on 22 September 2026.
   * Investigate government portal CDN routing, S3 keys, and alternate official endpoints to recover HTTP 200 access for these 16 books.

2. **Priority 2: Term-III Release Watch (25 Books)**
   * Keep Classes 1–7 Term-III under official watch. Maintain `RELEASE_STATUS_UNCONFIRMED`. No third-party downloads.

3. **Priority 3: Class 10 Audit Correction & Restructuring**
   * Reconcile Class 10 summary: Maintain `MANUAL_REVIEW_REQUIRED` for Maths TM, Maths EM, and English.
   * Restructure 1,432 pages in Science TM/EM and Social TM/EM into canonical `editions/2026-27-scert-official/` with formal `split_validation.json`.

4. **Priority 4: Layer 4 Content Diff Validation**
   * Perform systematic textual comparison for the 41 books where imprint and page counts match but content diff remains pending (Class 9: 8 books; Class 10: 1 book; Class 12: 32 books).

5. **Priority 5: Mapping Corrections**
   * Class 11 Chemistry EM Vol-1: Maintain `API_MAPPING_UNRESOLVED` (preserve 304 pages).
   * Class 3 Term-II: Fixed label for `TAMIL & ENGLISH_3_II_VOL-I.pdf` to `VOL-I (TAMIL & ENGLISH)`.
