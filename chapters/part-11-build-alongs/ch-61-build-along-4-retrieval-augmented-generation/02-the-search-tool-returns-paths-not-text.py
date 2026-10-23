# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 61: Build-Along 4: Retrieval-Augmented Generation with Deep Agents
# Section: The search tool returns paths, not text
# Snippet 2 of this chapter.

from deepagents.backends import StateBackend
from langchain.tools import tool
from langchain_core.utils.uuid import uuid7

backend = StateBackend()                                # the SAME instance must go to create_deep_agent

@tool
def search_documentation(query: str) -> str:
    """Search the LangChain documentation index. Returns file paths of retrieved chunks."""
    hits = vector_store.similarity_search(query, k=4)
    batch_id = str(uuid7())[:8]
    files, paths = [], []
    for n, doc in enumerate(hits, 1):
        path = f"/retrieved/{batch_id}/chunk_{n}.md"
        files.append((path, f"# Source: {doc.metadata.get('source','unknown')}\n\n{doc.page_content}".encode()))
        paths.append(path)
    backend.upload_files(files)
    return "Saved chunks:\n" + "\n".join(paths)
