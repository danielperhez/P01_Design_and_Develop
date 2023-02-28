from datetime import datetime

from schemas.card import Card


class CardController:

    @staticmethod
    def create_card(account: int, card_number: str,  register_date: datetime, initial_amount: int) -> Card:
        card = Card(account_id=account,
                    card_number=card_number,
                    register_date=register_date,
                    initial_amount=f"initial amount: {initial_amount}",
                    amount=initial_amount)
        card.save()
        return card
    
