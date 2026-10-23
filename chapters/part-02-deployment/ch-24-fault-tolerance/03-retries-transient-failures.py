# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 24: Fault Tolerance
# Section: Retries (transient failures)
# Snippet 3 of this chapter.

from langchain.agents.middleware import ModelRetryMiddleware, ToolRetryMiddleware

middleware = [
    ModelRetryMiddleware(max_retries=3, backoff_factor=2.0, initial_delay=1.0),
    ToolRetryMiddleware(
        max_retries=2,
        tools=["search", "fetch_url"],                       # scope to tools that call external APIs
        retry_on=(TimeoutError, ConnectionError),
    ),
]
