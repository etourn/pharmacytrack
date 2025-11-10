# backend/app/main.py
from fastapi import FastAPI
from .api.v1 import auth, medicines  # ensure package import path works

app = FastAPI(title="PharmacyTrack API")

app.include_router(auth.router)
app.include_router(medicines.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to PharmacyTrack API"}
