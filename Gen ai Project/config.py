import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # IBM Watsonx Granite LLM settings
    WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
    WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
    WATSONX_BASE_URL = os.getenv("WATSONX_BASE_URL")
    WATSONX_MODEL_ID = os.getenv("WATSONX_MODEL_ID")

    # Pinecone settings
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV = os.getenv("PINECONE_ENV")
    INDEX_NAME = os.getenv("INDEX_NAME")

settings = Settings()
