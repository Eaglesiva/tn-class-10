# தமிழ்நாடு அரசு SCERT அதிகாரப்பூர்வ பாடநூல் API vs உள்ளூர் PDF இறுதி தணிக்கை அறிக்கை (Final Corrected Audit Report)

**அதிகாரப்பூர்வ அரசு API:** `https://emis3.tnschools.gov.in/api/get_scert_books`  
**அரசு அதிகாரப்பூர்வ போர்டல்:** [`https://tnschools.gov.in/scert-textbook`](https://tnschools.gov.in/scert-textbook)  
**அரசு CDN தளம்:** `https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/`  
**தணிக்கை செய்யப்பட்ட தேதி:** 2026-11-03  
**ஆய்வு செய்த அமைப்பு:** Antigravity AI Engine (Strict 1-to-1 Mapping & Imprint/HTTP Audit)

---

## 1. 📊 அரசு API 587 பதிவுகளின் இறுதி வகைப்பாடு (Official API 587 Records)

| வகைப்பாடு (Classification) | எண்ணிக்கை (Count) | சதவீதப் பங்கு | விளக்கம் |
|:---|:---:|:---:|:---||
| **அரசு சிறுபான்மை மொழிப் புத்தகங்கள் (`OFFICIAL_MINORITY_LANGUAGE_NO_LOCAL`)** | **323** | 55.0% | தெலுங்கு, உருது, கன்னடம், மலையாளம், இந்தி, சமஸ்கிருதம், அரபு, பிரெஞ்சு (நமது தமிழ்/ஆங்கில ரெப்போவில் இல்லாதவை) |
| **அரசு ஒருங்கிணைந்த பருவப் புத்தகங்கள் (`OFFICIAL_COMBINED_VOLUME_LOCAL_SPLIT`)** | **49** | 7.3% | 1 முதல் 5 வகுப்புகள் வரை அரசு வழங்கும் Vol-I (தமிழ்+ஆங்கிலம்) மற்றும் Vol-II (கணிதம்+EVS) |
| **உள்ளூரில் நேரடித் தொடர்பில்லாத அரசுப் பதிவுகள் (`OFFICIAL_ENTRY_NO_LOCAL_MATCH`)** | **94** | 16.0% | Physics Vol-I/II, Chemistry Vol-I/II, தொழிற்கல்வி, சிறப்புப் பாடங்கள் |
| **அரசு சர்வருடன் 100% நேரடி ஹாஷ் பொருந்தியவை (`EXACT_HASH_MATCH`)** | **38** | 6.5% | 10-ஆம் வகுப்பு தமிழ் உட்பட அச்சுப்பிசகாமல் பொருந்தும் அதிகாரப்பூர்வ பாடங்கள் |
| **உள்ளடக்க & பதிப்பு மறுஆய்வு தேவைப்படுபவை (`PENDING_CONTENT_AND_EDITION_REVIEW`)** | **66** | 11.6% | வெற்றிகரமான HTTP பதில் கிடைத்து, உள்ளடக்கம்/பக்கங்கள்/இரண்டாம் பக்க அச்சு விவரங்கள் ஒப்பிடப்பட வேண்டியவை |
| **அரசு சர்வரில் அணுகல் மறுக்கப்பட்டவை (`DOWNLOAD_FAILED_RETRY_REQUIRED`)** | **17** | 3.6% | HTTP 403 / Size 0 என வந்தவை; இவை தவறான பதிப்புகள் அல்ல, மறுமுயற்சி தேவைப்படும் பதிவுகள் |
| **மொத்த அரசு API பதிவுகள்** | **587** | **100.0%** | SCERT Portal-ல் உள்ள அனைத்துப் பதிவுகளின் முழுமையான கூட்டுத்தொகை |

---

## 2. 🔄 உள்ளூர் 253 முதன்மை Master PDF-களின் தலைகீழ் தணிக்கை (Reverse Audit of 253 Local PDFs)

| உள்ளூர் நிலை (Local Status) | எண்ணிக்கை (Count) | விளக்கம் |
|:---|:---:|:---|
| **அரசு சர்வருடன் 100% நேரடிப் பொருத்தம் (`EXACT_GOVERNMENT_CDN_MATCH`)** | **31** | அரசு CDN கோப்புடன் ஒற்றை பைட் கூட மாறாமல் பொருந்தும் உள்ளூர் மாஸ்டர் PDF-கள் |
| **உள்ளடக்க & பதிப்பு மறுஆய்வு நிலை (`PENDING_CONTENT_AND_EDITION_REVIEW`)** | **44** | சரியான பாட மேப்பிங் செய்யப்பட்டு, பதிப்பு மற்றும் பக்கங்கள் ஆய்வு செய்யப்பட வேண்டியவை |
| **அரசு ஒருங்கிணைந்த புத்தகத்தின் உள்ளூர் பிரிப்பு (`LOCAL_MASTER_REPRESENTED_AS_SPLIT_IN_OFFICIAL_COMBINED`)** | **100** | 1-5 வகுப்புகளில் அரசால் இணைத்து வெளியிடப்பட்ட புத்தகங்களின் உள்ளூர் தனிப்பாடப் பிரிப்புகள் |
| **அரசு சர்வர் மறுமுயற்சி தேவைப்படுபவை (`DOWNLOAD_FAILED_RETRY_REQUIRED`)** | **9** | அரசு சர்வருக்கு HTTP 403 வந்த கோப்புகள் |
| **அரசு போர்டலில் பட்டியலிடப்படாத உள்ளூர் ஆவணங்கள் (`UNMATCHED_IN_OFFICIAL_API`)** | **69** | கூடுதல் பருவங்கள் அல்லது தனித்துவ ஆவணங்கள் |
| **மொத்த உள்ளூர் Master PDF-கள்** | **253** | `tn_school_books/` கீழ் உள்ள அனைத்து மாஸ்டர் கோப்புகள் |

*(அனைத்து 253 உள்ளூர் கோப்புகளின் முழுமையான Reverse Manifest: [`docs/local_master_pdf_reverse_audit.csv`](https://github.com/Eaglesiva/tn-class-10/blob/main/docs/local_master_pdf_reverse_audit.csv)).*

---

## 3. 🏆 10-ஆம் வகுப்பு நிலவரம் & பாதுகாப்பு உறுதிமொழி (Class 10 Production Protection)

| பாடம் | பயிற்று மொழி | அரசு CDN கோப்பு | உள்ளூர் கோப்பு | அரசு அளவு | உள்ளூர் அளவு | தணிக்கை நிலை |
|:---|:---:|:---|:---|:---:|:---:|:---:|
| Tamil | Tamil | `10th_Tamil_Text.pdf` | `Class_10_Tamil_Full_Book.pdf` | 54.92 MB | 54.92 MB | `EXACT_HASH_MATCH` |
| English | English | `10th_English_Text.pdf` | `Class_10_English_Full_Book.pdf` | 65.48 MB | 67.09 MB | `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Mathematics | Tamil | `10th_Mathametics Tamil Medium_Text.pdf` | `Class_10_Maths_TM_Full_Book.pdf` | 39.67 MB | 41.17 MB | `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Mathematics | English | `10th_Mathametics English Medium_Text.pdf` | `Class_10_Maths_EM_Full_Book.pdf` | 39.01 MB | 41.00 MB | `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Science | Tamil | `10th_Science_TM_Text.pdf` | `Class_10_Science_TM_Full.pdf` | 104.49 MB | 56.95 MB | `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Science | English | `10th_Science_EM_Text.pdf` | `Class_10_Science_EM_Full.pdf` | 100.59 MB | 62.48 MB | `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Social Science | Tamil | `10th_Social Science_TM_Text.pdf` | `Class_10_Social_Science_TM_Full.pdf` | 90.93 MB | 58.23 MB | `PENDING_CONTENT_AND_EDITION_REVIEW` |
| Social Science | English | `10th_Social Science_EM_Text.pdf` | `Class_10_Social_Science_EM_Full.pdf` | 81.52 MB | 47.67 MB | `PENDING_CONTENT_AND_EDITION_REVIEW` |

> [!NOTE]
> **உற்பத்திப் பாதுகாப்பு உறுதி:** முந்தைய Cloudflare தளம் இயங்கும் கோப்புகள் (`questions.md`, `quiz.md`, `page_xxx.pdf`, `viewer.html`, `index.html`) எவையும் மாற்றப்படவோ, நீக்கப்படவோ இல்லை. அனைத்தும் 100% பாதுகாப்பாகத் தொடர்கின்றன.
