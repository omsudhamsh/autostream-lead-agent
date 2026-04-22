# ✅ 1. Imports
from typing import TypedDict, Optional
from utils.intent_classifier import classify_intent
from utils.rag_pipeline import retrieve_answer
from tools.lead_capture import mock_lead_capture


# ✅ 2. State Definition
class AgentState(TypedDict):
    user_input: str
    intent: Optional[str]
    response: Optional[str]

    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]

    collecting_lead: Optional[bool]


# ✅ 3. Nodes

# 🔹 Intent Node
def intent_node(state: AgentState):
    # ✅ if already collecting → skip intent detection
    if state.get("collecting_lead"):
        return state

    intent = classify_intent(state["user_input"])
    state["intent"] = intent

    # ✅ activate lead flow
    if intent == "high_intent":
        state["collecting_lead"] = True

    return state


# 🔹 Greeting Node
def greeting_node(state: AgentState):
    state["response"] = "Hello! How can I help you with AutoStream today?"
    return state


# 🔹 RAG Node
def rag_node(state: AgentState):
    context = retrieve_answer(state["user_input"])

    state["response"] = f"""
Here’s what I found for you 👇

{context}

Let me know if you’d like help choosing the right plan 😊
"""
    return state


# 🔹 Lead Collection Node
import re

def lead_collection_node(state: AgentState):
    if not state.get("name"):
        state["response"] = "Great! Can I have your name?"
        return state

    elif not state.get("email"):
        state["response"] = "Please provide your email."
        return state

    elif not state.get("platform"):
        state["response"] = "Which platform do you create content on? (YouTube/Instagram)"
        return state

    return state


# 🔹 Tool Node
def tool_node(state: AgentState):
    if state.get("name") and state.get("email") and state.get("platform"):
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["response"] = "✅ You're all set! Our team will reach out soon."

        # ✅ reset lead flow
        state["collecting_lead"] = False

    return state