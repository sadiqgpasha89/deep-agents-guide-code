# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 5: Customization: Configuring a Deep Agent
# Section: Tools
# Snippet 3 of this chapter.

from langchain.mcp import MCPAdapter           # pip install "langchain[mcp]"

config = {"mcpServers": {"my_server": {"url": "http://localhost:8000/mcp"}}}
async with MCPAdapter(config) as adapter:
    tools = await adapter.list_tools()
    agent = create_deep_agent(model="openai:gpt-5.5", tools=tools)
