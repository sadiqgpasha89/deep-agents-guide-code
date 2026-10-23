# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 4: Quickstart: Your First Deep Agent
# Section: Creating and running the agent
# Snippet 4 of this chapter.

from deepagents import create_deep_agent

research_instructions = """You are an expert researcher. Conduct thorough research,
then write a polished report."""

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[anthropic_search],                 # or [internet_search]
    system_prompt=research_instructions,
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})
print(result["messages"][-1].content)
