# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 13: Managed Deep Agents: Tools, Middleware and MCP Connectors
# Section: Custom tools
# Snippet 2 of this chapter.

# agent.py
from managed_deepagents import define_deep_agent
from tools.customer import lookup_customer

agent = define_deep_agent(
    name="support-agent",
    model="openai:gpt-5.5",
    tools=[lookup_customer],
    interrupt_on={"lookup_customer": True},   # optional human approval
)
