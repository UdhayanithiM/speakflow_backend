# app/routers/vocab.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services import vocab_service

router = APIRouter(prefix="/vocab", tags=["Vocabulary"])


# --------------------------------------------------
# REQUEST MODELS
# --------------------------------------------------
class VocabResultRequest(BaseModel):
    score: int
    total: int


# --------------------------------------------------
# PART 1: PREVIEW (LISTEN ONLY)
# --------------------------------------------------
@router.get("/{category}/preview")
def preview(category: str):
    data = vocab_service.vocab_preview(category)

    if not data:
        raise HTTPException(status_code=404, detail="Category not found")

    return {
        "game_type": "vocab",
        "category": category,
        "part_index": 1,          # Preview
        "total_parts": 3,
        "payload": {
            "items": data
        }
    }


# --------------------------------------------------
# PART 2: LISTEN & CLICK
# --------------------------------------------------
@router.get("/{category}/listen-click")
def listen_click(category: str):
    questions = vocab_service.vocab_listen_click(category)

    if not questions:
        raise HTTPException(status_code=404, detail="Category not found")

    return {
        "game_type": "vocab",
        "category": category,
        "part_index": 2,          # Listen & Click
        "total_parts": 3,
        "payload": {
            "questions": questions
        }
    }


# --------------------------------------------------
# PART 3: RESULT
# --------------------------------------------------
@router.post("/{category}/result")
def result(category: str, body: VocabResultRequest):
    result_data = vocab_service.vocab_result(
        score=body.score,
        total=body.total
    )

    return {
        "game_type": "vocab",
        "category": category,
        "part_index": 3,          # Result
        "total_parts": 3,
        "payload": result_data
    }
