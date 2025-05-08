from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from api.dependencies.auth import verify_token
from api.dependencies.db import get_db
from db.models import user as UserModel
from db.schemas.transaction import TransactionCreate
from db.crud import (
    card as crud_card,
    user as crud_user,
    transaction as crud_transaction,
)

router = APIRouter(prefix="/transactions")


@router.post("/")
async def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_username: str = Depends(verify_token),
):
    user: UserModel = crud_user.get_user_by_username(db, current_username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    card = crud_card.get_card_by_id(db, transaction.card_id)

    if not card or card.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not card owner"
        )

    new_transaction = crud_transaction.create_transaction(db, transaction, user.id)
    if new_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to register transaction",
        )
    return new_transaction
