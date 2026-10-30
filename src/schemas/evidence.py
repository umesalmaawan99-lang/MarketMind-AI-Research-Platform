from pydantic import BaseModel, Field
from typing import List, Optional

class EvidenceItem(BaseModel):
    claim: str = Field(..., description="The specific factual claim extracted from the source.")
    source_url: str = Field(..., description="URL or provenance of the source.")
    credibility_score: float = Field(..., ge=0.0, le=1.0, description="Credibility score between 0.0 and 1.0.")
    supported: bool = Field(..., description="Whether the source genuinely supports the claim.")
    reasoning: str = Field(..., description="Justification for the credibility and support assessment.")

class EvidenceRecord(BaseModel):
    findings: List[EvidenceItem] = Field(..., description="List of validated evidence items.")