# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 13: Managed Deep Agents: Tools, Middleware and MCP Connectors
# Section: Middleware
# Snippet 4 of this chapter.

# middleware/audit.py
from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage
from langchain.tools.tool_node import ToolCallRequest
from langgraph.types import Command

@wrap_tool_call
async def log_tool_calls(request: ToolCallRequest, handler) -> ToolMessage | Command:
    print(f"calling {request.tool_call['name']}")
    result = await handler(request)
    print("done")
    return result
