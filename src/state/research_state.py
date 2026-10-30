from typing import List, Dict, Any, Optional

class ResearchState:
    def __init__(self, user_prompt: str):
        self.user_prompt: str = user_prompt
        self.objective: str = ""
        self.plan: List[Dict[str, Any]] = []
        self.current_step_index: int = 0
        self.evidence: List[Dict[str, Any]] = []
        self.raw_findings: List[str] = []
        self.quality_checks: List[Dict[str, Any]] = []
        self.human_approved: bool = False
        self.final_report: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_prompt": self.user_prompt,
            "objective": self.objective,
            "plan": self.plan,
            "current_step_index": self.current_step_index,
            "evidence": self.evidence,
            "raw_findings": self.raw_findings,
            "quality_checks": self.quality_checks,
            "human_approved": self.human_approved,
            "final_report": self.final_report
        }