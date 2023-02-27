from datetime import datetime

from schemas.card import Card


class CardController:

    @staticmethod
    def create_card(card_number: str, account: str, register_date: datetime, initial_amount: int) -> Card:
        card = Card(card_number=card_number,
                    account=account,
                    register_date=register_date,
                    initial_amount=initial_amount)
        card.save()
        return card
