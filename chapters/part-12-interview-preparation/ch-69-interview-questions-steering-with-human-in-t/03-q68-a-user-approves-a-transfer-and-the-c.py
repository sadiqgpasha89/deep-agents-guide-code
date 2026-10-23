# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 69: Interview Questions: Steering with Human-in-the-Loop and Rubrics
# Section: Q68. A user approves a transfer, and the customer is charged twice. What happened?
# Snippet 3 of this chapter.

@tool
def transfer_funds(amount: float, to: str) -> str:
    """Transfer money."""
    approval = interrupt({"type": "approval_request", "amount": amount, "to": to})  # first
    if not approval.get("approved"):
        return "cancelled"
    return pay(amount, to, idempotency_key=...)      # side effect only after approval
