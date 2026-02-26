import os
from dotenv import load_dotenv

load_dotenv()


def get_groq_api_key():
    """Get Groq API key from environment variables"""
    return os.getenv("GROQ_API_KEY")


def get_google_api_key():
    """Get Google API key from environment variables"""
    return os.getenv("GOOGLE_API_KEY")


def get_openai_api_key():
    """Get OpenAI API key from environment variables"""
    return os.getenv("OPENAI_API_KEY")
