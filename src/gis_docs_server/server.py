from mcp.server.mcpserver import  MCPServer

mcp =  MCPServer("gis-toolkit-hello")

@mcp.tool()
def hello(name: str) -> str:
    """A simple hello world tool."""
    return f"Hello, {name}! The MCP server is running and ready to process your requests."

@mcp.tool()
def search_docs(query: str) -> str:
    """A simple search tool for documentation."""
    # Placeholder for the real documentation search.
    return f"Searching for '{query}' in the documentation... (This is a placeholder response.)"

if __name__ == "__main__":
    mcp.run(transport="stdio")
    