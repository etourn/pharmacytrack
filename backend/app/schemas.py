# backend/app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from decimal import Decimal
from datetime import date, datetime

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: Optional[str] = None

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: Optional[str]

    class Config:
        from_attributes = True

class MedicineCreate(BaseModel):
    name: str
    brand: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[str] = None
    min_stock_level: Optional[int] = 0

class MedicineOut(BaseModel):
    id: int
    name: str
    brand: Optional[str]
    description: Optional[str]
    unit: Optional[str]
    min_stock_level: Optional[int]

    class Config:
        orm_mode = True

class InventoryBatchBase(BaseModel):
    medicine_id: int
    quantity: int
    expiry_date: date | None = None

class InventoryBatchCreate(InventoryBatchBase):
    pass

class InventoryBatch(InventoryBatchBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    batch_id: int
    quantity_sold: int

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
