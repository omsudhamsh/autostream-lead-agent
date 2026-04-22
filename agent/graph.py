from langgraph.graph import StateGraph, END
from agent.nodes import (
    AgentState,
    intent_node,
    rag_node,
    greeting_node,
    lead_collection_node,
    tool_node
)


def route_intent(state: AgentState):
    # ✅ if already collecting → stay in lead flow
    if state.get("collecting_lead"):
        return "lead"

    intent = state["intent"]

    if intent == "greeting":
        return "greeting"
    elif intent == "product_query":
        return "rag"
    elif intent == "high_intent":
        return "lead"

    return "rag"


def route_lead(state: AgentState):
    # if missing details → keep asking
    if not state.get("name") or not state.get("email") or not state.get("platform"):
        return "collect"

    return "tool"


def build_graph():
    builder = StateGraph(AgentState)

    # nodes
    builder.add_node("intent", intent_node)
    builder.add_node("greeting", greeting_node)
    builder.add_node("rag", rag_node)
    builder.add_node("collect", lead_collection_node)
    builder.add_node("tool", tool_node)

    # entry
    builder.set_entry_point("intent")

    # routing
    builder.add_conditional_edges(
        "intent",
        route_intent,
        {
            "greeting": "greeting",
            "rag": "rag",
            "lead": "collect",
        }
    )

    builder.add_conditional_edges(
        "collect",
        route_lead,
        {
            "collect": END,
            "tool": "tool",
        }
    )

    # end nodes
    builder.add_edge("greeting", END)
    builder.add_edge("rag", END)
    builder.add_edge("tool", END)

    return builder.compile()