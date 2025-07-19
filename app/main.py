# app/main.py
from fastapi import FastAPI
from app.routers import auth  # relative import from app/routers/auth.py
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
