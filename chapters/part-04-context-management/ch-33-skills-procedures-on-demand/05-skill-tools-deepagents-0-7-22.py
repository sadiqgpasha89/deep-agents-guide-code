# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IV: Context Management
# Chapter 33: Skills: Procedures on Demand
# Section: Skill tools (`deepagents>=0.7.22`)
# Snippet 5 of this chapter.

from deepagents.middleware.skills import SkillsMiddleware   # import path: confirm for your version

SkillsMiddleware(backend=backend, sources=["/skills/"], tools=[list_issues, create_issue])
# or tools=resolver, where resolver: (name: str, runtime: Runtime) -> list[BaseTool]
