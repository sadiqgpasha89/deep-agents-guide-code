# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 34: Memory: What the Agent Always Knows
# Section: Usage patterns
# Snippet 3 of this chapter.

threads = await client.threads.search(metadata={"user_id": "u1"}, limit=5)
history = await client.threads.get_history(thread_id=threads[0]["thread_id"])
