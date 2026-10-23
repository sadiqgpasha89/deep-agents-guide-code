# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 35: Retrieval: Bringing in Outside Knowledge
# Section: How Deep Agents integrates retrieval
# Snippet 1 of this chapter.

from langchain.tools import tool

@tool
def fetch_documentation(url: str) -> str:
    """Fetch a docs page and convert it to markdown."""
    ...

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[fetch_documentation],
    system_prompt="Answer using the documentation. Cite URLs. If a fetch fails, say so.",
    subagents=[{"name": "chunk-analyst", "description": "Reads ONE retrieved file and summarizes it",
                "system_prompt": "Read the file at the path you're given and return a 3-bullet summary."}],
)
