from datetime import datetime

from schemas.transactions import Transactions


class TransactionController:

    @staticmethod
    def create_transaction(account: int, amount: float, date: datetime, description: str, transaction_key = int) -> Transactions:
        transaction = Transactions(account=account,
                    amount=amount,
                    date=date,
                    description=description,
                    transaction_key=transaction_key)
        transaction.save()
        return transaction