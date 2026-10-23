# Build-Along 1: A Deep Research Agent

Companion to **Chapter 58: Build-Along 1: A Deep Research Agent** in *Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)*.

**Status:** assembled from the chapter's three code blocks. The prompts live in `prompts.py`, which contains short starter prompts written for this repository (the tutorial's own prompts are longer). Not executed during preparation of this repository.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r ../../requirements.txt
cp ../../.env.example ../../.env   # then fill in the keys listed below
python agent.py
```

Keys used: `ANTHROPIC_API_KEY`, `TAVILY_API_KEY`

The script defines `agent` and runs two example questions. Edit the questions at the bottom.
