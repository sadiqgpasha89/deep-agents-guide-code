# Capstone: A Release-Notes Assistant that Uses Every Layer

Companion to **Chapter 62: Capstone: A Release-Notes Assistant that Uses Every Layer** in *Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)*.

**Status:** illustrative. The `tools` lists of the two subagents contain `...` placeholders and `publish_release_notes` has no body, so you must supply real tools before running it. It shows how the layers fit together, with numbered comments matching the chapter.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r ../../requirements.txt
cp ../../.env.example ../../.env   # then fill in the keys listed below
python agent.py
```

Keys used: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` (fallback model)

Replace the in-memory checkpointer and store with durable ones in production.
