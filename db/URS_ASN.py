from peewee import SqliteDatabase


from schemas.card import Card
from schemas.Account import Account
from schemas.payments import Payments
from schemas.transactions import Transactions
from schemas.user import User




def create_db(path: str):
    db = SqliteDatabase(path)
    db.create_tables([User, Account, Card, Transactions, Payments])
