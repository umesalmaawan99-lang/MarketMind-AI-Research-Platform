from pydantic import BaseModel, Field
from typing import List

class ResearchStep(BaseModel):
    step_id: int = Field(..., description="Sequential ID of the research step.")
    query: str = Field(..., description="Specific search query or research question to investigate.")
    rationale: str = Field(..., description="Why this step is necessary to answer the core business problem.")

class ResearchPlan(BaseModel):
    objective: str = Field(..., description="The refined objective of the research task.")
    steps: List[ResearchStep] = Field(..., description="List of sequential research steps to execute.")