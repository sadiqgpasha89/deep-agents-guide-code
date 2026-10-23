# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part V: Delegation
# Chapter 38: Subagents: Delegating to Specialists
# Section: Isolated vs fork
# Snippet 3 of this chapter.

reviewer_fork = {"name": "pr-commenter", "description": "Drafts review comments for issues already found",
                 "mode": "fork"}      # no system_prompt: shares the parent's cache prefix
