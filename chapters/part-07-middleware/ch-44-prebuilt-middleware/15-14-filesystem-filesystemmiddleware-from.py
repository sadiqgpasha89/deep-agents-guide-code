# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: 14. Filesystem (`FilesystemMiddleware`, from `deepagents`)
# Snippet 15 of this chapter.

from deepagents.middleware.filesystem import FilesystemMiddleware
FilesystemMiddleware(backend=None, tools=["read_file", "ls", "glob", "grep"],
                     custom_tool_descriptions={"ls": "Use ls when..."})
