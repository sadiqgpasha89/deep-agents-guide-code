# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 25: Tools: The Built-in Toolbox
# Section: MCP tools
# Snippet 2 of this chapter.

import asyncio
from langchain.mcp import MCPAdapter

config = {"mcpServers": {"my_server": {"url": "http://localhost:8000/mcp"}}}

async def main():
    async with MCPAdapter(config) as adapter:
        tools = await adapter.list_tools()
        agent = create_deep_agent(model="openai:gpt-5.5", tools=tools)
        return await agent.ainvoke({"messages": [{"role": "user", "content": "..."}]})

asyncio.run(main())            # the docs' example defines main() but doesn't call it
