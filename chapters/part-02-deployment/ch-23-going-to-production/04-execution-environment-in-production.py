# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 23: Going to Production
# Section: Execution environment in production
# Snippet 4 of this chapter.

from langchain_core.runnables import RunnableConfig
# SandboxClient / LangSmithSandbox come from the `langsmith[sandbox]` package (check import paths for your version)

async def make_graph(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    name = f"thread-{thread_id}"                                  # assistant-scoped: f"assistant-{assistant_id}"
    client = SandboxClient()
    sandbox = find_sandbox_by_name(client, name)                  # pseudocode: look up an existing sandbox
    if sandbox is None:
        sandbox = client.create_sandbox(name=name, idle_ttl_seconds=3600)
    return create_deep_agent(model="anthropic:claude-sonnet-4-6",
                             backend=LangSmithSandbox(sandbox=sandbox))
