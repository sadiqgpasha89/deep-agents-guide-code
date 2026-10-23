# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part IX: Protocols
# Chapter 50: A2A with LangSmith
# Section: Sending messages
# Snippet 1 of this chapter.

curl -X POST "https://your-deployment/a2a/{assistant_id}" \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  -d '{
    "jsonrpc": "2.0", "id": 1, "method": "SendMessage",
    "params": { "message": { "role": "ROLE_USER", "parts": [{"text": "hello"}], "messageId": "test-1" } }
  }'
# response: result.task.id and result.task.contextId  → reuse contextId to continue the conversation

curl "https://your-deployment/a2a/{assistant_id}/.well-known/agent-card.json"     # fetch the Agent Card
