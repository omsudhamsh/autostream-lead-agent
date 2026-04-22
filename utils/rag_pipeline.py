import os
import json
from dotenv import load_dotenv

# 🔹 Updated: LangChain modules moved to core and community packages
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from google import genai as google_genai

# load env
load_dotenv()
client = google_genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


# 🔹 Custom Gemini Embeddings Wrapper
class GeminiEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [self.embed_query(text) for text in texts]

    def embed_query(self, text):
        response = client.models.embed_content(
            model="gemini-embedding-001", 
            contents=text
        )
        return response.embeddings[0].values


# 🔹 Load Knowledge Base
def load_knowledge():
    with open("data/knowledge.json", "r") as f:
        data = json.load(f)

    documents = []

    # convert JSON into text chunks
    documents.append(
        f"Basic Plan costs {data['pricing']['basic']['price']} with "
        f"{data['pricing']['basic']['videos']} at {data['pricing']['basic']['resolution']} resolution."
    )

    documents.append(
        f"Pro Plan costs {data['pricing']['pro']['price']} with "
        f"{data['pricing']['pro']['videos']} at {data['pricing']['pro']['resolution']} "
        f"and includes {', '.join(data['pricing']['pro']['features'])}."
    )

    documents.append(
        f"Refund policy: {data['policies']['refund']}."
    )

    documents.append(
        f"Support policy: {data['policies']['support']}."
    )

    return documents


# 🔹 Create Vector Store
def create_vectorstore():
    docs = load_knowledge()
    embeddings = GeminiEmbeddings()

    vectorstore = FAISS.from_texts(docs, embeddings)
    return vectorstore


# 🔹 Retrieve Answer
def retrieve_answer(query):
    vectorstore = create_vectorstore()

    results = vectorstore.similarity_search(query, k=2)

    context = "\n".join([doc.page_content for doc in results])

    return context