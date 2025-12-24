# app/services/gamification_data.py

# ==========================================
# VOICE MATCH GAME DATA
# ==========================================
# GAME RULE:
# - Show an emotion image
# - User says the emotion aloud
# - Exact / near-exact match validation
# ==========================================

VOICE_MATCH_LEVELS = [

    # ------------------------------------------------------
    # LEVEL 1: BASIC EMOTIONS
    # ------------------------------------------------------
    {
        "level_id": 1,
        "title": "Basic Emotions",
        "description": "Look at the face and say the feeling!",
        "questions": [
            {
                "id": "vm_101",
                "target_word": "Happy",
                # Clear smiling face
                "image": "https://img.freepik.com/free-vector/happy-boy-jumping-cartoon-character_1308-102618.jpg?semt=ais_hybrid&w=740&q=80"
            },
            {
                "id": "vm_102",
                "target_word": "Sad",
                # Crying/Sad face (Matches 'Sad')
                "image": "https://thumbs.dreamstime.com/b/sad-girl-cartoon-sitting-alone-illustration-96721136.jpg"
            },
            {
                "id": "vm_103",
                "target_word": "Angry",
                # Red angry face
                "image": "https://media.istockphoto.com/id/635961820/vector/furious-man.jpg?s=612x612&w=0&k=20&c=8jNAUhUfA7n9A7dUduZvEbg-w52xZYmT5O3PBUjmXAI="
            },
            {
                "id": "vm_104",
                "target_word": "Surprised",
                # Open mouth / Shocked
                "image": "https://images.rawpixel.com/image_png_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDI0LTEyL3Jhd3BpeGVsb2ZmaWNlMTFfY3V0ZV8zZF9yZW5kZXJfb2ZfY3V0ZV9ib3lfc3VycHJpc2VfbW91dGhfb3Blbl82NDU5MTI5NC03YzZiLTQ5OWMtYWM4Zi1iYTVjM2Y3MDU3MTgtbTRtaWp1YTYucG5n.png"
            },
            {
                "id": "vm_105",
                "target_word": "Scared",
                # Screaming in fear
                "image": "https://img.freepik.com/premium-vector/vector-illustration-cartoon-boy-with-scared-expression-pose_625612-23.jpg?semt=ais_hybrid&w=740&q=80"
            }
        ]
    },

    # ------------------------------------------------------
    # LEVEL 2: ADVANCED EMOTIONS
    # ------------------------------------------------------
    {
        "level_id": 2,
        "title": "Advanced Emotions",
        "description": "Say the emotion shown in the picture.",
        "questions": [
            {
                "id": "vm_201",
                "target_word": "Excited",
                # Star eyes / Grinning
                "image": "https://img.freepik.com/free-vector/joyful-child-jumping-with-excitement_1308-182468.jpg?semt=ais_hybrid&w=740&q=80"
            },
            {
                "id": "vm_202",
                "target_word": "Confused",
                # Monocle / Thinking expression
                "image": "https://img.freepik.com/premium-vector/cartoon-confuse-man-vector-illustration_851674-45948.jpg?semt=ais_hybrid&w=740&q=80"
            },
            {
                "id": "vm_203",
                "target_word": "Tired",
                # Sleeping / Zzz
                "image": "https://img.freepik.com/free-vector/tired-employee-worker-cartoon-icon-illustration-people-business-icon-concept-isolated-flat-cartoon-style_138676-2096.jpg?semt=ais_hybrid&w=740&q=80"
            },
            {
                "id": "vm_204",
                "target_word": "Proud",
                # Cool / Sunglasses (Represents confident/proud)
                "image": "https://img.freepik.com/free-vector/boy-showing-his-thumb_1308-18033.jpg?semt=ais_hybrid&w=740&q=80"
            },
            {
                "id": "vm_205",
                "target_word": "Nervous",
                # Sweat drop / Worried
                "image": "https://thumbs.dreamstime.com/b/cartoon-vector-illustration-boy-looking-scared-anxious-nervous-open-mouth-worried-expression-cartoon-boy-376262155.jpg"
            }
        ]
    }
]


def get_voice_match_level(level_id: int):
    """
    Returns the data for a specific Voice Match level.
    """
    for level in VOICE_MATCH_LEVELS:
        if level["level_id"] == level_id:
            return level
    return None