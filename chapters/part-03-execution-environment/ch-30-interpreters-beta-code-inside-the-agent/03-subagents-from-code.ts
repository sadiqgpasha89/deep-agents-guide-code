// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part III: Execution Environment
// Chapter 30: Interpreters (Beta): Code Inside the Agent
// Section: Subagents from code
// Snippet 3 of this chapter.

const reviews = await Promise.all(
  paths.map((path) => task({ description: `Review ${path}`, subagentType: "reviewer" })),
);
