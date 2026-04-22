import os
from groq import Groq
from dotenv import load_dotenv

# load env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_intent(user_input: str) -> str:
    """
    Classifies user input into:
    - greeting
    - product_query
    - high_intent
    """

    prompt = f"""
    You are an intent classification system.

    Classify the user input into ONE of these categories:
    1. greeting
    2. product_query
    3. high_intent

    Rules:
    - greeting: hello, hi, hey
    - product_query: asking about pricing, features, policies
    - high_intent: user wants to buy, subscribe, try, or shows strong interest

    Output ONLY one word:
    greeting OR product_query OR high_intent

    User Input: "{user_input}"
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        intent = completion.choices[0].message.content.strip().lower()

        # safety cleanup
        if "greeting" in intent:
            return "greeting"
        elif "product" in intent:
            return "product_query"
        elif "high" in intent:
            return "high_intent"
        else:
            return "product_query"  # fallback

    except Exception as e:
        print("Intent classification error:", e)
        return "product_query"