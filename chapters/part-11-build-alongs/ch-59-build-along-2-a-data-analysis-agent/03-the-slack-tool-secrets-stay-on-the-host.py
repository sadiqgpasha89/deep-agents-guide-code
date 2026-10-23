# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 59: Build-Along 2: A Data Analysis Agent
# Section: The Slack tool (secrets stay on the host)
# Snippet 3 of this chapter.

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
