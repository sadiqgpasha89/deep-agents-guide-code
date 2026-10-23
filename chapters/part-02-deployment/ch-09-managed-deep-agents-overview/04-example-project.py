# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 9: Managed Deep Agents: Overview
# Section: Example project
# Snippet 4 of this chapter.

# tools/search.py
from langchain.tools import tool

@tool(parse_docstring=True)
def internet_search(query: str) -> str:
    """Search the internet for relevant sources.

    Args:
        query: The search query.
    """
    return f"Results for: {query}"
