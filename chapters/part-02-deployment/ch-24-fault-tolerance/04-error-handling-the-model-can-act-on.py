# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 24: Fault Tolerance
# Section: Error handling the model can act on
# Snippet 4 of this chapter.

from langchain.agents.middleware import ToolErrorMiddleware

def on_error(exc: Exception, request) -> str | None:
    if isinstance(exc, ValueError):
        return f"Bad arguments: {exc}. Fix them and call the tool again."
    return None                       # None = let it propagate

middleware = [ToolErrorMiddleware(on_error)]
