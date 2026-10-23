# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 27: Permissions: Controlling File Access
# Section: Recipes
# Snippet 2 of this chapter.

# Read-only agent
[FilesystemPermission(operations=["write"], paths=["/**"], mode="deny")]

# Workspace isolation: allow /workspace, deny everything else
[FilesystemPermission(operations=["read", "write"], paths=["/workspace/**"], mode="allow"),
 FilesystemPermission(operations=["read", "write"], paths=["/**"], mode="deny")]

# Protect secrets: specific denies BEFORE the broad allow
[FilesystemPermission(operations=["read", "write"], paths=["/workspace/.env", "/workspace/examples/**"], mode="deny"),
 FilesystemPermission(operations=["read", "write"], paths=["/workspace/**"], mode="allow"),
 FilesystemPermission(operations=["read", "write"], paths=["/**"], mode="deny")]

# Read-only memory/policies (with a CompositeBackend)
[FilesystemPermission(operations=["write"], paths=["/memories/**", "/policies/**"], mode="deny")]

# Approval required for writes to /secrets
[FilesystemPermission(operations=["write"], paths=["/secrets/**"], mode="interrupt")]
