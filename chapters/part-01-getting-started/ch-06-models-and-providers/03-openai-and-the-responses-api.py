# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 6: Models and Providers
# Section: OpenAI and the Responses API
# Snippet 3 of this chapter.

from langchain.chat_models import init_chat_model
model = init_chat_model("openai:gpt-5.5", use_responses_api=True, store=False,
                        include=["reasoning.encrypted_content"])
