from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date

from db.session import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))
    description = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, default=date.today)
    installments = Column(Integer, default=1)
    monthly_charge = Column(Float, nullable=False)
    is_interest_free = Column(Boolean, default=True)

    user = relationship("User", back_populates="transactions")
    card = relationship("Card", back_populates="transactions")
    installments_list = relationship(
        "Installment", back_populates="transaction", cascade="all, delete-orphan"
    )
