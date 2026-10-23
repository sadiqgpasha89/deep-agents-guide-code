# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 33: Skills: Procedures on Demand
# Section: Sources and backends
# Snippet 4 of this chapter.

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Write a post about LangGraph"}]},
    files={"/skills/blog-post/SKILL.md": create_file_data(skill_md_text)},   # StateBackend seeding
)
