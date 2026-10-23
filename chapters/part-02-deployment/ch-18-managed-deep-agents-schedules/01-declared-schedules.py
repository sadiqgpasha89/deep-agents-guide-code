# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 18: Managed Deep Agents: Schedules
# Section: Declared schedules
# Snippet 1 of this chapter.

# schedules/daily_digest.py
from managed_deepagents import define_schedule

schedule = define_schedule(
    cron="0 8 * * 1-5",                 # 08:00 on weekdays
    timezone="America/Los_Angeles",     # omit for UTC
    prompt="Write the daily digest.",
)
