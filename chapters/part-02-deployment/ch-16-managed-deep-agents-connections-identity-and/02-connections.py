# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 16: Managed Deep Agents: Connections, Identity and the Runtime
# Section: Connections
# Snippet 2 of this chapter.

# in a tool
from managed_deepagents import connections   # import path: confirm against the MDA reference
api_key = await connections.get("organization-tavily", {"type": "agent"})
