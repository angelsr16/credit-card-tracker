from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from db.schemas.card import CardRead


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime
    cards: List[CardRead] = []  # Link to the user's cards

    class Config:
        from_attributes = True
