# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 16: Managed Deep Agents: Connections, Identity and the Runtime
# Section: Connections
# Snippet 1 of this chapter.

# opaque secret (always agent-owned)
uv run mda connections create organization-tavily --secret-from-env TAVILY_API_KEY
# catalog OAuth: you supply only client id + secret
uv run mda connections create team-github --oauth github --client-id <ID> --secret-from-env GH_SECRET
uv run mda connections catalog          # list preconfigured services
