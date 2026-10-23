# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part VII: Middleware
# Chapter 45: Custom Middleware
# Section: Practical patterns
# Snippet 4 of this chapter.

# Dynamic system prompt: rebuild the system message per call
from langchain.messages import SystemMessage

@wrap_model_call
def add_context(request: ModelRequest, handler):
    new = SystemMessage(content=[*request.system_message.content_blocks,
                                 {"type": "text", "text": "Today's focus: billing."}])
    return handler(request.override(system_message=new))

# Dynamic model selection
@wrap_model_call
def pick_model(request, handler):
    model = big_model if len(request.messages) > 10 else small_model
    return handler(request.override(model=model))

# Dynamic tool selection: filter request.tools (all tools must be registered up front)
@wrap_model_call
def only_read_tools(request, handler):
    return handler(request.override(tools=[t for t in request.tools if t.name.startswith("read_")]))

# Tool monitoring
@wrap_tool_call
def monitor(request, handler):
    print("calling", request.tool_call["name"], request.tool_call["args"])
    try:
        out = handler(request); print("ok"); return out
    except Exception as e:
        print("error", e); raise

# Anthropic prompt caching: append {"type": "text", ..., "cache_control": {"type": "ephemeral"}} to the system message
