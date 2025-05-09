from datetime import date
from sqlalchemy.orm import Session

from db.models.card import Card
from db.models.installment import Installment
from db.schemas.card import CardRead


def get_cards_summary(db: Session, user_id: int):
    today = date.today()
    cards = db.query(Card).filter(Card.user_id == user_id).all()

    card_summaries = []
    total_balance = 0

    for card in cards:
        cut_off = card.cut_off_date
        due_date = card.due_date

        installments = (
            db.query(Installment)
            .join(Installment.transaction)
            .filter(
                Installment.is_paid == False,
                Installment.transaction.has(card_id=card.id),
                Installment.due_date <= due_date,
            )
            .all()
        )

        payment_to_avoid_interest = sum(
            i.amount_due - i.amount_paid for i in installments
        )
        total_balance += card.balance

        card_summaries.append(
            {
                **CardRead.model_validate(card).model_dump(),
                "payment_to_avoid_interest": payment_to_avoid_interest,
            }
        )

    return card_summaries
