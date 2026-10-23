# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 5: Customization: Configuring a Deep Agent
# Section: State schema, runtime context
# Snippet 8 of this chapter.

from dataclasses import dataclass
from deepagents import DeepAgentState        # import path: confirm against your installed version

@dataclass
class Context:
    user_id: str

class MyState(DeepAgentState):          # must subclass DeepAgentState to keep the messages reducer
    extra_field: str

agent = create_deep_agent(model=..., context_schema=Context, state_schema=MyState)
agent.invoke({"messages": [...], "extra_field": "x"}, context=Context(user_id="u1"))
