# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part I: Getting Started
# Chapter 6: Models and Providers
# Section: Provider profiles (construction defaults)
# Snippet 2 of this chapter.

from deepagents import ProviderProfile, register_provider_profile

register_provider_profile("openai", ProviderProfile(init_kwargs={"temperature": 0}))              # every openai model
register_provider_profile("openai:gpt-5.5", ProviderProfile(init_kwargs={"reasoning_effort": "medium"}))  # one model; inherits temperature=0
