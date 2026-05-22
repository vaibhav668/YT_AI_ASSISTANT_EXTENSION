from fastapi import APIRouter
from app.utils.youtube import extract_video_id
from app.services.transcript_service import get_video_transcript
from app.services.rag_service import (
    split_text,
    create_vector_store,
    create_retriever,
    ask_question
)

router=APIRouter()

@router.post("/transcript")
def fetch_transcript(data:dict):
    video_url = data.get("url")
    video_id = extract_video_id(video_url)

    if not video_id:
        return {"error":"Invalid Youtube URL"}
    transcript = get_video_transcript(video_id)

    return{
        "video_id":video_id,
        "transcript":transcript
    }

@router.post("/ask")
def ask_video(data: dict):

    video_url= data.get("url")
    question= data.get("question")

    if not video_url or not question:
        return{
            "error": "URL and question are required"
        }
    video_id = extract_video_id(video_url)

    if not video_id:
        return{
            "error": "Invalid youtube url"
        }
    
    transcript= get_video_transcript(video_id)

    chunks= split_text(transcript)

    vector_store = create_vector_store(chunks)

    retriever= create_retriever(vector_store)

    answer= ask_question(retriever,question)

    return {
    "question": question,
    "answer": answer
    }

