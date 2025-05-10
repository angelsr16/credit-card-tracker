from typing import Annotated
from db.session import Base, engine
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from api.v1 import auth, cards, transactions, payments
from fastapi.middleware.cors import CORSMiddleware

from db.models import user, card, transaction, installment, payment

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(cards.router)
app.include_router(transactions.router)
app.include_router(payments.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # or ["*"] for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():

    return {"message": "Hi from the Server!"}
