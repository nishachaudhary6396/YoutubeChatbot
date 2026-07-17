import os
from dotenv import load_dotenv

from langchain_cohere import CohereEmbeddings

from utils.logger import get_logger

load_dotenv()

logger = get_logger(__name__)


def load_embedding_model():
    """
    Loads the Cohere embedding model.
    """

    logger.info("Loading Cohere Embedding Model...")

    embeddings = CohereEmbeddings(
        model="embed-english-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )

    logger.info("Embedding model loaded successfully.")

    return embeddings


if __name__ == "__main__":

    embedding_model = load_embedding_model()

    sample_text = "LangChain is a framework for building LLM applications."

    embedding = embedding_model.embed_query(sample_text)

    print(f"Embedding Dimension: {len(embedding)}")

    print("\nFirst 10 values:\n")

    print(embedding[:10])