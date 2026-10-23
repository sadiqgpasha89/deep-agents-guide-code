# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 32: Streaming: Watching the Agent Work
# Section: Enabling subagent events
# Snippet 1 of this chapter.

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Research quantum computing"}]},
    stream_mode="updates",
    subgraphs=True,           # without this, NO subagent events
    version="v2",
):
    ...
