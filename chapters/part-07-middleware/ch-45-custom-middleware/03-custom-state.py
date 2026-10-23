# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 45: Custom Middleware
# Section: Custom state
# Snippet 3 of this chapter.

from typing import NotRequired

class CustomState(AgentState):
    model_call_count: NotRequired[int]
    user_id: NotRequired[str]

@before_model(state_schema=CustomState)
def count_calls(state: CustomState, runtime: Runtime) -> dict[str, Any] | None:
    return {"model_call_count": state.get("model_call_count", 0) + 1}
