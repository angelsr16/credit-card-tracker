from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db.session import Base


class Installment(Base):
    __tablename__ = "installments"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    number = Column(Integer)
    due_date = Column(Date)
    amount_due = Column(Float)
    amount_paid = Column(Float, default=0)
    is_paid = Column(Boolean, default=False)
    paid_at = Column(Date, default=None)

    transaction = relationship("Transaction", back_populates="installments_list")
