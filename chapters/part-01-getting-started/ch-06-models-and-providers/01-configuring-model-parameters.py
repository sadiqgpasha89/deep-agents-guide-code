# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 6: Models and Providers
# Section: Configuring model parameters
# Snippet 1 of this chapter.

from langchain.chat_models import init_chat_model
model = init_chat_model(model="google_genai:gemini-3.6-flash", thinking_level="medium")
agent = create_deep_agent(model=model)
