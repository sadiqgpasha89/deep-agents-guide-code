# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IX: Protocols
# Chapter 48: ACP: Agent Client Protocol
# Section: How
# Snippet 2 of this chapter.

import asyncio
from acp import run_agent
from deepagents import create_deep_agent
from deepagents_acp.server import AgentServerACP
from langgraph.checkpoint.memory import MemorySaver

async def main():
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",         # provider:model; examples show Google/OpenAI/Anthropic/OpenRouter/Fireworks/Baseten/Ollama
        system_prompt="You are a coding assistant.",
        # tools=[...], middleware=[...], subagents=[...] all customisable
        checkpointer=MemorySaver(),                   # examples pass a checkpointer
    )
    server = AgentServerACP(agent)
    await run_agent(server)                           # stdio mode: reads stdin, writes stdout

if __name__ == "__main__":
    asyncio.run(main())
