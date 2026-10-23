# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 22: Tutorial: Extending the Research Assistant with Search, Memory and a Schedule
# Snippet 5 of this chapter.

from managed_deepagents import define_schedule

schedule = define_schedule(
    cron="0 8 * * 1-5",
    timezone="America/Los_Angeles",
    prompt=("Review durable memory for reusable research rules. "
            "Summarize anything useful, then list open questions for today."),
)
