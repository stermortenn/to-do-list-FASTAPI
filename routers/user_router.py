from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import users_model
from schemas import user_schema

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[user_schema.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(users_model.User).all()

@router.get("/{user_id}", response_model=user_schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(users_model.User).filter(users_model.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    return user