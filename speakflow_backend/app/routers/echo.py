# app/routers/echo.py

from fastapi import APIRouter, HTTPException
from ..services import echo_game_data 

# CHANGE THIS LINE: Add "/games" to the prefix
router = APIRouter(prefix="/games/echo", tags=["Echo"]) 

@router.get("/level/{level_id}")
def get_echo_level(level_id: int):
    level_data = echo_game_data.get_echo_level(level_id)
    
    if not level_data:
        raise HTTPException(status_code=404, detail="Level not found")

    return {"payload": level_data}