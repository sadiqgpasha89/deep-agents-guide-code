# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: 2. Tool retry (`ToolRetryMiddleware`)
# Snippet 3 of this chapter.

ToolRetryMiddleware(max_retries=3, backoff_factor=2.0, initial_delay=1.0, tools=["search", "fetch_url"])
