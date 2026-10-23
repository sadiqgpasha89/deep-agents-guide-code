# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 5: Customization: Configuring a Deep Agent
# Section: Middleware
# Snippet 4 of this chapter.

from langchain.agents.middleware import wrap_tool_call, SummarizationMiddleware
from deepagents.middleware.filesystem import FilesystemMiddleware

@wrap_tool_call
def log_tool_calls(request, handler):
    result = handler(request)
    return result

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    middleware=[
        log_tool_calls,                                   # inserted after PatchToolCallsMiddleware
        SummarizationMiddleware(                          # same .name -> REPLACES the built-in
            model="anthropic:claude-haiku-4-5",
            backend=my_backend,
            trigger=("tokens", 100_000),
            keep=("messages", 20),
        ),
        # read-only filesystem (read_file is mandatory in the list; deepagents>=0.7)
        FilesystemMiddleware(backend=my_backend, tools=["read_file", "ls", "glob", "grep"]),
    ],
)
