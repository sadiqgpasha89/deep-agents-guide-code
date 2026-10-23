# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 5: Customization: Configuring a Deep Agent
# Section: Subagents
# Snippet 5 of this chapter.

research_subagent = {
    "name": "research-agent",
    "description": "Used to research more in depth questions",
    "system_prompt": "You are a great researcher",
    "tools": [internet_search],
    "model": "openai:gpt-5.5",        # optional; default = main agent's model
}
agent = create_deep_agent(model="google_genai:gemini-3.6-flash", subagents=[research_subagent])
