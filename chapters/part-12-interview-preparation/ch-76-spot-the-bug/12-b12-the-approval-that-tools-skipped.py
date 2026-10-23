# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B12. The approval that tools.* skipped
# Snippet 12 of this chapter.

agent = create_deep_agent(
    model=...,
    tools=[send_email],
    interrupt_on={"send_email": True},
    middleware=[CodeInterpreterMiddleware(ptc=["send_email"])],
    checkpointer=MemorySaver(),
)
