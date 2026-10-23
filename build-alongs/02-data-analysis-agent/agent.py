# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Build-along: Build-Along 2: A Data Analysis Agent
# Assembled from the code blocks of the chapter, in order.

# --- Sandbox setup ----------------------------------------
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

# --- Sandbox setup ----------------------------------------
import csv, io
data = [["Date","Product","Units Sold","Revenue"],
        ["2025-08-01","Widget A",10,250], ["2025-08-02","Widget B",5,125],
        ["2025-08-03","Widget A",7,175],  ["2025-08-04","Widget C",3,90],
        ["2025-08-05","Widget B",8,200]]
buf = io.StringIO(); csv.writer(buf).writerows(data)
backend.upload_files([("/root/data/sales_data.csv", buf.getvalue().encode("utf-8"))])

# --- The Slack tool (secrets stay on the host) ----------------------------------------
import os
from langchain.tools import tool
from slack_sdk import WebClient

slack_client = WebClient(token=os.environ["SLACK_USER_TOKEN"])
channel = "C0123456ABC"

@tool(parse_docstring=True)
def slack_send_message(text: str, file_path: str | None = None) -> str:
    """Send message, optionally including attachments such as images.

    Args:
        text: (str) text content of the message
        file_path: (str) file path of attachment in the filesystem.
    """
    if not file_path:
        slack_client.chat_postMessage(channel=channel, text=text)
    else:
        fp = backend.download_files([file_path])
        slack_client.files_upload_v2(channel=channel, content=fp[0].content, initial_comment=text)
    return "Message sent."

# --- Assembly and run ----------------------------------------
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
