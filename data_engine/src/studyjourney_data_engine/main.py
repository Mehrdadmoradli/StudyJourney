import argparse
from pathlib import Path

from studyjourney_data_engine.parser.pdf_parser import extract_pages


def main() -> None:
    parser = argparse.ArgumentParser(
        description="StudyJourney Data Engine"
    )

    parser.add_argument(
        "pdf",
        type=Path,
        help="Path to a PDF document",
    )

    args = parser.parse_args()

    pages = extract_pages(args.pdf)

    for page in pages:
        print()
        print(f"===== PAGE {page.page_number} =====")
        print(page.text)


if __name__ == "__main__":
    main()
