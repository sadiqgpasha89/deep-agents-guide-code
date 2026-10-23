// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part V: Delegation
// Chapter 39: Dynamic Subagents (Beta): Delegation from Code
// Section: The six orchestration patterns
// Snippet 6 of this chapter.

const candidates = await Promise.all(Array.from({ length: 5 }, () =>
  task({ description: "Propose a design", subagentType: "designer" })));
const scores = await Promise.all(candidates.map((c) =>
  task({ description: `Score: ${c}`, subagentType: "judge", responseSchema: scoreSchema })));
const best = candidates[scores.indexOf(Math.max(...scores.map(s => s.value)))];
