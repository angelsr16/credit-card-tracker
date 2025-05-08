from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from api.dependencies.auth import verify_token
from api.dependencies.db import get_db
from db.models.user import User as UserModel
from db.schemas.card import CardCreate, CardRead, CardUpdate
from db.crud import card as crud_card, user as crud_user
from db.schemas.transaction import TransactionRead

router = APIRouter(prefix="/cards")


@router.get("/{card_id}")
async def get_card(
    card_id: str,
    db: Session = Depends(get_db),
    current_username: str = Depends(verify_token),
):
    user: UserModel = crud_user.get_user_by_username(db, current_username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    card = crud_card.get_card_by_id(db, card_id)

    return CardRead.model_validate(card)


@router.post("/", response_model=CardRead)
async def create_card(
    card: CardCreate,
    db: Session = Depends(get_db),
    current_username: str = Depends(verify_token),
):
    user: UserModel = crud_user.get_user_by_username(db, current_username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    new_card = crud_card.create_card(db=db, card=card, user_id=user.id)

    return new_card


@router.put("/{card_id}")
async def update_card(
    card_id: str,
    card_data: CardUpdate,
    db: Session = Depends(get_db),
    current_username: str = Depends(verify_token),
):
    user: UserModel = crud_user.get_user_by_username(db, current_username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    existing_card = crud_card.get_card_by_id(db, card_id)

    if not existing_card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Card not found"
        )

    if existing_card.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not the card owner"
        )

    updated_card = crud_card.update_card(db, card_id, card_data)
    if updated_card is None:
        raise HTTPException(status_code=500, detail="Failed to update card")

    return updated_card


@router.delete("/{card_ud}")
async def delete_card(
    card_id: str, db: Session = Depends(get_db), current_username=Depends(verify_token)
):
    user = crud_user.get_user_by_username(db, current_username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    existing_card = crud_card.get_card_by_id(db, card_id)

    if not existing_card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Card not found"
        )

    if existing_card.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not card owner"
        )

    deleted_card = crud_card.delete_card(db, card_id)
    if not deleted_card:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete card",
        )

    return {"msg": "Card deleted successfully"}
