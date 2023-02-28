from peewee import *

from schemas.account import Account

db = SqliteDatabase('card.db')


class Transactions(Model):
    account = ForeignKeyField(Account,backref="transactions")
    amount = float()
    date = DateField()
    description = CharField()
    transaction_key = int()
    
    class Meta:
        database = db  # This model uses the "card.db" database.