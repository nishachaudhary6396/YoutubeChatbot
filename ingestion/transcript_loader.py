from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound
)

from utils.logger import get_logger

logger = get_logger(__name__)


def get_video_transcript(video: str) -> str:
    """
    Fetch transcript from a YouTube video URL or Video ID.
    """

    # If user enters a URL, extract the Video ID
    if "youtube.com" in video or "youtu.be" in video:
        if "v=" in video:
            video = video.split("v=")[1].split("&")[0]
        elif "youtu.be/" in video:
            video = video.split("youtu.be/")[1].split("?")[0]

    logger.info(f"Starting transcript fetch for video: {video}")

    try:
        transcript_data = YouTubeTranscriptApi().fetch(
            video_id=video,
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

    video = input("Enter YouTube URL or Video ID: ")

    transcript = get_video_transcript(video)

    print(transcript[:1000])