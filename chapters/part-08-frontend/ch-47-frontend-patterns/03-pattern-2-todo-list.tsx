// Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
// Part VIII: Frontend
// Chapter 47: Frontend Patterns
// Section: Pattern 2: Todo list
// Snippet 3 of this chapter.

const STATUS = {
  pending:     { icon: "○", cls: "text-gray-500" },
  in_progress: { icon: "●", cls: "text-amber-500 animate-pulse" },
  completed:   { icon: "✓", cls: "text-green-600 line-through" },
} as const;

function TodoList({ stream }) {
  const todos = stream.values?.todos ?? [];
  if (todos.length === 0) return null;                     // empty state: hide or show "creating a plan..."
  const done = todos.filter((t) => t.status === "completed").length;
  const pct = Math.round((done / todos.length) * 100);
  return (
    <section>
      <h4>{done}/{todos.length} · {pct}%</h4><progress value={pct} max={100} />
      {todos.map((t) => <div key={t.id ?? t.content} className={STATUS[t.status].cls}>{STATUS[t.status].icon} {t.content}</div>)}
    </section>
  );
}
