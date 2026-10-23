# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 34: Memory: What the Agent Always Knows
# Section: Usage patterns
# Snippet 4 of this chapter.

await client.crons.create(
    assistant_id="consolidator",
    schedule="0 */6 * * *",                       # UTC! every 6 hours
    input={"messages": [{"role": "user", "content": "Consolidate the last 6 hours of conversations"}]},
)
