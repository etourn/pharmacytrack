# backend/app/core/config.py
import os
from datetime import timedelta

SECRET_KEY = os.getenv("SECRET_KEY", "change-me-to-a-random-secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "120"))

ACCESS_TOKEN_EXPIRE = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
