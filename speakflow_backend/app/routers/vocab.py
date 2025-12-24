# app/routers/vocab.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import vocab_service

router = APIRouter(prefix="/vocab", tags=["Vocabulary"])


# ==============================
# REQUEST MODELS
# ==============================
class VocabResultRequest(BaseModel):
    score: int
    total: int


# ==============================
# 1. PREVIEW (CATEGORY + LEVEL)
# ==============================
@router.get("/{category}/{level}/preview")
def preview(category: str, level: int):
    items = vocab_service.get_vocab_content(category, level)

    if not items:
        raise HTTPException(status_code=404, detail="Category or level not found")

    return {
        "game_type": "vocab_preview",
        "category": category,
        "level": level,
        "payload": {
            "items": items
        }
    }


# ==============================
# 2. LISTEN & CLICK GAME
# ==============================
@router.get("/{category}/{level}/listen-click")
def listen_click(category: str, level: int):
    questions = vocab_service.generate_quiz(category, level)

    if not questions:
        raise HTTPException(status_code=404, detail="Quiz data not found")

    return {
        "game_type": "vocab_listen_click",
        "category": category,
        "part": 2,
        "total_parts": 3,
        "payload": {
            "questions": questions
        }
    }


# ==============================
# 3. RESULT
# ==============================
@router.post("/{category}/result")
def result(category: str, body: VocabResultRequest):
    result_data = vocab_service.calculate_result(body.score, body.total)

    return {
        "game_type": "vocab_result",
        "category": category,
        "part": 3,
        "total_parts": 3,
        "payload": result_data
    }
