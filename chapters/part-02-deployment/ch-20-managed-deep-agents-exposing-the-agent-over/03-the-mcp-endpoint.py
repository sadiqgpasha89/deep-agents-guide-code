# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 20: Managed Deep Agents: Exposing the Agent over MCP, and Built-in Search
# Section: The MCP endpoint
# Snippet 3 of this chapter.

from langchain_mcp_adapters.client import MultiServerMCPClient
client = MultiServerMCPClient({"research-assistant": {
    "transport": "streamable_http", "url": "<DEPLOYMENT_API_URL>/mcp",
    "headers": {"x-api-key": os.environ["LANGSMITH_API_KEY"]}}})
tools = await client.get_tools()
