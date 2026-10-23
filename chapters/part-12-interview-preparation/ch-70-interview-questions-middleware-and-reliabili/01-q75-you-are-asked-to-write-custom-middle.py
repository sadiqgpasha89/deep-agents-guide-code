# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 70: Interview Questions: Middleware and Reliability
# Section: Q75. You are asked to write custom middleware. What are the patterns and pitfalls?
# Snippet 1 of this chapter.

@wrap_model_call
def pick_model(request, handler):
    model = big_model if len(request.messages) > 10 else small_model
    return handler(request.override(model=model))
