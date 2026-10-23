# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Build-along: Build-Along 4: Retrieval-Augmented Generation with Deep Agents
# Assembled from the code blocks of the chapter, in order.

from prompts import INSTRUCTIONS

# --- Indexing: load, split, embed, store ----------------------------------------
import requests
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings          # any embeddings model works

DOC_PATHS = [                                          # the tutorial indexed 14 curated pages; add yours
    "oss/python/deepagents/overview",
]

docs = []
for path in DOC_PATHS:
    r = requests.get(f"https://docs.langchain.com/{path}.md", timeout=30)
    if r.ok:
        docs.append(r.text)                              # failed fetches are skipped

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents(docs)
vector_store = InMemoryVectorStore.from_documents(chunks, OpenAIEmbeddings(model="text-embedding-3-small"))

# --- The search tool returns paths, not text ----------------------------------------
from deepagents import create_deep_agent
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

# --- The subagent and the orchestrator ----------------------------------------
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


if __name__ == "__main__":
    result = agent.invoke({"messages": [{"role": "user", "content": "How do I stream intermediate tool results from a subagent?"}]})
    print(result["messages"][-1].content)
