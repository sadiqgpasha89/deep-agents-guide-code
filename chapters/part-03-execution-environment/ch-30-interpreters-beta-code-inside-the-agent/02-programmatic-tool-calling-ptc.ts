// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part III: Execution Environment
// Chapter 30: Interpreters (Beta): Code Inside the Agent
// Section: Programmatic tool calling (PTC)
// Snippet 2 of this chapter.

const results = await Promise.all(
  topics.map((t) => tools.webSearch({ query: `${t} best practices` })),
);
