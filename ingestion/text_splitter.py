from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.transcript_loader import get_video_transcript
from utils.logger import get_logger

logger = get_logger(__name__)


def split_text(transcript: str):
    """
    Splits the transcript into smaller chunks.
    """

    logger.info("Splitting transcript into chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.create_documents([transcript])

    logger.info(f"Created {len(chunks)} chunks.")

    return chunks

if __name__ == "__main__":

    video_id = "90lLQVZe2Nc"

    transcript = get_video_transcript(video_id)

    chunks = split_text(transcript)

    print(f"Total Chunks: {len(chunks)}")

    print(chunks[0].page_content)