import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        client = genai.Client(api_key=api_key)
        flag = sys.argv[2] if len(sys.argv) == 3 else None 
        verbose = True if flag and flag.lstrip('-') == "verbose" else False 
        try:
            user_prompt = sys.argv[1]
            messages = [
                types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages
            )
            if verbose: print(f"User prompt: {user_prompt}")
            print(response.text)
            
            if verbose:
                metadata = response.usage_metadata
                print("Prompt tokens:",metadata.prompt_token_count)
                print("Response tokens:", metadata.candidates_token_count)
        except Exception as e:
            print(f"Something went woron.%n{e}")
            sys.exit(1)
    else:
        sys.exit(1)
