# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 36: Context Engineering: Offloading, Summarization and Isolation
# Section: Long-term memory
# Snippet 4 of this chapter.

agent = create_deep_agent(
    store=store,
    backend=CompositeBackend(default=StateBackend(),
                             routes={"/memories/": StoreBackend(namespace=lambda _rt: ("memories",))}),
)
