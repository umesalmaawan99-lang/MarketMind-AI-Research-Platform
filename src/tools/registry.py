from typing import Callable, Dict, Any
from src.tools.impl.web_search import web_search
from src.schemas.tools import WebSearchInput

TOOL_REGISTRY: Dict[str, Dict[str, Any]] = {
    "web_search": {
        "function": web_search,
        "schema": WebSearchInput,
        "description": "Search the web for up-to-date market information, competitor data, and facts."
    }
}

def get_tool(name: str) -> Callable:
    if name not in TOOL_REGISTRY:
        raise ValueError(f"Tool '{name}' is not registered.")
    return TOOL_REGISTRY[name]["function"]