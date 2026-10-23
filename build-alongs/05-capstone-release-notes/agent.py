# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Build-along: Capstone: A Release-Notes Assistant that Uses Every Layer
# Assembled from the code blocks of the chapter, in order.

# --- The code ----------------------------------------
from deepagents import create_deep_agent, FilesystemPermission, RubricMiddleware
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
from langchain.agents.middleware import (
    ModelCallLimitMiddleware, ModelFallbackMiddleware, ModelRetryMiddleware,
    TodoListMiddleware, ToolCallLimitMiddleware)
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver      # use a durable saver in production
from langgraph.types import Command
from langgraph.store.memory import InMemoryStore            # use a durable store in production

# (1) per-user long-term memory; everything else is thread-scoped
backend = CompositeBackend(
    default=StateBackend(),
    routes={"/memories/": StoreBackend(namespace=lambda rt: (rt.server_info.user.identity, "memories"))},
)

@tool
def publish_release_notes(version: str, markdown: str) -> str:
    """Publish approved release notes to the changelog site."""
    ...  # side effect: gated below

researcher = {"name": "researcher", "description": "Collects merged PRs and issues for a version.",
              "system_prompt": "Return a bulleted list of changes with PR links. Be concise.", "tools": [...]}
fact_checker = {"name": "fact-checker", "description": "Verifies each claim in a draft against its source link.",
                "system_prompt": "Return only claims you could NOT verify, with reasons.", "tools": [...]}

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[publish_release_notes],
    system_prompt="You draft accurate release notes. Delegate research and fact-checking; publish only after approval.",
    backend=backend,
    memory=["/memories/AGENTS.md"],                              # (1) always loaded
    skills=["/skills/"],                                         # (2) progressive disclosure
    permissions=[                                                # (3) first match wins
        FilesystemPermission(operations=["write"], paths=["/skills/**", "/memories/policy/**"], mode="deny"),
    ],
    subagents=[researcher, fact_checker],                        # (4)
    interrupt_on={"publish_release_notes": {"allowed_decisions": ["approve", "edit", "reject"]}},  # (5)
    middleware=[
        TodoListMiddleware(),
        RubricMiddleware(model="anthropic:claude-haiku-4-5", max_iterations=3),                 # (6)
        ModelRetryMiddleware(max_retries=3),                                                    # (7)
        ModelFallbackMiddleware("gpt-5.5"),
        ModelCallLimitMiddleware(run_limit=60),
        ToolCallLimitMiddleware(run_limit=200),
    ],
    checkpointer=InMemorySaver(),                                # required for interrupts
    store=InMemoryStore(),
)

# --- Running it ----------------------------------------
rubric = """- The notes start with a version header (## vX.Y.Z)
- The notes contain a 'Breaking changes' section, or say 'None'
- Every claim links to a PR or issue
"""
cfg = {"configurable": {"thread_id": "release-2.4"}}
state = {"messages": [{"role": "user", "content": "Draft and publish notes for v2.4"}], "rubric": rubric}

result = agent.invoke(state, cfg)
if result.get("__interrupt__"):                         # (5) a human decides
    reqs = result["__interrupt__"][0].value["action_requests"]
    decisions = [{"type": "approve"} for _ in reqs]      # one decision per request, same order
    result = agent.invoke(Command(resume={"decisions": decisions}), cfg)
print(result.get("_rubric_status"))                      # (6) satisfied / max_iterations_reached
