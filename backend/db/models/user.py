from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from db.session import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

    cards = relationship("Card", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")
