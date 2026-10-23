# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: 15. Subagent (`SubAgentMiddleware`, from `deepagents`)
# Snippet 16 of this chapter.

from deepagents.middleware.subagents import SubAgentMiddleware
SubAgentMiddleware(default_model="claude-sonnet-4-6", default_tools=[],
    subagents=[{"name": "weather", "description": "Gets weather in cities.",
                "system_prompt": "Use get_weather.", "tools": [get_weather], "model": "gpt-5.5", "middleware": []}])
