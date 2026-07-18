import streamlit as st
from urllib.parse import urlparse, parse_qs

from vectorstore.chroma_store import create_vector_store
from Retrieval.retriever import get_retriever
from chains.rag_chain import create_rag_chain


def extract_video_id(url: str):
    """
    Extract YouTube video ID from URL.
    """

    if "youtu.be" in url:
        return urlparse(url).path.lstrip("/")

    return parse_qs(urlparse(url).query)["v"][0]


st.set_page_config(
    page_title="YouTube Chatbot",
    page_icon="🎥"
)

st.title("🎥 YouTube Chatbot")

st.write("Ask questions about any YouTube video transcript.")

youtube_url = st.text_input(
    "Paste YouTube Video URL"
)

if st.button("Load Video"):

    if youtube_url:

        with st.spinner("Processing video..."):

            video_id = extract_video_id(youtube_url)

            create_vector_store(video_id)

            st.session_state["video_loaded"] = True

        st.success("Video processed successfully!")

    else:
        st.warning("Please enter a YouTube URL.")


if st.session_state.get("video_loaded"):

    question = st.text_input(
        "Ask a question about the video"
    )

    if st.button("Ask"):

        if question:

            with st.spinner("Generating answer..."):

                retriever = get_retriever()

                rag_chain = create_rag_chain(retriever)

                answer = rag_chain.invoke(question)

            st.subheader("Answer")

            st.write(answer)

        else:
            st.warning("Please enter a question.")