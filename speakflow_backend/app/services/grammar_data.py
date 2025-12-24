# ==========================================
# GRAMMAR SENTENCE BUILDER DATA
# ==========================================

GRAMMAR_LEVELS = [
    {
        "level": 1,
        "title": "Basic Sentences",
        "description": "Arrange words to form simple sentences.",
        "questions": [

            {
                "id": "q1",
                "image": "https://img.icons8.com/color/256/winter.png",
                "correct_sentence": "The weather is cold today",
                "jumbled_words": ["The", "weather", "is", "cold", "today", "hot", "very", "nice"]
            },

            {
                "id": "q2",
                "image": "https://media.istockphoto.com/id/1079800720/photo/sleeping-red-cat-on-white-background.jpg?s=612x612&w=0&k=20&c=oPBpugXs02jy4hlu7CSvQO-DdFsMkBsEtnHA5Vi4Nt4=",
                "correct_sentence": "The cat is sleeping",
                "jumbled_words": ["The", "cat", "is", "sleeping", "dog", "running", "fast"]
            },

            {
                "id": "q3",
                "image": "https://img.icons8.com/color/256/apple.png",
                "correct_sentence": "I like to eat apples",
                "jumbled_words": ["I", "like", "to", "eat", "apples", "drink", "red", "juice"]
            },

            {
                "id": "q4",
                "image": "https://img.icons8.com/color/256/bus.png",
                "correct_sentence": "The bus is yellow",
                "jumbled_words": ["The", "bus", "is", "yellow", "car", "blue", "big"]
            },

            {
                "id": "q5",
                "image": "https://img.icons8.com/color/256/running.png",
                "correct_sentence": "He runs very fast",
                "jumbled_words": ["He", "runs", "very", "fast", "she", "slow", "walks"]
            },

            {
                "id": "q6",
                "image": "https://img.icons8.com/color/256/reading.png",
                "correct_sentence": "She is reading a book",
                "jumbled_words": ["She", "is", "reading", "a", "book", "writing", "pen"]
            },

            {
                "id": "q7",
                "image": "https://img.icons8.com/color/256/sun.png",
                "correct_sentence": "The sun is very bright",
                "jumbled_words": ["The", "sun", "is", "very", "bright", "moon", "dark"]
            },

            {
                "id": "q8",
                "image": "https://www.shutterstock.com/image-vector/kids-playing-football-vector-260nw-588962903.jpg",
                "correct_sentence": "They are playing football",
                "jumbled_words": ["They", "are", "playing", "football", "watching", "cricket"]
            },

            {
                "id": "q9",
                "image": "https://img.icons8.com/color/256/water-bottle.png",
                "correct_sentence": "I drink water every day",
                "jumbled_words": ["I", "drink", "water", "every", "day", "milk", "night"]
            },

            {
                "id": "q10",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHaIRPzslWkr3JOuZjh9rTqgzDR3FQIpwDjA&s ",
                "correct_sentence": "The baby is smiling",
                "jumbled_words": ["The", "baby", "is", "smiling", "crying", "loud"]
            },

            {
                "id": "q11",
                "image": "https://media.baamboozle.com/uploads/images/510442/1637229778_122346.jpeg",
                "correct_sentence": "We go to school daily",
                "jumbled_words": ["We", "go", "to", "school", "daily", "office", "late"]
            },

            {
                "id": "q12",
                "image": "https://img.icons8.com/color/256/dog.png",
                "correct_sentence": "The dog is barking loudly",
                "jumbled_words": ["The", "dog", "is", "barking", "loudly", "quiet", "sleeping"]
            },

            {
                "id": "q13",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1ybUuCfwiMkO3L1H-67uDGkm624_nZfp7kg&s",
                "correct_sentence": "She likes ice cream",
                "jumbled_words": ["She", "likes", "ice", "cream", "hate", "spicy"]
            },

            {
                "id": "q14",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdjQK0ik17Hahpk4hGYJ_L7bhxg2c7SHO6JA&s",
                "correct_sentence": "The boy is happy",
                "jumbled_words": ["The", "boy", "is", "happy", "sad", "angry"]
            },

            {
                "id": "q15",
                "image": "https://t4.ftcdn.net/jpg/05/13/74/25/360_F_513742569_LLeI88QTirsf7erCeVnbUDgL5GaiVooD.jpg",
                "correct_sentence": "Birds are flying high",
                "jumbled_words": ["Birds", "are", "flying", "high", "fish", "swimming"]
            }

        ]
    }
]


def get_grammar_level(level_id: int):
    for level in GRAMMAR_LEVELS:
        if level["level"] == level_id:
            return level
    return None
