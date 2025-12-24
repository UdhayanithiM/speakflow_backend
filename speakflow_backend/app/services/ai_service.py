# =====================================================
# IMAGE SERVICE — CURATED, FAST, CORRECT
# =====================================================

STATIC_IMAGES = {

    # ---------- ANIMALS ----------
    "cat": "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg",
    "dog": "https://images.pexels.com/photos/1805164/pexels-photo-1805164.jpeg",
    "bird": "https://images.pexels.com/photos/1661179/pexels-photo-1661179.jpeg",
    "fish": "https://images.pexels.com/photos/128756/pexels-photo-128756.jpeg",
    "cow": "https://images.pexels.com/photos/422218/pexels-photo-422218.jpeg",
    "pig": "https://images.pexels.com/photos/110820/pexels-photo-110820.jpeg",

    # ✅ FIXED BEE (CLEAR, SINGLE BEE)
    "bee": "https://images.pexels.com/photos/460961/pexels-photo-460961.jpeg",

    # ✅ FIXED BAT (CARTOON-LIKE, CLEAR)
    "bat": "https://images.pexels.com/photos/2587639/pexels-photo-2587639.jpeg",

    "ant": "https://images.pexels.com/photos/1104974/pexels-photo-1104974.jpeg",
    "fox": "https://images.pexels.com/photos/134058/pexels-photo-134058.jpeg",

    # ---------- FOOD ----------
    "apple": "https://images.pexels.com/photos/102104/pexels-photo-102104.jpeg",
    "banana": "https://images.pexels.com/photos/2872755/pexels-photo-2872755.jpeg",
    "egg": "https://images.pexels.com/photos/162712/egg-white-food-protein-162712.jpeg",
    "milk": "https://images.pexels.com/photos/5946720/pexels-photo-5946720.jpeg",
    "bread": "https://images.pexels.com/photos/1775043/pexels-photo-1775043.jpeg",
    "cake": "https://images.pexels.com/photos/1702373/pexels-photo-1702373.jpeg",
    "rice": "https://images.pexels.com/photos/4110256/pexels-photo-4110256.jpeg",

    # ---------- COLORS (PNG — NOT SVG) ----------
    "red": "https://dummyimage.com/400x400/ff0000/ffffff.png&text=Red",
    "blue": "https://dummyimage.com/400x400/0000ff/ffffff.png&text=Blue",
    "green": "https://dummyimage.com/400x400/00ff00/ffffff.png&text=Green",
    "yellow": "https://dummyimage.com/400x400/ffff00/000000.png&text=Yellow",
    "black": "https://dummyimage.com/400x400/000000/ffffff.png&text=Black",
    "white": "https://dummyimage.com/400x400/ffffff/000000.png&text=White",

    # ---------- CLOTHING ----------
    "shirt": "https://www.crewclothing.co.uk/images/products/medium/MRB022_LAGOON.jpg",
    "pants": "https://images.pexels.com/photos/2343661/pexels-photo-2343661.jpeg",
    "dress": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg",
    "jacket": "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
    "shoes": "https://images.pexels.com/photos/19090/pexels-photo.jpg",
    "hat": "https://tse4.mm.bing.net/th/id/OIP.q7kmb5R6m_oM5fZroqY9ywHaE7?cb=ucfimg2&pid=Api&ucfimg=1",
}

def get_ai_image_url(word: str) -> str:
    clean = word.lower().strip()
    return STATIC_IMAGES.get(clean, f"https://loremflickr.com/400/400/{clean}")

def get_ai_audio_url(word: str) -> str:
    return ""
