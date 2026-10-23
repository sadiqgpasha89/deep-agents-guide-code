# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 16: Managed Deep Agents: Connections, Identity and the Runtime
# Section: The managed runtime
# Snippet 4 of this chapter.

@tool
async def check_order(order_id: str, runtime: ManagedToolRuntime[AppContext]) -> str:
    """Check the status of an order."""
    principal = runtime.server_info.principal if runtime.server_info else None
    if principal is None:
        return "Sign in to check orders."
    if runtime.channel is not None and runtime.channel.post is not None:
        await runtime.channel.post({"type": "content", "content": "Checking that order now."})
    region = runtime.context.region if runtime.context else "us"
    return f"Order {order_id} for {principal.id} ships from {region}."
