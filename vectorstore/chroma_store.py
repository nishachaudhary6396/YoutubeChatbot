from langchain_chroma import Chroma

from embeddings.embedding_generator import load_embedding_model
from ingestion.text_splitter import split_text
from ingestion.transcript_loader import get_video_transcript
from utils.logger import get_logger

logger = get_logger(__name__)


def create_vector_store(video: str):

    logger.info("Loading transcript...")

    transcript = get_video_transcript(video)

    logger.info("Splitting transcript...")

    chunks = split_text(transcript)

    logger.info("Loading embedding model...")

    embedding_model = load_embedding_model()

    logger.info("Creating Chroma Vector Store...")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    logger.info("Vector Store created successfully.")

    return vector_store


if __name__ == "__main__":

    video = "https://www.youtube.com/watch?v=90lLQVZe2Nc"

    vector_store = create_vector_store(video)

    print("\nTotal Documents Stored:")

    print(vector_store._collection.count())