from fastapi import APIRouter, HTTPException
from ..services import speed_race_data

# Prefix is set to /games/speed-race so endpoints are cleaner
router = APIRouter(prefix="/games/speed-race", tags=["Speed Race"])

@router.get("/level/{level_id}")
def get_speed_race_level(level_id: int):
    """
    Returns the list of phrases for the Speed Speak Race game.
    """
    data = speed_race_data.get_speed_race_level(level_id)
    
    if not data:
        raise HTTPException(status_code=404, detail="Level not found")
        
    return {
        "payload": data
    }