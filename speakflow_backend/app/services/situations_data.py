# app/services/situations_data.py

# ==========================================
# SITUATIONS DATABASE (Scripted Roleplay)
# ==========================================

import random
AI_AVATAR = "https://img.icons8.com/color/256/robot.png"

SITUATIONS_DB = [

    # =====================================================
    # RESTAURANT
    # =====================================================
    {
        "id": "restaurant",
        "title": "At a Restaurant",
        "description": "Order food and drinks",
        "total_turns": 7,
        "image": "https://img.icons8.com/color/256/restaurant.png",
        "turns": [
            {
                "turn_id": 1,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Good evening! Welcome to our restaurant. How many people?",
                "options": [
                    {"text": "Table for two, please", "is_correct": True, "points": 10},
                    {"text": "I want food", "is_correct": False, "points": 0},
                    {"text": "Yes", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 2,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Here are your menus. Are you ready to order?",
                "options": [
                    {"text": "Yes, please", "is_correct": True, "points": 10},
                    {"text": "Menu good", "is_correct": False, "points": 0},
                    {"text": "Food now", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 3,
                "ai_avatar": AI_AVATAR,
                "ai_text": "What would you like to eat?",
                "options": [
                    {"text": "I would like pasta", "is_correct": True, "points": 20},
                    {"text": "Eat pasta", "is_correct": False, "points": 0},
                    {"text": "Food pasta", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 4,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Would you like something to drink?",
                "options": [
                    {"text": "Just water, please", "is_correct": True, "points": 10},
                    {"text": "Drink water", "is_correct": False, "points": 0},
                    {"text": "Yes drink", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 5,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Would you like dessert?",
                "options": [
                    {"text": "No, thank you", "is_correct": True, "points": 10},
                    {"text": "Cake now", "is_correct": False, "points": 0},
                    {"text": "Sweet", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 6,
                "ai_avatar": AI_AVATAR,
                "ai_text": "How would you like to pay?",
                "options": [
                    {"text": "By card, please", "is_correct": True, "points": 10},
                    {"text": "Money", "is_correct": False, "points": 0},
                    {"text": "Cash give", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 7,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Thank you! Have a nice day.",
                "options": [
                    {"text": "Thank you, goodbye!", "is_correct": True, "points": 10},
                    {"text": "Bye", "is_correct": False, "points": 0},
                    {"text": "Ok", "is_correct": False, "points": 0}
                ]
            }
        ]
    },

    # =====================================================
    # AIRPORT
    # =====================================================
    {
        "id": "airport",
        "title": "At the Airport",
        "description": "Check-in and boarding",
        "total_turns": 7,
        "image": "https://img.icons8.com/color/256/airport.png",
        "turns": [
            {
                "turn_id": 1,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Good morning. May I see your passport?",
                "options": [
                    {"text": "Here you are", "is_correct": True, "points": 10},
                    {"text": "Passport yes", "is_correct": False, "points": 0},
                    {"text": "I travel", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 2,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Where are you flying today?",
                "options": [
                    {"text": "I am flying to London", "is_correct": True, "points": 20},
                    {"text": "Go London", "is_correct": False, "points": 0},
                    {"text": "Plane there", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 3,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Do you have any luggage?",
                "options": [
                    {"text": "Yes, one suitcase", "is_correct": True, "points": 10},
                    {"text": "Bag yes", "is_correct": False, "points": 0},
                    {"text": "I carry", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 4,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Would you like a window or aisle seat?",
                "options": [
                    {"text": "Window seat, please", "is_correct": True, "points": 10},
                    {"text": "Seat window", "is_correct": False, "points": 0},
                    {"text": "Anywhere", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 5,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Here is your boarding pass.",
                "options": [
                    {"text": "Thank you very much", "is_correct": True, "points": 10},
                    {"text": "Ok", "is_correct": False, "points": 0},
                    {"text": "Give fast", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 6,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Boarding starts at Gate 22.",
                "options": [
                    {"text": "Got it, thank you", "is_correct": True, "points": 10},
                    {"text": "Gate?", "is_correct": False, "points": 0},
                    {"text": "Where go", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 7,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Have a pleasant flight!",
                "options": [
                    {"text": "Thank you!", "is_correct": True, "points": 10},
                    {"text": "Bye", "is_correct": False, "points": 0},
                    {"text": "Ok flight", "is_correct": False, "points": 0}
                ]
            }
        ]
    },

    # =====================================================
    # HOTEL
    # =====================================================
    {
        "id": "hotel",
        "title": "At a Hotel",
        "description": "Check-in and room service",
        "total_turns": 6,
        "image": "https://img.icons8.com/color/256/hotel.png",
        "turns": [
            {
                "turn_id": 1,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Welcome to our hotel. Do you have a reservation?",
                "options": [
                    {"text": "Yes, I do", "is_correct": True, "points": 10},
                    {"text": "Reservation yes", "is_correct": False, "points": 0},
                    {"text": "I stay here", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 2,
                "ai_avatar": AI_AVATAR,
                "ai_text": "May I have your name, please?",
                "options": [
                    {"text": "My name is John", "is_correct": True, "points": 10},
                    {"text": "Name John", "is_correct": False, "points": 0},
                    {"text": "Me John", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 3,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Would you like a single or double room?",
                "options": [
                    {"text": "A double room, please", "is_correct": True, "points": 20},
                    {"text": "Two bed", "is_correct": False, "points": 0},
                    {"text": "Room big", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 4,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Here is your room key.",
                "options": [
                    {"text": "Thank you", "is_correct": True, "points": 10},
                    {"text": "Key good", "is_correct": False, "points": 0},
                    {"text": "Ok", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 5,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Breakfast is served from 7 AM.",
                "options": [
                    {"text": "Great, thank you", "is_correct": True, "points": 10},
                    {"text": "Food morning", "is_correct": False, "points": 0},
                    {"text": "Yes", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 6,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Enjoy your stay!",
                "options": [
                    {"text": "Thank you very much", "is_correct": True, "points": 10},
                    {"text": "Ok", "is_correct": False, "points": 0},
                    {"text": "Bye", "is_correct": False, "points": 0}
                ]
            }
        ]
    },

    # =====================================================
    # DOCTOR
    # =====================================================
    {
        "id": "doctor",
        "title": "At the Doctor",
        "description": "Describe symptoms",
        "total_turns": 6,
        "image": "https://img.icons8.com/color/256/hospital.png",
        "turns": [
            {
                "turn_id": 1,
                "ai_avatar": AI_AVATAR,
                "ai_text": "What seems to be the problem?",
                "options": [
                    {"text": "I have a headache", "is_correct": True, "points": 20},
                    {"text": "Head pain", "is_correct": False, "points": 0},
                    {"text": "Sick", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 2,
                "ai_avatar": AI_AVATAR,
                "ai_text": "How long have you had this?",
                "options": [
                    {"text": "For two days", "is_correct": True, "points": 10},
                    {"text": "Two day", "is_correct": False, "points": 0},
                    {"text": "Long time", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 3,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Do you have a fever?",
                "options": [
                    {"text": "Yes, a mild fever", "is_correct": True, "points": 10},
                    {"text": "Fever yes", "is_correct": False, "points": 0},
                    {"text": "Hot body", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 4,
                "ai_avatar": AI_AVATAR,
                "ai_text": "I will prescribe some medicine.",
                "options": [
                    {"text": "Thank you, doctor", "is_correct": True, "points": 10},
                    {"text": "Medicine give", "is_correct": False, "points": 0},
                    {"text": "Ok", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 5,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Please take rest and drink water.",
                "options": [
                    {"text": "I will, thank you", "is_correct": True, "points": 10},
                    {"text": "Yes rest", "is_correct": False, "points": 0},
                    {"text": "Ok", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 6,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Get well soon!",
                "options": [
                    {"text": "Thank you!", "is_correct": True, "points": 10},
                    {"text": "Bye", "is_correct": False, "points": 0},
                    {"text": "Ok", "is_correct": False, "points": 0}
                ]
            }
        ]
    },

    # =====================================================
    # SHOPPING
    # =====================================================
    {
        "id": "shopping",
        "title": "Shopping at Mall",
        "description": "Ask for sizes and prices",
        "total_turns": 6,
        "image": "https://img.icons8.com/color/256/shopping-bag.png",
        "turns": [
            {
                "turn_id": 1,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Can I help you?",
                "options": [
                    {"text": "I'm looking for a shirt", "is_correct": True, "points": 20},
                    {"text": "Shirt want", "is_correct": False, "points": 0},
                    {"text": "Buy clothes", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 2,
                "ai_avatar": AI_AVATAR,
                "ai_text": "What size do you need?",
                "options": [
                    {"text": "Medium size, please", "is_correct": True, "points": 10},
                    {"text": "Size medium", "is_correct": False, "points": 0},
                    {"text": "Normal", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 3,
                "ai_avatar": AI_AVATAR,
                "ai_text": "This one costs $25.",
                "options": [
                    {"text": "That's fine", "is_correct": True, "points": 10},
                    {"text": "Too money", "is_correct": False, "points": 0},
                    {"text": "Expensive", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 4,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Would you like to try it on?",
                "options": [
                    {"text": "Yes, please", "is_correct": True, "points": 10},
                    {"text": "Try now", "is_correct": False, "points": 0},
                    {"text": "Wear it", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 5,
                "ai_avatar": AI_AVATAR,
                "ai_text": "It fits you well.",
                "options": [
                    {"text": "I'll take it", "is_correct": True, "points": 20},
                    {"text": "Good shirt", "is_correct": False, "points": 0},
                    {"text": "Nice", "is_correct": False, "points": 0}
                ]
            },
            {
                "turn_id": 6,
                "ai_avatar": AI_AVATAR,
                "ai_text": "Thank you for shopping with us!",
                "options": [
                    {"text": "Thank you!", "is_correct": True, "points": 10},
                    {"text": "Bye", "is_correct": False, "points": 0},
                    {"text": "Ok", "is_correct": False, "points": 0}
                ]
            }
        ]
    }
]


def get_all_situations():
    return [
        {
            "id": s["id"],
            "title": s["title"],
            "description": s["description"],
            "turns_count": s["total_turns"],
            "image": s["image"]
        }
        for s in SITUATIONS_DB
    ]


def get_situation_detail(situation_id: str):
    for s in SITUATIONS_DB:
        if s["id"] == situation_id:
            # Deep copy so original data is not mutated
            situation = {
                **s,
                "turns": []
            }

            for turn in s["turns"]:
                turn_copy = dict(turn)

                if "options" in turn_copy and turn_copy["options"]:
                    options_copy = turn_copy["options"][:]
                    random.shuffle(options_copy)
                    turn_copy["options"] = options_copy

                situation["turns"].append(turn_copy)

            return situation

    return None

