# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B4. Everyone shares one memory
# Snippet 4 of this chapter.

backend = CompositeBackend(
    default=StateBackend(),
    routes={"/memories/": StoreBackend()},
)
