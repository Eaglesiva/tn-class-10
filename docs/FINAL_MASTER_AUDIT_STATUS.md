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
   * **Release Status**: The official Textbook Corporation 2026–2027 Price List (`PRICELIST.pdf`) covers only Term-I and Term-II; Term-III is not listed or priced in current notices. Status remains strictly unconfirmed pending official publication.
   * **Classification**: `RELEASE_STATUS_UNCONFIRMED; CDN_UNAVAILABLE_AT_CHECK; OFFICIAL_WATCH`. Third-party downloads are strictly prohibited until official publication.

3. **Class 10 Categorization & Verification Requirements (8 Books — 2,624 Pages)**:
   * **Tamil (1 book — 248p)**: `EXACT_MASTER_SHA256_MATCH` (bit-for-bit identical to official master PDF).
   * **Maths TM & EM (2 books — 720p)**: `MANUAL_REVIEW_REQUIRED` (temporarily excluded from confirmed GitHub Newer pending full master page comparison against refreshed API snapshot).
   * **English (1 book — 224p)**: `IMPRINT_AND_PAGE_COUNT_MATCHED; CONTENT_DIFF_PENDING`.
   * **Science & Social Science (4 books — 1,432p)**: `VERSION_DIFFERENT; OFFICIAL_SPLIT_STORED_IN_UPDATE_BRANCH` (pages verified and structured in canonical `editions/2026-27-scert-official/` with continuous `manifest.json`; Layer 4 content diff against main pending).

4. **Confirmed GitHub Is Newer Books (4 Books — 1,152 Pages)**:
   * Confirmed exclusively for **Class 11** (Tamil 176p, Maths TM Vol 1 320p, Maths TM Vol 2 288p, Maths EM Vol 1 368p = 1,152p).

5. **Layer 4 Full Content Diff Progress (2 Verified Equivalent / 39 Books Remaining — 12,104 Pages)**:
   * Matching page count and Page 2 imprint (Layers 2 & 3) does **not** prove word-for-word textual equivalence.
   * **Pilots Completed**:
     * Class 9 English (224p): 224/224 pages (100.0%) exact word-for-word match (commit `a2c6840f`).
     * Class 9 Tamil (272p): 270/272 pages exact raw match, 272/272 pages whitespace-collapsed match (`TEXT_EQUIVALENT_AFTER_WHITESPACE_NORMALIZATION`, 99.99% overall similarity, 0 words altered; commit `2f991681`).
   * Full textual diff against legacy GitHub `main` editions remains `FULL_DIFF_PENDING` for 39 books (12,104 pages):
     * **Class 9**: 6 books (2,008 pages)
     * **Class 10**: 1 book — English (224 pages)
     * **Class 12**: 32 books (9,872 pages)

6. **Scope Boundary**:
   * The 165 records cover core State Board Tamil and English medium books. Excluded from this register: CBSE Tamil books, minority language books (Telugu, Kannada, Malayalam, Urdu, Hindi), Classes 1–3 teacher handbooks, and Physical Education guides.

---

## 2. Harmonized Global Page & Status Accounting (Classes 1–12)

| Class | In-Scope Books | Tracked Pages on GitHub | Pages on Update Branch | Confirmed GitHub Newer (2025) | Same Version on Main (2024) | Manual Review Required | Audit Branch Split Validated | Term-II Sale Commenced (403) | Term-III Unconfirmed (403) | Layer 4 Content Diff Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | 9 | 848 | 0 | 0 | 0 | 0 | 6 (848p) | 0 | 3 (0p) | Audit Branch Verified |
| **2** | 9 | 824 | 0 | 0 | 0 | 0 | 6 (824p) | 0 | 3 (0p) | Audit Branch Verified |
| **3** | 9 | 1,016 | 0 | 0 | 0 | 0 | 6 (1,016p) | 0 | 3 (0p) | Audit Branch Verified (Mapping fixed) |
| **4** | 9 | 472 | 0 | 0 | 0 | 0 | 3 (472p) | **3 (0p)** | 3 (0p) | Term-II Recovery Pending |
| **5** | 9 | 544 | 0 | 0 | 0 | 0 | 3 (544p) | **3 (0p)** | 3 (0p) | Term-II Recovery Pending |
| **6** | 15 | 864 | 0 | 0 | 0 | 0 | 5 (864p) | **5 (0p)** | 5 (0p) | Term-II Recovery Pending |
| **7** | 15 | 880 | 0 | 0 | 0 | 0 | 5 (880p) | **5 (0p)** | 5 (0p) | Term-II Recovery Pending |
| **8** | 8 | 2,208 | 0 | 0 | 0 | 0 | 8 (2,208p) | 0 | 0 | Audit Branch Verified |
| **9** | 8 | 2,504 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 Verified Equivalent (496p) / **6 Books Pending Diff (2,008p)** |
| **10** | 8 | 2,624 | 1,432 (4 books)* | 0 | 0 | **2 (720p)** | 0 | 0 | 0 | 1 Exact SHA / **2 Manual Review** / **1 Pending Diff (224p)** / 4 Stored Updates |
| **11** | 32 | 10,288 | 7,832 (24 books)** | **4 (1,152p)** | 4 (1,304p) | 0 | 0 | 0 | 0 | 4 Newer / 4 Same / 23 Stored Updates / 1 Mapping Unresolved |
| **12** | 34 | 10,520 | 648 (2 books) | 0 | 32 (9,872p) | 0 | 0 | 0 | 0 | **32 Books Pending Diff (9,872p)** / 2 Stored Updates (648p) |
| **TOTAL** | **165** | **33,592** | **9,912 (30 books)** | **4 (1,152p)** | **36 (11,176p)** | **2 (720p)** | **42 (7,656p)** | **16 (0p)** | **25 (0p)** | 2 Verified Equivalent (496p) / **39 Books Pending Diff (12,104p)** |

*\* Class 10 Note: 1,432 pages across 4 edition folders on update branch (Science TM 360p, Science EM 360p, Social TM 368p, Social EM 344p) are sequentially verified and validated with manifest.json. Layer 4 content diff against main is pending.*  
*\*\* Class 11 Note: 7,832 stored pages = 23 Validated Official Updates (7,528p) + 1 API Mapping Unresolved (Chemistry EM Vol 1: 304p).*

---

## 3. Disambiguation of Storage vs Classification Metrics

1. **Pages Physically Present on Update Branches**:
   * Class 10 (`scert/class-10/official-version-updates`): 4 books = **1,432 pages**
   * Class 11 (`scert/class-11/official-version-updates`): 24 books = **7,832 pages**
   * Class 12 (`scert/class-12/official-version-updates`): 2 books = **648 pages**
   * **Total Pages Physically Stored on Update Branches**: **9,912 pages** across **30 edition directories**.

2. **Categorical Classification of Update Branch Pages**:
   * **Validated Official Edition Updates**: 29 books = **9,608 pages** (Class 10: 1,432p; Class 11: 7,528p; Class 12: 648p).
   * **API Mapping Unresolved**: 1 book = **304 pages** (Class 11 Chemistry EM Vol 1: SCERT API duplicated Vol-2 URL; genuine Vol-1 split pages preserved on branch pending official API fix).

3. **Baseline Editions on Production `main`**:
   * **Confirmed GitHub Is Newer (2025 Revised Edition)**: 4 books = **1,152 pages** (Class 11 Tamil, Maths TM 1/2, Maths EM 1).
   * **Same Version (2024 Reprint Match)**: 36 books = **11,176 pages** (Class 11: 1,304p; Class 12: 9,872p).
   * **Exact Master SHA-256 Match**: 1 book = **248 pages** (Class 10 Tamil).
   * **Manual Review Required**: 2 books = **720 pages** (Class 10 Maths TM & EM).

---

## 4. Five Core Action Priorities

1. **Priority 1: Official Downloads Recovery (16 Term-II Books)**
   * Classes 4, 5, 6, 7 Term-II books were officially released for sale on 22 September 2026.
   * Investigate government portal CDN routing, S3 keys, and alternate official endpoints to recover HTTP 200 access for these 16 books.

2. **Priority 2: Term-III Release Watch (25 Books)**
   * Keep Classes 1–7 Term-III under official watch. Maintain `RELEASE_STATUS_UNCONFIRMED`. No third-party downloads.

3. **Priority 3: Class 10 Audit Correction & Restructuring**
   * Maintain `MANUAL_REVIEW_REQUIRED` for Maths TM (368p) and Maths EM (352p).
   * Verify 1,432 pages in Science TM/EM and Social TM/EM stored in canonical `editions/2026-27-scert-official/` against main text for Layer 4 diff.

4. **Priority 4: Layer 4 Content Diff Validation**
   * Perform systematic textual comparison for the 39 books where imprint and page counts match but content diff remains pending (Class 9: 6 books / 2,008p; Class 10: 1 book / 224p; Class 12: 32 books / 9,872p).

5. **Priority 5: Mapping Corrections**
   * Class 11 Chemistry EM Vol-1: Maintain `API_MAPPING_UNRESOLVED` (preserve 304 pages).
   * Class 3 Term-II: Fixed label for `TAMIL & ENGLISH_3_II_VOL-I.pdf` to `VOL-I (TAMIL & ENGLISH)` across Master Index and Class 3 Audit Manifest.
