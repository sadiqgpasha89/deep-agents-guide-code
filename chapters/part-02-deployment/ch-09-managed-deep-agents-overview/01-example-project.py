# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 9: Managed Deep Agents: Overview
# Section: Example project
# Snippet 1 of this chapter.

# agent.py
from managed_deepagents import define_deep_agent

from middleware.audit import log_tool_calls
from tools.search import internet_search

agent = define_deep_agent(
    name="research-assistant",          # static name is REQUIRED
    model="openai:gpt-5.5",
    tools=[internet_search],
    middleware=[log_tool_calls],
)
