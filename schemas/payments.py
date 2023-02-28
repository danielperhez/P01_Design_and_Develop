from peewee import *

from schemas.Account import Account

db = SqliteDatabase('card.db')


class Payments(Model):
    account = ForeignKeyField(Account, backref="payments")
    amount = FloatField()
    date = DateField()
    payment_id = IntegerField()

    class Meta:
        database = db  # This model uses the "card.db" database.

