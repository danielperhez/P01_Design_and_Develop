from datetime import datetime
from schemas.user import User

from schemas.Account import Account


class AccountController:

    @staticmethod
    def create_account(user: User, card: str, type: str) -> Account:
        account = Account(user_id=user.id,
                          card=card,
                          type=f"TransactionType: {type}")
        account.save()
        return account
