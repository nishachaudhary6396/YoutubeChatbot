from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound
)

from utils.logger import get_logger

logger = get_logger(__name__)


def get_video_transcript(video_id: str) -> str:
    

    logger.info(f"Starting transcript fetch for video: {video_id}")

    try:
        transcript_data = YouTubeTranscriptApi().fetch(
            video_id=video_id,
            languages=["en", "hi"]
        )

        transcript = " ".join(
            segment.text for segment in transcript_data
        )

        logger.info("Transcript downloaded successfully.")
        logger.info(f"Total characters: {len(transcript)}")

        return transcript

    except NoTranscriptFound:
        logger.error("No transcript found for this video.")
        raise

    except TranscriptsDisabled:
        logger.error("Transcript is disabled for this video.")
        raise

    except Exception as error:
        logger.exception(f"Error while fetching transcript: {error}")
        raise


if __name__ == "__main__":

    video_id = "90lLQVZe2Nc"

    transcript = get_video_transcript(video_id)

    print(transcript[:1000])