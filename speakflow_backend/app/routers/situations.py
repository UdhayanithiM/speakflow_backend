from fastapi import APIRouter, HTTPException
from ..services import situations_data

router = APIRouter(prefix="/situations", tags=["Situations"])

@router.get("/all")
def get_all_situations():
    """
    Returns the list of scenarios (Restaurant, Airport, etc.) 
    for the selection screen.
    """
    return {
        "payload": situations_data.get_all_situations()
    }

@router.get("/{situation_id}")
def get_situation_details(situation_id: str):
    """
    Returns the full script (turns, questions, answers) for the game.
    """
    data = situations_data.get_situation_detail(situation_id)
    if not data:
        raise HTTPException(status_code=404, detail="Situation not found")
    
    return {
        "payload": data
    }