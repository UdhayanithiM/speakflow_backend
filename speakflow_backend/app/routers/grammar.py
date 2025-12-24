from fastapi import APIRouter, HTTPException
from ..services import grammar_data
import random

router = APIRouter(prefix="/grammar", tags=["Grammar"])

@router.get("/level/{level_id}")
def get_grammar_questions(level_id: int):
    """
    Returns the questions for a specific grammar level.
    We shuffle the 'jumbled_words' so they don't appear in a predictable order.
    """
    level_data = grammar_data.get_grammar_level(level_id)
    
    if not level_data:
        raise HTTPException(status_code=404, detail="Level not found")

    # Create a copy so we don't modify the original static data
    response_payload = {
        "level": level_data["level"],
        "title": level_data["title"],
        "description": level_data["description"],
        "questions": []
    }

    for q in level_data["questions"]:
        # Shuffle the words for the frontend
        words_pool = q["jumbled_words"].copy()
        random.shuffle(words_pool)
        
        response_payload["questions"].append({
            "id": q["id"],
            "image": q["image"],
            # The frontend needs to know the correct answer to validate locally (or you can validate on backend)
            # For MVP, validating locally is faster UI.
            "correct_sentence": q["correct_sentence"], 
            "words_pool": words_pool
        })
        
    return {"payload": response_payload}