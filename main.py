import os
from openai import OpenAI

# Set your OpenAI API key
api_key = "add ypur api-key here"
os.environ["OPENAI_API_KEY"] = api_key

client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    try:
        # Create a chat completion request
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        # Access and return the response content directly
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        # Print any error that occurs
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
