# app/routers/gamification.py
from fastapi import APIRouter, HTTPException
from ..services import gamification_data,echo_game_data

router = APIRouter(prefix="/games", tags=["Gamification"])

@router.get("/voice-match/level/{level_id}")
def get_voice_match_level(level_id: int):
    data = gamification_data.get_voice_match_level(level_id)
    
    if not data:
        raise HTTPException(status_code=404, detail="Level not found")
        
    return {
        "payload": data
    }
