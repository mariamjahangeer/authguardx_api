from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app import models, database
from app.schemas import user as user_schema

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(database.SessionLocal)):
    new_user = models.user.User(
        email=user.email,
        password=user.password  # (we'll hash later)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
