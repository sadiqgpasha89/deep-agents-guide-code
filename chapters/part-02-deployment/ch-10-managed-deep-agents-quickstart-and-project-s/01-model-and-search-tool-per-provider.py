# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 10: Managed Deep Agents: Quickstart and Project Structure
# Section: Model and search tool per provider
# Snippet 1 of this chapter.

# agent.py
from managed_deepagents import define_deep_agent

agent = define_deep_agent(
    name="research-assistant",          # graph ID and default deployment name
    model="openai:gpt-5.5",
    tools=[{"type": "web_search"}],     # provider built-in search; must match the model
)
