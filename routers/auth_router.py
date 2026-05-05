from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime, timedelta

from database.db import get_db
from models import users_model
from schemas import user_schema
from core.config import settings
from utils.hash import verify_password, hash_password

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/registration/", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    hashed_val = hash_password(user.user_password)
    db_user = db.query(users_model.User).filter(
        users_model.User.user_email == user.user_email
        ).first()

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    
    new_user = users_model.User(
        user_name=user.user_name, 
        user_email=user.user_email, 
        user_password=hashed_val
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    
@router.post("/login")
def login(user_credentials: user_schema.UserLogin, db: Session = Depends(get_db)):
    user = db.query(users_model.User).filter(
        users_model.User.user_email == user_credentials.user_email
    ).first()

    if not user or not verify_password(user_credentials.user_password, user.user_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
            )

    expire = datetime.utcnow() + timedelta(days=settings.access_token_expire_days)
    payload = {
        "user_id": user.user_id,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm
    )

    return {"access_token": token, "token_type": "bearer"}