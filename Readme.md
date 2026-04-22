# 🚀 Social-to-Lead Agentic Workflow

This project is a GenAI-powered conversational agent built for a fictional SaaS product **AutoStream**, designed to convert user conversations into qualified leads.

---

## 🎯 Features

* ✅ Intent Detection (Greeting, Product Query, High Intent)
* ✅ RAG-based Knowledge Retrieval (FAISS + Gemini Embeddings)
* ✅ Multi-turn Conversation Memory (LangGraph State)
* ✅ Lead Qualification Flow
* ✅ Controlled Tool Execution (Mock API)

---

## 🧠 Architecture Overview

This project uses **LangGraph** to design a structured agent workflow instead of a simple chatbot.

The system follows a state-driven approach where each user input is processed through nodes:

1. **Intent Node** → Classifies user intent using Gemini
2. **Routing Logic** → Directs flow based on intent
3. **RAG Node** → Retrieves accurate answers from local knowledge base
4. **Lead Collection Node** → Collects user details step-by-step
5. **Tool Node** → Executes lead capture only after all inputs are collected

LangGraph enables explicit control over transitions, ensuring reliable and predictable agent behavior. State is maintained across multiple turns using a shared dictionary, allowing the agent to remember user inputs like name, email, and platform.

---

## ⚙️ Tech Stack

* Python 3.10+
* LangChain + LangGraph
* Google Gemini (1.5 Flash)
* FAISS (Vector Store)
* JSON Knowledge Base

---

## ▶️ How to Run

```bash
git clone <your-repo-link>
cd social-to-lead-agent

python -m venv venv
source venv/Scripts/activate

pip install -r requirements.txt
```

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

Run the project:

```bash
python main.py
```

---

## 🧪 Sample Flow

```
User: Hi
Agent: Hello!

User: Tell me about pricing
Agent: (RAG response)

User: I want Pro plan
Agent: Can I have your name?

User: Om
Agent: Please provide your email

User: om@gmail.com
Agent: Which platform?

User: YouTube
Agent: ✅ Lead captured
```

---

## 📲 WhatsApp Integration (Concept)

To deploy this agent on WhatsApp:

1. Use **WhatsApp Business API (via Twilio or Meta Cloud API)**
2. Set up a webhook server (Flask/FastAPI)
3. On incoming message:

   * Pass message to LangGraph agent
   * Get response
   * Send response back via API
4. Maintain session state using:

   * Redis / Database (for scaling)

This enables real-time conversational lead capture from WhatsApp users.

---

## 🎥 Demo

(Attach your 2–3 minute screen recording here)

---

## 📌 Notes

This project demonstrates:

* Real-world agent design
* Controlled tool execution
* Retrieval-based responses
* Multi-turn reasoning
