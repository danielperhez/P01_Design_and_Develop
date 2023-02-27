from peewee import *

db = SqliteDatabase('card.db')


class Card(Model):
    card_number = CharField()
    account = CharField()
    register_date = DateTimeField()
    initial_amount = IntegerField()

    class Meta:
        database = db  # This model uses the "movies.db" database.
