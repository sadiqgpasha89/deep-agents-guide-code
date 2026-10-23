# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 26: Backends: Where Files Live
# Section: FilesystemBackend
# Snippet 2 of this chapter.

from deepagents.backends import FilesystemBackend
backend = FilesystemBackend(root_dir="/work/project", virtual_mode=True)
