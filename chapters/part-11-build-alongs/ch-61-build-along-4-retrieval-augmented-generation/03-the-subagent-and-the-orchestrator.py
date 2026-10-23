# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 61: Build-Along 4: Retrieval-Augmented Generation with Deep Agents
# Section: The subagent and the orchestrator
# Snippet 3 of this chapter.

chunk_analyst = {
    "name": "chunk-analyst",
    "description": "Reads ONE retrieved file and summarizes it",
    "system_prompt": ("Read the file at the path you are given with read_file and return a summary "
                      "under 300 words: key API names, steps, configuration details and the source URL."),
    "tools": [],                                        # built-in file tools only; no vector-store access
}

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[search_documentation],
    backend=backend,
    system_prompt=INSTRUCTIONS,       # plan -> search -> analyse -> synthesize -> verify
    subagents=[chunk_analyst],
)
