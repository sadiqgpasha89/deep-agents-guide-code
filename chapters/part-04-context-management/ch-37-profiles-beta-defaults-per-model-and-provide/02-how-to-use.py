# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 37: Profiles (Beta): Defaults per Model and Provider
# Section: How to use
# Snippet 2 of this chapter.

from deepagents import HarnessProfile, register_harness_profile, GeneralPurposeSubagentProfile  # confirm import paths for your version

register_harness_profile(
    "anthropic:claude-sonnet-4-6",
    HarnessProfile(
        system_prompt_suffix="Prefer concise answers.",
        excluded_tools=frozenset({"glob"}),
        general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=True),
    ),
)
agent = create_deep_agent(model="anthropic:claude-sonnet-4-6")   # profile applied automatically
