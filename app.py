import streamlit as st
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.state.research_state import ResearchState
from src.state.persistence import save_run_state
from src.agents.request_analyser import analyze_request
from src.agents.planner import generate_plan
from src.agents.researcher import execute_research_step
from src.agents.evidence_analyst import analyze_evidence
from src.agents.quality_control import run_quality_control
from src.agents.report_generator import generate_market_report

st.set_page_config(
    page_title="MarketMind AI - Autonomous Research Platform",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 MarketMind AI: Autonomous Business Research Platform")
st.markdown("Enterprise-grade multi-agent market research powered by OpenAI and structured validation.")

# Sidebar configuration
st.sidebar.header("Research Configuration")
sample_prompt = "Who is building tooling for AI model governance in 2026, and what capabilities do they offer?"
user_prompt = st.sidebar.text_area("Enter Research Topic / Prompt:", value=sample_prompt, height=100)

run_button = st.sidebar.button("🚀 Run Autonomous Research", type="primary")

if run_button:
    if not user_prompt.strip():
        st.warning("Please enter a valid research topic.")
    else:
        state = ResearchState(user_prompt=user_prompt)
        
        # Progress container
        progress_container = st.container()
        
        with progress_container:
            with st.spinner("🤖 [1/6] Analyzing request and distilling objective..."):
                state.objective = analyze_request(user_prompt)
            st.success(f"**Refined Objective:** {state.objective}")
            
            with st.spinner("🤖 [2/6] Generating strategic research plan..."):
                plan_data = generate_plan(state.objective)
                state.plan = plan_data.get("steps", [])
            
            st.markdown("### 📋 Generated Research Plan")
            for step in state.plan:
                st.info(f"**Step {step.get('step_id')}:** {step.get('query')} — *{step.get('rationale')}*")
                
            with st.spinner("🤖 [3/6] Executing research plan-act-observe loop..."):
                for step in state.plan:
                    state.current_step_index = step.get("step_id")
                    finding = execute_research_step(step)
                    state.raw_findings.append(finding)
            st.success("✅ Research execution completed.")
            
            with st.spinner("🤖 [4/6] Analyzing and validating evidence credibility..."):
                evidence_record = analyze_evidence(state.raw_findings)
                state.evidence = evidence_record.get("findings", [])
            
            with st.spinner("🤖 [5/6] Synthesizing final market report & running Quality Control..."):
                report_data = generate_market_report(state.objective, evidence_record)
                state.final_report = report_data
                qc_result = run_quality_control(state.objective, evidence_record, report_data)
                state.quality_checks.append(qc_result)
            
            # Save run state
            run_id = save_run_state(state)
            st.session_state["last_report"] = report_data
            st.session_state["last_qc"] = qc_result
            st.session_state["run_id"] = run_id
            st.success(f"🎉 Research completed successfully! Run saved as `{run_id}`.")

        # Display Report if available
        if "last_report" in st.session_state:
            st.markdown("---")
            st.header("📊 Final Market Research Report")
            report = st.session_state["last_report"]
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader("Executive Summary")
                st.write(report.get("executive_summary"))
            with col2:
                st.metric("Confidence Score", f"{report.get('confidence_score', 0)*100:.1f}%")
                qc = st.session_state.get("last_qc", {})
                st.metric("Quality Control", "Passed ✅" if qc.get("passed") else "Review Needed ⚠️")
                
            st.subheader("Key Findings")
            for finding in report.get("key_findings", []):
                st.markdown(f"- {finding}")
                
            st.subheader("Competitive Analysis")
            st.write(report.get("competitive_analysis"))
            
            st.subheader("Strategic Recommendations")
            for rec in report.get("recommendations", []):
                st.markdown(f"- **{rec.get('action')}**: {rec.get('impact')}")
                
            st.info(f"Audit Trail saved to `runs/{st.session_state.get('run_id')}.json`")