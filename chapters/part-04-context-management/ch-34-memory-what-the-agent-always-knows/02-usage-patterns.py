# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 34: Memory: What the Agent Always Knows
# Section: Usage patterns
# Snippet 2 of this chapter.

from deepagents.backends.utils import create_file_data      # import path: confirm for your version
store.put(("org-123",), "/AGENTS.md", create_file_data("# Policies\n- Never disclose internal pricing."))
