# Build-Along 4: Retrieval-Augmented Generation with Deep Agents

Companion to **Chapter 61: Build-Along 4: Retrieval-Augmented Generation with Deep Agents** in *Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)*.

**Status:** assembled from the chapter's three code blocks. `prompts.py` holds a starter orchestrator prompt written for this repository, and `DOC_PATHS` starts with a single page: add the pages you want to index. Not executed during preparation of this repository.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r ../../requirements.txt
cp ../../.env.example ../../.env   # then fill in the keys listed below
python agent.py
```

Keys used: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` (for the embeddings model)

The search tool saves retrieved chunks as files and returns only their paths, so the orchestrator's context stays small. The same `StateBackend` instance must be passed to `create_deep_agent`.
