from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.crud import (
    get_low_stock_batches,
    get_medicines_low_stock_summary,
    get_expiring_soon
)

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    return {
        "low_stock": [
            {"medicine_id": m.id, "name": m.name, "total_quantity": m.total_qty}
            for m in get_medicines_low_stock_summary(db)
        ],
        "expiring_soon": [
            {
                "batch_id": b.id,
                "batch_number": b.batch_number,
                "expiry_date": b.expiry_date,
                "quantity": b.quantity_available,
            }
            for b in get_expiring_soon(db)
        ]
    }
