# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 23: Going to Production
# Section: Guardrails
# Snippet 5 of this chapter.

from langchain.agents.middleware import PIIMiddleware

middleware = [
    PIIMiddleware("email", strategy="redact", apply_to_input=True),        # -> [REDACTED_EMAIL]
    PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),    # -> ****-****-****-1234
]
