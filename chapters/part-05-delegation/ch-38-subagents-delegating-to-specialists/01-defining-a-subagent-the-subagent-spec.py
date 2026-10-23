# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part V: Delegation
# Chapter 38: Subagents: Delegating to Specialists
# Section: Defining a subagent (the `SubAgent` spec)
# Snippet 1 of this chapter.

research_subagent = {
    "name": "research-agent",            # REQUIRED; used in task() calls and metadata
    "description": "Used to research more in depth questions",   # REQUIRED; drives delegation decisions
    "system_prompt": "You are a great researcher",   # REQUIRED for isolated; optional addendum for fork
    "mode": "isolated",                  # "isolated" (default) | "fork"
    "tools": [internet_search],          # INHERITS parent tools; if set, REPLACES them
    "model": "openai:gpt-5.5",           # INHERITS; "provider:model" or model object
    "middleware": [],                    # does NOT inherit; same .name replaces a default
    "interrupt_on": {"send_email": True},# INHERITS; needs a checkpointer
    "skills": ["/skills/research/"],     # does NOT inherit; gets its own SkillsMiddleware
    "response_format": ResearchResult,   # JSON result to parent (deepagents >= 0.5.3)
    "permissions": [FilesystemPermission(operations=["write"], paths=["/**"], mode="deny")],  # INHERITS; REPLACES
}
agent = create_deep_agent(model="google_genai:gemini-3.6-flash", subagents=[research_subagent])
