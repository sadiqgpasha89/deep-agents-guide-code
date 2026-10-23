# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part V: Delegation
# Chapter 38: Subagents: Delegating to Specialists
# Section: Task planning (`write_todos`): the companion tool
# Snippet 4 of this chapter.

from langchain.agents.middleware import TodoListMiddleware

agent = create_deep_agent(model=..., middleware=[TodoListMiddleware()])
