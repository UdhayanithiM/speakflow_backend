import random
import uuid

VOCAB_DB = {
    "animals": [
        {"word": "Chicken", "image": "🐔", "audio": "chicken.mp3"},
        {"word": "Sheep", "image": "🐑", "audio": "sheep.mp3"},
        {"word": "Monkey", "image": "🐵", "audio": "monkey.mp3"},
        {"word": "Frog", "image": "🐸", "audio": "frog.mp3"},
        {"word": "Duck", "image": "🦆", "audio": "duck.mp3"},
        {"word": "Rabbit", "image": "🐰", "audio": "rabbit.mp3"},
        {"word": "Pig", "image": "🐷", "audio": "pig.mp3"},
        {"word": "Fish", "image": "🐟", "audio": "fish.mp3"},
        {"word": "Zebra", "image": "🦓", "audio": "zebra.mp3"},
        {"word": "Horse", "image": "🐴", "audio": "horse.mp3"},
    ]
}

# ---------- PART 1: PREVIEW ----------
def vocab_preview(category: str):
    return VOCAB_DB.get(category)

# ---------- PART 2: LISTEN & CLICK ----------
def vocab_listen_click(category: str, count: int = 10):
    data = VOCAB_DB.get(category)
    if not data:
        return None

    questions = []
    selected = random.sample(data, min(count, len(data)))

    for item in selected:
        distractors = random.sample(
            [x for x in data if x["word"] != item["word"]], 3
        )

        options = distractors + [item]
        random.shuffle(options)

        questions.append({
            "question_id": str(uuid.uuid4()),
            "target_word": item["word"],
            "target_audio": item["audio"],
            "options": [
                {
                    "option_id": str(uuid.uuid4()),
                    "image": o["image"],
                    "word": o["word"]
                }
                for o in options
            ]
        })

    return questions

# ---------- PART 3: RESULT ----------
def vocab_result(score: int, total: int):
    return {
        "score": score,
        "total": total,
        "xp": score * 10
    }
