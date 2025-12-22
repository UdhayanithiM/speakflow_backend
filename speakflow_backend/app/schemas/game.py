from pydantic import BaseModel
from typing import List, Optional

# ---------- COMMON ----------

class ImageItem(BaseModel):
    id: str
    image: str
    label: Optional[str] = None
    audio: Optional[str] = None


class GameResponse(BaseModel):
    game_type: str
    category: str
    part: int
    total_parts: int
    payload: dict


# ---------- VOCAB ----------

class VocabPreviewItem(BaseModel):
    word: str
    image: str
    audio: str


class VocabListenClickQuestion(BaseModel):
    question_id: str
    target_word: str
    target_audio: str
    options: List[ImageItem]


# ---------- ADJECTIVES ----------

class AdjectivePair(BaseModel):
    pair_id: str
    left: str
    right: str


class AdjectiveImageQuestion(BaseModel):
    question_id: str
    image: str
    correct_word: str
    options: List[str]


class SentencePuzzle(BaseModel):
    image: str
    correct_sentence: str
    words: List[str]
