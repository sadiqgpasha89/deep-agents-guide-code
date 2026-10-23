# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 68: Interview Questions: Delegation and Subagents
# Section: Q49. What does the `task` tool do, and what does a subagent specification contain?
# Snippet 1 of this chapter.

research_subagent = {
    "name": "research-agent",                 # required; used in task() calls
    "description": "Researches deep questions",  # required; drives delegation decisions
    "system_prompt": "You are a careful researcher.",  # required for isolated mode
    "tools": [internet_search],               # if set, REPLACES the parent's tools
    "model": "openai:gpt-5.5",                # inherits if omitted
}
agent = create_deep_agent(model="google_genai:gemini-3.6-flash", subagents=[research_subagent])
