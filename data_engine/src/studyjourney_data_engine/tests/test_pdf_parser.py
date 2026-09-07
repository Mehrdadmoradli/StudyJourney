from pathlib import Path

import pytest

from studyjourney_data_engine.parser.pdf_parser import extract_pages


def test_missing_pdf_raises_error():
    path = Path("does-not-exist.pdf")

    with pytest.raises(FileNotFoundError):
        extract_pages(path)
