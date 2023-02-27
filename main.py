from datetime import datetime

from controllers.ticket_controller import TicketController
from controllers.user_controller import UserController
from controllers.card_controller import CardController

from db import URS_ASN

from schemas.card import Card
from schemas.ticket import Retirar
from schemas.user import User



user1 = UserController.new_user(names="Jesus Israel",
                                first_name="Reyes",
                                second_name="Valdez",
                                phone_number="3323-8405-20",
                                email="reyes0valdez0@gmail.com",
                                address="Frida Kahlo",
                                extern_number=108)



user2 = UserController.new_user(names="Alan",
                                first_name="Maldonado",
                                second_name="Jimenez",
                                phone_number="3233-8432-21",
                                email="alan120@outlook.com",
                                address="Guadalajara centro",
                                extern_number=13)

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