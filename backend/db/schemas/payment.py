from datetime import date
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    card_id: int
    amount: float
    paid_at: Optional[date]


class PaymentCreate(PaymentBase):
    pass


class PaymentRead(PaymentBase):
    class Config:
        from_attributes = True
