from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from .. import database, models

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/{user_id}")
def get_dashboard(user_id: int, db: Session = Depends(database.get_db)):
    # 1. Fetch User
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 2. LEVEL CALCULATION
    current_level = (user.total_xp // 1000) + 1
    xp_for_next_level = 1000
    current_level_xp = user.total_xp % xp_for_next_level
    level_progress = current_level_xp / xp_for_next_level

    # 3. TODAY COMPLETION FLAG
    today_completed = user.last_active_date == date.today()

    # 4. MODULE DEFINITIONS
    modules = [
        {
            "id": "vocab",
            "title": "Vocabulary",
            "subtitle": "Learn new words",
            "icon": "book",
            "locked": False
        },
        {
            "id": "speaking",
            "title": "Speaking",
            "subtitle": "Practice pronunciation",
            "icon": "mic",
            "locked": False
        },
        {
            "id": "grammar",
            "title": "Grammar",
            "subtitle": "Master the rules",
            "icon": "edit",
            "locked": False  # ✅ CHANGED FROM (current_level < 3) TO False
        },
        {
            "id": "situations",
            "title": "Situations",
            "subtitle": "Real-life scenarios",
            "icon": "chat",
            "locked": False # Keep this locked until we build it
        }
    ]

    return {
        "user_name": user.username,
        "day_streak": user.current_streak, # Ensure key name matches Android (day_streak vs current_streak)
        "total_xp": user.total_xp,
        "current_level": current_level,
        "level_progress": level_progress,
        "today_completed": today_completed,
        "modules": modules
    }