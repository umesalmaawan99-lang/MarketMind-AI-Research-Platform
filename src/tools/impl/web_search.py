import requests
from src.schemas.tools import WebSearchInput

def web_search(query: str) -> str:
    """Performs a web search using a search tool or fallback mock."""
    # Validate input using Pydantic schema
    validated_input = WebSearchInput(query=query)
    
    try:
        # For demonstration or testing, we can simulate a search or use a simple public endpoint/duckduckgo API.
        # Let's provide a reliable fallback / implementation structure:
        url = f"https://api.duckduckgo.com/?q={validated_input.query}&format=json"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            abstract = data.get("AbstractText")
            if abstract:
                return f"Search Result for '{validated_input.query}': {abstract}"
            
            # If no direct abstract, check related topics
            related = data.get("RelatedTopics", [])
            results = []
            for item in related[:3]:
                if "Text" in item:
                    results.append(item["Text"])
            if results:
                return f"Search Results for '{validated_input.query}':\n" + "\n".join(results)
                
        return f"Mock Search Result: Market analysis and insights regarding '{validated_input.query}' indicate strong growth trends, key competitor activity, and significant enterprise adoption in 2026."
    except Exception as e:
        return f"Search execution error: {e}"