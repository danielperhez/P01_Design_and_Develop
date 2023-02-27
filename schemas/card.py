import peewee
from peewee import *

db = SqliteDatabase('prueba_union.db')


class Card(Model):
    card_Number = CharField()
    register_date = DateTimeField()
    Account = CharField()

    class Meta:
        database = db  # This model uses the "movies.db" database.