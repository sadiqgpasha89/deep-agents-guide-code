# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part V: Delegation
# Chapter 40: Async Subagents: Background Work
# Section: Configuration
# Snippet 1 of this chapter.

from deepagents import AsyncSubAgent, create_deep_agent

async_subagents = [
    AsyncSubAgent(
        name="researcher",
        description="Researches a topic in depth; use for long-running research",   # drives routing: be specific
        graph_id="researcher",       # graph/assistant ID on the server
        # url omitted -> ASGI transport (co-deployed in the same langgraph.json, RECOMMENDED)
    ),
    AsyncSubAgent(
        name="coder", description="Writes and tests code", graph_id="coder",
        url="https://coder.example.com",          # set -> HTTP transport (remote, independent scaling)
        headers={"Authorization": "Bearer ..."},  # custom auth for remote
        mode="isolated",                           # "fork" is Python-only, experimental
    ),
]
agent = create_deep_agent(model="anthropic:claude-sonnet-4-6", subagents=async_subagents)
