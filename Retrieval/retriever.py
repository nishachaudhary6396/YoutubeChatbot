from langchain_core.vectorstores import VectorStoreRetriever

from langchain_chroma import Chroma

from embeddings.embedding_generator import load_embedding_model
from utils.logger import get_logger


logger = get_logger(__name__)


CHROMA_PATH = "chroma_db"


def load_vector_store():
    """
    Load existing Chroma vector database.
    """

    logger.info("Loading Chroma vector store...")

    try:
        embedding_model = load_embedding_model()

        vector_store = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embedding_model
        )

        logger.info("Chroma vector store loaded successfully.")

        return vector_store

    except Exception as e:
        logger.exception(f"Failed to load vector store: {e}")
        raise



def get_retriever(
    search_type: str = "similarity",
    k: int = 4
):
    """
    Create and return Chroma retriever.

    Args:
        search_type:
            - similarity
            - mmr
            - similarity_score_threshold

        k:
            Number of documents to retrieve

    Returns:
        Retriever object
    """

    logger.info("Creating retriever...")

    try:

        vector_store = load_vector_store()

        retriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": k
            }
        )

        logger.info("Retriever created successfully.")

        return retriever


    except Exception as e:
        logger.exception(f"Failed to create retriever: {e}")
        raise



if __name__ == "__main__":

    logger.info("Testing Retriever...")

    retriever = get_retriever()

    query = "What is explained in this video?"

    docs = retriever.invoke(query)

    logger.info(f"Retrieved {len(docs)} documents.")

    print("\nRetrieved Documents:\n")

    for i, doc in enumerate(docs, start=1):

        print(f"Document {i}")
        print("-" * 60)

        print(doc.page_content[:500])

        print()