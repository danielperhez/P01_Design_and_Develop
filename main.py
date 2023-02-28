from datetime import datetime

from controllers.account_controller import AccountController
from controllers.user_controller import UserController
from controllers.card_controller import CardController
from controllers.payment_controller import PaymentsController
from controllers.transaction_controller import TransactionController

from db import URS_ASN

from schemas.card import Card
from schemas.account import Account
from schemas.user import User
from schemas.payments import Payments
from schemas.transactions import Transactions



user1 = UserController.new_user(name="Jesus Israel",
                                phone_number="3323-8405-20",
                                email="reyes0valdez0@gmail.com",
                                address="Frida Kahlo",
                                password="abcdefg")



user2 = UserController.new_user(name="Alan",
                                phone_number="3233-8432-21",
                                email="alan120@outlook.com",
                                address="Guadalajara centro",
                                password="porhdkns")

card1 = CardController.create_card(card_number="41523136989065",
                                   account="12345678",
                                   register_date=datetime(2023, 11, 11, 16, 25, 3),
                                   initial_amount=10000)

card2 = CardController.create_card(card_number="7856892145632010",
                                   account="7651234",
                                   register_date=datetime(2023, 2, 14, 2, 56, 45),
                                   initial_amount=10000)

for u in User.select():
    print(u.id, u.names, u.first_name, u.second_name, u.phone_number, u.email, u.address, u.extern_number)


for c in Card.select():
    print(c.id, c.card_number, c.account, c.register_date, c.initial_amount)

User.delete().execute()
Card.delete().execute()

