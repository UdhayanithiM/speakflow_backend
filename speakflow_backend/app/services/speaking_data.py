import urllib.parse

def get_google_tts_url(text: str):
    """
    Generates a direct Google TTS URL for the AI prompt.
    Used by the Android app to play the AI's turn in the conversation.
    """
    encoded_text = urllib.parse.quote(text)
    return f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={encoded_text}&tl=en"

# ==========================================
# SPEAKING LESSONS DATABASE
# ==========================================
# Matches the "Speaking Practice" screenshot provided.

SPEAKING_LESSONS = [
    # ------------------------------------------------------
    # LESSON 1: GREETINGS & INTRODUCTIONS
    # ------------------------------------------------------
    {
        "id": 1,
        "title": "Greetings & Introductions",
        "description": "Learn to say hello and introduce yourself nicely.",
        "level": 1,
        # Icon: Waving Hand (Using a placeholder image URL for now)
        "image": "https://cdn-icons-png.flaticon.com/512/1828/1828884.png", 
        "dialogues": [
            {
                "id": 101,
                "order": 1,
                "ai_prompt": "Hello! It is nice to meet you.",
                "target_response": "Hello! Nice to meet you too.",
                "audio_url": get_google_tts_url("Hello! It is nice to meet you.")
            },
            {
                "id": 102,
                "order": 2,
                "ai_prompt": "What is your name?",
                "target_response": "My name is John.",
                "audio_url": get_google_tts_url("What is your name?")
            },
            {
                "id": 103,
                "order": 3,
                "ai_prompt": "How are you doing today?",
                "target_response": "I am doing great, thank you.",
                "audio_url": get_google_tts_url("How are you doing today?")
            }
        ]
    },

    # ------------------------------------------------------
    # LESSON 2: DAILY CONVERSATIONS
    # ------------------------------------------------------
    {
        "id": 2,
        "title": "Daily Conversations",
        "description": "Talk about your day, weather, and hobbies.",
        "level": 1,
        # Icon: Chat Bubble
        "image": "https://cdn-icons-png.flaticon.com/512/1380/1380338.png",
        "dialogues": [
            {
                "id": 201,
                "order": 1,
                "ai_prompt": "What do you usually do on weekends?",
                "target_response": "I usually relax and watch movies.",
                "audio_url": get_google_tts_url("What do you usually do on weekends?")
            },
            {
                "id": 202,
                "order": 2,
                "ai_prompt": "How is the weather today?",
                "target_response": "It is sunny and warm outside.",
                "audio_url": get_google_tts_url("How is the weather today?")
            },
            {
                "id": 203,
                "order": 3,
                "ai_prompt": "Do you like to cook?",
                "target_response": "Yes, I love cooking dinner for my family.",
                "audio_url": get_google_tts_url("Do you like to cook?")
            }
        ]
    },

    # ------------------------------------------------------
    # LESSON 3: ASKING QUESTIONS
    # ------------------------------------------------------
    {
        "id": 3,
        "title": "Asking Questions",
        "description": "Learn how to ask for help or information.",
        "level": 2,
        # Icon: Question Mark
        "image": "https://cdn-icons-png.flaticon.com/512/5726/5726678.png",
        "dialogues": [
            {
                "id": 301,
                "order": 1,
                "ai_prompt": "Excuse me, where is the library?",
                "target_response": "The library is down the street on the left.",
                "audio_url": get_google_tts_url("Excuse me, where is the library?")
            },
            {
                "id": 302,
                "order": 2,
                "ai_prompt": "What time does the store open?",
                "target_response": "It opens at nine in the morning.",
                "audio_url": get_google_tts_url("What time does the store open?")
            },
            {
                "id": 303,
                "order": 3,
                "ai_prompt": "How much does this cost?",
                "target_response": "That costs fifty dollars.",
                "audio_url": get_google_tts_url("How much does this cost?")
            }
        ]
    },

    # ------------------------------------------------------
    # LESSON 4: EXPRESSING OPINIONS
    # ------------------------------------------------------
    {
        "id": 4,
        "title": "Expressing Opinions",
        "description": "Share your thoughts and agree or disagree.",
        "level": 2,
        # Icon: Thought Bubble
        "image": "https://cdn-icons-png.flaticon.com/512/3050/3050525.png",
        "dialogues": [
            {
                "id": 401,
                "order": 1,
                "ai_prompt": "What do you think about this movie?",
                "target_response": "I think it is very exciting and funny.",
                "audio_url": get_google_tts_url("What do you think about this movie?")
            },
            {
                "id": 402,
                "order": 2,
                "ai_prompt": "Do you agree with this idea?",
                "target_response": "I am not sure, I need to think about it.",
                "audio_url": get_google_tts_url("Do you agree with this idea?")
            },
            {
                "id": 403,
                "order": 3,
                "ai_prompt": "Which color do you prefer, red or blue?",
                "target_response": "I prefer blue because it is calming.",
                "audio_url": get_google_tts_url("Which color do you prefer, red or blue?")
            }
        ]
    },

    # ------------------------------------------------------
    # LESSON 5: PHONE CONVERSATIONS (LOCKED)
    # ------------------------------------------------------
    {
        "id": 5,
        "title": "Phone Conversations",
        "description": "Practice talking on the phone.",
        "level": 3,
        # Icon: Lock / Phone
        "image": "https://cdn-icons-png.flaticon.com/512/724/724664.png",
        "dialogues": [
            {
                "id": 501,
                "order": 1,
                "ai_prompt": "Hello, may I speak to Sarah?",
                "target_response": "This is Sarah speaking.",
                "audio_url": get_google_tts_url("Hello, may I speak to Sarah?")
            },
            {
                "id": 502,
                "order": 2,
                "ai_prompt": "I am calling to confirm your appointment.",
                "target_response": "Thank you for letting me know.",
                "audio_url": get_google_tts_url("I am calling to confirm your appointment.")
            }
        ]
    },

    # ------------------------------------------------------
    # LESSON 6: JOB INTERVIEWS (LOCKED)
    # ------------------------------------------------------
    {
        "id": 6,
        "title": "Job Interviews",
        "description": "Answer common interview questions.",
        "level": 3,
        # Icon: Lock / Briefcase
        "image": "https://cdn-icons-png.flaticon.com/512/2910/2910791.png",
        "dialogues": [
            {
                "id": 601,
                "order": 1,
                "ai_prompt": "Tell me a little about yourself.",
                "target_response": "I am a hard worker and eager to learn.",
                "audio_url": get_google_tts_url("Tell me a little about yourself.")
            },
            {
                "id": 602,
                "order": 2,
                "ai_prompt": "Why do you want this job?",
                "target_response": "I want to grow my career with your company.",
                "audio_url": get_google_tts_url("Why do you want this job?")
            }
        ]
    }
]