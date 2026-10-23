# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B6. The subagent that lost its tools
# Snippet 6 of this chapter.

research = {"name": "research-agent", "description": "...", "tools": [fetch_url]}
agent = create_deep_agent(model=..., tools=[search, calculator], subagents=[research])
