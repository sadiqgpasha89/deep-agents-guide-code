# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: 1. Tool error (`ToolErrorMiddleware`, `langchain>=1.3.14`)
# Snippet 2 of this chapter.

from langchain.agents.middleware import ToolErrorMiddleware

def on_error(exc: Exception, request) -> str | None:
    if isinstance(exc, ValueError):
        return f"`{request.tool_call['name']}` failed with {type(exc).__name__}."
    # return None implicitly -> propagate everything else

agent = create_agent(model="gpt-5.5", tools=[...], middleware=[ToolErrorMiddleware(on_error)])
