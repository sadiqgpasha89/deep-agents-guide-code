# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 5: Customization: Configuring a Deep Agent
# Section: Model
# Snippet 2 of this chapter.

from langchain.chat_models import init_chat_model

agent = create_deep_agent(model="openai:gpt-5.5")                 # string form

model = init_chat_model(model="google_genai:gemini-3.6-flash", thinking_level="medium")
agent = create_deep_agent(model=model)                              # configured instance
