// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part V: Delegation
// Chapter 39: Dynamic Subagents (Beta): Delegation from Code
// Section: Setup and the `task()` global
// Snippet 2 of this chapter.

// inside the eval tool
const result = await task({
  description: string,        // the subagent's prompt
  subagentType: string,       // name of a configured subagent
  responseSchema?: object,    // optional JSON schema → typed result (don't JSON.parse it)
});
