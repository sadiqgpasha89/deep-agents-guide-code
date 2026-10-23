# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B9. The counter that races
# Snippet 9 of this chapter.

class CallCounter(AgentMiddleware):
    def __init__(self):
        self.calls = 0
    def before_model(self, state, runtime):
        self.calls += 1
