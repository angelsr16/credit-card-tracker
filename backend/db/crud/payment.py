from sqlalchemy.orm import Session

from db.models.card import Card
from db.models.installment import Installment
from db.models.payment import Payment
from db.schemas.payment import PaymentCreate


def create_payment(db: Session, payment_data: PaymentCreate):
    card = db.query(Card).filter(Card.id == payment_data.card_id).first()

    if not card:
        return None

    remaining_amount = payment_data.amount

    unpaid_installments = (
        db.query(Installment)
        .join(Installment.transaction)
        .filter(
            Installment.is_paid == False, Installment.transaction.has(card_id=card.id)
        )
        .order_by(Installment.due_date.asc())
        .all()
    )

    if not unpaid_installments:
        return None  # No payment required

    payment = Payment(
        card_id=card.id, amount=payment_data.amount, paid_at=payment_data.paid_at
    )

    db.add(payment)

    for installment in unpaid_installments:
        if remaining_amount <= 0:
            break

        to_pay = min(installment.amount_due - installment.amount_paid, remaining_amount)

        installment.amount_paid += to_pay
        remaining_amount -= to_pay

        if installment.amount_paid >= installment.amount_due:
            installment.is_paid = True
            installment.paid_at = payment_data.paid_at

    paid_amount = payment_data.amount - remaining_amount
    card.balance -= paid_amount

    if card.balance < 0:
        card.balance = 0  # prevent negative balance

    db.commit()
    db.refresh(payment)
    return payment
