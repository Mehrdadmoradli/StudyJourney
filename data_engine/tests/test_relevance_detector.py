from pathlib import Path

from studyjourney_data_engine.parser.pdf_parser import extract_pages
from studyjourney_data_engine.relevance_detector.relevance_detector import find_relevant_pages

file = Path(f"tests/results/pdf_downloader_result2.pdf")

extracted_pages = extract_pages(file)

relevant_pages = find_relevant_pages(extracted_pages)

for page in relevant_pages:
    for line in page.text.splitlines():
        print(line)
