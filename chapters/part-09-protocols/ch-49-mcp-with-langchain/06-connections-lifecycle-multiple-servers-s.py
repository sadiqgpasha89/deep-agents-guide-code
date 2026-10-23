# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IX: Protocols
# Chapter 49: MCP with LangChain
# Section: Connections: lifecycle, multiple servers, scaling
# Snippet 6 of this chapter.

from langchain.mcp import MCPAdapter, ClientGroup
from fastmcp import Client

group = ClientGroup({"weather": Client(legacy_url, mode="legacy"), "calc": Client(modern_url, mode="auto")})
async with MCPAdapter(group) as adapter:
    tools = await adapter.list_tools()
