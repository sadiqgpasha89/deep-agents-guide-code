# Build-Along 2: A Data Analysis Agent

Companion to **Chapter 59: Build-Along 2: A Data Analysis Agent** in *Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)*.

**Status:** assembled from the chapter's four code blocks. It needs a LangSmith sandbox and a Slack user token. The `channel` ID in the code is a placeholder to replace. Not executed during preparation of this repository.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r ../../requirements.txt
cp ../../.env.example ../../.env   # then fill in the keys listed below
python agent.py
```

Keys used: `LANGSMITH_API_KEY`, `GOOGLE_API_KEY`, `SLACK_USER_TOKEN`

Secrets stay on the host: the Slack token is read by the tool, never placed inside the sandbox.
