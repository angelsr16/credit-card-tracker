from datetime import datetime
from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db.session import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"))
    amount = Column(Float, nullable=False)
    paid_at = Column(Date, default=datetime.utcnow)

    card = relationship("Card", back_populates="payments")
