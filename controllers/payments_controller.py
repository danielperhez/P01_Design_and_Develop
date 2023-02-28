from datetime import datetime

from schemas.card import Card
from schemas.payments import Payments


class PaymentsController:

    @staticmethod
    def create_payments(account: float, amount: int, date: datetime, payment_id: int) -> Payments:
        payment = Payments(account=account,
                           amount=amount,
                           date=date,
                           payment_id=payment_id)
        payment.save()
        card = Card.get(account_id=account)
        card.amount += amount
        card.save()
        return payment
