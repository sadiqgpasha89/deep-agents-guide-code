# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 28: Multimodality
# Section: What and how
# Snippet 1 of this chapter.

# 1. user input with an image
agent.invoke({"messages": [{"role": "user", "content": [
    {"type": "text", "text": "What does this screenshot show?"},
    {"type": "image", "url": "https://example.com/screenshot.png"},
]}]})

# 3. tool returning text + image
@tool
def capture_screenshot() -> list[dict]:
    """Capture a screenshot of the page."""
    return [{"type": "text", "text": "Screenshot attached."},
            {"type": "image", "url": "https://example.com/page.png"}]
