# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 2: Background: Agents, LangChain and LangGraph
# Section: LangGraph in five ideas
# Snippet 2 of this chapter.

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command, interrupt

# 1. A checkpointer makes the thread resumable.
agent = create_agent("anthropic:claude-sonnet-4-6", tools=[get_weather], checkpointer=InMemorySaver())
cfg = {"configurable": {"thread_id": "demo-1"}}
agent.invoke({"messages": [{"role": "user", "content": "Hi, I'm Sadiq"}]}, cfg)
agent.invoke({"messages": [{"role": "user", "content": "What is my name?"}]}, cfg)   # remembers

# 2. A tool can pause for a human, then resume with a value.
@tool
def transfer(amount: float) -> str:
    """Transfer money."""
    ok = interrupt({"question": f"Approve transferring {amount}?"})
    return "sent" if ok else "cancelled"
# agent.invoke(Command(resume=True), cfg)   # continues from the checkpoint
