# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B1. The approval that never pauses
# Snippet 1 of this chapter.

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[send_email],
    interrupt_on={"send_email": True},
)
