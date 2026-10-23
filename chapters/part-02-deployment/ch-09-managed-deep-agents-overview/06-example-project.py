# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 9: Managed Deep Agents: Overview
# Section: Example project
# Snippet 6 of this chapter.

# tools/mcp.py : remote MCP servers as tools
from managed_deepagents import define_mcp

mcp = define_mcp(
    servers={
        "langchainDocs": {
            "transport": "http",
            "url": "https://docs.langchain.com/mcp",
            "include_tools": ["search_docs_by_lang_chain"],
        },
    },
)
