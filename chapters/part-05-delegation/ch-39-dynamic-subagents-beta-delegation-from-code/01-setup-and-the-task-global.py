# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part V: Delegation
# Chapter 39: Dynamic Subagents (Beta): Delegation from Code
# Section: Setup and the `task()` global
# Snippet 1 of this chapter.

from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    subagents=[
        {"name": "reviewer", "description": "Reviews one file", "system_prompt": "You review code."},
        {"name": "verifier", "description": "Skeptically verifies a finding", "system_prompt": "Be skeptical."},
    ],
    middleware=[CodeInterpreterMiddleware(ptc=["glob"], subagents=True)],   # subagents=False disables dispatch
)
