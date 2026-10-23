# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IX: Protocols
# Chapter 50: A2A with LangSmith
# Section: Distributed tracing
# Snippet 3 of this chapter.

thread_id = body["params"]["message"].get("contextId")
with tracer.start_as_current_span("agent") as span:
    if thread_id:
        span.set_attribute("langsmith.metadata.thread_id", thread_id)
