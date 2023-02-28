from random import randint

from schemas.card import Card
from schemas.account import Account
from schemas.user import User


class TicketController:

    @staticmethod
    def retirar(user: User, card: Card, amount: int) -> Account:
        account = Account(user=user.id,
                        card=card.id,
                        amount=amount)
        
        account.save()
        return account
