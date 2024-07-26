# sm-webdev-chatbot-task6
Task1: Create a chatbot using openai api
This project shows how to interact with OpenAI's GPT-3.5-turbo model using the latest version of the OpenAI Python client library. 
The script takes user input and generates a response from the model.

## Demo

## Installation
First, ensure you have Python 3.7+ installed. Then, install the OpenAI library:

```sh
pip install openai
```
## Setup
Open Visual Studio Code and paste the following code into a new Python file:

```python
import os
from openai import OpenAI

# Set your OpenAI API key
api_key = "your api key here"
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
```

## Troubleshooting


### Error 1: You tried to access `openai.ChatCompletion.create`, but this method is no longer supported in OpenAI Python library v1.0.0 or later.

**Solution:** Update your code to use the latest method provided by the updated library. The current method to create a chat completion is:

```python
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
```
For more details, see the README at https://github.com/openai/openai-python for the API.

### Error 2: Error Code 429 - You exceeded your current quota, please check your plan and billing details.
**Solution:**  To resolve this, you need to increase your quota by adding to your credit balance:

- Go to [platform.openai.com](https://platform.openai.com)
- Navigate to your profile and Organization section at the right.
- Go to Limits.
- Click on Add to Credit Balance.
- Enter your credit card information and continue.
- 
This will ensure you have sufficient credits to continue using the API.
