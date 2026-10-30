from src.tools.dispatcher import dispatch_tool

def execute_research_step(step: dict) -> str:
    """Executes a research step by calling the web search tool."""
    query = step.get("query")
    if not query:
        return "Error: No search query provided for this step."
    
    print(f"🔍 Executing search query: '{query}'")
    result = dispatch_tool("web_search", {"query": query})
    return result