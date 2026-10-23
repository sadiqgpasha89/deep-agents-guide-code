# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 59: Build-Along 2: A Data Analysis Agent
# Section: Assembly and run
# Snippet 4 of this chapter.

from langchain_core.utils.uuid import uuid7
from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware
from langgraph.checkpoint.memory import InMemorySaver

agent = create_deep_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[slack_send_message],
    backend=backend,
    checkpointer=InMemorySaver(),               # multi-turn state
    middleware=[TodoListMiddleware()],
)
config = {"configurable": {"thread_id": str(uuid7())}}

stream = agent.stream_events({"messages": [{"role": "user", "content":
    "Analyze ./data/sales_data.csv in the current dir and generate a beautiful plot. "
    "When finished, send your analysis and the plot to Slack using the tool."}]},
    config, version="v3")
for snapshot in stream.values:
    snapshot["messages"][-1].pretty_print()
