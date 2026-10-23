# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 65: Interview Questions: Tools, Backends and Permissions
# Section: Q21. A permission list protects `.env`, but the agent can still read it. Why?
# Snippet 3 of this chapter.

permissions = [
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/.env"], mode="deny"),
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/**"], mode="allow"),
    FilesystemPermission(operations=["read", "write"], paths=["/**"], mode="deny"),
]
