# Social-to-Lead Agentic Workflow

This project is a conversational AI agent built for a fictional SaaS product, AutoStream. It is designed to engage users in conversation, answer product queries, and convert them into qualified leads.

## Features

* Intent Detection: Identifies whether a user is greeting, asking a product question, or showing high intent to purchase.
* RAG-Based Knowledge Retrieval: Uses FAISS and Gemini Embeddings to answer questions accurately from a local database.
* Multi-Turn Memory: Remembers context and user details across the conversation.
* Lead Qualification Flow: Systematically collects necessary user information.
* Controlled Tool Execution: Uses a mock API to capture the lead only after all required data is gathered.

## Architecture Overview

Instead of a basic chatbot script, this project uses LangGraph to create a structured workflow. The system processes user input through a series of defined states:

1. Intent Node: Classifies what the user wants to achieve.
2. Routing Logic: Directs the conversation flow based on the identified intent.
3. RAG Node: Fetches accurate answers from the local knowledge base.
4. Lead Collection Node: Prompts the user for details step-by-step.
5. Tool Node: Executes the lead capture once all inputs are provided.

LangGraph allows for explicit control over these transitions, ensuring predictable behavior. The agent maintains a shared state dictionary to remember details like the user's name, email, and preferred platform across multiple messages.

## Tech Stack

* Python 3.10+
* LangChain & LangGraph
* Google Gemini (1.5 Flash)
* FAISS (Vector Store)
* JSON Knowledge Base

## How to Run

Clone the repository and set up your virtual environment:

    git clone <your-repo-link>
    cd social-to-lead-agent

    python -m venv venv
    source venv/Scripts/activate

    pip install -r requirements.txt

Create a `.env` file in the root directory:

    GOOGLE_API_KEY=your_api_key_here

Run the project:

    python main.py

## Sample Flow

User: Hi
Agent: Hello!

User: Tell me about pricing
Agent: [RAG response explaining pricing]

User: I want the Pro plan
Agent: Can I have your name?

User: Om
Agent: Please provide your email

User: om@gmail.com
Agent: Which platform?

User: YouTube
Agent: Lead captured successfully.

## WhatsApp Integration (Concept)

To deploy this agent on WhatsApp for real-time lead capture:

1. Connect to the WhatsApp Business API (via Twilio or Meta Cloud API).
2. Set up a webhook server using Flask or FastAPI.
3. When a message comes in:
   * Pass the message to the LangGraph agent.
   * Retrieve the generated response.
   * Send the response back to the user via the API.
4. Maintain session state using Redis or a standard database to support multiple users.

## Demo

[Attach your 2–3 minute screen recording here]

## Notes

This project serves as a demonstration of practical agent design, controlled tool execution, retrieval-augmented generation (RAG), and multi-turn reasoning.