# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B7. One decision for two requests
# Snippet 7 of this chapter.

payload = result["__interrupt__"][0].value        # two action_requests
decisions = [{"type": "approve"}]
agent.invoke(Command(resume={"decisions": decisions}), config=config)
