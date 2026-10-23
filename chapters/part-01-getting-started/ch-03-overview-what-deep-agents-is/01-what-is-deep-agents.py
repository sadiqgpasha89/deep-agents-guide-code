# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 3: Overview: What Deep Agents Is
# Section: What is Deep Agents?
# Snippet 1 of this chapter.

from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",   # "provider:model" string, or a chat model object
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)
agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
