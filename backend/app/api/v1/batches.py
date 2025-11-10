from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models
from app import schemas, deps  # Adjust import paths if needed

router = APIRouter(prefix="/batches", tags=["batches"])

@router.post("/", response_model=schemas.InventoryBatch)
def create_batch(
    batch_in: schemas.InventoryBatchCreate,
    db: Session = Depends(deps.get_db),
):
    # Check if medicine exists
    medicine = db.query(models.Medicine).filter(models.Medicine.id == batch_in.medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medicine not found")

    batch = models.InventoryBatch(**batch_in.dict())
    db.add(batch)
    db.commit()
    db.refresh(batch)
    return batch

@router.get("/", response_model=List[schemas.InventoryBatch])
def list_batches(db: Session = Depends(deps.get_db)):
    batches = db.query(models.InventoryBatch).all()
    return batches
