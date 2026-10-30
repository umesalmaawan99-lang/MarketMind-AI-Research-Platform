from pydantic import ValidationError
from src.tools.registry import TOOL_REGISTRY

def dispatch_tool(tool_name: str, arguments: dict) -> str:
    """Dispatches a tool call after strict schema validation."""
    if tool_name not in TOOL_REGISTRY:
        return f"Error: Tool '{tool_name}' does not exist."

    tool_info = TOOL_REGISTRY[tool_name]
    schema = tool_info["schema"]
    func = tool_info["function"]

    try:
        # Strict validation boundary
        validated_args = schema(**arguments)
        # Execute tool with validated arguments (unpacking model dump)
        return func(**validated_args.model_dump())
    except ValidationError as e:
        return f"Security/Validation Error: Invalid arguments for tool '{tool_name}': {e}"
    except Exception as e:
        return f"Execution Error in tool '{tool_name}': {e}"