# app/services/vocab_service.py
import random
import uuid
from .vocab_data import get_words_for_level
from .ai_service import get_ai_image_url, get_ai_audio_url

# ---------- PREVIEW DATA ----------
def get_vocab_content(category: str, level: int):
    words = get_words_for_level(category, level)
    if not words:
        return None

    content = []
    for word in words:
        content.append({
            "word": word,
            "image": get_ai_image_url(word),
            "audio": get_ai_audio_url(word)
        })
    return content

# ---------- QUIZ GENERATION ----------
def generate_quiz(category: str, level: int):
    # 1. Get words for this specific level
    target_words = get_words_for_level(category, level)
    if not target_words:
        return None

    questions = []
    
    for word in target_words:
        # 2. Generate Options
        # We need distractors. We can pick from the same level or other levels.
        # For simplicity, let's use words from the same level as distractors
        distractors = [w for w in target_words if w != word]
        
        # If not enough words in level, duplicate/pad (failsafe)
        if len(distractors) < 3:
            distractors += ["Apple", "Cat", "Dog"] # Fallback
            
        selected_distractors = random.sample(distractors, min(3, len(distractors)))
        
        options_data = selected_distractors + [word]
        random.shuffle(options_data)
        
        # 3. Build Option Objects
        options = []
        for opt_word in options_data:
            options.append({
                "id": str(uuid.uuid4()),
                "image": get_ai_image_url(opt_word), # Only show image in options
                "word": opt_word # Backend knows the word, frontend receives it to check
            })

        # 4. Create Question
        questions.append({
            "question_id": str(uuid.uuid4()),
            "target_word": word,
            "target_audio": get_ai_audio_url(word),
            "correct_option_id": next(o["id"] for o in options if o["word"] == word),
            "options": options
        })
        
    return questions

def calculate_result(score: int, total: int):
    return {
        "score": score,
        "total": total,
        "xp": score * 10,
        "message": "Excellent!" if score == total else "Keep Practicing!"
    }