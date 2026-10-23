# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 58: Build-Along 1: A Deep Research Agent
# Section: Running it
# Snippet 3 of this chapter.

from langchain.messages import HumanMessage

result = agent.invoke({"messages": [HumanMessage(
    content="What are the main differences between RAG and fine-tuning for LLM applications?")]})

# or stream tokens with event streaming v3
stream = agent.stream_events(
    {"messages": [HumanMessage(content="Compare Python vs JavaScript for web development")]},
    version="v3")
for message in stream.messages:
    for token in message.text:
        print(token, end="", flush=True)
