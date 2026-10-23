# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part II: Deployment
# Chapter 17: Managed Deep Agents: Channels and Agent-Owned Interrupts
# Section: The HTTP channel
# Snippet 3 of this chapter.

import hashlib, hmac, json, os, uuid

def verify(context) -> bool:                      # context: HttpChannelRequest
    secret = os.environ["ORDERS_WEBHOOK_SECRET"]
    digest = hmac.new(secret.encode(), context.raw_body, hashlib.sha256).hexdigest()
    received = context.request.headers.get("x-orders-signature", "")
    return hmac.compare_digest(f"sha256={digest}", received)

def parse(context):
    event = json.loads(context.raw_body)
    if event.get("type") != "order.comment":
        return {"type": "ignore"}
    return {
        "type": "message",
        "message": {
            "user_id": str(event["actor"]["id"]),
            "thread_id": str(uuid.uuid5(ORDERS_NAMESPACE, str(event["order"]["id"]))),
            "content": event["comment"]["body"],
            "target": str(event["order"]["id"]),
        },
        "raw_event": event,
    }
