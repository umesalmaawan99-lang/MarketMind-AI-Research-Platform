import sys
import os

# Ensure the parent directory is in sys.path so imports work smoothly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.state.research_state import ResearchState
from src.state.persistence import save_run_state
from src.agents.request_analyser import analyze_request
from src.agents.planner import generate_plan
from src.agents.researcher import execute_research_step
from src.agents.evidence_analyst import analyze_evidence
from src.agents.quality_control import run_quality_control
from src.agents.report_generator import generate_market_report
from src.approval.cli_gate import request_human_approval

def run_marketmind(user_prompt: str):
    print(f"\n🚀 Initializing MarketMind AI for prompt: '{user_prompt}'\n" + "-"*50)
    
    # Initialize state
    state = ResearchState(user_prompt=user_prompt)
    
    # Step 1: Request Analysis
    print("🤖 [1/7] Analyzing user request...")
    state.objective = analyze_request(user_prompt)
    print(f"🎯 Refined Objective: {state.objective}")
    
    # Step 2: Strategic Planning
    print("\n🤖 [2/7] Generating research plan...")
    plan_data = generate_plan(state.objective)
    state.plan = plan_data.get("steps", [])
    print(f"📋 Plan generated with {len(state.plan)} steps.")
    for step in state.plan:
        print(f"   - Step {step.get('step_id')}: {step.get('query')} ({step.get('rationale')})")
        
    # Step 3: Research Execution (Plan-Act-Observe Loop)
    print("\n🤖 [3/7] Executing research steps...")
    for step in state.plan:
        state.current_step_index = step.get("step_id")
        finding = execute_research_step(step)
        state.raw_findings.append(finding)
        
    # Step 4: Evidence Analysis
    print("\n🤖 [4/7] Analyzing and validating evidence...")
    evidence_record = analyze_evidence(state.raw_findings)
    state.evidence = evidence_record.get("findings", [])
    print(f"✅ Validated {len(state.evidence)} evidence items.")
    
    # Step 5: Report Synthesis
    print("\n🤖 [5/7] Synthesizing final market report...")
    report_data = generate_market_report(state.objective, evidence_record)
    state.final_report = report_data
    
    # Step 6: Automated Quality Control
    print("\n🤖 [6/7] Running Quality Control scrutiny...")
    qc_result = run_quality_control(state.objective, evidence_record, report_data)
    state.quality_checks.append(qc_result)
    print(f"🔍 QC Status - Passed: {qc_result.get('passed')}")
    print(f"   Critique: {qc_result.get('critique')}")
    
    # Step 7: Human Approval Gate & Persistence
    print("\n🤖 [7/7] Requesting human approval...")
    approved = request_human_approval(report_data)
    state.human_approved = approved
    
    # Save run state audit trail
    run_id = save_run_state(state)
    print(f"\n📁 Run state successfully saved to runs/{run_id}.json")
    
    if approved:
        print("\n🎉 MarketMind AI run completed successfully! Report published.")
    else:
        print("\n⚠️ Run completed, but report was rejected by reviewer.")

if __name__ == "__main__":
    # Default test prompt or accept CLI argument
    sample_prompt = "Who is building tooling for AI model governance in 2026, and what capabilities do they offer?"
    if len(sys.argv) > 1:
        sample_prompt = " ".join(sys.argv[1:])
    
    run_marketmind(sample_prompt)   