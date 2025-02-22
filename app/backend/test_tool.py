from rtmt import RTMiddleTier, Tool, ToolResult, ToolResultDirection
from typing import Any

_temperature_tool_schema = {
    "type": "function",
    "name": "get_temperature",
    "description": "Returns the temperature of a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "city name to get temperature"
            }
        },
        "required": ["city"],
        "additionalProperties": False
    }
}

async def _get_temperature_tool(args: Any) -> ToolResult:
    print(f"Getting temperature for '{args['city']}'")
    return ToolResult(
        destination=ToolResultDirection.TO_SERVER,
        text=f"The temperature of {args['city']} is 30C"
    )

def attach_temperature_tool(rtmt: RTMiddleTier) -> None:
    print("Attaching temperature tool")
    rtmt.tools["get_temperature"] = Tool(
        schema=_temperature_tool_schema,
        target=lambda args: _get_temperature_tool(args)
    )