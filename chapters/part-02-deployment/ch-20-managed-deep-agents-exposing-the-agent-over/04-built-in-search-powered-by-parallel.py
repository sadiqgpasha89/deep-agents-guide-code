# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 20: Managed Deep Agents: Exposing the Agent over MCP, and Built-in Search
# Section: Built-in search powered by Parallel
# Snippet 4 of this chapter.

from managed_deepagents import define_mcp

mcp = define_mcp(
    servers={
        "Parallel": {
            "transport": "http",
            "url": "https://api.smith.langchain.com/v1/managed-tools/servers/parallel/mcp",
        },
    },
)
