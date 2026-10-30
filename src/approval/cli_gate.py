def request_human_approval(report_data: dict) -> bool:
    """Presents the report summary to the human reviewer and requests approval."""
    print("\n" + "="*50)
    print(" 🛑 HUMAN APPROVAL GATE - REPORT REVIEW REQUIRED 🛑 ")
    print("="*50)
    print(f"\nExecutive Summary:\n{report_data.get('executive_summary', 'N/A')}")
    print(f"\nConfidence Score: {report_data.get('confidence_score', 'N/A')}")
    print("\nKey Findings:")
    for finding in report_data.get('key_findings', []):
        print(f" - {finding}")
    print("\n" + "="*50)
    
    while True:
        choice = input("Do you approve this report for final publication? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            print("✅ Report approved by human reviewer.")
            return True
        elif choice in ['n', 'no']:
            print("❌ Report rejected by human reviewer.")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")