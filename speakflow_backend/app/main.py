from fastapi import FastAPI
from .database import engine
from . import models
from fastapi.staticfiles import StaticFiles

# Routers
# ✅ Added 'speaking' to imports
from .routers import auth, dashboard, vocab, adjectives, session, speaking,grammar,situations,gamification,echo,speed_race

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# App instance
app = FastAPI(title="SpeakFlow API")

# Register routers
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(vocab.router)
app.include_router(adjectives.router)
app.include_router(session.router)
app.include_router(speaking.router) # ✅ Added this line
app.include_router(grammar.router)
app.include_router(situations.router)
app.include_router(gamification.router)
app.include_router(echo.router)
app.include_router(speed_race.router)

# Mount static folder for images/audio
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Health check
@app.get("/")
def read_root():
    return {
        "status": "active",
        "message": "SpeakFlow Backend is running successfully 🚀"
    }