from pathlib import Path

import pymupdf

from .models import DocumentPage


def extract_pages(pdf_path: Path) -> list[DocumentPage]:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    pages: list[DocumentPage] = []

    with pymupdf.open(pdf_path) as document:
        for index, page in enumerate(document):
            text = page.get_text(
                "text",
                sort=True,
            ).strip()

            pages.append(
                DocumentPage(
                    page_number=index + 1,
                    text=text,
                )
            )

    return pages
