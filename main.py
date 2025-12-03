import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types

def main():
    print("Hello from ai-agent-in-python-project!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Create a new list of types.Content, and set the user's prompt as the only message (for now):
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# Now we can access `args.prompt`
    response = client.models.generate_content(
        # model='gemini-2.0-flash-001'  # --> This model offers a generous free-tier
        model='gemini-2.5-flash',       # This specific model was required to pass the test case on boot.dev
        # contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        # contents=args.prompt
        contents=messages,
    )

    print(response.text)

    if response.usage_metadata is None:
        raise RuntimeError("No usage metadata received")

    # print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    # print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if args.verbose:
        print("User prompt:", args.user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:" ,response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()



