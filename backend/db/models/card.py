from datetime import datetime
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.session import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(70), nullable=False)
    bank = Column(String(70), nullable=False)
    limit = Column(Float, nullable=False)
    balance = Column(Float, default=0.0)
    due_date = Column(Date)
    cut_off_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="cards")
    transactions = relationship("Transaction", back_populates="card")
    payments = relationship("Payment", back_populates="card")
