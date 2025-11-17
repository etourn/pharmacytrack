# backend/app/api/v1/auth.py
from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas import Token, UserCreate, UserOut
from app.core.security import hash_password, verify_password, create_access_token
from app.deps import get_db
from app import models
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = models.User(
        name=user_in.name,
        email=user_in.email,
        password_hash=hash_password(user_in.password),
        role="cashier"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     # OAuth2PasswordRequestForm gives fields 'username' and 'password'
#     user = db.query(models.User).filter(models.User.email == form_data.username).first()
#     if not user or not verify_password(form_data.password, user.password_hash):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
#     token = create_access_token(subject=str(user.id))
#     return {"access_token": token, "token_type": "bearer"}

class LoginInput(BaseModel):
    email: EmailStr
    password: str

# @router.post("/login", response_model=Token)
# def login(data: LoginInput, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == data.email).first()
#     if not user or not verify_password(data.password, user.password_hash):
#         raise HTTPException(status_code=401, detail="Incorrect credentials")

#     token = create_access_token(subject=str(user.id))
    # return {"access_token": token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(data: LoginInput, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")

    token = create_access_token(subject=str(user.id))
    return {"access_token": token, "token_type": "bearer"}


