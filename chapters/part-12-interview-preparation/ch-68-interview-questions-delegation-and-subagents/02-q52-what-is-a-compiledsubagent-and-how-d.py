# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 68: Interview Questions: Delegation and Subagents
# Section: Q52. What is a `CompiledSubAgent`, and how does a subagent return structured output?
# Snippet 2 of this chapter.

custom = CompiledSubAgent(
    name="data-analyzer",
    description="Specialized agent for data analysis",
    runnable=create_agent(model="anthropic:claude-sonnet-4-6", tools=[run_sql], system_prompt="..."),
    mode="isolated",
)
