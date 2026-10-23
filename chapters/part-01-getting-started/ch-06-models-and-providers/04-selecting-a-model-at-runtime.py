# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 6: Models and Providers
# Section: Selecting a model at runtime
# Snippet 4 of this chapter.

from dataclasses import dataclass
from langchain.agents.middleware import wrap_model_call
from langchain.chat_models import init_chat_model

@dataclass
class Context:
    model: str

@wrap_model_call
def configurable_model(request, handler):
    model = init_chat_model(request.runtime.context.model)
    return handler(request.override(model=model))

agent = create_deep_agent(model="anthropic:claude-sonnet-4-6",
                          middleware=[configurable_model], context_schema=Context)
agent.invoke({"messages": [...]}, context=Context(model="openai:gpt-5.5"))
