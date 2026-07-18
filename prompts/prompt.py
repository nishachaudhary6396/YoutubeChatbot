from langchain_core.prompts import PromptTemplate

from utils.logger import get_logger

logger = get_logger(__name__)


def get_rag_prompt():
    """
    Returns the prompt template for the YouTube Chatbot.
    """

    logger.info("Loading RAG Prompt...")

    template = """
You are a helpful AI assistant that answers questions based only on the provided YouTube transcript.

Instructions:
- Use only the information from the transcript context.
- Do not use your own knowledge or make up information.
- If the answer is not available in the transcript, respond with:
  "I couldn't find the answer in the provided transcript."
- Keep your answer clear, concise, and easy to understand.
- If the answer contains multiple points, present them as bullet points.

Transcript Context:
{context}

User Question:
{question}

Answer:
"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )

    logger.info("RAG Prompt loaded successfully.")

    return prompt


if __name__ == "__main__":

    prompt = get_rag_prompt()

    formatted_prompt = prompt.format(
        context="""
LangChain is an open-source framework for building applications powered by large language models.
It provides components such as prompt templates, chains, retrievers, and memory.
""",
        question="What is LangChain?"
    )

    print(formatted_prompt)