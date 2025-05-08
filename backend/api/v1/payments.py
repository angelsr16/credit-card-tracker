from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from api.dependencies.auth import verify_token
from api.dependencies.db import get_db
from db.schemas.payment import PaymentCreate
from db.crud import user as crud_user, card as crud_card, payment as crud_payment

router = APIRouter(prefix="/payments")


@router.post("/")
async def create_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db),
    current_username: str = Depends(verify_token),
):
    user = crud_user.get_user_by_username(db, current_username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    card = crud_card.get_card_by_id(db, payment.card_id)
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Card not found"
        )

    if card.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not card owner"
        )

    new_payment = crud_payment.create_payment(db, payment_data=payment)

    if new_payment is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to register payment",
        )
    return new_payment
