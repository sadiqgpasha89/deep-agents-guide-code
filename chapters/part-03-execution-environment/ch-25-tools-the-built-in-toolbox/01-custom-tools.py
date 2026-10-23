# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 25: Tools: The Built-in Toolbox
# Section: Custom tools
# Snippet 1 of this chapter.

from typing import Literal

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
) -> str:
    """Run a web search and return results as text."""    # docstring + hints => schema
    ...

agent = create_deep_agent(model="anthropic:claude-sonnet-4-6", tools=[internet_search])
