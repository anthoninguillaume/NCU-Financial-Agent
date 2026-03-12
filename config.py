import os
from dotenv import load_dotenv

load_dotenv()

# Load the Gemini API key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# No API key, or wrong key name in .env
if not GEMINI_API_KEY:
    raise ValueError("ERROR: Missing GEMINI_API_KEY")