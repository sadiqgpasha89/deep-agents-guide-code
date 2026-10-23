# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VI: Steering
# Chapter 41: Human-in-the-Loop: Approvals and Interrupts
# Section: How to configure `interrupt_on`
# Snippet 2 of this chapter.

interrupt_on={
    "execute_sql": {
        "allowed_decisions": ["approve", "reject"],
        "when": lambda request: "drop" in request.tool_call["args"]["query"].lower(),   # only risky queries pause
    },
}
