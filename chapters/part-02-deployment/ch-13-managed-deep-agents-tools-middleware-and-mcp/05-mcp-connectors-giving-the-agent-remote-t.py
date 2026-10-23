# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 13: Managed Deep Agents: Tools, Middleware and MCP Connectors
# Section: MCP connectors: giving the agent remote tools
# Snippet 5 of this chapter.

# tools/mcp.py
from managed_deepagents import define_mcp

mcp = define_mcp(
    servers={
        "langchainDocs": {
            "transport": "http",          # Streamable HTTP; "sse" is the legacy option
            "url": "https://docs.langchain.com/mcp",
        },
    },
)
