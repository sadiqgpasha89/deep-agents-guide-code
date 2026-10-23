# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 24: Fault Tolerance
# Section: Rate limiting
# Snippet 2 of this chapter.

from langchain.agents.middleware import ModelCallLimitMiddleware, ToolCallLimitMiddleware

middleware = [
    ModelCallLimitMiddleware(run_limit=50),     # resets every turn
    ToolCallLimitMiddleware(run_limit=200),
    # thread_limit=... caps calls across a whole conversation (needs a checkpointer)
]
