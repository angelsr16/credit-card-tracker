from datetime import date
from pydantic import BaseModel


class InstallmentsBase(BaseModel):
    number: int
    due_date: date
    amount_due: float
    amount_paid: float = 0
    is_paid: bool = False


class InstallmentCreate(InstallmentsBase):
    class Config:
        from_attributes = True


class InstallmentRead(InstallmentsBase):
    id: int
    transaction_id: int

    class Config:
        from_attributes = True
