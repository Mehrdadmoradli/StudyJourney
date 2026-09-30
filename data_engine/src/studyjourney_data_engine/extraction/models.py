from pydantic import BaseModel

class Evidence(BaseModel):
    page: int
    text: str

class NumericRequirement(BaseModel):
    type: str
    operator: str
    value: float
    unit: str | None = None
    evidence: Evidence

class AdmissionExtraction(BaseModel):
    requirements: list[NumericRequirement]
