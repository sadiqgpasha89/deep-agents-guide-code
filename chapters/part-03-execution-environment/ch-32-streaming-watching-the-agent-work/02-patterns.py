# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 32: Streaming: Watching the Agent Work
# Section: Patterns
# Snippet 2 of this chapter.

from langgraph.config import get_stream_writer
from langchain.tools import tool

@tool
def analyze(data: str) -> str:
    """Analyze data."""
    writer = get_stream_writer()
    writer({"status": "starting", "progress": 0})
    ...
    writer({"status": "done", "progress": 100})
    return "ok"
# pass `analyze` to a subagent via its "tools" key; events surface under that subagent's namespace
