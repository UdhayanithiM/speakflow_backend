import uuid
from sqlalchemy.orm import Session
from ..models import GameSession
from .vocab_service import (
    get_vocab_content,  # Renamed from vocab_preview
    generate_quiz,      # Renamed from vocab_listen_click
    calculate_result    # Renamed from vocab_result
)

# --------------------------------------------------
# START VOCAB SESSION (PART 0: PREVIEW)
# --------------------------------------------------
def start_vocab_session(db: Session, user_id: int, category: str):
    """
    Initializes a new Vocabulary session.
    PART FLOW:
    0 = Preview
    1 = Listen & Click
    2 = Results
    """
    
    # FIX: Use get_vocab_content and pass a default level (e.g., 1)
    # Since the session start doesn't specify level yet, we default to 1.
    preview_data = get_vocab_content(category, level=1)
    
    if not preview_data:
        raise ValueError("Invalid category or empty content")

    session = GameSession(
        session_id=str(uuid.uuid4()),
        user_id=user_id,
        game_type="vocab",
        category=category,
        current_part=0,          # PREVIEW
        current_index=0,
        score=0,
        total_questions=0,
        questions=[],            # JSON Column
        answers=[],              # JSON Column
        status="active"
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "session_id": session.session_id,
        "part": 0,
        "preview": preview_data
    }


# --------------------------------------------------
# MOVE TO PART 1: LISTEN & CLICK
# --------------------------------------------------
def start_listen_click(db: Session, session: GameSession):
    """
    Generates questions ONLY when entering PART 1
    """
    # FIX: Use generate_quiz and pass level (defaulting to 1 for now)
    questions = generate_quiz(session.category, level=1)

    if not questions:
        raise ValueError("Failed to generate questions")

    session.questions = questions
    session.total_questions = len(questions)
    session.current_index = 0
    session.current_part = 1   # LISTEN & CLICK

    db.commit()
    db.refresh(session)

    return {
        "part": 1,
        "total_questions": session.total_questions,
        "question": session.questions[0]
    }


# --------------------------------------------------
# GET CURRENT QUESTION (PART 1)
# --------------------------------------------------
def get_current_question(session: GameSession):
    if session.current_part != 1:
        raise ValueError("Not in Listen & Click part")

    # Ensure we don't go out of bounds
    if session.current_index >= len(session.questions):
        return None
        
    return session.questions[session.current_index]


# --------------------------------------------------
# SUBMIT ANSWER (PART 1)
# --------------------------------------------------
def submit_vocab_answer(
    db: Session,
    session: GameSession,
    selected_word: str
):
    if session.current_part != 1:
        raise ValueError("Invalid game state")

    question = session.questions[session.current_index]
    
    # Check answer (Logic matches your quiz generation structure)
    correct = selected_word == question["target_word"]

    # Append to answers list (create new list to trigger SQLAlchemy detection if needed)
    current_answers = list(session.answers) if session.answers else []
    current_answers.append({
        "question_id": question["question_id"],
        "correct_word": question["target_word"],
        "selected_word": selected_word,
        "correct": correct
    })
    session.answers = current_answers

    if correct:
        session.score += 1 

    session.current_index += 1

    # Finished all questions → move to RESULTS
    if session.current_index >= session.total_questions:
        session.current_part = 2
        session.status = "completed"

        # FIX: Use calculate_result
        result = calculate_result(
            score=session.score,
            total=session.total_questions
        )

        db.commit()
        db.refresh(session)

        return {
            "completed": True,
            "result": result,
            "answers": session.answers
        }

    db.commit()
    db.refresh(session)

    return {
        "completed": False,
        "correct": correct,
        "next_question": session.questions[session.current_index]
    }