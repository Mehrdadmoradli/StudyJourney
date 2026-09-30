from pathlib import Path

from studyjourney_data_engine.parser.pdf_parser import extract_pages
from studyjourney_data_engine.relevance_detector.relevance_detector import find_relevant_pages
from studyjourney_data_engine.extraction.extractor import information_extractor


file = Path("tests/results/pdf_downloader_result2.pdf")
destination = Path("tests/results/information_extractor_result.txt")

pages = extract_pages(file)

relevant_pages = find_relevant_pages(pages)

results = information_extractor(relevant_pages)


destination.parent.mkdir(
        parents=True,
        exist_ok=True,
)

destination.write_text(
    results.model_dump_json(indent=2),
    encoding="utf-8"
)
