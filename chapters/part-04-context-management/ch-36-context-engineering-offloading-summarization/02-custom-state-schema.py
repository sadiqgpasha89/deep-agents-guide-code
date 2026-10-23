# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 36: Context Engineering: Offloading, Summarization and Isolation
# Section: Custom state schema
# Snippet 2 of this chapter.

class MyState(DeepAgentState):          # must subclass DeepAgentState (keeps the messages reducer)
    extra_field: str

agent = create_deep_agent(model=..., state_schema=MyState)        # needs deepagents>=0.6.6
agent.invoke({"messages": [...], "extra_field": "hello"})
# inside a tool: runtime.state["extra_field"]
