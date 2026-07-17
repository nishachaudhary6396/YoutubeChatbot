import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Mistral LLM
MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "mistral-small-latest"
)

# Cohere Embedding Model
EMBED_MODEL = os.getenv(
    "EMBED_MODEL",
    "embed-english-v3.0"
)

# Chroma Database
VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "chroma_db"
)