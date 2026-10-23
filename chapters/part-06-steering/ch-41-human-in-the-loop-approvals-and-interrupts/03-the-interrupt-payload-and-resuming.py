# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VI: Steering
# Chapter 41: Human-in-the-Loop: Approvals and Interrupts
# Section: The interrupt payload and resuming
# Snippet 3 of this chapter.

import uuid
from langgraph.types import Command

config = {"configurable": {"thread_id": str(uuid.uuid4())}}      # keep the SAME thread_id on resume
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Delete temp.txt and email the team"}]}, config=config
)

if result.get("__interrupt__"):
    payload = result["__interrupt__"][0].value
    # {"action_requests": [{"name": str, "args": dict}, ...],
    #  "review_configs":  [{"action_name": str, "allowed_decisions": [...]}, ...]}
    review = {c["action_name"]: c for c in payload["review_configs"]}

    decisions = []
    for req in payload["action_requests"]:                       # ONE decision per request, SAME order
        if req["name"] == "notify_email":
            decisions.append({"type": "reject", "message": "Don't email anyone yet."})
        else:
            decisions.append({"type": "approve"})
        # edit example:
        # {"type": "edit", "edited_action": {"name": "remove_file", "args": {"path": "/tmp/other.txt"}}}

    result = agent.invoke(Command(resume={"decisions": decisions}), config=config)
