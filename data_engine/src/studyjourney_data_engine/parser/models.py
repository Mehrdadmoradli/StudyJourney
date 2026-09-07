from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentPage:
    page_number: int
    text: str
