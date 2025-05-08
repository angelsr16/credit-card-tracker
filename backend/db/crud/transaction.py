from datetime import date
from sqlalchemy.orm import Session

from db.crud.card import get_card_by_id
from db.models.card import Card
from db.models.installment import Installment as InstallmentModel
from db.models.transaction import Transaction as TransactionModel
from db.schemas.transaction import TransactionCreate

from dateutil.relativedelta import relativedelta


def create_transaction(db: Session, transaction: TransactionCreate, user_id: str):
    card = (
        db.query(Card)
        .filter(Card.id == transaction.card_id, Card.user_id == user_id)
        .first()
    )

    if not card:
        return None

    monthly_charge = round(transaction.amount / transaction.installments, 2)
    if not transaction.is_interest_free and transaction.monthly_charge != None:
        monthly_charge = transaction.monthly_charge

    new_transaction = TransactionModel(
        user_id=user_id,
        card_id=transaction.card_id,
        description=transaction.description,
        amount=transaction.amount,
        date=transaction.date,
        installments=transaction.installments,
        monthly_charge=monthly_charge,
        is_interest_free=transaction.is_interest_free,
    )

    card.balance += transaction.amount

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    for i in range(transaction.installments):
        due_date = calculate_installment_due_dates(
            transaction.date, card.cut_off_date.day, card.due_date.day, i
        )

        new_installment = InstallmentModel(
            transaction_id=new_transaction.id,
            amount_due=monthly_charge,
            due_date=due_date,
            number=i + 1,
        )

        db.add(new_installment)
    db.commit()
    return new_transaction


def calculate_installment_due_dates(
    transaction_date: date, cut_off_day: int, due_day: int, installment_number: int
) -> date:

    # First billing cycle due date
    if transaction_date.day <= cut_off_day:
        first_due = date(transaction_date.year, transaction_date.month, due_day)
        if first_due <= transaction_date:
            first_due = first_due + relativedelta(months=1)
    else:
        first_due = date(
            transaction_date.year, transaction_date.month, due_day
        ) + relativedelta(months=1)

    return first_due + relativedelta(months=installment_number)
