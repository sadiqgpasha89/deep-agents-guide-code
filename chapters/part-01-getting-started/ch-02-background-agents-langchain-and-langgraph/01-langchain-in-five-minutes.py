# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 2: Background: Agents, LangChain and LangGraph
# Section: LangChain in five minutes
# Snippet 1 of this chapter.

from langchain.agents import create_agent
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """Return the current weather for a city."""
    return f"It is sunny in {city}."

agent = create_agent("anthropic:claude-sonnet-4-6", tools=[get_weather])
result = agent.invoke({"messages": [{"role": "user", "content": "Weather in Pune?"}]})
print(result["messages"][-1].content)
