from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math")


@mcp.tool(name="add", description="Add two numbers together.")
def add(x:int, y:int) -> int:
    """Add two numbers together.""" 
    return x + y


@mcp.tool(name="multiply", description="Multiply two numbers together.")
def multiply(x:int, y:int) -> int:
    """Multiply two numbers together."""
    return x * y


if __name__ == "__main__":
    mcp.run(transport="stdio")