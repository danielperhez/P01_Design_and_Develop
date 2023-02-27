from peewee import *

from schemas.user import User
from schemas.card import Card

db = SqliteDatabase('prueba_union.db')


class Ticket(Model):
    user = ForeignKeyField(User, backref='tickets')
    card = ForeignKeyField(Card, backref='tickets')
    proxy = CharField()
    status = BooleanField()  # True is active

    class Meta:
        database = db  # This model uses the "movies.db" database.