from sqlalchemy.orm import Session

from db.models.card import Card as CardModel
from db.schemas.card import CardCreate, CardUpdate


def get_cards_by_user(db: Session, user_id):
    return db.query(CardModel).filter(CardModel.user_id == user_id).all()


def get_card_by_id(db: Session, card_id: str):
    return db.query(CardModel).filter(CardModel.id == card_id).first()


def create_card(db: Session, card: CardCreate, user_id: str):
    db_card = CardModel(
        user_id=user_id,
        name=card.name,
        bank=card.bank,
        limit=card.limit,
        balance=card.balance,
        due_date=card.due_date,
        cut_off_date=card.cut_off_date,
    )

    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def update_card(db: Session, card_id: str, card_data: CardUpdate):
    card = get_card_by_id(db, card_id)
    if not card:
        return None

    for field, value in card_data.model_dump(exclude_unset=True).items():
        setattr(card, field, value)

    db.commit()
    db.refresh(card)
    return card


def delete_card(db: Session, card_id: str):
    card = get_card_by_id(db, card_id)
    if not card:
        return None
    db.delete(card)
    db.commit()
    return card
