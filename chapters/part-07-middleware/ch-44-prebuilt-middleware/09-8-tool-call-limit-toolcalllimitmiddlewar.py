# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: 8. Tool call limit (`ToolCallLimitMiddleware`)
# Snippet 9 of this chapter.

middleware=[
    ToolCallLimitMiddleware(thread_limit=20, run_limit=10),                       # global
    ToolCallLimitMiddleware(tool_name="search", thread_limit=5, run_limit=3),     # per tool
]
