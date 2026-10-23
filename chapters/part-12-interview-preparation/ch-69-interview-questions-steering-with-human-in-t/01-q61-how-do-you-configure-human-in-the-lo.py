# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 69: Interview Questions: Steering with Human-in-the-Loop and Rubrics
# Section: Q61. How do you configure human-in-the-loop, and what are the four decisions?
# Snippet 1 of this chapter.

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[remove_file, fetch_file, notify_email],
    interrupt_on={
        "remove_file": True,                                           # all four decisions
        "fetch_file": False,                                           # never interrupt
        "notify_email": {"allowed_decisions": ["approve", "reject"]},  # no editing
    },
    checkpointer=MemorySaver(),                                        # required
)
