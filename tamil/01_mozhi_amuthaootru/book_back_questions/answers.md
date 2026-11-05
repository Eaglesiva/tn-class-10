# 10ஆம் வகுப்பு தமிழ் — இயல் 1: அமுதூற்று
# Answer Collection & Guide — Verified Working Draft

**ஆய்வு தேதி:** 05-11-2026  
**Repository:** \`Eaglesiva/tn-class-10\`  
**Base branch:** \`content/class10-tamil-iyal1-answers-quiz-2026-11-04\`  
**Working branch:** \`content/class10-tamil-iyal1-answer-guide-2026-11-05\`  
**File:** \`tamil/01_mozhi_amuthaootru/book_back_questions/answers.md\`

## 0. ஆய்வு வரம்பும் பதிப்பு நிலையும்

- இந்தப் பணியின் Original Question Inventory: அதே branch-ல் உள்ள \`questions.md\`. அதன் கேள்வி வரிசை, சொற்கள், வகைகள், options மாற்றப்படவில்லை.
- இந்த இயல் தொகுப்பில் உள்ள கேள்விகள்: **19** — கற்பவை கற்றபின் 5, MCQ 5, குறுவினா 2, சிறுவினா 4, நெடுவினா 3.
- Project Blueprint-ன் Section 22 மற்றும் \`docs/OFFICIAL_GOVERNMENT_CDN_VERIFICATION_PROOF.md\` பதிவின்படி, repository-யின் 248-page / 9-Iyal Class 10 Tamil PDF, SCERT API-யிலிருந்து கிடைத்த \`10th_Tamil_Text.pdf\` கோப்புடன் byte-size மற்றும் MD5/ETag அடிப்படையில் பொருந்தியதாகப் பதிவு செய்யப்பட்டுள்ளது. அதனால் இந்த வேலை 248-page / 9-Iyal பதிப்பை அடிப்படையாகக் கொள்கிறது; 184-page / 7-Iyal third-party copy-ஐ பதிப்புச் சான்றாக ஏற்கவில்லை.
- \`tamil/pages.json\`-ல் Iyal 1 PDF வரிசை \`page_011.pdf\` முதல் \`page_035.pdf\` வரை உள்ளது. \`questions.md\`-ல் உள்ள பழைய HTML mapping குறிப்புகளின்படி Karpavai வினாக்கள் page 28, MCQ page 29, குறுவினா/சிறுவினா தொகுதி page 30 எனக் குறிக்கப்பட்டுள்ளன.
- அந்த mapping-ஐ அடிப்படையாகக் கொண்டு Physical PDF Page குறிப்புகள் பதிவு செய்யப்பட்டுள்ளன. GitHub-இல் உள்ள தனிப்பட்ட page PDF-களை இந்த ஆய்வில் screenshot மூலம் திறந்து கண்ணால் ஒப்பிட முடியாததால், **Printed Textbook Page எண்கள் உறுதிசெய்யப்படவில்லை**. ஊகித்து அச்சுப் பக்க எண் சேர்க்கப்படவில்லை.
- பழைய 430-line \`answers.md\` இந்தப் புதிய branch-ன் parent branch-ல் அப்படியே உள்ளது. அந்தப் பழைய draft-ன் Source Findings மற்றும் வேறுபாடுகள் இங்கே மீளாய்வு செய்யப்பட்டுள்ளன; பழைய file-ஐ அழிக்கவோ மாற்றவோ இல்லை.
- இங்கே உள்ள “நமது சொந்த விடை” என்பது source-களின் கருத்துகளை ஒப்பிட்டு, அசல் \`questions.md\` கேள்வியை மாற்றாமல் எழுதப்பட்ட மாணவர் பயன்பாட்டு விடை. Source answer மற்றும் நமது விடை ஒன்றாகக் கலக்கப்படவில்லை.

## 1. பயன்படுத்திய Source Register

| ID | Source / Publisher | Direct URL | ஆண்டு / Edition | இந்த ஆய்வில் நிலை |
|---|---|---|---|---|
| S1 | BrainKart — 10th Tamil Iyal 1 Q&A | https://www.brainkart.in/article/Questions-and-Answers_11807/ | 21-07-2022 எனப் பக்கத்தில் காட்டுகிறது; பழைய 10th Tamil guide page | நேரடியாகத் திறந்து வினா/விடைகள் சரிபார்க்கப்பட்டது |
| S2 | TN Board Solutions — Chapter 1.5 எழுத்து, சொல் | https://tnboardsolutions.com/samacheer-kalvi-10th-tamil-guide-chapter-1-5/ | 11/14-10-2024 எனப் பக்கத்தில் காட்டுகிறது; exact edition குறிப்பிடப்படவில்லை | நேரடியாகத் திறந்து K1–K5, MCQ4, SQ1, MA3 போன்றவை சரிபார்க்கப்பட்டன |
| S3 | KalviBot — Unit 1 Section 1.5 Solutions | https://docs.kalvibot.in/2021/02/10th-tamil-unit-1-section-1-5-solutions.html | 23-02-2021 | நேரடியாகத் திறந்து K1–K5, MCQ4, SQ1, MA3 விடைகள் சரிபார்க்கப்பட்டன |
| S4 | GreenTamil — Iyal 1 Karpavai Kattrapin | https://www.greentamil.in/2021/06/1-10-tamil-iyal-1-karpavai-karrapin.html | 21-06-2021 | நேரடியாகத் திறந்து K1–K5 மற்றும் மாதிரி உரையாடல் சரிபார்க்கப்பட்டது; சில பதிவுகளில் வினைமுற்று/தொழிற்பெயர் குழப்பம் உள்ளது |
| S5 | Padasalai — 10th Tamil Book Back One Word PDF | https://padasalai.info/wp-content/uploads/2022/12/10th-Tamil-Book-Back-One-Word-Question-Paper-Tamil-Medium-PDF-Download.pdf | 12-2022 URL; PDF-ல் தனி edition குறிப்பிடப்படவில்லை | PDF திறக்கப்பட்டு முதல் பக்கம் screenshot மூலம் பார்த்து MCQ1–MCQ5 சரிபார்க்கப்பட்டன |
| S6 | தமிழ்ச்சங்கமம் — Iyal 1 Tamil Sol Valam Q&A | https://www.tamilsangamam.in/2021/08/10-1.html | 08-2021 | நேரடியாகத் திறந்து MA2 மற்றும் LA2 குறிப்புகள் சரிபார்க்கப்பட்டன |
| S7 | Samacheer Kalvi Guide — 10th Tamil Chapter 1.1 Annai Mozhiye | https://samacheerkalviguide.com/samacheer-kalvi-10th-tamil-guide-annai-mozhiye-question-answer/ | 30-11-2023 | நேரடியாகத் திறந்து MCQ3, SQ2, MA1, LA1 ஒப்பிடப்பட்டன |
| S8 | Tamil Virtual Academy — பெயர்ச் சொல் வகைகள் / தொழிற்பெயர் | https://www.tamilvu.org/en/node/1542 | பக்கத்தில் புதுப்பிப்பு 16-09-2026 | நேரடியாகத் திறந்து தொழிற்பெயர் வகை/விகுதி வரையறை சரிபார்க்கப்பட்டது |
| S9 | Tamil Virtual Academy — தொழிற்பெயரும் வினையாலணையும் பெயரும் | https://www.tamilvu.org/ta/courses-degree-a021-a0211-html-a02114l5-6138 | பக்கத்தில் புதுப்பிப்பு 16-09-2026 | நேரடியாகத் திறந்து பெயர்வகை வேறுபாடு சரிபார்க்கப்பட்டது |
| S10 | Tamil Virtual Academy — சிகரம், முதல் பருவம் PDF | https://www.tamilvu.org/courses/new_courses/level05/sem01/pdf/Cikaram_Sem_1.pdf#page=128 | 2025 முதல்பதிப்பு; PDF-ல் பக்கம் 128 குறிப்பு | பொதுமொழி வரையறை/வேங்கை எடுத்துக்காட்டு search text-ல் கிடைத்தது; PDF மிகப்பெரியதால் screenshot திறப்பு தோல்வியடைந்தது |
| S11 | TamilVithai — 10th Tamil Unit 1 Karpavai Kattrapin | https://www.tamilvithai.com/2022/07/10th-tamil-unit-1-karpavai-kattrapin.html | 03-07-2022 என indexed metadata காட்டுகிறது | Search excerpt-ல் K1–K5 தொடர்பான பதில்கள் கிடைத்தன; நேரடிப் பக்கத்தைத் திறக்கும்போது CAPTCHA/redirect தடையால் முழு verification முடியவில்லை |

### Source handling குறிப்புகள்

1. S1–S9-ல் மேற்கண்ட கேள்விகளுக்கான பதில் நேரடியாகக் காணப்பட்ட இடங்களையே கேள்வி வாரியான Source Answer ஆகப் பயன்படுத்தியுள்ளேன்.
2. S10 ஒரு 2025 Tamil Virtual Academy நூல்; அது 2019–2024 SCERT பாடநூல் பதிப்புக்குப் பதிலாகக் கொள்ளப்படவில்லை. பொதுமொழி வரையறைக்கான துணை இலக்கண ஆதாரமாக மட்டும் பயன்படுத்தப்பட்டுள்ளது.
3. S11-ன் search excerpt பழைய draft-ல் உள்ள findings-ஐ உறுதிப்படுத்துகிறது; ஆனால் நேரடி பக்கம் திறக்கப்படாததால் தனித்த Verified Source என எண்ணப்படவில்லை.
4. பழைய \`answers.md\`-ல் இருந்த GreenTamil main Iyal1 Q&A மற்றும் KalviWorld link-கள் பழைய ஆதாரப் பதிவுகளாகப் பாதுகாக்கப்பட்டுள்ளன. இந்த run-ல் அவற்றின் முழுப் பக்கத்தை மறுதிறந்து சரிபார்க்க முடியாத இடங்களில் புதிய Verified Source எண்ணிக்கையில் சேர்க்கவில்லை.
5. Search snippet மட்டும் கிடைத்த A2Z TNPSC / TamilVithai போன்ற பழைய candidates-ஐ உறுதிப்படுத்தப்பட்ட பதில் ஆதாரமாகக் கணக்கிடவில்லை.

---

## 2. கற்பவை கற்றபின் — 5 வினாக்கள்

### K1 | தனிமொழிகளுடன் சொற்களைச் சேர்த்துத் தொடர்மொழிகளாக்குக

**Original Question:**  
தேன், நூல், பை, மலர், வா - இத் தனிமொழிகளுடன் சொற்களைச் சேர்த்துத் தொடர்மொழிகளாக்குக.

**Book Reference:**
- Physical PDF Page: 28 — \`questions.md\` பழைய HTML page_28 mapping அடிப்படையில்; screenshot மூலம் உறுதிசெய்யப்படவில்லை.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; 05. எழுத்து, சொல் / கற்பவை கற்றபின்.
- Existing Page Mapping: \`tamil/pages.json\` → \`tamil/01_mozhi_amuthaootru/page_028.pdf\`; source HTML page_28 குறிப்பு.

**Source 1 — TN Board Solutions (S2):**
- Direct URL: https://tnboardsolutions.com/samacheer-kalvi-10th-tamil-guide-chapter-1-5/
- Edition / Year: 2024-ல் வெளியிடப்பட்ட guide page; edition விவரம் குறிப்பிடப்படவில்லை.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: தேன் — தேன் மருந்துப் பொருளாகப் பயன்படுகிறது; நூல் — நூல் பல கல்; பை — பை நிறைய பணம் இருந்தது; மலர் — மலர் பறித்து வந்தேன்; வா — விரைந்து வா.

**Source 2 — KalviBot (S3):**
- Direct URL: https://docs.kalvibot.in/2021/02/10th-tamil-unit-1-section-1-5-solutions.html
- Edition / Year: 23-02-2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: இதே ஐந்து தனிமொழிகளுக்கும் வாக்கிய/தொடர் எடுத்துக்காட்டுகள் தரப்பட்டுள்ளன.

**Source Comparison:**
- இரண்டு source-களும் ஐந்து சொற்களுக்கும் தொடர்மொழி எடுத்துக்காட்டுகளைத் தருகின்றன.
- எடுத்துக்காட்டு வாக்கியங்களில் சொல் தேர்வு மாறலாம்; கேள்வியின் நோக்கம் மாறவில்லை.

**நமது சொந்த விடை:**
1. தேன் — தேன் மருந்துப் பொருளாகப் பயன்படுகிறது.
2. நூல் — நூல் பல கல்.
3. பை — பை நிறையப் பணம் இருந்தது.
4. மலர் — மலர் பறித்து வந்தேன்.
5. வா — விரைந்து வா.

**காரண விளக்கம்:**  
தனித்து நின்று பொருள் தரும் ஒவ்வொரு சொல்லுடனும் மற்றொரு சொல் சேர்ந்து பொருள் முழுமை பெறும் வகையில் தொடர் அமைக்கப்பட்டுள்ளது. “நூல் பல கல்” என்பது நூல்களைப் பலவாகக் கற்று அறிவைப் பெருக்குக என்ற தொடராகப் பொருள் தருகிறது.

**Final Status:** \`ANSWER_FOUND\`

---

### K2 | வினையடிகளை விகுதிகளுடன் இணைத்துத் தொழிற்பெயர்களை உருவாக்குக

**Original Question:**  
வினையடியை விகுதிகளுடன் இணைத்துத் தொழிற்பெயர்களை உருவாக்குக. காண், சிரி, படி, தடு. எ.கா. காட்சி, காணுதல், காணல், காணாமை.

**Book Reference:**
- Physical PDF Page: 28 — existing page_28 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; 05. எழுத்து, சொல் / கற்பவை கற்றபின்.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_028.pdf\`.

**Source 1 — TN Board Solutions (S2):**
- Direct URL: https://tnboardsolutions.com/samacheer-kalvi-10th-tamil-guide-chapter-1-5/
- Edition / Year: 2024 guide page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: சிரி — சிரிப்பு, சிரித்தல், சிரிக்காமை; படி — படிப்பு, படித்தல், படிக்காமை; தடு — தடுப்பு, தடுத்தல், தடுக்காமை. காண் எடுத்துக்காட்டுகள் கேள்வியிலேயே கொடுக்கப்பட்டுள்ளன.

**Source 2 — KalviBot (S3):**
- Direct URL: https://docs.kalvibot.in/2021/02/10th-tamil-unit-1-section-1-5-solutions.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: S2-க்கு ஒத்த தொழிற்பெயர் வடிவங்கள் தரப்பட்டுள்ளன.

**Source 3 — Tamil Virtual Academy (S8):**
- Direct URL: https://www.tamilvu.org/en/node/1542
- Edition / Year: 2026-09-16 புதுப்பிப்பு.
- Answer Status: இலக்கண வரையறை சரிபார்க்கப்பட்டது.
- Source Answer: தொழிலை உணர்த்தும் பெயர் தொழிற்பெயர்; அல், தல் போன்ற விகுதிகள் கொண்டு வரும். விகுதி இல்லாத முதனிலை/முதனிலை திரிந்த தொழிற்பெயர்களும் உள்ளன.

**Source Comparison:**
- S2/S3 தொழிற்பெயர் வடிவங்களை வழங்குகின்றன.
- GreenTamil (S4) சில இடங்களில் “காண்பேன்”, “சிரிப்பேன்”, “சிரித்தாள்” போன்ற காலம்/நபர் காட்டும் வினைமுற்று வடிவங்களையும் பட்டியலில் சேர்த்துள்ளது. அவை தொழிற்பெயர்கள் அல்ல; அவற்றை விடையாக ஏற்கவில்லை.

**நமது சொந்த விடை:**

| வினையடி | தொழிற்பெயர் வடிவங்கள் |
|---|---|
| காண் | காட்சி, காணுதல், காணல், காணாமை |
| சிரி | சிரிப்பு, சிரித்தல், சிரிக்காமை |
| படி | படிப்பு, படித்தல், படிக்காமை |
| தடு | தடுப்பு, தடுத்தல், தடுக்காமை |

**காரண விளக்கம்:**  
தொழிற்பெயர் என்பது செயலைப் பெயராகக் குறிக்கும். “சிரித்தல்”, “படித்தல்”, “தடுத்தல்” போன்றவை தல் விகுதியுடன் வருகின்றன; “சிரிப்பு”, “படிப்பு”, “தடுப்பு” போன்றவை செயலைப் பெயராக்கும் வடிவங்கள். “சிரிப்பேன்” போன்றவை காலம்/நபர் காட்டும் வினைமுற்றுகள் என்பதால் இங்கே சேர்க்கப்படவில்லை.

**Final Status:** \`ANSWER_FOUND\`

---

### K3 | தனிமொழி, தொடர்மொழி கொண்டு உரையாடலைத் தொடர்க

**Original Question:**  
தனிமொழி, தொடர்மொழி ஆகியவற்றைக் கொண்டு உரையாடலைத் தொடர்க.

அண்ணன் : எங்கே செல்கிறாய்? (தொடர்மொழி)  
தம்பி : _____ (தனிமொழி)  
அண்ணன் : _____ _______ வாங்குகிறாய்? (தொடர்மொழி)  
தம்பி : _________________ (தொடர்மொழி)  
அண்ணன் : ______________(தனிமொழி)  
தம்பி : ____________ (தொடர்மொழி)  
அண்ணன் :  
தம்பி :

**Book Reference:**
- Physical PDF Page: 28 — existing page_28 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; 05. எழுத்து, சொல் / கற்பவை கற்றபின்.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_028.pdf\`.

**Source 1 — TN Board Solutions (S2):**
- Direct URL: https://tnboardsolutions.com/samacheer-kalvi-10th-tamil-guide-chapter-1-5/
- Edition / Year: 2024 guide page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: “கடைக்கு”, “இப்பொழுது என்ன வாங்குகிறாய்?”, “பருப்பு வாங்குகிறேன்”, “எதற்கு?”, “பருப்பு சோறு செய்ய அம்மா வாங்கி வரச் சொன்னார்கள்” என உரையாடல் எடுத்துக்காட்டு.

**Source 2 — KalviBot (S3):**
- Direct URL: https://docs.kalvibot.in/2021/02/10th-tamil-unit-1-section-1-5-solutions.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: S2-ல் உள்ள உரையாடல் அமைப்புடன் ஒத்த மாதிரி உரையாடல்.

**Source 3 — GreenTamil (S4):**
- Direct URL: https://www.greentamil.in/2021/06/1-10-tamil-iyal-1-karpavai-karrapin.html
- Edition / Year: 21-06-2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: கடைக்கு செல்வது, தேங்காய் வாங்குவது, கோயிலுக்குச் செல்வது, குன்றத்தூர் கோயில் என வேறு உரையாடல் எடுத்துக்காட்டு.

**Source Comparison:**
- அனைத்து source-களும் உரையாடலில் தனிமொழி/தொடர்மொழி பயன்பாட்டைக் காட்டுகின்றன.
- உரையாடல் உள்ளடக்கம் source-க்கு source மாறுகிறது; ஒரே மாதிரி உரையாடல் மட்டுமே கட்டாயம் என்று source கூறவில்லை.

**நமது சொந்த விடை:**

அண்ணன் : எங்கே செல்கிறாய்? (தொடர்மொழி)  
தம்பி : கடைக்கு. (தனிமொழி)  
அண்ணன் : இப்பொழுது என்ன வாங்குகிறாய்? (தொடர்மொழி)  
தம்பி : பருப்பு வாங்குகிறேன். (தொடர்மொழி)  
அண்ணன் : எதற்கு? (தனிமொழி)  
தம்பி : பருப்பு சோறு செய்ய அம்மா வாங்கிவரச் சொன்னார்கள். (தொடர்மொழி)  
அண்ணன் : இன்று பருப்புச் சோறு வேண்டாமென்று அம்மாவிடம் சொல்வோம். (தொடர்மொழி)  
தம்பி : சரி, இன்று அம்மாவைப் பிரியாணி செய்து தரச் சொல்வோம். (தொடர்மொழி)

**காரண விளக்கம்:**  
“கடைக்கு”, “எதற்கு?” போன்ற தனியாக வரும் ஒரு சொல் தனிமொழியாகப் பயன்படுத்தப்பட்டுள்ளது. “இப்பொழுது என்ன வாங்குகிறாய்?”, “பருப்பு வாங்குகிறேன்” போன்ற பல சொற்கள் இணைந்து முழுப் பொருள் தரும் இடங்கள் தொடர்மொழியாக அமைந்துள்ளன.

**Final Status:** \`ANSWER_FOUND\`

---

### K4 | வினைமுற்றுகளைத் தொழிற்பெயர்களாக மாற்றுக

**Original Question:**  
மலை என்னை அடிக்கடி அழைக்கும். மலைமீது ஏறுவேன்; ஓரிடத்தில் அமர்வேன்; மேலும் கீழும் பார்ப்பேன்; சுற்றுமுற்றும் பார்ப்பேன். மனம் அமைதி எய்தும். இத்தொடர்களில் உள்ள வினைமுற்றுகளைத் தனியே எடுத்தெழுதித் தொழிற்பெயர்களாக மாற்றுக.

**Book Reference:**
- Physical PDF Page: 28 — existing page_28 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; 05. எழுத்து, சொல் / கற்பவை கற்றபின்.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_028.pdf\`.

**Source 1 — TN Board Solutions (S2):**
- Direct URL: https://tnboardsolutions.com/samacheer-kalvi-10th-tamil-guide-chapter-1-5/
- Edition / Year: 2024 guide page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: அழைக்கும்—அழைத்தல்; ஏறுவேன்—ஏறுதல்; அமர்வேன்—அமர்தல்; பார்ப்பேன்—பார்த்தல்; எய்தும்—எய்தல்.

**Source 2 — KalviBot (S3):**
- Direct URL: https://docs.kalvibot.in/2021/02/10th-tamil-unit-1-section-1-5-solutions.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: S2-க்கு ஒத்த ஐந்து மாற்றங்கள்; இறுதி வடிவம் “எய்தல்”.

**Source 3 — GreenTamil (S4):**
- Direct URL: https://www.greentamil.in/2021/06/1-10-tamil-iyal-1-karpavai-karrapin.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: முதல் நான்கு மாற்றங்கள் ஒத்துள்ளன; கடைசியாக “எய்தும் — எய்துதல்” எனக் கொடுக்கப்பட்டுள்ளது.

**Source Comparison:**
- அழைத்தல், ஏறுதல், அமர்தல், பார்த்தல் ஆகிய நான்கு மாற்றங்களிலும் source-கள் ஒத்துள்ளன.
- கடைசி மாற்றத்தில் S2/S3 “எய்தல்” என்றும் S4 “எய்துதல்” என்றும் வேறுபடுகிறது.
- இரண்டு source-கள் தரும் “எய்தல்” வடிவத்தை இங்கு முதன்மை விடையாக வைத்துள்ளேன்; GreenTamil மாற்று வடிவம் மறைக்கப்படவில்லை.

**நமது சொந்த விடை:**

| வினைமுற்று | தொழிற்பெயர் |
|---|---|
| அழைக்கும் | அழைத்தல் |
| ஏறுவேன் | ஏறுதல் |
| அமர்வேன் | அமர்தல் |
| பார்ப்பேன் | பார்த்தல் |
| எய்தும் | எய்தல் |

**காரண விளக்கம்:**  
வினைமுற்றில் வரும் காலம்/நபர் சார்ந்த முடிவை நீக்கி, செயலைப் பெயராகக் குறிக்கும் தொழிற்பெயர் வடிவமாக மாற்ற வேண்டும். “மேலும் கீழும் பார்ப்பேன்”, “சுற்றுமுற்றும் பார்ப்பேன்” ஆகிய இரு இடங்களிலும் ஒரே “பார்ப்பேன்” வினைமுற்றே வருகிறது.

**Final Status:** \`CONFLICT\` — கடைசி வினைமுற்றின் தொழிற்பெயர் வடிவத்தில் source வேறுபாடு உள்ளது.

---

### K5 | தொழிற்பெயர்களை வகைப்படுத்துக

**Original Question:**  
கட்டு, சொட்டு, வழிபாடு, கேடு, பாடுதல் - இத்தொழிற்பெயர்களை வகைப்படுத்துக.

**Book Reference:**
- Physical PDF Page: 28 — existing page_28 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; 05. எழுத்து, சொல் / கற்பவை கற்றபின்.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_028.pdf\`.

**Source 1 — TN Board Solutions (S2):**
- Direct URL: https://tnboardsolutions.com/samacheer-kalvi-10th-tamil-guide-chapter-1-5/
- Edition / Year: 2024 guide page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது; ஆனால் ஐந்தாவது சொல் வேறுபடுகிறது.
- Source Answer: “கட்டு”, “சொட்டு”, “வழிபாடு”, “கேடு”, “கோறல்” என்ற பட்டியலில் கட்டு/சொட்டு — முதனிலைத் தொழிற்பெயர்; வழிபாடு/கோறல் — விகுதி பெற்ற தொழிற்பெயர்; கேடு — முதனிலை திரிந்த தொழிற்பெயர்.

**Source 2 — KalviBot (S3):**
- Direct URL: https://docs.kalvibot.in/2021/02/10th-tamil-unit-1-section-1-5-solutions.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது; ஐந்தாவது சொல் “கோறல்”.
- Source Answer: S2-க்கு ஒத்த வகைப்பாடு.

**Source 3 — GreenTamil (S4):**
- Direct URL: https://www.greentamil.in/2021/06/1-10-tamil-iyal-1-karpavai-karrapin.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது; ஐந்தாவது சொல் “கோறல்”.
- Source Answer: கட்டு/சொட்டு — முதனிலை; கேடு — முதனிலை திரிந்த; கோறல் — விகுதி பெற்ற. ஆனால் “வழிபாடு” மட்டும் முதனிலைத் தொழிற்பெயர் எனக் கூறுகிறது.

**Source 4 — Tamil Virtual Academy (S8):**
- Direct URL: https://www.tamilvu.org/en/node/1542
- Edition / Year: 2026-09-16 புதுப்பிப்பு.
- Answer Status: தொழிற்பெயர் விகுதி விதி சரிபார்க்கப்பட்டது.
- Source Answer: “தல்” விகுதி பெற்ற வடிவம் தொழிற்பெயராக அமையும்; “பாடுதல்” தல் விகுதி பெற்ற வடிவம்.

**Source Comparison:**
- \`questions.md\`-ல் உள்ள ஐந்தாவது சொல் **“பாடுதல்”**. S2/S3/S4-ல் அதற்குப் பதிலாக **“கோறல்”** உள்ளது. இவை ஒரே சொல் அல்ல; மாற்றப்படவில்லை.
- “வழிபாடு” வகைப்பாட்டில் S2/S3 விகுதி பெற்றது எனவும் S4 முதனிலை எனவும் முரண்படுகின்றன.
- ஆகவே source-ல் உள்ள “கோறல்” வகைப்பாட்டை “பாடுதல்” என்று மாற்றிப் பயன்படுத்தவில்லை.
- “பாடுதல்” என்பதற்கு TVA தொழிற்பெயர் விகுதி விதியைப் பயன்படுத்தி விகுதி பெற்ற தொழிற்பெயர் எனக் குறிக்க முடிகிறது.

**நமது சொந்த விடை — தற்போது ஆதரிக்கப்படும் பகுதி:**

| சொல் | வகை | ஆதார நிலை |
|---|---|---|
| கட்டு | முதனிலைத் தொழிற்பெயர் | S2/S3/S4 ஒத்துள்ளன |
| சொட்டு | முதனிலைத் தொழிற்பெயர் | S2/S3/S4 ஒத்துள்ளன |
| வழிபாடு | முதனிலை / விகுதி பெற்றது என்ற இரு வகைப்பாடுகள் உள்ளன | முரண்பாடு தீர்க்கப்படவில்லை |
| கேடு | முதனிலை திரிந்த தொழிற்பெயர் | S2/S3/S4 ஒத்துள்ளன |
| பாடுதல் | விகுதி பெற்ற தொழிற்பெயர் (தல் விகுதி) | S8 இலக்கண விதி ஆதரவு |

**காரண விளக்கம்:**  
முதனிலைத் தொழிற்பெயரில் வினைப்பகுதி தனியே தொழிற்பெயராக வரும். முதனிலை திரிந்த தொழிற்பெயரில் வினைப்பகுதி ஒலி/வடிவ மாற்றத்துடன் வரும். “தல்” போன்ற விகுதி இணைந்தால் விகுதி பெற்ற தொழிற்பெயராகும். “பாடுதல்” என்பதில் “தல்” விகுதி தெளிவாக உள்ளது. “வழிபாடு” பற்றிய source முரண்பாட்டை ஆதாரமின்றி ஒருதலைப்பட்சமாக முடிவு செய்யவில்லை.

**Final Status:** \`REVIEW_REQUIRED\` — “வழிபாடு” வகைப்பாடு முரண்பாடு மற்றும் “பாடுதல்” / “கோறல்” கேள்வி உரை வேறுபாடு காரணமாக இறுதி QC தேவை.

---

## 3. பலவுள் தெரிக — 5 வினாக்கள்

### MCQ1 | ‘மெத்த வணிகலன்’ என்னும் தொடரில் தமிழழகனார் குறிப்பிடுவது

**Original Question:**  
'மெத்த வணிகலன்' என்னும் தொடரில் தமிழகனார் குறிப்பிடுவது-

- அ) வணிக் கப்பல்களும் ஐம்பெரும் காப்பியங்களும்
- ஆ) பெரும் வணிகமும் பெருமக் கலன்களும்
- இ) ஐம்பெரும் காப்பியங்களும் அணிகலன்களும்
- ஈ) வணிக் கப்பல்களும் அணிகலன்களும்

**Book Reference:**
- Physical PDF Page: 29 — existing page_29 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; ஒருங்கிணைந்த Book Back MCQ.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_029.pdf\`.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 21-07-2022 எனப் பக்கத்தில் காட்டுகிறது.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: “வணிகக் கப்பல்களும் ஐம்பெருங்காப்பியங்களும்”.

**Source 2 — Padasalai PDF (S5):**
- Direct URL: https://padasalai.info/wp-content/uploads/2022/12/10th-Tamil-Book-Back-One-Word-Question-Paper-Tamil-Medium-PDF-Download.pdf
- Edition / Year: 2022 URL; PDF முதல் பக்கம்.
- Answer Status: PDF திறந்து முதல் பக்கம் screenshot மூலம் சரிபார்க்கப்பட்டது.
- Source Answer: அ) வணிகக் கப்பல்களும் ஐம்பெரும் காப்பியங்களும்.

**Source Comparison:**
- S1/S5 இரண்டும் option அ-ஐக் காட்டுகின்றன.
- பழைய \`answers.md\`-ல் இருந்த KalviWorld source option ஆ எனக் கூறியதாக பதிவு இருந்தது; அந்தப் பக்கத்தை இம்முறை மீண்டும் திறந்து சரிபார்க்க முடியவில்லை. அது legacy unverified conflict எனப் பாதுகாக்கப்படுகிறது; verified answer-ஐ மாற்றவில்லை.

**நமது சொந்த விடை:**  
**அ) வணிகக் கப்பல்களும் ஐம்பெரும் காப்பியங்களும்.**

**காரண விளக்கம்:**  
இரட்டுற மொழிதலில் ஒரே தொடர் தமிழுக்கும் கடலுக்கும் பொருந்தும். தமிழுக்கு ஐம்பெருங்காப்பியங்கள் அணிகலன்களாகக் குறிக்கப்படுகின்றன; கடலில் மிகுதியான வணிகக் கப்பல்கள் செல்வது குறிக்கப்படுகிறது. ஆகவே இரண்டு பொருள்களையும் இணைக்கும் option அ பொருந்துகிறது.

**Final Status:** \`ANSWER_FOUND\`

---

### MCQ2 | ‘காய்ந்த இலையும் காய்ந்த தோகையும்’ — அடிக்கோடிட்ட பகுதி

**Original Question:**  
'காய்ந்த இலையும் காய்ந்த தோகையும்' நிலத்துக்கு நல்ல உரங்கள். இத்தொடரில் அடிக்கோடிட்ட பகுதி குறிப்பிடுவது -

- அ) இலையும் சருகும்
- ஆ) தோகையும் சண்டும்
- இ) தாளும் ஓலையும்
- ஈ) சருகும் சண்டும்

**Book Reference:**
- Physical PDF Page: 29 — existing page_29 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; ஒருங்கிணைந்த Book Back MCQ.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_029.pdf\`.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: “சருகும் சண்டும்”.

**Source 2 — Padasalai PDF (S5):**
- Direct URL: https://padasalai.info/wp-content/uploads/2022/12/10th-Tamil-Book-Back-One-Word-Question-Paper-Tamil-Medium-PDF-Download.pdf
- Edition / Year: 2022 URL; PDF பக்கம் 1.
- Answer Status: screenshot மூலம் சரிபார்க்கப்பட்டது.
- Source Answer: ஈ) சருகும் சண்டும்.

**Source 3 — தமிழ்ச்சங்கமம் (S6):**
- Direct URL: https://www.tamilsangamam.in/2021/08/10-1.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகத் திறந்து சரிபார்க்கப்பட்டது.
- Source Answer: ஈ) சருகும் சண்டும்.

**Source Comparison:**
- மூன்று நேரடி ஆதாரங்களும் option ஈ-யில் ஒத்துள்ளன.
- பழைய draft-ல் KalviWorld option இ எனக் கூறியதாகப் பதிவு இருந்தது; நேரடிப் பக்கம் இம்முறை மீண்டும் சரிபார்க்கப்படவில்லை. அந்தப் பதிவு legacy unverified conflict ஆக மட்டுமே வைக்கப்பட்டுள்ளது.

**நமது சொந்த விடை:**  
**ஈ) சருகும் சண்டும்.**

**காரண விளக்கம்:**  
காய்ந்த இலைகள் சருகு எனவும், காய்ந்த தோகைச் சார்ந்த பகுதி சண்டு எனவும் இப்பாடப் பயன்பாட்டில் வேறுபடுத்தப்படுகிறது. எனவே இரண்டையும் இணைக்கும் விடை “சருகும் சண்டும்”.

**Final Status:** \`ANSWER_FOUND\`

---

### MCQ3 | ‘எந்தமிழ்நா’ என்பதைப் பிரித்தல்

**Original Question:**  
'எந்தமிழ்நா' என்பதைப் பிரித்தால் இவ்வாறு வரும் -

- அ) எந் + தமிழ் + நா
- ஆ) எந்த + தமிழ் + நா
- இ) எம் + தமிழ் + நா
- ஈ) எந்தம் + தமிழ் + நா

**Book Reference:**
- Physical PDF Page: 29 — existing page_29 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; Book Back MCQ.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_029.pdf\`.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: எம் + தமிழ் + நா.

**Source 2 — Samacheer Kalvi Guide (S7):**
- Direct URL: https://samacheerkalviguide.com/samacheer-kalvi-10th-tamil-guide-annai-mozhiye-question-answer/
- Edition / Year: 30-11-2023.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: option 3 — எம் + தமிழ் + நா.

**Source 3 — Padasalai PDF (S5):**
- Direct URL: https://padasalai.info/wp-content/uploads/2022/12/10th-Tamil-Book-Back-One-Word-Question-Paper-Tamil-Medium-PDF-Download.pdf
- Edition / Year: 2022 URL; PDF பக்கம் 1.
- Answer Status: screenshot மூலம் சரிபார்க்கப்பட்டது.
- Source Answer: இ) எம் + தமிழ் + நா.

**Source Comparison:**  
மூன்று ஆதாரங்களும் ஒரே பிரிப்பைத் தருகின்றன; முரண்பாடு இல்லை.

**நமது சொந்த விடை:**  
**இ) எம் + தமிழ் + நா.**

**காரண விளக்கம்:**  
பாடலில் உள்ள “எந்தமிழ்நா” என்ற தொடரின் பிரிப்பு “எம் + தமிழ் + நா” என வழங்கப்படுகிறது. இது S1, S5, S7 ஆகிய மூன்று ஆதாரங்களிலும் ஒத்துள்ளது.

**Final Status:** \`ANSWER_FOUND\`

---

### MCQ4 | தொழிற்பெயரும் வினையாலணையும் பெயரும்

**Original Question:**  
'கேட்டவர் மகிழப் பாடிய பாடல் இது' - தொடரில் இடம்பெற்றுள்ள தொழிற்பெயரும் வினையாலணையும் பெயரும் முறையே -

- அ) பாடிய; கேட்டவர்
- ஆ) பாடல்; பாடிய
- இ) கேட்டவர்; பாடிய
- ஈ) பாடல்; கேட்டவர்

**Book Reference:**
- Physical PDF Page: 29 — existing page_029 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; Book Back MCQ.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_029.pdf\`.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: பாடல்; கேட்டவர்.

**Source 2 — Padasalai PDF (S5):**
- Direct URL: https://padasalai.info/wp-content/uploads/2022/12/10th-Tamil-Book-Back-One-Word-Question-Paper-Tamil-Medium-PDF-Download.pdf
- Edition / Year: 2022 URL; PDF பக்கம் 1.
- Answer Status: screenshot மூலம் சரிபார்க்கப்பட்டது.
- Source Answer: ஈ) பாடல்; கேட்டவர்.

**Source 3 — Tamil Virtual Academy (S9):**
- Direct URL: https://www.tamilvu.org/ta/courses-degree-a021-a0211-html-a02114l5-6138
- Edition / Year: 2026-09-16 புதுப்பிப்பு.
- Answer Status: இலக்கண வேறுபாடு சரிபார்க்கப்பட்டது.
- Source Answer: தொழிற்பெயர் செயலைக் குறிக்கும்; வினையாலணையும் பெயர் அந்தச் செயலைச் செய்தவரைக் குறிக்கும்.

**Source Comparison:**  
S1/S5 பதில்கள் ஒத்துள்ளன. S9 இலக்கண வரையறை அந்தத் தேர்வை ஆதரிக்கிறது.

**நமது சொந்த விடை:**  
**ஈ) பாடல்; கேட்டவர்.**

**காரண விளக்கம்:**  
“பாடல்” என்பது பாடும் செயலைப் பெயராகக் குறிக்கும் தொழிற்பெயர். “கேட்டவர்” என்பது கேட்கும் செயலைச் செய்த நபரைக் குறிக்கிறது; எனவே அது வினையாலணையும் பெயர்.

**Final Status:** \`ANSWER_FOUND\`

---

### MCQ5 | பயிர்வகை

**Original Question:**  
வேர்க்கடலை, மிளகாய் விதை, மாங்கொட்டை ஆகியவற்றைக் குறிக்கும் பயிர்வகை -

- அ) குலை வகை
- ஆ) மணி வகை
- இ) கொழுந்து வகை
- ஈ) இலை வகை

**Book Reference:**
- Physical PDF Page: 29 — existing page_029 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; Book Back MCQ.
- Existing Page Mapping: \`tamil/pages.json\` → \`page_029.pdf\`.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: மணிவகை.

**Source 2 — Padasalai PDF (S5):**
- Direct URL: https://padasalai.info/wp-content/uploads/2022/12/10th-Tamil-Book-Back-One-Word-Question-Paper-Tamil-Medium-PDF-Download.pdf
- Edition / Year: 2022 URL; PDF பக்கம் 1.
- Answer Status: screenshot மூலம் சரிபார்க்கப்பட்டது.
- Source Answer: ஆ) மணிவகை.

**Source 3 — தமிழ்ச்சங்கமம் (S6):**
- Direct URL: https://www.tamilsangamam.in/2021/08/10-1.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: ஆ) மணி வகை.

**Source Comparison:**  
மூன்று ஆதாரங்களும் “மணி வகை” என ஒத்துள்ளன.

**நமது சொந்த விடை:**  
**ஆ) மணி வகை.**

**காரண விளக்கம்:**  
வேர்க்கடலை, மிளகாய் விதை, மாங்கொட்டை ஆகியவை விதை/மணியை அடிப்படையாகக் கொண்ட பயிர்வகை என வகைப்படுத்தப்பட்டுள்ளன.

**Final Status:** \`ANSWER_FOUND\`

---

## 4. குறுவினா — 2 வினாக்கள்

### SQ1 | ‘வேங்கை’ — தொடர்மொழி மற்றும் பொதுமொழி

**Original Question:**  
'வேங்கை' என்பதைத் தொடர்மொழியாகவும் பொதுமொழியாகவும் வேறுபடுத்திக் காட்டுக.

**Book Reference:**
- Physical PDF Page: 30 — \`questions.md\`-ல் உள்ள குறுவினா block mapping அடிப்படையில்; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; ஒருங்கிணைந்த Book Back குறுவினா.
- Existing Page Mapping: \`tamil/pages.json\` → Iyal 1 PDF range \`page_011.pdf\`–\`page_035.pdf\`; exact item mapping screenshot pending.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: “வேங்கை” மரத்தைக் குறிக்கும் தனிமொழி; “வேம் + கை” என்பது “வேகுகின்ற கை” எனப் பொருள் தரும் தொடர்மொழி.

**Source 2 — TN Board Solutions (S2):**
- Direct URL: https://tnboardsolutions.com/samacheer-kalvi-10th-tamil-guide-chapter-1-5/
- Edition / Year: 2024 guide page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: S1-க்கு ஒத்த மரம் / வேம் + கை விளக்கம்.

**Source 3 — Tamil Virtual Academy (S10):**
- Direct URL: https://www.tamilvu.org/courses/new_courses/level05/sem01/pdf/Cikaram_Sem_1.pdf#page=128
- Edition / Year: 2025 முதல்பதிப்பு; PDF பக்கம் 128.
- Answer Status: PDF text excerpt கிடைத்தது; screenshot செய்யும் முயற்சி PDF அளவு காரணமாக தோல்வியடைந்தது.
- Source Answer: பொதுமொழி என்பது தனிமொழியாக ஒரு பொருளையும், பிரிந்து தொடர்மொழியாக வேறு பொருளையும் தரும் ஒரே சொல் என வரையறுக்கிறது. “வேங்கை” எடுத்துக்காட்டில் தனிமொழிப் பொருளாக “புலி” எனக் குறிப்பிடுகிறது; “வேம் + கை” எனப் பிரித்து “வேகின்ற கை” எனவும் கூறுகிறது.

**Source Comparison:**
- “பொதுமொழி” என்ற இலக்கண வரையறையில் source-கள் ஒத்துள்ளன.
- தனிமொழியாக “வேங்கை” தரும் பொருளில் பழைய Class 10 guide pages “மரம்” எனவும், 2025 TVA நூல் “புலி” எனவும் வேறுபடுகின்றன.
- 2025 TVA நூல் வேறு வெளியீடு என்பதால் பழைய Class 10 பாடநூல் விடையை மாற்றுவதற்குப் பயன்படுத்தப்படவில்லை. ஆனால் பொருள் வேறுபாடு தெளிவாகப் பதிவு செய்யப்பட்டுள்ளது.

**நமது சொந்த விடை:**
- **தனிமொழி:** “வேங்கை” — வகை மரத்தைக் குறிக்கும் (Class 10 guide ஆதாரங்களில் வழங்கப்பட்ட பொருள்).
- **தொடர்மொழி:** “வேம் + கை” — வேகுகின்ற கை.
- **பொதுமொழி:** “வேங்கை” என்ற ஒரே சொல் தனியாக நின்று ஒரு பொருளையும், “வேம் + கை” எனப் பிரிந்தால் வேறு பொருளையும் தருவதால் பொதுமொழியாக அமைகிறது.

**காரண விளக்கம்:**  
ஒரே சொல் தனியாக நின்று ஒரு பொருளையும், பிரிக்கப்பட்டு தொடராக நின்று வேறு பொருளையும் தந்தால் அது பொதுமொழி. இங்கு தனிமொழி / தொடர்மொழி இரு நிலைகளும் ஒரே சொல்லில் அமைகின்றன.

**Final Status:** \`CONFLICT\` — தனிமொழிப் பொருளில் 2019–2024 Class 10 guide-களுக்கும் 2025 TVA நூலுக்கும் வேறுபாடு உள்ளது. பள்ளிப் பாடநூல் பக்கத்தை கண்ணால் ஒப்பிட்ட பின் இறுதி சொல் பொருளை lock செய்ய வேண்டும்.

---

### SQ2 | எஞ்சியுள்ள ஐம்பெருங்காப்பியங்களின் பெயர்கள்

**Original Question:**  
“மன்னும் சிலம்பே! மணிமேகலைவடிவே! முன்னும் நினைவால் முடிதாழ வாழ்த்துவமே!” – இவ்வடிகளில் இடம்பெற்றுள்ள காப்பியங்களைத் தவிர எஞ்சியுள்ள ஐம்பெருங் காப்பியங்களின் பெயர்களை எழுதுக.

**Book Reference:**
- Physical PDF Page: 30 — குறுவினா block-ன் existing page mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; அன்னை மொழியே.
- Existing Page Mapping: Iyal 1 PDF range \`page_011.pdf\`–\`page_035.pdf\`; exact printed page pending.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: சீவகசிந்தாமணி, வளையாபதி, குண்டலகேசி.

**Source 2 — Samacheer Kalvi Guide (S7):**
- Direct URL: https://samacheerkalviguide.com/samacheer-kalvi-10th-tamil-guide-annai-mozhiye-question-answer/
- Edition / Year: 30-11-2023.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: அதே மூன்று காப்பியங்கள்.

**Source Comparison:**  
S1/S7 ஒரே மூன்று பெயர்களையும் தருகின்றன. செய்யுளில் சிலப்பதிகாரம் மற்றும் மணிமேகலை குறிப்பிடப்பட்டுள்ளதால், மீதமுள்ள மூன்றையே எழுத வேண்டும்.

**நமது சொந்த விடை:**
1. சீவகசிந்தாமணி
2. வளையாபதி
3. குண்டலகேசி

**காரண விளக்கம்:**  
ஐம்பெருங்காப்பியங்களில் சிலப்பதிகாரம், மணிமேகலை ஆகிய இரண்டு நூல்கள் கொடுக்கப்பட்ட அடிகளில் சுட்டப்பட்டுள்ளன. எனவே அவற்றைத் தவிர மீதமுள்ள மூன்று காப்பியங்களின் பெயர்கள் எழுதப்படுகின்றன.

**Final Status:** \`ANSWER_FOUND\`

---

## 5. சிறுவினா — 4 வினாக்கள்

### MA1 | தமிழன்னையை வாழ்த்துவதற்கான காரணங்கள்

**Original Question:**  
தமிழன்னையை வாழ்த்துவதற்கான காரணங்களாகப் பாவலரேறு சுட்டுவன யாவை?

**Book Reference:**
- Physical PDF Page: 30 — \`questions.md\`-ல் உள்ள page_30 HTML source note; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; அன்னை மொழியே.
- Existing Page Mapping: \`tamil/pages.json\` → Iyal 1 PDF range \`page_011.pdf\`–\`page_035.pdf\`.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: செழுமை மிக்க தமிழ் உயிராக இருப்பது; அதன் பெருமையை முழுமையாகச் சொல்ல முடியாதது; தொன்மை, தனிச்சிறப்பு, இலக்கிய வளம்; நீண்ட நிலைத்தன்மை மற்றும் பிறமொழியினரின் பாராட்டு ஆகிய நான்கு காரணங்கள்.

**Source 2 — Samacheer Kalvi Guide (S7):**
- Direct URL: https://samacheerkalviguide.com/samacheer-kalvi-10th-tamil-guide-annai-mozhiye-question-answer/
- Edition / Year: 30-11-2023.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: குமரிக்கண்டம், பாண்டிய மன்னனின் மகள் என்ற உருவகம், திருக்குறள், பத்துப்பாட்டு, எட்டுத்தொகை, பதினெண்கீழ்க்கணக்கு, சிலப்பதிகாரம், மணிமேகலை ஆகிய இலக்கியச் செல்வங்களைச் சுட்டுகிறது.

**Source Comparison:**
- S1 நான்கு பொதுக் காரணங்களாகச் சுருக்குகிறது.
- S7 பாடல் வரிகளின் உருவகங்களையும் இலக்கியப் பெயர்களையும் விரிவாகக் கொடுக்கிறது.
- இரண்டையும் சேர்த்து எழுதும்போது பாடலின் பெருமைச் சுட்டுகளும் பொதுக் காரணங்களும் முழுமையாகக் கிடைக்கின்றன.

**நமது சொந்த விடை:**
1. தமிழ் இனிமையும் செழுமையும் நிறைந்த அன்னைமொழி; தமிழ்மொழி தமிழரின் உயிரோடு தொடர்புடையது.
2. தமிழின் பெருமையை முழுமையாகச் சொல்லி முடிப்பது அரிது.
3. தமிழ் மிகப் பழமையான மொழி; அதே நேரத்தில் இன்றும் இளமையும் தனிச்சிறப்பும் கொண்டதாக விளங்குகிறது.
4. திருக்குறள், எட்டுத்தொகை, பத்துப்பாட்டு, பதினெண்கீழ்க்கணக்கு, சிலப்பதிகாரம், மணிமேகலை போன்ற இலக்கியச் செல்வங்களை உடையது.
5. குமரிக்கண்டம், பாண்டிய மரபு போன்ற வரலாற்று/கவித்துவப் பெருமைகளுடன் பாடலில் தமிழன்னை போற்றப்படுகிறாள்.
6. பிறமொழியினரும் தமிழின் சிறப்பைப் பாராட்டும் அளவுக்கு அதன் புகழ் பரவியுள்ளது.

**காரண விளக்கம்:**  
பாடல் தமிழின் தொன்மை, இலக்கிய வளம், தனித்தன்மை, நிலைத்த வாழ்வு ஆகியவற்றைத் தமிழன்னையை வாழ்த்துவதற்கான அடிப்படைகளாக முன்வைக்கிறது. S1-ன் நான்கு காரணங்களும் S7-ன் பாடல் சார்ந்த குறிப்புகளும் இதை ஆதரிக்கின்றன.

**Final Status:** \`ANSWER_FOUND\`

---

### MA2 | இளம் பயிர் வகை ஐந்தின் பெயர்களைத் தொடர்களில் அமைக்க

**Original Question:**  
'புளியங்கன்று ஆழமாக நடப்பட்டுள்ளது.' இதுபோல் இளம் பயிர் வகை ஐந்தின் பெயர்களைத் தொடர்களில் அமைக்க.

**Book Reference:**
- Physical PDF Page: 30 — existing page_30 mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; தமிழ்ச்சொல் வளம்.
- Existing Page Mapping: Iyal 1 PDF range \`page_011.pdf\`–\`page_035.pdf\`.

**Source 1 — தமிழ்ச்சங்கமம் (S6):**
- Direct URL: https://www.tamilsangamam.in/2021/08/10-1.html
- Edition / Year: 08-2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: பிள்ளை, வடலி, நாற்று, கன்று, பைங்கூழ் என ஐந்து பெயர்களையும் வாக்கியங்களுடன் தருகிறது.

**Source 2 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: கன்று, பிள்ளை, நாற்று, பைங்கூழ் என நான்கு எடுத்துக்காட்டுகள் மட்டுமே அந்தப் பக்கத்தில் தரப்பட்டுள்ளன.

**Source 3 — Padasalai Quarterly Exam Answer Key (legacy candidate):**
- Direct URL: https://padasalai.info/wp-content/uploads/2022/09/10th-Tamil-Answer-Keys-to-Quarterly-Exam-2022-Original-Question-Paper-Maduarai-District-PDF-Download.pdf
- Edition / Year: 2022 மாவட்ட காலாண்டுத் தேர்வு answer key.
- Answer Status: Search excerpt-ல் ஐந்து பெயர்கள் கிடைத்தன; PDF பக்கத்தை இந்த run-ல் திறந்து screenshot செய்யவில்லை. Verified source எண்ணிக்கையில் சேர்க்கப்படவில்லை.
- Search excerpt: பிள்ளை, வடலி, நாற்று, கன்று, பைங்கூழ்.

**Source Comparison:**
- S6 கேள்வி கேட்டுள்ள ஐந்து எடுத்துக்காட்டுகளையும் வழங்குகிறது.
- S1 நான்கு எடுத்துக்காட்டுகள் மட்டுமே வழங்குகிறது; அது ஐந்தாவது எடுத்துக்காட்டை மறுப்பதில்லை, ஆனால் முழு எண்ணிக்கையை நிறைவேற்றவில்லை.
- S6-ன் ஐந்து பெயர்கள் source-ஆதாரமுள்ள விடையாகப் பயன்படுத்தப்பட்டுள்ளன.

**நமது சொந்த விடை:**
1. பிள்ளை — தென்னம்பிள்ளை வாங்கி வந்தேன்.
2. வடலி — காட்டில் பனைவடலியைப் பார்த்தேன்.
3. நாற்று — நெல் நாற்று நட்டேன்.
4. கன்று — வாழைக்கன்று நட்டேன்.
5. பைங்கூழ் — சோளப் பைங்கூழ் பசுமையாக உள்ளது.

**காரண விளக்கம்:**  
இளம் தென்னை/பனை/நெற்பயிர்/வாழை/சோளம் போன்ற தாவர வளர்ச்சிநிலைகளைச் சுட்டும் சொற்கள் தேர்ந்தெடுக்கப்பட்டுள்ளன. ஒவ்வொரு சொல்லும் தனித்தொடரில் பொருள் தெளிவாகப் பயன்படுத்தப்பட்டுள்ளது.

**Final Status:** \`ANSWER_FOUND\`

---

### MA3 | வினைமுற்றுகளைத் தொழிற்பெயர்களாக மாற்றுக

**Original Question:**  
'அறிந்து, அறியாது, புரிந்து, புரியாது, தெரிந்து, தெரியாது, பிறந்து, பிறவாது' இவை அனைத்தையும் யாம் அறிவோம். அதுபற்றி உமது அறிவுரை எமக்குத் தேவை இல்லை. எல்லாம் எமக்குத் தெரியும். இக்கூற்றில் வண்ண எழுத்துகளில் உள்ள வினைமுற்றுகளைத் தொழிற்பெயர்களாக மாற்றி எழுதுக.

**Book Reference:**
- Physical PDF Page: 30 — existing page_30 source reference; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; எழுத்து, சொல் / இலக்கணப் பயிற்சி.
- Existing Page Mapping: \`tamil/pages.json\` → Iyal 1 PDF range \`page_011.pdf\`–\`page_035.pdf\`.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது; ஆனால் source-ல் உள்ள வினை வடிவங்கள் \`questions.md\`-இல் உள்ள வடிவங்களிலிருந்து வேறுபடுகின்றன.
- Source Answer: அறிதல், அறியாமை, தெரிதல், தெரியாமை, புரிதல், புரியாமை, பிறத்தல், பிறவாமை.

**Source 2 — TN Board Solutions (S2):**
- Direct URL: https://tnboardsolutions.com/samacheer-kalvi-10th-tamil-guide-chapter-1-5/
- Edition / Year: 2024 guide page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது; source question-ல் \`அறிந்தது, அறியாதது...\` என்ற வேறு உரை வடிவம் உள்ளது.
- Source Answer: அறிதல்/அறியாமை, புரிதல்/புரியாமை, தெரிதல்/தெரியாமை, பிறத்தல்/பிறவாமை.

**Source 3 — KalviBot (S3):**
- Direct URL: https://docs.kalvibot.in/2021/02/10th-tamil-unit-1-section-1-5-solutions.html
- Edition / Year: 2021.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது; source question wording வேறுபடுகிறது.
- Source Answer: அதே எட்டு தொழிற்பெயர் வடிவங்கள்.

**Source Comparison:**
- \`questions.md\`-ல் “அறிந்து, புரிந்து, தெரிந்து, பிறந்து” என வரும் இடங்களில், S1/S2/S3 மற்றும் கிடைத்த 2024 பாடநூல் mirror text-ல் சில சொற்கள் “அறிந்தது, புரிந்தது, தெரிந்தது, பிறந்தது” என வருகின்றன. எதிர்மறை வடிவங்களிலும் source-களுக்கிடையே உரை வேறுபாடு உள்ளது.
- கேள்வி உரையை மாற்றவில்லை. கேள்வியில் உள்ள ஒவ்வொரு வினைச்சொல்லுக்கும் தொழிற்பெயர் வடிவத்தைத் தனியாகப் பொருத்தி எழுதியுள்ளேன்.
- source answer வடிவங்கள் ஒரே பொதுவான தொழிற்பெயர் மாற்றத்தை ஆதரித்தாலும், அசல் பக்கத்தில் வண்ண எழுத்துகளாக இருந்த துல்லியமான சொற்கள் PDF screenshot மூலம் உறுதிசெய்யப்படவில்லை.

**நமது சொந்த விடை:**

| கேள்வியில் உள்ள சொல் | தொழிற்பெயர் |
|---|---|
| அறிந்து | அறிதல் |
| அறியாது | அறியாமை |
| புரிந்து | புரிதல் |
| புரியாது | புரியாமை |
| தெரிந்து | தெரிதல் |
| தெரியாது | தெரியாமை |
| பிறந்து | பிறத்தல் |
| பிறவாது | பிறவாமை |

**காரண விளக்கம்:**  
தொழிற்பெயர் செயலைப் பெயராகக் குறிக்கும். நேர்மறை வடிவங்களில் செயலைக் குறிக்கும் “தல்” வடிவமும், எதிர்மறை வடிவங்களில் “ஆமை” வடிவமும் பயன்படுத்தப்படுகின்றன. மேலே உள்ள அட்டவணை \`questions.md\`-ல் உள்ள சொற்களை மாற்றாமல் அவற்றுக்கான பதில்களை இணைக்கிறது.

**Final Status:** \`PARTIAL\` — மாற்று வடிவங்கள் source-களில் உள்ளன; ஆனால் வண்ண எழுத்துகளின் அசல் வடிவம் மற்றும் page image உறுதிசெய்யப்பட வேண்டும்.

---

### MA4 | தமிழையும் கடலையும் இரட்டுற மொழியும் பாங்கு

**Original Question:**  
தமிழகனார் தமிழையும் கடலையும் இரட்டுறமொழியும் பாங்கினை விளக்குக.

**Book Reference:**
- Physical PDF Page: 30 — existing short-answer mapping; visual verification pending.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; இரட்டுற மொழிதல்.
- Existing Page Mapping: Iyal 1 PDF range \`page_011.pdf\`–\`page_035.pdf\`.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: முத்தமிழ்/முத்து, முச்சங்கம்/மூவகைச் சங்கு, ஐம்பெருங்காப்பியம்/வணிகக் கப்பல்கள், சங்கப் புலவர்கள்/அலைகள் காப்பது ஆகிய பொருத்தங்களை விளக்குகிறது.

**Source 2 — பழைய answers.md-ல் பதிவு செய்யப்பட்ட GreenTamil main Q&A (legacy evidence):**
- Direct URL: https://www.greentamil.in/2021/06/1-10-tamil-iyal-1-book-back-question.html
- Edition / Year: 19-06-2021 என பழைய source register-ல் பதிவு.
- Answer Status: முந்தைய draft-ல் பதில் உள்ளதாகப் பதிவு; இந்த run-ல் direct page anti-bot தடையால் மீண்டும் திறக்க முடியவில்லை. புதிய verified source கணக்கில் சேர்க்கப்படவில்லை.
- Legacy Answer Summary: முத்தமிழ், முச்சங்கம், மெத்த வணிகலன், சங்கத்தவர் காக்க ஆகிய நான்கு இரட்டுறப் பொருள்களை ஒப்பிடுகிறது.

**Source 3 — 2024 textbook mirror (supporting text only):**
- Direct URL: https://cbsetamil.com/wp-content/uploads/2024/02/10th-Tamil-Textbook-2024.pdf
- Edition / Year: PDF முகப்பில் 2019; திருத்திய பதிப்புகள் 2020–2024 எனக் குறிப்பிடுகிறது; third-party mirror.
- Answer Status: PDF text extraction-ல் இரட்டுற மொழிதல் அட்டவணை கிடைத்தது; இது official edition proof ஆகக் கணக்கிடப்படவில்லை.
- Source Answer: “மெத்த வணிகன்” பகுதியில் தமிழுக்கு ஐம்பெருங்காப்பியங்கள்; கடலுக்கு வணிகக் கப்பல்கள் எனப் பொருத்தம் காட்டப்படுகிறது.

**Source Comparison:**
- S1 நான்கு பொருத்தங்களையும் நேரடியாகத் தருகிறது.
- பழைய GreenTamil draft-லும் அதே அடிப்படைப் பொருத்தங்கள் பதிவு செய்யப்பட்டுள்ளன; ஆனால் direct page மீள்சரிபார்ப்பு முடியவில்லை.
- பாடநூல் mirror அட்டவணை குறைந்தபட்சம் “மெத்த வணிகலன்” பொருத்தத்தை ஆதரிக்கிறது.

**நமது சொந்த விடை:**

தமிழழகனார் ஒரே பாடல் தொடரில் தமிழின் சிறப்பையும் கடலின் வளத்தையும் இரட்டுற மொழிகிறார்.

1. **முத்தமிழ் — முத்து:** தமிழ் இயல், இசை, நாடகம் என முத்தமிழைக் கொண்டது. கடல் முத்துகளைத் தருகிறது.
2. **முச்சங்கம் — மூவகைச் சங்கு:** தமிழை முதல், இடை, கடை ஆகிய முச்சங்கங்கள் வளர்த்தன. கடல் வெண்சங்கு, சலஞ்சலம், பாஞ்சசன்யம் போன்ற மூவகைச் சங்குகளைத் தருகிறது.
3. **ஐம்பெருங்காப்பியங்கள் — வணிகக் கப்பல்கள்:** ஐம்பெருங்காப்பியங்கள் தமிழுக்கு அணிகலன்களாக உள்ளன. கடலில் ஏராளமான வணிகக் கப்பல்கள் செல்கின்றன.
4. **சங்கப் புலவர்கள் — கடல் அலைகள்:** சங்கப் புலவர்கள் தமிழைக் காத்தனர். கடல் அலைகள் சங்குகளைப் பாதுகாக்கின்றன என உருவகப்படுத்தப்படுகிறது.

**காரண விளக்கம்:**  
ஒரே சொல் அல்லது கருத்து இரண்டு வேறு பொருட்களுக்குப் பொருந்துமாறு அமைவது இரட்டுற மொழிதல். இப்பாடலில் தமிழின் இலக்கியச் சிறப்பும் கடலின் இயற்கை வளமும் இணையாகப் பொருத்தப்பட்டுள்ளன.

**Final Status:** \`ANSWER_FOUND\`

---

## 6. நெடுவினா — 3 வினாக்கள்

### LA1 | தமிழ்த்தாய் வாழ்த்துப் பாடல்களையும் பெருஞ்சித்திரனாரின் தமிழ் வாழ்த்தையும் ஒப்பிட்டு மேடைப்பேச்சு

**Original Question:**  
மனோன்மணீயம் சுந்தரனாரின் தமிழ்த்தாய் வாழ்த்துப் பாடலையும் பெருஞ்சித்திரனாரின் தமிழ் வாழ்த்தையும் ஒப்பிட்டு மேடைப்பேச்சு ஒன்றை உருவாக்குக.

**Book Reference:**
- Physical PDF Page: \`questions.md\`-ல் தனி physical page mapping தெளிவாக இல்லை.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; அன்னை மொழியே.
- Existing Page Mapping: \`tamil/pages.json\`-ல் இயல் 1க்கு \`page_011.pdf\`–\`page_035.pdf\`; நீண்ட வினாவுக்கான தனிப்பட்ட PDF பக்கம் மீள்குறிக்கப்பட வேண்டும்.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: சுந்தரனார் — கடலை ஆடையாக அணிந்த பூமிப் பெண், பாரதக் கண்டம் முகம், தக்காணப் பீடபூமி பிறைநெற்றி, தமிழகம் மணமிக்க திலகம்; தமிழ் தொன்மையுடனும் இளமையுடனும் விளங்குதல். பெருஞ்சித்திரனார் — குமரிக்கண்டம், பாண்டிய மன்னன் மகள், திருக்குறள், எட்டுத்தொகை, பத்துப்பாட்டு, பதினெண்கீழ்க்கணக்கு, சிலப்பதிகாரம், மணிமேகலை ஆகிய பெருமைகள்.

**Source 2 — Samacheer Kalvi Guide (S7):**
- Direct URL: https://samacheerkalviguide.com/samacheer-kalvi-10th-tamil-guide-annai-mozhiye-question-answer/
- Edition / Year: 30-11-2023.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: ஒப்பீட்டுப் பேச்சுக்கான அறிமுக உரை மற்றும் இரண்டு கவிஞர்களின் தமிழ்ப்பெருமைச் சுட்டுகள் வழங்கப்பட்டுள்ளன.

**Source Comparison:**
- இரண்டு source-களும் தமிழின் தொன்மை, இலக்கிய வளம், தனித்தன்மை ஆகியவற்றை இரு கவிஞர்களின் பாராட்டின் பொதுக் கருத்துகளாகக் காட்டுகின்றன.
- சுந்தரனார் புவியியல் உருவகத்தின் வழியாகத் தமிழகம்/தமிழ்த்தாயின் பெருமையைப் பாடுகிறார்; பெருஞ்சித்திரனார் வரலாறு மற்றும் இலக்கியச் செல்வங்களின் வழியாகப் பாடுகிறார்.

**நமது சொந்த விடை:**

**மதிப்பிற்குரிய தலைமை ஆசிரியரே, ஆசிரியப் பெருமக்களே, அன்பான மாணவச் செல்வங்களே! அனைவருக்கும் என் வணக்கம்.**

தமிழ்மொழியின் பெருமையைப் போற்றிய இரு கவிஞர்களின் தமிழ்த்தாய் வாழ்த்துகளை ஒப்பிட்டுப் பேசுவதில் மகிழ்ச்சி அடைகிறேன்.

மனோன்மணீயம் சுந்தரனார் தமது தமிழ்த்தாய் வாழ்த்தில் பூமியைப் பெண்ணாக உருவகப்படுத்துகிறார். கடலை ஆடையாக அணிந்த நிலமகளின் முகமாகப் பாரதக் கண்டத்தையும், பிறை போன்ற நெற்றியாகத் தென்னாட்டையும், நறுமணம் வீசும் திலகமாகத் தமிழகத்தையும் வருணிக்கிறார். அந்தத் திலகத்தின் மணம் உலகெங்கும் பரவுவது போலத் தமிழின் புகழும் எல்லாத் திசைகளிலும் பரவுகிறது என்கிறார். உலகின் மூத்த மொழியாக இருந்தாலும் தமிழ் இன்றும் இளமையுடனும் தனிச்சிறப்புடனும் விளங்குகிறது என்பதை அவர் வலியுறுத்துகிறார்.

பாவலரேறு பெருஞ்சித்திரனார் தமது தமிழ் வாழ்த்தில் தமிழின் தொன்மையையும் வரலாற்றுப் பெருமையையும் முன்னிறுத்துகிறார். குமரிக்கண்டம், பாண்டிய மன்னனின் மகள் என்ற உருவகம், திருக்குறளின் மாண்பு ஆகியவற்றைக் குறிப்பிடுகிறார். எட்டுத்தொகை, பத்துப்பாட்டு, பதினெண்கீழ்க்கணக்கு, சிலப்பதிகாரம், மணிமேகலை போன்ற இலக்கியச் செல்வங்களையும் தமிழின் பெருமைக்குச் சான்றுகளாகக் காட்டுகிறார்.

இரு கவிஞர்களின் பாடல்களிலும் தமிழின் பழமை, இனிமை, இலக்கிய வளம், தனித்தன்மை ஆகியவை போற்றப்படுகின்றன. சுந்தரனார் இயற்கை மற்றும் நில அமைப்பின் உருவகங்களால் தமிழின் புகழைப் பேசுகிறார்; பெருஞ்சித்திரனார் வரலாற்றையும் இலக்கியங்களையும் முன்வைத்து தமிழின் பெருமையை எடுத்துரைக்கிறார்.

**தமிழின் பெருமையை அறிந்து, அதன் செல்வங்களைப் படித்து, நம் வாழ்வில் தமிழைப் பயன்படுத்துவோம். தமிழை நேசிப்போம்; தமிழில் அறிவை வளர்ப்போம்.**

நன்றி. வணக்கம்.

**காரண விளக்கம்:**  
கேள்வி ஒப்பீட்டுப் பேச்சைக் கோருவதால், இரண்டு பாடல்களின் தனித்துவமான படிமங்களையும் அவற்றின் பொதுக் கருத்துகளையும் தனித்தனியாகக் கூறி, இறுதியில் ஒற்றுமையையும் வேற்றுமையையும் இணைத்துள்ளேன். முக்கியமான வரலாற்று/இலக்கியக் குறிப்புகள் S1/S7-ல் உள்ள சுருக்கங்களின் அடிப்படையில் எழுதப்பட்டுள்ளன.

**Final Status:** \`ANSWER_FOUND\`

---

### LA2 | தமிழின் சொல்வளம் மற்றும் புதிய சொல்லாக்கத் தேவை — உரைக் குறிப்புகள்

**Original Question:**  
தமிழின் சொல்வளம் பற்றியும் புதிய சொல்லாக்கத்திற்கான தேவை குறித்தும் தமிழ் மன்றத்தில் பேசுவதற்கான உரைக் குறிப்புகளை எழுதுக.

**Book Reference:**
- Physical PDF Page: \`questions.md\`-ல் தனி page mapping தெளிவாக இல்லை.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; உரைநடை உலகம் — தமிழ்ச்சொல் வளம்.
- Existing Page Mapping: \`tamil/pages.json\`-ல் Iyal 1க்கு \`page_011.pdf\`–\`page_035.pdf\`; குறிப்பிட்ட long-question PDF page மீள்குறிக்கப்பட வேண்டும்.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: தமிழின் சொல்வளம், ஒருபொருள் பல சொற்கள், பிற திராவிட மொழிச் சொற்களுடனான தொடர்பு; புதிய சொல்லாக்கத்தின் பயன்பாடு, மொழி வளர்ச்சி, உயர்கல்வி, பாடநூல், ஆய்வு, தமிழின் தனித்தன்மை ஆகியவை.

**Source 2 — தமிழ்ச்சங்கமம் (S6):**
- Direct URL: https://www.tamilsangamam.in/2021/08/10-1.html
- Edition / Year: 08-2021.
- Answer Status: நேரடியாகத் திறந்து சரிபார்க்கப்பட்டது.
- Source Answer: அறிமுகவுரை, சொல்வளம், சொல்லாக்கத் தேவை, நிறைவுரை என உரைக்குறிப்பு அமைப்பு; அறிவியல் வளர்ச்சி மற்றும் பிற ஆய்வுச் சிந்தனைகளைத் தமிழில் எழுத வேண்டிய அவசியம்.

**Source Comparison:**
- S1/S6 ஒரே மையக் கருத்துகளைத் தருகின்றன.
- S6 உரைக்குறிப்பு வடிவத்தைத் தெளிவாக அமைக்கிறது; S1 சொல்லாக்கத் தேவையின் கூடுதல் காரணங்களை விரிவாக்குகிறது.

**நமது சொந்த விடை:**

**தலைப்பு: தமிழின் சொல்வளமும் புதிய சொல்லாக்கத்தின் தேவையும்**

**அறிமுகம்**
- அன்னைமொழியான தமிழ் தொன்மையும் இனிமையும் கொண்ட செம்மொழி.
- மொழியின் வளத்தை அதன் சொற்களின் பெருக்கம், நுண்பொருள் வேறுபாடு, புதிய கருத்துகளை வெளிப்படுத்தும் திறன் ஆகியவை காட்டுகின்றன.

**தமிழின் சொல்வளம்**
1. ஒரே பொருளைக் குறிக்கப் பல சொற்கள் தமிழில் உள்ளன. எடுத்துக்காட்டாக, சொல்லுதல், பேசுதல், உரைத்தல், கூறுதல், இயம்பல் போன்ற சொற்கள் பயன்படுகின்றன.
2. நிலம், தாவரம், பயிர், உணவு, இயற்கை போன்ற வாழ்வியல் துறைகளுக்கே உரிய நுணுக்கமான சொற்கள் தமிழில் உள்ளன.
3. ஒரே சொல்லின் பொருள் சூழலுக்கு ஏற்ப மாறுபடுவதும் தமிழின் சொல்வளத்தை வெளிப்படுத்துகிறது.
4. இலக்கியங்களும் பழமையான வாழ்வியல் அனுபவங்களும் தமிழின் சொற்களஞ்சியத்தை வளப்படுத்தியுள்ளன.

**புதிய சொல்லாக்கத்திற்கான தேவை**
1. அறிவியல், தொழில்நுட்பம், மருத்துவம், கணினி போன்ற துறைகளில் உருவாகும் புதிய கருத்துகளைத் தமிழில் கூற புதிய கலைச்சொற்கள் தேவை.
2. உயர்கல்வி மற்றும் பாடநூல்களைத் தமிழில் உருவாக்கத் துல்லியமான சொல்லாக்கம் அவசியம்.
3. உலகின் புதிய ஆய்வுகள் மற்றும் சிந்தனைகளைத் தமிழில் மொழிபெயர்த்து அனைவரும் புரிந்துகொள்ளச் சொல்லாக்கம் உதவுகிறது.
4. பிறமொழிச் சொற்களைத் தேவையின்றி கலக்காமல் தமிழின் தனித்தன்மை, இனிமை ஆகியவற்றைப் பேண உதவுகிறது.
5. காலத்திற்கேற்ப மொழி வளரவும் புதிய அறிவை வெளிப்படுத்தவும் சொல்லாக்கம் தேவை.

**நிறைவுரை**
- தமிழின் பழைய சொல்வளத்தைப் பாதுகாப்பதோடு புதிய அறிவுக்கும் ஏற்ற சொற்களை உருவாக்குவோம்.
- தமிழில் கல்வி, அறிவியல், ஆய்வு ஆகிய துறைகளை வளர்ப்போம். தமிழின் தனித்தன்மையைப் பேணி அடுத்த தலைமுறைக்கு எடுத்துச் செல்வோம்.

**காரண விளக்கம்:**  
கேள்வி “சொல்வளம்” மற்றும் “புதிய சொல்லாக்கத் தேவை” என்ற இரண்டு தலைப்புகளைக் கோருகிறது. எனவே அவற்றைத் தனித்தனி பிரிவுகளாக அமைத்து, source-களில் உள்ள பலசொல் வளம், துறைக்கேற்ற நுண்சொற்கள், உயர்கல்வி, அறிவியல், மொழிபெயர்ப்பு, மொழித்தன்மை ஆகிய காரணங்களை இணைத்துள்ளேன்.

**Final Status:** \`ANSWER_FOUND\`

---

### LA3 | தமிழ் உரைநடையின் சிறப்பைப் பற்றி உரையாடுக

**Original Question:**  
ஒரு பக்க அளவில் உரையாடல் எழுதுக.  
சூழல் – வெளிநாட்டிலிருந்து உங்கள் இல்லத்திற்கு வந்திருக்கும் உறவினரின் மகளுக்குத் தமிழ் மொழியைப் பேச மட்டுமே தெரியும். ஆங்கில இலக்கியம் படித்த அவரிடம் தமிழ் உரைநடையின் சிறப்புப் பற்றி உரையாடுதல்.

**Book Reference:**
- Physical PDF Page: \`questions.md\`-ல் தனி page mapping தெளிவாக இல்லை.
- Printed Textbook Page: உறுதிசெய்யப்படவில்லை.
- Chapter: இயல் 1 — அமுதூற்று; விரிவானம் — உரைநடையின் அணிநலன்கள்.
- Existing Page Mapping: \`tamil/pages.json\`-ல் Iyal 1க்கு \`page_011.pdf\`–\`page_035.pdf\`; குறிப்பிட்ட long-question PDF page மீள்குறிக்கப்பட வேண்டும்.

**Source 1 — BrainKart (S1):**
- Direct URL: https://www.brainkart.in/article/Questions-and-Answers_11807/
- Edition / Year: 2022 page.
- Answer Status: நேரடியாகச் சரிபார்க்கப்பட்டது.
- Source Answer: குமரன்–யாழினி உரையாடல்; உரையாடல்/உரைநடை பொருள், உரைநடை வளர்ச்சி, உவமை/உருவகம், உணர்ச்சியை வெளிப்படுத்தும் நடை, சங்க இலக்கியக் குறிப்புகள் ஆகியவை இடம்பெறுகின்றன.

**Source 2 — GreenTamil main Iyal1 Q&A (legacy source finding):**
- Direct URL: https://www.greentamil.in/2021/06/1-10-tamil-iyal-1-book-back-question.html
- Edition / Year: பழைய \`answers.md\`-ல் 19-06-2021 எனப் பதிவு.
- Answer Status: பழைய draft-ல் மாற்று உரையாடல் இருந்ததாகக் குறிப்பிடப்பட்டுள்ளது; anti-bot தடையால் இந்த run-ல் நேரடியாக மீண்டும் திறக்க முடியவில்லை. Verified second answer source எனக் கணக்கிடப்படவில்லை.
- Legacy Answer Summary: தமிழரசி–கவியரசி என்ற பாத்திரங்களுடன் உரைநடை, வாசிப்பு, வளர்ச்சி, சிறுகதை/புதினம்/மொழிபெயர்ப்பு பற்றிய உரையாடல்.

**Source Comparison:**
- S1-ல் கேள்விக்கான நேரடி உரையாடல் உள்ளது.
- S2-ல் மாற்று உரையாடல் இருந்ததாக முந்தைய draft பதிவு செய்கிறது; இந்த ஆய்வில் direct re-verification கிடைக்கவில்லை.
- எனவே கீழே உள்ள உரையாடல் S1 கருத்துகளை அடிப்படையாகக் கொண்டு புதிதாக அமைக்கப்பட்ட சொந்த மாதிரி; இரண்டாவது source-ல் இருந்து நேரடியாக எடுக்கப்பட்டதாகக் கூறவில்லை.

**நமது சொந்த விடை:**

**பாத்திரங்கள்: அருண் — வீட்டிற்கு வந்திருக்கும் உறவினர் மகள் மீனா**

மீனா : வணக்கம் அருண்! நான் தமிழ் பேசுவேன். ஆனால் தமிழ் நூல்களை அதிகம் படித்ததில்லை. தமிழ் உரைநடை என்றால் என்ன?

அருண் : வணக்கம் மீனா! நாம் இயல்பாகப் பேசும் கருத்துகளைத் தெளிவான வாக்கியங்களாக எழுதுவது உரைநடை. செய்யுளைப் போல குறிப்பிட்ட யாப்பு அமைப்பில் இருக்க வேண்டிய கட்டாயம் இதற்கு இல்லை.

மீனா : அப்படியானால் உரைநடை எதற்கெல்லாம் பயன்படுகிறது?

அருண் : கதை, புதினம், கட்டுரை, வாழ்க்கை வரலாறு, வரலாறு, அறிவியல் விளக்கம், செய்தி, பாடநூல் எனப் பலவற்றை உரைநடையில் எழுதலாம். கடினமான கருத்துகளையும் எளிய வாக்கியங்களில் விளக்க முடியும்.

மீனா : தமிழ் உரைநடைக்கு நீண்ட வரலாறு உள்ளதா?

அருண் : ஆம். தொல்காப்பியர் காலத்திலேயே உரைநடை பற்றிய குறிப்புகள் இருப்பதாக அறியலாம். பின்னர் பல நூற்றாண்டுகளாக உரைநடை வளர்ந்து, குறிப்பாகப் பிற்காலத்தில் பல உரைநடை நூல்கள் வெளிவந்தன.

மீனா : உரைநடையில் அழகும் இருக்குமா? அது வெறும் தகவல் சொல்லும் முறையா?

அருண் : இல்லை. உரைநடையிலும் அழகு உண்டு. சரியான சொல் தேர்வு, தெளிவான வாக்கிய அமைப்பு, உவமை, உருவகம், கருத்துகளை அழகாக அடுக்குதல் ஆகியவை வாசிப்பவரின் மனத்தில் உணர்ச்சியை ஏற்படுத்தும்.

மீனா : செய்யுளுக்கும் உரைநடைக்கும் என்ன வேறுபாடு?

அருண் : செய்யுள் ஓசை, அடி, யாப்பு போன்ற அமைப்புகளுடன் அமையும். உரைநடை இயல்பான வாக்கிய ஓட்டத்தில் கருத்தைச் சொல்லும். அதனால் உரைநடை வழியாக நீண்ட கருத்துகளையும் விளக்கங்களையும் எளிதில் புரிந்துகொள்ளலாம்.

மீனா : தமிழ் உரைநடையில் நான் எதை முதலில் படிக்கலாம்?

அருண் : உனக்குப் பிடித்த சிறுகதைகள், கட்டுரைகள், வாழ்க்கை வரலாறுகள், செய்தித்தாள்களின் சிறப்புக் கட்டுரைகள் ஆகியவற்றில் தொடங்கலாம். தெரியாத சொற்களைப் பொருளுடன் குறித்துக்கொள்.

மீனா : மிகவும் பயனுள்ள விளக்கம். இனிமேல் தமிழ் நூல்களையும் உரைநடைக் கட்டுரைகளையும் படிக்கத் தொடங்குகிறேன்.

அருண் : மகிழ்ச்சி! தொடர்ந்து படித்தால் தமிழில் பேசுவதோடு நன்றாக எழுதவும் முடியும்.

**காரண விளக்கம்:**  
இந்த உரையாடல் கேள்வியில் கொடுக்கப்பட்ட சூழலைப் பின்பற்றுகிறது. உரைநடையின் வரையறை, பயன்பாடுகள், வளர்ச்சி, உவமை/உருவகம் மற்றும் தெளிவான கருத்து வெளிப்பாடு ஆகியவை S1-ல் உள்ள பாடக்கருத்துகளின் அடிப்படையில் சொந்த வார்த்தைகளில் அமைக்கப்பட்டுள்ளன.

**Final Status:** \`PARTIAL\` — ஒரு நேரடி answer source மட்டும் இந்த run-ல் மீள்சரிபார்க்கப்பட்டது; இரண்டாவது source-ன் முந்தைய finding மீண்டும் திறந்து உறுதிசெய்யப்படவில்லை.

---

## 7. Legacy Source Findings — பாதுகாக்கப்பட்ட குறிப்புகள்

பழைய \`answers.md\`-ல் இருந்த பயனுள்ள findings-ஐ இழக்காமல் இருக்க கீழே சுருக்கமாகப் பதிவு செய்கிறேன். இவை அனைத்தும் இந்தப் புதிய run-ல் direct source verification பெற்றவை என்று பொருள் கொள்ளக்கூடாது.

| பழைய Source | பழைய finding | புதிய ஆய்வில் கையாளும் முறை |
|---|---|---|
| GreenTamil main Iyal1 Q&A — https://www.greentamil.in/2021/06/1-10-tamil-iyal-1-book-back-question.html | Iyal1 வினாக்கள், MA1–MA4, LA1–LA3, source answer summaries | பழைய draft-ல் இருந்த findings பாதுகாக்கப்பட்டன; தற்போதைய browser run-ல் anti-bot காரணமாக page மீள்சரிபார்ப்பு முடியவில்லை |
| TamilVithai — https://www.tamilvithai.com/2022/07/10th-tamil-unit-1-karpavai-kattrap in.html | K1–K5-க்கு மாற்று எடுத்துக்காட்டுகள்/பதில்கள் | Search excerpt மட்டும் மீண்டும் கிடைத்தது; direct page CAPTCHA காரணமாக verified எண்ணிக்கையில் சேர்க்கப்படவில்லை |
| KalviWorld — https://www.kalviworldofficial.in/2025/06/10th-tamil-book-back-answers-unit-1.html | MCQ1/MCQ2-ல் பிற ஆதாரங்களிலிருந்து மாறுபட்ட விடைகள் | பழைய conflicting findings அழிக்கப்படவில்லை; direct page இந்த run-ல் மீண்டும் திறக்கப்படாததால் unverified legacy conflict எனக் குறிக்கப்பட்டது |
| A2Z TNPSC — https://www.a2ztnpsc.in/2024/07/10th-std-1.html | MCQ1 தொடர்பான search preview | முந்தைய draft-ல் direct page open 502 எனப் பதிவு; answer verification source ஆக எண்ணப்படவில்லை |
| Tamil Virtual Academy PDF — https://www.tamilvu.org/courses/new_courses/level05/sem01/pdf/Cikaram_Sem_1.pdf#page=128 | தனிமொழி/தொடர்மொழி/பொதுமொழி வரையறை | புதிய 2025 TVA வெளியீட்டின் துணை இலக்கண ஆதாரமாகப் பயன்படுத்தப்பட்டது; பழைய SCERT edition-ஐ மாற்றாது |

---

## 8. Chapter QA — கணக்கீடு

**Original inventory:** \`questions.md\`-ல் 19 கேள்விகள்.  
**New answer entries:** இந்த file-ல் 19/19 கேள்விகளுக்கும் தனி entry உருவாக்கப்பட்டுள்ளது.

| QA அளவுகோல் | எண்ணிக்கை | குறிப்பு |
|---|---:|---|
| மொத்த கேள்விகள் | 19 | \`questions.md\` inventory எண்ணிக்கை |
| answers.md-ல் entry உள்ளவை | 19 | K1–K5, MCQ1–5, SQ1–2, MA1–4, LA1–3 |
| குறைந்தது ஒரு நேரடி Answer Page-ல் பதில் காணப்பட்டவை | 19 | சிலவற்றில் source wording mismatch/partial answer உள்ளது |
| இரண்டு அல்லது அதற்கு மேற்பட்ட answer references உள்ளவை | 18 | LA3 மட்டும் இம்முறை ஒரு direct answer page-ல் உறுதிசெய்யப்பட்டது |
| ஒரே direct answer reference மட்டும் verified | 1 | LA3 |
| Source / wording conflict உள்ளவை | 5 | K2, K4, K5, SQ1, MA3 |
| Final Status: ANSWER_FOUND | 14 | source ஒப்பீட்டால் ஏற்ற விடை கிடைத்தவை |
| Final Status: PARTIAL | 2 | MA3, LA3 |
| Final Status: CONFLICT | 2 | K4, SQ1 |
| Final Status: REVIEW_REQUIRED | 1 | K5 |
| Final Status: OWN_ANSWER_FROM_TEXTBOOK | 0 | இந்த இயலில் தனியாக source-இல்லாத textbook-only answer என வகைப்படுத்திய வினா இல்லை |
| Final Status: ANSWER_NOT_FOUND | 0 | எல்லா 19 கேள்விகளுக்கும் குறைந்தது ஒரு பதில்/ஆதார வழி உள்ளது |
| Final Status: WRONG_EDITION | 0 | தற்போதைய working source-களில் edition mismatch எனத் தீர்மானிக்கப்பட்ட வினா இல்லை |
| Book PDF Printed Page verified | 0 | தனிப்பட்ட page PDF screenshot திறக்கப்படவில்லை; அச்சுப் பக்க எண்கள் ஊகிக்கப்படவில்லை |
| Existing PDF mapping reference | 3 mapping groups | page 28 / page 29 / page 30; physical file naming மற்றும் \`questions.md\` HTML note அடிப்படையில் |

### திறந்த QA பணிகள்

1. K4: “எய்தல்” / “எய்துதல்” இரண்டில் பாடநூல் பக்கத்தின் எழுத்துருவை நேரில் ஒப்பிட்டு ஒன்றை உறுதிசெய்ய வேண்டும்.
2. K5: “வழிபாடு” வகைப்பாட்டில் source முரண்பாட்டை அதிகாரப்பூர்வ பாடநூல் இலக்கண உதாரணத்துடன் தீர்க்க வேண்டும்; “பாடுதல்” என்பதை “கோறல்” என மாற்றக்கூடாது.
3. SQ1: பாடநூல் பக்கத்தில் “வேங்கை” தனிமொழிப் பொருளை நேரில் சரிபார்க்க வேண்டும்; 2025 TVA துணை நூல் “புலி” எனக் குறிப்பிடுவது பழைய guide-களின் “மரம்” பதிலுடன் வேறுபடுகிறது.
4. MA3: PDF பக்கத்தில் வண்ண எழுத்துகளாக அச்சிடப்பட்ட துல்லியமான வினை வடிவங்களை screenshot மூலம் உறுதிசெய்ய வேண்டும். \`questions.md\` உரை மாற்றப்படவில்லை.
5. LA3: இரண்டாவது direct answer source மீள்திறந்து சரிபார்க்கப்பட வேண்டும்.
6. page 28/29/30 மற்றும் LA1–LA3 ஆகியவற்றுக்கான exact printed page number / physical PDF cross-check இன்னும் செய்யப்பட வேண்டும்.

## 9. பாதுகாப்பு மற்றும் மாற்ற வரம்பு

- \`main\` branch மாற்றப்படவில்லை.
- \`questions.md\` மாற்றப்படவில்லை.
- \`quiz.md\`, \`quiz.json\`, \`pages.json\`, PDF files, viewer/routing configuration மாற்றப்படவில்லை.
- Edition Audit branch-கள் பயன்படுத்தப்படவில்லை.
- பழைய \`answers.md\` அடங்கிய branch அப்படியே பாதுகாக்கப்பட்டுள்ளது.
- இந்த commit புதிய working branch-ல் \`answers.md\` மட்டும் புதுப்பிக்கிறது.
- Pull Request / merge உருவாக்கப்படவில்லை.

**அடுத்த Chapter-க்கு செல்லும் முன்:** மேலே \`CONFLICT\`, \`REVIEW_REQUIRED\`, \`PARTIAL\` எனக் குறிக்கப்பட்ட ஐந்து வினாக்களுக்கான page-level QC-ஐ முடித்த பின் இதே format-ஐ அடுத்த இயலுக்குப் பயன்படுத்தலாம்.
