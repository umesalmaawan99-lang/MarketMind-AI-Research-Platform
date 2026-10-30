import json
import os
from datetime import datetime
from src.state.research_state import ResearchState

RUNS_DIR = "runs"

def save_run_state(state: ResearchState, run_id: Optional[str] = None) -> str:
    """Saves the current research state to a JSON file in the runs/ directory."""
    if not os.path.exists(RUNS_DIR):
        os.makedirs(RUNS_DIR)

    if not run_id:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        run_id = f"run_{timestamp}"

    file_path = os.path.join(RUNS_DIR, f"{run_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(state.to_dict(), f, indent=4)

    return run_id