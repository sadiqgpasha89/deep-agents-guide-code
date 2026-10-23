# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 13: Managed Deep Agents: Tools, Middleware and MCP Connectors
# Section: Custom tools
# Snippet 1 of this chapter.

# tools/customer.py
from langchain.tools import tool

@tool(parse_docstring=True)
def lookup_customer(customer_id: str) -> str:
    """Look up a customer record.

    Args:
        customer_id: The customer's unique ID.
    """
    ...
