# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 17: Managed Deep Agents: Channels and Agent-Owned Interrupts
# Section: The Slack channel
# Snippet 1 of this chapter.

# channels/slack.py
from managed_deepagents import channels

channel = channels.slack(
    name="Orders Helper",
    description="Answers questions about order status and returns",
    icon="orders-helper.png",          # 512x512 PNG, <= 1 MB, relative to channels/
    background_color="#0f766e",
)
