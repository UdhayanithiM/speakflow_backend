# app/services/echo_game_data.py

# ==========================================
# ECHO GAME DATA (Listen & Repeat)
# ==========================================

ECHO_LEVELS = [
    {
        "level_id": 1,
        "title": "Short Phrases",
        "description": "Listen and repeat these simple phrases.",
        "questions": [
            {"id": "echo_101", "text": "Hello, how are you?"},
            {"id": "echo_102", "text": "I like blue cars."},
            {"id": "echo_103", "text": "It is sunny today."},
            {"id": "echo_104", "text": "Can I have some water?"},
            {"id": "echo_105", "text": "This game is fun."}
        ]
    },
    {
        "level_id": 2,
        "title": "Daily Sentences",
        "description": "Repeat these common daily sentences.",
        "questions": [
            {"id": "echo_201", "text": "Where is the nearest supermarket?"},
            {"id": "echo_202", "text": "I wake up at seven o'clock."},
            {"id": "echo_203", "text": "My favorite color is green."},
            {"id": "echo_204", "text": "Please open the window."},
            {"id": "echo_205", "text": "See you tomorrow morning."}
        ]
    }
]

def get_echo_level(level_id: int):
    for level in ECHO_LEVELS:
        if level["level_id"] == level_id:
            return level
    return None