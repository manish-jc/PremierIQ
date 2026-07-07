from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.pipeline import RAGPipeline

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)

pipeline = RAGPipeline()


class ChatRequest(BaseModel):

    question: str


@router.post("/")
def chat(request: ChatRequest):

    answer = pipeline.ask(
        request.question
    )

    return {

        "question": request.question,

        "answer": answer

    }