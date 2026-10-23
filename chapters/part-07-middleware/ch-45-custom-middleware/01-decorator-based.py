# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 45: Custom Middleware
# Section: Decorator-based
# Snippet 1 of this chapter.

from typing import Any, Callable
from langchain.agents.middleware import (before_model, wrap_model_call, wrap_tool_call, dynamic_prompt,
                                         AgentState, ModelRequest, ModelResponse)
from langchain.messages import AIMessage
from langgraph.runtime import Runtime

@before_model(can_jump_to=["end"])                       # early exit needs can_jump_to
def check_message_limit(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    if len(state["messages"]) >= 50:
        return {"messages": [AIMessage("Conversation limit reached.")], "jump_to": "end"}
    return None

@wrap_model_call
def retry_model(request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse:
    for attempt in range(3):
        try:
            return handler(request)                      # call through (maybe more than once)
        except Exception as e:
            if attempt == 2:
                raise
            print(f"Retry {attempt + 1}/3 after error: {e}")

agent = create_agent(model="gpt-5.5", tools=[...], middleware=[check_message_limit, retry_model])
