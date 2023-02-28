from datetime import datetime

from schemas.account import Account


class AccountController:

    @staticmethod
    def create_account(user: int, card: str, type: str) -> Account:
        account = Account(user=user.id,
                    card=card,
                    type=f"TransactionType: {type}")
        account.save()
        return account