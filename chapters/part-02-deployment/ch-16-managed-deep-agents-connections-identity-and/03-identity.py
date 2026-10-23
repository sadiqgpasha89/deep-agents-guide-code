# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 16: Managed Deep Agents: Connections, Identity and the Runtime
# Section: Identity
# Snippet 3 of this chapter.

# identity.py: API key (default)
identity = define_identity(auth=auth.langsmith_api_key())
# Supabase
identity = define_identity(auth=auth.supabase(project_ref="your-project-ref"))
# Own backend
identity = define_identity(auth="backend")
