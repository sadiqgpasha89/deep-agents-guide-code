# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 4: Quickstart: Your First Deep Agent
# Section: Creating a search tool
# Snippet 3 of this chapter.

# Tavily wrapper (works with any model)
import os
from typing import Literal
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search."""
    return tavily_client.search(
        query, max_results=max_results,
        include_raw_content=include_raw_content, topic=topic,
    )
