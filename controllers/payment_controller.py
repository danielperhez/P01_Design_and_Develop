from datetime import datetime

from schemas.account import Account
from schemas.payments import Payments


class PaymentsController:

    @staticmethod
    def create_payments(account: int, amount: float, date: datetime, payment_id: int) -> Payments:
        payment = Payments(account=account,
                           amount=amount,
                           date=date,
                           payment_id=payment_id)
        payment.save()
        acc = Account.select().where(Account.id == account).get()
        acc.balance += amount
        acc.save()
        return payment