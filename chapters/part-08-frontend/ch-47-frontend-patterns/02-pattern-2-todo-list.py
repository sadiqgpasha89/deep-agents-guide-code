# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VIII: Frontend
# Chapter 47: Frontend Patterns
# Section: Pattern 2: Todo list
# Snippet 2 of this chapter.

from langchain.agents.middleware import TodoListMiddleware
agent = create_deep_agent(model=..., middleware=[TodoListMiddleware()])   # adds write_todos + persists todos in state
