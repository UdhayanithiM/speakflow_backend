from sqlalchemy.orm import Session
from ..models import GameSession
from .adjectives_data import ADJECTIVES_DB
from .sentence_validator import validate_sentence


def start_adjective_session(db: Session, user_id: int, category: str):
    if category not in ADJECTIVES_DB:
        return None

    data = ADJECTIVES_DB[category]

    session = GameSession(
        user_id=user_id,
        game_type="adjectives",
        category=category,
        current_part=1,
        current_index=0,
        total_questions=3,
        questions=data,
        answers=[],
        score=0
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session


def get_adjective_question(session: GameSession):
    data = session.questions

    if session.current_part in [1, 2]:
        return data["rounds"][session.current_part - 1]

    if session.current_part == 3:
        return data["sentence"]

    return None


def submit_adjective_answer(db: Session, session: GameSession, answer: str):
    data = session.questions
    correct = False
    reason = None

    # ---------------- PART 1 & 2 ----------------
    if session.current_part in [1, 2]:
        expected = data["rounds"][session.current_part - 1]["answer"]
        correct = answer == expected

    # ---------------- PART 3 (UPDATED) ----------------
    elif session.current_part == 3:
        sentence_cfg = data["sentence"]

        correct, reason = validate_sentence(
            answer,
            sentence_cfg["required_words"],
            sentence_cfg["template"],
            sentence_cfg["min_length"]
        )

    session.answers.append({
        "part": session.current_part,
        "answer": answer,
        "correct": correct,
        "reason": reason
    })

    if correct:
        session.score += 1

    session.current_part += 1

    if session.current_part > 3:
        session.status = "completed"

    db.commit()
    db.refresh(session)

    return correct, session
