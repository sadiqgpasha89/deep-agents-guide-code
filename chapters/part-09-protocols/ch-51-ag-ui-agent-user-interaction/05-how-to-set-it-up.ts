// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part IX: Protocols
// Chapter 51: AG-UI: Agent User Interaction
// Section: How to set it up
// Snippet 5 of this chapter.

import { LangGraphAgent } from "@ag-ui/langgraph";
const agent = new LangGraphAgent({
  graphId: "agent",                         // must match a key in langgraph.json
  deploymentUrl: "http://localhost:2024",   // change for non-local environments
  // emitInterruptOutcome: true,            // structured interrupt results on RUN_FINISHED
});
agent.subscribe({ onTextMessageContentEvent: ({ event }) => console.log(event.delta) });   // on…Event callbacks (illustrative)
await agent.runAgent({ /* input */ });
