# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 36: Context Engineering: Offloading, Summarization and Isolation
# Section: Runtime context (per run)
# Snippet 1 of this chapter.

from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime

@dataclass
class Context:
    user_id: str

@tool
def whoami(runtime: ToolRuntime[Context]) -> str:
    """Return the current user id."""
    return runtime.context.user_id

agent = create_deep_agent(model=..., tools=[whoami], context_schema=Context)
agent.invoke({"messages": [...]}, context=Context(user_id="u1"))
