# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part V: Delegation
# Chapter 38: Subagents: Delegating to Specialists
# Section: CompiledSubAgent (bring your own graph)
# Snippet 2 of this chapter.

from langchain.agents import create_agent
from deepagents import CompiledSubAgent

custom = CompiledSubAgent(
    name="data-analyzer",
    description="Specialized agent for data analysis",
    runnable=create_agent(model="anthropic:claude-sonnet-4-6", tools=[run_sql], system_prompt="..."),
    mode="isolated",                    # or "fork"
)
agent = create_deep_agent(model=..., subagents=[custom])
