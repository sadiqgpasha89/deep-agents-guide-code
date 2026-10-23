# Deep Agents: companion code

Code from **Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)** by Sadiq G Pasha, one file per code block, organised by part and chapter, plus five build-along projects.

> **Unofficial.** This repository is independent. It is not published, sponsored or endorsed by LangChain, Inc. See [NOTICE.md](NOTICE.md).

## What is here

- `chapters/`: every code block in the book (223 blocks, 166 of them runnable Python snippets), in folders that match the book's parts and chapters. The chapter numbers are the ones in the book's contents.
- `build-alongs/`: the five projects from Part XI, assembled from the chapters' code blocks.
- `scripts/`: `check_imports.py` tries every import in the snippets against the packages you installed; `check_json.py` validates the JSON files.

## Quick start

```bash
git clone https://github.com/sadiqgpasha89/deep-agents-guide-code.git
cd deep-agents-guide-code
python -m venv .venv && source .venv/bin/activate     # Python 3.11 or newer is recommended
pip install -r requirements.txt
cp .env.example .env                                   # then add the keys for the chapters you run
```

Optional packages for individual chapters (MCP, ACP, the interpreter, `langgraph dev`) are listed in `requirements-extras.txt`.

## How to use the snippets

- **They are excerpts.** A snippet shows the idea of its section. Many rely on names defined in an earlier snippet of the same chapter, or on placeholders such as `...` and `<backend>`. Read the section in the book first.
- **Checked for syntax, not executed.** Every `.py` and `.json` file parses, and the TypeScript files were transpiled without syntax errors. The snippets were **not** run against live packages or model providers when this repository was prepared. Run `python scripts/check_imports.py` after installing the packages to see where names have drifted; the same check runs in CI and is informational.
- **Top-level `await`.** Some async snippets use `await` at the top level, as in a notebook or an `asyncio` REPL. Put them inside an `async def` and run it with `asyncio.run(...)` in a script.
- **Shell files are command listings.** The `.sh` files list commands to type, some with placeholders such as `<provider>`; they are not meant to run as one script.
- **Signatures are reference only.** Files ending in `.signature.txt` show a function signature from the book; they are not runnable Python.
- **Versions move.** The book describes the documentation as of October 2026. Beta features and version gates change; pin the versions you test against.
- **Keys and cost.** Examples call model providers and other services that need your own keys and may cost money. Keep keys in `.env`; it is git-ignored.

## Build-alongs

| Project | Chapter | Status |
|---|---|---|
| [01-deep-research-agent](build-alongs/01-deep-research-agent) | 58 | Assembled; starter prompts in `prompts.py` |
| [02-data-analysis-agent](build-alongs/02-data-analysis-agent) | 59 | Assembled; needs a LangSmith sandbox and Slack token |
| [03-content-builder-agent](build-alongs/03-content-builder-agent) | 60 | Partial; you write the data files and image tools |
| [04-rag-agent](build-alongs/04-rag-agent) | 61 | Assembled; starter prompt in `prompts.py` |
| [05-capstone-release-notes](build-alongs/05-capstone-release-notes) | 62 | Illustrative; fill in the tools |

## Chapter index

### Part I: Getting Started

| Chapter | Snippets | Folder |
|---|---|---|
| 2. Background: Agents, LangChain and LangGraph | 2 | [`ch-02-background-agents-langchain-and-langgraph`](chapters/part-01-getting-started/ch-02-background-agents-langchain-and-langgraph) |
| 3. Overview: What Deep Agents Is | 1 | [`ch-03-overview-what-deep-agents-is`](chapters/part-01-getting-started/ch-03-overview-what-deep-agents-is) |
| 4. Quickstart: Your First Deep Agent | 5 | [`ch-04-quickstart-your-first-deep-agent`](chapters/part-01-getting-started/ch-04-quickstart-your-first-deep-agent) |
| 5. Customization: Configuring a Deep Agent | 8 | [`ch-05-customization-configuring-a-deep-agent`](chapters/part-01-getting-started/ch-05-customization-configuring-a-deep-agent) |
| 6. Models and Providers | 4 | [`ch-06-models-and-providers`](chapters/part-01-getting-started/ch-06-models-and-providers) |

### Part II: Deployment

| Chapter | Snippets | Folder |
|---|---|---|
| 9. Managed Deep Agents: Overview | 6 | [`ch-09-managed-deep-agents-overview`](chapters/part-02-deployment/ch-09-managed-deep-agents-overview) |
| 10. Managed Deep Agents: Quickstart and Project Structure | 1 | [`ch-10-managed-deep-agents-quickstart-and-project-s`](chapters/part-02-deployment/ch-10-managed-deep-agents-quickstart-and-project-s) |
| 11. Managed Deep Agents: Defining the Agent | 1 | [`ch-11-managed-deep-agents-defining-the-agent`](chapters/part-02-deployment/ch-11-managed-deep-agents-defining-the-agent) |
| 12. Managed Deep Agents: Instructions, Skills and Context Hub | 2 | [`ch-12-managed-deep-agents-instructions-skills-and`](chapters/part-02-deployment/ch-12-managed-deep-agents-instructions-skills-and) |
| 13. Managed Deep Agents: Tools, Middleware and MCP Connectors | 5 | [`ch-13-managed-deep-agents-tools-middleware-and-mcp`](chapters/part-02-deployment/ch-13-managed-deep-agents-tools-middleware-and-mcp) |
| 14. Managed Deep Agents: Durable Memory | 1 | [`ch-14-managed-deep-agents-durable-memory`](chapters/part-02-deployment/ch-14-managed-deep-agents-durable-memory) |
| 15. Managed Deep Agents: Sandboxes | 1 | [`ch-15-managed-deep-agents-sandboxes`](chapters/part-02-deployment/ch-15-managed-deep-agents-sandboxes) |
| 16. Managed Deep Agents: Connections, Identity and the Runtime | 4 | [`ch-16-managed-deep-agents-connections-identity-and`](chapters/part-02-deployment/ch-16-managed-deep-agents-connections-identity-and) |
| 17. Managed Deep Agents: Channels and Agent-Owned Interrupts | 3 | [`ch-17-managed-deep-agents-channels-and-agent-owned`](chapters/part-02-deployment/ch-17-managed-deep-agents-channels-and-agent-owned) |
| 18. Managed Deep Agents: Schedules | 1 | [`ch-18-managed-deep-agents-schedules`](chapters/part-02-deployment/ch-18-managed-deep-agents-schedules) |
| 20. Managed Deep Agents: Exposing the Agent over MCP, and Built-in Search | 4 | [`ch-20-managed-deep-agents-exposing-the-agent-over`](chapters/part-02-deployment/ch-20-managed-deep-agents-exposing-the-agent-over) |
| 21. Managed Deep Agents: Evals and Migration | 2 | [`ch-21-managed-deep-agents-evals-and-migration`](chapters/part-02-deployment/ch-21-managed-deep-agents-evals-and-migration) |
| 22. Tutorial: Extending the Research Assistant with Search, Memory and a Schedule | 5 | [`ch-22-tutorial-extending-the-research-assistant-wi`](chapters/part-02-deployment/ch-22-tutorial-extending-the-research-assistant-wi) |
| 23. Going to Production | 5 | [`ch-23-going-to-production`](chapters/part-02-deployment/ch-23-going-to-production) |
| 24. Fault Tolerance | 4 | [`ch-24-fault-tolerance`](chapters/part-02-deployment/ch-24-fault-tolerance) |

### Part III: Execution Environment

| Chapter | Snippets | Folder |
|---|---|---|
| 25. Tools: The Built-in Toolbox | 2 | [`ch-25-tools-the-built-in-toolbox`](chapters/part-03-execution-environment/ch-25-tools-the-built-in-toolbox) |
| 26. Backends: Where Files Live | 4 | [`ch-26-backends-where-files-live`](chapters/part-03-execution-environment/ch-26-backends-where-files-live) |
| 27. Permissions: Controlling File Access | 2 | [`ch-27-permissions-controlling-file-access`](chapters/part-03-execution-environment/ch-27-permissions-controlling-file-access) |
| 28. Multimodality | 1 | [`ch-28-multimodality`](chapters/part-03-execution-environment/ch-28-multimodality) |
| 29. Sandboxes: Isolated Execution | 2 | [`ch-29-sandboxes-isolated-execution`](chapters/part-03-execution-environment/ch-29-sandboxes-isolated-execution) |
| 30. Interpreters (Beta): Code Inside the Agent | 3 | [`ch-30-interpreters-beta-code-inside-the-agent`](chapters/part-03-execution-environment/ch-30-interpreters-beta-code-inside-the-agent) |
| 31. Event Streaming (Beta) | 1 | [`ch-31-event-streaming-beta`](chapters/part-03-execution-environment/ch-31-event-streaming-beta) |
| 32. Streaming: Watching the Agent Work | 2 | [`ch-32-streaming-watching-the-agent-work`](chapters/part-03-execution-environment/ch-32-streaming-watching-the-agent-work) |

### Part IV: Context Management

| Chapter | Snippets | Folder |
|---|---|---|
| 33. Skills: Procedures on Demand | 5 | [`ch-33-skills-procedures-on-demand`](chapters/part-04-context-management/ch-33-skills-procedures-on-demand) |
| 34. Memory: What the Agent Always Knows | 4 | [`ch-34-memory-what-the-agent-always-knows`](chapters/part-04-context-management/ch-34-memory-what-the-agent-always-knows) |
| 35. Retrieval: Bringing in Outside Knowledge | 1 | [`ch-35-retrieval-bringing-in-outside-knowledge`](chapters/part-04-context-management/ch-35-retrieval-bringing-in-outside-knowledge) |
| 36. Context Engineering: Offloading, Summarization and Isolation | 4 | [`ch-36-context-engineering-offloading-summarization`](chapters/part-04-context-management/ch-36-context-engineering-offloading-summarization) |
| 37. Profiles (Beta): Defaults per Model and Provider | 3 | [`ch-37-profiles-beta-defaults-per-model-and-provide`](chapters/part-04-context-management/ch-37-profiles-beta-defaults-per-model-and-provide) |

### Part V: Delegation

| Chapter | Snippets | Folder |
|---|---|---|
| 38. Subagents: Delegating to Specialists | 4 | [`ch-38-subagents-delegating-to-specialists`](chapters/part-05-delegation/ch-38-subagents-delegating-to-specialists) |
| 39. Dynamic Subagents (Beta): Delegation from Code | 8 | [`ch-39-dynamic-subagents-beta-delegation-from-code`](chapters/part-05-delegation/ch-39-dynamic-subagents-beta-delegation-from-code) |
| 40. Async Subagents: Background Work | 1 | [`ch-40-async-subagents-background-work`](chapters/part-05-delegation/ch-40-async-subagents-background-work) |

### Part VI: Steering

| Chapter | Snippets | Folder |
|---|---|---|
| 41. Human-in-the-Loop: Approvals and Interrupts | 5 | [`ch-41-human-in-the-loop-approvals-and-interrupts`](chapters/part-06-steering/ch-41-human-in-the-loop-approvals-and-interrupts) |
| 42. Grading Rubrics (Beta) | 3 | [`ch-42-grading-rubrics-beta`](chapters/part-06-steering/ch-42-grading-rubrics-beta) |

### Part VII: Middleware

| Chapter | Snippets | Folder |
|---|---|---|
| 43. Middleware: Overview | 2 | [`ch-43-middleware-overview`](chapters/part-07-middleware/ch-43-middleware-overview) |
| 44. Prebuilt Middleware | 21 | [`ch-44-prebuilt-middleware`](chapters/part-07-middleware/ch-44-prebuilt-middleware) |
| 45. Custom Middleware | 4 | [`ch-45-custom-middleware`](chapters/part-07-middleware/ch-45-custom-middleware) |

### Part VIII: Frontend

| Chapter | Snippets | Folder |
|---|---|---|
| 46. Frontend: Overview | 1 | [`ch-46-frontend-overview`](chapters/part-08-frontend/ch-46-frontend-overview) |
| 47. Frontend Patterns | 5 | [`ch-47-frontend-patterns`](chapters/part-08-frontend/ch-47-frontend-patterns) |

### Part IX: Protocols

| Chapter | Snippets | Folder |
|---|---|---|
| 48. ACP: Agent Client Protocol | 3 | [`ch-48-acp-agent-client-protocol`](chapters/part-09-protocols/ch-48-acp-agent-client-protocol) |
| 49. MCP with LangChain | 7 | [`ch-49-mcp-with-langchain`](chapters/part-09-protocols/ch-49-mcp-with-langchain) |
| 50. A2A with LangSmith | 4 | [`ch-50-a2a-with-langsmith`](chapters/part-09-protocols/ch-50-a2a-with-langsmith) |
| 51. AG-UI: Agent User Interaction | 5 | [`ch-51-ag-ui-agent-user-interaction`](chapters/part-09-protocols/ch-51-ag-ui-agent-user-interaction) |

### Part X: OpenWiki

| Chapter | Snippets | Folder |
|---|---|---|
| 52. OpenWiki: Overview and Quickstart | 2 | [`ch-52-openwiki-overview-and-quickstart`](chapters/part-10-openwiki/ch-52-openwiki-overview-and-quickstart) |
| 53. OpenWiki: Code Mode in Depth | 2 | [`ch-53-openwiki-code-mode-in-depth`](chapters/part-10-openwiki/ch-53-openwiki-code-mode-in-depth) |
| 54. OpenWiki: Personal Mode | 1 | [`ch-54-openwiki-personal-mode`](chapters/part-10-openwiki/ch-54-openwiki-personal-mode) |
| 55. OpenWiki: Coding-Agent Integrations, Search and Workspaces | 2 | [`ch-55-openwiki-coding-agent-integrations-search-an`](chapters/part-10-openwiki/ch-55-openwiki-coding-agent-integrations-search-an) |
| 57. OpenWiki: Visualizing and Automating Updates | 2 | [`ch-57-openwiki-visualizing-and-automating-updates`](chapters/part-10-openwiki/ch-57-openwiki-visualizing-and-automating-updates) |

### Part XI: Build-Alongs

| Chapter | Snippets | Folder |
|---|---|---|
| 58. Build-Along 1: A Deep Research Agent | 3 | [`ch-58-build-along-1-a-deep-research-agent`](chapters/part-11-build-alongs/ch-58-build-along-1-a-deep-research-agent) |
| 59. Build-Along 2: A Data Analysis Agent | 4 | [`ch-59-build-along-2-a-data-analysis-agent`](chapters/part-11-build-alongs/ch-59-build-along-2-a-data-analysis-agent) |
| 60. Build-Along 3: A Content Builder Agent | 2 | [`ch-60-build-along-3-a-content-builder-agent`](chapters/part-11-build-alongs/ch-60-build-along-3-a-content-builder-agent) |
| 61. Build-Along 4: Retrieval-Augmented Generation with Deep Agents | 3 | [`ch-61-build-along-4-retrieval-augmented-generation`](chapters/part-11-build-alongs/ch-61-build-along-4-retrieval-augmented-generation) |
| 62. Capstone: A Release-Notes Assistant that Uses Every Layer | 2 | [`ch-62-capstone-a-release-notes-assistant-that-uses`](chapters/part-11-build-alongs/ch-62-capstone-a-release-notes-assistant-that-uses) |

### Part XII: Interview Preparation

| Chapter | Snippets | Folder |
|---|---|---|
| 65. Interview Questions: Tools, Backends and Permissions | 3 | [`ch-65-interview-questions-tools-backends-and-permi`](chapters/part-12-interview-preparation/ch-65-interview-questions-tools-backends-and-permi) |
| 66. Interview Questions: Sandboxes, Interpreters and Streaming | 1 | [`ch-66-interview-questions-sandboxes-interpreters-a`](chapters/part-12-interview-preparation/ch-66-interview-questions-sandboxes-interpreters-a) |
| 68. Interview Questions: Delegation and Subagents | 2 | [`ch-68-interview-questions-delegation-and-subagents`](chapters/part-12-interview-preparation/ch-68-interview-questions-delegation-and-subagents) |
| 69. Interview Questions: Steering with Human-in-the-Loop and Rubrics | 3 | [`ch-69-interview-questions-steering-with-human-in-t`](chapters/part-12-interview-preparation/ch-69-interview-questions-steering-with-human-in-t) |
| 70. Interview Questions: Middleware and Reliability | 1 | [`ch-70-interview-questions-middleware-and-reliabili`](chapters/part-12-interview-preparation/ch-70-interview-questions-middleware-and-reliabili) |
| 72. Interview Questions: Deployment and Production | 2 | [`ch-72-interview-questions-deployment-and-productio`](chapters/part-12-interview-preparation/ch-72-interview-questions-deployment-and-productio) |
| 73. Interview Questions: Managed Deep Agents | 1 | [`ch-73-interview-questions-managed-deep-agents`](chapters/part-12-interview-preparation/ch-73-interview-questions-managed-deep-agents) |
| 76. Spot the Bug | 14 | [`ch-76-spot-the-bug`](chapters/part-12-interview-preparation/ch-76-spot-the-bug) |

### Appendices

| Chapter | Snippets | Folder |
|---|---|---|
| A. Cheat Sheet: Code, Defaults and Decisions | 1 | [`app-A-cheat-sheet-code-defaults-and-decisions`](chapters/appendices/app-A-cheat-sheet-code-defaults-and-decisions) |

## Corrections and updates

Found a mistake or a changed API? Please open an issue.

## Licence

[MIT](LICENSE). Parts adapted from MIT-licensed LangChain material; see [NOTICE.md](NOTICE.md).
