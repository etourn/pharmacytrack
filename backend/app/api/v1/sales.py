from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, deps
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter(prefix="/sales", tags=["sales"])

@router.post("/", response_model=schemas.Sale)
def create_sale(sale_in: schemas.SaleCreate, db: Session = Depends(deps.get_db)):
    try:
        # start transation
        with db.begin():
            # Check if batch exists
            batch = db.query(models.InventoryBatch).filter(models.InventoryBatch.id == sale_in.batch_id).first()
            if not batch:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Batch not found")
            # deduct quantity
            batch.quantity -= sale_in.quantity_sold

            # record sale 
            sale = models.Sale(**sale_in.dict())
            db.add(sale)
        return sale

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
