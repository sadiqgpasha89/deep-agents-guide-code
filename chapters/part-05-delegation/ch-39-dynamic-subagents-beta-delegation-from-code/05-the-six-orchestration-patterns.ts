// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part V: Delegation
// Chapter 39: Dynamic Subagents (Beta): Delegation from Code
// Section: The six orchestration patterns
// Snippet 5 of this chapter.

const verdicts = await Promise.all(findings.map((f) =>
  task({ description: `Verify ${f.file}:${f.line}`, subagentType: "verifier", responseSchema: verdictSchema })));
const confirmed = findings.filter((_, i) => verdicts[i]?.confirmed);
