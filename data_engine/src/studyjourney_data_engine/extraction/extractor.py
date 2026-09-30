from openai import OpenAI
from studyjourney_data_engine.parser.models import DocumentPage
from studyjourney_data_engine.extraction.prompt import SYSTEM_PROMPT
from studyjourney_data_engine.extraction.models import AdmissionExtraction


def information_extractor (relevant_pages: list[DocumentPage]) -> AdmissionExtraction:

    text = ""
    for page in relevant_pages:
        text += f"=== PAGE {page.page_number} ===\n"
        text += page.text
        text += "\n\n"


    client = OpenAI()

    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        text_format=AdmissionExtraction,
    )

    extraction = response.output_parsed

    if extraction is None:
        raise ValueError(
            "The LLM did not return a valid AdmissionExtraction."
        )

    return extraction
