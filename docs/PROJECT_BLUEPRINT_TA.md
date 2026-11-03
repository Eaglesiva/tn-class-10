# TN Samacheer Kalvi — Project Blueprint & Source Research Report

> **ஆவண நிலை:** Working Blueprint / Initial Source Research  
> **ஆய்வு தேதி:** 03-11-2026  
> **மொழி:** தமிழ் + தேவையான Technical English  
> **Repository Reference:** [Eaglesiva/tn-class-10](https://github.com/Eaglesiva/tn-class-10)

## 1. Project நோக்கம்

தமிழ்நாடு Samacheer Kalvi வகுப்பு 1–12 பாடப்புத்தகங்களில் உள்ள Book Back Questions-ஐச் சரிபார்த்து, இரண்டு தனித்தனி பணிகளைச் செய்வது:

1. **Quiz Creation:** ஏற்கெனவே One-word / Objective / MCQ வடிவில் உள்ள கேள்விகளை மட்டும் Quiz-ஆக அமைத்தல்.
2. **Answer Reference Collection:** Book Back-ல் உள்ள எல்லா வகைக் கேள்விகளுக்கும் Website, Professional Guide PDF மற்றும் தேவையான பிற வெளிப்புற Source-களிலிருந்து பதில்களைச் சேகரித்தல்.

பல Source-களின் பதில்களை ஒப்பிட்ட பிறகே நம்முடைய சொந்த wording-ல் Final Answers உருவாக்கப்படும். ஆரம்ப Reference Collection-ஐ Final Answer என்று கருதக்கூடாது.

GitHub இந்தப் பணிக்கான Common Working Space. இது Final Student-facing Website அல்ல. புதிய Chat அல்லது வேறு AI / Developer இந்த ஆவணத்தைப் படித்தாலும் Project நோக்கம், முடிவுகள், Source பட்டியல், அடுத்த வேலை ஆகியவை புரிந்து தொடரக்கூடியதாக இருக்க வேண்டும்.

## 2. Finalized Decisions — இதுவரை எடுக்கப்பட்ட முடிவுகள்

| எண் | முடிவு | செயல்படுத்த வேண்டிய விதி |
|---|---|---|
| 1 | ஏற்கெனவே Extract செய்த கேள்விகளே அடிப்படை | Existing questions.md-ஐப் பயன்படுத்த வேண்டும்; தேவையில்லாமல் மீண்டும் Extract செய்ய வேண்டாம் |
| 2 | PDF தான் Cross-check Reference | சந்தேகமான கேள்வியை அதற்குரிய PDF Page-ல் திறந்து சரிபார்க்க வேண்டும் |
| 3 | Quiz-ல் Objective Questions மட்டும் | One-word / Objective / Textbook-ல் ஏற்கெனவே MCQ வடிவில் உள்ளவை மட்டும் |
| 4 | பெரிய கேள்விகளை MCQ-ஆக மாற்ற வேண்டாம் | குறுவினா, சிறுவினா, நெடுவினா, விளக்கவுரை, கட்டுரை, Homework / Writing Tasks Quiz-ல் வரக்கூடாது |
| 5 | answers.md-ல் எல்லா கேள்விகளும் இடம்பெற வேண்டும் | One-mark முதல் நீண்ட விளக்கக் கேள்விகள் வரை அனைத்துக்கும் Source தேட வேண்டும் |
| 6 | Answer-க்கு External Source கட்டாயம் | AI Training Data, சொந்த அறிவு அல்லது ஊகத்திலிருந்து Answer உருவாக்கக்கூடாது |
| 7 | குறிப்பிட்ட Page Link கட்டாயம் | அந்தப் பாடம் / கேள்விக்கான பதில் உள்ள நேரடி URL வேண்டும்; Homepage மட்டும் போதாது |
| 8 | PDF Source-க்கு Page Number தேவை | Publisher, Guide Title, Edition, Class, Subject, Medium, Term, PDF Page பதிவு செய்ய வேண்டும் |
| 9 | Source எண்ணிக்கை கட்டாயமாக ஐந்து அல்ல | 1, 2, 3 அல்லது அதற்கு மேல் — உண்மையில் Answer உள்ள Source-களை மட்டுமே பதிவு செய்ய வேண்டும் |
| 10 | Round-wise Collection | முதலில் அதிக Coverage உள்ள Source; பிறகு விடுபட்ட கேள்விகள் மற்றும் மாற்று பதில்களுக்கு அடுத்த Source |
| 11 | Final Answer பின்னர் | Reference சேகரிப்பு மற்றும் ஒப்பீடு முடிந்த பிறகே சொந்த Final Answer உருவாக்க வேண்டும் |
| 12 | Lesson Folder எளிமையாக இருக்க வேண்டும் | தேவையில்லாத புதிய Files-ஐ ஒவ்வொரு Chapter Folder-க்கும் சேர்க்கக்கூடாது |
| 13 | GitHub Common Working Space | பல AI tools ஒரே Repository-ஐ அணுகவும், ஒரே Reference-இலிருந்து பணியைத் தொடரவும் |
| 14 | வேலை முடிந்ததும் Local Copy | தேவையான Files-ஐ Local-ஆக எடுத்துக்கொண்டு Public Repository-யிலிருந்து அகற்ற திட்டமிடப்பட்டுள்ளது |

## 3. Repository மற்றும் File Structure

தற்போது நேரடியாகச் சரிபார்க்கப்பட்ட Repository:

[https://github.com/Eaglesiva/tn-class-10](https://github.com/Eaglesiva/tn-class-10)

இதில் Class 10 Subject Folders உள்ளன. இதன் தற்போதைய Folder Structure-ஐ மற்ற வகுப்புகளுக்கு Template ஆகப் பயன்படுத்தலாம். இந்த Blueprint Classes 1–12 முழுவதற்குமானது; ஆனால் மற்ற வகுப்புகளின் Repository URLs / Access இன்னும் தனியாகச் சரிபார்க்கப்பட வேண்டும்.

### ஒவ்வொரு Chapter-ன் File Structure

    <subject>/
    └── <chapter>/
        └── book_back_questions/
            ├── questions.md
            ├── quiz.md
            ├── quiz.json
            └── answers.md

| File | நோக்கம் |
|---|---|
| **questions.md** | ஏற்கெனவே Extract செய்த Original Book Back Questions; PDF-உடன் Cross-check |
| **quiz.md** | மாணவர்களுக்கான வாசிக்க எளிய Quiz |
| **quiz.json** | Quiz-க்கான Structured Data; quiz.md-க்கு ஒத்த Data |
| **answers.md** | எல்லா Book Back Questions-க்குமான Source-wise Answer References |

Project-level Blueprint மற்றும் Source Research Report மட்டும் Repository Root-ல் தனி docs/ Documentation Folder-ல் இருக்கும். இந்த ஆவணம் அந்த Project-level Document ஆகும்.

## 4. Quiz Creation Rules

### Quiz-ல் சேர்க்க வேண்டியவை

- ஏற்கெனவே One-word / One-mark Answer வகையில் உள்ள கேள்விகள்.
- பலவுள் தெரிக போன்ற Objective / MCQ கேள்விகள்.
- பாடப்புத்தகத்தில் ஏற்கெனவே நான்கு Options கொடுக்கப்பட்டுள்ள கேள்விகள்.
- தெளிவான ஒரே சரியான விடையுடன் Objective வடிவில் அமைக்கக்கூடிய பொருத்துக வினாக்கள் மட்டும்.

### Quiz-ல் சேர்க்கக்கூடாதவை

- குறுவினா, சிறுவினா, நெடுவினா.
- 2 / 5 / 10 மதிப்பெண் விளக்கக் கேள்விகள்.
- கட்டுரை, Paragraph, விரிவான விடை.
- வீட்டுப்பாடம் / எழுதிப் பழகும் / Open-ended Writing Tasks.

இந்தக் கேள்விகள் answers.md-ல் இடம்பெறும். அவற்றை செயற்கையாக MCQ-ஆக மாற்றக்கூடாது.

### Quiz Quality Rules

1. ஒவ்வொரு MCQ-க்கும் நான்கு Options.
2. ஒரே ஒரு Correct Answer மட்டுமே.
3. மூன்று தவறான Options நம்பகமான Distractors ஆக இருக்க வேண்டும்.
4. இரண்டு Options-மும் சரியாக இருக்கக்கூடிய கேள்வியை வெளியிடக்கூடாது.
5. கேள்வியின் அசல் பொருள் / நோக்கம் மாறக்கூடாது.
6. Textbook PDF-ஐ வைத்து Options மற்றும் Answer சரிபார்க்க வேண்டும்.
7. quiz.md மற்றும் quiz.json இரண்டிலும் ஒரே கேள்வி, Options, Correct Answer இருக்கிறதா Validate செய்ய வேண்டும்.
8. நிலையான Question ID வைத்தால் Update மற்றும் Cross-check எளிதாகும்.

## 5. Answers Collection — முக்கிய Workflow

### 5.1 answers.md என்பது முதலில் Reference Collection

ஒவ்வொரு Book Back Question-க்கும் கிடைக்கும் ஒவ்வொரு உண்மையான Source-இலிருந்தும் பதில் சேகரிக்கப்படும்.

- Website என்றால் அந்த Answer இருக்கும் குறிப்பிட்ட Page URL.
- PDF என்றால் நேரடி PDF Link, Guide விவரம், PDF Page Number.
- App என்றால் App பெயர், Store Link, அதற்குள் உள்ள குறிப்பிட்ட Answer-ஐ எவ்வாறு சரிபார்த்தோம் என்ற விவரம்.
- Answer இல்லையென்றால் ANSWER_NOT_FOUND / NO_ANSWER_ON_PAGE என்று பதிவு செய்ய வேண்டும்.
- Page-ல் Answer இல்லாதபோது Website பெயரை மட்டும் வைத்து Answer உள்ளது என்று காட்டக்கூடாது.
- AI-ன் சொந்த அறிவால் Source Answer-ஐ நிரப்பக்கூடாது.
- Source-களின் பதில்கள் மாறுபட்டால் அனைத்தையும் தனித்தனியாகப் பதிவு செய்ய வேண்டும். உடனே ஒன்றைத் தேர்ந்தெடுக்க வேண்டாம்.

### 5.2 ஒவ்வொரு Question-க்கான Reference Record

    Question ID: T10-U01-Q001

    Original Question:
    [questions.md-ல் உள்ள அசல் கேள்வி]

    Source 1 — Website:
    Website Name:
    Direct Answer Page:
    Access Date:
    Edition / Syllabus:
    Answer Status: FOUND

    Source Answer:
    [Source-ல் உண்மையில் உள்ள பதிலுக்கான Reference Record]

    Source 2 — Professional Guide PDF:
    Publisher:
    Guide Title:
    Class / Subject:
    Medium:
    Term:
    Edition / Year:
    Direct PDF:
    PDF Page:
    Answer Status: FOUND

    Source Answer:
    [PDF-ல் உள்ள பதிலுக்கான Reference Record]

    Source 3:
    ...

    Collection Status:
    Sources checked:
    Sources with answer:
    Sources not found:
    Conflicts / Notes:
    Final Answer: NOT CREATED YET

### 5.3 Round-wise Source Collection

| Round | பணி |
|---|---|
| Round 0 | Website, Guide PDF, App Source-களை அடையாளம் காணுதல்; Source Coverage Audit |
| Round 1 | அதிக Coverage கொண்ட Website / Guide Source-ல் முதலில் Answers சேகரித்தல் |
| Round 2 | முதல் Source-ல் விடுபட்ட கேள்விகளை இரண்டாவது Source-ல் தேடுதல் |
| Round 3 | வேறுபட்ட விளக்கங்கள் மற்றும் கூடுதல் Answers-ஐ மூன்றாவது Source-ல் சேகரித்தல் |
| Round 4+ | தேவைப்பட்டால் கூடுதல் Source-களில் தொடருதல் |
| Final Comparison | Reference-களை ஒப்பிட்டு, பின்னர் சொந்த wording-ல் Final Answers உருவாக்குதல் |

ஐந்து Source என்பது கட்டாய எண்ணிக்கை அல்ல. உண்மையில் பதில் உள்ள தரமான Source எத்தனை கிடைக்கிறதோ அவ்வளவையே பதிவு செய்ய வேண்டும்.

### 5.4 Website மற்றும் PDF Reference-களில் பதிவு செய்ய வேண்டியவை

| விவரம் | Website | Guide PDF |
|---|---|---|
| Direct Reference | குறிப்பிட்ட Answer Page URL | நேரடி PDF Link |
| Answer Location | Page URL + Section | PDF Page Number |
| Edition | Page-ல் உள்ள ஆண்டு / பாடத்திட்டம் | Guide Edition / Academic Year |
| Medium | TM / EM | TM / EM |
| Term | Term 1 / 2 / 3 / Annual | Term 1 / 2 / 3 / Full Year |
| Verification | பக்கத்தைத் திறந்து Answer இருப்பதைப் பார்க்க வேண்டும் | PDF திறந்து குறிப்பிட்ட Page-ல் Answer இருப்பதைப் பார்க்க வேண்டும் |

Search Result-ல் Website பெயர் அல்லது Download Link தெரிகிறது என்பதற்காக மட்டும் Verified Answer Source என்று கருதக்கூடாது. குறிப்பிட்ட கேள்வியின் பதில் உண்மையில் அந்தப் பக்கத்தில் / PDF Page-ல் இருக்க வேண்டும்.

---

## 6. Source Research Report — ஆரம்ப Source பட்டியல்

இந்தப் பட்டியல் 03-11-2026 அன்று நடந்த ஆரம்ப Web Research அடிப்படையில் தொகுக்கப்பட்டது. இது முழுமையான Coverage Audit அல்ல. ஒவ்வொரு Class / Subject / Medium / Term / Chapter-க்கும் தனியாகச் சரிபார்க்க வேண்டிய Source Candidates.

### A. Answer Websites — நேரடி பதில்கள்

| Source | முக்கிய இணைப்பு | இப்போது தெரிந்த Coverage / பயன்பாடு | நிலை / கவனம் |
|---|---|---|---|
| **BrainKart** | [1st–12th State Board Index](https://www.brainkart.com/materials/1st-to-12th---tamilnadu-state-board-school-%28english-and-tamil-medium%29-1001/) | 1–12 TM/EM என்று Class Index; Book Back Answers, One Mark, Guides போன்றவை பட்டியலிடப்பட்டுள்ளன | **High Priority.** Class-wise index உள்ளது; எல்லா பாடங்களிலும் முழு Answers உள்ளதா Audit செய்ய வேண்டும் |
| **BrainKart — Example Answer Page** | [10th Tamil — இயல் 1](https://www.brainkart.in/article/Questions-and-Answers_11807/) | ஒரு மதிப்பெண், குறுவினா, சிறுவினா, நெடுவினா போன்ற பல Question Types | குறிப்பிட்ட பாடத்திற்கான உண்மையான Answer Page எடுத்துக்காட்டு |
| **FreeTNBooks** | [Book Back Questions Index](https://www.freetnbooks.com/samacheer-kalvi-book-back-questions/) | Tamil: Class 3–12; English: Class 5–12 என்று பக்கத்தில் தெளிவாகக் காணப்படுகிறது. பிற Subject Links-யும் உள்ளன | **High Priority.** 1–2க்கு Answer Coverage இந்தப் பக்கத்தில் உறுதி செய்யப்படவில்லை |
| **Padasalai** | [10th Guide / Book Back / Answer Key Index](https://www.padasalai.net/2025/06/10th-Standard-Book-Back-Questions-and-Answer-Keys-Full-Guide.html) | Guide, Answer Key, Question Paper, Study Material Index | Index / Material Source; ஒவ்வொரு Destination Page-ஐத் திறந்து சரிபார்க்க வேண்டும் |
| **KalviTips** | [10th Tamil — Unit 1 Answers](https://www.kalvitips.com/2025/05/10th-tamil-book-back-answers-unit-1-guide-tamilnadu-school-books.html) | 10ஆம் வகுப்பு தமிழ் இயல் 1-க்கான பாடம்-குறிப்பிட்ட Answer Page | நேரடி Answer Source; பிற Class / Subject Coverage தனியாக Audit |
| **Kalvi Imayam** | [12th All Subject Book Back Answers](https://www.kalviimayam.com/2023/02/12th-all-subject-guide-book-back-answers.html) | 12ஆம் வகுப்பு பல பாடங்களுக்கு Book Back Answer Links | 2023 பக்கம்; தற்போதைய Edition-ஐ உறுதிப்படுத்த வேண்டும் |
| **StudentsGuide360** | [10th Tamil Unit 1–9](https://www.studentsguide360.com/10th-tamil-guide-unit-1-to-9-full-answers/) | 10ஆம் வகுப்பு தமிழ் பாடம் வாரியான Answer Material | பழைய / குறைக்கப்பட்ட பாடத்திட்டம் இருக்கலாம் |
| **GreenTamil** | [10th Tamil — இயல் 1](https://www.greentamil.in/2021/06/1-10-tamil-iyal-1-book-back-question.html) | 10ஆம் வகுப்பு தமிழ் Unit 1க்கு கூடுதல் Answer Reference | பழைய பக்கம்; தற்போதைய Textbook Edition-உடன் பொருத்திப் பார்க்க வேண்டும் |
| **eKalvi** | [Solutions Index](https://ekalvi.in/solutions/) | சில வகுப்புகள் / பாடங்களுக்கு Solutions | Partial Source Candidate; முழு 1–12 coverage என்று கருத வேண்டாம் |
| **Nibunan** | [Tamil Study Material](https://nibunan.in/clear-tnpsc-tamil/) | கூடுதல் One-mark / தமிழ் கேள்வி-பதில் போன்றவற்றுக்கு உதவலாம் | Book Back Answer-களுக்கான முதன்மை Source அல்ல; Supplementary மட்டும் |

**Source Independence கவனம்:** BrainKart .com / .in பக்கங்கள் அல்லது ஒரே Content-ஐ Mirror செய்யும் தளங்களை இரண்டு சுயாதீன Sources என்று எண்ணக்கூடாது. Content Origin தெரிந்தால் பதிவு செய்ய வேண்டும்.

### B. Guide PDF Index / Download Websites

| Source | இணைப்பு | பயன்பாடு | கவனம் |
|---|---|---|---|
| **Samacheer Kalvi Students** | [Class 1–12 Guide Index](https://samacheerkalvistudents.in/tamilnadu-school-guides/) | 1–12 Classes; Tamil / English Medium மற்றும் Subject-wise Guide பட்டியல் | Class Pages-ல் நேரடி PDF உள்ளதா திறந்து சரிபார்க்க வேண்டும்; பழைய PDF-களும் இருக்கலாம் |
| Class 1 Guide Page | [1st Standard](https://samacheerkalvistudents.in/tamilnadu-school-guides/1st-standard.html) | Primary Guides, TM/EM என்று பட்டியலிடுகிறது | Term / Edition / Download File சரிபார்ப்பு அவசியம் |
| **KalviMani** | [Main Website](https://kalvimani.in/) | 2026–27 Textbooks; 1–12 Guides 2024–2026; TM/EM மற்றும் Primary Guide Hub என்று தெரிவிக்கிறது | Browser fetch சில நேரங்களில் 521 Error கொடுத்தது; நேரடியாக திறந்து PDF Links சரிபார்க்க வேண்டும் |
| KalviMani Primary | [Classes 1–5 Guides](https://kalvimani.in/primary-school-guides/) | Primary Guide PDF தேடல் | Term மற்றும் உண்மையான PDF Edition சரிபார்க்க வேண்டும் |
| KalviMani — Class 10 | [10th Sura Guides](https://kalvimani.in/10th-standard/sura-guides/) | 10ஆம் வகுப்பு Sura Guide பட்டியல் | PDF Download / Edition சரிபார்ப்பு |
| KalviMani — Class 11 | [11th Sura Guides](https://kalvimani.in/11th-standard/sura-guides/) | 11ஆம் வகுப்பு Guide பட்டியல் | PDF Download / Medium சரிபார்ப்பு |
| KalviMani — Class 12 | [12th Sura Guides](https://kalvimani.in/12th-standard/sura-guides/) | 12ஆம் வகுப்பு Guide பட்டியல் | Subject / Stream / Medium சரிபார்ப்பு |
| **Kalvi Kadal** | [Site Map](https://www.kalvikadal.in/p/sitemap.html) | 9th–12th Guide PDF, Question Paper, Answer Keys, Materials | சில Page-கள் பழைய தேதியுடன் இருக்கலாம்; உள்ளே உள்ள PDF Link-ஐச் சரிபார்க்க வேண்டும் |
| **Tamilaruvi** | [6th–12th All Subject Full Guides](https://www.tamilaruvi.in/p/6th-to-12th-all-subject-full-study.html) | 6–12க்கு Sura, Don, Way to Success, Selection, Penguin, Brilliants, EC Loyola போன்ற Publisher Guides | 2026–27 என்று பட்டியல் கூறுகிறது; PDF Edition / Medium / Page சரிபார்க்க வேண்டும் |
| Tamilaruvi — Class 10 | [10th All Subject Full Guides](https://www.tamilaruvi.in/p/10th-all-subject-full-study-guide.html) | 10ஆம் வகுப்பு பல Publisher Guide-கள் | சில PDF-கள் மூன்றாம் தரப்பு Upload / Mirror; Origin அறிய வேண்டும் |
| Tamilaruvi — Class 11 | [11th Full Guide Collection](https://www.tamilaruvi.in/2022/08/11th-standard-all-subjects-full-study-guides-collection-tamil-medium-and-english-medium-download-pdf.html) | 11ஆம் வகுப்பு பாடங்கள், TM/EM, பல Publishers | பழைய URL; தற்போதைய Download Links தனியாகச் சரிபார்க்க வேண்டும் |
| Tamilaruvi — 2024–25 Collection | [6th–12th 2024–25 Guide List](https://www.tamilaruvi.in/2024/07/tamilnadu-schools-notes-guides-all-subjects-pdf-download-6th-to-12th-all-subjects-full-study-guides-notes-2024-2025.html) | பழைய Editions-ஐ ஒப்பிடவும் | 2026–27 Answer Source ஆக நேரடியாகப் பயன்படுத்த வேண்டாம் |
| **NCERTBooksPDF** | [Tamil Nadu Textbook PDF Index](https://ncertbookspdf.com/tamilnadu-samacheer-kalvi-books/) | 2026–27 Textbook PDF Class 1–12 TM/EM Index | Textbook Source மட்டுமே; Guide Answer Source என்று கருத வேண்டாம் |

### C. Professional Guide Publishers

இவை Publisher / Guide பெயர்கள். ஒவ்வொரு Publisher-ன் முழு PDF இலவசமாகக் கிடைக்கிறது என்று அர்த்தமில்லை.

| Publisher / Guide | எங்கு காணப்பட்டது | Coverage Candidate | சரிபார்க்க வேண்டியது |
|---|---|---|---|
| **Sura Publications** | [Official 2026–27 School Guides](https://www.surabooks.com/collections/school-guides-2026-27) | 6–12; பல Subjects மற்றும் TM/EM | Official Catalogue / Paid Guide / Sample PDF; முழு இலவச PDF என்று கருதக்கூடாது |
| **Ganga Publications** | SamacheerKalviStudents, KalviMani, Tamilaruvi Index-கள் | Primary முதல் Higher Classes வரை | Class / Term / Medium PDF உறுதி |
| **Way to Success** | Tamilaruvi, KalviMani Index-கள் | Middle / High / Higher Secondary | Edition மற்றும் PDF முழுமை |
| **EC Loyola** | Tamilaruvi, KalviKadal, KalviMani | 6–12 Guide Candidates | Sample vs Full Guide பிரிக்க வேண்டும் |
| **Don Publications** | Tamilaruvi மற்றும் பிற Index-கள் | 6–12 Guide Candidates | Edition / Subject / Medium |
| **Selection** | Tamilaruvi / பிற Index-கள் | 6–10 Guide Candidates | Subject / Medium |
| **Penguin** | Tamilaruvi | 6–12 Guide Candidates | Edition / PDF முழுமை |
| **Brilliants / Brilliant** | Tamilaruvi | 6–12 Guide Candidates | Publisher / PDF Origin உறுதி |
| **Dolphin** | Tamilaruvi | 9–12 Guide Candidates | Subject-wise PDF |
| **Diamond, Kavin, KSJ, Nithish, Rasi, Kavimani, Surya, Roots** | Tamilaruvi / பிற Guide Index-கள் | குறிப்பிட்ட Class / Subject / Edition-களில் கூடுதல் Reference | ஒவ்வொன்றையும் தனியாகச் சோதிக்க வேண்டும் |

### D. Play Store Apps — App Source Candidates

| App | Google Play Link | Listing-ல் கூறப்படும் Coverage | பயன்பாடு / வரம்பு |
|---|---|---|---|
| **TN School App — BrainKart** | [Play Store](https://play.google.com/store/apps/details?id=in.brainkart.tnschool) | Class 1–12; TM/EM; Book Back Answers, Solutions, Notes, Question Papers | 10K+ Downloads என்று Play Store காட்டியது. Public Listing பார்க்க முடியும்; App-க்குள் உள்ள ஒவ்வொரு Answer-யும் Browser-ல் நேரடியாக ஆய்வு செய்ய முடியாது |
| **TN TextBooks: Samacheer Kalvi — VirkozKalvi** | [Play Store](https://play.google.com/store/apps/details?id=com.virkoz.tntextbooks) | Class 1–12 Textbooks, Book Back Solutions, TM/EM என்று கூறுகிறது | 10K+ Downloads. Ads / In-App Purchases உள்ளது; Developer தன்னை Independent Initiative என்று குறிப்பிடுகிறது |
| **TN 12th Guide (All sub)** | [Play Store](https://play.google.com/store/apps/details?id=com.samacheerkalvi.tn12thguide) | Class 12; TM/EM; Book Back, Detailed Explanations, Long Answers | 1K+ Downloads; 12ஆம் வகுப்புக்கான Supplementary Candidate |
| **Padi App: TN Samacheer Kalvi** | [Play Store](https://play.google.com/store/apps/details?id=com.tndigitalapps.padi_app) | Public Listing-ல் Class 10 மற்றும் 12 பகுதிகள், TM/EM, Book Back / Board Questions / MCQ Practice | 1–12 முழு Answer Source என்று கருத வேண்டாம்; குறிப்பிட்ட Class / Subject மட்டும் சோதிக்கவும் |

**App Access Limitation:** Public Google Play Listing, App Description, Downloads, Ratings / Reviews போன்றவற்றைப் பார்க்க முடியும். ஆனால் Play Store-லிருந்து App-ஐ நிறுவி Login செய்து உள்ளே உள்ள ஒவ்வொரு பாடம் / Answer-ஐ நேரடியாகத் திறந்து ஆய்வு செய்ய முடியாது. App Content Public Website / PDF-ல் கிடைத்தால் அதைத் தனியாக ஆய்வு செய்யலாம். இல்லையெனில் User வழங்கும் Export / PDF / Screenshot போன்ற அணுகக்கூடிய Reference தேவைப்படும்.

### E. Official Textbook / Syllabus Verification

| Official Source | Link | பயன்பாடு |
|---|---|---|
| Tamil Nadu Textbook and Educational Services Corporation | [textbookcorp.in](https://www.textbookcorp.in/) | Official Textbook Release / Term / Academic Year / Edition அறிவிப்புகள் |
| Official Textbook Sales / School Page | [textbookcorp.in/schools](https://textbookcorp.in/schools) | எந்த Class-க்கு எந்த Academic Year / Medium / Term புத்தகம் வெளியானது என்பதைச் சரிபார்க்க |
| SCERT Textbook Index (Secondary Index) | [NCERTBooksPDF Tamil Nadu Index](https://ncertbookspdf.com/tamilnadu-samacheer-kalvi-books/) | PDF Reference; Official Announcement-உடன் ஒப்பிட வேண்டும் |

Official Textbook Source தான் Edition / Term சரிபார்ப்புக்கான முதன்மை Reference. Guide Website-ல் இருக்கும் பழைய PDF-ஐ தற்போதைய புத்தகத்திற்குச் சரியானது என்று தானாக ஏற்றுக்கொள்ளக்கூடாது.

---

## 7. Source Quality, Popularity மற்றும் Reliability மதிப்பீடு

ஒரு Website பிரபலமானது என்பதால் அதிலுள்ள எல்லா Answers-யும் சரியானவை என்று கருதக்கூடாது.

| அளவுகோல் | சரிபார்க்க வேண்டியது |
|---|---|
| Coverage | 1–12 வகுப்புகள் முழுவதும் உள்ளதா? எந்த Class / Subject விடுபட்டுள்ளது? |
| Medium | TM மற்றும் EM இரண்டும் உள்ளனவா? |
| Term | Primary Classes-ல் Term 1 / 2 / 3 அனைத்தும் உள்ளனவா? |
| Edition | 2026–27 அல்லது தேவையான Academic Year-க்கு பொருந்துகிறதா? |
| Direct Access | குறிப்பிட்ட பாடம் / கேள்விக்கான Page அல்லது PDF நேரடியாகத் திறக்கிறதா? |
| Completeness | Short Answers மட்டும் தானா? Long Answers மற்றும் அனைத்து Exercises உள்ளனவா? |
| Source Origin | Publisher / ஆசிரியர் / ஆசிரியர் குழு யார்? Mirror Copy தானா? |
| Consistency | பல பாடங்களிலும் ஒரே மாதிரியான Answer Quality உள்ளதா? |
| Popularity Signal | Play Store Downloads / Reviews, Website Traffic Estimate போன்ற ஆதாரம் உள்ளதா? |
| Availability | Free, Sample-only, Paid, Login அல்லது App-only ஆக உள்ளதா? |

### இப்போது தெரிந்த Popularity Signals

- TN School App — Play Store-ல் 10K+ Downloads.
- TN TextBooks: Samacheer Kalvi — Play Store-ல் 10K+ Downloads.
- TN 12th Guide — Play Store-ல் 1K+ Downloads.

இவை Play Store Listing-ல் தெரிந்த Signals மட்டுமே. மாணவர்களின் உண்மையான பயன்பாடு, Review Quality அல்லது Answer Accuracy-க்கு முழு சான்று அல்ல. Website Traffic / Reviews கிடைத்தால் தேதி மற்றும் Data Provider உடன் பதிவு செய்ய வேண்டும். ஆதாரமில்லாமல் ஒரு தளத்தை “மிகவும் பிரபலமானது” என்று வகைப்படுத்தக்கூடாது.

---

## 8. முழுமையான Coverage Audit — அடுத்த கட்டத்தின் முக்கியப் பணி

ஒரு Website “1–12 All Subjects” என்று கூறினாலும், ஒவ்வொரு பாடத்திலும் முழு Answer இருப்பது உறுதியல்ல. எனவே Class × Subject × Medium × Term × Chapter அடிப்படையில் Audit செய்ய வேண்டும்.

### ஒவ்வொரு Book / Chapter-க்கும் பதிவு செய்ய வேண்டியவை

- Class: 1–12
- Subject
- Medium: TM / EM
- Academic Year
- Term: 1 / 2 / 3 / Annual
- Textbook Edition
- Chapter Number & Name
- questions.md உள்ளது / இல்லை
- PDF Reference உள்ளது / இல்லை
- PDF Page / Chapter Cross-check Status
- Source Website / Guide / App
- Direct Page / PDF Link
- Answer Found / Not Found
- Answer Completeness
- Source Version
- Verification Date

### Source Status Values

| Status | பொருள் |
|---|---|
| INDEX_FOUND | Website / Index Page கிடைத்தது; Answer சரிபார்க்கப்படவில்லை |
| PAGE_FOUND | குறிப்பிட்ட பாடத்தின் Direct Page கிடைத்தது |
| ANSWER_FOUND | அந்தப் பக்கத்தில் குறிப்பிட்ட கேள்விக்கான பதில் உள்ளது |
| PDF_FOUND | Guide PDF திறக்கப்பட்டது |
| PDF_PAGE_VERIFIED | குறிப்பிட்ட Answer PDF-ல் குறிப்பிட்ட Page-ல் சரிபார்க்கப்பட்டது |
| PARTIAL | சில கேள்விகளுக்கு மட்டுமே Answer உள்ளது |
| WRONG_EDITION | தற்போதைய Textbook-க்கு பொருந்தாத பழைய Edition |
| WRONG_MEDIUM | தேவைப்பட்ட TM / EM அல்ல |
| BROKEN_LINK | Link திறக்கவில்லை |
| APP_ONLY | App உள்ளே மட்டுமே உள்ளது; Public Page / PDF உறுதிப்படுத்தப்படவில்லை |
| NO_ANSWER_ON_PAGE | Page திறந்தது; ஆனால் அந்தக் கேள்விக்கான Answer இல்லை |
| ANSWER_NOT_FOUND | தேடலுக்குப் பிறகும் Answer கிடைக்கவில்லை |
| CONFLICT | இரண்டு அல்லது அதற்கு மேற்பட்ட Sources வேறுபட்ட Answers தருகின்றன |
| VERIFIED_FOR_CURRENT_EDITION | தற்போதைய சரியான Edition-க்கு பொருந்துவது உறுதி செய்யப்பட்டது |

### Coverage கணக்கிடும் முறை

உதாரணமாக ஒரு Website 10ஆம் வகுப்பு தமிழ் பாடத்தின் 20 Questions-ல் 15-க்கு மட்டும் பதில் கொடுத்திருந்தால்:

- Total Questions: 20
- Answer Found: 15
- Missing: 5
- Coverage: 75%

ஒரு பாடத்திற்கான Coverage-ஐ முழு வகுப்பின் Coverage என்று தவறாகக் கூறக்கூடாது. Class / Subject / Medium / Term / Chapter அடிப்படையில் கணக்கிட வேண்டும்.

---

## 9. Academic Year / Textbook Edition கவனம்

2026–27 Academic Year-க்கு Class மற்றும் Term அடிப்படையில் Textbook மாற்றங்கள் இருக்கலாம். குறிப்பாக Primary Classes-ல் Term-wise Books இருப்பதால் Edition தவறினால் Answer மாறக்கூடும்.

[Official Textbook Corporation](https://www.textbookcorp.in/) வெளியிட்டுள்ள 2026–27 அறிவிப்புகளில்:

- 1–3 வகுப்புகளுக்கான Term 1 புத்தகங்கள் 25-05-2026 முதல் கிடைக்கும் என்று அறிவிக்கப்பட்டது.
- 1–7 வகுப்புகளுக்கான Term 2 புத்தகங்கள் 22-09-2026 முதல் கிடைக்கும் என்று அறிவிக்கப்பட்டது.
- 4–7 வகுப்புகளுக்கான Term 1 மற்றும் 8ஆம் வகுப்பு Annual Textbooks உள்ளிட்டவை 14-05-2026 முதல் கிடைக்கும் என்று அறிவிக்கப்பட்டது.
- 2025–26-ல் அச்சிடப்பட்ட Classes 1–3 Term 1 புத்தகங்கள் தற்போது நடைமுறையில் இல்லாத பழைய பதிப்புகள் என்று Official Site குறிப்பிடுகிறது.

ஒவ்வொரு Source-க்கும் Edition Match கட்டாயம். பழைய Guide-ல் Answer கிடைத்தாலும் அது தற்போதைய Book Question-க்கு பொருந்துகிறதா என்று questions.md மற்றும் PDF Page மூலம் உறுதிப்படுத்த வேண்டும்.

---

## 10. Copyright, Public GitHub மற்றும் Working Space

### 10.1 GitHub ஏன் பயன்படுத்தப்படுகிறது?

- பல AI tools ஒரே Repository-ஐ அணுக முடியும்.
- Research Notes மற்றும் Source Links ஒரே இடத்தில் இருக்கும்.
- புதிய Chat / AI வந்தாலும் Blueprint படித்து அதே Workflow-ஐத் தொடர முடியும்.
- என்ன முடிவு எடுக்கப்பட்டது, என்ன Pending என்று தெளிவாக இருக்கும்.

GitHub இந்தத் திட்டத்தின் Final Student Website அல்ல. Final Answer Content பின்னர் தனியாக உருவாக்கப்படும்.

### 10.2 Reference vs Final Answer

| Stage | உள்ளடக்கம் | நோக்கம் |
|---|---|---|
| Research / Reference Stage | பல Website / PDF-களில் கிடைத்த Answer References, Source Links, Page Numbers, Differences | ஒப்பீடு மற்றும் ஆய்வு |
| Final Answer Stage | பல Reference-களின் தகவலை ஒப்பிட்டு நம்முடைய சொந்த wording-ல் உருவாக்கப்படும் Answer | நம்முடைய சொந்த கல்வி உள்ளடக்கம் |
| Student-facing Website | இறுதியில் உருவாக்கப்பட்ட சொந்த Answer Guide / Quiz | மாணவர் பயன்பாடு |

### 10.3 Public Repository-யின் உண்மையான வரம்பு

Repository Public ஆக இருக்கும் வரை அதன் Files-ஐ மற்றவர்களும் பார்க்க முடியும். அது Final Website அல்ல என்றாலும் Public Working Space என்பதால் Private Storage அல்ல.

வேலை முடிந்ததும் Local Copy எடுத்துக்கொண்டு Repository-யிலிருந்து Working Reference Files-ஐ அகற்ற திட்டமிடப்பட்டுள்ளது. ஆனால் ஒரு File-ஐ புதிய Commit-ல் Delete செய்தால் பழைய Commit History-யில் அதன் பழைய Content இன்னும் இருக்கக்கூடும். Git History-யிலிருந்தும் அகற்ற வேண்டும் என்றால் தனியாக History Rewrite / Force Push போன்ற Cleanup தேவை. எனவே “File Delete செய்தோம்” என்பதும் “Git History-யிலிருந்து முழுமையாக நீக்கினோம்” என்பதும் வெவ்வேறு.

**Cleanup Process:**
1. Local Backup உருவாக்குதல்.
2. Local Copy சரியாக உள்ளதா சரிபார்த்தல்.
3. Public Repository-யில் Working Reference Files-ஐ அகற்றுதல்.
4. தேவையானால் Git History-யிலிருந்தும் அகற்ற தனி Cleanup செய்தல்.
5. Public Link / Commit History மீண்டும் சரிபார்த்தல்.

இந்த Project-ன் இறுதி நோக்கம் மூன்றாம் தரப்பு Guide-களை Final Website-ல் அப்படியே வெளியிடுவது அல்ல; பல Reference-களை ஒப்பிட்டு நம்முடைய சொந்த Answer உருவாக்குவதே. இருப்பினும் Public GitHub-ல் சேமிக்கப்படும் Reference Text அந்தக் காலத்தில் பொதுமக்களுக்கும் தெரியும். License / Permission நிலை தெளிவில்லாத முழு Guide-களை Public-ஆக சேமிப்பதைத் தவிர்த்து, தேவையான Reference Extract, Page Link, PDF Page மற்றும் சொந்த ஆய்வு குறிப்புகளை வைத்திருப்பது பாதுகாப்பான நடைமுறை.

---

## 11. Error Prevention / Quality Control

| ஏற்படக்கூடிய தவறு | தவிர்க்கும் முறை |
|---|---|
| questions.md-ல் OCR / Extract பிழை | PDF Page-ஐ திறந்து Original Text-உடன் ஒப்பிடுதல் |
| கேள்வி விடுபடுதல் | PDF Exercises மற்றும் questions.md எண்ணிக்கையை ஒப்பிடுதல் |
| Wrong Edition Answer | Academic Year / Term / Edition பதிவு செய்து Textbook ஒப்பிடுதல் |
| Generic Homepage Link | அந்தக் கேள்விக்கான Direct Page மட்டும் பதிவு செய்தல் |
| Page-ல் Answer இல்லாமல் உள்ளது என்று கூறுதல் | ANSWER_FOUND கொடுப்பதற்கு முன் Answer-ஐத் திறந்து பார்க்க வேண்டும் |
| AI சொந்த அறிவால் Answer நிரப்புதல் | Source evidence இல்லாவிட்டால் ANSWER_NOT_FOUND |
| Mirror Pages-ஐ தனித்தனி Sources என்று எண்ணுதல் | Content Origin / Publisher / Identical Text ஒப்பிடுதல் |
| Multiple Correct MCQ Options | ஒரே Correct Answer இருக்கிறதா சோதித்தல் |
| Long Answer-ஐ MCQ-ஆக மாற்றுதல் | Quiz Rules படி Exclude செய்தல் |
| quiz.md / quiz.json வேறுபடுதல் | Automated Consistency Validation |
| PDF Page Number விடுபடுதல் | Guide Page Number கட்டாயமாகப் பதிவு செய்தல் |
| Source Answers முரண்படுதல் | அனைத்தையும் பதிவு செய்து Final Comparison-க்கு ஒதுக்குதல் |
| Final Answer விரைவாக உருவாக்குதல் | Reference Collection முடியும் வரை Final Answer உருவாக்க வேண்டாம் |

---

## 12. End-to-End Work Plan

| Stage | வேலை | Result |
|---|---|---|
| 0 | Project Blueprint / Rules Lock | எல்லா AI / Developer-க்கும் ஒரே Workflow |
| 1 | Classes 1–12 Repository / Folder Audit | Class-wise Existing Structure |
| 2 | Questions + PDF Inventory | questions.md மற்றும் PDF பட்டியல் |
| 3 | Question Cross-check | Extracted Questions சரிபார்ப்பு |
| 4 | Website Research | Answer Website Master List |
| 5 | Guide PDF Research | Publisher / Guide / PDF Source List |
| 6 | App Research | Public App Listings மற்றும் Access Status |
| 7 | Source Coverage Audit | Class × Subject × Medium × Term × Chapter Matrix |
| 8 | Quiz Generation | quiz.md + quiz.json |
| 9 | Answer Reference Collection | Source-wise answers.md |
| 10 | Missing Answer Search | கிடைக்காத கேள்விகளுக்கான கூடுதல் Source Search |
| 11 | Source Comparison | Differences / Common Points / Quality Notes |
| 12 | Final Answer Drafting | நம்முடைய சொந்த wording-ல் Answers |
| 13 | Final QA | Textbook, PDF, Sources, Quiz அனைத்தும் சரிபார்ப்பு |
| 14 | Local Backup & GitHub Cleanup | Working Files Local-ல்; Public Repo Cleanup |

Stage 4–7 முடிவதற்கு முன் 1–12 Classes முழுவதற்கும் Source கிடைத்துவிட்டது என்று அறிவிக்கக்கூடாது. Reference Collection முடிவதற்கு முன் Final Answers எழுத வேண்டாம்.

---

## 13. அடுத்ததாக செய்ய வேண்டியவை

1. தற்போதைய Class 10 Repository-யில் Folder Structure மற்றும் questions.md / PDF இணைப்புகளை Audit செய்தல்.
2. Classes 1–12 Repository URLs கிடைத்தால் அவற்றின் Folder Structure Audit செய்தல்.
3. Website / Guide PDF / App Source Research-ஐ முடித்து Source Coverage Master List உருவாக்குதல்.
4. 1–12 வகுப்புகளுக்கான TM/EM, Term, Subject, Edition Coverage எவ்வளவு என்பதை ஆதாரத்துடன் கணக்கிடுதல்.
5. அதிக Coverage கொண்ட Source-ல் Round 1 தொடங்குதல்.
6. Quiz மற்றும் Answer Collection-ஐத் தனித்தனி பணிகளாகச் செயல்படுத்துதல்.

## 14. Quick Handover Summary — புதிய Chat / மற்ற AI-க்காக

**Project:** TN Samacheer Kalvi Classes 1–12 Book Back Question, Quiz & Answer Reference Project.

**Input Sources:**
- questions.md — ஏற்கெனவே Extract செய்யப்பட்ட Book Back Questions.
- Textbook PDF — Page-level Cross-check.
- Public Answer Websites — குறிப்பிட்ட Answer Page Links.
- Professional Guide PDFs — Publisher / Edition / Medium / Term / Page Number உடன்.
- Public Play Store App Listings — App Source Candidates; App உள்ளே உள்ள Content தனியாக அணுகக்கூடியதாக இருந்தால் மட்டுமே.

**Quiz Rule:** One-word / Objective / Existing MCQ கேள்விகள் மட்டும். குறுவினா, சிறுவினா, நெடுவினா, Essay, Writing Tasks Quiz-ல் வேண்டாம்.

**Answers Rule:** Book Back-ல் உள்ள எல்லா வகைக் கேள்விகளுக்கும் Source-based Reference Collection. AI-ன் சொந்த அறிவிலிருந்து Answer உருவாக்கக்கூடாது. Direct Page / PDF Page ஆதாரம் இல்லாவிட்டால் கிடைக்கவில்லை என்று பதிவு செய்ய வேண்டும்.

**Final Answer Rule:** பல Source-களை ஒப்பிட்ட பிறகு மட்டுமே சொந்த Wording-ல் Final Answer எழுத வேண்டும்.

**Files per Chapter:** questions.md, quiz.md, quiz.json, answers.md.

**Research Priority:** முதலில் 1–12 வகுப்புகளுக்கான Website / Guide PDF / App Source Coverage-ஐ உறுதிப்படுத்துதல். பின்னர் Class × Subject × Medium × Term × Chapter அடிப்படையில் Round-wise Answer Collection.

**Repository Purpose:** Common AI Working Space; Final Student-facing Website அல்ல. வேலை முடிந்ததும் Local Backup மற்றும் Public GitHub Cleanup செய்ய வேண்டும்.

**Current Status:** Blueprint மற்றும் Initial Source List தயார். Full Coverage Audit இன்னும் Pending.


### நேரடியாகத் திறக்கப்பட்ட Guide PDF உதாரணங்கள்

கீழே உள்ளவை Guide Index மட்டும் அல்ல; முன்பு ஆய்வில் நேரடியாகத் திறந்து பார்த்த PDF Link உதாரணங்கள். இவை எல்லா வகுப்புகளுக்கும் தற்போதைய முழு Coverage நிரூபிக்கவில்லை; குறிப்பிட்ட வகுப்பு / Term / Edition-க்கான மாதிரி ஆதாரங்கள் மட்டுமே.

| வகுப்பு | Publisher / Guide | Medium / Term | நேரடி PDF | சரிபார்ப்பு குறிப்பு |
|---|---|---|---|---|
| 2 | Ganga Guide | Tamil / Term 1 | [2nd Standard Tamil Ganga Guide PDF](https://samacheerkalvistudents.in/Guides/Guides%20Samacheer%20kalvi/2nd%20std/Guides/2nd_standard_tamil_guide_term_1.pdf) | 49-page PDF எனக் காட்டப்பட்டது; current edition match இன்னும் செய்ய வேண்டும் |
| 5 | Ganga Guide | Tamil / Term 1 | [5th Standard Tamil Ganga Guide PDF](https://samacheerkalvistudents.in/Guides/Guides%20Samacheer%20kalvi/5th%20std/Ganga/5th_tamil_ganga_guide_term_1.pdf) | 90-page PDF எனக் காட்டப்பட்டது; current edition match இன்னும் செய்ய வேண்டும் |
| 6 | Sura Science Guide | Tamil Medium / Term 1 | [6th Standard Science Sura Sample PDF](https://samacheerkalvistudents.in/Guides/Guides%20Samacheer%20kalvi/6th%20std/Science/6th_science_sura_sample_guide_term_1_tm_219286.pdf) | 56-page Sample Copy; முழு Guide அல்ல |

**இந்த PDF-களைப் பயன்படுத்தும் முன்:** PDF-ன் Cover / Copyright / Edition Page, Academic Year, Medium, Term மற்றும் Chapter Question Number ஆகியவற்றைச் சரிபார்க்க வேண்டும். PDF பக்க எண்ணிக்கை மட்டும் முழுமையான Answer Coverage-க்கு சான்று அல்ல.


---

## 15. Execution Protocol — ஒவ்வொரு Subject / Chapter-க்கும் பின்பற்ற வேண்டிய நடைமுறை

இந்த Protocol தான் இனிமேல் புதிய Chat / AI பணியைத் தொடங்கும்போது பின்பற்ற வேண்டிய Default Order.

### 15.1 Subject தொடங்கும் முன் — Book Version Gate (ஒருமுறை)

ஒவ்வொரு Subject-க்கும் முதலில் அதன் முழுப் புத்தகத்தைப் பற்றிய விவரங்களை உறுதிப்படுத்த வேண்டும்:

1. Class, Subject, Medium.
2. Academic Year — தற்போது வேலை செய்யும் கல்வியாண்டு.
3. Book Title / Edition / Reprint Year / Correction Year.
4. Term-based book ஆ அல்லது Annual / Full-Year book ஆ.
5. PDF Page Count, Contents / TOC, Chapter Names.
6. Official Textbook Corporation / SCERT அறிவிப்புடன் Version Match.

**Term விதி:** Term 1 / 2 / 3 என எல்லா வகுப்புகளுக்கும் தானாக எழுதக்கூடாது. அந்த Class-ன் உண்மையான Textbook Structure term-based என்றால் மட்டுமே Term field பயன்படுத்த வேண்டும். உதாரணமாக 10ஆம் வகுப்பு Tamil என்பது Annual / Full-Year book; Term 1 என்று பதிவு செய்ய வேண்டாம். 1–7 வகுப்புகளுக்கு 2026–27 Term-wise announcements உள்ளதால் அந்த வகுப்புகளின் உண்மையான புத்தகப் பிரிவுகளை தனியாகச் சரிபார்க்க வேண்டும்.

### 15.2 ஒவ்வொரு Chapter-க்கும்

| படி | வேலை | Output / Check |
|---|---|---|
| 1 | அந்த Chapter-ன் questions.md மற்றும் PDF Page Range கண்டறிதல் | Original Question Inventory |
| 2 | questions.md-ல் உள்ள ஒவ்வொரு கேள்வியையும் PDF Page-க்கு எதிராகச் சரிபார்த்தல் | Correct / Typo / Missing / Extra / Unclear Status |
| 3 | அசல் கேள்வியின் சொற்களைச் சரிசெய்ய வேண்டுமெனில் PDF ஆதாரம் இருந்தால் மட்டுமே திருத்துதல் | Verified questions.md |
| 4 | Quiz-க்கு தகுதியான Objective Questions-ஐ மட்டும் குறித்தல் | Quiz Candidate List |
| 5 | Round 1-ல் ஒரு நல்ல Direct Answer Source தேர்வு செய்தல் | குறிப்பிட்ட பாடத்திற்கான Source Page / PDF |
| 6 | அந்த Source-ல் உள்ள கேள்வி வாரியான பதில்களை answers.md-ல் Reference ஆகச் சேகரித்தல் | Source 1 Answer Collection |
| 7 | அந்த Source-ல் பதில் இல்லாத கேள்விகளை Missing எனக் குறித்தல்; தேவையானால் அதே கட்டத்தில் ஒரு கூடுதல் Source தேடுதல் | Honest Coverage Status |
| 8 | Objective Questions-ன் Correct Answer-ஐ Textbook / நம்பகமான Answer Source-உடன் சரிபார்த்தல் | Quiz Answer Validation |
| 9 | உறுதிசெய்யப்பட்ட Objective Questions-ஐ ஏற்கெனவே உள்ள 10th Tamil Quiz Format-ல் அமைத்தல் | quiz.md |
| 10 | அதே Data-வை quiz.json-ல் அமைத்து இரண்டையும் ஒப்பிடுதல் | Valid JSON + Content Match |
| 11 | Question Count, Correct Answer Count, Options, Explanations, PDF references ஆகியவற்றை QA செய்தல் | Chapter Completion Check |

**ஒவ்வொரு பாடத்திலும் Answers முதலில், Quiz அதன் பிறகு.** இதனால் Quiz-ல் உள்ள Answer மற்றும் Explanation-க்கு முன்னதாக Source ஆதாரம் இருக்கும்.

### 15.3 Quiz Explanation (காரண விளக்கம்) விதி

- காரண விளக்கம் வெறும் அலங்கார உரையாக இருக்கக்கூடாது.
- அது பாடத்தின் கருத்து / இலக்கண விதி / உரை பகுதியிலிருந்து ஆதரிக்கப்பட வேண்டும்.
- BrainKart அல்லது Guide-ல் ஏற்கெனவே விளக்கம் இருந்தால் அதனை Reference-ஆகப் பயன்படுத்தலாம்.
- Explanation Source-ல் இல்லாவிட்டால் Textbook-ல் உள்ள தொடர்புடைய பகுதியைச் சரிபார்த்து ஆதரிக்க வேண்டும்.
- எந்த ஆதாரமும் இல்லாத நிலையில் AI தானாகக் காரணம் உருவாக்கக்கூடாது; REVIEW_REQUIRED என்று குறிக்க வேண்டும்.

### 15.4 Source 1-ன் பங்கு

ஒரு Direct Answer Website-ல் இருந்து முதற்கட்ட Reference Set உருவாக்குவது நோக்கம். இது Final Answer அல்லது முழு சுயாதீன Cross-verification என்று கருதப்படக்கூடாது.

- அந்த Source-ல் உண்மையில் உள்ள கேள்வி / பதில்களையே பதிவு செய்ய வேண்டும்.
- Source-ல் இல்லாத கேள்வியைத் தானாக நிரப்பக்கூடாது.
- Source Answer மற்றும் Textbook Question பொருந்துகிறதா பார்க்க வேண்டும்.
- பின்னர் Round 2 / 3-ல் மற்ற Guide / Website Source-களிலிருந்து ஒப்பீடு செய்ய வேண்டும்.
- Quiz-ல் பயன்படுத்தப்படும் Objective Answer-களுக்கு குறைந்தது Textbook Context அல்லது இரண்டாவது நம்பகமான ஆதாரம் மூலம் தனி சரிபார்ப்பு இருக்க வேண்டும்.

### 15.5 Subject முடிக்கும் முறை

ஒரு Subject-ல் உள்ள எல்லா Chapters-க்கும்:
- questions.md PDF Cross-check முடிந்திருக்க வேண்டும்.
- answers.md-ல் கிடைத்த Source Answers அனைத்தும் பதிவு செய்யப்பட்டிருக்க வேண்டும்.
- Quiz eligible questions அனைத்தும் மட்டும் quiz.md / quiz.json-ல் இருக்க வேண்டும்.
- Missing / Conflict / Wrong Edition ஆகியவை வெளிப்படையாகக் குறிக்கப்பட்டிருக்க வேண்டும்.
- இறுதியில் Subject-level coverage மற்றும் pending list தயாரிக்க வேண்டும்.

பிறகுதான் அடுத்த Subject-க்கு செல்ல வேண்டும். எல்லா Subject-களின் Reference Collection முடிந்த பிறகே Final Answer Comparison மற்றும் நம்முடைய சொந்த Wording-ல் பதில் உருவாக்கும் கட்டம்.

---

## 16. Current Audit Finding — Class 10 Tamil Book Version (Provisional Warning)

**Repository:** [Eaglesiva/tn-class-10](https://github.com/Eaglesiva/tn-class-10)

GitHub Tree Audit-ல் Tamil Subject-க்கான PDF Page Files:
- tamil/00_prelims/page_001.pdf முதல் page_010.pdf
- பாட அத்தியாயங்களின் கீழ் தொடர்ச்சியாக page_011.pdf முதல் page_248.pdf
- மொத்தம்: **248 individual one-page PDF files**.

### 16.1 வெளிப்புற புத்தகப் பதிப்பு ஒப்பீடு

- FreeTNBooks 10ஆம் வகுப்பு புத்தகப் பக்கம் 2024 Tamil PDF மற்றும் தனியாக “New” 2025 Tamil PDF என இரண்டு பதிவுகளை வேறுபடுத்துகிறது. 2025 Edition Tamil புத்தகம் வெளியிடப்பட்டதாகவும் அந்தப் பக்கம் குறிப்பிடுகிறது: [10th Standard Books](https://www.freetnbooks.com/10th-standard-books/).
- மற்றொரு 2026 textbook index 2025 10th Tamil book-ஐ 184 pages என்றும் 2024 Tamil book-ஐ 248 pages என்றும் வேறுபடுத்துகிறது: [Class 10 Tamil Book 2026 listing](https://cbsetamil.com/ncert-tamil-book-for-class-10-pdf/).
- Tamil Nadu Textbook and Educational Services Corporation 2026–27 Class 10 Annual Textbooks விற்பனை 10-04-2026 முதல் தொடங்கியதாக அறிவித்துள்ளது: [Official Textbook Corporation](https://textbookcorp.in/schools).
- 2026–27-ல் Classes 4–12 பழைய syllabus-ஐத் தொடரும் என்றும் புதிய curriculum 2027–28-ல் அமல்படுத்தப்படுமென்றும் செய்தி அறிக்கைகள் தெரிவிக்கின்றன: [DT Next — Classes 4–12 textbook work](https://www.dtnext.in/news/tamilnadu/teachers-continue-with-classes-4-12-textbook-work-despite-new-regime-uncertainty), [New Indian Express — draft curriculum](https://www.newindianexpress.com/states/tamil-nadu/2026/Aug/21/tn-revamps-syllabus-for-class-6-10-with-emphasis-on-critical-thinking).

### 16.2 தற்போதைய நிலை / தீர்மானம்

Repo-வில் உள்ள 248 page sequence, வெளியிடப்பட்ட 2024 Edition 248-page தகவலுடன் பொருந்துகிறது. 2025 Revised Tamil Edition 184 pages என்று மற்றொரு Source காட்டுகிறது. எனவே Repo-வில் உள்ள 248-page copy **2024 Edition ஆக இருக்கக்கூடிய வலுவான சாத்தியம் உள்ளது**.

ஆனால் PDF Cover / Imprint / Edition Page-ஐ நேரடியாகப் படித்து, 2025 copy-யுடன் page-level content comparison முடிக்காமல் இதை 100% உறுதிப்படுத்தக்கூடாது.

**தற்காலிக முடிவு:** தற்போதைய Repo PDF-ஐ 2026–27-க்கான Verified Current Edition என்று குறிக்க வேண்டாம். 2025 Revised Tamil PDF (அல்லது 2026–27 official reprint) கிடைத்து அதன் title page, revision imprint, TOC, lesson pages மற்றும் Book Back Questions ஒப்பிடப்படும் வரை Quiz Finalization-ஐ நிறுத்த வேண்டும்.

### 16.3 Class 10 Tamil — முதற்கட்ட Answer Source Candidate

[BrainKart — 10th Tamil, இயல் 1: அமுத ஊற்று — Questions & Answers](https://www.brainkart.in/article/Questions-and-Answers_11807/)

இந்தப் பக்கம் இயல் 1-க்கான Objective, குறுவினா, சிறுவினா, நெடுவினா வகை உள்ளடக்கங்களை வழங்குகிறது. அதே பாடத்திற்கான Subject Index-ல் பிற இயல்களுக்கும் தனிப்பட்ட Questions & Answers பதிவுகள் உள்ளன: [BrainKart 10th Tamil Subject Index](https://www.brainkart.in/subject/Tamil-10th-Std_396).

இது Round 1 Source Candidate மட்டுமே; பக்கம் 2022-ல் வெளியிடப்பட்டது. Current 2026–27 Textbook-உடன் ஒவ்வொரு கேள்வியும் பொருந்துகிறதா என்பதைக் கட்டாயம் சரிபார்க்க வேண்டும். இந்த Source-ல் இல்லாத கேள்விகளுக்கு பதில் உள்ளது என்று கருதக்கூடாது.

### 16.4 Existing Class 10 Tamil Unit 1 File Cross-check Note

தற்போதைய Repository-ல்:
- [questions.md — Unit 1](https://github.com/Eaglesiva/tn-class-10/blob/main/tamil/01_mozhi_amuthaootru/book_back_questions/questions.md)
- [quiz.md — Unit 1](https://github.com/Eaglesiva/tn-class-10/blob/main/tamil/01_mozhi_amuthaootru/book_back_questions/quiz.md)

இரண்டிலும் சில சொல் / Option வேறுபாடுகள் உள்ளன. உதாரணமாக:
- questions.md-ல் “எந்தமிழ்நா”; quiz.md-ல் “எண்தமிழ்நா” என்று உள்ளது.
- ஒரு கேள்வியின் பெயர்/சொல் மற்றும் சில Options-ன் wording / ordering மாறுபடுகின்றன.

இவை எது சரி என்று இப்போது தீர்மானிக்கக்கூடாது. சரியான 2026–27 Textbook Page-ஐப் பார்த்தே உறுதி செய்ய வேண்டும். தற்போதைய quiz.md-ன் **format**-ஐ மட்டும் Reference-ஆகப் பயன்படுத்தலாம்; அதில் உள்ள Question Content-ஐ Verified என்று கருதக்கூடாது.

மேலும் questions.md-ல் உள்ள file:///e:/... போன்ற Local Computer Links மற்ற AI-க்கு அணுக முடியாது. Cross-check முடிந்தபின் அவற்றை Repository-relative link அல்லது GitHub Page Link-ஆக மாற்ற வேண்டும்.

---

## 17. புதிய Chat / AI-க்கு உடனடி அடுத்த செயல்

1. முதலில் Section 16-ல் உள்ள Class 10 Tamil Version Warning-ஐத் தீர்க்க வேண்டும்.
2. 2025 Revised / 2026–27 current Tamil textbook PDF-ஐப் பெற்று Cover, Revision Imprint, TOC, Chapter-1 pages, Book Back exercise pages ஆகியவற்றை பழைய Repo copy-யுடன் ஒப்பிட வேண்டும்.
3. அது சரியான Current Edition என்று உறுதியான பின், Unit 1 questions.md-ஐ PDF-க்கு எதிராகத் திருத்த / உறுதி செய்ய வேண்டும்.
4. BrainKart Unit 1 Direct Answer Page-ல் உள்ள ஒவ்வொரு கேள்வியையும் questions.md-உடன் ஒப்பிட்டு, Source 1 answers-ஐ answers.md-ல் பதிவு செய்ய வேண்டும்.
5. அடுத்து Unit 1-ன் Objective questions-ஐ மட்டும் எடுத்துக் கொண்டு, ஆதாரமுள்ள Correct Answer மற்றும் உண்மையான Explanation உடன் quiz.md / quiz.json உருவாக்க / சரிபார்க்க வேண்டும்.
6. Unit 1 முடிந்ததும் Unit 2-க்கு இதே நடைமுறையை மீண்டும் செய்ய வேண்டும்.
7. எல்லா Tamil Chapters முடிந்த பின் Tamil Subject-level Audit முடித்து அடுத்த Subject-க்கு செல்ல வேண்டும்.

**நிறுத்த வேண்டிய நிலை:** சரியான Book Edition உறுதி ஆகவில்லை என்றால், Source Answer Research-ஐ முன்னெடுத்துச் செல்லலாம்; ஆனால் அந்தப் பழைய புத்தகத்தின் PDF Page References அல்லது Quiz-ஐ Current Edition என்று Finalize செய்யக்கூடாது.


---

## 18. User Clarification + Cloudflare / Current-Book Verification Update (03-11-2026)

### 18.1 User's authoritative rule for textbook version

The project must use the textbook that students are actually studying in the **current academic year (2026–27)**. Do not assume a future year's planned syllabus, draft curriculum or proposed new edition is relevant.

For each supplied book, verify whether it matches the currently used student copy. A book may retain an older First Edition year while having a newer Revised Edition / Reprint / Correction. Therefore:
- First Edition year alone does not identify the current version.
- Reprint year alone does not prove content changed.
- Revised Edition / correction information, textbook contents, chapter structure, question text, page count and official current-year distribution must be compared together.
- If the same book was reprinted with corrections, record the correction/revision evidence and verify affected pages.
- If a substantially revised book has a new page count / TOC / unit structure, treat it as a different content version until verified.

**The user's supplied current book is the primary reference for question wording and scope once it is confirmed to match the current student edition.** Answer Websites such as BrainKart may be older. They are answer sources only: do not make the current questions fit an older website. Use an old Answer Source only where the underlying question and textbook context actually match; otherwise mark it as a mismatch and look for another source.

### 18.2 Cloudflare Pages URL supplied by user

- User-provided site: [https://tn-class-10.pages.dev/](https://tn-class-10.pages.dev/)
- The site is understood to be the Cloudflare Pages deployment of the same Class 10 GitHub repository.
- Its page links are relative, for example:
  - `./viewer.html?pdf=./tamil/00_prelims/page_001.pdf`
  - `./tamil/00_prelims/page_001.pdf`
- During this audit, the browser/web retrieval layer returned “URL is not accessible via this tool” for both the Cloudflare root and direct PDF route. This is a tool-access limitation; it does **not** establish that the site is broken for ordinary browsers.
- GitHub Repository access is working. The GitHub connector can read text files such as `index.html`, `viewer.html`, `questions.md`, `quiz.md`, and the recursive file Tree. It can retrieve PDF file bytes as Base64, but this connector response does not itself render PDF pages visually.
- The current Cloudflare deployment is a useful alternate page-viewing route for a browser that can access it. If direct PDF rendering is unavailable in the assistant's tools, record that limitation honestly; do not claim to have visually inspected the page.

### 18.3 Class 10 Tamil — comparison evidence

**Repo / Cloudflare index evidence (GitHub API):**
- Repository: [Eaglesiva/tn-class-10](https://github.com/Eaglesiva/tn-class-10)
- [Class 10 index.html](https://github.com/Eaglesiva/tn-class-10/blob/main/index.html) describes the site as the Class 10 annual textbook edition / digitised printed pages.
- Its Tamil section reports **248 pages**.
- It lists 9 Tamil lesson folders / units:
  1. mozhi_amuthaootru
  2. iyarkai_kaetkiradhaa
  3. panpaadu_virundhu
  4. ariviyal_seyarkai_nunnarivu
  5. kalvi_mozhipeyarppu
  6. kalai_panmugak_kalaignar
  7. naagarigam_sirragal_oli
  8. aram_sangailakkiyam
  9. manidham_jeyakaandham
- The PDF page files are split one page per file from `tamil/00_prelims/page_001.pdf` onward, continuing through `page_248.pdf`.

**Publicly viewable 2025 Revised Tamil textbook evidence:**
- [10th Tamil new book 2025–2026 — TAMILVITHAI FlipHTML5](https://fliphtml5.com/bison/xbxt/10th_Tamil_new_book_2025_-_2026/)
- The publication view contains **184 pages** (pages P:01 through P:184).
- Its second printed page states: First Edition 2019; Revised Editions 2020, 2021, 2022, 2023, 2024 and 2025; SCERT / Tamil Nadu Textbook and Educational Services Corporation details are printed on the page.
- Its Contents pages show **7 iyals**, not 9:
  1. மொழி, மனிதம்
  2. இயற்கை, சுற்றுச்சூழல், அறிவியல்
  3. பண்பாடு
  4. கல்வி
  5. கலை, அழகியல், புதுமை
  6. நாகரிகம், நாடு, சமூகம்
  7. அறம், தத்துவம், சிந்தனை
- The book's first Iyal begins with the same broad title group “மொழி, மனிதம்”; its contents include “அன்னை மொழியே”, “அமுதஊற்று”, “தமிழ்ச்சொல் வளம்”, etc.
- Page 184 is present as the final page in the publication view.

**Current academic-year distribution evidence:**
- [Tamil Nadu Textbook and Educational Services Corporation — Schools](https://textbookcorp.in/schools) states that the 2026–27 annual Tamil textbooks for Classes 1–10 and the annual books for Classes 9, 10 and 12 (Tamil and English Medium) went on sale from 10-04-2026.
- [Padasalai Class 10 2026–27 textbook page](https://www.padasalai.net/2026/05/Tamilnadu-Class-10-Text-Books-PDF-Download-2026-2027.html) separately lists 2026–27 Class 10 Tamil Medium and English Medium textbooks for Tamil, English, Maths, Science and Social Science. This is an index / distribution source, not the Government publisher itself.
- [CBSE Tamil Class 10 textbook comparison page](https://cbsetamil.com/ncert-tamil-book-for-class-10-pdf/) labels the 2025 Class 10 Tamil book as 184 pages and the 2024 book as 248 pages, and describes the 2025 book as current for 2026–27. This is a secondary comparison source; use the printed book / official distribution evidence as the authority.

### 18.4 Provisional finding — do not use repo Tamil PDF as the current book yet

There is a **strong structural mismatch**:
- Repo Tamil: 248 pages and 9 lesson folders.
- Public 2025 Revised Tamil book: 184 pages and 7 iyals.

The 2025 book publication also displays the 2025 revised-edition imprint. Official textbook distribution confirms 2026–27 annual Tamil books for Classes 1–10 are in the current distribution cycle.

Therefore, the current Repo Tamil PDF is **likely an older 248-page version**, while the 2025 Revised 184-page textbook is the leading candidate for the current 2026–27 student edition.

This remains a **strong provisional finding**, not a final visual audit of the supplied Repo PDF: the assistant's web/browser layer could not open the Cloudflare PDF page, and the GitHub PDF connector returned binary Base64 rather than a visual page. Before marking the Repo copy definitively “old”, compare the actual PDF's cover / imprint / contents / selected page images against the 184-page revised copy or an official 2026–27 issued copy.

**Do not generate or finalize current-year Tamil quiz data using the 248-page Repo book until this mismatch is resolved.** Preserve it as a legacy reference if needed.

### 18.5 Unit 1 Question wording clue

The 2025 Revised 184-page publication's first Iyal text includes the printed form **“எந்தமிழ்நா”** in the poem / prose section. The current Repo `questions.md` uses “எந்தமிழ்நா”, while the existing `quiz.md` has “எண்தமிழ்நா” in one question. This supports checking the original current textbook before copying quiz wording. It does not make the existing quiz question verified.

### 18.6 Correct next actions for Class 10 Tamil

1. Use the user's Cloudflare site and GitHub paths as the Repo-copy locator. Attempt the direct PDF / viewer route when tools support it; if not, record that page-level visual inspection was unavailable.
2. Obtain / open the 2025 Revised 184-page Tamil textbook or an official 2026–27 issued copy.
3. Compare cover, imprint, contents, total pages, all 7 Iyal titles, and Book Back evaluation pages against the Repo's 248-page / 9-folder structure.
4. If confirmed mismatch, label the existing Repo files as Legacy / Old Edition in the audit notes; do not destructively delete them.
5. Create or point to the correct current PDF page set before editing questions.md.
6. Verify the existing extracted questions against the current book. Preserve exact printed question wording and source page references.
7. Only after that, use BrainKart or another Answer Source as an answer reference. Compare each Answer Source question with the current textbook question before using it.
8. Create answers.md Source 1 records for all question types found. Mark missing answers honestly.
9. Derive quiz.md / quiz.json from verified objective questions and verified answers; preserve the existing Class 10 Tamil quiz presentation format, but do not blindly preserve the old quiz question text or answers.

### 18.7 Scope across other Classes

The supplied Cloudflare URL is specifically named `tn-class-10.pages.dev`. Do not infer Cloudflare hostnames for other classes. For Classes 1–12, obtain / verify the correct GitHub Repository or Cloudflare Pages URL for each class, then repeat the same Current-Book Version Gate at subject / medium / term level. A general URL pattern must not be invented.
