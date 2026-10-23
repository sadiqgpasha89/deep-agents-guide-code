# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 14: Managed Deep Agents: Durable Memory
# Section: Enabling it
# Snippet 1 of this chapter.

# memory.py: agent layer only (the tutorial's form)
from managed_deepagents import MemoryLayer, define_memory
memory = define_memory(agent=MemoryLayer())

# memory.py: both layers
memory = define_memory(agent=MemoryLayer(), user=MemoryLayer())
