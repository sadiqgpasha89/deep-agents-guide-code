# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VI: Steering
# Chapter 41: Human-in-the-Loop: Approvals and Interrupts
# Section: How to configure `interrupt_on`
# Snippet 1 of this chapter.

from langgraph.checkpoint.memory import MemorySaver
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[remove_file, fetch_file, notify_email],
    interrupt_on={
        "remove_file": True,                                           # all four decisions allowed
        "fetch_file": False,                                           # never interrupt
        "notify_email": {"allowed_decisions": ["approve", "reject"]},  # no editing
    },
    checkpointer=MemorySaver(),                                        # REQUIRED
)
