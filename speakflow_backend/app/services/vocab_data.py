VOCAB_DATABASE = {

    "animals": {
        1: ["Cat", "Dog", "Bird", "Fish", "Cow", "Pig", "Ant", "Bat", "Bee", "Fox"],
    },

    "food": {
        1: ["Apple", "Banana", "Egg", "Milk", "Bread", "Cake", "Rice"],
    },

    "colors": {
        1: ["Red", "Blue", "Green", "Yellow", "Black", "White"],
    },

    # ✅ NEW: CLOTHING
    "clothing": {
        1: ["Shirt", "Pants", "Dress", "Jacket", "Shoes", "Hat"],
    }
}

def get_words_for_level(category: str, level: int):
    return VOCAB_DATABASE.get(category.lower(), {}).get(level, [])
