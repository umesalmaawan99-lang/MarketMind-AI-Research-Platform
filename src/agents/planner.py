import json
from src.llm.client import llm_client
from src.schemas.plan import ResearchPlan

def generate_plan(objective: str) -> dict:
    """Generates a structured research plan based on the objective using OpenAI structured outputs."""
    system_prompt = (
        "You are the Strategic Planner agent for MarketMind AI. "
        "Create a structured research plan consisting of 3 to 5 sequential steps to thoroughly investigate the objective."
    )
    
    # We use OpenAI structured outputs via Pydantic model representation
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Research Objective: {objective}"}
    ]
    
    try:
        completion = llm_client.client.beta.chat.completions.parse(
            model=llm_client.model,
            messages=messages,
            response_format=ResearchPlan,
            temperature=0.2,
        )
        plan_obj = completion.choices.message.parsed
        return plan_obj.model_dump()
    except Exception as e:
        # Fallback dictionary if structured parse fails
        return {
            "objective": objective,
            "steps": [
                {"step_id": 1, "query": objective, "rationale": "General market overview and key insights."}
            ]
        }