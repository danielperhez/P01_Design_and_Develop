from peewee import SqliteDatabase

from schemas.card import Card
from schemas.account import Account
from schemas.user import User
from schemas.payments import Payments
from schemas.transactions import Transactions

db_card = SqliteDatabase('card.db')
db_card.create_tables([User,Card,Account,Payments,Transactions])
