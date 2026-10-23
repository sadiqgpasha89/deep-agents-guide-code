# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XII: Interview Preparation
# Chapter 76: Spot the Bug
# Section: B14. The Slack form that posts twice
# Snippet 14 of this chapter.

@tool
async def ask_refund_approval(order_id: str, runtime):
    await post_block_kit_card(runtime, order_id)           # posts an approve/reject card
    answer = interrupt({"correlation": make_id(), "order": order_id})
    return answer
