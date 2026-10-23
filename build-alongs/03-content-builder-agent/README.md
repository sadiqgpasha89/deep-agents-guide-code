# Build-Along 3: A Content Builder Agent

Companion to **Chapter 60: Build-Along 3: A Content Builder Agent** in *Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)*.

**Status:** partial. The chapter shows how to create the agent; the files it loads (`AGENTS.md`, `subagents.yaml`, `skills/`) and the two image tools are yours to write. `helpers.py` provides a working `load_subagents` and two stubs for the image tools.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r ../../requirements.txt
cp ../../.env.example ../../.env   # then fill in the keys listed below
python content_writer.py
```

Keys used: `ANTHROPIC_API_KEY` plus whatever your image tools need

Create `AGENTS.md`, `subagents.yaml` and `skills/*/SKILL.md` as described in the chapter, then implement `generate_cover` and `generate_social_image` in `helpers.py`.
