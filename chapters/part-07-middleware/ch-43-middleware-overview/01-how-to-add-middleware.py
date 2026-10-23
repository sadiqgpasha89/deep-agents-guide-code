# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 43: Middleware: Overview
# Section: How to add middleware
# Snippet 1 of this chapter.

from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, HumanInTheLoopMiddleware

agent = create_agent(
    model="gpt-5.5",
    tools=[...],
    middleware=[SummarizationMiddleware(...), HumanInTheLoopMiddleware(...)],
)
# Deep Agents: the same objects go into create_deep_agent(middleware=[...])
