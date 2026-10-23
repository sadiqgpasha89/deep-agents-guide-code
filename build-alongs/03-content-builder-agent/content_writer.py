# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Build-along: Build-Along 3: A Content Builder Agent
# Assembled from the code blocks of the chapter, in order.

from pathlib import Path

from helpers import generate_cover, generate_social_image, load_subagents

EXAMPLE_DIR = str(Path(__file__).parent / "workspace")

# --- Creating the agent ----------------------------------------
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
