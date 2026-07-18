from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser

from Retrieval.retriever import get_retriever
from prompts.prompt import get_rag_prompt
from llm.model import load_llm
from utils.logger import get_logger

logger = get_logger(__name__)


def combine_documents(documents):
    """
    Combine retrieved documents into a single context string.
    """

    return "\n\n".join(doc.page_content for doc in documents)


def create_rag_chain(retriever):
    """
    Creates and returns the complete RAG pipeline.
    """

    logger.info("Creating RAG Chain...")

    try:

        prompt = get_rag_prompt()
        llm = load_llm()

        rag_chain = (
            RunnableParallel(
                {
                    "context": retriever | RunnableLambda(combine_documents),
                    "question": RunnablePassthrough()
                }
            )
            | prompt
            | llm
            | StrOutputParser()
        )

        logger.info("RAG Chain created successfully.")

        return rag_chain

    except Exception as e:
        logger.exception(f"Failed to create RAG Chain: {e}")
        raise


if __name__ == "__main__":

    logger.info("Testing RAG Chain...")

    retriever = get_retriever()

    chain = create_rag_chain(retriever)

    query = "What is explained in this video?"

    answer = chain.invoke(query)

    print("\nGenerated Answer:\n")

    print(answer)