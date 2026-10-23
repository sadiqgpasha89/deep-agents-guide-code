# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VI: Steering
# Chapter 41: Human-in-the-Loop: Approvals and Interrupts
# Section: Filesystem permission interrupts (`deepagents>=0.6.8`)
# Snippet 5 of this chapter.

from deepagents import FilesystemPermission
FilesystemPermission(operations=["write"], paths=["/secrets/**"], mode="interrupt")
