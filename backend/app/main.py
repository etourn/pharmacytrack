# backend/app/main.py
from fastapi import FastAPI
from .api.v1 import auth, medicines  # ensure package import path works
from app.api.v1 import auth, medicines, batches, sales
from app.api.v1 import dashboard

app = FastAPI(title="PharmacyTrack API")

app.include_router(auth.router)
app.include_router(medicines.router)
app.include_router(batches.router)
app.include_router(sales.router)
app.include_router(dashboard.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to PharmacyTrack API"}
