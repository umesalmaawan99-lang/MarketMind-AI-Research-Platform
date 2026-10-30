import json
from src.llm.client import llm_client

def analyze_request(user_prompt: str) -> str:
    """Analyzes the user request and distills it into a clear research objective."""
    system_prompt = (
        "You are the Request Analyser agent for MarketMind AI. "
        "Your job is to take a raw user request about a market or business topic and "
        "distill it into a precise, actionable research objective."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"User Request: {user_prompt}\n\nProvide a clear, refined research objective:"}
    ]
    response = llm_client.chat_completion(messages, temperature=0.2)
    return response.strip()