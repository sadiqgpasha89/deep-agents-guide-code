# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IX: Protocols
# Chapter 49: MCP with LangChain
# Section: Connections: lifecycle, multiple servers, scaling
# Snippet 5 of this chapter.

CONFIG = {"mcpServers": {
    "weather": {"command": "python", "args": ["/path/to/weather_server.py"]},
    "calc":    {"command": "python", "args": ["/path/to/calc_server.py"]},
}}
async with MCPAdapter(CONFIG) as adapter:
    tools = await adapter.list_tools()
