# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VI: Steering
# Chapter 42: Grading Rubrics (Beta)
# Section: Streaming evaluations
# Snippet 3 of this chapter.

stream = agent.stream_events(input, version="v3", transformers=[CustomTransformer])
# read stream.custom for "rubric_evaluation_start" / "rubric_evaluation_end"
