# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VI: Steering
# Chapter 42: Grading Rubrics (Beta)
# Section: How to use
# Snippet 1 of this chapter.

from deepagents import RubricMiddleware, create_deep_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

def on_eval(ev):                                   # observability only; errors here are swallowed
    print(ev.iteration, ev.result, ev.explanation)

agent = create_deep_agent(
    model="google_genai:gemini-3.6-flash",
    middleware=[
        RubricMiddleware(
            model="anthropic:claude-haiku-4-5",    # grader: often a smaller/cheaper model
            max_iterations=3,
            tools=None,                            # give the grader tools (e.g. run tests) to gather evidence
            on_evaluation=on_eval,
        ),
    ],
    checkpointer=InMemorySaver(),
)

rubric = """- The answer is one sentence
- The answer includes a source URL
"""
result = agent.invoke(
    {"messages": [HumanMessage("What is LangGraph?")], "rubric": rubric},
    config={"configurable": {"thread_id": "t1"}},
)
print(result.get("_rubric_status"))                # e.g. satisfied / max_iterations_reached
