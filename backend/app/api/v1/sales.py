from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, deps

router = APIRouter(prefix="/sales", tags=["sales"])

@router.post("/", response_model=schemas.Sale)
def create_sale(sale_in: schemas.SaleCreate, db: Session = Depends(deps.get_db)):
    # Check if batch exists
    batch = db.query(models.InventoryBatch).filter(models.InventoryBatch.id == sale_in.batch_id).first()
    if not batch:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Batch not found")

    sale = models.Sale(**sale_in.dict())
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale
