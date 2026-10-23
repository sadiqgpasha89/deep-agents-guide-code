# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 30: Interpreters (Beta): Code Inside the Agent
# Section: How to set it up (parameters)
# Snippet 1 of this chapter.

from langchain_quickjs import CodeInterpreterMiddleware
from langgraph.checkpoint.memory import MemorySaver

agent = create_deep_agent(
    model="openai:gpt-5.5",
    middleware=[CodeInterpreterMiddleware(ptc=["web_search"])],
    checkpointer=MemorySaver(),          # optional: durable threads, time travel
)
