# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part X: OpenWiki
# Chapter 53: OpenWiki: Code Mode in Depth
# Section: Commands
# Snippet 1 of this chapter.

openwiki --init
openwiki --update
openwiki code --update --print          # non-interactive, e.g. for CI
openwiki --init --language ko           # BCP-47 locales such as ko, zh-CN, pt-BR
OPENWIKI_PAGE_CONCURRENCY=4 openwiki --update
