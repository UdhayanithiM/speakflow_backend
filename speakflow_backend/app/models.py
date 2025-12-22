# app/models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    DateTime,
    Date
)
from sqlalchemy.sql import func
from datetime import datetime
from .database import Base


# --------------------------------------------------
# USER TABLE (STREAK + XP READY)
# --------------------------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # ---------------- Gamification ----------------
    total_xp = Column(Integer, default=0, nullable=False)

    # 🔥 Day-based streak (critical for SpeakFlow)
    current_streak = Column(Integer, default=0, nullable=False)
    last_active_date = Column(Date, nullable=True)

    # ---------------- Tracking ----------------
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    last_login = Column(
        DateTime(timezone=True),
        nullable=True
    )


# --------------------------------------------------
# GAME SESSION TABLE (SERVER-DRIVEN GAMES)
# --------------------------------------------------
class GameSession(Base):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, index=True, nullable=False)

    # Game identity
    game_type = Column(String, nullable=False)     # vocab / adjectives
    category = Column(String, nullable=False)      # animals / cold-hot

    # Progress tracking
    current_part = Column(Integer, default=0)      # 0=preview, 1,2,3
    current_index = Column(Integer, default=0)

    # Scoring
    score = Column(Integer, default=0, nullable=False)
    total_questions = Column(Integer, nullable=False)

    # Locked server data
    questions = Column(JSON, nullable=False)

    # ⚠️ MUST use lambda to avoid shared state
    answers = Column(JSON, default=lambda: [])

    # Lifecycle
    status = Column(String, default="active")      # active / completed

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
