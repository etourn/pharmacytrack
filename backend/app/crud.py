from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

from app.models import InventoryBatch, Medicine

LOW_STOCK_THRESHOLD = 10
EXPIRING_DAYS = 30

def get_low_stock_batches(db: Session, limit=LOW_STOCK_THRESHOLD):
    return (
        db.query(InventoryBatch)
        .filter(InventoryBatch.quantity_available < limit)
        .order_by(InventoryBatch.quantity_available.asc())
        .all()
    )


def get_medicines_low_stock_summary(db: Session):
    return (
        db.query(
            Medicine.id,
            Medicine.name,
            func.sum(InventoryBatch.quantity_available).label("total_qty")
        )
        .join(InventoryBatch, Medicine.id == InventoryBatch.medicine_id)
        .group_by(Medicine.id)
        .having(func.sum(InventoryBatch.quantity_available) < LOW_STOCK_THRESHOLD)
        .all()
    )


def get_expiring_soon(db: Session):
    cutoff = datetime.utcnow() + timedelta(days=EXPIRING_DAYS)
    return (
        db.query(InventoryBatch)
        .filter(InventoryBatch.expiry_date <= cutoff)
        .order_by(InventoryBatch.expiry_date.asc())
        .all()
    )
