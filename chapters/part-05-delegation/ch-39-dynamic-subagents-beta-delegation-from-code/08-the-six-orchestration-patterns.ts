// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part V: Delegation
// Chapter 39: Dynamic Subagents (Beta): Delegation from Code
// Section: The six orchestration patterns
// Snippet 8 of this chapter.

const seen = new Set();
while (true) {
  const found = await task({ description: "Find unused exports not in: " + [...seen].join(","),
                             subagentType: "scanner", responseSchema: listSchema });
  const fresh = found.items.filter((x) => !seen.has(x));
  if (fresh.length === 0) break;
  fresh.forEach((x) => seen.add(x));
}
