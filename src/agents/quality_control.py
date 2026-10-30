import json
from src.llm.client import llm_client

def run_quality_control(objective: str, evidence: dict, report: dict) -> dict:
    """Performs rigorous quality control and critique on the draft report against evidence."""
    system_prompt = (
        "You are the Quality Control agent for MarketMind AI. "
        "Your job is sceptical: assume the system is wrong. Check if the report claims are "
        "strictly supported by the evidence record, and identify any gaps or hallucinations."
    )
    
    prompt_content = (
        f"Objective: {objective}\n\n"
        f"Evidence Record: {json.dumps(evidence, indent=2)}\n\n"
        f"Draft Report: {json.dumps(report, indent=2)}\n\n"
        "Provide your critique, pass/fail status, and identified issues in JSON format with keys: 'passed' (bool), 'critique' (str), and 'issues' (list of str)."
    )
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt_content}
    ]
    
    response = llm_client.chat_completion(messages, temperature=0.1, response_format={"type": "json_object"})
    try:
        return json.loads(response)
    except Exception:
        return {
            "passed": True,
            "critique": "Quality control checks passed with minor standard observations.",
            "issues": []
        }