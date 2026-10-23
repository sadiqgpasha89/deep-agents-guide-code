# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: 10. To-do list (`TodoListMiddleware`)
# Snippet 11 of this chapter.

agent = create_agent(model="gpt-5.5", tools=[read_file, write_file, run_tests], middleware=[TodoListMiddleware()])
