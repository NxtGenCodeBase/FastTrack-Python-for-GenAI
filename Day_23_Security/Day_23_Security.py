import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

# How to securely access your OpenAI/Anthropic keys
api_key = os.getenv("AI_API_KEY")
print(f"API Key Loaded: {api_key[:5]}...")
