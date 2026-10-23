# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B2. The resume that starts over
# Snippet 2 of this chapter.

def resume(decisions):
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    return agent.invoke(Command(resume={"decisions": decisions}), config=config)
