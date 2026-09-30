from studyjourney_data_engine.parser.models import DocumentPage

KEYWORDS = {
    # German
    "zugangsvoraussetzungen": 5,
    "zulassungsvoraussetzungen": 5,
    "zugangsordnung": 5,
    "zulassungsordnung": 5,

    "bachelorabschluss": 3,
    "erster berufsqualifizierender abschluss": 4,

    "leistungspunkte": 2,
    "ects": 2,

    "sprachkenntnisse": 3,
    "englischkenntnisse": 3,
    "deutschkenntnisse": 3,

    "auswahlverfahren": 4,
    "eignungsverfahren": 4,

    "bewerbung": 1,
    "bewerbungsfrist": 3,

    "mindestnote": 4,
    "gesamtnote": 2,

    "berufserfahrung": 3,

    "mathematik": 2,
    "informatik": 2,
    "theoretische informatik": 3,

    # English
    "admission requirements": 5,
    "entry requirements": 5,
    "entrance requirements": 5,
    "eligibility requirements": 5,
    "admission regulations": 5,

    "admission criteria": 4,
    "eligibility criteria": 4,

    "bachelor's degree": 3,
    "bachelor degree": 3,
    "undergraduate degree": 3,
    "previous degree": 2,

    "credit points": 2,

    "language requirements": 3,
    "english proficiency": 3,
    "english language requirements": 4,
    "german proficiency": 3,
    "german language requirements": 4,

    "selection procedure": 4,
    "aptitude assessment": 4,

    "application requirements": 4,
    "application process": 2,
    "application deadline": 3,
    "application period": 2,

    "minimum grade": 4,
    "grade point average": 3,
    "gpa": 3,

    "toefl": 3,
    "ielts": 3,
    "gre": 3,
    "gate": 3,

    "work experience": 3,
    "professional experience": 3,

    "mathematics": 2,
    "computer science": 2,
    "theoretical computer science": 3,
}


def find_relevant_pages (pages: list[DocumentPage]) -> list[DocumentPage]:

    relevant_pages = []
    MINIMUM_RELEVANCE_SCORE = 5

    for page in pages:
        text = page.text.lower()
        score = 0;
        for keyword, weight in KEYWORDS.items():
            if keyword in text:
                score += weight
        if score >= MINIMUM_RELEVANCE_SCORE:
            relevant_pages.append(page)


    return relevant_pages
