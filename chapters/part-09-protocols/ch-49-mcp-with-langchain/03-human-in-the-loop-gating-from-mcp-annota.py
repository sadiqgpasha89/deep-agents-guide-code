# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IX: Protocols
# Chapter 49: MCP with LangChain
# Section: Human-in-the-loop gating from MCP annotations
# Snippet 3 of this chapter.

from langgraph.types import Command

# read the server-declared hint once, defensively (every field is optional)
destructive = {
    t.name for t in tools
    if ((t.metadata or {}).get("mcp", {}).get("annotations") or {}).get("destructive_hint")
}
interrupt_on = {
    name: {
        "allowed_decisions": ["approve", "reject"],
        "when": lambda req: req.tool_call["args"].get("dry_run") is not True,   # safe inputs run freely, risky ones pause
    }
    for name in destructive
}
agent = create_deep_agent(model=..., tools=tools, interrupt_on=interrupt_on, checkpointer=checkpointer)
# approve a paused call
agent.invoke(Command(resume={"decisions": [{"type": "approve"}]}), config)
