from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="cashier")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brand = Column(String)
    description = Column(String)
    unit = Column(String)
    min_stock_level = Column(Integer, default=10)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class InventoryBatch(Base):
    __tablename__ = "inventory_batches"

    id = Column(Integer, primary_key=True, index=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=False)
    batch_number = Column(String)
    quantity_available = Column(Integer, nullable=False)
    expiry_date = Column(DateTime)
    purchase_price = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    medicine = relationship("Medicine", backref="batches")
