# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 22: Tutorial: Extending the Research Assistant with Search, Memory and a Schedule
# Snippet 2 of this chapter.

from managed_deepagents import define_deep_agent
from tools.search import internet_search

agent = define_deep_agent(name="research-assistant", model="openai:gpt-5.5", tools=[internet_search])
