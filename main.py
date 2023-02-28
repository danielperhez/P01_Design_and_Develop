from datetime import datetime

from controllers.user_controller import UserController
from controllers.card_controller import CardController
from controllers.Account_controller import AccountController
from controllers.payments_controller import PaymentsController
from controllers.transaction_controller import TransactionController

from db.URS_ASN import create_db

from schemas.transactions import Transactions
from schemas.payments import Payments
from schemas.card import Card
from schemas.user import User
from schemas.Account import Account

create_db('card.db')

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

account1 = AccountController.create_account(user=user1, card="41523136989065", type="spei")

account2 = AccountController.create_account(user=user2, card="7856892145632010", type="spei")

card1 = CardController.create_card(account=account1.id,
                                   card_number="41523136989065",
                                   register_date=datetime(2023, 11, 11, 16, 25, 3),
                                   initial_amount=10000)

card2 = CardController.create_card(account=account2.id,
                                   card_number="7856892145632010",
                                   register_date=datetime(2023, 2, 14, 2, 56, 45),
                                   initial_amount=10000)


transaction1 = TransactionController.create_transaction(account=account1.id,amount= 100,date= datetime.now(),description= "transaction 1",transaction_key= 12345678)

transaction2 = TransactionController.create_transaction(account=account2.id, amount=500, date= datetime.now(), description="transaction 2",transaction_key= 12387658)

#try more than balance
transaction3 = TransactionController.create_transaction(account=account1.id,amount= 10000,date= datetime.now(),description= "transaction 3",transaction_key= 12345678)


payment1 = PaymentsController.create_payments(account1.id, 1000, datetime.now(), 65432)
payment2 = PaymentsController.create_payments(account2.id, 1000, datetime.now(), 75432)


for u in User.select():
    print(u.id, u.names, u.first_name, u.second_name, u.phone_number, u.email, u.address, u.extern_number)

for a in Account.select():
    print(a.id, a.user_id, a.card, a.type)

for c in Card.select():
    print(c.id, c.account_id, c.card_number, c.register_date, c.amount)

for t in Transactions.select():
    print(t.id,t.account, t.amount, t.date, t.description, t.transaction_key)

for p in Payments.select():
    print(p.id, p.amount, p.date, p.payment_id)

Payments.delete().execute()
Transactions.delete().execute()
User.delete().execute()
Account.delete().execute()
Card.delete().execute()
