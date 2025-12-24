# app/services/speaking_service.py

from sqlalchemy.orm import Session
from ..models import SpeakingLessonProgress, SpeakingDialogueProgress
from .speaking_data import SPEAKING_LESSONS

import os
import difflib
import json
from groq import Groq
from dotenv import load_dotenv

# ==========================================
# 1. CONFIGURATION
# ==========================================
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is missing! Check your .env file.")

client = Groq(api_key=GROQ_API_KEY)

# ---------------------------------------------------------
# 2. GET LESSONS (STATIC + DB MERGE)
# ---------------------------------------------------------
def get_lessons_with_progress(db: Session, user_id: int):
    """
    Returns speaking lessons enriched with lock + progress data.
    """
    enriched_lessons = []

    # Ensure lesson 1 is always unlocked
    check_and_unlock_lesson(db, user_id, 1)

    for static_lesson in SPEAKING_LESSONS:
        progress = db.query(SpeakingLessonProgress).filter_by(
            user_id=user_id,
            lesson_id=static_lesson["id"]
        ).first()

        enriched_lessons.append({
            "id": static_lesson["id"],
            "title": static_lesson["title"],
            "description": static_lesson["description"],
            "level": static_lesson["level"],
            "image": static_lesson["image"],
            "total_dialogues": len(static_lesson["dialogues"]),
            "is_locked": progress.is_locked if progress else True,
            "progress_percent": progress.progress_percent if progress else 0.0
        })

    return enriched_lessons

# ---------------------------------------------------------
# 3. SAVE DIALOGUE SCORE + UPDATE LESSON
# ---------------------------------------------------------
def save_dialogue_progress(
    db: Session,
    user_id: int,
    lesson_id: int,
    dialogue_id: int,
    score: int
):
    # Save / update dialogue score
    record = db.query(SpeakingDialogueProgress).filter_by(
        user_id=user_id,
        lesson_id=lesson_id,
        dialogue_id=dialogue_id
    ).first()

    if not record:
        record = SpeakingDialogueProgress(
            user_id=user_id,
            lesson_id=lesson_id,
            dialogue_id=dialogue_id,
            score=score
        )
        db.add(record)
    else:
        if record.score is None or score > record.score:
            record.score = score

    db.commit()

    # Update lesson progress
    update_lesson_completion(db, user_id, lesson_id)

# ---------------------------------------------------------
# 4. UPDATE LESSON COMPLETION + UNLOCK NEXT
# ---------------------------------------------------------
def update_lesson_completion(db: Session, user_id: int, lesson_id: int):
    static_lesson = next(
        (l for l in SPEAKING_LESSONS if l["id"] == lesson_id),
        None
    )
    if not static_lesson:
        return

    total_dialogues = len(static_lesson["dialogues"])

    completed_count = db.query(SpeakingDialogueProgress).filter_by(
        user_id=user_id,
        lesson_id=lesson_id
    ).count()

    progress_percent = int((completed_count / total_dialogues) * 100)

    lesson_progress = db.query(SpeakingLessonProgress).filter_by(
        user_id=user_id,
        lesson_id=lesson_id
    ).first()

    if not lesson_progress:
        lesson_progress = SpeakingLessonProgress(
            user_id=user_id,
            lesson_id=lesson_id,
            is_locked=False
        )
        db.add(lesson_progress)

    lesson_progress.progress_percent = progress_percent

    if progress_percent >= 80:
        lesson_progress.is_completed = True
        next_lesson_id = lesson_id + 1
        check_and_unlock_lesson(db, user_id, next_lesson_id)

    db.commit()

# ---------------------------------------------------------
# 5. ENSURE / UNLOCK LESSON
# ---------------------------------------------------------
def check_and_unlock_lesson(db: Session, user_id: int, lesson_id: int):
    progress = db.query(SpeakingLessonProgress).filter_by(
        user_id=user_id,
        lesson_id=lesson_id
    ).first()

    if not progress:
        progress = SpeakingLessonProgress(
            user_id=user_id,
            lesson_id=lesson_id,
            is_locked=False,
            progress_percent=0.0
        )
        db.add(progress)
    else:
        progress.is_locked = False

    db.commit()

# ---------------------------------------------------------
# 6. AUDIO ANALYSIS (UNCHANGED LOGIC)
# ---------------------------------------------------------
def analyze_audio(file_binary, target_sentence: str):
    """
    1. Transcribe Audio
    2. Score Pronunciation
    3. Generate AI Feedback
    """

    # --- A. TRANSCRIBE ---
    try:
        transcription = client.audio.transcriptions.create(
            file=("audio.m4a", file_binary),
            model="whisper-large-v3",
            response_format="json",
            language="en"
        )
        user_spoken_text = transcription.text.strip()
    except Exception:
        user_spoken_text = ""

    # --- B. SCORING ---
    matcher = difflib.SequenceMatcher(
        None,
        user_spoken_text.lower(),
        target_sentence.lower()
    )
    clarity_score = int(matcher.ratio() * 100)

    target_words = len(target_sentence.split())
    user_words = len(user_spoken_text.split())

    fluency_score = (
        min(100, int((user_words / target_words) * 100))
        if target_words > 0 else 0
    )

    if clarity_score < 50:
        fluency_score = max(0, fluency_score - 30)

    accent_score = max(0, clarity_score - 10)

    overall_score = int(
        (clarity_score + fluency_score + accent_score) / 3
    )

    # --- C. WORD ANALYSIS ---
    word_analysis = generate_word_breakdown(
        user_spoken_text,
        target_sentence
    )

    # --- D. AI FEEDBACK ---
    feedback = generate_ai_feedback(
        user_spoken_text,
        target_sentence,
        overall_score
    )

    return {
        "overall_score": overall_score,
        "metrics": {
            "fluency": fluency_score,
            "clarity": clarity_score,
            "accent": accent_score
        },
        "feedback": feedback,
        "word_analysis": word_analysis,
        "debug_transcript": user_spoken_text
    }

# ---------------------------------------------------------
# 7. WORD BREAKDOWN
# ---------------------------------------------------------
def generate_word_breakdown(spoken: str, target: str):
    target_clean = target.lower().replace(".", "").replace(",", "").split()
    spoken_clean = spoken.lower().replace(".", "").replace(",", "").split()

    analysis = []

    for word in target_clean:
        if word in spoken_clean:
            analysis.append({
                "word": word,
                "status": "perfect",
                "score": 95,
                "correction": None
            })
        else:
            matches = difflib.get_close_matches(word, spoken_clean, n=1, cutoff=0.7)
            if matches:
                analysis.append({
                    "word": word,
                    "status": "good",
                    "score": 80,
                    "correction": word
                })
            else:
                analysis.append({
                    "word": word,
                    "status": "poor",
                    "score": 40,
                    "correction": word
                })

    return analysis

# ---------------------------------------------------------
# GET SINGLE LESSON DETAILS (STATIC ONLY)
# ---------------------------------------------------------
def get_lesson_details(lesson_id: int):
    """
    Returns static lesson content (dialogues) by lesson_id
    """
    for lesson in SPEAKING_LESSONS:
        if lesson["id"] == lesson_id:
            return {
                "id": lesson["id"],
                "title": lesson["title"],
                "dialogues": lesson["dialogues"]
            }
    return None

# ---------------------------------------------------------
# 8. AI COACH FEEDBACK
# ---------------------------------------------------------
def generate_ai_feedback(spoken: str, target: str, score: int):
    if not spoken:
        return {
            "summary": "We couldn't hear you clearly.",
            "tips": [
                "Check your microphone.",
                "Speak louder.",
                "Try again slowly."
            ]
        }

    try:
        prompt = f"""
Act as an English speaking coach.

Target Sentence: "{target}"
Student Said: "{spoken}"
Score: {score}/100

Return ONLY raw JSON with:
- summary (1 sentence)
- tips (array of 3 short tips)
"""

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    except Exception:
        return {
            "summary": "Good effort! Keep practicing.",
            "tips": [
                "Pronounce each word clearly.",
                "Speak at a steady pace.",
                "Listen and repeat."
            ]
        }
