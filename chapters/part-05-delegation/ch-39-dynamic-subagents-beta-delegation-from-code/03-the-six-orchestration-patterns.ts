// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part V: Delegation
// Chapter 39: Dynamic Subagents (Beta): Delegation from Code
// Section: The six orchestration patterns
// Snippet 3 of this chapter.

const labels = await Promise.all(items.map((it) =>
  task({ description: `Classify: ${it}`, subagentType: "classifier", responseSchema: labelSchema })));
const results = await Promise.all(items.map((it, i) =>
  task({ description: `Handle: ${it}`, subagentType: labels[i].category })));   // route to the right specialist
