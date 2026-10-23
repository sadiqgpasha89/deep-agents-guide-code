# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 26: Backends: Where Files Live
# Section: CompositeBackend (routing)
# Snippet 3 of this chapter.

from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

backend = CompositeBackend(
    default=StateBackend(),                                          # ephemeral thread scratch
    routes={"/memories/": StoreBackend(
        namespace=lambda rt: (rt.server_info.user.identity,)         # per-user isolation
    )},
)
agent = create_deep_agent(model=..., backend=backend, store=store)  # pass store= HERE, not to the composite
