# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 5: Customization: Configuring a Deep Agent
# Section: Human-in-the-loop
# Snippet 6 of this chapter.

from langgraph.checkpoint.memory import MemorySaver

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[remove_file, fetch_file, notify_email],
    interrupt_on={
        "remove_file": True,                                           # approve / edit / reject / respond
        "fetch_file": False,                                           # never interrupt
        "notify_email": {"allowed_decisions": ["approve", "reject"]},  # no editing
    },
    checkpointer=MemorySaver(),                                        # REQUIRED
)
