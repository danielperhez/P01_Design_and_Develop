from datetime import datetime
from controllers.card_controller import CardController

from schemas.card import Card


def test_create_card():
    card = CardController.create_card(card_number="41523136989065",
                                   account="12345678",
                                   register_date=datetime(2023, 11, 11, 16, 25, 3),
                                   initial_amount=10000)

    created_card = Card.select().where(Card.id == card.id).get()

    assert card.id == created_card.id
    assert card.card_number == created_card.card_number
    assert card.account == created_card.account
    assert card.register_date == created_card.register_date
    assert card.initial_amount == created_card.initial_amount

    created_card.delete_instance()