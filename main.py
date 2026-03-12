import json
import time
from openai import OpenAI
from openai import RateLimitError

from config import GEMINI_API_KEY
from schemas import tools_schema
from tools import get_stock_price, get_exchange_rate


# AI Model
MODEL = "gemini-3.1-flash-lite-preview"

# AI Client
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Aivalable functions for the AI Agent
available_functions = {
    "get_stock_price": get_stock_price,
    "get_exchange_rate": get_exchange_rate
}

# History and initialization of the chat
messages = [
    {
        "role": "system",
        "content": "You are a Financial Assistant that helps with stock prices and currency exchange rates."
    }
]

def safe_llm_call(client, **kwargs):
    """
    To prevent error with free version of Gemini when too many questions are sent.
    It will automatically wait if the limit has been reached and send again the question.
    """
    
    # Waiting time before new AI call
    delay = 10

    while True:
        try:
            return client.chat.completions.create(**kwargs)

        except RateLimitError:
            print(f"Rate limit reached. Retrying in {delay}s...")
            time.sleep(delay)
            delay = min(delay*2, 60)


def run_agent():
    print("=== Financial Assistant CLI ===")
    print("Agent Started. Type 'exit' to quit.")
    print()

    while True:

        user_input = input("User:  ")

        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({
            "role": "user",
            "content": user_input
        })

        while True:

            # Send the user question and chat history to the AI
            response = safe_llm_call(
                client,
                model=MODEL,
                messages=messages,
                tools=tools_schema
            )

            # The AI response message
            message = response.choices[0].message

            # No tools calls
            if not message.tool_calls:
                messages.append({
                    "role": "assistant",
                    "content": message.content
                })

                print("Agent: " + str(message.content))
                print()
                break

            tool_calls = message.tool_calls

            messages.append(message)

            tool_results = []

            # Executes tool calls
            for tool_call in tool_calls:

                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                function = available_functions[function_name]

                result = function(**function_args)

                tool_results.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

            # Append messages in an history list
            messages.extend(tool_results)


if __name__ == "__main__":
    run_agent()