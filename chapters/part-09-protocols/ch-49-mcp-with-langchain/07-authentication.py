# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IX: Protocols
# Chapter 49: MCP with LangChain
# Section: Authentication
# Snippet 7 of this chapter.

# Bearer
async with MCPAdapter(Client(url, auth=token)) as adapter: ...

# OAuth 2.1: discovery + dynamic client registration + browser redirect + token exchange
async with MCPAdapter(Client(url, auth="oauth")) as adapter: ...
# persist tokens so you don't repeat the browser step
oauth = OAuth(mcp_url="https://example.com/mcp", token_storage=...)
client = Client("https://example.com/mcp", auth=oauth)

# Per-server (mix auth types)
group = ClientGroup({"billing": Client(billing_url, auth="oauth"), "docs": Client(docs_url, auth=docs_token)})

# Per-user (inside a graph factory: authenticate caller at the LangGraph server, then mint/exchange a per-user token)
user = runtime.user.identity if runtime.user is not None else "anonymous"
auth = BearerAuth(token_for(user))                        # token_for = your exchange (OAuth gateway, FastMCP provider, ...)
async with MCPAdapter(Client(CONFIG, auth=auth)) as adapter:
    tools = await adapter.list_tools()
