# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 21: Managed Deep Agents: Evals and Migration
# Section: Evaluating with Harbor
# Snippet 1 of this chapter.

uvx --from npx-skills skills add langchain-ai/langchain-skills --skill eval-engineering --yes
uv run mda evals init -i      # creates evals/harbor-job.json and .mda/evals/ ; launches a coding agent
