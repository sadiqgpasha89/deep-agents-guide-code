# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 11: Managed Deep Agents: Defining the Agent
# Section: Per-run configuration with a graph factory
# Snippet 1 of this chapter.

# agent.py (sketch; field names follow the documentation)
from managed_deepagents import define_deep_agent

async def agent(runtime):
    ctx = runtime.execution_runtime.context if runtime.execution_runtime else None
    # ctx is None on channel runs, and execution_runtime is None when the
    # server loads the agent only to inspect its schema.
    return define_deep_agent(
        name="support-agent",           # must be an inline string literal
        model="openai:gpt-5.5",
        # instructions=..., skills=[...], mcp=[...], sandbox=...  (selectable resources)
    )
