from typing import Annotated
from db.session import Base, engine
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from api.v1 import auth, cards, transactions, payments

from db.models import user, card, transaction, installment, payment

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(cards.router)
app.include_router(transactions.router)
app.include_router(payments.router)


@app.get("/")
async def root():

    return {"message": "Hi from the Server!"}
