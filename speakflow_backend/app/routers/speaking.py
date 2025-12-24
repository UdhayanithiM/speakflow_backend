# app/routers/speaking.py

from fastapi import (
    APIRouter,
    HTTPException,
    UploadFile,
    File,
    Form,
    Depends
)
from sqlalchemy.orm import Session

from ..database import get_db
from ..services import speaking_service
from ..schemas import SpeakingProgressRequest

router = APIRouter(prefix="/speaking", tags=["Speaking"])


# --------------------------------------------------
# GET ALL SPEAKING LESSONS (WITH LOCK / PROGRESS)
# --------------------------------------------------
@router.get("/lessons/{user_id}")
def get_lessons(user_id: int, db: Session = Depends(get_db)):
    return {
        "payload": speaking_service.get_lessons_with_progress(db, user_id)
    }


# --------------------------------------------------
# GET SINGLE LESSON DETAILS (STATIC CONTENT)
# --------------------------------------------------
@router.get("/lesson/{lesson_id}")
def get_lesson_detail(lesson_id: int):
    lesson = speaking_service.get_lesson_details(lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return {
        "payload": lesson
    }


# --------------------------------------------------
# SAVE DIALOGUE PROGRESS (SCORE + UNLOCK LOGIC)
# --------------------------------------------------
@router.post("/progress")
def save_progress(
    req: SpeakingProgressRequest,
    db: Session = Depends(get_db)
):
    speaking_service.save_dialogue_progress(
        db=db,
        user_id=req.user_id,
        lesson_id=req.lesson_id,
        dialogue_id=req.dialogue_id,
        score=req.score
    )

    return {
        "status": "success",
        "message": "Progress saved"
    }


# --------------------------------------------------
# ANALYZE AUDIO (WHISPER + SCORING + AI FEEDBACK)
# --------------------------------------------------
@router.post("/analyze")
async def analyze_speaking(
    file: UploadFile = File(...),
    target_sentence: str = Form(...),
    lesson_id: int = Form(...)
):
    try:
        file_bytes = await file.read()
        result = speaking_service.analyze_audio(
            file_bytes,
            target_sentence
        )

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        print(f"❌ API Error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Audio analysis failed"
        )
