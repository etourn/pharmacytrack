# backend/app/api/v1/medicines.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas import MedicineCreate, MedicineOut
from app.deps import get_db, get_current_user
from app import models

router = APIRouter(prefix="/api/v1/medicines", tags=["medicines"])

@router.get("", response_model=List[MedicineOut])
def list_medicines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    meds = db.query(models.Medicine).offset(skip).limit(limit).all()
    return meds

@router.post("", response_model=MedicineOut, status_code=status.HTTP_201_CREATED)
def create_medicine(payload: MedicineCreate, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    # Optional: check role
    if user.role != "admin":
        # allow non-admin to create? change logic as you want
        raise HTTPException(status_code=403, detail="Admins only")
    med = models.Medicine(
        name=payload.name,
        brand=payload.brand,
        description=payload.description,
        unit=payload.unit,
        min_stock_level=payload.min_stock_level or 0
    )
    db.add(med)
    db.commit()
    db.refresh(med)
    return med
