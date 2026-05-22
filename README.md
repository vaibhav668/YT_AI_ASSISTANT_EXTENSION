# YouTube AI Assistant Extension

An AI-powered Chrome extension that allows users to ask questions about the currently playing YouTube video using Retrieval-Augmented Generation (RAG).

The extension automatically detects the active YouTube video, fetches its transcript, processes it using embeddings and vector search, and generates contextual answers using a Large Language Model.

---

## Features

* Detects currently opened YouTube video automatically
* Fetches video transcript using YouTube Transcript API
* Uses semantic search with FAISS vector database
* Retrieval-Augmented Generation (RAG) pipeline
* AI-powered question answering
* Clean chat-based Chrome extension UI
* FastAPI backend integration
* HuggingFace embeddings and LLM support

---

## Tech Stack

### Frontend

* HTML
* CSS
* Vanilla JavaScript
* Chrome Extension APIs

### Backend

* Python
* FastAPI
* LangChain
* FAISS
* HuggingFace Embeddings
* HuggingFace LLM Endpoint
* YouTube Transcript API

---

## Project Structure

```bash
youtube-ai-assistant/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── extension/
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.css
│   └── popup.js
│
└── README.md
```

---

## How It Works

1. User opens a YouTube video
2. Chrome extension detects the current tab URL
3. Frontend sends video URL and question to FastAPI backend
4. Backend fetches transcript from YouTube
5. Transcript is split into chunks
6. Chunks are converted into embeddings
7. FAISS performs semantic similarity search
8. Relevant context is sent to the LLM
9. AI-generated answer is returned to the extension UI

---

## RAG Pipeline

```text
YouTube Transcript
        ↓
Text Chunking
        ↓
Embeddings
        ↓
FAISS Vector Store
        ↓
Semantic Retrieval
        ↓
Prompt Construction
        ↓
LLM Response
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/vaibhav668/YT_AI_ASSISTANT_EXTENSION.git
```

---

### 2. Backend Setup

Move to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Environment Variables

Create `.env` file inside backend folder:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

### 4. Run Backend

```bash
uvicorn app.main:app --reload
```

Backend will run on:

```text
http://127.0.0.1:8000
```

---

### 5. Load Chrome Extension

1. Open Chrome
2. Go to:

```text
chrome://extensions
```

3. Enable Developer Mode
4. Click "Load unpacked"
5. Select the `extension` folder

---

## Usage

1. Open any YouTube video with available transcript
2. Click the extension icon
3. Ask questions about the video
4. Receive AI-generated contextual answers

---

## Example Questions

* What is this video about?
* Summarize the video
* Explain the main concept discussed
* What are the key points?
* What technologies are mentioned?

---

## Future Improvements

* Transcript caching
* Markdown response rendering
* Better prompt engineering
* Persistent sidebar UI
* Streaming responses
* Deployment support
* Conversation memory
* Multi-video support

---

## Learning Outcomes

This project helped in understanding:

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Embeddings and semantic search
* Chrome extension development
* FastAPI backend architecture
* Frontend-backend integration
* Async JavaScript
* API handling and debugging

---

## License

This project is for educational and portfolio purposes.
