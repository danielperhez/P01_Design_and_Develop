from peewee import *

db = SqliteDatabase('card.db')


class Payments(Model):
    payer = CharField()
    payee = CharField()
    amount = DateTimeField()
    date = IntegerField()
    payment_method = CharField()
    transaction_key = IntegerField()

    class Meta:
        database = db