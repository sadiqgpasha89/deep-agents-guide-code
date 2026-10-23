# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B3. The `.env` that stayed readable
# Snippet 3 of this chapter.

permissions = [
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/**"], mode="allow"),
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/.env"], mode="deny"),
]
