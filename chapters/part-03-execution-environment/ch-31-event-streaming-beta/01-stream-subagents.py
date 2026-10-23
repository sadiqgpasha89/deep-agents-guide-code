# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 31: Event Streaming (Beta)
# Section: `stream.subagents`
# Snippet 1 of this chapter.

stream = agent.stream_events(
    {"messages": [{"role": "user", "content": "Research LangGraph and write a summary"}]},
    version="v3",
)
for subagent in stream.subagents:
    print(f"[{subagent.name}] status={subagent.status}")
    for call in subagent.tool_calls:
        print("  tool:", call.tool_name, call.input)
    for nested in subagent.subagents:           # nested subagents: recurse
        print("  nested:", nested.name)
print(stream.output)
