# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VI: Steering
# Chapter 41: Human-in-the-Loop: Approvals and Interrupts
# Section: In-tool interrupts (custom, free-form)
# Snippet 4 of this chapter.

from langgraph.types import interrupt, Command
from langchain.tools import tool

@tool
def transfer_funds(amount: float, to: str) -> str:
    """Transfer money."""
    approval = interrupt({"type": "approval_request", "amount": amount, "to": to})   # returns the resume value
    return "sent" if approval.get("approved") else "cancelled"

agent.invoke(Command(resume={"approved": True}), config=config)     # arbitrary payload, NOT {"decisions": ...}
