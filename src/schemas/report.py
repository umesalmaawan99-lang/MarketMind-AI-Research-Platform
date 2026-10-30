from pydantic import BaseModel, Field
from typing import List

class Recommendation(BaseModel):
    action: str = Field(..., description="Actionable recommendation for business stakeholders.")
    impact: str = Field(..., description="Expected impact or rationale.")

class MarketReport(BaseModel):
    executive_summary: str = Field(..., description="Concise executive summary of the research findings.")
    key_findings: List[str] = Field(..., description="Bulleted list of key data-backed findings.")
    competitive_analysis: str = Field(..., description="Analysis of competitors or market players.")
    recommendations: List[Recommendation] = Field(..., description="Strategic recommendations.")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Overall confidence score of the report.")