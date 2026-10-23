# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 44: Prebuilt Middleware
# Section: 6. Human-in-the-loop (`HumanInTheLoopMiddleware`)
# Snippet 7 of this chapter.

HumanInTheLoopMiddleware(interrupt_on={
    "your_send_email_tool": {"allowed_decisions": ["approve", "edit", "reject"]},
    "your_read_email_tool": False,
})
