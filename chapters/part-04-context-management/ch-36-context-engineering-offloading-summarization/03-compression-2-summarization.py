# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 36: Context Engineering: Offloading, Summarization and Isolation
# Section: Compression 2: summarization
# Snippet 3 of this chapter.

from langchain.agents.middleware import SummarizationMiddleware

agent = create_deep_agent(
    model=..., 
    middleware=[SummarizationMiddleware(
        model="anthropic:claude-haiku-4-5", backend=backend,
        trigger=("tokens", 100_000), keep=("messages", 20),
    )],
)
