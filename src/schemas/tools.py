from pydantic import BaseModel, Field

class WebSearchInput(BaseModel):
    query: str = Field(..., description="The search query to look up on the web.")