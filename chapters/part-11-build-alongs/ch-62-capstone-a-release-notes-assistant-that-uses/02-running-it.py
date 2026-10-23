# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 62: Capstone: A Release-Notes Assistant that Uses Every Layer
# Section: Running it
# Snippet 2 of this chapter.

rubric = """- The notes start with a version header (## vX.Y.Z)
- The notes contain a 'Breaking changes' section, or say 'None'
- Every claim links to a PR or issue
"""
cfg = {"configurable": {"thread_id": "release-2.4"}}
state = {"messages": [{"role": "user", "content": "Draft and publish notes for v2.4"}], "rubric": rubric}

result = agent.invoke(state, cfg)
if result.get("__interrupt__"):                         # (5) a human decides
    reqs = result["__interrupt__"][0].value["action_requests"]
    decisions = [{"type": "approve"} for _ in reqs]      # one decision per request, same order
    result = agent.invoke(Command(resume={"decisions": decisions}), cfg)
print(result.get("_rubric_status"))                      # (6) satisfied / max_iterations_reached
