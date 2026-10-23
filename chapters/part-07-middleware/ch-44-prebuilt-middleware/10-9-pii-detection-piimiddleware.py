# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: 9. PII detection (`PIIMiddleware`)
# Snippet 10 of this chapter.

middleware=[
    PIIMiddleware("email", strategy="redact", apply_to_input=True),
    PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
]
