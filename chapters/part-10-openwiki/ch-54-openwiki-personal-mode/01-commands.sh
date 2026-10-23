# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part X: OpenWiki
# Chapter 54: OpenWiki: Personal Mode
# Section: Commands
# Snippet 1 of this chapter.

openwiki personal --init
openwiki personal --update "Refresh the wiki from configured connectors"
openwiki auth notion | gmail | x | slack
openwiki auth configure <provider>       # regenerate connector config from saved env vars
openwiki auth tools <provider>           # list live MCP tools for MCP-backed providers
openwiki ingest all                      # or: ingest web-search / web-search-2
openwiki ngrok start [https://your-domain.ngrok.app]   # HTTPS tunnel for Slack OAuth
openwiki cron list | pause <source|all> | resume <source|all> | delete <source|all>
