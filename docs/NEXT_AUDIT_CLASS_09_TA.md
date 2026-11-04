# அடுத்த பணி — Class 9 Official Catalog vs GitHub Audit

## தற்போதைய நிலை

- Class 1–8-க்கான audit summary, manifest CSV, official API snapshot ஆகியவை தனித்தனி GitHub audit branches-ல் ஏற்கெனவே உள்ளன.
- Class 2, 3, 4 அறிக்கைகளை மீண்டும் உருவாக்க வேண்டாம். அவை ஏற்கெனவே remote-ல் உள்ளன; HTTP 403 பற்றிய விளக்கங்களும் திருத்தப்பட்டுள்ளன.
- Eaglesiva/tn-class-09-க்கு SCERT audit branch தேடலில் கிடைக்கவில்லை. எனவே Class 9 அடுத்த audit target.
- Class 9 annual textbooks-க்கான 2026–27 விற்பனை அறிவிப்பு அதிகாரப்பூர்வ Textbook Corporation notice-ல் உள்ளது. CDN 403 வந்தால் “வெளியிடப்படவில்லை” என்று தானாக முடிவு செய்யக்கூடாது.

## Antigravity செய்ய வேண்டிய பணி

1. Eaglesiva/tn-class-09-ன் current main SHA மற்றும் முழு Git tree-ஐ பதிவு செய்.
2. Live official endpoint https://emis3.tnschools.gov.in/api/get_scert_books-ஐ மீண்டும் அழைத்து Class 9-க்கு பொருந்தும் raw API rows-ஐ exact source fields உடன் சேமி. API snapshot JSON, retrieval timestamp, SHA-256 ஆகியவற்றை evidence-ஆக வைத்துக்கொள்.
3. State Board Tamil/English annual academic books-ஐ மட்டும் in-scope எனத் தேர்வு செய். CBSE, minority-language readers, supplementary/teacher-resource books ஆகியவற்றை தனியாக out-of-scope என்று குறி.
4. ஒவ்வொரு official book-க்கும் exact API filename/URL, HTTP status, final URL, content type, content length, actual PDF page count, SHA-256, page-2 raw imprint text ஆகியவற்றைச் சேகரி. Academic year 2026–27 மற்றும் printed first/revised/reprint year-ஐத் தனித்தனியாகப் பதிவு செய்.
5. HTTP 403 வந்தால் அது CDN retrieval status மட்டுமே. Class 9 annual textbook sale 2026–27-க்கு அதிகாரப்பூர்வமாக அறிவிக்கப்பட்டுள்ளது. Exact URL, redirect, filename encoding, CDN access issue ஆகியவற்றை investigate செய்து evidence-ஐப் பதிவு செய்.
6. GitHub main-ல் ஏற்கெனவே உள்ள Class 9 folders, pages.json, individual page PDFs, local/current edition manifests ஆகியவற்றை inventory செய். Filename அல்லது page count மட்டுமே வைத்து match என்று சொல்லாதே.
7. Page-2 imprint, TOC, page count, normalized text/page order ஆகியவற்றை available source evidence உடன் ஒப்பிடு. முழுப் பக்க ஒப்பீடு செய்ய இயலாவிட்டால் NOT_CHECKED அல்லது MANUAL_REVIEW_REQUIRED என்று தெளிவாகக் குறி.
8. Class 9 audit branch உருவாக்கு: scert/class-09/audit-2026-27. அதில் மட்டும் கீழ்கண்ட evidence files-ஐ commit செய்:
   - class_09_official_api_snapshot.json
   - class_09_2026_27_audit_manifest.csv
   - class_09_audit_summary.md
   - ஒவ்வொரு official master-க்கும் download/evidence/comparison JSON report
9. Official master PDF-ஐ GitHub-ல் commit செய்யாதே. Temporary runner storage-ல் மட்டும் வைத்திரு. இப்போது புதிய edition-ஐ permanent-ஆக split/upload செய்யாதே; production main, viewer, index, active edition எதையும் மாற்றாதே.
10. இறுதியில் Class 9-ன் official availability, printed imprint, GitHub-ல் உள்ள edition/imprint, exact missing/older/mapping rows ஆகியவற்றை மூன்று பட்டியல்களாகத் தா. Class 9 verified rows-ஐ Class 10 central index CSV-யிலும் சேர்த்து scert/master-edition-tracking branch-ல் commit செய்.

## முடிவில் தர வேண்டிய மூன்று பட்டியல்கள்

1. Official listed + GitHub current/matching — content evidence உள்ளவற்றை மட்டும் சேர்க்கவும்.
2. Official listed + GitHub older/missing/mapping unresolved — ஒவ்வொரு புத்தகத்துக்கும் என்ன குறை என்று துல்லியமாகக் குறிப்பிடவும்.
3. Official record/release unresolved or retrieval blocked — API இல்லை, URL 403, PDF invalid, ambiguity போன்றவற்றைத் தனித்தனியாகப் பிரிக்கவும்.

## கட்டுப்பாடு

இது catalog-first audit. Permanent book ingestion/production deployment-க்கு முன் report-ஐப் பகிர்ந்து review பெறுக.
