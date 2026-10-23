// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part V: Delegation
// Chapter 39: Dynamic Subagents (Beta): Delegation from Code
// Section: The six orchestration patterns
// Snippet 4 of this chapter.

const reviews = await Promise.all(files.map((file) =>
  task({ description: `Review ${file}`, subagentType: "reviewer", responseSchema })));
const summary = await task({ description: `Synthesize: ${JSON.stringify(reviews.flatMap(r => r.issues))}`,
                             subagentType: "synthesizer" });
