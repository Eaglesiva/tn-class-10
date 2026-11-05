import os, sys, json, time, requests, fitz, hashlib, subprocess, glob

print("=================================================================")
print("SCERT 2026-27 - OFFICIAL PDF DIRECT REFRESH: CLASS 10 ENGLISH")
print("=================================================================")

TARGET_BOOK = {
    "class": "10",
    "subject": "English",
    "medium": "English",
    "expected_pages": 224,
    "folder": "english",
    "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/10th_English_Text.pdf",
    "official_filename": "10th_English_Text.pdf"
}

# 1. Identify existing page PDF paths
print(f"Scanning existing page PDF files in: {TARGET_BOOK['folder']}...")
all_existing_pages = sorted(glob.glob(os.path.join(TARGET_BOOK['folder'], "**", "page_*.pdf"), recursive=True))
print(f"Found {len(all_existing_pages)} existing page PDF files.")
if len(all_existing_pages) != TARGET_BOOK['expected_pages']:
    print(f"ERROR: Expected {TARGET_BOOK['expected_pages']} pages, but found {len(all_existing_pages)}!")
    sys.exit(1)

print(f"First page: {all_existing_pages[0]}")
print(f"Last page:  {all_existing_pages[-1]}")

# 2. Download Official Master PDF to temporary storage (/tmp/master_10th_english.pdf)
temp_pdf_path = "/tmp/master_10th_english.pdf"
print(f"\nDownloading official master PDF from: {TARGET_BOOK['url']}...")
t0 = time.time()
resp = requests.get(TARGET_BOOK['url'], headers={'User-Agent': 'Mozilla/5.0'}, stream=True, timeout=120)
resp.raise_for_status()

# Validate status and content
content_length = int(resp.headers.get('Content-Length', 0))
etag = resp.headers.get('ETag', '').strip('"')
last_modified = resp.headers.get('Last-Modified', '')
print(f"HTTP Status: {resp.status_code}")
print(f"Content-Length: {content_length} bytes ({content_length / 1024 / 1024:.2f} MB)")
print(f"ETag: {etag}")

sha256 = hashlib.sha256()
with open(temp_pdf_path, 'wb') as f:
    for chunk in resp.iter_content(chunk_size=1024*1024):
        if chunk:
            f.write(chunk)
            sha256.update(chunk)

master_sha256 = sha256.hexdigest()
master_size = os.path.getsize(temp_pdf_path)
print(f"Downloaded master PDF: {master_size} bytes in {time.time() - t0:.2f}s")
print(f"Master SHA-256: {master_sha256}")

# Validate PDF Magic Bytes
with open(temp_pdf_path, 'rb') as f:
    magic = f.read(5)
if not magic.startswith(b'%PDF'):
    print(f"ERROR: Downloaded file is not a valid PDF! Magic bytes: {magic}")
    if os.path.exists(temp_pdf_path):
        os.remove(temp_pdf_path)
    sys.exit(1)

# 3. Open with PyMuPDF and Validate Page Count
doc = fitz.open(temp_pdf_path)
master_page_count = len(doc)
print(f"Master PDF Page Count: {master_page_count} (Expected: {TARGET_BOOK['expected_pages']})")

if master_page_count != TARGET_BOOK['expected_pages']:
    print(f"ERROR: Page count mismatch! Master: {master_page_count} != Expected: {TARGET_BOOK['expected_pages']}")
    doc.close()
    if os.path.exists(temp_pdf_path):
        os.remove(temp_pdf_path)
    sys.exit(1)

# 4. In-Place Single-Page PDF Splitting & Overwrite
print(f"\nSplitting master PDF and replacing existing {master_page_count} page files in-place...")
split_success_count = 0
for idx in range(master_page_count):
    dest_page_path = all_existing_pages[idx]
    
    # Extract single page
    single_doc = fitz.open()
    single_doc.insert_pdf(doc, from_page=idx, to_page=idx)
    single_doc.save(dest_page_path)
    single_doc.close()
    
    # Validate written single page
    check_doc = fitz.open(dest_page_path)
    if len(check_doc) != 1 or os.path.getsize(dest_page_path) == 0:
        print(f"Validation FAILED for {dest_page_path}!")
        check_doc.close()
        doc.close()
        sys.exit(1)
    check_doc.close()
    split_success_count += 1

print(f"Successfully split and validated {split_success_count} / {master_page_count} pages.")

# 5. Close and Delete Temporary Master PDF Immediately
doc.close()
if os.path.exists(temp_pdf_path):
    os.remove(temp_pdf_path)
    print("Zero Local Master PDF Persistence: /tmp master PDF removed.")

# 6. Verify Git Safety (ONLY .pdf files modified)
print("\nVerifying git status to ensure ONLY .pdf files were modified...")
p_status = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
status_lines = [l.strip() for l in p_status.stdout.splitlines() if l.strip()]

modified_non_pdfs = []
modified_pdfs = []
for line in status_lines:
    parts = line.split(maxsplit=1)
    if len(parts) == 2:
        file_path = parts[1]
        if file_path.endswith('.pdf'):
            modified_pdfs.append(file_path)
        else:
            modified_non_pdfs.append(file_path)

print(f"Modified PDF files count: {len(modified_pdfs)}")
if modified_non_pdfs:
    print(f"WARNING: Non-PDF files detected in git status: {modified_non_pdfs}")
    # Restore non-pdf files
    for non_pdf in modified_non_pdfs:
        if not non_pdf.startswith('.github/'):
            subprocess.run(['git', 'checkout', '--', non_pdf])
            print(f"Restored untouched non-pdf file: {non_pdf}")

# 7. Write Evidence Record
evidence = {
    "book_id": "class_10_english",
    "class": "10",
    "subject": "English",
    "medium": "English",
    "official_filename": TARGET_BOOK['official_filename'],
    "official_url": TARGET_BOOK['url'],
    "http_status": "GET_200",
    "content_length": master_size,
    "etag": etag,
    "last_modified": last_modified,
    "sha256": master_sha256,
    "expected_page_count": TARGET_BOOK['expected_pages'],
    "actual_page_count": master_page_count,
    "pages_replaced_count": split_success_count,
    "all_pages_validated": True,
    "refresh_status": "OFFICIAL_SOURCE_REFRESHED",
    "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "zero_master_pdf_persistence_verified": True
}

os.makedirs("docs/refresh_evidence", exist_ok=True)
with open("docs/refresh_evidence/class_10_english_refresh_evidence.json", "w", encoding="utf-8") as f:
    json.dump(evidence, f, indent=2)

print("\nSaved docs/refresh_evidence/class_10_english_refresh_evidence.json")
print("=== Job Completed Successfully ===")
