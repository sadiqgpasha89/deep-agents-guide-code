# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 60: Build-Along 3: A Content Builder Agent
# Section: Creating the agent
# Snippet 2 of this chapter.

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend

def create_content_writer():
    return create_deep_agent(
        model="anthropic:claude-sonnet-4-6",                 # only the model string changes per provider
        memory=["./AGENTS.md"],
        skills=["./skills/"],
        tools=[generate_cover, generate_social_image],
        subagents=load_subagents("./subagents.yaml"),
        backend=FilesystemBackend(root_dir=EXAMPLE_DIR),
    )
