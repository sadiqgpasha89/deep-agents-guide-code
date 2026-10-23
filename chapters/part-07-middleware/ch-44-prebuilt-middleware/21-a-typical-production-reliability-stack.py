# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: A typical production reliability stack
# Snippet 21 of this chapter.

middleware=[
    ModelRetryMiddleware(max_retries=3),
    ModelFallbackMiddleware("gpt-5.4-mini", "claude-sonnet-4-6"),
    ToolRetryMiddleware(max_retries=2, tools=["search"], on_failure="error"),   # inside ToolError
    ToolErrorMiddleware(on_error),
    ModelCallLimitMiddleware(run_limit=50),
    ToolCallLimitMiddleware(run_limit=200),
    PIIMiddleware("email", strategy="redact", apply_to_input=True),
]
