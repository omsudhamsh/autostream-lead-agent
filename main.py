from agent.graph import build_graph
import re
graph = build_graph()

# memory state
state = {
    "name": None,
    "email": None,
    "platform": None,
    "intent": None,
    "response": None,
    "collecting_lead": False
}

print("🤖 AutoStream AI Agent (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        print("Agent: Please enter something so I can help you 🙂")
        continue

    if user_input.lower() == "exit":
        break

    state["user_input"] = user_input

    # 🧠 Logic to capture details based on active collection
    # If the last response asked for name/email/platform, save the next input
    last_response = state.get("response", "")
    if last_response == "Great! Can I have your name?":
        state["name"] = user_input
    elif last_response == "Please provide your email.":
        if re.match(r"[^@]+@[^@]+\.[^@]+", user_input):
            state["email"] = user_input
        else:
            print("Agent: ❌ Please enter a valid email address.")
            continue
    elif last_response == "Which platform do you create content on? (YouTube/Instagram)":
        state["platform"] = user_input

    # 🚀 Run LangGraph
    state = graph.invoke(state)

    print("Agent:", state.get("response"))

    # 🔹 Reset state after lead capture tool node finishes
    if state.get("response") == "✅ You're all set! Our team will reach out soon.":
        state["name"] = None
        state["email"] = None
        state["platform"] = None
        state["intent"] = None
        state["response"] = None