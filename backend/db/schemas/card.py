from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional

from db.schemas.payment import PaymentRead
from db.schemas.transaction import TransactionRead


class CardBase(BaseModel):
    name: str
    bank: str
    limit: float
    balance: Optional[float] = 0.0
    due_date: Optional[date]
    cut_off_date: Optional[date]


class CardCreate(CardBase):
    class Config:
        from_attributes = True


class CardUpdate(BaseModel):
    name: Optional[str] = None
    bank: Optional[str] = None
    limit: Optional[float] = None
    balance: Optional[float] = None
    due_date: Optional[date] = None
    cut_off_date: Optional[date] = None

    class Config:
        from_attributes = True


class CardRead(CardBase):
    id: int
    user_id: int
    created_at: datetime

    transactions: List[TransactionRead] = []
    payments: List[PaymentRead] = []

    class Config:
        from_attributes = True
