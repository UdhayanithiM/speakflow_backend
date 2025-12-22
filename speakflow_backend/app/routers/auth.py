from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, utils, database

router = APIRouter(tags=["Authentication"])

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # 1. Check if email exists
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Hash the password
    hashed_pwd = utils.hash_password(user.password)
    
    # 3. Save to DB
    new_user = models.User(email=user.email, username=user.username, hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    # 1. Find user
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    
    # 2. Check password
    if not user or not utils.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=403, detail="Invalid credentials")
    
    # 3. Return Success (We will add Tokens later, keeping it simple for now)
    return {"message": "Login Successful", "user_id": user.id, "xp": user.total_xp}