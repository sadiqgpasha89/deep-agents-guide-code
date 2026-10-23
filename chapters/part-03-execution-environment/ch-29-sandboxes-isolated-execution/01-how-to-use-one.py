# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 29: Sandboxes: Isolated Execution
# Section: How to use one
# Snippet 1 of this chapter.

from langchain_anthropic import ChatAnthropic

client = SandboxClient()                                   # LangSmith example
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)             # DaytonaSandbox(sandbox=...), E2BSandbox(sandbox=...), ...

agent = create_deep_agent(
    model=ChatAnthropic(model="claude-sonnet-4-6"),
    backend=backend,
    system_prompt="You are a coding assistant with sandbox access.",
)
try:
    agent.invoke({"messages": [{"role": "user", "content": "Create a hello-world Python file and run it"}]})
finally:
    client.delete_sandbox(ls_sandbox.name)                 # ALWAYS tear down (it costs money until shut down)
