// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part XII: Interview Preparation
// Chapter 66: Interview Questions: Sandboxes, Interpreters and Streaming
// Section: Q31. What is programmatic tool calling, and what is its security model?
// Snippet 1 of this chapter.

const results = await Promise.all(
  topics.map((t) => tools.webSearch({ query: `${t} best practices` })),
);
return results.map((r) => r.title);
