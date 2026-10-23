// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part VIII: Frontend
// Chapter 46: Frontend: Overview
// Section: What the SDK exposes
// Snippet 1 of this chapter.

import { useStream } from "@langchain/react";          // package/import: confirm for your SDK version
import type { agent } from "./agent";

function Chat() {
  const stream = useStream<typeof agent>({
    apiUrl: "http://localhost:2024",                    // LangSmith Deployment URL in production
    assistantId: "agent",
  });

  return (
    <>
      {stream.messages.map((m) => <Message key={m.id} message={m} />)}
      <button onClick={() => stream.submit({ messages: [{ type: "human", content: "Research LangGraph" }] })}>
        Send
      </button>
    </>
  );
}
