from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool(name="get_weather", description="Get the current weather for a given city.")
async def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    # Placeholder implementation
    return f"The current weather in {city} is sunny." 

if __name__ == "__main__":
    mcp.run(transport="streamable-http")