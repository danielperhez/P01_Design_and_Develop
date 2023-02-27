from datetime import datetime

from schemas.card import Card


class CardController:

    @staticmethod
    def create_card(card_Number: str, Account: str,register_date:datetime) -> Card:
        card = Card(card_Number=card_Number, Account=Account, register_date=register_date)
        card.save()
        return card