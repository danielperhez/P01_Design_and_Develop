from peewee import *

from schemas.ticket import Retirar

db = SqliteDatabase('card.db')


class Transactions(Model):
    account = ForeignKeyField(Retirar, backref='tickets')
    amount = IntegerField()
    date = IntegerField()
    description = CharField()
    transaction_key = IntegerField()

    class Meta:
        database = db