# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 17: Managed Deep Agents: Channels and Agent-Owned Interrupts
# Section: The HTTP channel
# Snippet 2 of this chapter.

# channels/orders.py
from managed_deepagents import channels
from lib.orders import parse, verify

channel = channels.http(provider="orders", verify=verify, parse=parse)
