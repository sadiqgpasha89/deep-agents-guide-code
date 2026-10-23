# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 65: Interview Questions: Tools, Backends and Permissions
# Section: Q18. How does `CompositeBackend` route, and what is the canonical memory pattern?
# Snippet 2 of this chapter.

backend = CompositeBackend(
    default=StateBackend(),
    routes={"/memories/": StoreBackend(
        namespace=lambda rt: (rt.server_info.user.identity,)
    )},
)
agent = create_deep_agent(model=..., backend=backend, store=store)  # store goes here
