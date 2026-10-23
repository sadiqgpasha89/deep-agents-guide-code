# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 20: Managed Deep Agents: Exposing the Agent over MCP, and Built-in Search
# Section: The MCP endpoint
# Snippet 1 of this chapter.

claude mcp add --transport http research-assistant \
  <DEPLOYMENT_API_URL>/mcp \
  --header "x-api-key: $LANGSMITH_API_KEY"
