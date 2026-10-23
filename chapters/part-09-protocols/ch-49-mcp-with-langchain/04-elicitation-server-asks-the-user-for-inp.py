# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IX: Protocols
# Chapter 49: MCP with LangChain
# Section: Elicitation (server asks the user for input)
# Snippet 4 of this chapter.

[interrupt] = paused["__interrupt__"]
[question] = interrupt.value["requests"]
answer = {"action": "accept", "content": {"date": "2026-09-14"}}      # or "decline" / "cancel"
result = await agent.ainvoke(Command(resume={"responses": {question["key"]: answer}}), config)
