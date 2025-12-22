from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import GameSession
from ..services import session_service

router = APIRouter(prefix="/game", tags=["Game Session"])


@router.post("/start")
def start_game(
    user_id: int,
    game_type: str,
    category: str,
    db: Session = Depends(get_db)
):
    if game_type != "vocab":
        raise HTTPException(400, "Unsupported game type")

    session = session_service.start_vocab_session(
        db, user_id, category
    )

    return {
        "session_id": session.id,
        "part": session.current_part,
        "total_questions": session.total_questions
    }


@router.get("/question/{session_id}")
def get_question(session_id: int, db: Session = Depends(get_db)):
    session = db.query(GameSession).get(session_id)
    if not session or session.status != "active":
        raise HTTPException(404, "Session not found")

    question = session_service.get_current_question(session)

    return {
        "part": session.current_part,
        "index": session.current_index,
        "question": question
    }


@router.post("/answer/{session_id}")
def submit_answer(
    session_id: int,
    selected: str,
    db: Session = Depends(get_db)
):
    session = db.query(GameSession).get(session_id)
    if not session or session.status != "active":
        raise HTTPException(404, "Session not active")

    correct, updated = session_service.submit_answer(
        db, session, selected
    )

    return {
        "correct": correct,
        "part": updated.current_part,
        "next_index": updated.current_index,
        "status": updated.status,
        "score": updated.score
    }
