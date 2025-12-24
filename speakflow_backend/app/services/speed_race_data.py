# app/services/speed_race_data.py

# ==========================================
# SPEED SPEAK RACE DATA
# ==========================================

SPEED_RACE_LEVELS = [
    {
        "level_id": 1,
        "title": "Speed Challenge",
        "description": "Race against the clock! Read as many phrases as you can.",
        "time_limit": 60, # 60 Seconds
        "questions": [
            {"id": "sr_101", "text": "The quick brown fox jumps over the lazy dog."},
            {"id": "sr_102", "text": "She sells seashells by the seashore."},
            {"id": "sr_103", "text": "I scream, you scream, we all scream for ice cream."},
            {"id": "sr_104", "text": "How much wood would a woodchuck chuck?"},
            {"id": "sr_105", "text": "Red leather, yellow leather."},
            {"id": "sr_106", "text": "Peter Piper picked a peck of pickled peppers."},
            {"id": "sr_107", "text": "A big black bug bit a big black bear."},
            {"id": "sr_108", "text": "I saw a kitten eating chicken in the kitchen."},
            {"id": "sr_109", "text": "Good morning, how are you today?"},
            {"id": "sr_110", "text": "I would like a cup of coffee please."},
            {"id": "sr_111", "text": "Where is the nearest subway station?"},
            {"id": "sr_112", "text": "It is raining cats and dogs outside."},
            {"id": "sr_113", "text": "Time flies when you are having fun."},
            {"id": "sr_114", "text": "Actions speak louder than words."},
            {"id": "sr_115", "text": "Practice makes perfect."},
            {"id": "sr_116", "text": "Better late than never."},
            {"id": "sr_117", "text": "Break a leg!"},
            {"id": "sr_118", "text": "Under the weather."},
            {"id": "sr_119", "text": "Piece of cake."},
            {"id": "sr_120", "text": "Once in a blue moon."},
            {"id": "sr_121", "text": "The early bird catches the worm."},
            {"id": "sr_122", "text": "A penny for your thoughts."},
            {"id": "sr_123", "text": "Do not judge a book by its cover."},
            {"id": "sr_124", "text": "Honesty is the best policy."},
            {"id": "sr_125", "text": "To be or not to be, that is the question."}
        ]
    }
]

def get_speed_race_level(level_id: int):
    for level in SPEED_RACE_LEVELS:
        if level["level_id"] == level_id:
            return level
    return None