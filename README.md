# 🎥 YouTube Chatbot using GenAI, LangChain & RAG

A Retrieval-Augmented Generation (RAG) based YouTube Chatbot that allows users to ask questions about any YouTube video using its transcript. The application retrieves the most relevant transcript chunks from a Chroma vector database and generates accurate answers using Mistral AI.

---

## 🚀 Features

* Extracts transcripts from YouTube videos.
* Supports YouTube URLs, shortened URLs, and Video IDs.
* Splits long transcripts into manageable chunks.
* Generates embeddings using **Cohere Embeddings**.
* Stores embeddings in a **Chroma Vector Database**.
* Retrieves the most relevant transcript chunks using LangChain Retriever.
* Uses **Mistral AI** as the Large Language Model (LLM).
* Interactive Streamlit web interface.
* Logging support for easier debugging.

---

## 🛠️ Tech Stack

* Python
* LangChain
* Mistral AI
* Cohere Embeddings
* Chroma DB
* Streamlit
* YouTube Transcript API

---

## 📂 Project Structure

```text
YouTubeChatbot/
│
├── app.py
├── .env
├── requirements.txt
│
├── embeddings/
│   └── embedding_generator.py
│
├── ingestion/
│   ├── transcript_loader.py
│   └── text_splitter.py
│
├── vectorstore/
│   └── chroma_store.py
│
├── Retrieval/
│   └── retriever.py
│
├── prompts/
│   └── prompt.py
│
├── chains/
│   └── rag_chain.py
│
├── llm/
│   └── model.py
│
├── utils/
│   ├── logger.py
│   └── settings.py
│
└── chroma_db/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd YouTubeChatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
COHERE_API_KEY=your_cohere_api_key
```

---

## ▶️ Running the Project

Start the Streamlit application:

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

---

## 📝 How It Works

1. User enters a YouTube video URL.
2. The transcript is fetched using the YouTube Transcript API.
3. The transcript is divided into smaller chunks.
4. Cohere generates embeddings for each chunk.
5. Embeddings are stored in Chroma DB.
6. The retriever searches for the most relevant chunks.
7. The prompt combines the retrieved context with the user's question.
8. Mistral AI generates an answer based only on the retrieved transcript.


---

## 📸 Application Workflow

```text
YouTube URL
      │
      ▼
Transcript Loader
      │
      ▼
Text Splitter
      │
      ▼
Cohere Embeddings
      │
      ▼
Chroma Vector Database
      │
      ▼
Retriever (MMR / Similarity)
      │
      ▼
Prompt Template
      │
      ▼
Mistral LLM
      │
      ▼
Final Answer
```

---

## 📖 Example Questions

* What is the main topic of this video?
* Summarize the video.
* What are the key points discussed?
* Explain a particular concept mentioned in the video.
* What conclusion does the speaker provide?

---

## ⚠️ Limitations

* Works only for videos that have transcripts available.
* Private or transcript-disabled videos are not supported.
* Very long videos may hit embedding API rate limits depending on the API plan.

---


## 👩‍💻 Author

**Nisha Chaudhary**

Final Year B.Tech (Computer Science)

Built using **LangChain**, **RAG**, **Mistral AI**, **Cohere**, **Chroma DB**, and **Streamlit**.
