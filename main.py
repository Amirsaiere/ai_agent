import os
from dotenv import load_dotenv
from google import genai
import argparse


def main():
    load_dotenv()
    API_KEY = os.environ.get("GEMINI_API_KEY")
    if not API_KEY:
        raise RuntimeError("API Key not found")


    client = genai.Client(api_key=API_KEY)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()


    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=args.user_prompt
    )
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)


if __name__ == "__main__":
    main()
