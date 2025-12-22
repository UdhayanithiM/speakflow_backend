from datetime import date, timedelta

def apply_xp_and_streak(user, xp_earned: int, db):
    today = date.today()

    # ---- STREAK LOGIC ----
    if user.last_active_date is None:
        user.current_streak = 1

    elif user.last_active_date == today:
        # Already counted today → no streak change
        pass

    elif user.last_active_date == today - timedelta(days=1):
        user.current_streak += 1

    else:
        # Missed a day
        user.current_streak = 1

    user.last_active_date = today

    # ---- XP LOGIC ----
    user.total_xp += xp_earned

    db.commit()
    db.refresh(user)

    return {
        "xp_added": xp_earned,
        "total_xp": user.total_xp,
        "current_streak": user.current_streak
    }
