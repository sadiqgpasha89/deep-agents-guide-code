# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 23: Going to Production
# Section: Memory scoping in production
# Snippet 3 of this chapter.

from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

backend = CompositeBackend(
    default=StateBackend(),                                   # thread scratch
    routes={"/memories/": StoreBackend(
        namespace=lambda rt: (rt.server_info.assistant_id, rt.server_info.user.identity)
    )},
)
