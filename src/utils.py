import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


def get_model():
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
return genai.GenerativeModel("gemini-1.5-flash")
