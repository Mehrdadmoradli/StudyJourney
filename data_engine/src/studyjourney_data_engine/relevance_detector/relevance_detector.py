from studyjourney_data_engine.parser.models import DocumentPage

KEYWORDS = [
    # German
    "zugangsvoraussetzungen",
    "zulassungsvoraussetzungen",
    "zugangsordnung",
    "zulassungsordnung",
    "bachelorabschluss",
    "erster berufsqualifizierender abschluss",
    "leistungspunkte",
    "ects",
    "sprachkenntnisse",
    "englischkenntnisse",
    "deutschkenntnisse",
    "auswahlverfahren",
    "eignungsverfahren",
    "bewerbung",
    "bewerbungsfrist",
    "mindestnote",
    "gesamtnote",
    "berufserfahrung",
    "mathematik",
    "informatik",
    "theoretische informatik",

    # English
    "admission requirements",
    "entry requirements",
    "entrance requirements",
    "eligibility requirements",
    "admission regulations",
    "admission criteria",
    "eligibility criteria",
    "bachelor's degree",
    "bachelor degree",
    "undergraduate degree",
    "previous degree",
    "credit points",
    "language requirements",
    "english proficiency",
    "english language requirements",
    "german proficiency",
    "german language requirements",
    "selection procedure",
    "aptitude assessment",
    "application requirements",
    "application process",
    "application deadline",
    "application period",
    "minimum grade",
    "grade point average",
    "gpa",
    "toefl",
    "ielts",
    "gre",
    "gate",
    "work experience",
    "professional experience",
    "mathematics",
    "computer science",
    "theoretical computer science",
]

def find_relevant_pages (pages: list[DocumentPage]) -> list[DocumentPage]:

    relevant_pages = []

    for page in pages:
        text = page.text.lower()
        for keyword in KEYWORDS:
            if keyword in text:
                relevant_pages.append(page)
                break

    return relevant_pages
