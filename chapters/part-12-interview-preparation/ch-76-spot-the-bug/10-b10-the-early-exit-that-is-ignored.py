# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B10. The early exit that is ignored
# Snippet 10 of this chapter.

@before_model
def stop_if_long(state, runtime):
    if len(state["messages"]) > 50:
        return {"messages": [AIMessage("Conversation limit reached.")], "jump_to": "end"}
