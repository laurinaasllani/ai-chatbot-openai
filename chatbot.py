from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatbot(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Answer clearly and briefly."},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"AI service is currently unavailable. Error: {e}"


print("AI Chatbot with OpenAI API")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    answer = ask_chatbot(user_input)
    print("Chatbot:", answer)