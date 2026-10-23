# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 24: Fault Tolerance
# Section: Rate limiting
# Snippet 1 of this chapter.

from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain.chat_models import init_chat_model

limiter = InMemoryRateLimiter(
    requests_per_second=0.5,        # target request rate
    check_every_n_seconds=0.1,      # how often to check whether a request is allowed
    max_bucket_size=5,              # maximum burst
)
model = init_chat_model("anthropic:claude-sonnet-4-6", rate_limiter=limiter)
