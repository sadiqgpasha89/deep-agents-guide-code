// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part V: Delegation
// Chapter 39: Dynamic Subagents (Beta): Delegation from Code
// Section: The six orchestration patterns
// Snippet 7 of this chapter.

let pool = candidates;
while (pool.length > 1) {
  const next = [];
  for (let i = 0; i < pool.length; i += 2) {
    if (i + 1 === pool.length) { next.push(pool[i]); continue; }
    const v = await task({ description: `Which is better?\nA: ${pool[i]}\nB: ${pool[i+1]}`,
                           subagentType: "judge", responseSchema: pickSchema });
    next.push(v.winner === "A" ? pool[i] : pool[i + 1]);
  }
  pool = next;
}
