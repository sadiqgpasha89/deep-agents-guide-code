# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 27: Permissions: Controlling File Access
# Section: Rule structure
# Snippet 1 of this chapter.

from deepagents import FilesystemPermission

FilesystemPermission(
    operations=["read", "write"],        # "read" = ls, read_file, glob, grep; "write" = write_file, edit_file, delete
    paths=["/workspace/**"],             # glob patterns; ** recursive, {a,b} alternatives
    mode="deny",                         # "allow" (default) | "deny" | "interrupt" (needs checkpointer + deepagents>=0.6.8)
)
agent = create_deep_agent(model=..., backend=..., permissions=[...], checkpointer=...)
