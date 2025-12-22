from fastapi import FastAPI
from .database import engine
from . import models

# Routers
from .routers import auth, dashboard, vocab, adjectives,session

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

# Health check
@app.get("/")
def read_root():
    return {
        "status": "active",
        "message": "SpeakFlow Backend is running successfully 🚀"
    }
