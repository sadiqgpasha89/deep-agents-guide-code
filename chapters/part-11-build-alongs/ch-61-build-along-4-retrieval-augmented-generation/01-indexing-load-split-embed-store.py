# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 61: Build-Along 4: Retrieval-Augmented Generation with Deep Agents
# Section: Indexing: load, split, embed, store
# Snippet 1 of this chapter.

import requests
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings          # any embeddings model works

DOC_PATHS = [...]                                       # 14 curated documentation pages

docs = []
for path in DOC_PATHS:
    r = requests.get(f"https://docs.langchain.com/{path}.md", timeout=30)
    if r.ok:
        docs.append(r.text)                              # failed fetches are skipped

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents(docs)
vector_store = InMemoryVectorStore.from_documents(chunks, OpenAIEmbeddings(model="text-embedding-3-small"))
