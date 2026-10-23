# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 69: Interview Questions: Steering with Human-in-the-Loop and Rubrics
# Section: Q62. Walk through the interrupt payload and how you resume.
# Snippet 2 of this chapter.

config = {"configurable": {"thread_id": str(uuid.uuid4())}}   # keep the SAME thread_id
result = agent.invoke({"messages": [...]}, config=config)

if result.get("__interrupt__"):
    payload = result["__interrupt__"][0].value
    decisions = []
    for req in payload["action_requests"]:                    # one decision per request, same order
        if req["name"] == "notify_email":
            decisions.append({"type": "reject", "message": "Do not email anyone yet."})
        else:
            decisions.append({"type": "approve"})
    result = agent.invoke(Command(resume={"decisions": decisions}), config=config)
