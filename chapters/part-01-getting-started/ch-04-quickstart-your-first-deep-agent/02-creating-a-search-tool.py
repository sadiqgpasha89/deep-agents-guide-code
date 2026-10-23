# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 4: Quickstart: Your First Deep Agent
# Section: Creating a search tool
# Snippet 2 of this chapter.

# Provider built-in search: pass the dict straight into tools=[...]
google_search    = {"google_search": {}}
openai_search    = {"type": "web_search"}
anthropic_search = {"type": "web_search_20260209", "name": "web_search"}
