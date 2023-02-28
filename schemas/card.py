from peewee import *

from schemas.Account import Account

db = SqliteDatabase('card.db')


class Card(Model):
    account_id = ForeignKeyField(Account, backref="cards")
    card_number = CharField()
    register_date = DateTimeField()
    initial_amount = IntegerField()
    amount = FloatField()

    class Meta:
        database = db  # This model uses the "movies.db" database.
