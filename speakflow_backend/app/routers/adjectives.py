from fastapi import APIRouter
from ..services import adjective_service

router = APIRouter(prefix="/adjectives", tags=["Adjectives"])

@router.get("/pairs")
def pairs():
    return {
        "game_type": "adjectives",
        "part": 0,
        "total_parts": 3,
        "payload": {
            "pairs": adjective_service.list_pairs()
        }
    }


@router.get("/image-text/{word}")
def image_text(word: str):
    return {
        "game_type": "adjectives",
        "part": 1,
        "total_parts": 3,
        "payload": adjective_service.image_to_text(word)
    }


@router.get("/sentence/{word}")
def sentence(word: str):
    return {
        "game_type": "adjectives",
        "part": 3,
        "total_parts": 3,
        "payload": adjective_service.sentence_game(word)
    }
