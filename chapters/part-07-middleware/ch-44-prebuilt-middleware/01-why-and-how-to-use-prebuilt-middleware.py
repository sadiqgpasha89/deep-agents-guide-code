# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: Why and how to use prebuilt middleware
# Snippet 1 of this chapter.

from deepagents import create_deep_agent
from langchain.agents.middleware import ModelRetryMiddleware, ToolCallLimitMiddleware

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    middleware=[ModelRetryMiddleware(max_retries=3), ToolCallLimitMiddleware(run_limit=50)],
)
