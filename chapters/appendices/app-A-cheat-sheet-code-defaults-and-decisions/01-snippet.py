# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Appendices
# Appendix A: Cheat Sheet: Code, Defaults and Decisions
# Snippet 1 of this chapter.

# ── Create ─────────────────────────────────────────────────────────────
from deepagents import create_deep_agent, FilesystemPermission
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
from langchain.agents.middleware import TodoListMiddleware
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",           # or a model object
    tools=[my_tool],                                # + MCP via MCPAdapter
    system_prompt="...",
    memory=["/memories/AGENTS.md"],                 # always loaded
    skills=["/skills/"],                            # progressive disclosure
    backend=CompositeBackend(default=StateBackend(),
            routes={"/memories/": StoreBackend(namespace=lambda rt: (rt.server_info.user.identity,))}),
    permissions=[FilesystemPermission(operations=["write"], paths=["/skills/**"], mode="deny")],
    subagents=[{"name": "...", "description": "...", "system_prompt": "...", "tools": [...]}],
    middleware=[TodoListMiddleware()],              # opt-in planning
    interrupt_on={"send_email": True},              # HITL
    context_schema=Ctx, state_schema=MyState,
    checkpointer=MemorySaver(), store=InMemoryStore(),
)

# ── Run ────────────────────────────────────────────────────────────────
cfg = {"configurable": {"thread_id": "t1"}}
agent.invoke({"messages": [{"role": "user", "content": "..."}]}, config=cfg, context=Ctx(...))

# ── Resume after HITL ─────────────────────────────────────────────────
from langgraph.types import Command
agent.invoke(Command(resume={"decisions": [{"type": "approve"}]}), config=cfg)

# ── Stream ─────────────────────────────────────────────────────────────
for c in agent.stream(inp, stream_mode="updates", subgraphs=True, version="v2", config=cfg): ...
stream = agent.stream_events(inp, version="v3")      # → stream.subagents / stream.messages / stream.values
