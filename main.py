import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
  if(len(sys.argv) < 2):
    print("No prompt was provided, exiting program.")
    exit(1)
  user_prompt = sys.argv[1]
  verbose = False
  if(len(sys.argv) > 2 and sys.argv[2] == "--verbose"):
    verbose = True

  messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
  ]

  load_dotenv()
  api_key = os.environ.get("GEMINI_API_KEY")

  client = genai.Client(api_key=api_key)
  response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

  if(verbose):
    print(f"User prompt: {response.text}Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
  else:
    print(response.text)

if __name__ == "__main__":
    main()
