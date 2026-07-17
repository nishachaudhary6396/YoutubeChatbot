from langchain_mistralai import ChatMistralAI

from config.settings import MODEL_NAME
from utils.logger import get_logger

logger = get_logger(__name__)


def load_llm():
    """
    Loads the Mistral Chat Model.
    """

    logger.info(f"Loading Mistral Model: {MODEL_NAME}")

    try:
        llm = ChatMistralAI(
            model=MODEL_NAME,
            temperature=0,
            max_tokens=1024
        )

        logger.info("Mistral model loaded successfully.")

        return llm

    except Exception as e:
        logger.exception(f"Failed to initialize Mistral LLM: {e}")
        raise


if __name__ == "__main__":

    logger.info("Testing Mistral LLM...")

    llm = load_llm()

    response = llm.invoke("Who is the Prime Minister of India?")

    print(response.content)