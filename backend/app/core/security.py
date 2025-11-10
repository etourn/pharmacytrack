# backend/app/core/security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = {"sub": str(subject)}
    expire = datetime.utcnow() + (expires_delta if expires_delta else ACCESS_TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
