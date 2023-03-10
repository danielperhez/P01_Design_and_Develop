from peewee import *

from schemas.Account import Account

db = SqliteDatabase('card.db')


class Transactions(Model):
    account = ForeignKeyField(Account, backref="transactions")
    amount = FloatField()
    date = DateField()
    description = CharField()
    transaction_key = IntegerField()
    class Meta:
        database = db  # This model uses the "card.db" database.
