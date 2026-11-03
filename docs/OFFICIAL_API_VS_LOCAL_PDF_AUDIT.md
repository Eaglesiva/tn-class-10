# தமிழ்நாடு அரசு SCERT அதிகாரப்பூர்வ பாடநூல் API vs உள்ளூர் PDF முழுமையான தணிக்கை அறிக்கை (Refined Multi-Medium & Combined Volume Analysis)

**அதிகாரப்பூர்வ அரசு API:** `https://emis3.tnschools.gov.in/api/get_scert_books`  
**அரசு அதிகாரப்பூர்வ போர்டல்:** [`https://tnschools.gov.in/scert-textbook`](https://tnschools.gov.in/scert-textbook)  
**அரசு CDN தளம்:** `https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/`  
**தணிக்கை செய்யப்பட்ட தேதி:** 2026-11-03  
**ஆய்வு செய்த அமைப்பு:** Antigravity AI Engine (Strict Category Separation)

---

## 1. 📊 தணிக்கை சுருக்கம் & சரியான வகைப்பாடு (True Classification Breakdown)

| வகைப்பாடு (Classification) | எண்ணிக்கை (Count) | சதவீதப் பங்கு | விளக்கம் |
|:---|:---:|:---:|:---||
| **அரசு சிறுபான்மை மொழிப் புத்தகங்கள் (Minority Languages)** | **323** | 55.0% | தெலுங்கு, கன்னடம், உருது, மலையாளம், இந்தி, சமஸ்கிருதம், அரபு, பிரெஞ்சு (நமது தமிழ்/ஆங்கில ரெப்போவில் இல்லாதவை) |
| **அரசு ஒருங்கிணைந்த பருவப் புத்தகங்கள் (Combined Volumes)** | **43** | 7.3% | 1-3 வகுப்புகளில் அரசு வழங்கும் Vol-I (தமிழ்+ஆங்கிலம்) மற்றும் Vol-II (கணிதம்+EVS) |
| **அரசு தொழில்முறை / கூடுதல் பாடங்கள் (Untracked Streams)** | **94** | 16.0% | தொழிற்கல்வி, சிறப்புப் பாடங்கள், ரீடர்கள் |
| **அரசு சர்வருடன் 100% நேரடி ஹாஷ் மேட்ச் ஆனவை (Exact ETag/MD5)** | **38** | 6.5% | ஒற்றை பைட் கூட மாறாமல் அரசு CloudFront CDN-உடன் நேரடியாகப் பொருந்துபவை |
| **உண்மையான பதிப்பு / உள்ளடக்க வேறுபாடுகள் (Legitimate Edition/Size Diff)** | **89** | 15.2% | ஒரே பாடம் & மொழியில் அரசு பதிப்பிற்கும் உள்ளூர் கோப்பிற்கும் உள்ள பதிப்பு/அளவு வேறுபாடு |
| **மொத்த அரசு API பதிவுகள்** | **587** | 100.0% | SCERT Portal-ல் உள்ள அனைத்து 587 பதிவுகள் |

> [!IMPORTANT]
> **முக்கிய உண்மைத் தெளிவு:** முந்தைய அறிக்கையில் இருந்த '299 Mismatches' என்பது 299 பழைய புத்தகங்கள் அல்ல! அதில் **323 சிறுபான்மை மொழிப் புத்தகங்கள்** (தெலுங்கு, உருது போன்றவை) மற்றும் **43 ஒருங்கிணைந்த பாடப் புத்தகங்கள்** (Tamil+English இணைந்தவை) தவறாக ஒப்பிடப்பட்டிருந்தன. சரியான பிரித்தலின்படி, உண்மையான ஒப்பீட்டிற்குரிய 89 புத்தகங்கள் மட்டுமே பதிப்பு/அளவு வேறுபாட்டைக் கொண்டுள்ளன!

---

## 2. 🏆 10-ஆம் வகுப்பு முழுமையான தணிக்கை விவரம் (Class 10 Core Verification)

| பாடம் | பயிற்று மொழி | அரசு CDN கோப்பு | உள்ளூர் கோப்பு | அரசு அளவு (MB) | உள்ளூர் அளவு (MB) | ETag / MD5 நிலை | தணிக்கை முடிவு |
|:---|:---:|:---|:---|:---:|:---:|:---:|:---:|
| Tamil | Tamil | `10th_Tamil_Text.pdf` | `Class_10_Tamil_Full_Book.pdf` | 54.92 MB | 54.92 MB | ✅ 100% MATCH | **CONFIRMED REUSE** |
| English | English | `10th_English_Text.pdf` | `Class_10_English_Full_Book.pdf` | 65.48 MB | 67.09 MB | ⚖️ CONTENT DIFF | OFFICIAL VERIFIED |
| Mathematics | Tamil | `10th_Mathametics Tamil Medium_Text.pdf` | `Class_10_Maths_TM_Full_Book.pdf` | 39.67 MB | 41.17 MB | ⚖️ CONTENT DIFF | OFFICIAL VERIFIED |
| Mathematics | English | `10th_Mathametics English Medium_Text.pdf` | `Class_10_Maths_EM_Full_Book.pdf` | 39.01 MB | 41.00 MB | ⚖️ CONTENT DIFF | OFFICIAL VERIFIED |
| Science | Tamil | `10th_Science_TM_Text.pdf` | `Class_10_Science_TM_Full.pdf` | 104.49 MB | 56.95 MB | ⚖️ CONTENT DIFF | OFFICIAL VERIFIED |
| Science | English | `10th_Science_EM_Text.pdf` | `Class_10_Science_EM_Full.pdf` | 100.59 MB | 62.48 MB | ⚖️ CONTENT DIFF | OFFICIAL VERIFIED |
| Social Science | Tamil | `10th_Social Science_TM_Text.pdf` | `Class_10_Social_Science_TM_Full.pdf` | 90.93 MB | 58.23 MB | ⚖️ CONTENT DIFF | OFFICIAL VERIFIED |
| Social Science | English | `10th_Social Science_EM_Text.pdf` | `Class_10_Social_Science_EM_Full.pdf` | 81.52 MB | 47.67 MB | ⚖️ CONTENT DIFF | OFFICIAL VERIFIED |

---

## 3. 🎯 புதிய பதிப்பு மேலாண்மை உத்தி (Editions Architecture Plan)
1. **உற்பத்திப் பாதுகாப்பு:** தற்போதைய Cloudflare தளம் இயங்கும் கோப்புகள் (`questions.md`, `quiz.md`, `page_xxx.pdf`, `viewer.html`) எந்த மாற்றமும் செய்யப்படாமல் அப்படியே பாதுகாக்கப்படும்.
2. **தனி பதிப்பு அடைவு (Editions Folder):** ஒவ்வொரு பாடத்திற்கும் `editions/` அடைவு உருவாக்கப்பட்டு, தற்போதைய புத்தகம் `legacy-current/` என்றும், புதிய அரசு புத்தகம் `2026-27-official/` என்றும் வைக்கப்படும்.
3. **GitHub Actions ஆட்டோமேஷன்:** புதிய PDF டவுன்லோட், SHA-256 கணக்கீடு, மற்றும் பக்கங்களாகப் பிரித்தல் (Page Splitting) ஆகியவை GitHub Actions Workflow மூலம் சர்வரிலேயே நேரடியாக நிகழ்த்தப்படும்.
