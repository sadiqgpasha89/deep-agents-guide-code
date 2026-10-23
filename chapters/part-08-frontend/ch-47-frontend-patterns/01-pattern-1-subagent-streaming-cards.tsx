// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part VIII: Frontend
// Chapter 47: Frontend Patterns
// Section: Pattern 1: Subagent streaming cards
// Snippet 1 of this chapter.

function SubagentCard({ stream, subagent }) {
  const messages = useMessages(stream, subagent);       // scoped to this subagent; subscribes while mounted
  const toolCalls = useToolCalls(stream, subagent);
  const lastAi = [...messages].reverse().find((m) => m.type === "ai");
  return (
    <details open={subagent.status !== "completed"}>   // collapsible
      <summary>
        {subagent.name} <Badge status={subagent.status} /> · {toolCalls.length} tool calls
      </summary>
      <p className={subagent.status === "running" ? "pulse" : ""}>
        {lastAi?.text ?? subagent.output}                {/* fallback to snapshot output */}
      </p>
    </details>
  );
}

// In the message list: attach cards to the turn that spawned them
const byToolCallId = Object.fromEntries(stream.subagents.map((s) => [s.id, s]));
{message.tool_calls?.map((tc) => byToolCallId[tc.id] && <SubagentCard stream={stream} subagent={byToolCallId[tc.id]} />)}
