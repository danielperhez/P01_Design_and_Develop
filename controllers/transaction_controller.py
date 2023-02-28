from peewee import *
from datetime import datetime
from schemas.card import Card
from schemas.transactions import Transactions


class TransactionController:

    @staticmethod
    def create_transaction(account: int, amount: float, date: datetime, description: str,
                           transaction_key: int):

        card = Card.get(account_id=account)
        balance=card.amount
        if balance-amount<0:
            print("Not enough money")
        else:
            card.amount = balance-amount
            card.save()
            transaction = Transactions(account=account,
                                       amount=amount,
                                       date=date,
                                       description=description,
                                       transaction_key=transaction_key)
            transaction.save()
            return transaction
