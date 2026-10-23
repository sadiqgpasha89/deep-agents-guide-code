# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 5: Customization: Configuring a Deep Agent
# Section: Skills and memory
# Snippet 7 of this chapter.

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    skills=["/skills/"],                  # directory that CONTAINS skill folders
    memory=["/AGENTS.md"],                # always loaded
    # seed the files into the backend (StateBackend example):
    # agent.invoke({...}, files={"/AGENTS.md": create_file_data(text)})
)
