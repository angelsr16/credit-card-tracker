from typing import List, Optional
from pydantic import BaseModel
from datetime import date

from db.schemas.installment import InstallmentRead


class TransactionBase(BaseModel):
    description: str
    amount: float = 0.0
    date: date
    installments: int = 1


class TransactionCreate(TransactionBase):
    card_id: int
    monthly_charge: Optional[float] = None
    is_interest_free: bool = True

    class Config:
        from_attributes = True


class TransactionRead(TransactionBase):
    id: int
    user_id: int
    card_id: int
    installments_list: List[InstallmentRead] = []

    class Config:
        from_attributes = True
