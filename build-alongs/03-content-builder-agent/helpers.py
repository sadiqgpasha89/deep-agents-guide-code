"""Helpers the chapter says you write yourself.

`load_subagents` is implemented. The two image tools are stubs: connect them to your image model.
"""
from pathlib import Path

import yaml
from langchain.tools import tool


@tool
def generate_cover(prompt: str, slug: str) -> str:
    """Generate a hero image for a blog post and save it as blogs/<slug>/hero.png.

    Args:
        prompt: description of the image
        slug: the post's folder name
    """
    raise NotImplementedError("Connect an image-generation model here and save the file under blogs/<slug>/hero.png")


@tool
def generate_social_image(prompt: str, platform: str, slug: str) -> str:
    """Generate an image for a social post and save it as <platform>/<slug>/image.png.

    Args:
        prompt: description of the image
        platform: "linkedin" or "tweets"
        slug: the post's folder name
    """
    raise NotImplementedError("Connect an image-generation model here and save the file under <platform>/<slug>/image.png")


def load_subagents(path: str, available_tools: dict | None = None) -> list[dict]:
    """Read subagents.yaml and map tool names to Python callables.

    The YAML maps a subagent name to its description, system_prompt, model and a list of tool names.
    Pass `available_tools` as {"web_search": web_search, ...}.
    """
    available_tools = available_tools or {}
    data = yaml.safe_load(Path(path).read_text()) or {}
    subagents = []
    for name, spec in data.items():
        spec = dict(spec)
        spec["name"] = name
        missing = [t for t in spec.get("tools", []) if t not in available_tools]
        if missing:
            raise KeyError(f"subagent {name!r} uses tools that were not provided to load_subagents: {missing}")
        spec["tools"] = [available_tools[t] for t in spec.get("tools", [])]
        subagents.append(spec)
    return subagents
