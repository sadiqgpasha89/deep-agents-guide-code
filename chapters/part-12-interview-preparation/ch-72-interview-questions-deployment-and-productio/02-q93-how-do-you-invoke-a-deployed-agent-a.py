# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 72: Interview Questions: Deployment and Production
# Section: Q93. How do you invoke a deployed agent, and why does production code use async?
# Snippet 2 of this chapter.

client = get_client(url="https://my-deployment", api_key="...")
thread = await client.threads.create()      # new conversation; reuse thread_id for follow-ups

async for chunk in client.runs.stream(
    thread["thread_id"], "agent",
    input={"messages": [{"role": "user", "content": "hi"}]},
    context={"user_id": "u1"},
    stream_mode="updates",
):
    print(chunk)
