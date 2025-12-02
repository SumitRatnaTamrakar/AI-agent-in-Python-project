import os
from dotenv import load_dotenv
from google import genai
import argparse

def main():
    print("Hello from ai-agent-in-python-project!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    args = parser.parse_args()

# Now we can access `args.prompt`
    response = client.models.generate_content(
        # model='gemini-2.0-flash-001'  # --> This model offers a generous free-tier
        model='gemini-2.5-flash',       # This specific model was required to pass the test case on boot.dev
        # contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        contents=args.prompt
    )

    print(response.text)

    if response.usage_metadata is None:
        raise RuntimeError("No usage metadata received")

    # print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    # print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:" ,response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()



