from pathlib import Path

import pytest

from studyjourney_data_engine.downloader.pdf_downloader import download_pdf
from studyjourney_data_engine.parser.pdf_parser import extract_pages

url = "https://www.fh-dortmund.de/medien/po/fb4/infBA_ab_2013/StgPO_BA_Informatik_2026_final.pdf"
destination = Path(f"tests/results/pdf_downloader_result.pdf")
pdf_path = download_pdf(url, destination)

pages = extract_pages(pdf_path)

for page in pages:
    print(f"PAGE {page.page_number}")
    print(page.text)
